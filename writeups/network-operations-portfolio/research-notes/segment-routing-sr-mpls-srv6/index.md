---
layout: page-toc
title: "Segment Routing (SR-MPLS / SRv6)"
permalink: /writeups/network-operations-portfolio/research-notes/segment-routing-sr-mpls-srv6/
toc: true
---
# Segment Routing (SR-MPLS / SRv6) — Hướng đi Mới của Lớp Truyền tải Core

> **Đối tượng:** IP/Core Network Engineer muốn hiểu kiến trúc mạng lõi hiện đại — tại sao MPLS truyền thống với LDP/RSVP-TE đang bị thay thế, và Segment Routing giải quyết bài toán đó như thế nào.
>
> **Mức độ:** Intermediate–Advanced — giả định bạn đã hiểu MPLS label switching, IGP (OSPF/IS-IS), và khái niệm traffic engineering cơ bản.

---

## Mục lục

1. [Bối cảnh: Vấn đề của MPLS truyền thống](#1-bối-cảnh-vấn-đề-của-mpls-truyền-thống)
2. [Nguyên lý cốt lõi: Source Routing và Segment](#2-nguyên-lý-cốt-lõi-source-routing-và-segment)
3. [Segment ID (SID) — các loại và ý nghĩa](#3-segment-id-sid--các-loại-và-ý-nghĩa)
4. [SR-MPLS — triển khai trên data plane MPLS](#4-sr-mpls--triển-khai-trên-data-plane-mpls)
5. [SRv6 — triển khai trên data plane IPv6](#5-srv6--triển-khai-trên-data-plane-ipv6)
6. [Control Plane: IGP Extensions cho SR](#6-control-plane-igd-extensions-cho-sr)
7. [SR Traffic Engineering (SR-TE) và SR Policy](#7-sr-traffic-engineering-sr-te-và-sr-policy)
8. [TI-LFA — Fast Reroute thế hệ mới](#8-ti-lfa--fast-reroute-thế-hệ-mới)
9. [So sánh: LDP/RSVP-TE vs Segment Routing](#9-so-sánh-ldprsvp-te-vs-segment-routing)
10. [Phân tích số liệu: Scale 1,000 Node](#10-phân-tích-số-liệu-scale-1000-node)
11. [SRv6 Network Programming](#11-srv6-network-programming)
12. [Tích hợp SDN: PCEP, BGP-LS, và SR Controller](#12-tích-hợp-sdn-pcep-bgp-ls-và-sr-controller)
13. [Liên hệ Automation, Telemetry, và AI](#13-liên-hệ-automation-telemetry-và-ai)
14. [Lộ trình triển khai thực tế](#14-lộ-trình-triển-khai-thực-tế)
15. [Lab mini: Cấu hình SR-MPLS cơ bản](#15-lab-mini-cấu-hình-sr-mpls-cơ-bản)
16. [Glossary](#16-glossary)
17. [Tài liệu tham khảo](#17-tài-liệu-tham-khảo)

---

## 1. Bối cảnh: Vấn đề của MPLS Truyền thống

### Kiến trúc MPLS cổ điển

Mạng Core của ISP/nhà mạng truyền thống dùng MPLS để chuyển tiếp gói tin tốc độ cao. MPLS hoạt động tốt, nhưng đi kèm với một hệ sinh thái giao thức phức tạp:

```
MPLS Traditional Control Plane:

┌────────────────────────────────────────────────────────────────────┐
│                    Protocol Stack (per router)                     │
├────────────────────────────────────────────────────────────────────┤
│  IS-IS / OSPF        → IGP, tính toán shortest path               │
│  LDP                 → Label Distribution Protocol, phân phối nhãn│
│  RSVP-TE             → Traffic Engineering, tạo TE tunnel          │
│  BGP                 → Phân phối route, VPN signaling              │
│  PCEP (optional)     → Path Computation Element Protocol          │
└────────────────────────────────────────────────────────────────────┘

Vấn đề: đây là 4-5 giao thức cần vận hành đồng thời trên mọi node lõi.
```

### LDP — đơn giản nhưng thiếu linh hoạt

**LDP (Label Distribution Protocol)** phân phối nhãn MPLS tự động dựa trên IGP routing table. Mỗi prefix được gán một nhãn, router hàng xóm trao đổi nhãn với nhau.

```
LDP label distribution (ví dụ):

Router A ──────── Router B ──────── Router C
                                  (prefix 10.0.0.0/24)

B quảng bá: "Label 200 → forward đến C"
A quảng bá: "Label 100 → forward đến B (sẽ swap thành 200)"

Gói vào A đến 10.0.0.0/24:
  Push label 100 → B nhận → swap 200 → C nhận → pop → IP forward

Nhược điểm LDP:
  ✗ Theo shortest path hoàn toàn, không traffic engineering
  ✗ Không load-balance tốt với nhiều equal-cost paths
  ✗ Phải chạy song song LDP session với từng neighbor → state O(N)
  ✗ LDP convergence chậm hơn IGP → có khoảng trống traffic black-hole
```

### RSVP-TE — mạnh nhưng nặng state

**RSVP-TE (Resource Reservation Protocol - Traffic Engineering)** cho phép tạo TE tunnel theo đường chỉ định, có thể tránh congestion, enforce bandwidth.

**Vấn đề state bùng nổ:**

```
RSVP-TE State Problem:

Giả sử 100 edge node, full-mesh TE tunnel:
  Số tunnel = 100 × 99 = 9,900 tunnel (một chiều)
  Mỗi tunnel đi qua trung bình 6 hop
  → 9,900 × 6 = 59,400 mục trạng thái RSVP trên toàn mạng

Per-node impact:
  Một core router transit qua 500 tunnel
  → Router đó giữ 500 RSVP PATH/RESV state
  → Mỗi state phải refresh mỗi 30 giây (soft-state mechanism)
  → 500 × 2 (PATH + RESV) / 30s ≈ 33 RSVP messages/giây liên tục
  → Chỉ riêng RSVP keepalive đã tốn CPU đáng kể

Khi N tăng lên (1,000 edge node):
  9,000 × 999 / 2 ≈ ~450,000 tunnel
  → State bùng nổ theo bình phương: O(N²)
  → Không thể scale được
```

**Vấn đề vận hành:**
- Khi thêm router mới vào Core: cần update RSVP session với tất cả neighbor
- Debug RSVP: phải trace PATH/RESV message qua từng hop
- Failure recovery: phức tạp, cần re-signal toàn bộ tunnel bị ảnh hưởng
- RSVP graceful restart: cần implement trên mọi node để tránh traffic loss khi restart

---

## 2. Nguyên lý Cốt lõi: Source Routing và Segment

### Ý tưởng nền tảng

**Source routing** không phải khái niệm mới — xuất hiện từ thời IP (IP Strict Source Route, IPv4 Option 9). Ý tưởng: node nguồn quyết định toàn bộ đường đi, nhúng thông tin này vào header gói tin. Node trung gian chỉ đọc và thực thi, không cần "nhớ" gì về flow đó.

Segment Routing hiện đại hóa ý tưởng này, chuẩn hóa trong **RFC 8402 (2018)**:

```
Nguyên lý SR:

Truyền thống (RSVP-TE):
  Ingress ──► Mọi node trên đường đi cần biết về tunnel ──► Egress
              [State tại EVERY hop]

Segment Routing:
  Ingress ──► [SID1, SID2, SID3] ──► Trung gian chỉ đọc SID đầu ──► Egress
  (nhúng đường đi vào gói)            [Stateless forwarding]
```

### Segment là gì?

**Segment** là một chỉ thị (instruction) mô tả một hành động cụ thể trong mạng:
- "Đưa gói đến node X theo đường ngắn nhất"
- "Đẩy gói qua link L cụ thể này"
- "Áp dụng service function Y"

**Segment List (hay SID Stack):** danh sách ordered của các segment, xác định toàn bộ hành vi chuyển tiếp từ ingress đến egress.

```
Segment List execution (SR-MPLS):

Gói vào ingress A với segment list: [SID_B, Adj_BF, Adj_FD, SID_E]
                                      └─────────────────────────────┘
                                           Stack (top = SID_B)

Tại A:   Active segment = SID_B → forward toward B (IGP shortest path)
Tại B:   Pop SID_B, active = Adj_BF → forward qua link B→F (adjacency)
Tại F:   Pop Adj_BF, active = Adj_FD → forward qua link F→D (adjacency)
Tại D:   Pop Adj_FD, active = SID_E → forward toward E (IGP shortest path)
Tại E:   Pop SID_E → gói đến đích, IP forwarding bình thường

Điểm mấu chốt: B, F, D không giữ state về "đường hầm" này.
Chúng chỉ làm việc với segment trên cùng của stack → stateless!
```

---

## 3. Segment ID (SID) — Các loại và Ý nghĩa

### 3.1 Prefix-SID (Node SID)

**Prefix-SID** định danh một node (thường là loopback /32) trong toàn mạng. Có phạm vi **global** — mọi node trong SR domain đều hiểu ý nghĩa của SID này.

```
Prefix-SID properties:
  - Phạm vi: Global (domain-wide)
  - Gán: trong SRGB (SR Global Block), ví dụ 16000-23999
  - Quảng bá: qua IGP (IS-IS hoặc OSPF extension)
  - Ý nghĩa: "Forward đến prefix này theo IGP shortest path"

Ví dụ topology:
  Node A: Prefix-SID = 16001 (loopback 192.0.2.1/32)
  Node B: Prefix-SID = 16002 (loopback 192.0.2.2/32)
  Node C: Prefix-SID = 16003 (loopback 192.0.2.3/32)
  Node D: Prefix-SID = 16004 (loopback 192.0.2.4/32)
  Node E: Prefix-SID = 16005 (loopback 192.0.2.5/32)

Gói tại A đến E, chỉ dùng Prefix-SID:
  Stack: [16005]
  → A forward về phía E theo IGP shortest path
  → Mọi node trên đường chỉ cần biết SRGB base + SID index
  → Label thực tế = SRGB_base + SID_index = 16000 + 5 = 16005
```

**SRGB (SR Global Block):** dải nhãn MPLS được reserve cho Prefix-SID. Mỗi vendor có default khác nhau nhưng có thể cấu hình. Quan trọng: SRGB phải **đồng nhất** trên toàn domain để đảm bảo tính global của Prefix-SID.

```
SRGB ví dụ:
  Cisco IOS-XR default: 16000–23999 (8,000 SID)
  Juniper default: 16000–32767
  Nokia default: 32768–65535 (có thể customize)

Nếu SRGB khác nhau giữa các vendor:
  Node A (Cisco, SRGB 16000+): SID 16005 = Node E
  Node X (Juniper, SRGB 32768+): SID 32773 = Node E?
  
  → Cần align SRGB giữa các vendor trước khi deploy multi-vendor SR domain
```

### 3.2 Adjacency-SID

**Adjacency-SID** định danh một **link** cụ thể ra khỏi một node. Có phạm vi **local** — chỉ có ý nghĩa tại node đó.

```
Adjacency-SID properties:
  - Phạm vi: Local (chỉ valid tại node assign)
  - Gán: dynamic (tự động từ dynamic label range), hoặc static
  - Quảng bá: qua IGP, được tag là "local"
  - Ý nghĩa: "Đẩy gói ra đúng interface/link này"

Ví dụ:
  Node B có các Adjacency-SID:
    B→A: Adj-SID 24001 (dynamic)
    B→C: Adj-SID 24002 (dynamic)
    B→F: Adj-SID 24003 (dynamic)  ← Link đặc biệt, tránh congestion

  Ingress A muốn ép traffic qua đường A→B→F→D→E:
    Stack: [SID_B(16002), AdjSID(24003), AdjSID_FD, SID_E(16005)]
    
    Tại A: forward đến B theo IGP (SID_B = 16002)
    Tại B: pop 16002, active = 24003 → đẩy ra link B→F (bất kể IGP nói gì)
    Tại F: pop 24003, active = AdjSID_FD → đẩy ra link F→D
    Tại D: pop AdjSID_FD, active = 16005 → forward đến E theo IGP
    Tại E: pop 16005 → IP forward đến destination
```

### 3.3 Anycast-SID

**Anycast-SID** cùng một SID được assign cho nhiều node trong một nhóm. Gói được forward đến node gần nhất (theo IGP metric) trong nhóm.

```
Use case: Load balancing, redundancy cho service node

                  ┌── Node C1 (SID 16100) ──┐
A → [SID 16100] ──┤                         ├── (anycast group)
                  └── Node C2 (SID 16100) ──┘

A forward về SID 16100 → IGP chọn C1 hoặc C2 tùy đường ngắn nhất
Nếu C1 fail → traffic tự động sang C2, không cần reconfigure
```

### 3.4 Service SID (SRv6 specific)

Trong SRv6, SID còn có thể encode **network function** (sẽ giải thích chi tiết ở phần SRv6 Network Programming):
- `End` — node endpoint, tương đương Prefix-SID
- `End.X` — adjacency endpoint, tương đương Adj-SID
- `End.DT4/DT6` — decapsulation + routing table lookup (cho VPN)
- `End.B6.Encaps` — binding SID với SRH mới (SR Policy)

---

## 4. SR-MPLS — Triển khai trên Data Plane MPLS

### Tại sao SR-MPLS là con đường chuyển đổi phổ biến nhất

SR-MPLS không thay đổi data plane — vẫn dùng MPLS label switching như cũ. Những gì thay đổi chỉ là **control plane**: bỏ LDP/RSVP-TE, dùng IGP extension để phân phối SID.

```
Upgrade path:
  Before SR: IGP + LDP + RSVP-TE (3 protocols)
  After SR:  IGP (với SR extension) only

Data plane hardware:   không thay đổi → tận dụng router cũ
MPLS forwarding:       vẫn hoạt động như cũ (label lookup, swap, push, pop)
ASICs/Linecards:       không cần upgrade
```

### Label stack và forwarding mechanics

```
SR-MPLS packet (ví dụ 3-segment stack):

 ┌─────────────────────────────────────────────────────┐
 │ Outer Ethernet Header                               │
 ├─────────────────────────────────────────────────────┤
 │ MPLS Label 1: 16005 [S=0, TTL=63]  ← Top of stack  │
 │ MPLS Label 2: 24003 [S=0, TTL=63]  ← Middle        │
 │ MPLS Label 3: 16008 [S=1, TTL=63]  ← Bottom (S=1)  │
 ├─────────────────────────────────────────────────────┤
 │ IP Header (inner payload)                           │
 └─────────────────────────────────────────────────────┘

MPLS label field (32 bits):
 ┌──────────────────────┬──────┬───┬─────────┐
 │   Label (20 bits)    │  Exp │ S │   TTL   │
 │   (forwarding key)   │(3bit)│(1)│ (8 bits)│
 └──────────────────────┴──────┴───┴─────────┘
 S=1: Bottom of Stack (last label)
 Exp: Traffic Class / QoS marking

Forwarding actions:
  PUSH:   thêm label vào top of stack (ingress)
  SWAP:   thay label hiện tại bằng label mới (transit)
  POP:    xóa label khỏi top of stack (egress hoặc penultimate hop)
```

### PHP — Penultimate Hop Popping

**PHP** là cơ chế tối ưu: node kề cuối (penultimate hop) pop label cuối cùng, để egress node chỉ cần IP lookup thay vì MPLS lookup.

```
Với SR-MPLS:
  Node A (ingress) push SID_E(16005)
  ...
  Node D (penultimate) → nhận label 16005, biết đây là last-hop toward E
  → Pop label 16005 (PHP) → gửi IP packet đến E
  Node E (egress) → nhận IP packet, forward đến destination

Thay thế PHP: Explicit Null
  Nếu muốn E nhận MPLS packet (cho QoS preservation):
  Node D SWAP 16005 → Explicit Null (label 0 cho IPv4, 2 cho IPv6)
  Node E pop Explicit Null → IP forward (nhưng đọc được EXP/TC bits)
```

---

## 5. SRv6 — Triển khai trên Data Plane IPv6

### Kiến trúc SRv6

SRv6 thay thế hoàn toàn MPLS label stack bằng **IPv6 Segment Routing Header (SRH)** — một extension header của IPv6. Mỗi segment là một địa chỉ IPv6 128-bit đầy đủ.

```
SRv6 Packet Structure:

┌──────────────────────────────────────────────────────────┐
│ IPv6 Header (40 bytes)                                   │
│   Source:      2001:db8:a::1   (ingress node)            │
│   Destination: 2001:db8:b::1   (CURRENT active segment)  │
│   Next Header: 43 (Routing Header)                       │
├──────────────────────────────────────────────────────────┤
│ SRH (Segment Routing Header):                            │
│   Next Header: 59 (no next header) or 4 (IPv4) or 41    │
│   Hdr Ext Len: 4 (= 6 segments × 2 words... variable)   │
│   Routing Type: 4 (SRH)                                 │
│   Segments Left: 2   ← bao nhiêu segment còn lại        │
│   Last Entry: 2      ← index của segment cuối           │
│   Flags: 0                                               │
│   Tag: 0                                                 │
│   Segment List[2]: 2001:db8:c::1   ← SID 3 (first hop)  │
│   Segment List[1]: 2001:db8:d::1   ← SID 2              │
│   Segment List[0]: 2001:db8:e::1   ← SID 1 (last/egress)│
├──────────────────────────────────────────────────────────┤
│ Payload (IPv4/IPv6/Ethernet...)                          │
└──────────────────────────────────────────────────────────┘

Lưu ý: Segment List đảo ngược (SID đầu tiên đến = index cao nhất)
IPv6 Destination = SID đang active (node hiện tại)
```

### SRv6 forwarding tại mỗi node

```
SRv6 processing tại SR node:

Nhận packet với:
  IPv6 Dst = 2001:db8:b::1  (SID của node B = mình)
  SRH Segments Left = 2
  SRH Segment List[2] = 2001:db8:c::1
  SRH Segment List[1] = 2001:db8:d::1
  SRH Segment List[0] = 2001:db8:e::1

Node B xử lý:
  1. IPv6 Dst match local SID 2001:db8:b::1 → SR node processing
  2. Segments Left > 0 → decrement Segments Left (2 → 1)
  3. New active segment = Segment List[Segments Left] = Segment List[1] = 2001:db8:d::1
  4. Update IPv6 Dst = 2001:db8:d::1
  5. Forward packet theo IPv6 Dst mới → đến node D

→ Không pop/push như MPLS, chỉ update Dst và decrement counter
→ Packet size không thay đổi qua transit nodes
```

### SRv6 SID Structure: Locator + Function + Argument

SRv6 SID không chỉ là địa chỉ định tuyến — nó còn encode **hàm** cần thực thi:

```
SRv6 SID format (128 bits):

┌────────────────┬──────────────┬──────────────────────────────┐
│  Locator       │   Function   │       Arguments              │
│  (N bits)      │   (F bits)   │       (A bits)               │
│  e.g., 48 bits │  e.g., 16b  │       remaining              │
└────────────────┴──────────────┴──────────────────────────────┘

Ví dụ: 2001:db8:1::/48 là locator của Node 1
  2001:db8:1::1    → Function 1 = End (node SID, route to this node)
  2001:db8:1::2    → Function 2 = End.X (adjacency to specific neighbor)
  2001:db8:1::d004 → Function d004 = End.DT4 (VRF routing table 4)

Locator được quảng bá qua IGP như một prefix IPv6 thông thường
→ Toàn mạng biết cách route đến locator → route đến SID
```

### SR-MPLS vs SRv6: So sánh thực tế

| Tiêu chí | SR-MPLS | SRv6 |
|---|---|---|
| Data plane | MPLS | IPv6 |
| SID size | 20-bit label | 128-bit IPv6 address |
| Header overhead | 4 bytes/SID | 16 bytes/SID + 8 byte SRH fixed |
| Phần cứng cũ | Tương thích cao | Cần phần cứng hỗ trợ SRH |
| Deployment today | Phổ biến, production | Mới nổi, tăng nhanh |
| Network programming | Hạn chế | Mạnh (End functions) |
| IPv6-native | Không | Có |
| 5G transport | Có thể | Tốt hơn |
| Multi-domain TE | Khó | Dễ hơn (IP routable SID) |
| Interop MPLS network | Tự nhiên | Cần encap/decap |

---

## 6. Control Plane: IGP Extensions cho SR

### SR không cần giao thức phân phối nhãn mới

Đây là điểm khác biệt cơ bản nhất: SR phân phối SID thông qua **IGP hiện có** (IS-IS hoặc OSPF) bằng cách thêm TLV/sub-TLV mới. Không cần LDP, không cần RSVP.

### IS-IS Extensions (RFC 8667)

```
IS-IS SR TLVs mới:

1. SR Capabilities Sub-TLV (trong Router Capability TLV 242):
   → Quảng bá SRGB range của node
   → "Tôi hỗ trợ SR, SRGB của tôi là 16000-23999"

2. Prefix-SID Sub-TLV (trong Extended IP Reachability TLV 135):
   → Attach SID index vào một prefix (thường là loopback)
   → "Loopback 192.0.2.5/32 có SID index 5"
   → Các node khác tính label = local_SRGB_base + 5 = 16005

3. Adjacency-SID Sub-TLV (trong Extended IS Reachability TLV 22):
   → Quảng bá local Adj-SID cho từng link
   → "Link tôi đến neighbor X có local label 24003"

4. LAN Adjacency-SID Sub-TLV (cho môi trường broadcast):
   → Tương tự nhưng cho Ethernet segment, một Adj-SID cho mỗi neighbor

IS-IS SR LSP ví dụ (Node B):
  Router Capability:
    SR Algorithm: 0 (Shortest Path, SPF)
    SRGB: base=16000, range=8000
  Extended IP Reachability:
    Prefix: 192.0.2.2/32
    Prefix-SID: index=2, flags: Node-SID, PHP
  Extended IS Reachability (to C):
    Neighbor: Node-C
    Metric: 10
    Adj-SID: 24002 (local to B, protected)
    Adj-SID: 24012 (local to B, unprotected backup)
```

### OSPF Extensions (RFC 8665)

Tương tự IS-IS nhưng dùng OSPF Opaque LSA (Type 10):

```
OSPF SR Sub-TLVs:

Router Information Opaque LSA (Type 10, TLV 3):
  → SR-Algorithm TLV: quảng bá algorithm hỗ trợ (SPF, Flex-Algo)
  → SID/Label Range TLV: quảng bá SRGB

Extended Prefix Opaque LSA (Type 10, TLV 2):
  → Extended Prefix SID Sub-TLV: prefix → SID index mapping

Extended Link Opaque LSA (Type 10, TLV 1):
  → Adj-SID Sub-TLV: link → local Adj-SID mapping
  → LAN Adj-SID Sub-TLV: broadcast segment
```

### Flexible Algorithm (Flex-Algo)

**Flex-Algo** (RFC 9350) mở rộng SR để hỗ trợ nhiều topology/metric song song:

```
Flex-Algo concept:

Algorithm 0 (default): IGP metric (shortest path by hop count/admin metric)
Algorithm 128: delay-based topology (chọn đường có latency thấp nhất)
Algorithm 129: TE bandwidth (tránh link tắc nghẽn)
Algorithm 130: disjoint path (đường vật lý khác với algo 0)

Mỗi node tính SPF riêng cho từng algorithm
Prefix-SID được gán per-algorithm: SID_E algo0 ≠ SID_E algo128

Use case 5G:
  eMBB slice: algo 0 (bandwidth optimized)
  URLLC slice: algo 128 (latency < 1ms)
  mMTC slice: algo 0 (cost optimized)
```

---

## 7. SR Traffic Engineering (SR-TE) và SR Policy

### SR Policy là gì?

**SR Policy** là abstraction của một "đường đi" trong SR domain, bao gồm:
- **Headend:** node ingress apply policy
- **Color:** tag để match traffic (ví dụ: color 100 = low-latency service)
- **Endpoint:** node egress cuối cùng
- **Candidate Paths:** một hoặc nhiều đường (segment list) có priority

```
SR Policy structure:

SR Policy: (headend=A, color=100, endpoint=E)
  Candidate Path 1 (preference=200, active):
    Segment List: [SID_C(16003), SID_E(16005)]
    → Đường qua C → E
    
  Candidate Path 2 (preference=100, standby):
    Segment List: [SID_D(16004), SID_E(16005)]
    → Đường backup qua D → E
    
  Candidate Path 3 (preference=50, standby):
    Segment List: [SID_E(16005)]
    → Shortest path (fallback)
```

### Traffic Steering vào SR Policy

Làm thế nào traffic được đưa vào đúng SR Policy?

```
Phương pháp 1: BGP Color Community
  BGP route đến prefix X được tag color 100
  SR Policy với color=100 match → apply segment list
  
  Ví dụ:
    BGP route: 10.1.0.0/16, next-hop E, community 100:100 (color)
    Policy: headend=A, color=100, endpoint=E, SL=[SID_C, SID_E]
    → Traffic đến 10.1.0.0/16 từ A → push [SID_C, SID_E]

Phương pháp 2: Binding SID (BSID)
  SR Policy được assign một Binding-SID (local label)
  BSID = "proxy" cho toàn bộ segment list
  
  Policy headend=A: color=200, BSID=99001, SL=[SID_C, Adj_CE, SID_E]
  
  Upstream node cần gửi traffic vào policy này:
  → Push chỉ [BSID=99001] → A nhận, swap thành [SID_C, Adj_CE, SID_E]
  → Ẩn đi độ phức tạp của segment list
  → Đặc biệt quan trọng cho inter-domain SR-TE

Phương pháp 3: Policy-based routing / Service function chaining
  ACL hoặc classifier match traffic → redirect vào SR Policy
```

### Controller-driven SR-TE (vs Distributed)

```
Hai mô hình SR-TE:

1. Distributed (node tự tính):
   Mỗi node chạy CSPF (Constrained Shortest Path First)
   Dùng TE database (từ IGP-TE extension)
   Phù hợp: mạng đơn giản, không cần global optimization
   
2. Controller-driven (PCEP / BGP-LS):
   Controller thu thập toàn bộ topology qua BGP-LS
   Controller tính đường tối ưu toàn cục (global view)
   Controller cài segment list xuống headend qua PCEP hoặc gNMI/NETCONF
   
   Phù hợp: mạng lớn, multi-domain, cần optimization phức tạp
             (minimize congestion, multi-constraint path)
```

---

## 8. TI-LFA — Fast Reroute Thế hệ Mới

### Vấn đề của LFA cổ điển

**LFA (Loop-Free Alternates)** — RFC 5286 — là cơ chế pre-computed backup path trong IGP. Khi link/node fail, chuyển traffic sang LFA không cần re-convergence.

**Giới hạn:** LFA chỉ tìm được backup trong một số topology đặc biệt. Nhiều trường hợp không có LFA — coverage thường chỉ ~70-80% trong mạng thực tế.

### TI-LFA: Topology Independent

**TI-LFA (Topology Independent LFA)** — RFC 9350 — dùng SR để mã hóa đường backup, đảm bảo **100% coverage** cho bất kỳ topology nào (link protection và node protection).

```
TI-LFA concept:

Topology:
  A ── B ── C ── D ── E
       │              │
       └──── F ───────┘

Protected link: B → C

Nếu không có TI-LFA:
  Từ B, backup đến C → không có loop-free alternate (phụ thuộc topology)

Với TI-LFA:
  B tính: "Nếu link B→C fail, làm sao đến C?"
  B tìm Post-Convergence Path (PCP): B → F → E → D → C
  B encode path này thành SR segment list: [Adj_BF, SID_E, Adj_ED, SID_C]
  
  Khi link B→C fail:
    → Hardware detect failure (< 1ms, BFD)
    → B immediately forward traffic với segment list backup
    → Không cần đợi IGP reconverge (vài giây)
    → Total protection time: < 50ms (typically < 10ms)

Coverage: 100% (bất kỳ link/node failure nào cũng có pre-computed backup)
```

### Node Protection vs Link Protection

```
Link Protection:
  Bảo vệ khi link A→B fail
  Backup path: tránh link đó, có thể vẫn qua node B
  
Node Protection:
  Bảo vệ khi node B hoàn toàn fail (crash, power loss)
  Backup path: tránh hoàn toàn node B
  Khó hơn → TI-LFA handle được

TI-LFA P-Space và Q-Space:
  P-space: set of nodes reachable from S (source) without traversing the protected segment
  Q-space: set of nodes from which D is reachable without traversing the protected segment
  
  Backup path: S → [P node] → [Q node] → D
  Encoding: [Adj-SID to reach P] + [SID của Q nếu P≠Q] + [SID của D]
  
  Nếu P và Q overlap → "PQ node" → backup đơn giản hơn
```

---

## 9. So sánh: LDP/RSVP-TE vs Segment Routing

### Bảng so sánh toàn diện

| Tiêu chí | LDP | RSVP-TE | SR-MPLS | SRv6 |
|---|---|---|---|---|
| **RFC** | RFC 5036 (2007) | RFC 3209 (2001) | RFC 8660 (2019) | RFC 8754 (2020) |
| **Data plane** | MPLS | MPLS | MPLS | IPv6 |
| **Control plane** | LDP protocol | RSVP protocol | IGP extension | IGP extension |
| **Số protocol cần** | IGP + LDP | IGP + RSVP-TE | IGP only | IGP only |
| **State tại core** | Per-prefix (FIB) | Per-tunnel (LFIB) | Stateless | Stateless |
| **Traffic Engineering** | Không | Có (complex) | Có (đơn giản) | Có (đơn giản) |
| **Scale** | O(N) prefixes | O(N²) tunnels | O(N) SID | O(N) SID |
| **Fast Reroute** | LFA (~70-80%) | RSVP FRR (complex) | TI-LFA (100%) | TI-LFA (100%) |
| **ECMP** | Hạn chế | Kém với tunnel | Xuất sắc | Xuất sắc |
| **SDN integration** | Khó | Khó | PCEP, gNMI, NETCONF | PCEP, gNMI |
| **Flexibility** | Thấp | Trung bình | Cao | Rất cao |
| **Vendor support** | Universal | Universal | Rộng rãi | Đang tăng |
| **Hardware requirement** | Bất kỳ MPLS | Bất kỳ MPLS | Bất kỳ MPLS | IPv6 + SRH |
| **Debugging** | Phức tạp | Rất phức tạp | Đơn giản | Đơn giản |
| **Network programming** | Không | Không | Hạn chế | Phong phú |

### Vì sao đây không phải "RSVP-TE bị xóa ngay"

```
Thực tế migration:

Phase 1: SR-MPLS coexistence với LDP
  → Chạy song song LDP và SR trên cùng mạng
  → SR prefill FIB entry, LDP là fallback
  → Dần dần tắt LDP từng router một

Phase 2: SR thay thế RSVP-TE
  → SR-TE Policy thay thế RSVP-TE tunnel
  → Phức tạp hơn: cần re-implement mọi TE tunnel sang SR Policy
  → Thường làm theo từng vùng mạng (domain)

Phase 3 (dài hạn): SRv6
  → Khi phần cứng mới hỗ trợ SRH
  → Khi mạng chuyển sang IPv6-only
  → Khi cần network programming capability
```

---

## 10. Phân tích Số liệu: Scale 1,000 Node

### Kịch bản so sánh định lượng

**Setup:**
- 1,000 node trong SR domain (router Core và PE)
- 100 edge/PE node cần full-mesh TE (customer-facing)
- Mỗi TE path trung bình 6 hop
- Mỗi node có trung bình 4 neighbor

### RSVP-TE Analysis

```
State calculation:

Số tunnel (one-way): 100 × 99 = 9,900
State per tunnel per hop: 2 (PATH state + RESV state)
Tổng RSVP state trên toàn mạng: 9,900 × 6 × 2 = 118,800 entries

Per-node impact (core router transit 500 tunnels):
  RSVP state: 500 × 2 = 1,000 entries
  RSVP refresh (30s interval): 1,000 / 30 = ~33 messages/giây
  Memory: mỗi RSVP state ~500 bytes → 1,000 × 500 = 500KB/router
  
Scaling problem: Tăng edge node lên 200:
  Tunnel = 200 × 199 = 39,800
  State = 39,800 × 6 × 2 = 477,600 entries
  → Gấp 4x khi edge node tăng 2x → O(N²)

Thêm rủi ro:
  Soft-state: nếu RSVP refresh bị delay/drop → tunnel timeout → traffic loss
  Reoptimization: khi topology thay đổi → phải re-signal nhiều tunnel
  Preemption: tunnel priority conflict → complex to manage
```

### SR-MPLS Analysis

```
State calculation:

Với SR-MPLS, core node chỉ cần biết:
  - Prefix-SID của mọi node (N entries = 1,000 entries trong SRGB)
  - Adjacency-SID của local links (4 entries/node)
  - Không có per-tunnel state

Tổng state tại mọi core node:
  SRGB forwarding entries: 1,000 (giống FIB bình thường, chỉ là label lookup)
  Local Adj-SID: 4 (rất nhỏ)
  
  KHÔNG có: per-tunnel state, RSVP refresh overhead

Scaling: tăng edge node từ 100 → 200:
  SR Policy tại 200 edge node: 200 × 199 = 39,800 policies
  → CHỈ tồn tại tại 200 headend node, KHÔNG ở core
  → Core state: vẫn là 1,000 SRGB entries → O(N), không phải O(N²)
  
Memory comparison (per core router):
  RSVP-TE: 500 KB cho tunnel state + refresh CPU
  SR-MPLS:  ~100 KB SRGB entries + local adj (chủ yếu là FIB bình thường)
  
CPU comparison:
  RSVP-TE: 33 messages/giây chỉ cho refresh, tăng theo số tunnel
  SR-MPLS:  0 (không có keepalive, không có soft-state)
```

### Kết quả tổng hợp

| Chỉ số | RSVP-TE (100 edge) | RSVP-TE (200 edge) | SR-MPLS (200 edge) |
|---|---|---|---|
| Total tunnel state | 118,800 | 477,600 | 0 (core) |
| Memory per core node | ~500 KB | ~2 MB | ~100 KB |
| RSVP CPU overhead | ~33 msg/s | ~130 msg/s | 0 |
| Scale behavior | O(N²) | O(N²) | O(N) |
| Recovery time (link fail) | ~1-2s (re-signal) | ~1-2s | <50ms (TI-LFA) |

---

## 11. SRv6 Network Programming

### Concept: Network Function as Segment

SRv6 cho phép mã hóa **network function** vào SID. Thay vì chỉ "forward đến node X", SID có thể nghĩa là "thực hiện function Y tại node X". Đây gọi là **SRv6 Network Programming** (RFC 8986).

```
SRv6 Function types (một số quan trọng):

End:
  Node endpoint, tương đương Prefix-SID trong SR-MPLS
  Giảm Segments Left, update IPv6 Dst, forward

End.X:
  Adjacency endpoint, forward qua link L cụ thể
  Tương đương Adj-SID trong SR-MPLS

End.T:
  Lookup trong specific routing table (không decrypt payload)
  Dùng cho inter-VRF steering

End.DT4 / End.DT6:
  Decapsulate + Lookup trong VRF routing table
  IPv4 hoặc IPv6
  → Thay thế cho MPLS VPN (L3VPN không cần MPLS!)
  
  Ví dụ: PE node nhận SRv6 packet với Dst = End.DT4 SID
  → Decap outer IPv6
  → Lookup inner IPv4 trong VRF table
  → Forward đến CE customer

End.DX2:
  Decapsulate + forward L2 frame (cho L2 VPN / EVPN)

End.B6.Encaps:
  Binding SID: encapsulate với new SRH
  Dùng cho SR Policy steering và hierarchical SRv6

uSID (Micro Segment):
  Đóng gói nhiều SID nhỏ (16-bit) vào một địa chỉ IPv6 128-bit
  Giải quyết overhead của SRH header
  → 8 node IDs fit vào 1 SID → giảm overhead 8x
```

### SRv6 cho L3VPN (thay thế MPLS VPN)

```
MPLS L3VPN truyền thống:

CE ─── PE1 ─── [MPLS Core: VPN label + Transport label] ─── PE2 ─── CE
                Cần: LDP/SR transport + BGP VPN signaling + MPLS

SRv6 L3VPN (không cần MPLS):

CE ─── PE1 ─── [IPv6 Core: SRH với End.DT4 SID của PE2] ─── PE2 ─── CE
                Chỉ cần: IPv6 forwarding + SRH + BGP VPN signaling

PE2 SID: 2001:db8:pe2::d004 (End.DT4, VRF ID 4)

Gói từ PE1 đến customer trong VRF 4:
  Outer IPv6 Dst: 2001:db8:pe2::d004  ← SID chứa cả node + function + VRF
  No SRH needed for simple case (direct PE1 → PE2)
  
  PE2 nhận:
  → Dst match local SID 2001:db8:pe2::d004
  → Function: End.DT4 → decap, lookup trong VRF 4
  → Forward IP payload đến CE
```

### Network Slicing với SRv6 và Flex-Algo

```
5G Network Slicing ví dụ:

Slice eMBB (enhanced Mobile Broadband):
  SRv6 Flex-Algo 128 (bandwidth-optimized topology)
  End.DT SID trên Flex-Algo 128 nodes
  → Traffic chọn đường băng thông cao nhất

Slice URLLC (Ultra-Reliable Low-Latency Communication):
  SRv6 Flex-Algo 129 (latency-optimized topology)
  End.DT SID trên Flex-Algo 129 nodes
  → Traffic chọn đường latency thấp nhất (<1ms)

Slice mMTC (massive Machine Type Communication):
  SRv6 default SPF (cost-optimized)
  → Traffic chọn đường rẻ nhất

Một physical network → nhiều logical slice → controlled bởi SRv6 SID
```

---

## 12. Tích hợp SDN: PCEP, BGP-LS, và SR Controller

### BGP-LS — thu thập topology

**BGP-LS (BGP Link State)** — RFC 7752 — cho phép export thông tin topology IGP (node, link, prefix, SID) ra ngoài domain thông qua BGP. Controller nhận được "ảnh" topology đầy đủ.

```
BGP-LS flow:

IGP (IS-IS/OSPF) ──► BGP-LS speaker ──► BGP session ──► SR Controller
                      (router hoặc       (BGP-LS NLRI)   (PCE, SDN platform)
                       route reflector)
                       
BGP-LS NLRI types:
  Node NLRI: thông tin về router (Router-ID, capabilities, SID)
  Link NLRI: thông tin về link (metric, bandwidth, delay, Adj-SID)
  Prefix NLRI: thông tin về prefix (metric, Prefix-SID)
  
Controller thấy:
  {Node A, SRGB 16000, SID_index=1}
  {Link A→B, metric=10, delay=5ms, bandwidth=100G, Adj-SID=24001}
  {Node B, SRGB 16000, SID_index=2}
  ... toàn bộ topology

→ Có đủ thông tin để tính bất kỳ constrained path nào
```

### PCEP — cài đường xuống node

**PCEP (Path Computation Element Protocol)** — RFC 5440 — cho phép controller (PCE) tính đường và cài xuống router (PCC - Path Computation Client).

```
PCEP interaction (Stateful PCE + SR):

1. PCC (router) báo cáo SR Policy hiện tại lên PCE:
   PCC → PCE: PCRpt (Report)
   "Tôi có SR Policy: headend=A, endpoint=E, active SL=[16003, 16005]"

2. PCE nhận telemetry: link A→C đang 85% utilization
   PCE tính lại: đường mới qua D thay vì C
   PCE → PCC: PCUpd (Update)
   "SR Policy: headend=A, endpoint=E, new SL=[16004, 16005]"

3. PCC (router A) áp dụng SL mới:
   Traffic đang chạy qua C → tự động chuyển sang D
   Không cần operator can thiệp

PCEP message types:
  Open:    establish PCEP session, exchange capabilities
  PCReq:   PCC request PCE compute path
  PCRep:   PCE reply với computed path
  PCRpt:   PCC report state lên PCE (stateful)
  PCUpd:   PCE update SR Policy tại PCC (stateful)
  PCInitiate: PCE tạo SR Policy mới tại PCC (PCE-initiated)
```

### SR Controller Architecture

```
Full SR Controller Stack:

┌──────────────────────────────────────────────────────────────┐
│                      SR Controller                           │
│                                                              │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────┐  │
│  │  Topology DB   │  │  Traffic       │  │  Path         │  │
│  │  (BGP-LS       │  │  Matrix        │  │  Computation  │  │
│  │   input)       │  │  (Telemetry    │  │  Engine       │  │
│  │                │  │   input)       │  │  (CSPF, TE)   │  │
│  └────────────────┘  └────────────────┘  └───────────────┘  │
│          │                  │                    │           │
│          └──────────────────┴────────────────────┘           │
│                             │                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Policy Manager                          │   │
│  │  (SR Policy CRUD, conflict resolution, priority)     │   │
│  └──────────────────────────┬─────────────────────────┘    │
│                             │                                │
│  ┌──────────────┐  ┌────────────────┐  ┌──────────────┐    │
│  │  PCEP Agent  │  │  BGP Speaker   │  │  gNMI/NETCONF│    │
│  │  (PCEP south │  │  (BGP-LS north,│  │  (config push│    │
│  │   bound)     │  │   SR Policy    │  │   southbound)│    │
│  │              │  │   via BGP)     │  │              │    │
│  └──────┬───────┘  └───────┬────────┘  └──────┬───────┘    │
└─────────┼──────────────────┼──────────────────┼────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
    (PCEP session)    (BGP session)      (gNMI session)
    Routers           Route Reflector    Routers
```

---

## 13. Liên hệ Automation, Telemetry, và AI

### SR là nền tảng lý tưởng cho Closed-Loop Automation

```
Closed-Loop Automation với SR + Telemetry + AI:

Step 1: Observe (Streaming Telemetry từ bài trước)
  ┌─────────────────────────────────────────────────────────┐
  │ Mọi router push telemetry mỗi giây:                     │
  │   - Link utilization per interface                      │
  │   - SR Policy active/standby status                     │
  │   - BFD session state                                   │
  │   - Latency measurements (TWAMP, Y.1731)                │
  └──────────────────────────┬──────────────────────────────┘
                             │
Step 2: Analyze (AI/ML Engine)
  ┌─────────────────────────────────────────────────────────┐
  │ AI Engine nhận real-time telemetry:                     │
  │   "Link A→C: utilization tăng từ 60% → 78% → 89%"      │
  │   ML model dự đoán: "sẽ đạt 100% trong 3 phút"         │
  │   Recommendation: "Shift 30% traffic sang A→D→E path"   │
  └──────────────────────────┬──────────────────────────────┘
                             │
Step 3: Act (SR Controller + PCEP)
  ┌─────────────────────────────────────────────────────────┐
  │ Controller nhận recommendation:                         │
  │   Tính SR Policy mới: A→E via D, SL=[SID_D, SID_E]     │
  │   PCUpd → Router A: cập nhật SR Policy color=200        │
  │   BGP Color Community update: redirect 30% traffic      │
  └──────────────────────────┬──────────────────────────────┘
                             │
Step 4: Verify (feedback loop)
  ┌─────────────────────────────────────────────────────────┐
  │ Telemetry 5 giây sau:                                   │
  │   Link A→C: 63% (giảm, OK)                              │
  │   Link A→D: 45% (tăng vừa phải, OK)                     │
  │   Action: verified successful                           │
  └─────────────────────────────────────────────────────────┘

Toàn bộ: Detect → Decide → Act → Verify trong < 30 giây, không cần người
```

### SR Policy as Code — GitOps approach

```
SR Policy được quản lý như code:

# sr_policy.yaml (Ansible/NETCONF playbook)
sr_policies:
  - name: "voip-low-latency"
    headend: router-core-01
    endpoint: 192.0.2.50
    color: 100
    candidate_paths:
      - preference: 200
        segment_list:
          - sid: 16003  # via Node C (low latency path)
          - sid: 16050  # endpoint
        constraints:
          max_delay: 5ms
      - preference: 100
        segment_list:
          - sid: 16050  # best-effort fallback
          
# Apply via Ansible + NETCONF:
# ansible-playbook deploy_sr_policy.yml --limit router-core-01

Lợi ích GitOps:
  → Version control cho SR Policy (git blame, git revert)
  → Code review trước khi apply production
  → CI/CD pipeline: validate → test in staging → deploy production
  → Rollback trong giây: git revert → ansible-playbook
```

### Cross-Layer Automation: Optical + SR-TE

Kết hợp với kiến thức từ bài DWDM:

```
Scenario: Optical degradation → proactive SR reroute

1. Optical Telemetry (từ DWDM system):
   OSNR trên fiber A→B đang giảm dần (baseline: 18dB, now: 15dB)
   BER đang tăng, dự đoán link lỗi trong < 1 giờ

2. Cross-layer correlation engine:
   Mapping: Optical λ5 → IP link Router-A GigE0/0/1 → Router-B
   Prediction: "IP link A→B sẽ down trong ~45 phút với confidence 85%"

3. Proactive SR action:
   Controller update SR Policy:
     Priority 1 (active): path through A→B → SWAP to A→C (healthy path)
     Priority 2 (standby): original path through B (kept for monitor)
   
4. Maintenance coordination:
   Auto-create ticket: "Optical degradation on span A-B, fiber maintenance needed"
   Pre-position: notify maintenance team 45 min trước khi estimated failure

→ Proactive maintenance thay vì reactive incident response
→ Zero user impact (traffic re-routed trước khi lỗi)
```

---

## 14. Lộ trình Triển khai Thực tế

### Phase 1: SR-MPLS song song với LDP (Low risk)

```
Mục tiêu: Thêm SR mà không gây gián đoạn, LDP vẫn là primary

Bước 1: Enable SR trong IGP (IS-IS hoặc OSPF)
  → Assign Prefix-SID cho mọi loopback (cần planning SRGB)
  → IS-IS: segment-routing mpls, prefix-sid index X
  → OSPF: segment-routing mpls, prefix-sid index X
  → Không ảnh hưởng traffic: SR và LDP forward song song

Bước 2: Verify SR prefix propagation
  → show segment-routing mpls lb detail
  → show mpls forwarding (kiểm tra SR label entry)
  → Traceroute với SR header: traceroute sr-mpls x.x.x.x

Bước 3: Enable TI-LFA
  → fast-reroute per-prefix ti-lfa (IS-IS/OSPF)
  → Kiểm tra backup path tính sẵn
  → show isis fast-reroute summary

Bước 4: Pilot SR-TE Policy
  → Chọn 1-2 traffic flow không quan trọng
  → Tạo SR Policy thủ công, verify forwarding
  → Monitor qua telemetry

Timeline Phase 1: 4-8 tuần
Risk: Rất thấp (LDP vẫn là primary, SR là overlay)
```

### Phase 2: SR-MPLS thay thế RSVP-TE

```
Mục tiêu: Migrate TE tunnel từ RSVP-TE sang SR Policy

Bước 5: Inventory RSVP-TE tunnels
  → List tất cả tunnel, headend, endpoint, constraint
  → Classify: bandwidth TE, disjoint path, latency-sensitive

Bước 6: Convert từng tunnel sang SR Policy
  → Bắt đầu từ non-critical tunnel
  → SR Policy với cùng constraint (bandwidth, disjoint, v.v.)
  → A/B test: chạy song song, compare latency và loss

Bước 7: Migrate traffic steering
  → Chuyển BGP route từ RSVP tunnel nhex-hop sang SR Policy BSID
  → Verify với telemetry: traffic đang đi đúng SR path

Bước 8: Drain và tắt RSVP-TE
  → Sau khi 100% traffic trên SR Policy
  → Disable RSVP-TE tunnel (admin-down)
  → Monitor 24h → remove RSVP config
  → Dần dần tắt RSVP-TE hoàn toàn khỏi mạng

Timeline Phase 2: 3-6 tháng
Risk: Trung bình (cần test kỹ từng tunnel trước khi migrate)
```

### Phase 3: LDP Deprecation

```
Mục tiêu: Tắt hoàn toàn LDP, chạy SR-only

Bước 9: SR Prefer (LDP still running)
  → Cấu hình: SR label trumps LDP label (SR-prefer)
  → Traffic đã chạy trên SR label, LDP chỉ là backup
  → Verify: không còn traffic trên LDP path

Bước 10: Disable LDP per-interface
  → Remove LDP từng interface một
  → Monitor BGP VPN label (LDP vẫn cần nếu dùng MPLS VPN)
  → Nếu dùng L3VPN: cần SR-TE với BGP Segment hoặc chuyển sang SRv6

Bước 11: LDP cleanup
  → Remove LDP config hoàn toàn
  → Verify mọi VPN service vẫn hoạt động
  → Control plane đơn giản hơn đáng kể: chỉ còn IS-IS/OSPF

Timeline Phase 3: 2-4 tháng
Risk: Trung bình-Cao (ảnh hưởng VPN service nếu chưa migrate)
```

### Phase 4 (Long-term): SRv6 Migration

```
Điều kiện để xem xét SRv6:
  ✓ Phần cứng thế hệ mới hỗ trợ SRH (ASIC, NP)
  ✓ Team hiểu SRv6 đủ sâu
  ✓ Use case rõ ràng: 5G transport, DC interconnect, IPv6-only
  ✓ OS version hỗ trợ SRv6 production (không phải beta)

Migration path:
  → SR-MPLS + SRv6 dual-stack (giai đoạn đầu)
  → SRv6 cho vùng mạng mới (greenfield)
  → SR-MPLS cho vùng mạng cũ (brownfield, legacy hardware)
  → Dần dần replace hardware → full SRv6

Timeline: 1-3 năm (tùy quy mô và tốc độ hardware refresh)
```

---

## 15. Lab Mini: Cấu hình SR-MPLS Cơ bản

### Topology lab

```
Lab Topology (4 node):

        10.0.12.0/30              10.0.23.0/30
  ┌─────────────────┐       ┌─────────────────┐
  │    10.0.12.1    │       │    10.0.23.1    │
[R1]─────────────[R2]─────────────────────[R3]──────[R4]
  │ Lo: 1.1.1.1   │ Lo: 2.2.2.2   │ Lo: 3.3.3.3   │ Lo: 4.4.4.4
  │ SID: 16001     │ SID: 16002     │ SID: 16003     │ SID: 16004
  └─────────────────┘               └─────────────────┘
         │                                  │
         └───────── 10.0.14.0/30 ──────────[R4]
                                    backup path
```

### Cấu hình IS-IS + SR-MPLS (Cisco IOS-XR)

```
! === R1 Configuration ===

! IS-IS với SR extension
router isis CORE
  net 49.0001.0000.0000.0001.00
  address-family ipv4 unicast
    metric-style wide
    advertise link attributes                  ! quảng bá TE attributes
    segment-routing mpls                       ! enable SR
  !
  interface Loopback0
    passive
    address-family ipv4 unicast
      prefix-sid index 1                       ! Prefix-SID = SRGB_base + 1 = 16001
  !
  interface GigabitEthernet0/0/0/0             ! link to R2
    point-to-point
    address-family ipv4 unicast
      adjacency-sid absolute 24001             ! static Adj-SID (optional)
      fast-reroute per-prefix ti-lfa           ! enable TI-LFA

! SRGB configuration (nếu cần customize)
segment-routing
  global-block 16000 23999
!

! Verify:
show segment-routing mpls lb detail
! Expected:
!   Prefix: 1.1.1.1/32
!   Label: 16001 (out), Next-hop: local
!   Backup: TI-LFA: via R2, label 16001
```

```
! === R2 Configuration (tương tự, SID index 2) ===

router isis CORE
  net 49.0001.0000.0000.0002.00
  address-family ipv4 unicast
    metric-style wide
    segment-routing mpls
  !
  interface Loopback0
    passive
    address-family ipv4 unicast
      prefix-sid index 2                       ! SID = 16002
  !
  interface GigabitEthernet0/0/0/0             ! link to R1
    point-to-point
    address-family ipv4 unicast
      fast-reroute per-prefix ti-lfa
  !
  interface GigabitEthernet0/0/0/1             ! link to R3
    point-to-point
    address-family ipv4 unicast
      fast-reroute per-prefix ti-lfa
```

### Cấu hình SR-TE Policy (Cisco IOS-XR)

```
! === SR Policy tại R1: force traffic đến R4 qua R2→R3 ===

segment-routing
  traffic-eng
    policy TO_R4_VIA_R2_R3
      color 100 end-point ipv4 4.4.4.4
      candidate-paths
        preference 200
          explicit segment-list SL_R2_R3_R4
            index 10 mpls label 16002          ! hop qua R2
            index 20 mpls label 16003          ! hop qua R3  
            index 30 mpls label 16004          ! endpoint R4
          !
        preference 100
          dynamic
            metric type igp                    ! fallback: shortest path
          !
      !
    !
  !
!

! Segment list định nghĩa riêng (alternative syntax):
segment-routing
  traffic-eng
    segment-list SL_R2_R3_R4
      index 10 mpls label 16002
      index 20 mpls label 16003
      index 30 mpls label 16004

! Verify SR Policy:
show segment-routing traffic-eng policy name TO_R4_VIA_R2_R3
! Expected:
!   Color: 100, End-point: 4.4.4.4
!   Status: Admin up, Operational up
!   Candidate-paths:
!     Preference 200 (Active):
!       SID-list: [16002, 16003, 16004]

! Verify forwarding:
traceroute sr-policy color 100 endpoint 4.4.4.4 source 1.1.1.1
! Expected: R1 → R2 → R3 → R4
```

### Cấu hình IS-IS + SR (Junos)

```
# === Juniper (Junos) SR configuration ===

# IS-IS với SR
protocols {
    isis {
        source-packet-routing {
            srgb start-label 16000 index-range 8000;
            node-segment {
                ipv4-index 1;                    # Prefix-SID index = 1 → label 16001
            }
        }
        interface ge-0/0/0.0 {
            point-to-point;
            level 2 {
                post-convergence-lfa {           # TI-LFA trên Junos
                    node-protection;
                }
            }
        }
        interface lo0.0 {
            passive;
        }
    }
}

# SR-TE Policy (Junos Flex LSP)
routing-options {
    source-routing-path sr-policy-to-r4 {
        to 4.4.4.4;
        primary {
            hop 0 label 16002;
            hop 1 label 16003;
            hop 2 label 16004;
        }
    }
}
```

### Verification commands tổng hợp

```
# Cisco IOS-XR:
show segment-routing mpls lb detail              # SRGB entries
show segment-routing mpls forwarding detail      # SR forwarding table
show isis segment-routing label table            # IS-IS SR label info
show mpls forwarding labels 16001 16005          # specific label range
show isis fast-reroute summary                   # TI-LFA coverage
show segment-routing traffic-eng policy          # SR Policy status
show segment-routing traffic-eng forwarding policy name <X>  # Policy forwarding
traceroute mpls ipv4 x.x.x.x/32 fec-type sr-preferred  # SR traceroute

# Juniper Junos:
show isis spring label-switched-path             # SR LSP
show route protocol isis label-switched-path     # SR routes
show mpls label-switched-path sr                 # SR forwarding
show isis backup coverage                        # TI-LFA coverage

# Useful debug:
debug mpls lfib-program (IOS-XR)                # MPLS programming debug
show isis database detail | include SID          # IS-IS SID advertisement
```

---

## 16. Glossary

| Thuật ngữ | Tiếng Anh đầy đủ | Giải nghĩa ngắn gọn |
|---|---|---|
| SR | Segment Routing | Kiến trúc routing nhúng đường đi vào header gói |
| SID | Segment Identifier | Định danh của một segment (label MPLS hoặc IPv6 address) |
| SRH | Segment Routing Header | Extension header IPv6 chứa SID list (SRv6) |
| SRGB | SR Global Block | Dải nhãn MPLS reserve cho Prefix-SID |
| Prefix-SID | - | SID global đại diện cho một node (loopback prefix) |
| Adj-SID | Adjacency SID | SID local đại diện cho một link cụ thể |
| Anycast-SID | - | SID dùng chung cho nhiều node trong một nhóm |
| BSID | Binding SID | SID đại diện cho toàn bộ SR Policy (proxy) |
| SR-MPLS | SR with MPLS data plane | SR dùng label stack MPLS |
| SRv6 | SR version 6 | SR dùng IPv6 extension header |
| uSID | Micro SID | SID nhỏ 16-bit đóng gói nhiều cái vào 1 IPv6 address |
| SR Policy | - | Định nghĩa đường đi SR: headend + color + endpoint + SL |
| SL | Segment List | Danh sách ordered các SID xác định đường đi |
| SR-TE | SR Traffic Engineering | Dùng SR để điều khiển đường đi traffic |
| TI-LFA | Topology Independent LFA | Fast reroute pre-computed dùng SR, coverage 100% |
| LFA | Loop-Free Alternate | Backup path pre-computed trong IGP, coverage ~70-80% |
| PHP | Penultimate Hop Popping | Pop label tại node kề cuối thay vì egress |
| Flex-Algo | Flexible Algorithm | Nhiều topology/metric song song trong SR domain |
| BGP-LS | BGP Link State | Export topology IGP qua BGP cho controller |
| PCEP | Path Computation Element Protocol | Giao thức giữa SR controller và router |
| PCE | Path Computation Element | Thực thể tính đường trong mạng (controller) |
| PCC | Path Computation Client | Router nhận đường từ PCE |
| CSPF | Constrained Shortest Path First | SPF có ràng buộc (bandwidth, delay, color) |
| LDP | Label Distribution Protocol | Giao thức phân phối nhãn MPLS cổ điển |
| RSVP-TE | Resource Reservation Protocol - TE | Giao thức tạo MPLS TE tunnel cổ điển |
| Soft-state | - | State cần refresh định kỳ (đặc trưng của RSVP) |
| End | SRv6 End function | Node endpoint, forward đến next SID |
| End.X | SRv6 End.X function | Adjacency endpoint, forward qua link cụ thể |
| End.DT4 | SRv6 End.DT4 function | Decap + IPv4 VRF lookup (thay MPLS VPN label) |
| Network Programming | SRv6 Network Programming | Mã hóa network function vào SID (RFC 8986) |
| Source Routing | - | Node nguồn quyết định toàn bộ đường đi |
| Stateless Core | - | Node lõi không giữ per-flow/per-tunnel state |

---

## 17. Tài liệu Tham khảo

### RFCs Nền tảng
- **RFC 8402** — Segment Routing Architecture (2018) — đọc đầu tiên
- **RFC 8660** — Segment Routing with the MPLS Data Plane
- **RFC 8754** — IPv6 Segment Routing Header (SRH)
- **RFC 8986** — Segment Routing over IPv6 (SRv6) Network Programming
- **RFC 8667** — IS-IS Extensions for Segment Routing
- **RFC 8665** — OSPF Extensions for Segment Routing
- **RFC 9350** — IGP Flexible Algorithm (Flex-Algo)

### RFC Liên quan
- **RFC 5286** — Basic Specification for IP Fast Reroute: Loop-Free Alternates (LFA)
- **RFC 7752** — North-Bound Distribution of Link-State and TE Information using BGP (BGP-LS)
- **RFC 5440** — Path Computation Element (PCE) Communication Protocol (PCEP)
- **RFC 5036** — LDP Specification
- **RFC 3209** — RSVP-TE Extensions for LSP Tunnels

### Vendor Documentation
- **Cisco:** Segment Routing Configuration Guide (IOS-XR, NX-OS, IOS-XE)
- **Cisco:** SR-TE Policy Configuration and Design Guide
- **Juniper:** Segment Routing User Guide (Junos)
- **Nokia:** Segment Routing in SR-OS
- **Arista:** EOS Segment Routing Configuration Guide

### Community và Learning
- **segment-routing.net** — tài liệu kỹ thuật cộng đồng, tutorials, topology labs
- **NANOG / RIPE presentations** — deployment experience từ các ISP tier-1
- **IETF SPRING WG** — datatracker.ietf.org (working group phát triển chuẩn SR)
- **OpenConfig SR Policy** — openconfig.net/docs/models/sr

### Sách
- *Segment Routing, Part I* — Clarence Filsfils et al. (Cisco Press) — tác giả chính của SR
- *Segment Routing, Part II* — Clarence Filsfils et al. — SRv6 và advanced topics

---

*Bài viết phản ánh trạng thái công nghệ tính đến mid-2026. SR-MPLS đã production-ready trên mọi major vendor. SRv6 đang tăng tốc adoption đặc biệt trong 5G transport và DC interconnect — theo dõi IETF SPRING WG và vendor release notes để cập nhật.*

*Tác giả: IP/Core Network Engineer — Series "Networking from the Ground Up"*


---
layout: page-toc
title: "MPLS L3VPN: VRF, RD, RT"
permalink: /writeups/network-operations-portfolio/research-notes/mpls-l3vpn-vrf-rd-rt/
toc: true
---
# MPLS L3VPN — VRF, Route Distinguisher, Route Target

> **Đối tượng:** IP/Core Network Engineer muốn hiểu nền tảng dịch vụ VPN lớp 3 trong mạng ISP — cách ISP cung cấp private connectivity cho hàng trăm doanh nghiệp trên cùng một hạ tầng mà không bị xung đột.
>
> **Mức độ:** Intermediate–Advanced — giả định bạn đã hiểu MPLS label switching, BGP cơ bản, và khái niệm routing table. Bài này kết nối chặt chẽ với bài Segment Routing trước đó trong series.

---

## Mục lục

1. [Bối cảnh: Bài toán multi-tenant trên shared infrastructure](#1-bối-cảnh-bài-toán-multi-tenant-trên-shared-infrastructure)
2. [Kiến trúc CE–PE–P–PE–CE](#2-kiến-trúc-cepepe-ce)
3. [VRF — Virtual Routing and Forwarding](#3-vrf--virtual-routing-and-forwarding)
4. [MP-BGP — Backbone của L3VPN control plane](#4-mp-bgp--backbone-của-l3vpn-control-plane)
5. [Route Distinguisher (RD) — Định danh prefix toàn cục](#5-route-distinguisher-rd--định-danh-prefix-toàn-cục)
6. [Route Target (RT) — Chính sách import/export](#6-route-target-rt--chính-sách-importexport)
7. [Luồng dữ liệu end-to-end: Gói tin đi như thế nào](#7-luồng-dữ-liệu-end-to-end-gói-tin-đi-như-thế-nào)
8. [PE–CE Routing: Các lựa chọn giao thức](#8-pece-routing-các-lựa-chọn-giao-thức)
9. [Topology VPN nâng cao: Hub-and-Spoke, Extranet](#9-topology-vpn-nâng-cao-hub-and-spoke-extranet)
10. [Route Reflector trong L3VPN](#10-route-reflector-trong-l3vpn)
11. [MPLS L3VPN với Segment Routing (SR-MPLS)](#11-mpls-l3vpn-với-segment-routing-sr-mpls)
12. [So sánh: L3VPN vs các giải pháp VPN khác](#12-so-sánh-l3vpn-vs-các-giải-pháp-vpn-khác)
13. [Troubleshooting: Phương pháp và lệnh thực tế](#13-troubleshooting-phương-pháp-và-lệnh-thực-tế)
14. [Automation: Provision VPN bằng NETCONF/Ansible](#14-automation-provision-vpn-bằng-netconfansible)
15. [Lab mini: Cấu hình L3VPN đầy đủ](#15-lab-mini-cấu-hình-l3vpn-đầy-đủ)
16. [Glossary](#16-glossary)
17. [Tài liệu tham khảo](#17-tài-liệu-tham-khảo)

---

## 1. Bối cảnh: Bài toán Multi-tenant trên Shared Infrastructure

### Vấn đề cốt lõi

Khi ISP cần cung cấp **private connectivity** cho hàng trăm doanh nghiệp (enterprise) trên cùng một hạ tầng Core, hai yêu cầu mâu thuẫn nhau xuất hiện:

1. **Hiệu quả kinh tế:** Chia sẻ phần cứng, giảm chi phí vận hành
2. **Tách biệt hoàn toàn:** Khách hàng A không được "nhìn thấy" traffic của khách hàng B, kể cả khi họ dùng trùng địa chỉ IP

```
Vấn đề IP overlap:

Khách hàng A (Ngân hàng):    Khách hàng B (Bệnh viện):
  Branch 1: 10.1.0.0/16        Branch 1: 10.1.0.0/16  ← TRÙNG!
  HQ:       10.2.0.0/16        HQ:       10.2.0.0/16  ← TRÙNG!
  Data Center: 10.3.0.0/16     Data Center: 10.3.0.0/16 ← TRÙNG!

Nếu cả hai đều kết nối vào PE-1 với global routing table:
  PE-1 routing table:
    10.1.0.0/16 via CE-A1  ← Customer A
    10.1.0.0/16 via CE-B1  ← Customer B (GHI ĐÈ!)
  
  → Conflict! Traffic của B có thể đi nhầm sang A → security breach nghiêm trọng
```

### Trước khi có MPLS L3VPN

Giải pháp cũ: **mỗi khách hàng một bộ router vật lý riêng**. Chi phí khổng lồ, không scale được. Một ISP phục vụ 500 khách hàng enterprise = 500 bộ PE router riêng biệt.

**MPLS L3VPN (RFC 4364, 2006)** — tiền thân là RFC 2547 (1999) — giải quyết triệt để bằng ba cơ chế:
- **VRF:** tách biệt routing table theo từng khách hàng
- **RD:** làm cho prefix trùng lặp trở nên duy nhất trong BGP
- **RT:** chính sách kiểm soát route nào vào VRF nào

---

## 2. Kiến trúc CE–PE–P–PE–CE

### Vai trò của từng thành phần

```
┌────────────────────────────────────────────────────────────────────┐
│                    MPLS L3VPN Architecture                         │
└────────────────────────────────────────────────────────────────────┘

Customer A Network          ISP Core Network          Customer A Network
(Site 1)                                              (Site 2)

  ┌──────┐     ┌──────────────────────────────────┐     ┌──────┐
  │CE-A1 │─────│PE-1 ──── P1 ──── P2 ──── PE-2   │─────│CE-A2 │
  └──────┘     │                                  │     └──────┘
               │   (MPLS Label Switched Path)      │
  ┌──────┐     │                                  │     ┌──────┐
  │CE-B1 │─────│                                  │─────│CE-B2 │
  └──────┘     └──────────────────────────────────┘     └──────┘

Customer B Network                                Customer B Network
(Site 1)                                              (Site 2)

Responsibilities:
┌──────┬────────────────────────────────────────────────────────────┐
│ CE   │ Customer Edge: router của khách hàng                       │
│      │ - Không chạy MPLS, không biết về VPN                      │
│      │ - Chạy routing protocol với PE (BGP/OSPF/EIGRP/static)    │
│      │ - Đơn giản: chỉ thấy "kết nối đến ISP"                   │
├──────┼────────────────────────────────────────────────────────────┤
│ PE   │ Provider Edge: router biên ISP — node PHỨC TẠP NHẤT       │
│      │ - Duy trì VRF riêng cho mỗi khách hàng                   │
│      │ - Chạy MP-BGP với PE khác để trao đổi VPNv4 route        │
│      │ - Áp/tháo MPLS label (imposition/disposition)             │
│      │ - Nơi RD/RT logic được thực thi                           │
├──────┼────────────────────────────────────────────────────────────┤
│ P    │ Provider Core: router lõi ISP — chỉ chuyển tiếp nhãn     │
│      │ - Chạy IGP (IS-IS/OSPF) + LDP hoặc SR                    │
│      │ - CHỈ xử lý transport label (outer label)                 │
│      │ - KHÔNG biết về VPN, VRF, RD, RT, hay địa chỉ khách hàng│
│      │ - Đây là lý do mạng Core scale được: P node stateless     │
└──────┴────────────────────────────────────────────────────────────┘
```

### Tại sao P node không cần biết về VPN?

Đây là **điểm mạnh kiến trúc** cốt lõi của MPLS L3VPN:

```
P node forwarding decision:

Nhận packet với label stack:
  [Transport Label: 1001] [VPN Label: 2001] [IP Header: 10.1.1.10→10.2.2.10]

P node:
  → Đọc Label 1001
  → Tra MPLS FIB: "Label 1001 → swap to 1002, forward to PE-2"
  → Gửi đi. Xong.
  
P node không bao giờ nhìn vào:
  - VPN Label (2001)
  - IP Source (10.1.1.10)
  - IP Destination (10.2.2.10)
  - Đây là traffic của Customer A hay B

→ Thêm 1,000 VPN khách hàng mới:
  PE node: thêm VRF, cấu hình RD/RT
  P node: KHÔNG thay đổi gì cả
  
→ Đây là lý do MPLS L3VPN scale cực tốt
```

---

## 3. VRF — Virtual Routing and Forwarding

### 3.1 Khái niệm: Router ảo trong Router vật lý

VRF tạo ra các **instance định tuyến hoàn toàn độc lập** trên cùng một router vật lý. Mỗi VRF có:

```
VRF Instance = Complete routing context:

┌─────────────────────────────────────────────────────────────────┐
│                     Router PE-1 (Physical)                      │
│                                                                 │
│  ┌──────────────────────┐   ┌──────────────────────┐           │
│  │   VRF Customer_A     │   │   VRF Customer_B     │           │
│  │                      │   │                      │           │
│  │  RIB (Routing table) │   │  RIB (Routing table) │           │
│  │  10.1.0.0/16 → CE-A  │   │  10.1.0.0/16 → CE-B  │          │
│  │  10.2.0.0/16 → MPLS  │   │  10.2.0.0/16 → MPLS  │          │
│  │                      │   │                      │           │
│  │  FIB (Forwarding)    │   │  FIB (Forwarding)    │           │
│  │  (CEF entries)       │   │  (CEF entries)       │           │
│  │                      │   │                      │           │
│  │  ARP table           │   │  ARP table           │           │
│  │  Interfaces: Gi0/0   │   │  Interfaces: Gi0/1   │           │
│  └──────────────────────┘   └──────────────────────┘           │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Global Routing Table                        │  │
│  │  (Core IGP: IS-IS/OSPF, loopback, P2P links)            │  │
│  │  10.255.255.1/32 (loopback) → local                     │  │
│  │  10.255.255.2/32 (PE-2)     → via Core                  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

Tách biệt hoàn toàn:
  - Packet vào Gi0/0 → lookup trong VRF Customer_A FIB
  - Packet vào Gi0/1 → lookup trong VRF Customer_B FIB
  - Không có "leak" giữa hai VRF (trừ khi cấu hình route leak có chủ đích)
```

### 3.2 VRF-Lite vs MPLS VRF

**VRF-Lite:** dùng VRF mà không cần MPLS — phù hợp cho switch/router thuần IP. Tách biệt bảng định tuyến nhưng traffic phải đi qua physical/sub-interface riêng cho từng VRF.

**MPLS VRF (L3VPN):** dùng VRF kết hợp MPLS để transport traffic qua Core mà không cần physical link riêng cho từng VPN. Đây là cái chúng ta đang nói đến.

### 3.3 Cấu hình VRF — IOS-XE và IOS-XR

**Cisco IOS-XE (truyền thống):**
```
! Tạo VRF
ip vrf Customer_A
 rd 65000:100
 route-target export 65000:100
 route-target import 65000:100
!
ip vrf Customer_B
 rd 65000:200
 route-target export 65000:200
 route-target import 65000:200

! Gán interface vào VRF
interface GigabitEthernet0/0
 description "Link to CE-A1"
 ip vrf forwarding Customer_A     ! ← Lệnh này XÓA IP hiện có!
 ip address 192.168.1.1 255.255.255.252
```

**Cisco IOS-XR (modern syntax):**
```
vrf Customer_A
 address-family ipv4 unicast
  import route-target 65000:100
  export route-target 65000:100
 !
!
interface GigabitEthernet0/0/0/0
 vrf Customer_A
 ipv4 address 192.168.1.1 255.255.255.252
```

**Juniper Junos:**
```
routing-instances {
    Customer_A {
        instance-type vrf;
        interface ge-0/0/0.0;
        route-distinguisher 65000:100;
        vrf-target target:65000:100;     # shortcut: import+export cùng RT
        vrf-table-label;                 # enable VPN label allocation
    }
}
```

> ⚠️ **Lưu ý quan trọng (IOS-XE):** Lệnh `ip vrf forwarding <name>` sẽ **xóa toàn bộ IP address** trên interface. Phải cấu hình lại IP address ngay sau lệnh này. Đây là trap phổ biến khi config live.

### 3.4 VRF và MPLS label allocation

Khi VRF được tạo và interface được gán, PE tự động cấp phát một **VPN label** cho mỗi prefix trong VRF. Label này được quảng bá đến PE peers qua MP-BGP:

```
Label allocation per-VRF (per-prefix mặc định):

VRF Customer_A:
  10.1.0.0/16 → VPN label 2001 (chỉ PE-1 biết)
  10.3.0.0/16 → VPN label 2002

VRF Customer_B:
  10.1.0.0/16 → VPN label 3001 (label khác với A!)
  10.3.0.0/16 → VPN label 3002

PE-2 nhận VPNv4 update từ PE-1:
  65000:100:10.1.0.0/16 → label=2001, next-hop=PE-1_loopback
  65000:200:10.1.0.0/16 → label=3001, next-hop=PE-1_loopback
  
→ PE-2 biết: gói đến 10.1.0.0/16 của Customer_A → push label 2001 → gửi đến PE-1
             PE-1 nhận label 2001 → lookup VPN label table → VRF Customer_A → forward đến CE-A1
```

---

## 4. MP-BGP — Backbone của L3VPN Control Plane

### 4.1 Tại sao cần MP-BGP?

Các PE cần trao đổi VPN routing information với nhau. BGP được chọn vì:
- **Scale tốt:** BGP thiết kế cho hàng triệu prefix
- **Policy-rich:** Extended Community (RT) tích hợp tự nhiên
- **Không cần full mesh:** Route Reflector cho phép scale lên hàng nghìn PE
- **iBGP:** Các PE trong cùng AS dùng iBGP, không cần external routing

### 4.2 Address Family VPNv4/VPNv6

Để transport VPN prefix (12-byte VPNv4 = 8-byte RD + 4-byte IPv4) qua BGP, cần mở rộng BGP với **Multiprotocol Extensions (RFC 4760)**:

```
BGP Address Families trong L3VPN:

AFI (Address Family Identifier):
  1   = IPv4
  2   = IPv6
  
SAFI (Subsequent Address Family Identifier):
  1   = Unicast
  128 = VPN (VPNv4 khi AFI=1, VPNv6 khi AFI=2)

VPNv4 session: AFI=1, SAFI=128
VPNv6 session: AFI=2, SAFI=128

Một BGP session giữa hai PE:
  - Global BGP session (TCP 179): trao đổi capability
  - Trong session đó, activate address-family vpnv4
  - VPNv4 NLRI được mang trong MP_REACH_NLRI attribute (RFC 4760)
```

### 4.3 Cấu trúc BGP Update cho VPNv4

```
BGP Update message mang VPNv4 prefix:

MP_REACH_NLRI attribute:
  AFI: 1 (IPv4)
  SAFI: 128 (VPN)
  Next-hop: 10.255.255.1  ← Loopback của PE-1
             (IPv4 VPN next-hop, must be reachable via Core IGP)
  NLRI: 65000:100:10.1.0.0/16   ← RD + prefix (12 bytes)

Extended Community attribute:
  Route Target: 65000:100        ← RT để PE-2 biết đưa vào VRF nào

MPLS Label attribute (RFC 3107):
  Label: 2001                    ← VPN label (bottom of stack)
  
BGP Path Attributes chuẩn:
  AS-PATH: empty (iBGP)
  LOCAL-PREF: 100
  MED: (nếu có)
  ORIGIN: IGP hoặc EGP
```

### 4.4 Cấu hình MP-BGP trên PE (IOS-XE)

```
router bgp 65000
 bgp router-id 10.255.255.1
 bgp log-neighbor-changes
 
 ! Session iBGP đến PE-2 (dùng loopback để ổn định khi link vật lý fail)
 neighbor 10.255.255.2 remote-as 65000
 neighbor 10.255.255.2 update-source Loopback0
 neighbor 10.255.255.2 next-hop-self         ! quan trọng nếu không dùng RR
 
 ! === Address Family VPNv4 ===
 address-family vpnv4
  neighbor 10.255.255.2 activate
  neighbor 10.255.255.2 send-community extended  ! gửi RT community
  neighbor 10.255.255.2 next-hop-unchanged       ! preserve PE-1 as next-hop
 exit-address-family
 
 ! === Per-VRF Address Family ===
 address-family ipv4 vrf Customer_A
  redistribute connected                         ! quảng bá CE-A subnets
  redistribute ospf 100 vrf Customer_A           ! nếu dùng OSPF với CE
  maximum-paths 4                                ! ECMP trong VRF
 exit-address-family
 
 address-family ipv4 vrf Customer_B
  redistribute connected
  neighbor 192.168.2.2 remote-as 65001          ! BGP với CE-B
  neighbor 192.168.2.2 activate
 exit-address-family
```

---

## 5. Route Distinguisher (RD) — Định danh Prefix Toàn cục

### 5.1 Vấn đề RD giải quyết

Khi PE-1 nhận `10.1.0.0/16` từ CE-A và `10.1.0.0/16` từ CE-B, rồi quảng bá cả hai qua MP-BGP — PE-2 nhận hai prefix `10.1.0.0/16` hoàn toàn giống nhau. BGP sẽ chọn một và bỏ một (best path selection). Dữ liệu của Customer A hoặc B bị mất.

**RD giải quyết:** biến hai prefix giống nhau thành hai VPNv4 prefix khác nhau hoàn toàn trong BGP:

```
Không có RD:                    Với RD:
  BGP NLRI: 10.1.0.0/16          BGP NLRI: 65000:100:10.1.0.0/16 (Customer A)
  BGP NLRI: 10.1.0.0/16  ←TRÙNG  BGP NLRI: 65000:200:10.1.0.0/16 (Customer B)
  → BGP chọn 1, bỏ 1              → Hai prefix KHÁC NHAU, BGP giữ cả hai ✓
```

### 5.2 Cấu trúc RD (64-bit / 8 byte)

```
RD Format (RFC 4364, Section 4.2):

Type 0: 2-byte ASN : 4-byte assigned number
  ┌────────────┬─────────────────────────────────┐
  │  Type: 0   │  ASN (2B)  │  Admin# (4B)       │
  │  (2 bytes) │  e.g. 65000│  e.g. 100           │
  └────────────┴────────────┴─────────────────────┘
  Ví dụ: 65000:100

Type 1: 4-byte IP address : 2-byte assigned number
  ┌────────────┬─────────────────────────────────┐
  │  Type: 1   │  IP (4B)       │  Admin# (2B)   │
  │  (2 bytes) │  e.g. 10.0.0.1 │  e.g. 100      │
  └────────────┴────────────────┴─────────────────┘
  Ví dụ: 10.0.0.1:100

Type 2: 4-byte ASN : 2-byte assigned number
  ┌────────────┬─────────────────────────────────┐
  │  Type: 2   │  ASN (4B)    │  Admin# (2B)     │
  │  (2 bytes) │  e.g. 131072 │  e.g. 100        │
  └────────────┴──────────────┴─────────────────┘
  Ví dụ: 131072:100 (khi ISP dùng 4-byte ASN)
```

### 5.3 RD naming convention thực tế

```
Convention phổ biến tại ISP Việt Nam / khu vực:

Format: <ISP_ASN>:<Customer_ID>

Ví dụ ISP với AS 45899:
  45899:1001  → Customer ID 1001 (Enterprise Corp)
  45899:1002  → Customer ID 1002 (Bank XYZ)
  45899:1003  → Customer ID 1003 (Hospital ABC)

Mỗi PE của cùng customer dùng cùng RD:
  PE-1, VRF Customer_1001: rd 45899:1001
  PE-2, VRF Customer_1001: rd 45899:1001
  PE-3, VRF Customer_1001: rd 45899:1001
  (tất cả cùng RD → prefix của customer 1001 nhận dạng được trên toàn mạng)

Alternative: Per-PE unique RD (để BGP multipath hoạt động tốt hơn):
  PE-1, VRF Customer_1001: rd 45899:10011001
  PE-2, VRF Customer_1001: rd 45899:10021001
  PE-3, VRF Customer_1001: rd 45899:10031001
  (mỗi PE có RD khác nhau → BGP không merge path → optimal multipath)
```

### 5.4 RD ≠ RT: Sự khác biệt quan trọng

```
Nhầm lẫn phổ biến nhất khi học L3VPN:

RD (Route Distinguisher):
  ✓ Mục đích: làm prefix trở nên UNIQUE trong BGP table
  ✓ Chỉ là "tên" (identifier), không có ý nghĩa chính sách
  ✓ Không quyết định route nào vào VRF nào
  ✓ Thuộc về prefix (được encode vào NLRI)
  ✓ Một VRF có DUY NHẤT một RD

RT (Route Target):
  ✓ Mục đích: kiểm soát CHÍNH SÁCH import/export
  ✓ Là BGP Extended Community (gắn vào attribute của route)
  ✓ Quyết định route nào được đưa vào VRF nào
  ✓ Một VRF có thể có NHIỀU RT (import và/hoặc export)
  ✓ RT giống như "nhãn chính sách" (policy tag)

Analogy:
  RD = Số chứng minh nhân dân (unique ID)
  RT = Nhóm máu (xác định ai có thể nhận/cho gì)
```

---

## 6. Route Target (RT) — Chính sách Import/Export

### 6.1 Cơ chế hoạt động

RT là một **BGP Extended Community** (RFC 4360) — 8 byte — được gắn vào VPNv4 prefix khi quảng bá. RT hoạt động như "nhãn" để PE biết prefix này thuộc VPN nào và nên đưa vào VRF nào:

```
RT Export (khi PE quảng bá VPNv4 prefix ra BGP):
  
  VRF Customer_A có route 10.1.0.0/16 từ CE
  Export RT = 65000:100
  
  PE-1 gắn RT:65000:100 vào BGP update
  → Prefix quảng bá ra BGP với community: RT=65000:100

RT Import (khi PE nhận VPNv4 prefix từ BGP):
  
  PE-2 nhận: 65000:100:10.1.0.0/16 với RT=65000:100
  
  PE-2 kiểm tra tất cả VRF:
    VRF Customer_A: import RT = {65000:100} → MATCH!
    VRF Customer_B: import RT = {65000:200} → no match
    VRF Customer_C: import RT = {65000:300} → no match
  
  → Prefix được đưa vào VRF Customer_A
  → Không ai khác nhận được prefix này
```

### 6.2 Full mesh: Simple VPN

Mô hình đơn giản nhất — tất cả site của cùng customer kết nối full mesh:

```
Simple VPN (any-to-any):

Site A1 ──── PE-1:VRF_A (export RT=65:1, import RT=65:1)
                  ↕ MP-BGP
Site A2 ──── PE-2:VRF_A (export RT=65:1, import RT=65:1)
                  ↕ MP-BGP
Site A3 ──── PE-3:VRF_A (export RT=65:1, import RT=65:1)

Flow: Mọi PE export RT=65:1, mọi PE import RT=65:1
→ Mọi site nhận route của mọi site → full mesh connectivity
→ Đơn giản nhất, phù hợp cho customer không cần traffic control
```

### 6.3 Hub-and-Spoke: Kiểm soát topology bằng RT

Khách hàng muốn các branch chỉ nói chuyện qua HQ (không nói chuyện trực tiếp với nhau):

```
Hub-and-Spoke topology:

                 ┌─── HQ (Hub) ───┐
                 │                │
                 ▼                ▼
             Branch 1          Branch 2
             (Spoke)           (Spoke)

Spoke KHÔNG được nói chuyện trực tiếp với Spoke

RT Design:
  Hub VRF:   export RT=65:10   import RT=65:20
  Spoke VRF: export RT=65:20   import RT=65:10

Trace routes:
  Spoke→Hub: Spoke export 65:20, Hub import 65:20 → HUB NHẬN route Spoke ✓
  Hub→Spoke: Hub export 65:10, Spoke import 65:10 → SPOKE NHẬN route Hub ✓
  Spoke→Spoke: Spoke export 65:20, Spoke import 65:10 → 20 ≠ 10 → KHÔNG NHẬN ✓

Full diagram:
  PE-HQ  (VRF_Hub):   export 65:10, import 65:20
  PE-Br1 (VRF_Spk1):  export 65:20, import 65:10
  PE-Br2 (VRF_Spk2):  export 65:20, import 65:10

BGP update flow:
  PE-Br1 → (BGP Update: 10.1.0.0/24, RT=65:20) → PE-HQ
    PE-HQ: import RT match 65:20? YES → nhập vào VRF_Hub → quảng bá lại với RT=65:10
  PE-HQ → (BGP Update: 10.1.0.0/24 + 10.0.0.0/8, RT=65:10) → PE-Br2
    PE-Br2: import RT match 65:10? YES → nhập vào VRF_Spk2
    
→ Branch 2 nhận route của Branch 1, nhưng CHỈ QUA Hub
→ Traffic Branch1→Branch2: Branch1 → HQ → Branch2 (Hair-pin tại HQ)
```

### 6.4 Extranet: Chia sẻ resource giữa các VPN khác nhau

Khách hàng A và B cần truy cập chung một server Shared Service (ví dụ: DNS, NTP, Security Gateway):

```
Extranet Design:

  VPN_A: export 65:100, import {65:100, 65:300}
  VPN_B: export 65:200, import {65:200, 65:300}
  Shared_SVC: export 65:300, import {65:100, 65:200}

Shared Service quảng bá:
  10.100.0.0/24 (DNS server) với RT=65:300

VPN_A import RT=65:300 → nhận 10.100.0.0/24 ✓
VPN_B import RT=65:300 → nhận 10.100.0.0/24 ✓

VPN_A KHÔNG import RT=65:200 → không nhận route của VPN_B ✓
VPN_B KHÔNG import RT=65:100 → không nhận route của VPN_A ✓

→ Shared Service visible to A và B, nhưng A và B vẫn isolated với nhau
```

---

## 7. Luồng Dữ liệu End-to-End: Gói tin Đi như thế nào

### 7.1 Data plane walkthrough chi tiết

Giả sử: Host 10.1.1.10 (CE-A1, Site 1) gửi packet đến 10.2.2.10 (CE-A2, Site 2).

```
Topology:
  CE-A1 ──(eth)── PE-1 ──(MPLS)── P1 ──(MPLS)── P2 ──(MPLS)── PE-2 ──(eth)── CE-A2
  
Label assignments:
  Transport: PE-2 loopback = Label 1001 (LDP) hoặc SID 16002 (SR)
  VPN:       10.2.2.0/24 in VRF_A at PE-1 = Label 2001

═══════════════════════════════════════════════════════════════
STEP 1: CE-A1 → PE-1
═══════════════════════════════════════════════════════════════

CE-A1 gửi IP packet thông thường:
┌──────────────────────────────┐
│ IP Header                    │
│   Src: 10.1.1.10             │
│   Dst: 10.2.2.10             │
│   TTL: 64                    │
├──────────────────────────────┤
│ Payload                      │
└──────────────────────────────┘

PE-1 nhận vào interface GigE0/0 (thuộc VRF Customer_A)
→ Tra VRF Customer_A routing table:
  10.2.2.0/24 → next-hop PE-2, VPN label=2001, transport via MPLS

═══════════════════════════════════════════════════════════════
STEP 2: PE-1 — Label Imposition (áp 2 nhãn)
═══════════════════════════════════════════════════════════════

PE-1 push 2 label (inner first, outer second):
┌──────────────────────────────┐
│ MPLS Label: 1001 [S=0,TTL=63]│  ← Transport label (outer)
│  "Đưa đến PE-2"              │     push bởi PE-1
├──────────────────────────────┤
│ MPLS Label: 2001 [S=1,TTL=63]│  ← VPN label (inner, bottom of stack S=1)
│  "VRF Customer_A tại PE-2"   │     học từ MP-BGP
├──────────────────────────────┤
│ IP: 10.1.1.10 → 10.2.2.10   │
└──────────────────────────────┘

═══════════════════════════════════════════════════════════════
STEP 3: P1 — Transit, chỉ xử lý outer label
═══════════════════════════════════════════════════════════════

P1 nhận:
┌──────────┬──────────┬──────────────────┐
│ L: 1001  │ L: 2001  │ IP Header+Payload│
└──────────┴──────────┴──────────────────┘
  ↑ P1 chỉ đọc label này

P1: MPLS FIB lookup → Label 1001: SWAP→1002, next-hop=P2
┌──────────┬──────────┬──────────────────┐
│ L: 1002  │ L: 2001  │ IP Header+Payload│
└──────────┴──────────┴──────────────────┘

═══════════════════════════════════════════════════════════════
STEP 4: P2 — Penultimate Hop Popping (PHP)
═══════════════════════════════════════════════════════════════

P2 biết PE-2 là next-hop và PE-2 yêu cầu PHP:
→ P2 POP transport label (1002), gửi chỉ VPN label đến PE-2

┌──────────┬──────────────────┐
│ L: 2001  │ IP Header+Payload│  ← Chỉ còn VPN label
└──────────┴──────────────────┘

(Nếu không PHP: PE-2 nhận 2 label, phải double-pop)

═══════════════════════════════════════════════════════════════
STEP 5: PE-2 — Label Disposition (tháo nhãn, forward vào VRF)
═══════════════════════════════════════════════════════════════

PE-2 nhận packet với Label 2001:
→ Tra VPN label table: Label 2001 = VRF Customer_A, interface đến CE-A2
→ POP Label 2001
→ Tra VRF Customer_A: 10.2.2.10 → CE-A2 (direct connected)
→ Forward IP packet

┌──────────────────────────────┐
│ IP Header                    │
│   Src: 10.1.1.10             │
│   Dst: 10.2.2.10             │
│   TTL: 63                    │ ← TTL giảm 1 tại PE (hoặc tùy config)
├──────────────────────────────┤
│ Payload                      │
└──────────────────────────────┘

═══════════════════════════════════════════════════════════════
STEP 6: CE-A2 nhận IP packet thông thường
═══════════════════════════════════════════════════════════════

CE-A2 không biết gì về MPLS, VRF, hay VPN.
Nhận IP packet bình thường, forward đến host 10.2.2.10.
```

### 7.2 TTL behavior trong MPLS VPN

```
TTL propagation modes:

1. Uniform mode (default):
   IP TTL được copy vào MPLS TTL khi push
   MPLS TTL decrement tại mỗi hop
   Khi pop label, MPLS TTL copy ngược lại IP TTL
   → traceroute sẽ thấy các P node → topology visible đến customer

2. Pipe mode:
   IP TTL KHÔNG thay đổi khi đi qua MPLS core
   MPLS TTL hoạt động độc lập, customer không thấy
   → traceroute từ CE chỉ thấy PE-1 và PE-2, không thấy P node
   → Ẩn topology internal của ISP (security, cleaner output)
   
3. Short Pipe mode (phổ biến nhất trong L3VPN):
   Giống Pipe nhưng PE-2 dùng MPLS TTL cho IP TTL update
   → Cân bằng giữa privacy và traceroute functionality

Cấu hình (IOS-XE):
  mpls ip propagate-ttl          ! Uniform mode (default)
  no mpls ip propagate-ttl       ! Pipe mode
```

---

## 8. PE–CE Routing: Các Lựa chọn Giao thức

PE và CE cần trao đổi routing information. Có nhiều lựa chọn, mỗi cái phù hợp với tình huống khác nhau:

### 8.1 Static Route (đơn giản nhất)

```
Khi nào dùng: Khách hàng nhỏ, ít site, ít thay đổi

PE-1 config:
  ip route vrf Customer_A 10.1.0.0 255.255.0.0 192.168.1.2  ! nhớ keyword vrf

CE-A1 config:
  ip route 0.0.0.0 0.0.0.0 192.168.1.1  ! default route về PE

Ưu điểm: Đơn giản, không cần BGP/IGP với CE
Nhược điểm: Không automatic failover, quản lý thủ công
```

### 8.2 BGP (PE-CE BGP) — phổ biến nhất

```
Khi nào dùng: Khách hàng lớn, nhiều site, muốn control routing policy

PE-1 config (IOS-XE):
  router bgp 65000
   address-family ipv4 vrf Customer_A
    neighbor 192.168.1.2 remote-as 65001   ! CE-A1 AS
    neighbor 192.168.1.2 activate
    neighbor 192.168.1.2 as-override       ! nếu CE sites dùng cùng AS
   exit-address-family

CE-A1 config:
  router bgp 65001
   neighbor 192.168.1.1 remote-as 65000   ! PE-1 AS
   network 10.1.0.0 mask 255.255.0.0

Ưu điểm:
  - Full routing policy control (communities, local-pref, MED)
  - AS-path loop prevention built-in
  - Scalable
  
Nhược điểm: CE phải chạy BGP (cần đội ngũ hiểu BGP)

as-override: Khi tất cả CE sites của khách hàng dùng cùng private AS
  → BGP normally reject: thấy own AS trong AS-path
  → as-override: PE replace CE's AS với PE's AS trong updates đến CE sites khác
  → CE nhận được route mà không bị loop prevention block
```

### 8.3 OSPF (PE-CE OSPF)

```
Khi nào dùng: Khách hàng đã dùng OSPF nội bộ, muốn seamless integration

Vấn đề đặc biệt với OSPF: "Backdoor link" và soop problem
  CE-A sites kết nối với nhau qua ISP (PE-CE OSPF)
  Nếu CE-A sites còn có WAN link trực tiếp với nhau (backdoor)
  → OSPF có thể tạo routing loop

Giải pháp: OSPF Sham-link (RFC 4576)
  PE tạo "sham-link" — virtual OSPF link giữa hai PE trong VRF
  → Traffic luôn đi qua MPLS Core, không bị reroute qua backdoor

PE-1 config:
  router ospf 100 vrf Customer_A
   router-id 10.255.255.1
   redistribute bgp 65000 subnets         ! từ MP-BGP vào OSPF
   area 0
    sham-link 10.255.255.1 10.255.255.2  ! OSPF sham-link với PE-2
   !
  !
```

### 8.4 So sánh PE-CE protocols

| Tiêu chí | Static | eBGP | OSPF | EIGRP | RIP |
|---|---|---|---|---|---|
| Độ phức tạp | Thấp | Cao | Trung bình | Trung bình | Thấp |
| Scalability | Kém | Tốt nhất | Tốt | Tốt | Kém |
| Policy control | Không | Đầy đủ | Hạn chế | Hạn chế | Không |
| Convergence | N/A | Trung bình | Nhanh | Nhanh | Chậm |
| Phổ biến | Small CE | Large CE | Medium CE | Cisco-only | Legacy |
| ISP recommend | Simple | Preferred | Common | Possible | Avoid |

---

## 9. Topology VPN Nâng cao: Hub-and-Spoke, Extranet

### 9.1 Hub-and-Spoke với Inter-VRF route leak

```
Advanced Hub-and-Spoke: Centralized Internet Access

Branch sites không có Internet trực tiếp
→ Tất cả Internet traffic phải đi qua HQ (firewall tập trung)
→ HQ inspect và forward

Design:
  Spoke VRF: import RT=65:1 (nhận default route từ Hub)
              export RT=65:2 (quảng bá local subnet)
              
  Hub VRF:   export RT=65:1 (quảng bá default route 0.0.0.0/0)
             import RT=65:2 (nhận subnet của mọi Spoke)
             
  Hub VRF cũng có Internet interface → NAT/firewall tại đây

Traffic flow: Branch → MPLS → Hub (firewall) → Internet
→ Internet traffic của tất cả branch đều đi qua HQ security policy
```

### 9.2 Extranet với Overlapping RT

```
Multi-VPN Shared Service (Complex Extranet):

Company có 3 VPN:
  VPN-PROD: Production servers
  VPN-DEV: Development
  VPN-MGMT: Management (backup, monitoring)

Requirement:
  - MGMT truy cập được PROD và DEV (monitoring)
  - DEV truy cập được PROD (deploy/test)
  - PROD KHÔNG truy cập DEV (bảo mật)
  - PROD và DEV không truy cập lẫn nhau trực tiếp

RT Design:
  VPN-PROD: export RT=65:101   import RT={65:102, 65:103}
  VPN-DEV:  export RT=65:102   import RT={65:101, 65:103}
  VPN-MGMT: export RT=65:103   import RT={65:101, 65:102}

Verify:
  MGMT→PROD: MGMT import 65:101, PROD export 65:101 → ✓
  MGMT→DEV:  MGMT import 65:102, DEV export 65:102 → ✓
  DEV→PROD:  DEV import 65:101, PROD export 65:101 → ✓
  PROD→DEV:  PROD import 65:102?? NO → ✗ (không import 65:102)
  PROD→MGMT: PROD import 65:103, MGMT export 65:103 → ✓ (ngược lại OK)
```

---

## 10. Route Reflector trong L3VPN

### Vấn đề: iBGP full mesh không scale

iBGP yêu cầu full mesh giữa tất cả PE (để tránh loop, iBGP không quảng bá học được từ iBGP peer). Với N PE:

```
Full mesh iBGP sessions = N × (N-1) / 2

N = 10  PE → 45 sessions     (manageable)
N = 50  PE → 1,225 sessions  (khó)
N = 100 PE → 4,950 sessions  (rất khó)
N = 500 PE → 124,750 sessions (impossible)
```

### Route Reflector (RR)

RR là một (hoặc một vài) BGP router đặc biệt phản chiếu VPNv4 update giữa các PE:

```
L3VPN với Route Reflector:

PE-1 ─────┐
PE-2 ─────┤
PE-3 ─────┼──── RR-1 ────┬──── RR-2 (redundancy)
PE-4 ─────┤              │
PE-5 ─────┘              │ (RR-1 và RR-2 full mesh với nhau)
                         │
PE-6 ────────────────────┘
...

Sessions cần thiết:
  Mỗi PE: chỉ cần session đến RR (1-2 sessions)
  RR: N sessions (một với mỗi PE)
  Total: ~2N thay vì N² → scale tuyến tính

Cấu hình RR (IOS-XE):
  router bgp 65000
   neighbor PE_GROUP peer-group
   neighbor PE_GROUP remote-as 65000
   neighbor PE_GROUP update-source Loopback0
   bgp listen range 10.255.255.0/24 peer-group PE_GROUP  ! dynamic PE discovery
   
   address-family vpnv4
    neighbor PE_GROUP activate
    neighbor PE_GROUP route-reflector-client    ! ← key config
    neighbor PE_GROUP send-community extended
   exit-address-family

RR thường là router riêng biệt (không phải PE), thường redundant (2 RR minimum):
  - RR không cần giữ VRF → ít tải hơn PE
  - RR chỉ reflect VPNv4, không terminate VPN customer traffic
  - Thường đặt tại data center hoặc NOC
```

---

## 11. MPLS L3VPN với Segment Routing (SR-MPLS)

### Từ LDP Label đến SR SID

Như đã học trong bài Segment Routing: transport label (outer label) trong L3VPN có thể là LDP label hoặc SR label. VPN label (inner label) không thay đổi.

```
L3VPN + LDP (truyền thống):
┌───────────┬───────────┬─────────────────┐
│ LDP Label │ VPN Label │   IP Payload    │
│ (transport│ (service) │                 │
│  label)   │           │                 │
└───────────┴───────────┴─────────────────┘
  Outer: học từ LDP    Inner: học từ MP-BGP

L3VPN + SR-MPLS (hiện đại):
┌───────────┬───────────┬─────────────────┐
│ SR Label  │ VPN Label │   IP Payload    │
│ (Prefix-  │ (service) │                 │
│  SID)     │           │                 │
└───────────┴───────────┴─────────────────┘
  Outer: Prefix-SID từ IS-IS/OSPF   Inner: học từ MP-BGP (không đổi!)

Migration:
  → Thay thế transport: LDP → SR (change control plane only)
  → VPN service layer: không thay đổi gì!
  → Customer không cảm nhận được sự thay đổi
```

### L3VPN + SR-TE Policy

Kết hợp SR Traffic Engineering với L3VPN cho phép per-VPN traffic engineering:

```
Use case: Khách hàng A có SLA latency <5ms, phải đi đường thấp latency
          Khách hàng B chỉ cần best-effort

Configuration tại PE-1:
  SR Policy (cho Customer_A):
    color: 100 (low-latency)
    endpoint: PE-2
    segment-list: [SID_via_fiber1(low_lat), SID_PE2]
    
  BGP steering:
    Customer_A BGP routes tagged với color community 100
    → Packet match SR Policy color=100 → push SR SID stack (low-lat path)
    → Inner VPN label vẫn giữ nguyên
    
  Customer_B BGP routes: không có color → best-effort IGP path

Packet stack cho Customer_A:
┌───────────┬──────────────┬───────────┬─────────────────┐
│ SR SID    │ SR SID       │ VPN Label │   IP Payload    │
│ (fiber1   │ (PE-2        │ (2001,    │ (Customer A     │
│  node SID)│  Prefix-SID) │  Cust_A)  │  traffic)       │
└───────────┴──────────────┴───────────┴─────────────────┘
  ↑ SR-TE stack        ↑ VPN service label (unchanged)
```

---

## 12. So sánh: L3VPN vs Các Giải pháp VPN Khác

### Bảng so sánh toàn diện

| Tiêu chí | MPLS L3VPN | IPsec VPN | SD-WAN | VXLAN/EVPN | SRv6 L3VPN |
|---|---|---|---|---|---|
| **RFC** | RFC 4364 | RFC 4301 | Proprietary | RFC 7432 | RFC 9252 |
| **Mô hình** | Peer (PE routing) | Overlay | Overlay | Overlay | Peer |
| **Mã hóa** | Không (trusted core) | AES/3DES | Optional (TLS) | Không | Không |
| **Quản lý routing** | ISP (PE-CE) | Khách hàng | Khách hàng | Khách hàng/DC | ISP (PE-CE) |
| **IP overlap** | Có (VRF) | Không tự nhiên | Có (VPN) | Có (VNI) | Có (VRF) |
| **Performance** | Rất cao (HW MPLS) | Trung bình (crypto) | Trung bình | Cao (HW) | Rất cao |
| **TE capability** | Với SR-TE | Không | Có | Hạn chế | Có (SRv6-TE) |
| **Multicast** | Có (MVPN) | Không | Không | Có (BUM) | Có |
| **Scale** | Rất cao | Trung bình | Cao | Cao | Rất cao |
| **Complexity** | Cao | Trung bình | Thấp | Trung bình | Cao |
| **Internet access** | Separate VRF | Inline | Inline | Separate | Separate VRF |
| **Phù hợp** | ISP enterprise | Site-to-site | Branch WAN | DC/Cloud | New ISP core |
| **Mature/Stable** | Rất cao | Rất cao | Trung bình | Cao | Đang phát triển |

### L3VPN vs SD-WAN: Xu hướng thị trường

```
Trend: Enterprise đang migrate từ MPLS L3VPN sang SD-WAN cho WAN edge
       Nhưng MPLS vẫn dùng cho backbone và high-performance applications

MPLS L3VPN còn mạnh ở:
  ✓ Financial services: latency guarantee, security, SLA
  ✓ Healthcare: guaranteed delivery, compliance
  ✓ Large enterprise: nhiều site, cần centralized management
  ✓ Carrier-grade: ISP interconnect, wholesale VPN

SD-WAN chiếm ưu thế ở:
  ✓ SMB/Mid-market: chi phí thấp, dễ triển khai
  ✓ Cloud-heavy workload: trực tiếp Internet access tốt hơn
  ✓ Retail/distributed: nhiều site nhỏ, bandwidth không lớn
  ✓ Agility: provision nhanh, change dễ

Xu hướng: Hybrid — MPLS core + SD-WAN edge overlay
  SD-WAN headend tại PE site → SD-WAN branches → Internet → SD-WAN headend
  MPLS L3VPN vẫn làm backbone giữa các PE/data center
```

---

## 13. Troubleshooting: Phương pháp và Lệnh Thực tế

### 13.1 Framework phân tầng

```
L3VPN Troubleshooting Layers:

Layer 1: Transport (MPLS core reachability)
  Câu hỏi: PE-1 có ping được PE-2 loopback không?
  Công cụ: ping, traceroute, show mpls ldp neighbor

Layer 2: MP-BGP (VPNv4 session và route exchange)
  Câu hỏi: Session up? VPNv4 prefix có được quảng bá/nhận không?
  Công cụ: show bgp vpnv4 unicast, show bgp neighbor

Layer 3: VRF (prefix trong đúng VRF, RT match)
  Câu hỏi: Prefix có trong VRF? RT có khớp không?
  Công cụ: show ip route vrf, show bgp vpnv4 unicast all <prefix>

Layer 4: MPLS label (label allocation và forwarding)
  Câu hỏi: Label được gán đúng? Forwarding table đúng?
  Công cụ: show mpls forwarding-table vrf, show bgp vpnv4 unicast all labels

Layer 5: PE-CE routing (route learning từ CE)
  Câu hỏi: CE quảng bá route vào VRF? Routing protocol up?
  Công cụ: show ip route vrf <name>, show bgp vrf <name>
```

### 13.2 Checklist troubleshooting đầy đủ

```bash
# ===== LAYER 1: Transport =====
# Kiểm tra IGP reachability PE-PE
show ip route 10.255.255.2                  # PE-2 loopback có trong IGP?
ping 10.255.255.2 source loopback0          # Reachable?
traceroute 10.255.255.2 source loopback0    # Đường đi?

# Kiểm tra MPLS label (LDP)
show mpls ldp neighbor                      # LDP session với neighbors?
show mpls ldp bindings 10.255.255.2/32      # Label binding cho PE-2?

# Kiểm tra SR label (nếu dùng SR)
show segment-routing mpls lb detail         # SRGB entries
show mpls forwarding labels 16001 16010     # SR labels forwarding

# ===== LAYER 2: MP-BGP =====
# Kiểm tra BGP session
show bgp vpnv4 unicast all summary          # Tất cả VPNv4 BGP neighbors
show bgp neighbor 10.255.255.2              # Chi tiết session với PE-2
show bgp vpnv4 unicast all                  # Toàn bộ VPNv4 table

# Tìm prefix cụ thể
show bgp vpnv4 unicast all 10.2.2.0/24     # Prefix này từ đâu?
show bgp vpnv4 unicast all 10.2.2.0/24 detail  # Chi tiết: RT, label, path

# Kiểm tra update statistics
show bgp vpnv4 unicast all neighbors 10.255.255.2 routes    # Received
show bgp vpnv4 unicast all neighbors 10.255.255.2 advertised-routes  # Sent

# ===== LAYER 3: VRF =====
# Kiểm tra VRF definition
show vrf                                    # Liệt kê tất cả VRF
show vrf detail Customer_A                  # Chi tiết VRF: RD, RT, interface

# Kiểm tra routing table trong VRF
show ip route vrf Customer_A                # Toàn bộ route trong VRF
show ip route vrf Customer_A 10.2.2.0      # Route cụ thể
show ip route vrf Customer_A bgp           # Chỉ BGP routes
show ip route vrf Customer_A connected     # Chỉ connected routes

# Kiểm tra RT matching
show bgp vpnv4 unicast all 10.2.2.0/24 | include Target  # RT trong BGP update
show vrf detail Customer_A | include Target               # RT của VRF

# ===== LAYER 4: MPLS Labels =====
# Kiểm tra label allocation trong VRF
show mpls forwarding-table vrf Customer_A   # CEF entries với labels
show ip cef vrf Customer_A 10.2.2.0        # CEF entry cho prefix cụ thể

# BGP label thông tin
show bgp vpnv4 unicast all labels           # Labels được quảng bá qua BGP
show bgp vpnv4 unicast vrf Customer_A 10.2.2.0/24  # Label cho prefix cụ thể

# ===== LAYER 5: PE-CE Routing =====
# Nếu dùng BGP với CE
show bgp vrf Customer_A summary             # BGP session với CE
show bgp vrf Customer_A neighbors 192.168.1.2 routes  # Routes từ CE-A

# Nếu dùng OSPF với CE
show ip ospf vrf Customer_A neighbor        # OSPF neighbor state
show ip ospf vrf Customer_A database        # OSPF LSDB

# ===== END-TO-END TEST =====
# Ping trong VRF context
ping vrf Customer_A 10.2.2.10 source 192.168.1.1

# Traceroute trong VRF
traceroute vrf Customer_A 10.2.2.10 source 192.168.1.1

# MPLS ping/traceroute (kiểm tra MPLS path)
ping mpls ipv4 10.255.255.2/32 repeat 5    # Test transport path
traceroute mpls ipv4 10.255.255.2/32       # Trace MPLS path
```

### 13.3 Common Issues và Root Cause

```
Issue 1: Route không xuất hiện trong VRF
  Symptom: show ip route vrf Customer_A → prefix không có
  
  Cause A: RT không khớp
    Debug: show bgp vpnv4 unicast all <prefix> → xem RT trong update
           show vrf detail Customer_A → xem import RT
    Fix: sửa route-target import cho khớp với RT trong BGP update
  
  Cause B: BGP session không active
    Debug: show bgp vpnv4 unicast all summary → neighbor state
    Fix: check BGP config, loopback reachability, AS number
  
  Cause C: Route chưa được redistribute vào BGP
    Debug: show bgp vrf Customer_A → route có trong BGP không?
    Fix: thêm redistribute connected/static/ospf trong address-family vrf

Issue 2: Ping OK nhưng traceroute lạ (extra hop, unexpected path)
  Symptom: traceroute vrf Customer_A 10.2.2.10 → thấy hop bất thường
  
  Cause: SR-TE Policy đang forward khác shortest path
  Debug: show segment-routing traffic-eng policy → active segment list
  Fix: verify SR Policy segment list, kiểm tra color community trên route

Issue 3: VPN label 0 hoặc không có label
  Symptom: show bgp vpnv4 unicast all labels → "nolabel"
  
  Cause: MPLS chưa enable trên interface hoặc VRF chưa enable MPLS
  Debug: show mpls interfaces
  Fix: mpls ip trên các interface, hoặc với IOS-XR: mpls trong interface config

Issue 4: Asymmetric routing (ping OK một chiều, fail chiều kia)
  Symptom: Ping từ Site 1 → Site 2 OK, ngược lại fail
  
  Cause: Route chỉ có một chiều — PE-1 có route đến Site 2, PE-2 không có route về Site 1
  Debug: show ip route vrf Customer_A tại cả hai PE
  Fix: kiểm tra PE-CE routing protocol bidirectional; kiểm tra redistribute
```

---

## 14. Automation: Provision VPN bằng NETCONF/Ansible

### 14.1 Tại sao automation quan trọng với L3VPN

Provision VPN thủ công cho một khách hàng mới:
- Tạo VRF trên nhiều PE (có thể 5-10 PE)
- Cấu hình RD/RT
- Cấu hình BGP address-family per VRF
- Cấu hình PE-CE routing
- Verify end-to-end

Thủ công: 2-4 giờ, cao khả năng typo/lỗi cấu hình. Automation: 5-10 phút, consistent, auditable.

### 14.2 YANG model cho VPN

```yang
// OpenConfig VPN model (rút gọn)
module openconfig-network-instance {
  container network-instances {
    list network-instance {
      key "name";
      
      leaf name {
        type string;            // "Customer_A"
      }
      
      leaf type {
        type identityref {
          base oc-ni-types:NETWORK_INSTANCE_TYPE;
        }
        // L3VRF, DEFAULT_INSTANCE, etc.
      }
      
      container config {
        leaf route-distinguisher {
          type string;         // "65000:100"
        }
      }
      
      container inter-instance-policies {
        container apply-policy {
          leaf-list import-policy {
            type string;       // RT import
          }
          leaf-list export-policy {
            type string;       // RT export
          }
        }
      }
    }
  }
}
```

### 14.3 Ansible Playbook: Provision L3VPN

{% raw %}
```yaml
# provision_l3vpn.yml
---
- name: Provision MPLS L3VPN for new customer
  hosts: pe_routers
  gather_facts: no
  
  vars:
    customer:
      name: "Customer_NewBank"
      id: 1050
      rd: "65000:1050"
      rt_export: "65000:1050"
      rt_import: "65000:1050"
      pe_ce_routing: "bgp"
      ce_as: 65050

  tasks:
    # Step 1: Validate inputs
    - name: Validate RD format
      assert:
        that:
          - customer.rd | regex_search('^[0-9]+:[0-9]+$')
        fail_msg: "RD format invalid: {{ customer.rd }}"
    
    # Step 2: Check if VRF already exists
    - name: Check VRF existence
      ios_command:
        commands: "show vrf {{ customer.name }}"
      register: vrf_check
      ignore_errors: yes
    
    - name: Fail if VRF exists (idempotency check)
      fail:
        msg: "VRF {{ customer.name }} already exists on {{ inventory_hostname }}"
      when: "'VRF-Name' in vrf_check.stdout[0]"
    
    # Step 3: Create VRF via NETCONF
    - name: Create VRF with RD and RT
      netconf_config:
        content: |
          <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
              <vrf>
                <definition>
                  <name>{{ customer.name }}</name>
                  <rd>{{ customer.rd }}</rd>
                  <address-family>
                    <ipv4>
                      <route-target>
                        <export>
                          <asn-ip>{{ customer.rt_export }}</asn-ip>
                        </export>
                        <import>
                          <asn-ip>{{ customer.rt_import }}</asn-ip>
                        </import>
                      </route-target>
                    </ipv4>
                  </address-family>
                </definition>
              </vrf>
            </native>
          </config>
    
    # Step 4: Configure BGP address-family for VRF
    - name: Configure MP-BGP for VRF
      ios_config:
        lines:
          - address-family ipv4 vrf {{ customer.name }}
          - redistribute connected
          - neighbor {{ hostvars[inventory_hostname]['ce_ip'] }} remote-as {{ customer.ce_as }}
          - neighbor {{ hostvars[inventory_hostname]['ce_ip'] }} activate
          - exit-address-family
        parents: router bgp 65000
    
    # Step 5: Verify VRF was created
    - name: Verify VRF creation
      ios_command:
        commands:
          - "show vrf detail {{ customer.name }}"
          - "show bgp vpnv4 unicast all summary"
      register: verify_output
    
    - name: Display verification
      debug:
        var: verify_output.stdout_lines
    
    # Step 6: Log change to CMDB/ticket
    - name: Record provisioning in audit log
      uri:
        url: "https://cmdb.example.com/api/vpn"
        method: POST
        body_format: json
        body:
          customer_name: "{{ customer.name }}"
          customer_id: "{{ customer.id }}"
          rd: "{{ customer.rd }}"
          pe_node: "{{ inventory_hostname }}"
          provisioned_at: "{{ ansible_date_time.iso8601 }}"
          provisioned_by: "{{ lookup('env', 'USER') }}"
        status_code: 201
```
{% endraw %}

### 14.4 Nornir + NETCONF (Python) approach

```python
# provision_vpn.py
from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_edit_config
from nornir_utils.plugins.functions import print_result
import xmltodict
import json

# VPN configuration as data structure
vpn_config = {
    "customer_name": "Customer_NewBank",
    "rd": "65000:1050",
    "rt_export": "65000:1050",
    "rt_import": "65000:1050",
}

def create_vrf_payload(config: dict) -> str:
    """Generate NETCONF XML payload for VRF creation"""
    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <vrf>
          <definition>
            <name>{config['customer_name']}</name>
            <rd>{config['rd']}</rd>
            <address-family>
              <ipv4>
                <route-target>
                  <export>
                    <asn-ip>{config['rt_export']}</asn-ip>
                  </export>
                  <import>
                    <asn-ip>{config['rt_import']}</asn-ip>
                  </import>
                </route-target>
              </ipv4>
            </address-family>
          </definition>
        </vrf>
      </native>
    </config>
    """

def provision_vpn(task, config):
    """Task to provision VPN on a single device"""
    payload = create_vrf_payload(config)
    
    result = task.run(
        task=netconf_edit_config,
        target="running",
        config=payload
    )
    
    return result

# Initialize Nornir with PE inventory
nr = InitNornir(config_file="nornir_config.yaml")

# Filter only PE routers that serve this customer
pe_routers = nr.filter(groups=["pe_routers"])

# Run provisioning
results = pe_routers.run(
    task=provision_vpn,
    config=vpn_config
)

print_result(results)

# Verify
def verify_vrf(task):
    """Verify VRF was created correctly"""
    from nornir_napalm.plugins.tasks import napalm_cli
    result = task.run(
        task=napalm_cli,
        commands=[f"show vrf detail {vpn_config['customer_name']}"]
    )
    return result

verify_results = pe_routers.run(task=verify_vrf)
print_result(verify_results)
```

---

## 15. Lab Mini: Cấu hình L3VPN Đầy đủ

### Topology

```
Lab Topology:

  ┌──────────┐        ┌──────────┐        ┌──────────┐
  │  CE-A1   │        │   PE-1   │        │   PE-2   │        ┌──────────┐
  │10.1.0.0/8│──eth───│ VRF_CustA│──MPLS──│ VRF_CustA│──eth───│  CE-A2   │
  │AS 65001  │        │          │        │          │        │10.2.0.0/8│
  └──────────┘        │          │        │          │        │AS 65001  │
                      │          │        │          │        └──────────┘
  ┌──────────┐        │          │        │          │        ┌──────────┐
  │  CE-B1   │        │ VRF_CustB│        │ VRF_CustB│        │  CE-B2   │
  │10.1.0.0/8│──eth───│          │        │          │──eth───│10.2.0.0/8│
  │AS 65002  │        └────┬─────┘        └─────┬────┘        │AS 65002  │
  └──────────┘             │                    │             └──────────┘
                           └─── Core P ─────────┘
                                (MPLS/SR)
                           
Addresses:
  PE-1 Loopback: 10.255.255.1/32
  PE-2 Loopback: 10.255.255.2/32
  PE-1 ↔ CE-A1: 192.168.1.0/30
  PE-1 ↔ CE-B1: 192.168.2.0/30
  PE-2 ↔ CE-A2: 192.168.3.0/30
  PE-2 ↔ CE-B2: 192.168.4.0/30
  Core P-P: 10.0.0.0/30 range
```

### PE-1 Full Configuration (IOS-XE)

```
! ===== Global MPLS =====
mpls ip
mpls label protocol ldp  ! hoặc dùng SR (xem bài trước)

! ===== IGP (IS-IS hoặc OSPF) =====
router ospf 1
 router-id 10.255.255.1
 passive-interface Loopback0
 network 10.255.255.1 0.0.0.0 area 0  ! loopback
 network 10.0.0.0 0.0.0.255 area 0    ! core links

! ===== VRF Definitions =====
ip vrf Customer_A
 rd 65000:100
 route-target export 65000:100
 route-target import 65000:100

ip vrf Customer_B
 rd 65000:200
 route-target export 65000:200
 route-target import 65000:200

! ===== Interfaces =====
! Loopback (global, for BGP/IGP)
interface Loopback0
 ip address 10.255.255.1 255.255.255.255

! Core link (global, không phải VRF)
interface GigabitEthernet0/0
 description "Link to P router"
 ip address 10.0.0.1 255.255.255.252
 mpls ip
 no shutdown

! CE-facing interfaces (trong VRF)
interface GigabitEthernet0/1
 description "Link to CE-A1"
 ip vrf forwarding Customer_A
 ip address 192.168.1.1 255.255.255.252
 no shutdown

interface GigabitEthernet0/2
 description "Link to CE-B1"
 ip vrf forwarding Customer_B
 ip address 192.168.2.1 255.255.255.252
 no shutdown

! ===== MP-BGP =====
router bgp 65000
 bgp router-id 10.255.255.1
 bgp log-neighbor-changes
 
 ! iBGP session với PE-2
 neighbor 10.255.255.2 remote-as 65000
 neighbor 10.255.255.2 update-source Loopback0
 
 ! VPNv4 address family
 address-family vpnv4
  neighbor 10.255.255.2 activate
  neighbor 10.255.255.2 send-community extended
 exit-address-family
 
 ! VRF Customer_A: BGP với CE-A1
 address-family ipv4 vrf Customer_A
  neighbor 192.168.1.2 remote-as 65001
  neighbor 192.168.1.2 activate
  redistribute connected
 exit-address-family
 
 ! VRF Customer_B: static redistribute
 address-family ipv4 vrf Customer_B
  neighbor 192.168.2.2 remote-as 65002
  neighbor 192.168.2.2 activate
  redistribute connected
 exit-address-family

! ===== Verification =====
! show ip vrf detail
! show ip route vrf Customer_A
! show bgp vpnv4 unicast all summary
! show bgp vpnv4 unicast all
! show mpls forwarding-table vrf Customer_A
```

### PE-2 Configuration (IOS-XR — khác syntax)

```
! IOS-XR syntax

! ===== VRF =====
vrf Customer_A
 address-family ipv4 unicast
  import route-target 65000:100
  export route-target 65000:100
!
vrf Customer_B
 address-family ipv4 unicast
  import route-target 65000:200
  export route-target 65000:200
!

! ===== Interface =====
interface Loopback0
 ipv4 address 10.255.255.2 255.255.255.255
!
interface GigabitEthernet0/0/0/0
 description "Link to P"
 ipv4 address 10.0.0.5 255.255.255.252
 mpls ip
!
interface GigabitEthernet0/0/0/1
 description "Link to CE-A2"
 vrf Customer_A
 ipv4 address 192.168.3.1 255.255.255.252
!
interface GigabitEthernet0/0/0/2
 description "Link to CE-B2"
 vrf Customer_B
 ipv4 address 192.168.4.1 255.255.255.252
!

! ===== MP-BGP =====
router bgp 65000
 bgp router-id 10.255.255.2
 
 neighbor 10.255.255.1
  remote-as 65000
  update-source Loopback0
  address-family vpnv4 unicast
   !
  !
 !
 
 vrf Customer_A
  rd 65000:100
  address-family ipv4 unicast
   redistribute connected
   !
   neighbor 192.168.3.2
    remote-as 65001
    !
  !
 !
 
 vrf Customer_B
  rd 65000:200
  address-family ipv4 unicast
   redistribute connected
   neighbor 192.168.4.2
    remote-as 65002
    !
  !
 !
!
```

### CE-A1 Configuration (simple)

```
! CE-A1 (Customer A, Site 1)
interface GigabitEthernet0/0
 description "Link to PE-1"
 ip address 192.168.1.2 255.255.255.252
 no shutdown

interface Loopback0
 ip address 10.1.1.1 255.255.255.255  ! simulate customer network

router bgp 65001
 bgp router-id 10.1.1.1
 neighbor 192.168.1.1 remote-as 65000   ! PE-1
 
 address-family ipv4
  neighbor 192.168.1.1 activate
  network 10.1.0.0 mask 255.255.0.0     ! quảng bá customer subnet
  network 10.1.1.1 mask 255.255.255.255
 exit-address-family
```

---

## 16. Glossary

| Thuật ngữ | Tiếng Anh đầy đủ | Giải nghĩa ngắn gọn |
|---|---|---|
| L3VPN | Layer 3 VPN | VPN lớp 3, ISP định tuyến thay customer |
| VRF | Virtual Routing and Forwarding | Instance định tuyến độc lập trên router |
| RD | Route Distinguisher | 64-bit prefix để làm VPN route unique trong BGP |
| RT | Route Target | BGP Extended Community kiểm soát import/export route |
| VPNv4 | VPN IPv4 | AFI/SAFI dùng trong MP-BGP: RD+IPv4 prefix |
| MP-BGP | Multiprotocol BGP | BGP mở rộng hỗ trợ nhiều address family |
| CE | Customer Edge | Router của khách hàng, không biết về MPLS/VPN |
| PE | Provider Edge | Router biên ISP, xử lý VRF/RD/RT/MP-BGP |
| P | Provider Core | Router lõi ISP, chỉ forward transport label |
| Transport Label | - | Outer MPLS label, đưa packet từ PE đến PE |
| VPN Label | - | Inner MPLS label, PE egress biết VRF nào |
| Label Imposition | - | PE ingress push cả 2 label vào packet |
| Label Disposition | - | PE egress pop label, forward vào VRF |
| PHP | Penultimate Hop Popping | P node pop outer label trước khi đến PE |
| SAFI | Subsequent Address Family Identifier | Phân loại address family trong MP-BGP |
| Extended Community | BGP Extended Community | 8-byte BGP attribute, dùng để mang RT |
| VRF-Lite | - | VRF không có MPLS, chỉ tách routing table |
| Route Leak | - | Chia sẻ route giữa hai VRF có chủ đích |
| Hub-and-Spoke | - | Topology VPN: Spoke chỉ nói chuyện qua Hub |
| Extranet | - | Chia sẻ resource có kiểm soát giữa các VPN |
| MVPN | Multicast VPN | L3VPN hỗ trợ multicast traffic |
| as-override | - | PE thay CE AS trong BGP AS-path để tránh loop |
| Sham-link | - | Virtual OSPF link giữa PE trong VRF để prevent backdoor |
| RR | Route Reflector | BGP router phản chiếu update, thay thế full-mesh iBGP |
| CMDB | Configuration Management Database | DB lưu inventory và configuration |

---

## 17. Tài liệu Tham khảo

### RFCs Nền tảng
- **RFC 4364** — BGP/MPLS IP Virtual Private Networks (L3VPN) — tài liệu gốc, bắt buộc đọc
- **RFC 4360** — BGP Extended Communities Attribute — định nghĩa RT format
- **RFC 4760** — Multiprotocol Extensions for BGP-4 (MP-BGP)
- **RFC 3107** — Carrying Label Information in BGP-4 — VPN label trong BGP
- **RFC 4576** — Using a Link State Advertisement Options Bit to Prevent Looping in BGP/MPLS IP VPNs
- **RFC 4577** — OSPF as the Provider/Customer Edge Protocol for BGP/MPLS IP VPNs (OSPF PE-CE)
- **RFC 4271** — A Border Gateway Protocol 4 (BGP-4) — BGP cơ bản

### RFC Liên quan
- **RFC 4456** — BGP Route Reflection: An Alternative to Full Mesh Internal BGP
- **RFC 2547** — BGP/MPLS VPNs — phiên bản gốc, đã được RFC 4364 thay thế (đọc để hiểu lịch sử)
- **RFC 9252** — BGP Overlay Services Based on Segment Routing over IPv6 (SRv6) — SRv6 L3VPN

### Vendor Documentation
- **Cisco MPLS L3VPN Configuration Guide** (IOS-XE)
- **Cisco IOS-XR MPLS VPN Configuration Guide**
- **Juniper MPLS L3VPN Feature Guide** (Junos)
- **Nokia MPLS L3VPN Configuration Guide** (SR-OS)
- **Arista MPLS L3VPN EOS Guide**

### Sách Kinh điển
- *MPLS and VPN Architectures, Volume I & II* — Ivan Pepelnjak & Jim Guichard (Cisco Press)
- *MPLS-Enabled Applications* — Ina Minei & Julian Lucek (Wiley)
- *BGP Design and Implementation* — Randy Zhang & Micah Bartell

### Online Resources
- **Cisco Learning Network** — MPLS L3VPN labs và configurations
- **Juniper Learning Portal** — L3VPN implementation guides
- **NANOG / RIPE NCC** — Operator presentations về L3VPN deployment

---

*Bài viết phản ánh trạng thái công nghệ tính đến mid-2026. MPLS L3VPN (RFC 4364) là chuẩn mực ổn định đã trên 20 năm — core concepts không thay đổi. Xu hướng mới: SRv6 L3VPN đang tăng adoption, và SD-WAN overlay đang thay thế L3VPN tại edge trong nhiều deployment.*

*Tác giả: IP/Core Network Engineer — Series "Networking from the Ground Up"*


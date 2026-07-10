---
layout: page-toc
title: "IS-IS User Guide Juniper/Junos"
permalink: /writeups/learn-juniper/isis-user-guide/
toc: true
---
# IS-IS User Guide Juniper/Junos — Toàn bộ lý thuyết theo từng mục

> Nguồn tham khảo chính: Juniper Networks — **IS-IS User Guide for Junos OS**  
> Link: <https://www.juniper.net/documentation/us/en/software/junos/is-is/index.html>  
> Bản PDF chính thức: <https://www.juniper.net/documentation/us/en/software/junos/is-is/is-is.pdf>

---

## Sơ đồ nhớ tổng quát IS-IS

```text
IS-IS
 |
 |-- 1. Overview
 |      |-- Link-state IGP
 |      |-- SPF / Dijkstra
 |      |-- Level 1 / Level 2
 |      |-- NET / NSAP / System ID
 |      |-- IIH / LSP / CSNP / PSNP
 |
 |-- 2. Configuration
 |      |-- Basic IS-IS
 |      |-- Area / Level / DIS
 |      |-- Authentication / Checksum
 |      |-- Policy / Redistribution / Route leaking
 |      |-- BFD
 |      |-- Flooding
 |      |-- IPv6 / Multi-topology
 |      |-- LFA / Fast reroute
 |      |-- Traffic Engineering / MPLS
 |      |-- Segment Routing / SRv6
 |      |-- Scaling / Throttling
 |
 |-- 3. Monitoring & Troubleshooting
 |      |-- show isis adjacency
 |      |-- show isis interface
 |      |-- show isis database
 |      |-- show route protocol isis
 |      |-- traceoptions
 |
 |-- 4. CLI Reference
```

Công thức dễ nhớ nhất:

```text
NET → family iso → IIH Hello → Adjacency → LSP → LSDB → SPF → Route → Forwarding
```

---

# 1. Overview — Tổng quan IS-IS

## 1.1 IS-IS là gì?

**IS-IS — Intermediate System to Intermediate System** là một giao thức định tuyến nội bộ **IGP — Interior Gateway Protocol**, thuộc nhóm **link-state**.

Nghĩa là router không chỉ học route từ hàng xóm như distance-vector, mà nó xây dựng một “bản đồ mạng” dựa trên thông tin link-state rồi dùng thuật toán **SPF / Dijkstra** để tính đường đi ngắn nhất.

Juniper mô tả IS-IS dùng SPF để xác định route và có thể chạy:

- **Full SPF**: tính lại toàn bộ cây đường đi ngắn nhất.
- **PRC — Partial Route Calculation**: chỉ tính lại một phần khi topology thay đổi nhỏ.

Nhớ đơn giản:

```text
IS-IS = Router tự vẽ bản đồ mạng → chạy SPF → chọn đường tốt nhất
```

Ứng dụng thực tế:

```text
ISP / Core IP / MPLS Backbone / Data Center / Segment Routing / IPv6 Core
```

IS-IS thường dùng trong mạng core vì:

- Scale tốt.
- Ổn định trong mạng lớn.
- Hỗ trợ IPv4, IPv6, MPLS, Segment Routing.
- Không phụ thuộc vào IP để thiết lập neighbor.
- Phù hợp mạng ISP/Core cần hội tụ nhanh.

---

## 1.2 IS-IS Terminology — Thuật ngữ

Trong IS-IS, một mạng được xem như một **routing domain**. Routing domain có thể chia thành nhiều **area**.

Các thuật ngữ cơ bản:

| Thuật ngữ | Ý nghĩa |
|---|---|
| End System | Thiết bị đầu cuối, host, server |
| Intermediate System | Router |
| Routing Domain | Toàn bộ miền định tuyến IS-IS |
| Area | Vùng định tuyến trong IS-IS domain |
| Level 1 | Định tuyến trong cùng area |
| Level 2 | Định tuyến giữa các area |
| L1/L2 | Router biên nối Level 1 với Level 2 |
| PDU | Protocol Data Unit, gói điều khiển của IS-IS |

Nhớ nhanh:

```text
End System          = host / endpoint
Intermediate System = router
Area                = vùng trong IS-IS domain
Level 1             = route trong area
Level 2             = route giữa area
L1/L2               = router biên giữa L1 và L2
```

---

## 1.3 Level 1, Level 2, L1/L2

Sơ đồ:

```text
                 LEVEL 2 BACKBONE / CORE
          R3 L1/L2 ---------------- R4 L1/L2
             |                          |
             |                          |
       AREA 49.0001                AREA 49.0002
             |                          |
           R1 L1                      R5 L1
           R2 L1
```

Ý nghĩa thực tế:

```text
Level 1  = định tuyến nội bộ trong một area
Level 2  = định tuyến giữa nhiều area
L1/L2    = router biên, vừa nói chuyện với L1 vừa nói chuyện với L2
```

Ví dụ doanh nghiệp/ISP:

```text
Router chi nhánh / access     → Level 1
Router core / backbone        → Level 2
Router nối chi nhánh với core → L1/L2
```

Level boundary quyết định phạm vi lan truyền link-state update.

- Router Level 1 giữ LSDB Level 1.
- Router Level 2 giữ LSDB Level 2.
- Router L1/L2 giữ cả LSDB Level 1 và Level 2.

---

# 2. ISO Network Address — NET / NSAP / System ID

IS-IS không dùng IP để định danh router giống OSPF. Nó dùng địa chỉ ISO.

## 2.1 NSAP

**NSAP — Network Service Access Point** là địa chỉ ISO xác định một điểm kết nối vào mạng.

## 2.2 NET

**NET — Network Entity Title** có cấu trúc giống NSAP nhưng byte cuối cùng, gọi là **N-selector**, luôn là `00`.

Trong Junos, NET thường đặt trên interface loopback `lo0`.

Ví dụ NET:

```text
49.0001.1921.6800.1001.00
```

Tách ra:

```text
49        .0001      .1921.6800.1001      .00
|          |          |                    |
AFI        Area ID    System ID            Selector
```

Nhớ:

```text
NET = Area ID + System ID + 00
```

Trong đó:

| Phần | Ý nghĩa |
|---|---|
| AFI | Authority and Format Identifier |
| Area ID | Router thuộc area nào |
| System ID | Định danh duy nhất của router |
| Selector | Thường là `00` với NET |

System ID phải **unique trong domain**.

Lưu ý quan trọng:

```text
System ID không được là 0000.0000.0000
```

Nếu System ID toàn số 0, adjacency sẽ không hình thành.

---

## 2.3 Cách tạo NET dễ nhớ

Ví dụ router có loopback:

```text
1.1.1.1
```

Có thể tạo System ID dạng:

```text
0000.0000.0001
```

NET hoàn chỉnh:

```text
49.0001.0000.0000.0001.00
```

Ví dụ nhiều router cùng area:

```text
R1: 49.0001.0000.0000.0001.00
R2: 49.0001.0000.0000.0002.00
R3: 49.0001.0000.0000.0003.00
```

Ví dụ khác area:

```text
R1: 49.0001.0000.0000.0001.00
R2: 49.0001.0000.0000.0002.00
R3: 49.0002.0000.0000.0003.00
```

---

# 3. IS-IS Packets / PDU

IS-IS dùng các gói điều khiển gọi là **PDU — Protocol Data Unit**.

```text
IS-IS PDU
 |
 |-- IIH   = Hello, tạo neighbor
 |-- LSP   = Link-State PDU, mang thông tin topology
 |-- CSNP  = Complete Sequence Number PDU, danh sách full LSDB
 |-- PSNP  = Partial Sequence Number PDU, xin/ACK LSP còn thiếu
```

---

## 3.1 IIH — IS-IS Hello

**IIH — IS-IS Hello** dùng để:

- Phát hiện neighbor.
- Duy trì adjacency.
- Kiểm tra level tương thích.
- Kiểm tra area đối với Level 1.
- Kiểm tra authentication nếu có.

IS-IS có hello cho:

```text
Point-to-point link
Level 1 broadcast link
Level 2 broadcast link
```

Điều kiện quan trọng:

```text
Level 1 adjacency  → phải cùng area
Level 2 adjacency  → không bắt buộc cùng area
```

Nhớ:

```text
IIH = gói Hello để router “bắt tay” với nhau
```

---

## 3.2 LSP — Link-State PDU

**LSP — Link-State PDU** chứa:

- Router ID/System ID.
- Interface/link information.
- Neighbor information.
- Metric.
- Prefix IPv4/IPv6.
- Các TLV mở rộng như TE, SR, SRv6.

Router flood LSP cho các router cùng level để mọi router có cùng bản đồ LSDB.

Nhớ:

```text
LSP = bản đồ topology mà router gửi cho toàn mạng
```

---

## 3.3 CSNP — Complete Sequence Number PDU

**CSNP** chứa danh sách đầy đủ các LSP trong database.

Dùng để:

- Đồng bộ LSDB.
- Kiểm tra router có thiếu LSP nào không.
- Hỗ trợ flooding trên broadcast network.

Nhớ:

```text
CSNP = danh sách full database
```

---

## 3.4 PSNP — Partial Sequence Number PDU

**PSNP** dùng để:

- Yêu cầu LSP còn thiếu.
- ACK LSP trên point-to-point link.

Nhớ:

```text
PSNP = xin phần còn thiếu hoặc xác nhận đã nhận LSP
```

---

# 4. Basic IS-IS Configuration trên Junos

Đây là phần cực kỳ quan trọng khi làm lab.

Để cấu hình IS-IS trên Junos, cần:

```text
1. Cấu hình NET address, nên đặt trên lo0.
2. Bật family iso trên các interface chạy IS-IS.
3. Khai báo interface trong protocols isis.
4. Kiểm tra level nếu cần L1 hoặc L2 riêng.
```

Khi enable IS-IS trên interface, Junos mặc định bật cả:

```text
Level 1 và Level 2
```

---

## 4.1 Cấu hình tối thiểu

Ví dụ R1:

```bash
set interfaces ge-0/0/0 unit 0 family inet address 10.0.12.1/30
set interfaces ge-0/0/0 unit 0 family iso

set interfaces lo0 unit 0 family inet address 1.1.1.1/32
set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0001.00

set protocols isis interface ge-0/0/0.0
set protocols isis interface lo0.0
commit
```

Giải thích:

```text
family inet = chạy IP
family iso  = chạy IS-IS
lo0 NET     = định danh router
protocols isis interface = bật IS-IS trên interface
```

---

## 4.2 Vì sao cần family iso?

IS-IS chạy trực tiếp trên Layer 2, không chạy trên IP như OSPF.

Vì vậy interface muốn gửi/nhận IS-IS PDU phải bật:

```bash
family iso
```

Nếu thiếu `family iso`, neighbor IS-IS sẽ không lên.

---

## 4.3 Vì sao cần lo0?

`lo0` thường dùng để đặt:

- IP loopback.
- NET address.
- Router identity ổn định.

Trong IS-IS trên Junos, `lo0` thường passive mặc định: nó được advertise nhưng không gửi/nhận hello.

---

# 5. IS-IS Areas và Multi-Level Topology

IS-IS dùng area để chia routing domain lớn thành nhiều vùng nhỏ.

Lý do chia area:

- Giảm LSDB size.
- Giảm flooding.
- Giảm SPF calculation.
- Dễ scale mạng core lớn.

```text
Level 1 router:
- Chỉ biết route trong area.
- Muốn đi ra ngoài area thì đi tới L1/L2 gần nhất.

Level 2 router:
- Biết route liên area.
- Dùng trong core/backbone.

L1/L2 router:
- Vừa giữ LSDB Level 1.
- Vừa giữ LSDB Level 2.
- Là điểm nối giữa area nội bộ và core.
```

---

## 5.1 Mô hình multi-level thực tế

```text
                      Level 2 Core
             R3 --------------------- R4
             |                         |
           L1/L2                     L1/L2
             |                         |
       Area 49.0001              Area 49.0002
        R1 ----- R2                R5 ----- R6
```

Ý nghĩa:

```text
R1/R2/R5/R6 = Level 1 router
R3/R4       = L1/L2 hoặc Level 2 core router
```

---

# 6. Default Route trong IS-IS

Level 1 router không cần biết toàn bộ route ngoài area.

Khi L1/L2 router biết nó có thể reach area khác, nó set **ATTACHED bit** trong LSP Level 1.

Sau đó router Level 1 có thể cài default route về router L1/L2 gần nhất.

Sơ đồ:

```text
R1 L1 ---- R2 L1/L2 ---- R3 L2 ---- Area khác
 |
 | muốn đi ra ngoài area
 v
đi default route về R2
```

Nhớ:

```text
L1 không biết hết bên ngoài
L1 chỉ cần biết đường ra L1/L2
```

Ứng dụng thực tế:

```text
Area access không cần giữ full route core
Chỉ cần default route ra core
Giảm bảng định tuyến và LSDB trong area nhỏ
```

---

# 7. DIS — Designated Intermediate System

Trên mạng broadcast Ethernet, IS-IS bầu **DIS — Designated Intermediate System**.

DIS giúp:

- Đại diện LAN segment trong LSDB.
- Tối ưu flooding trên broadcast network.
- Giảm số lượng adjacency/flooding dư thừa.

Sơ đồ:

```text
Broadcast LAN
 |
 |-- R1
 |-- R2  ← DIS
 |-- R3
```

DIS được chọn dựa trên:

```text
Priority cao hơn thắng
Nếu priority bằng nhau, MAC address cao hơn thắng
```

Ví dụ cấu hình priority:

```bash
set protocols isis interface ge-0/0/0.0 level 1 priority 100
set protocols isis interface ge-0/0/0.0 level 2 priority 100
```

Khác OSPF:

```text
OSPF có DR/BDR
IS-IS chỉ có DIS, không có BDR giống OSPF
```

---

# 8. Authentication và Checksum

## 8.1 IS-IS Authentication

IS-IS authentication đảm bảo chỉ router tin cậy mới tham gia routing domain.

Mặc định authentication bị tắt.

Có thể dùng:

```text
Simple authentication
HMAC-MD5
Keychain / hitless key rollover
```

Simple authentication gửi password dạng text nên không an toàn nếu bị sniff.

Mẫu cấu hình global:

```bash
set protocols isis authentication-type md5
set protocols isis authentication-key "PASSWORD"
```

Mẫu cấu hình theo interface:

```bash
set protocols isis interface ge-0/0/0.0 authentication-type md5
set protocols isis interface ge-0/0/0.0 authentication-key "PASSWORD"
```

Ứng dụng thực tế:

```text
Không bật auth:
Router lạ có thể join routing domain nếu đấu vào mạng.

Bật auth:
Chỉ router có cùng key mới tạo adjacency.
```

---

## 8.2 Hitless Authentication Key Rollover

Hitless key rollover dùng để đổi key authentication mà không làm rớt neighbor.

Cách hoạt động:

```text
Tạo keychain
Cấu hình nhiều key
Mỗi key có start-time
Đến thời điểm mới, router chuyển key
Adjacency không bị reset
```

Ứng dụng:

```text
Mạng production cần đổi key định kỳ
Không muốn mất adjacency khi thay password
```

---

## 8.3 Checksum

Checksum dùng để kiểm tra lỗi trong PDU.

Mục đích:

- Phát hiện lỗi control packet.
- Tăng độ tin cậy trong môi trường core.
- Hỗ trợ troubleshooting khi có lỗi bất thường.

---

# 9. Routing Policy, Redistribution, Route Leaking

Đây là phần cực kỳ quan trọng trong thực tế vận hành Junos.

---

## 9.1 Routing policy trong Junos

Junos dùng policy để kiểm soát route vào/ra protocol.

Nhớ:

```text
Import = protocol → routing table
Export = routing table → protocol
```

Trong Junos:

- Route từ protocol đi vào routing table thông qua import policy.
- Route từ routing table được advertise ra protocol thông qua export policy.

Ví dụ static route đưa vào IS-IS:

```bash
set policy-options policy-statement EXPORT-STATIC from protocol static
set policy-options policy-statement EXPORT-STATIC then accept
set protocols isis export EXPORT-STATIC
```

---

## 9.2 Redistribution

Redistribution là đưa route từ protocol khác vào IS-IS.

Ví dụ:

```text
OSPF   → IS-IS
BGP    → IS-IS
Static → IS-IS
Direct → IS-IS
```

Ứng dụng thực tế:

```text
Mạng có nhiều protocol
Cần đưa route static/direct vào core IS-IS
Cần migrate OSPF sang IS-IS
Cần redistribute route từ BGP vào IGP có kiểm soát
```

Lưu ý:

```text
Không redistribute bừa bãi
Phải dùng policy để tránh route loop hoặc làm bảng route quá lớn
```

---

## 9.3 Route leaking

Route leaking là truyền route giữa Level 1 và Level 2.

Nhớ:

```text
L1 → L2: mặc định có
L2 → L1: cần policy
```

Ứng dụng thực tế:

```text
Level 1 area thường chỉ cần default route.
Nhưng nếu L1 cần biết một prefix cụ thể từ core,
ta dùng route leaking L2 → L1.
```

Ví dụ policy leak L2 xuống L1:

```bash
set policy-options policy-statement LEAK-L2-TO-L1 from protocol isis
set policy-options policy-statement LEAK-L2-TO-L1 from level 2
set policy-options policy-statement LEAK-L2-TO-L1 to protocol isis
set policy-options policy-statement LEAK-L2-TO-L1 to level 1
set policy-options policy-statement LEAK-L2-TO-L1 then accept
set protocols isis export LEAK-L2-TO-L1
```

---

# 10. Route Tagging và Route Priority

## 10.1 Route Tagging

IS-IS có thể gắn tag/attribute vào route.

Route tag dùng để:

- Match route trong policy.
- Kiểm soát import/export.
- Kiểm soát route leaking.
- Đánh dấu route từ nguồn cụ thể.

Ứng dụng thực tế:

```text
Tag route khách hàng quan trọng
→ policy ưu tiên hoặc leak riêng
→ kiểm soát route tốt hơn trong mạng lớn
```

---

## 10.2 Route Priority

Route priority giúp ưu tiên xử lý/cập nhật những route quan trọng khi topology thay đổi.

Ứng dụng:

```text
ISP muốn route khách hàng quan trọng hội tụ nhanh hơn
Mạng lớn cần tối ưu convergence
```

---

# 11. Overload

Overload dùng khi router không muốn làm transit router.

Ý nghĩa:

```text
Router vẫn tham gia IS-IS
Nhưng báo với mạng: đừng dùng tôi làm đường transit
```

Ứng dụng thực tế:

```text
Maintenance router core
Router mới khởi động lại
Router chưa sync BGP/MPLS/LDP xong
Router thiếu tài nguyên hoặc có vấn đề
```

Cấu hình cơ bản:

```bash
set protocols isis overload
```

Cấu hình overload có timeout:

```bash
set protocols isis overload timeout 300
```

Hiểu đơn giản:

```text
Overload = vẫn sống trong IS-IS nhưng không muốn gánh traffic transit
```

---

# 12. BFD cho IS-IS

**BFD — Bidirectional Forwarding Detection** là cơ chế phát hiện lỗi nhanh hơn timer IS-IS thông thường.

BFD gửi hello định kỳ. Nếu router không nhận reply sau khoảng thời gian định trước thì xác định neighbor/link bị lỗi.

Sơ đồ:

```text
IS-IS adjacency up
        |
        v
BFD session chạy song song
        |
        v
Link/neighbor lỗi
        |
        v
BFD báo down rất nhanh
        |
        v
IS-IS tính lại route
```

Mẫu cấu hình:

```bash
set protocols isis interface ge-0/0/0.0 bfd-liveness-detection minimum-interval 300
set protocols isis interface ge-0/0/0.0 bfd-liveness-detection multiplier 3
```

Ứng dụng thực tế:

```text
Core network cần hội tụ nhanh
MPLS / ISP backbone
Link quan trọng cần phát hiện lỗi nhanh
```

---

## 12.1 BFD Authentication

BFD authentication giúp bảo vệ BFD session khỏi giả mạo.

Nên dùng khi:

```text
BFD chạy qua tunnel
BFD chạy qua mạng không tin cậy
Mạng production cần bảo mật control plane
```

---

# 13. Flood Group và Flood Reflector

IS-IS dùng flooding để lan truyền LSP. Mạng càng lớn thì flooding càng nhiều, dễ tạo overhead.

---

## 13.1 Flood Group

Flood group giới hạn việc flood LSP trên IS-IS interfaces.

Nhớ:

```text
Flooding bình thường:
LSP lan rộng nhiều hướng

Flood group:
Giới hạn hướng flood LSP
```

Ứng dụng thực tế:

```text
Mạng lớn
Nhiều router core
Cần giảm overhead flooding
Cần tối ưu convergence
```

---

## 13.2 Flood Reflector

Flood reflector dùng để giảm flooding path, tối ưu hội tụ, tăng hiệu quả mạng và scale tốt hơn trong topology lớn.

Nhớ:

```text
Flood reflector = phản xạ LSP ở control plane
Không phải đường forward data traffic
```

Ứng dụng:

```text
Large-scale IS-IS domain
Mạng core nhiều node
Cần giảm flooding mesh phức tạp
```

---

# 14. IPv6, Dual Stack và Multi-Topology

## 14.1 Dual Stack IPv4/IPv6

IS-IS hỗ trợ cả IPv4 và IPv6.

Vì IS-IS dùng ISO address nên cách cấu hình IPv4 và IPv6 IS-IS về nền tảng là giống nhau.

Cần có:

```text
family iso cho IS-IS
family inet cho IPv4
family inet6 cho IPv6
```

---

## 14.2 Multi-Topology

Multi-topology cho phép IPv4 và IPv6 có topology/metric riêng.

Ví dụ:

```text
IPv4 topology đi đường A
IPv6 topology đi đường B
```

Ứng dụng thực tế:

```text
Mạng chuyển đổi IPv4 → IPv6
IPv6 chưa chạy trên tất cả link
Cần metric IPv4 và IPv6 khác nhau
Cần multicast/unicast topology riêng
```

---

# 15. Link Protection, Node-Link Protection, LFA

**LFA — Loop-Free Alternate** là cơ chế fast reroute.

Junos precompute backup route cho các IS-IS route và cài sẵn vào Packet Forwarding Engine.

Khi primary next-hop lỗi, PFE local repair ngay, trước khi Routing Engine tính xong route mới.

Sơ đồ:

```text
Primary path:
R1 ---- R2 ---- R4

Backup path đã tính sẵn:
R1 ---- R3 ---- R4
```

Khi link R1-R2 lỗi:

```text
PFE chuyển traffic sang R1-R3-R4 gần như ngay lập tức
```

---

## 15.1 Link Protection

Bảo vệ khi **link** lỗi.

```bash
set protocols isis interface ge-0/0/0.0 link-protection
```

---

## 15.2 Node-Link Protection

Bảo vệ khi cả **neighbor node** lỗi.

```bash
set protocols isis interface ge-0/0/0.0 node-link-protection
```

Ứng dụng thực tế:

```text
ISP core
MPLS backbone
Mạng yêu cầu downtime rất thấp
```

---

# 16. Remote LFA và Weighted ECMP

## 16.1 Remote LFA

Remote LFA mở rộng khả năng backup path khi local LFA không đủ coverage.

Thường dùng với:

```text
LDP tunnel
MPLS network
Large core topology
```

Ứng dụng:

```text
Local LFA không tìm được backup path
Remote LFA dùng tunnel tới node phù hợp để bảo vệ traffic
```

---

## 16.2 Weighted ECMP

Weighted ECMP cho phép chia tải không đều giữa các next-hop.

Thay vì chia đều 50/50, có thể chia theo weight.

Ứng dụng thực tế:

```text
2 link không cùng capacity:
Link 10G nhận nhiều traffic hơn link 1G
```

Ví dụ ý tưởng:

```text
Link A = 10G → weight cao
Link B = 1G  → weight thấp
Traffic chia theo tỷ lệ phù hợp
```

---

# 17. Traffic Engineering với IS-IS

IS-IS hỗ trợ **Traffic Engineering — TE** bằng cách thêm TLV mang link attributes vào LSP.

Các thông tin TE có thể gồm:

- Link bandwidth.
- TE metric.
- Administrative group/color.
- SRLG.
- Delay/link attributes.

Luồng thực tế:

```text
IS-IS TE TLV
     |
     v
Traffic Engineering Database
     |
     v
CSPF tính đường theo constraint
     |
     v
RSVP setup MPLS LSP
     |
     v
Traffic đi theo tunnel TE
```

Ứng dụng:

```text
MPLS Traffic Engineering
ISP muốn ép traffic đi theo đường cụ thể
Tránh link nghẽn
Reserve bandwidth cho service quan trọng
```

---

# 18. IGP Shortcut và Forwarding Adjacency

## 18.1 IGP Shortcut

IS-IS có thể dùng MPLS LSP như next-hop logic, giống như có một “interface ảo” từ ingress router tới egress router.

Hiểu đơn giản:

```text
Có MPLS LSP từ R1 tới R5
IS-IS có thể xem LSP này như một đường đi logic
```

Ứng dụng:

```text
Tận dụng MPLS TE tunnel để cải thiện đường đi IGP
```

---

## 18.2 Forwarding Adjacency

Forwarding adjacency là advertise MPLS LSP vào IS-IS như một link trong topology.

Khi đó SPF có thể xem tunnel như một đường đi.

Ứng dụng thực tế:

```text
Core có MPLS TE tunnel
Muốn IGP biết tunnel đó như một link logic
```

---

# 19. Wide Metrics

Wide metrics dùng khi cần metric lớn hơn và cần hỗ trợ TE/SR.

Trong mạng core hiện đại, thường dùng wide metrics vì narrow metric cũ không đủ linh hoạt.

Mẫu cấu hình:

```bash
set protocols isis level 1 wide-metrics-only
set protocols isis level 2 wide-metrics-only
```

Ứng dụng:

```text
MPLS TE
Segment Routing
Core network có metric lớn/phức tạp
```

Nhớ:

```text
Wide metric = metric mở rộng cho mạng core hiện đại
```

---

# 20. LDP-IGP Synchronization

LDP-IGP synchronization dùng để tránh blackhole khi IGP đã chọn link nhưng LDP label chưa sẵn sàng.

Sơ đồ lỗi nếu không sync:

```text
IGP thấy link up
→ traffic MPLS đi vào link
→ nhưng LDP label chưa có
→ blackhole
```

Có sync:

```text
LDP chưa ready
→ IS-IS tăng metric / tránh dùng link
→ LDP ready
→ IS-IS dùng link bình thường
```

Ứng dụng:

```text
MPLS LDP network
Core IP/MPLS cần tránh mất traffic khi link vừa up
```

---

# 21. Layer 2 Mapping cho IS-IS

Layer 2 mapping giúp next-hop resolution dựa trên topology thay vì đợi traffic tới rồi mới ARP/ND.

Không có Layer 2 mapping:

```text
Route có rồi → traffic đến → mới ARP/ND → có thể mất packet đầu
```

Có Layer 2 mapping:

```text
IS-IS Hello mang binding → ARP/ND cache sẵn → giảm traffic loss
```

Ứng dụng:

```text
Mạng cần hội tụ nhanh
Ethernet core
Giảm packet loss khi link/interface vừa active
```

---

# 22. Segment Routing / SPRING với IS-IS

IS-IS có thể advertise Segment Routing information.

Các khái niệm cần nhớ:

```text
SID         = Segment Identifier
Node SID    = định danh router/node
Prefix SID  = định danh prefix
Adj SID     = định danh link/adjacency cụ thể
Anycast SID = nhiều router cùng SID
SRGB        = dải label dùng cho Segment Routing
```

---

## 22.1 SRGB

**SRGB — Segment Routing Global Block** là dải label dùng cho Segment Routing.

Mẫu cấu hình SRGB:

```bash
set protocols isis source-packet-routing srgb start-label 16000
set protocols isis source-packet-routing srgb index-range 8000
```

Ứng dụng:

```text
SR-MPLS
Traffic engineering không cần RSVP
TI-LFA
Core IP hiện đại
```

---

## 22.2 Prefix SID / Node SID / Adj SID

```text
Node SID:
Đi tới một router cụ thể.

Prefix SID:
Đi tới một prefix cụ thể.

Adjacency SID:
Đi qua một link cụ thể, bất kể metric.
```

Ví dụ thực tế:

```text
Traffic cần đi R1 → R2 → R4
Có thể dùng SID list để ép đường đi
```

---

# 23. SRv6 Network Programming

SRv6 là Segment Routing trên IPv6 dataplane.

SRv6 encode “network instruction” vào IPv6 packet header.

SRv6 SID là địa chỉ IPv6 128-bit.

Cấu trúc SID:

```text
SRv6 SID = Locator + Function
```

Ví dụ:

```text
2001:DB8:AC05:FF01:A000::
|------------------|----|
 Locator            Function
```

Ứng dụng:

```text
Core IPv6
Không muốn phụ thuộc MPLS
Segment Routing dùng IPv6 header
```

So sánh:

```text
SR-MPLS: SID ánh xạ thành MPLS label
SRv6:    SID là IPv6 address mang instruction
```

---

# 24. Flexible Algorithm

Flexible Algorithm cho phép tính đường theo tiêu chí khác nhau.

Ví dụ:

```text
Algo 0   = đường ngắn nhất theo IGP metric
Algo 128 = đường low-delay
Algo 129 = đường tránh link không mong muốn
```

Ứng dụng:

```text
Dịch vụ cần delay thấp
Dịch vụ cần bandwidth cao
Traffic engineering bằng Segment Routing
```

Hiểu đơn giản:

```text
Cùng một topology nhưng có nhiều cách tính đường khác nhau
```

---

# 25. TI-LFA

**TI-LFA — Topology Independent Loop-Free Alternate** là fast reroute dùng Segment Routing.

TI-LFA tạo backup path gần với đường sau khi mạng hội tụ xong.

Sơ đồ nhớ:

```text
Link lỗi
  |
  v
TI-LFA dùng SID list
  |
  v
Traffic đi backup path
  |
  v
Sau đó IGP hội tụ lại bình thường
```

Ứng dụng:

```text
ISP core cần phục hồi nhanh
Segment Routing network
Bảo vệ link/node failure
```

---

# 26. Scaling và Throttling

Mạng càng lớn thì LSP flooding càng nhiều.

Các cơ chế scaling/throttling giúp:

- Giảm control-plane overhead.
- Giảm burst LSP.
- Tối ưu hội tụ.
- Tránh làm quá tải link băng thông thấp.

---

## 26.1 LSP Interval

`lsp-interval` dùng để điều khiển tốc độ flood LSP tới neighbor.

Mẫu:

```bash
set protocols isis interface ge-0/0/0.0 lsp-interval 1000
```

Ứng dụng:

```text
Link băng thông thấp
Mạng lớn nhiều LSP
Cần giảm control-plane burst
```

---

## 26.2 CSNP Frequency

CSNP giúp đồng bộ database.

Trong mạng broadcast hoặc mạng lớn, có thể tinh chỉnh tần suất CSNP để phù hợp môi trường.

---

# 27. Mesh Group

Mesh group dùng trong mạng nhiều kết nối mesh để giảm flooding dư thừa.

Thay vì mỗi router flood LSP qua mọi link gây lặp lại nhiều bản copy, mesh group giúp tối ưu flooding.

Ứng dụng:

```text
Full-mesh / partial-mesh core
Nhiều đường ngang giữa router
Cần giảm LSP duplication
```

Nhớ:

```text
Mesh group = giảm flooding lặp trong topology mesh
```

---

# 28. CLNS

IS-IS ban đầu được thiết kế cho OSI CLNP/CLNS.

Vì vậy Junos vẫn có phần cấu hình IS-IS cho CLNS.

Với lab JNCIA/Junos hoặc Core IP hiện nay, bạn chủ yếu cần biết vì sao IS-IS dùng:

```text
family iso
NET
NSAP
System ID
```

Nhớ:

```text
Nguồn gốc IS-IS = OSI / CLNS
Hiện đại = dùng để route IPv4 / IPv6 / MPLS / SR
```

---

# 29. Logical Systems

Logical systems cho phép một router vật lý chạy nhiều router logic riêng biệt.

Ứng dụng:

```text
Lab nhiều router trên một thiết bị
Mô phỏng topology
Tách routing table logic
Test IS-IS nhiều vùng trên một thiết bị Juniper
```

Ví dụ tư duy:

```text
Một router vật lý
→ logical-system R1
→ logical-system R2
→ logical-system R3
```

Mỗi logical system có thể có IS-IS configuration riêng.

---

# 30. Monitoring và Troubleshooting IS-IS

Đây là phần ứng dụng thực tế nhất.

---

## 30.1 Lệnh kiểm tra chính

```bash
show isis adjacency
show isis adjacency detail
show isis interface
show isis interface detail
show isis database
show isis database detail
show isis route
show route protocol isis
show configuration protocols isis
show route forwarding-table destination <prefix>
```

---

## 30.2 Kiểm tra adjacency

```bash
show isis adjacency
```

Nếu `State` là `Up`, neighbor đã hình thành.

Nếu không `Up`, kiểm tra:

```text
Interface up chưa?
Có family iso chưa?
Có NET trên lo0 chưa?
Có add interface vào protocols isis chưa?
Level có khớp không?
Nếu Level 1 thì area có giống không?
Authentication có khớp không?
MTU có vấn đề không?
```

---

## 30.3 Lỗi level mismatch

Đây là lỗi rất hay gặp khi lab.

Ví dụ:

```text
R1 chạy Level 2
R2 chạy Level 1
→ Không tạo adjacency
```

Router cần cùng level để tạo adjacency.

---

## 30.4 Lỗi area mismatch

Với Level 1, hai router phải cùng area.

Ví dụ:

```text
R1 NET: 49.0001.0000.0000.0001.00
R2 NET: 49.0002.0000.0000.0002.00
```

Nếu R1 và R2 chỉ chạy Level 1:

```text
Area khác nhau → không lên Level 1 adjacency
```

Nếu chạy Level 2:

```text
Có thể lên Level 2 adjacency dù khác area
```

---

## 30.5 Kiểm tra interface và NET

```bash
show isis interface
show configuration interfaces
show configuration protocols isis
```

Cần kiểm tra:

```text
Interface có family iso chưa?
lo0 có NET chưa?
lo0.0 đã add vào protocols isis chưa?
Interface transit đã add vào protocols isis chưa?
```

---

## 30.6 Kiểm tra database

```bash
show isis database
show isis database detail
```

Nếu adjacency Up nhưng không có route, kiểm tra database.

Cần xem:

```text
Có LSP của neighbor không?
LSP đúng level không?
Prefix có được advertise trong LSP không?
Metric đúng không?
```

---

## 30.7 Kiểm tra route

```bash
show route protocol isis
show isis route
```

Nếu database có LSP nhưng không có route:

```text
Prefix không được advertise
Policy chặn route
Route leaking sai
Metric/path không đúng
Level không đúng
```

---

## 30.8 Kiểm tra forwarding table

```bash
show route forwarding-table destination <prefix>
```

Dùng để xác nhận route đã được đưa xuống forwarding plane chưa.

---

## 30.9 Traceoptions

Dùng khi cần debug sâu.

Ví dụ:

```bash
set protocols isis traceoptions file isis-log size 5m
set protocols isis traceoptions flag error
set protocols isis traceoptions flag lsp detail
commit
show log isis-log
```

Lưu ý:

```text
Không bật traceoptions quá rộng trong production nếu không cần
Có thể tạo nhiều log và ảnh hưởng tài nguyên
```

---

# 31. Checklist cấu hình IS-IS thực tế

```text
[ ] Interface up/up chưa?
[ ] Interface có IP chưa?
[ ] Interface có family iso chưa?
[ ] lo0 có IP loopback chưa?
[ ] lo0 có NET chưa?
[ ] protocols isis đã add interface chưa?
[ ] lo0.0 đã add vào protocols isis chưa?
[ ] Level 1/Level 2 đã đúng chưa?
[ ] Nếu L1, area ID có giống nhau chưa?
[ ] Authentication có khớp không?
[ ] show isis adjacency đã Up chưa?
[ ] show isis database có LSP chưa?
[ ] show route protocol isis có route chưa?
[ ] ping loopback neighbor được chưa?
```

---

# 32. Sơ đồ xử lý khi IS-IS không chạy

```text
Không ping được loopback
        |
        v
show isis adjacency
        |
        |-- Down
        |     |
        |     v
        |  Check interface / family iso / NET / level / auth
        |
        |-- Up
              |
              v
        show isis database
              |
              |-- Không có LSP
              |      |
              |      v
              |   Check flooding / level / policy
              |
              |-- Có LSP
                     |
                     v
              show route protocol isis
                     |
                     |-- Không có route
                     |      |
                     |      v
                     |   Check prefix advertise / policy / route leaking
                     |
                     |-- Có route
                            |
                            v
                     show route forwarding-table
```

---

# 33. Bảng tóm tắt học nhanh

| Mục           | Ý nghĩa                | Dùng thực tế khi nào        |
| ------------- | ---------------------- | --------------------------- |
| IS-IS         | Link-state IGP         | Core/IP/MPLS                |
| SPF           | Tính đường ngắn nhất   | Khi topology thay đổi       |
| NET           | Định danh router IS-IS | Bắt buộc khi cấu hình       |
| family iso    | Cho phép IS-IS frame   | Bắt buộc trên interface     |
| Level 1       | Route trong area       | Access/area nội bộ          |
| Level 2       | Route giữa area        | Core/backbone               |
| L1/L2         | Router biên            | Nối area với core           |
| IIH           | Hello tạo neighbor     | Kiểm tra adjacency          |
| LSP           | Mang topology/prefix   | Kiểm tra database           |
| CSNP          | Full list LSP          | Đồng bộ LSDB                |
| PSNP          | Xin/ACK LSP thiếu      | Đồng bộ LSDB                |
| BFD           | Detect lỗi nhanh       | Core cần hội tụ nhanh       |
| LFA           | Backup path local      | Fast reroute                |
| TE            | Điều khiển traffic     | MPLS RSVP                   |
| SR            | Segment Routing        | Core hiện đại               |
| SRv6          | SR trên IPv6           | IPv6 core không MPLS        |
| Flood group   | Giảm flooding          | Mạng lớn                    |
| Route leaking | Leak L1/L2             | Cần route cụ thể giữa level |
| Policy        | Import/export route    | Redistribution              |
| Overload      | Không làm transit      | Maintenance/reboot router   |
| Wide metrics  | Metric mở rộng         | TE/SR/core lớn              |
| LDP-IGP Sync  | Tránh MPLS blackhole   | MPLS LDP network            |

---

# 34. Phần quan trọng nhất nên học trước

Theo hướng ứng dụng thực tế Juniper/Junos, học theo thứ tự:

```text
1. IS-IS là link-state IGP, SPF, LSDB.
2. NET / NSAP / System ID.
3. Level 1, Level 2, L1/L2.
4. IIH, LSP, CSNP, PSNP.
5. Basic Junos config: family iso, lo0 NET, protocols isis interface.
6. show isis adjacency / interface / database / route.
7. Metric, passive interface, DIS.
8. Authentication.
9. Route leaking và redistribution.
10. BFD.
11. LFA / link-protection / node-link-protection.
12. MPLS TE / Segment Routing / SRv6.
```

Nhớ câu này là nắm lõi IS-IS:

```text
IS-IS chạy được khi router có NET, interface có family iso,
neighbor lên bằng IIH, topology đi bằng LSP,
router tạo LSDB, chạy SPF rồi cài route vào routing table.
```

---

# 35. Mẫu lab 2 router IS-IS Junos

## 35.1 Topology

```text
R1 ge-0/0/0 ---------------- ge-0/0/0 R2

R1 lo0: 1.1.1.1/32
R2 lo0: 2.2.2.2/32

Area: 49.0001
```

---

## 35.2 Cấu hình R1

```bash
set interfaces ge-0/0/0 unit 0 family inet address 10.0.12.1/30
set interfaces ge-0/0/0 unit 0 family iso

set interfaces lo0 unit 0 family inet address 1.1.1.1/32
set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0001.00

set protocols isis interface ge-0/0/0.0
set protocols isis interface lo0.0
commit
```

---

## 35.3 Cấu hình R2

```bash
set interfaces ge-0/0/0 unit 0 family inet address 10.0.12.2/30
set interfaces ge-0/0/0 unit 0 family iso

set interfaces lo0 unit 0 family inet address 2.2.2.2/32
set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0002.00

set protocols isis interface ge-0/0/0.0
set protocols isis interface lo0.0
commit
```

---

## 35.4 Kiểm tra

```bash
show isis adjacency
show isis interface
show isis database
show route protocol isis
ping 2.2.2.2 source 1.1.1.1
```

Kỳ vọng:

```text
Adjacency Up
Có LSP của R1/R2
R1 học route 2.2.2.2/32 qua IS-IS
R2 học route 1.1.1.1/32 qua IS-IS
Ping loopback thành công
```

---

# 36. Mẫu troubleshooting nhanh

## Case 1: Neighbor không Up

Kiểm tra:

```bash
show interfaces terse
show isis interface
show configuration interfaces ge-0/0/0
show configuration protocols isis
```

Nguyên nhân hay gặp:

```text
Thiếu family iso
Chưa add interface vào protocols isis
Sai level
Sai area nếu chạy L1
Sai authentication
Interface down
```

---

## Case 2: Neighbor Up nhưng không có route

Kiểm tra:

```bash
show isis database detail
show route protocol isis
show configuration protocols isis
```

Nguyên nhân hay gặp:

```text
lo0 chưa add vào protocols isis
Prefix chưa được advertise
Policy chặn route
Route leaking sai
Level không đúng
```

---

## Case 3: Có route nhưng ping không được

Kiểm tra:

```bash
show route forwarding-table destination <prefix>
show interfaces terse
ping <destination> source <source>
traceroute <destination>
```

Nguyên nhân hay gặp:

```text
Forwarding table chưa có
Firewall filter chặn
Sai source ping
Route chiều về thiếu
Interface data-plane lỗi
```

---

# 37. Sơ đồ nhớ cuối cùng

```text
                IS-IS thực tế trên Junos
                         |
        ------------------------------------------------
        |                 |              |              |
      NET              ISO            PDU             SPF
        |                 |              |              |
  Định danh router   Chạy trên L2   Trao đổi info   Tính route
        |                 |              |              |
        ------------------|--------------|--------------
                           |
                           v
                    Adjacency Up
                           |
                           v
                    LSDB đầy đủ
                           |
                           v
                    Route được cài
                           |
                           v
                    Traffic forward
```

Câu nhớ nhanh:

```text
NET là căn cước router
Hello là bắt tay
LSP là bản đồ mạng
LSDB là kho bản đồ
SPF là thuật toán chọn đường
Route là kết quả cuối cùng
```

---

# 38. Kết luận trọng tâm

IS-IS trong Junos là giao thức IGP link-state quan trọng cho mạng core. Muốn hiểu và làm được IS-IS, cần nắm chắc:

```text
NET / System ID
family iso
Level 1 / Level 2 / L1-L2
IIH / LSP / CSNP / PSNP
LSDB / SPF
Routing policy / route leaking
BFD / LFA / TE / SR
Monitoring bằng show isis
Troubleshooting adjacency, database, route
```

Phần ứng dụng thực tế quan trọng nhất:

```text
IS-IS giúp router core tự động biết topology,
tự tính đường đi tốt nhất,
tự chuyển hướng traffic khi link/router bị lỗi,
và làm nền cho MPLS, Segment Routing, Traffic Engineering.
```


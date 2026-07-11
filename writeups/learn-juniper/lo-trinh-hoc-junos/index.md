---
layout: page-toc
title: "Lộ trình học Juniper Junos"
permalink: /writeups/learn-juniper/lo-trinh-hoc-junos/
toc: true
---

# Lộ Trình Học Juniper Junos - Đầy Đủ Lý Thuyết + Thực Hành

> Mỗi chủ đề trong tài liệu này gồm 4 phần: **(1) Lý thuyết là gì**, **(2) Mục đích / dùng để làm gì**, **(3) Cấu hình thực tế**, **(4) Ưu điểm - Nhược điểm**. Mục tiêu là học không chỉ để gõ lệnh, mà hiểu *tại sao* cần công nghệ đó.

---

## MỤC LỤC

1. [Giai đoạn 1: Junos cơ bản](#giai-đoạn-1-junos-cơ-bản)
2. [Giai đoạn 2: Switching](#giai-đoạn-2-switching)
3. [Giai đoạn 3: Routing](#giai-đoạn-3-routing)
4. [Giai đoạn 4: ISP/Core (MPLS)](#giai-đoạn-4-ispcore-mpls)
5. [Giai đoạn 5: Vận hành](#giai-đoạn-5-vận-hành)
6. [Giai đoạn 6: Automation](#giai-đoạn-6-automation)
7. [Bộ 15 Lab chi tiết](#bộ-lab-nên-làm-chi-tiết)
8. [Công cụ thực hành đề xuất](#công-cụ-thực-hành-đề-xuất)

---

## GIAI ĐOẠN 1: JUNOS CƠ BẢN

### 1.1 CLI và Hierarchy

**Lý thuyết:** Junos OS là hệ điều hành dạng modular chạy trên FreeBSD kernel, cấu hình được lưu dưới dạng **cây phân cấp (hierarchical tree)** thay vì danh sách lệnh tuần tự như IOS. Toàn bộ cấu hình là một file dạng cấu trúc (giống JSON/XML), mỗi node là 1 stanza (`system {}`, `interfaces {}`, `protocols {}`...).

**Mục đích:** Giúp cấu hình dễ đọc, dễ audit, và đặc biệt là cho phép **candidate configuration** (soạn trước, chưa áp dụng) — khác hẳn IOS là gõ lệnh nào chạy lệnh đó ngay lập tức.

**Thực tế áp dụng:** Khi bạn sửa cấu hình router đang chạy production ở xa (remote), nếu gõ sai trên IOS có thể mất kết nối vĩnh viễn phải nhờ người xuống tận nơi. Trên Junos, sai thì đơn giản là chưa `commit`, hoặc dùng `rollback`.

```
router> configure
router# edit interfaces ge-0/0/0
router# up
router# top
router# show interfaces ge-0/0/0
```

**Ưu điểm:**
- Cấu trúc rõ ràng, dễ tìm lỗi (tránh gõ nhầm giữa nhiều context như IOS).
- Hỗ trợ commit theo nhóm thay đổi (transactional), không sợ để config nửa vời.
- Dễ tự động hóa vì cấu hình có cấu trúc (dễ parse bằng XML/JSON qua NETCONF).

**Nhược điểm:**
- Người quen IOS ban đầu sẽ thấy lạ, cần thời gian làm quen tư duy "cây" thay vì "dòng lệnh".
- Cấu hình dài dòng hơn IOS ở một số chỗ (ví dụ set từng dòng thay vì gõ tắt).

---

### 1.2 Commit / Rollback

**Lý thuyết:** Junos tách biệt 2 phiên bản cấu hình: **candidate config** (đang soạn, chưa có hiệu lực) và **active config** (đang chạy thật). Chỉ khi gõ `commit`, candidate mới được đẩy thành active. Junos lưu tối đa 50 bản rollback gần nhất.

**Mục đích:** Đảm bảo an toàn khi thay đổi cấu hình — đặc biệt quan trọng trong môi trường production, ISP, nơi 1 lỗi nhỏ có thể gây downtime diện rộng.

**Thực tế áp dụng:** Khi thay đổi ACL/policy có nguy cơ tự khóa kết nối SSH của chính mình, dùng `commit confirmed 5` — nếu sau 5 phút không xác nhận lại bằng `commit`, hệ thống tự rollback về config cũ, tránh phải chạy ra phòng máy.

```
# commit confirmed 5
# commit check
# rollback 1
# commit and-quit
```

**Ưu điểm:**
- An toàn tuyệt đối khi thay đổi từ xa (self-healing nếu lỗi).
- Có lịch sử rollback, dễ truy vết ai đã đổi gì, khi nào (`show system commit`).
- Hỗ trợ review trước khi apply (`show | compare`).

**Nhược điểm:**
- Thao tác chậm hơn một chút so với sửa-là-chạy-ngay như IOS (phải nhớ gõ `commit`).
- Nếu quên `commit`, thay đổi sẽ mất khi thiết bị reboot hoặc session bị đóng.

---

### 1.3 Interface

**Lý thuyết:** Interface trên Junos đặt tên theo cấu trúc vật lý thực của khung máy: `<media>-<fpc>/<pic>/<port>`. Có 2 lớp: **physical interface** (ge-0/0/0) và **logical unit** (ge-0/0/0.0) — 1 interface vật lý có thể chứa nhiều logical unit (dùng cho sub-interface/VLAN tagging).

**Mục đích:** Interface là điểm kết nối Layer 1/2/3 với thế giới bên ngoài — cấu hình IP, mô tả, MTU, VLAN tag... đều gắn ở đây.

**Thực tế áp dụng:** Một cổng vật lý ge-0/0/0 nối tới switch trunk có thể tách thành nhiều logical unit ứng với nhiều VLAN (dùng cho router-on-a-stick), ví dụ `ge-0/0/0.10` cho VLAN10, `ge-0/0/0.20` cho VLAN20.

```
# set interfaces ge-0/0/0 unit 0 family inet address 10.0.0.1/30
# set interfaces ge-0/0/0 unit 10 vlan-id 10
# set interfaces ge-0/0/0 unit 10 family inet address 192.168.10.1/24
```

**Ưu điểm:**
- Tách biệt rõ vật lý và logical → linh hoạt khi cần nhiều VLAN/sub-interface trên 1 port.
- Hỗ trợ nhiều family cùng lúc trên 1 unit (inet, inet6, mpls, iso...) → tiết kiệm tài nguyên.

**Nhược điểm:**
- Tên interface dài, khó nhớ ban đầu so với kiểu "GigabitEthernet0/1" của Cisco.
- Cần hiểu rõ khái niệm unit mới tránh nhầm lẫn khi troubleshoot.

---

### 1.4 User, SSH

**Lý thuyết:** Junos quản lý user theo **class** (nhóm quyền): `super-user`, `operator`, `read-only`, `unauthorized`, hoặc class tùy chỉnh (custom permission bits). Xác thực có thể local (plain-text-password/ssh-key) hoặc tập trung qua RADIUS/TACACS+.

**Mục đích:** Kiểm soát ai được làm gì trên thiết bị (AAA - Authentication, Authorization, Accounting), tránh việc mọi kỹ sư đều có quyền full admin.

**Thực tế áp dụng:** Trong NOC lớn, kỹ sư trực ca 1 (level 1) chỉ nên có quyền `read-only` để xem log/monitor, còn kỹ sư senior mới có `super-user` để sửa cấu hình. Việc này giảm rủi ro thao tác nhầm.

```
# set system login user noc1 class read-only authentication plain-text-password
# set system login user admin class super-user authentication ssh-rsa "ssh-rsa AAAA..."
# set system services ssh root-login deny
```

**Ưu điểm:**
- Phân quyền chi tiết theo class, dễ audit ai làm gì (kết hợp AAA/RADIUS có accounting log).
- Hỗ trợ SSH key-based login → an toàn hơn password, tránh brute-force.

**Nhược điểm:**
- Cấu hình custom class (permission bits) khá phức tạp, dễ set thiếu quyền cần thiết.
- Nếu không tích hợp RADIUS/TACACS+ tập trung, quản lý user local trên hàng trăm thiết bị sẽ rất cực.

---

### 1.5 Static Route

**Lý thuyết:** Static route là tuyến đường được khai báo thủ công (không qua giao thức định tuyến động), có độ ưu tiên (preference/AD) mặc định là 5, thấp hơn connected (0) nhưng thường cao hơn OSPF (10)/BGP (170) nên **connected > static > OSPF > BGP** theo Junos default preference (số càng nhỏ càng ưu tiên).

**Mục đích:** Dùng khi mạng nhỏ, ít thay đổi, hoặc dùng làm default route ra Internet, hoặc backup route khi routing protocol chết (floating static).

**Thực tế áp dụng:** Route ra Internet ở chi nhánh nhỏ (branch office) thường chỉ cần 1 static default route trỏ về ISP, không cần chạy BGP phức tạp.

```
# set routing-options static route 0.0.0.0/0 next-hop 10.0.0.254
# set routing-options static route 172.16.0.0/24 next-hop 10.0.0.2 preference 200   (floating static - backup)
```

**Ưu điểm:**
- Đơn giản, không tốn CPU/tài nguyên xử lý giao thức động.
- Dễ kiểm soát, dự đoán được đường đi traffic (predictable).

**Nhược điểm:**
- Không tự động hội tụ (converge) khi mạng thay đổi/link down → phải sửa tay.
- Không scale được cho mạng lớn nhiều node (dễ sai sót, khó bảo trì).

---

### 1.6 Monitoring Command

**Lý thuyết:** Đây là nhóm lệnh **operational mode** (không sửa cấu hình) dùng để quan sát trạng thái runtime: interface, routing table, process, log, alarm...

**Mục đích:** Là "con mắt" của kỹ sư mạng — bước đầu tiên của mọi troubleshoot đều bắt đầu từ các lệnh show/monitor này.

**Thực tế áp dụng:** Khi khách hàng báo mất mạng, việc đầu tiên NOC làm là `show interfaces terse` để xem link còn up không, rồi mới đi sâu vào routing/ACL.

```
> show interfaces terse
> show system alarms
> monitor traffic interface ge-0/0/0
> show log messages | last 50
```

**Ưu điểm:**
- Cung cấp cái nhìn nhanh, real-time về sức khỏe hệ thống.
- Không rủi ro làm hỏng cấu hình (chỉ đọc, không ghi).

**Nhược điểm:**
- Với hệ thống lớn, xem thủ công từng lệnh tốn thời gian → cần kết hợp SNMP/monitoring tool để tự động hóa.

---

## GIAI ĐOẠN 2: SWITCHING

### 2.1 VLAN

**Lý thuyết:** VLAN (Virtual LAN) là kỹ thuật chia 1 switch vật lý (hoặc hệ thống switch) thành nhiều broadcast domain độc lập ở Layer 2, dùng VLAN ID (1-4094) để phân biệt, đóng gói theo chuẩn IEEE 802.1Q.

**Mục đích:** Cô lập traffic giữa các phòng ban/nhóm người dùng (ví dụ Kế toán, Kỹ thuật, Guest Wifi) dù cùng cắm chung 1 switch vật lý — tăng bảo mật và giảm broadcast storm.

**Thực tế áp dụng:** Trong 1 công ty, phòng Kế toán VLAN10 và phòng IT VLAN20 dùng chung switch tầng nhưng không thấy broadcast của nhau, và có thể áp policy riêng (VLAN10 không được ra Internet trực tiếp, phải qua proxy).

```
# set vlans VLAN10 vlan-id 10
# set interfaces ge-0/0/5 unit 0 family ethernet-switching vlan members VLAN10
```

**Ưu điểm:**
- Giảm broadcast domain → tăng hiệu năng mạng.
- Cô lập bảo mật giữa các nhóm mà không cần switch vật lý riêng (tiết kiệm chi phí phần cứng).
- Dễ quản lý logic theo phòng ban/chức năng thay vì theo vị trí vật lý.

**Nhược điểm:**
- Cần thêm router/L3 switch (IRB) nếu muốn các VLAN nói chuyện được với nhau.
- Cấu hình sai VLAN trunk dễ gây mất kết nối toàn bộ (nếu quên add VLAN vào trunk).

---

### 2.2 Trunk / Access

**Lý thuyết:** **Access port** chỉ thuộc 1 VLAN duy nhất (dùng nối PC, máy in, camera...). **Trunk port** mang nhiều VLAN cùng lúc, gắn thẻ 802.1Q tag để switch/router phía bên kia phân biệt được gói tin thuộc VLAN nào.

**Mục đích:** Trunk cho phép nhiều VLAN đi qua 1 đường link duy nhất giữa 2 switch (hoặc switch-router), tránh phải kéo dây riêng cho từng VLAN.

**Thực tế áp dụng:** Giữa Switch tầng 1 và Switch tầng 2 chỉ có 1 sợi cáp quang, nhưng cần mang cả VLAN10, VLAN20, VLAN30 → cấu hình trunk trên cả 2 đầu.

```
# set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode trunk
# set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members [ VLAN10 VLAN20 ]
```

**Ưu điểm:**
- Tiết kiệm số lượng cổng/cáp vật lý cần dùng.
- Linh hoạt mở rộng thêm VLAN mới mà không cần đi dây mới.

**Nhược điểm:**
- Nếu cấu hình sai (native VLAN mismatch, thiếu VLAN trong danh sách members) → traffic VLAN đó sẽ không đi qua được, rất khó phát hiện nếu không kiểm tra kỹ.
- Trunk port là điểm tập trung traffic nhiều VLAN → nếu đứt link này, nhiều VLAN bị ảnh hưởng cùng lúc.

---

### 2.3 IRB (Integrated Routing and Bridging)

**Lý thuyết:** IRB là interface ảo Layer 3 gắn vào 1 VLAN, cho phép switch (hoặc router có tính năng switch) vừa bridging (L2) vừa routing (L3) cùng lúc trên cùng 1 thiết bị.

**Mục đích:** Cho phép các VLAN khác nhau (khác broadcast domain) giao tiếp được với nhau — đây chính là **inter-VLAN routing**.

**Thực tế áp dụng:** PC ở VLAN10 (phòng Kế toán, 192.168.10.0/24) muốn in tài liệu trên máy in ở VLAN20 (phòng IT, 192.168.20.0/24) → traffic phải đi qua IRB (đóng vai trò default gateway của từng VLAN).

```
# set interfaces irb unit 10 family inet address 192.168.10.1/24
# set vlans VLAN10 l3-interface irb.10
```

**Ưu điểm:**
- Không cần router riêng cho inter-VLAN routing (switch layer 3 làm luôn) → tiết kiệm chi phí và độ trễ.
- Cấu hình tập trung, dễ quản lý default gateway cho nhiều VLAN trên 1 thiết bị.

**Nhược điểm:**
- Cần switch hỗ trợ Layer 3 (không phải switch layer 2 thông thường nào cũng làm được).
- Nếu thiết bị này chết, cả routing lẫn switching của các VLAN đó đều bị ảnh hưởng (single point of failure) — nên cần thêm VRRP/redundancy.

---

### 2.4 STP (Spanning Tree Protocol)

**Lý thuyết:** STP (IEEE 802.1D, và biến thể RSTP 802.1w, MSTP 802.1s) là giao thức chống loop ở Layer 2 bằng cách chặn (block) các port dư thừa tạo thành vòng lặp vật lý, chỉ giữ lại 1 đường logic duy nhất (loop-free topology), dựa vào Bridge ID và cost để bầu Root Bridge.

**Mục đích:** Trong thực tế, để dự phòng (redundancy), người ta thường nối 2 switch bằng 2 sợi cáp — nhưng nếu không có STP, việc này tạo ra **broadcast storm** (gói tin lặp vô hạn) làm sập cả mạng trong vài giây.

**Thực tế áp dụng:** Switch tầng nối với Switch core bằng 2 dây để dự phòng — STP sẽ tự động chặn 1 dây (blocking), chỉ khi dây kia đứt thì dây dự phòng mới chuyển sang forwarding.

```
# set protocols rstp interface all
# set protocols rstp bridge-priority 4096   (ưu tiên làm root bridge - số càng nhỏ càng ưu tiên)
```

**Ưu điểm:**
- Ngăn chặn broadcast storm/loop chết mạng — bắt buộc phải có khi thiết kế mạng dự phòng vật lý.
- RSTP hội tụ nhanh (vài giây) so với STP cổ điển (30-50 giây).

**Nhược điểm:**
- Có port bị block → lãng phí băng thông (1 trong 2 đường dự phòng không được dùng đồng thời).
- Cấu hình sai priority có thể khiến switch không mong muốn trở thành Root Bridge, gây định tuyến traffic không tối ưu.
- (Đây là lý do các mạng hiện đại chuyển sang dùng LACP/MC-LAG/EVPN để tận dụng cả 2 đường thay vì block bớt.)

---

### 2.5 LACP (Link Aggregation Control Protocol)

**Lý thuyết:** LACP (IEEE 802.3ad) gộp nhiều link vật lý thành 1 logical link (gọi là `ae` - aggregated ethernet trên Junos), tăng băng thông tổng và cung cấp dự phòng — khác STP là **không cần block port nào**, tất cả các link đều active cùng lúc.

**Mục đích:** Vừa tăng băng thông (ví dụ 4x1Gbps = 4Gbps logic) vừa có failover tức thời nếu 1 trong các link đứt, mà không cần chờ STP hội tụ lại.

**Thực tế áp dụng:** Kết nối giữa 2 Core Switch trong Data Center thường dùng LACP với 2-4 sợi cáp quang gộp lại, để vừa đủ băng thông cho traffic lớn vừa chịu được đứt 1 sợi mà không gián đoạn dịch vụ.

```
# set interfaces ae0 aggregated-ether-options lacp active
# set interfaces ge-0/0/2 ether-options 802.3ad ae0
# set interfaces ge-0/0/3 ether-options 802.3ad ae0
```

**Ưu điểm:**
- Tận dụng được toàn bộ băng thông của tất cả các link (không lãng phí như STP).
- Failover nhanh (sub-second) khi một link trong bó bị đứt.
- Được hỗ trợ rộng rãi, tương thích đa vendor (theo chuẩn IEEE).

**Nhược điểm:**
- Cả 2 đầu link phải cùng hỗ trợ LACP và cấu hình khớp (số lượng link, mode active/passive).
- Nếu 2 link trong ae0 khác độ trễ/băng thông thực tế → có thể gây load-balancing không đều (hashing theo 5-tuple không hoàn hảo 100%).

---

### 2.6 Virtual Chassis (VC)

**Lý thuyết:** Virtual Chassis là công nghệ độc quyền Juniper cho phép gộp nhiều switch vật lý riêng biệt (cùng dòng, ví dụ EX4300) thành **1 thiết bị logic duy nhất**, quản lý bằng 1 IP, 1 bảng cấu hình, 1 control-plane (có Master và Backup).

**Mục đích:** Đơn giản hóa quản trị (thay vì login 4-8 switch riêng lẻ, chỉ cần quản lý 1 "switch ảo"), đồng thời cho phép làm LACP/redundancy **giữa 2 switch vật lý khác nhau** (Multi-Chassis LAG).

**Thực tế áp dụng:** 1 phòng server có 4 switch access đặt ở 4 tủ rack khác nhau, gộp thành 1 Virtual Chassis — khi cấu hình VLAN mới, chỉ cần commit 1 lần trên Master, tự động áp dụng cho cả 4 switch.

```
> request virtual-chassis vc-port set pic-slot 0 port 0
# set virtual-chassis member 0 mastership-priority 255
```

**Ưu điểm:**
- Giảm số điểm quản lý (1 IP quản lý thay vì N switch).
- Cho phép Multi-chassis LACP (server/switch phía dưới có thể LAG lên 2 switch vật lý khác nhau trong cùng VC → dự phòng thật sự, không như STP phải block).
- Đơn giản hóa STP topology (vì với phần còn lại của mạng, VC là 1 switch duy nhất).

**Nhược điểm:**
- Phụ thuộc vào 1 hãng (Juniper only, không tương thích chuẩn mở).
- Upgrade phần mềm phải làm đồng bộ cả cụm (ISSU - In-Service Software Upgrade) khá phức tạp, rủi ro nếu thao tác sai.
- Giới hạn số lượng thành viên trong 1 VC tùy dòng sản phẩm (thường 10 units).

---

## GIAI ĐOẠN 3: ROUTING

### 3.1 OSPF (Open Shortest Path First)

**Lý thuyết:** OSPF là giao thức **link-state, IGP** (Interior Gateway Protocol), dùng thuật toán Dijkstra (SPF) để tính đường đi ngắn nhất dựa trên cost (metric). Mỗi router xây dựng bản đồ toàn bộ topology trong area của mình (Link State Database) rồi tự tính toán, khác với distance-vector chỉ biết "hàng xóm nói gì".

**Mục đích:** Dùng làm giao thức định tuyến nội bộ (trong 1 tổ chức/AS), hội tụ nhanh, hỗ trợ chia area để giảm tải tính toán cho mạng lớn.

**Thực tế áp dụng:** Một doanh nghiệp có 20 chi nhánh kết nối qua MPLS/VPN, dùng OSPF để các router học route của nhau tự động thay vì cấu hình 20x20 static route thủ công.

```
# set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
# set protocols ospf area 0.0.0.0 interface lo0.0 passive
```

**Ưu điểm:**
- Hội tụ nhanh (vài giây) nhờ link-state, biết được toàn bộ topology.
- Hỗ trợ chia area giúp scale tốt hơn cho mạng lớn (giảm kích thước LSDB, giảm CPU).
- Là chuẩn mở (RFC), tương thích đa vendor (Cisco, Juniper, Huawei...).

**Nhược điểm:**
- Tốn CPU/RAM hơn distance-vector vì phải lưu toàn bộ LSDB và chạy SPF.
- Không scale tốt cho mạng cực lớn (hàng chục nghìn route) như BGP — thường dùng OSPF cho nội bộ, BGP cho liên AS/Internet.
- Area 0 (backbone) là bắt buộc và là điểm phải thiết kế cẩn thận ngay từ đầu.

---

### 3.2 IS-IS (Intermediate System to Intermediate System)

**Lý thuyết:** IS-IS cũng là link-state IGP giống OSPF, nhưng chạy trực tiếp trên Layer 2 (không đóng gói trong IP, dùng CLNS/OSI) — nên **độc lập với IP**, dễ mở rộng hỗ trợ IPv6 song song IPv4 (dual-stack) mà không cần 2 tiến trình riêng như OSPFv2/OSPFv3.

**Mục đích:** Được các nhà mạng lớn (ISP, Telco) ưa chuộng làm IGP cho mạng core MPLS vì tính ổn định, khả năng mở rộng cao, và ít bug/lỗ hổng bảo mật hơn do chạy ở Layer 2.

**Thực tế áp dụng:** Hầu hết mạng core của các ISP lớn (Tier 1/2) dùng IS-IS thay vì OSPF để chạy MPLS/LDP, vì IS-IS xử lý tốt hơn với hàng nghìn router trong 1 domain.

```
# set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0001.00
# set protocols isis interface ge-0/0/0.0 level 2 metric 10
```

**Ưu điểm:**
- Ổn định, scale tốt cho mạng core lớn (được chứng minh qua nhiều ISP toàn cầu).
- Hỗ trợ dual-stack IPv4/IPv6 tự nhiên hơn OSPF.
- Ít bị tấn công/exploit qua IP vì chạy trực tiếp trên L2.

**Nhược điểm:**
- Ít phổ biến trong mạng doanh nghiệp thông thường (chủ yếu dùng trong ISP/Telco) → khó tìm nhân sự có kinh nghiệm sâu.
- Khái niệm NET address, area-id ban đầu khó hiểu hơn OSPF (dùng địa chỉ kiểu OSI thay vì IP quen thuộc).

---

### 3.3 BGP (Border Gateway Protocol)

**Lý thuyết:** BGP là giao thức **path-vector**, EGP (Exterior Gateway Protocol) dùng để định tuyến **giữa các AS (Autonomous System)** khác nhau — đây chính là giao thức giữ cho Internet toàn cầu hoạt động. BGP không dùng cost/metric như IGP mà dùng nhiều thuộc tính (attribute) như AS-path, Local Preference, MED để chọn đường đi tốt nhất.

**Mục đích:** eBGP dùng để trao đổi route giữa các tổ chức/ISP khác nhau (khác AS); iBGP dùng để phân phối route học được từ bên ngoài cho các router nội bộ trong cùng AS.

**Thực tế áp dụng:** Một doanh nghiệp thuê 2 đường Internet từ 2 ISP khác nhau (multihoming) sẽ chạy eBGP với cả 2 ISP để tự động chọn đường tốt nhất hoặc có dự phòng khi 1 ISP down.

```
# set protocols bgp group EBGP-PEER type external
# set protocols bgp group EBGP-PEER peer-as 65002
# set protocols bgp group EBGP-PEER neighbor 10.0.0.2
```

**Ưu điểm:**
- Là giao thức duy nhất scale được cho toàn bộ Internet (hàng trăm nghìn route/prefix).
- Rất linh hoạt trong việc điều khiển traffic đi vào/ra (traffic engineering) qua policy/attribute.
- Ổn định, ít gửi update trừ khi có thay đổi thật (path-vector, không phải periodic flooding).

**Nhược điểm:**
- Hội tụ chậm hơn IGP (có thể mất vài chục giây đến vài phút khi có sự cố lớn).
- Cấu hình và troubleshoot phức tạp hơn nhiều so với OSPF (nhiều attribute, nhiều policy chain).
- Cấu hình sai (ví dụ leak route ra ngoài không kiểm soát) có thể gây sự cố ảnh hưởng cả Internet (đã từng có case thực tế nổi tiếng như BGP hijack).

---

### 3.4 Routing Policy

**Lý thuyết:** Routing policy là cơ chế lọc/sửa đổi route khi trao đổi giữa các giao thức hoặc giữa các neighbor, dựa trên các `term` (điều kiện `from` và hành động `then`), xử lý tuần tự như firewall rule.

**Mục đích:** Kiểm soát chính xác route nào được học/quảng bá, tránh leak nhầm route nội bộ ra ngoài, hoặc ưu tiên đường đi theo ý muốn thay vì để giao thức tự quyết định 100%.

**Thực tế áp dụng:** ISP không muốn khách hàng vô tình trở thành "transit" (chuyển tiếp traffic hộ ISP khác) nên sẽ áp policy chỉ chấp nhận đúng các prefix mà khách hàng sở hữu, chặn mọi prefix khác dù khách hàng có quảng bá.

```
# set policy-options policy-statement FILTER-IN term 1 from prefix-list CUSTOMER-ROUTES
# set policy-options policy-statement FILTER-IN term 1 then accept
# set policy-options policy-statement FILTER-IN term 2 then reject
```

**Ưu điểm:**
- Kiểm soát chi tiết, linh hoạt (theo prefix, AS-path, community, MED...).
- Là công cụ bắt buộc để bảo mật routing (chống route leak/hijack) trong môi trường ISP.

**Nhược điểm:**
- Cú pháp term-based dễ nhầm thứ tự xử lý (default action là reject nếu không match term nào — dễ quên và mất toàn bộ route).
- Policy phức tạp (nhiều term/policy lồng nhau) khó debug khi có sự cố.

---

### 3.5 Route Redistribution

**Lý thuyết:** Redistribution là việc lấy route học được từ 1 giao thức (hoặc static) và "tiêm" (inject) vào 1 giao thức khác, thông qua export policy.

**Mục đích:** Dùng khi mạng có nhiều giao thức chạy song song (ví dụ 1 phần mạng chạy OSPF, phần khác chạy BGP) và cần chúng biết route của nhau.

**Thực tế áp dụng:** Router biên (Edge router) học route Internet qua BGP từ ISP, cần "tiêm" default route đó vào OSPF để các router nội bộ (chỉ chạy OSPF) cũng biết đường ra Internet.

```
# set policy-options policy-statement OSPF-TO-BGP term 1 from protocol ospf
# set protocols bgp group EBGP-PEER export OSPF-TO-BGP
```

**Ưu điểm:**
- Cho phép tích hợp nhiều giao thức trong 1 hệ thống mạng phức tạp (thường gặp khi sáp nhập hạ tầng 2 công ty, hoặc mạng legacy + mới).

**Nhược điểm:**
- Rủi ro **routing loop** nếu redistribute 2 chiều mà không kiểm soát tốt (route đi vào OSPF rồi lại được redistribute ngược lại BGP, tạo vòng lặp).
- Metric giữa các giao thức khác nhau (OSPF cost vs BGP AS-path) không tương đồng, cần seed-metric hợp lý tránh chọn đường sai.

---

## GIAI ĐOẠN 4: ISP/CORE (MPLS)

### 4.1 MPLS + LDP

**Lý thuyết:** MPLS (Multiprotocol Label Switching) chèn thêm 1 "label" (nhãn, 32-bit) vào giữa Layer 2 và Layer 3 của gói tin. Router trong mạng core chỉ cần nhìn label để chuyển tiếp (label switching) thay vì phải tra bảng định tuyến IP đầy đủ ở mỗi hop — nhanh hơn và mềm dẻo hơn cho traffic engineering/VPN. LDP (Label Distribution Protocol) là giao thức tự động phân phối label giữa các router dựa trên route học được từ IGP (OSPF/IS-IS).

**Mục đích:** MPLS là nền tảng để triển khai **L3VPN, L2VPN, Traffic Engineering** — cho phép 1 mạng lõi (core) vật lý duy nhất phục vụ nhiều khách hàng riêng biệt (multi-tenant) mà vẫn cô lập traffic hoàn toàn.

**Thực tế áp dụng:** Một ISP có 1 mạng core MPLS duy nhất, nhưng bán dịch vụ VPN riêng biệt cho hàng trăm doanh nghiệp khác nhau (Bank, Manufacturing, Retail) mà không ai thấy traffic của ai — tất cả nhờ MPLS label phân biệt VPN.

```
# set protocols mpls interface ge-0/0/0.0
# set protocols ldp interface ge-0/0/0.0
```

**Ưu điểm:**
- Chuyển tiếp nhanh (label lookup đơn giản hơn IP longest-prefix-match ở core, dù hiện tại hardware đã tối ưu cả 2).
- Nền tảng linh hoạt để làm VPN, TE, QoS mà không cần đổi hạ tầng vật lý.
- Cô lập traffic khách hàng tốt (mỗi VPN có bảng định tuyến riêng - VRF).

**Nhược điểm:**
- Thêm độ phức tạp vận hành đáng kể (thêm 1 lớp label cần quản lý, troubleshoot khó hơn IP thuần).
- Cần IGP (OSPF/IS-IS) ổn định làm nền trước — nếu IGP lỗi, LDP/MPLS cũng sập theo.

---

### 4.2 RSVP-TE

**Lý thuyết:** RSVP (Resource Reservation Protocol) mở rộng cho Traffic Engineering (RSVP-TE), cho phép thiết lập đường đi MPLS **tường minh** (explicit path) và **đặt trước băng thông** dọc đường đi đó, khác với LDP là chỉ đi theo đường IGP tính toán sẵn (shortest path).

**Mục đích:** Dùng khi cần kiểm soát chính xác đường đi traffic (ví dụ tránh 1 link cụ thể, hoặc đảm bảo băng thông cam kết cho dịch vụ quan trọng như thoại/video).

**Thực tế áp dụng:** ISP cam kết SLA băng thông 1Gbps cho khách hàng lớn — dùng RSVP-TE để đặt trước 1Gbps dọc đường đi cụ thể, tránh bị nghẽn chung với traffic best-effort khác dù IGP có thể chọn đường khác.

```
# set protocols mpls label-switched-path LSP-R1-R3 to 3.3.3.3
# set protocols mpls path PATH1 10.0.1.2
```

**Ưu điểm:**
- Kiểm soát đường đi chính xác, đặt trước tài nguyên (bandwidth reservation) → đảm bảo SLA.
- Hỗ trợ fast-reroute (chuyển đường dự phòng cực nhanh <50ms) cho dịch vụ quan trọng.

**Nhược điểm:**
- Phức tạp hơn LDP nhiều (phải tính path thủ công hoặc dùng CSPF), tốn state trên mỗi router dọc đường LSP.
- Không scale tốt bằng LDP khi số lượng LSP lớn (mỗi LSP tốn state riêng trên router).

---

### 4.3 MP-BGP (Multiprotocol BGP)

**Lý thuyết:** Mở rộng BGP để mang được nhiều loại route ngoài IPv4 unicast thông thường — như `inet-vpn` (L3VPN), `inet6-vpn`, `l2vpn`, `evpn`... bằng cách thêm AFI/SAFI (Address Family Identifier).

**Mục đích:** Là "đường ống" để phân phối route VPN của khách hàng giữa các router PE (Provider Edge) trong mạng MPLS, mang kèm Route Distinguisher/Route Target để phân biệt VPN nào với VPN nào.

**Thực tế áp dụng:** PE1 và PE2 (2 router biên khác nhau của ISP) trao đổi route VPN của khách hàng A qua MP-BGP family `inet-vpn unicast`, dù bản thân route đó (192.168.100.0/24) là route private trùng lặp giữa nhiều khách hàng khác nhau.

```
# set protocols bgp group IBGP family inet-vpn unicast
```

**Ưu điểm:**
- 1 giao thức BGP duy nhất mang được nhiều loại dịch vụ (VPN, IPv6, EVPN) → không cần chạy nhiều giao thức riêng lẻ.
- Route Distinguisher cho phép các khách hàng dùng trùng dải IP private (RFC1918) mà không xung đột.

**Nhược điểm:**
- Cấu hình phức tạp hơn BGP thường (cần hiểu RD, RT, VRF cùng lúc).
- Yêu cầu router PE có tài nguyên (RAM/CPU) đủ mạnh nếu phục vụ nhiều VPN cùng lúc.

---

### 4.4 L3VPN

**Lý thuyết:** L3VPN dùng VRF (Virtual Routing and Forwarding) để tạo bảng định tuyến **riêng biệt và cô lập** cho từng khách hàng trên cùng 1 router PE vật lý, kết hợp MPLS label (VPN label) để phân biệt traffic khi đi qua mạng core.

**Mục đích:** Cho phép 1 hạ tầng ISP vật lý duy nhất cung cấp dịch vụ VPN riêng biệt hoàn toàn cho nhiều khách hàng khác nhau — đúng như tên gọi "Virtual Private Network" ở tầng Layer 3.

**Thực tế áp dụng:** Ngân hàng có 50 chi nhánh toàn quốc, thuê dịch vụ L3VPN của 1 ISP — tất cả chi nhánh nằm trong 1 VRF riêng, hoạt động như 1 mạng WAN riêng tư của ngân hàng dù thực tế chạy chung hạ tầng MPLS với khách hàng khác.

```
# set routing-instances CUST-A instance-type vrf
# set routing-instances CUST-A route-distinguisher 65000:1
# set routing-instances CUST-A vrf-target target:65000:1
```

**Ưu điểm:**
- Cô lập hoàn toàn giữa các khách hàng dù dùng chung hạ tầng vật lý → tiết kiệm chi phí lớn cho ISP và khách hàng so với thuê đường riêng (leased line).
- Dễ mở rộng thêm site mới cho khách hàng (chỉ cần thêm PE-CE link, không cần đụng vào core).

**Nhược điểm:**
- Cấu hình PE phức tạp (RD, RT, VRF, MP-BGP) — sai RT có thể làm lộ route giữa 2 khách hàng khác nhau (rủi ro bảo mật nghiêm trọng).
- Khách hàng phụ thuộc hoàn toàn vào ISP (không kiểm soát được core network).

---

### 4.5 Route Reflector (RR)

**Lý thuyết:** Theo quy tắc iBGP mặc định, route học từ 1 iBGP neighbor **không được** quảng bá tiếp cho iBGP neighbor khác (để tránh loop) — nghĩa là cần full-mesh (mọi router phải peer trực tiếp với nhau), rất tốn kém khi số router lớn (N routers cần N(N-1)/2 session). Route Reflector phá vỡ quy tắc này một cách có kiểm soát: RR được phép phản chiếu (reflect) route giữa các client của nó.

**Mục đích:** Giảm số lượng iBGP session cần thiết trong mạng lớn, từ mô hình full-mesh phức tạp xuống mô hình hub-spoke đơn giản hơn nhiều.

**Thực tế áp dụng:** ISP có 100 router PE trên toàn quốc — thay vì mỗi PE phải peer iBGP với 99 PE còn lại (~4950 session), chỉ cần 2-3 Route Reflector ở trung tâm, mỗi PE chỉ cần peer với RR (100 session, giảm gần 50 lần).

```
# set protocols bgp group RR-CLIENTS type internal
# set protocols bgp group RR-CLIENTS cluster 1.1.1.1
```

**Ưu điểm:**
- Giảm đáng kể số lượng BGP session cần cấu hình/quản lý trong mạng lớn.
- Client không cần biết gì về RR (cấu hình phía client y hệt iBGP thường) → dễ triển khai.

**Nhược điểm:**
- RR trở thành single point of failure/bottleneck nếu chỉ có 1 RR (nên luôn triển khai tối thiểu 2 RR dự phòng).
- Có thể gây ra hiện tượng chọn đường đi không tối ưu (suboptimal routing) vì client không thấy đầy đủ mọi lựa chọn đường đi như full-mesh.

---

## GIAI ĐOẠN 5: VẬN HÀNH

### 5.1 Syslog

**Lý thuyết:** Syslog (RFC 5424) là giao thức gửi log sự kiện (theo mức độ severity: emergency → debug) từ thiết bị mạng đến 1 server tập trung, qua UDP/TCP port 514.

**Mục đích:** Tập trung hóa log của hàng trăm thiết bị về 1 nơi để dễ tra cứu, cảnh báo (alert), và lưu trữ phục vụ audit/điều tra sự cố (vì log local trên thiết bị có giới hạn dung lượng, dễ bị ghi đè).

**Thực tế áp dụng:** Khi có sự cố mất mạng lúc 2h sáng, kỹ sư không cần login vào từng router để tìm log — chỉ cần tra trên hệ thống tập trung (ELK/Splunk/Graylog) đã nhận syslog từ toàn bộ thiết bị, lọc theo thời gian là ra ngay nguyên nhân.

```
# set system syslog host 10.0.0.100 any notice
```

**Ưu điểm:**
- Tập trung log giúp tra cứu/điều tra sự cố nhanh, không phải login từng thiết bị.
- Có thể tích hợp SIEM để cảnh báo real-time (ví dụ phát hiện login thất bại nhiều lần).

**Nhược điểm:**
- Syslog qua UDP có thể mất gói nếu mạng nghẽn (không đảm bảo 100% log đến nơi) — cần cân nhắc TCP hoặc syslog-over-TLS cho log quan trọng.
- Nếu không lọc severity hợp lý, log server dễ bị "ngập" bởi log không quan trọng (debug/info).

---

### 5.2 SNMP

**Lý thuyết:** SNMP (Simple Network Management Protocol) là giao thức chuẩn để giám sát (polling) và nhận cảnh báo (trap) từ thiết bị mạng, dựa trên cấu trúc dữ liệu MIB (Management Information Base) và OID (Object Identifier). Có 3 version: v1, v2c (dùng community string - kém an toàn), v3 (có authentication + encryption).

**Mục đích:** Cho phép hệ thống giám sát (Zabbix, PRTG, LibreNMS, SolarWinds...) tự động lấy số liệu (CPU, RAM, băng thông interface, trạng thái link) định kỳ mà không cần con người login thủ công.

**Thực tế áp dụng:** Dashboard NOC hiển thị biểu đồ traffic real-time của 200 interface trên toàn hệ thống, tất cả dữ liệu lấy qua SNMP polling mỗi 1-5 phút.

```
# set snmp community public authorization read-only
# set snmp trap-group MYGROUP targets 10.0.0.100
```

**Ưu điểm:**
- Chuẩn hóa, hỗ trợ hầu hết mọi thiết bị mạng đa vendor.
- Nhẹ, ít tốn tài nguyên thiết bị khi polling (so với chạy script SSH thủ công).

**Nhược điểm:**
- SNMP v1/v2c dùng community string dạng plain-text → dễ bị nghe lén nếu không kiểm soát ACL/mạng quản trị riêng (nên ưu tiên v3).
- Chỉ lấy được dữ liệu dạng đã định nghĩa sẵn trong MIB — muốn lấy thông tin đặc thù/tùy chỉnh phải kết hợp thêm NETCONF/script.

---

### 5.3 NTP

**Lý thuyết:** NTP (Network Time Protocol) đồng bộ thời gian giữa các thiết bị với 1 nguồn thời gian chuẩn (time server), qua nhiều "stratum" (tầng), càng gần nguồn atomic clock stratum càng nhỏ (chính xác hơn).

**Mục đích:** Đảm bảo mọi thiết bị trong hệ thống có cùng 1 mốc thời gian chính xác — cực kỳ quan trọng khi troubleshoot (đối chiếu log giữa nhiều thiết bị), hoặc khi cần chứng cứ pháp lý (forensic).

**Thực tế áp dụng:** Khi điều tra sự cố bảo mật, cần đối chiếu log giữa Firewall, Router, Server — nếu thời gian mỗi thiết bị lệch nhau vài phút, rất khó ghép nối chuỗi sự kiện thành 1 timeline chính xác.

```
# set system ntp server 0.pool.ntp.org
```

**Ưu điểm:**
- Đơn giản, nhẹ, gần như bắt buộc phải có trên mọi thiết bị production.
- Đồng bộ chính xác tới mili-giây, đủ cho hầu hết nhu cầu vận hành.

**Nhược điểm:**
- Phụ thuộc vào NTP server bên ngoài (nếu không có server nội bộ) → rủi ro nếu mất kết nối Internet, thời gian có thể trôi dần (clock drift).
- NTP không mã hóa mặc định, có thể bị giả mạo (spoofing) nếu không kiểm soát nguồn tin cậy.

---

### 5.4 Backup / Restore

**Lý thuyết:** Là quá trình lưu trữ bản sao cấu hình (configuration) hiện tại ra nơi lưu trữ ngoài (external), và khả năng nạp lại (restore) khi cần.

**Mục đích:** Đảm bảo có thể khôi phục nhanh khi thiết bị hỏng phần cứng cần thay thế, hoặc khi cấu hình bị sửa sai nghiêm trọng mà rollback local không đủ (ví dụ mất luôn cả file rollback do factory-reset).

**Thực tế áp dụng:** Khi 1 router bị cháy nguồn phải thay thiết bị mới hoàn toàn, kỹ sư chỉ cần restore file backup đã lưu trước đó thay vì phải gõ lại từ đầu toàn bộ cấu hình (có thể hàng nghìn dòng).

```
> show configuration | save /var/tmp/backup.conf
# set system archival configuration transfer-on-commit
```

**Ưu điểm:**
- Giảm thời gian khôi phục sự cố (RTO) từ hàng giờ xuống vài phút.
- `transfer-on-commit` tự động backup mỗi lần commit → không cần nhớ backup thủ công.

**Nhược điểm:**
- Cần có nơi lưu trữ (FTP/SCP server) và giám sát việc backup có chạy thành công hay không (backup lỗi âm thầm là rủi ro phổ biến nếu không kiểm tra định kỳ).
- Backup không tự động bao gồm license key/thông tin phần cứng đặc thù — cần lưu riêng.

---

### 5.5 Upgrade Junos

**Lý thuyết:** Là quá trình thay thế phần mềm hệ điều hành (Junos image) sang phiên bản mới hơn, thường để vá lỗi bảo mật, thêm tính năng, hoặc theo yêu cầu vendor support lifecycle (EoL - End of Life).

**Mục đích:** Đảm bảo thiết bị luôn chạy phiên bản được vendor hỗ trợ, có bản vá cho các lỗ hổng bảo mật đã biết (CVE).

**Thực tế áp dụng:** Khi Juniper công bố lỗ hổng bảo mật nghiêm trọng (CVE) ảnh hưởng phiên bản đang chạy, đội vận hành phải lên kế hoạch upgrade trong maintenance window được duyệt trước, có rollback plan nếu upgrade thất bại.

```
> request system software validate /var/tmp/junos-install-package.tgz
> request system software add /var/tmp/junos-install-package.tgz reboot
```

**Ưu điểm:**
- Vá lỗ hổng bảo mật, tăng tính ổn định, có tính năng mới.

**Nhược điểm:**
- Luôn có rủi ro downtime khi reboot (trừ khi có redundancy/ISSU).
- Một số phiên bản có thể có bug mới hoặc thay đổi hành vi (behavior change) gây ảnh hưởng cấu hình cũ — cần đọc kỹ release notes và test trên lab trước khi áp dụng production.

---

### 5.6 Troubleshooting

**Lý thuyết:** Là quy trình có hệ thống để xác định nguyên nhân gốc rễ (root cause) của sự cố, thường đi từ Layer thấp lên cao (bottom-up: Physical → Data Link → Network → Transport → Application) theo mô hình OSI.

**Mục đích:** Giảm thời gian khắc phục sự cố (MTTR - Mean Time To Repair), tránh đoán mò gây mất thời gian hoặc sửa sai chỗ.

**Thực tế áp dụng:** Khi khách hàng báo "mạng chậm", quy trình chuẩn: kiểm tra interface error/drop trước (Layer 1/2), rồi mới đến routing (Layer 3), rồi mới nghi ngờ ứng dụng/server (Layer 7) — tránh việc vội vàng nghi ngờ sai tầng gây lãng phí thời gian.

```
> show interfaces terse
> show route <prefix>
> monitor traffic interface <if>
```

**Ưu điểm:**
- Quy trình có hệ thống giúp xử lý nhanh, nhất quán dù ai trực ca cũng làm theo cùng 1 quy trình.

**Nhược điểm:**
- Đòi hỏi kỹ sư có kiến thức nền tảng vững (hiểu rõ OSI, giao thức) mới áp dụng hiệu quả — người mới dễ bỏ qua bước cơ bản.

---

### 5.7 Incident và Change Management

**Lý thuyết:** Là khung quy trình quản lý vận hành theo chuẩn ITIL — **Incident Management** xử lý sự cố đang xảy ra (khôi phục dịch vụ nhanh nhất), **Change Management** kiểm soát mọi thay đổi có kế hoạch (change request, approval, rollback plan) để tránh chính thay đổi lại là nguyên nhân gây sự cố mới.

**Mục đích:** Giảm rủi ro con người/thay đổi gây ra sự cố (thực tế phần lớn sự cố mạng lớn là do human error khi thay đổi cấu hình, không phải do lỗi phần cứng).

**Thực tế áp dụng:** Trước khi thay đổi cấu hình BGP trên router core giờ hành chính, phải có Change Request được duyệt, thông báo trước cho các bên liên quan, có kế hoạch rollback rõ ràng, và thực hiện trong maintenance window (thường là 12h đêm - ít ảnh hưởng người dùng).

**Ưu điểm:**
- Giảm rủi ro sự cố do thay đổi không kiểm soát, có trách nhiệm rõ ràng (ai duyệt, ai thực hiện).
- Có SLA rõ ràng cho từng mức độ ưu tiên sự cố (P1-P4), giúp tổ chức phản ứng đúng mức độ khẩn cấp.

**Nhược điểm:**
- Quy trình phê duyệt (approval) có thể làm chậm việc xử lý các thay đổi khẩn cấp nếu không có luồng "emergency change" riêng.
- Áp dụng cứng nhắc quy trình cho tổ chức nhỏ có thể gây quá tải thủ tục không cần thiết.

---

## GIAI ĐOẠN 6: AUTOMATION

### 6.1 NETCONF

**Lý thuyết:** NETCONF (RFC 6241) là giao thức quản lý cấu hình chuẩn IETF, dùng XML qua SSH, cho phép lấy/sửa cấu hình theo cách **có cấu trúc (structured)** và **transactional** (giống commit của Junos) — thay vì gửi lệnh CLI dạng text như con người gõ.

**Mục đích:** Cho phép hệ thống automation (Ansible, script Python) tương tác với thiết bị 1 cách đáng tin cậy, dễ parse, thay vì phải "scrape" text output của CLI (dễ vỡ khi vendor đổi format output).

**Thực tế áp dụng:** Hệ thống tự động hóa cấu hình cho 500 router chi nhánh mới mỗi tháng, dùng NETCONF để đẩy cấu hình theo template thay vì con người gõ tay từng router.

```
# set system services netconf ssh
```

**Ưu điểm:**
- Dữ liệu có cấu trúc (XML/YANG) → dễ tích hợp với công cụ automation, ít lỗi hơn parse text.
- Hỗ trợ transaction (commit/rollback) qua API, an toàn hơn khi tự động hóa hàng loạt.

**Nhược điểm:**
- Cần học thêm khái niệm XML/YANG data model, đường cong học tập cao hơn CLI thuần với người mới.
- Không phải mọi tính năng CLI đều có sẵn qua NETCONF ở mọi phiên bản Junos (cần kiểm tra RPC tương ứng).

---

### 6.2 Ansible

**Lý thuyết:** Ansible là công cụ automation **agentless** (không cần cài phần mềm trên thiết bị đích), dùng SSH/NETCONF kết nối, playbook viết theo YAML mô tả trạng thái mong muốn (declarative).

**Mục đích:** Tự động hóa các tác vụ lặp lại trên nhiều thiết bị cùng lúc (backup, đẩy cấu hình chuẩn, kiểm tra compliance) mà không cần viết code phức tạp — chỉ cần YAML dễ đọc.

**Thực tế áp dụng:** Đội NetOps của 1 ISP dùng Ansible để đẩy đồng loạt policy BGP mới cho 50 router PE trong 1 lệnh chạy playbook, thay vì login tay từng router mất cả ngày.

```yaml
- name: Backup Junos config
  hosts: all
  tasks:
    - name: Backup config
      juniper.device.command:
        commands: "show configuration | display set"
```

**Ưu điểm:**
- Không cần cài agent trên thiết bị, dễ triển khai nhanh.
- YAML dễ đọc, dễ review (code review) trước khi chạy trên production — giảm rủi ro sai sót.
- Cộng đồng lớn, nhiều module có sẵn (không phải viết từ đầu).

**Nhược điểm:**
- Không mạnh bằng ngôn ngữ lập trình đầy đủ (Python) khi cần logic phức tạp (điều kiện phức tạp, xử lý dữ liệu nâng cao).
- Chạy tuần tự/song song theo cấu hình mặc định — cần cấu hình kỹ (forks, strategy) để tối ưu tốc độ khi số lượng thiết bị lớn.

---

### 6.3 Junos PyEZ

**Lý thuyết:** PyEZ là thư viện Python chính thức của Juniper, wrap qua NETCONF, cung cấp API dễ dùng hơn để lấy facts, đẩy cấu hình, chạy RPC trực tiếp từ code Python.

**Mục đích:** Dùng khi cần logic tùy chỉnh phức tạp (mà Ansible module có sẵn không đáp ứng được), ví dụ: tính toán động, tích hợp với hệ thống khác (database, ticketing system), xử lý điều kiện phức tạp.

**Thực tế áp dụng:** Viết 1 script Python tự động: đọc danh sách VLAN cần tạo từ 1 file Excel/CSDL, sau đó tự sinh cấu hình và đẩy lên đúng switch tương ứng, đồng thời ghi log kết quả vào hệ thống ticket.

```python
from jnpr.junos import Device
dev = Device(host='10.0.0.1', user='admin', passwd='xxx')
dev.open()
print(dev.facts)
```

**Ưu điểm:**
- Linh hoạt tối đa vì là code Python thuần, tích hợp được với bất kỳ hệ thống nào khác (API, DB, message queue...).
- Truy cập trực tiếp RPC của Junos, không giới hạn bởi module có sẵn như Ansible.

**Nhược điểm:**
- Cần biết lập trình Python (rào cản với người chỉ quen CLI mạng thuần túy).
- Tự viết code nghĩa là tự chịu trách nhiệm xử lý lỗi (error handling), không có sẵn nhiều "rào chắn an toàn" như Ansible module đã được cộng đồng kiểm chứng.

---

### 6.4 Configuration Template (Jinja2)

**Lý thuyết:** Template engine (Jinja2) cho phép định nghĩa 1 khuôn mẫu cấu hình chung, sau đó "render" (điền biến số) ra cấu hình cụ thể cho từng thiết bị dựa trên dữ liệu đầu vào (biến, danh sách, điều kiện).

**Mục đích:** Đảm bảo tính nhất quán (consistency) khi cấu hình hàng loạt thiết bị giống nhau về mặt cấu trúc nhưng khác nhau về giá trị cụ thể (IP, tên, VLAN ID...), tránh sai sót do gõ tay lặp lại.

**Thực tế áp dụng:** Khi triển khai 200 chi nhánh mới có cấu trúc mạng giống hệt nhau (chỉ khác dải IP), dùng 1 template Jinja2 duy nhất kết hợp file dữ liệu (CSV/YAML chứa IP từng chi nhánh) để sinh ra 200 file cấu hình chính xác trong vài giây.

```jinja
set interfaces {{ ifname }} unit 0 family inet address {{ ip_address }}
```

**Ưu điểm:**
- Đảm bảo tính nhất quán, giảm lỗi con người khi cấu hình số lượng lớn thiết bị tương tự nhau.
- Tách biệt rõ ràng giữa "logic cấu hình" (template) và "dữ liệu" (variables) → dễ bảo trì, dễ audit.

**Nhược điểm:**
- Cần thời gian đầu tư xây dựng template chuẩn, không phù hợp nếu chỉ cấu hình 1-2 thiết bị đơn lẻ.
- Nếu thiết kế template không tốt (quá cứng nhắc), khó xử lý các trường hợp ngoại lệ (edge case) của từng site riêng biệt.

---

### 6.5 Automated Backup

**Lý thuyết:** Là việc kết hợp script (Python/Ansible) với lịch chạy tự động (cron, scheduler) để backup cấu hình định kỳ mà không cần con người can thiệp thủ công.

**Mục đích:** Đảm bảo luôn có bản backup mới nhất (thường là hằng ngày) sẵn sàng cho mọi thiết bị, giảm phụ thuộc vào việc con người "nhớ" backup thủ công (rất dễ bị quên).

**Thực tế áp dụng:** Cron job chạy lúc 2h sáng mỗi ngày, tự động backup toàn bộ 300 thiết bị trong hệ thống, lưu vào Git repository để có version history đầy đủ (biết chính xác cấu hình thay đổi gì giữa các ngày).

```bash
0 2 * * * /usr/bin/python3 /home/admin/backup_junos.py
```

**Ưu điểm:**
- Không phụ thuộc vào việc con người nhớ backup → giảm rủi ro mất dữ liệu cấu hình khi cần khôi phục khẩn cấp.
- Kết hợp Git → có lịch sử thay đổi rõ ràng, dễ so sánh (diff) giữa các version.

**Nhược điểm:**
- Cần giám sát riêng để đảm bảo job backup chạy thành công (backup lỗi âm thầm nhiều ngày liền là rủi ro thực tế phổ biến).
- Backup tự động không thay thế được kiểm tra thủ công trước các thay đổi lớn/quan trọng.

---

### 6.6 Compliance Check

**Lý thuyết:** Là việc so sánh cấu hình thực tế trên thiết bị với 1 baseline/policy chuẩn đã định nghĩa trước (ví dụ: bắt buộc phải có NTP, syslog, banner, password policy...), để phát hiện thiết bị nào "lệch chuẩn" (non-compliant).

**Mục đích:** Đảm bảo tính nhất quán và bảo mật trên toàn bộ hạ tầng, đặc biệt quan trọng khi cần đáp ứng các chuẩn audit (ISO 27001, PCI-DSS) hoặc đơn giản là tránh cấu hình thiếu sót do quên.

**Thực tế áp dụng:** Trước đợt audit bảo mật hàng năm, chạy script compliance check trên toàn bộ 300 thiết bị để đảm bảo 100% đã tắt Telnet, bật SSH v2, có NTP, có syslog đúng chuẩn công ty — thay vì kiểm tra thủ công mất hàng tuần.

```python
required_lines = ["set system ntp server", "set system syslog host"]
for line in required_lines:
    if line not in str(config_text):
        print(f"[NON-COMPLIANT] Missing: {line}")
```

**Ưu điểm:**
- Phát hiện sớm cấu hình sai lệch/thiếu sót trên diện rộng, tiết kiệm thời gian audit thủ công.
- Có thể tích hợp thành pipeline tự động chạy định kỳ, báo cáo cho quản lý.

**Nhược điểm:**
- Cần đầu tư thời gian ban đầu xây dựng bộ baseline/rule chuẩn phù hợp với tổ chức.
- Compliance check chỉ phát hiện "có/thiếu cấu hình theo rule đã định nghĩa" — không thay thế được đánh giá bảo mật chuyên sâu (penetration test).

---

## BỘ LAB NÊN LÀM (CHI TIẾT)

> Mỗi lab dưới đây nhằm minh họa trực tiếp 1 khái niệm lý thuyết đã học ở trên — làm lab xong nên tự hỏi "mình vừa chứng minh được lý thuyết gì".

### Lab 1: Cấu hình ban đầu cho router Juniper
**Minh họa lý thuyết:** CLI/hierarchy, commit, user/SSH — nền tảng bắt buộc trước khi làm bất cứ lab nào khác.

```
# set system host-name R1
# set system root-authentication plain-text-password
# set system login user admin class super-user authentication plain-text-password
# set system services ssh
# set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
# commit
```

### Lab 2: Hai PC ping qua hai router
**Minh họa lý thuyết:** Static route + preference — hiểu vì sao cần next-hop, vì sao route phải khớp 2 chiều (đi và về).

R1:
```
# set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
# set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.1/30
# set routing-options static route 192.168.2.0/24 next-hop 10.0.0.2
```
R2:
```
# set interfaces ge-0/0/0 unit 0 family inet address 192.168.2.1/24
# set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.2/30
# set routing-options static route 192.168.1.0/24 next-hop 10.0.0.1
```

### Lab 3: VLAN và Inter-VLAN routing
**Minh họa lý thuyết:** VLAN cô lập broadcast domain, IRB là cầu nối L2-L3.

```
# set vlans VLAN10 vlan-id 10
# set vlans VLAN20 vlan-id 20
# set interfaces irb unit 10 family inet address 192.168.10.1/24
# set interfaces irb unit 20 family inet address 192.168.20.1/24
# set vlans VLAN10 l3-interface irb.10
# set vlans VLAN20 l3-interface irb.20
```

### Lab 4: LACP giữa hai switch
**Minh họa lý thuyết:** LACP không block port như STP — thử rút 1 dây trong bó ae0 và quan sát traffic KHÔNG gián đoạn (khác hẳn STP phải chờ hội tụ).

```
# set interfaces ae0 aggregated-ether-options lacp active
# set interfaces ge-0/0/2 ether-options 802.3ad ae0
# set interfaces ge-0/0/3 ether-options 802.3ad ae0
```

### Lab 5: OSPF ba router
**Minh họa lý thuyết:** Link-state — quan sát `show ospf database` để thấy mỗi router đều có bản đồ topology giống hệt nhau (khác BGP path-vector).

```
# set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
# set protocols ospf area 0.0.0.0 interface lo0.0 passive
```

### Lab 6: IS-IS Level 2 bốn router
**Minh họa lý thuyết:** So sánh trực tiếp với Lab 5 (OSPF) - cùng là link-state nhưng khác cách định danh (NET address thay vì router-id kiểu IP).

```
# set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0001.00
# set protocols isis interface ge-0/0/0.0 level 2 metric 10
```

### Lab 7: iBGP và eBGP
**Minh họa lý thuyết:** Phân biệt rõ khi nào dùng type internal (cùng AS, dùng loopback) và external (khác AS, dùng IP trực tiếp) — đây là lỗi hay gặp nhất với người mới học BGP.

```
# set protocols bgp group IBGP type internal
# set protocols bgp group IBGP local-address <loopback>
# set protocols bgp group EBGP type external
# set protocols bgp group EBGP peer-as 65002
```

### Lab 8: BGP Route Reflector
**Minh họa lý thuyết:** Chứng minh 2 client không peer trực tiếp vẫn học được route của nhau qua RR — quan sát AS-path/next-hop để hiểu cơ chế reflect.

```
# set protocols bgp group RR-CLIENTS type internal
# set protocols bgp group RR-CLIENTS cluster <loopback-RR>
```

### Lab 9: Routing policy lọc prefix
**Minh họa lý thuyết:** Thứ tự xử lý term và default-reject — cố tình thử bỏ term "accept" cuối để thấy TOÀN BỘ route bị chặn (bài học quan trọng nhất của routing-policy).

```
# set policy-options policy-statement FILTER-OUT term BLOCK from prefix-list DENY-LIST
# set policy-options policy-statement FILTER-OUT term BLOCK then reject
```

### Lab 10: MPLS LDP trong mạng Core
**Minh họa lý thuyết:** Label switching — dùng `traceroute` để quan sát label thực tế được gắn vào gói tin khi đi qua core.

```
# set protocols mpls interface ge-0/0/0.0
# set protocols ldp interface ge-0/0/0.0
```

### Lab 11: MPLS L3VPN giữa hai khách hàng
**Minh họa lý thuyết:** Cô lập VRF — cố tình đặt 2 khách hàng dùng TRÙNG dải IP (ví dụ cả 2 đều dùng 192.168.1.0/24) để chứng minh VRF cô lập hoàn toàn, không xung đột.

```
# set routing-instances CUST-A instance-type vrf
# set routing-instances CUST-A route-distinguisher 65000:1
# set routing-instances CUST-A vrf-target target:65000:1
```

### Lab 12: Mô phỏng mất link và kiểm tra hội tụ
**Minh họa lý thuyết:** So sánh thời gian hội tụ giữa OSPF (giây) và BGP (có thể lâu hơn) — đo bằng ping liên tục khi cắt link.

```
# set interfaces ge-0/0/1 disable
# commit
```

### Lab 13: Gửi Syslog đến máy chủ Linux
**Minh họa lý thuyết:** Tập trung hóa log — thử tắt/bật interface và xác nhận log xuất hiện đồng thời trên cả router và server Linux.

```
# set system syslog host 10.0.0.100 any notice
```

### Lab 14: Giám sát Juniper bằng SNMP
**Minh họa lý thuyết:** Polling tự động — dùng `snmpwalk` để lấy dữ liệu mà không cần login SSH vào thiết bị.

```bash
snmpwalk -v2c -c public 10.0.0.1 system
```

### Lab 15: Backup cấu hình bằng Ansible hoặc Python
**Minh họa lý thuyết:** Automation thay thế thao tác thủ công — so sánh thời gian backup 1 thiết bị bằng tay (login, gõ lệnh, copy) với chạy script cho 10 thiết bị cùng lúc.

```python
from jnpr.junos import Device
dev = Device(host="10.0.0.1", user="admin", passwd="xxx")
dev.open()
config = dev.rpc.get_config(options={"format": "text"})
```

---

## CÔNG CỤ THỰC HÀNH ĐỀ XUẤT

| Công cụ | Mục đích | Ưu điểm | Nhược điểm |
|---|---|---|---|
| **GNS3 / EVE-NG** | Mô phỏng topology nhiều router/switch | Miễn phí, linh hoạt topology tùy ý | Cần máy cấu hình mạnh nếu chạy nhiều node |
| **vJunos-router/switch** | Ảo hóa chính thức Juniper | Nhẹ, chính thức, miễn phí | Vẫn cần license Juniper account để tải |
| **Juniper vLabs** | Lab cloud có sẵn kịch bản | Không cần cài đặt, có bài lab dựng sẵn | Giới hạn thời gian sử dụng, cần tài khoản |
| **Ansible + junos collection** | Automation | Dễ học, YAML dễ đọc | Hạn chế logic phức tạp |
| **Junos PyEZ** | Scripting Python | Linh hoạt tối đa | Cần biết lập trình |
| **Wireshark** | Phân tích gói tin | Trực quan, chi tiết từng byte | Cần hiểu sâu giao thức để đọc hiệu quả |

---

## GỢI Ý THỜI GIAN HỌC (THAM KHẢO)

- Giai đoạn 1-2: 2-3 tuần (cơ bản, làm quen CLI + switching)
- Giai đoạn 3: 3-4 tuần (routing là trọng tâm, cần làm kỹ OSPF/BGP)
- Giai đoạn 4: 4-6 tuần (MPLS/L3VPN khó, cần lab nhiều lần)
- Giai đoạn 5: song song với các giai đoạn trên, không tách riêng
- Giai đoạn 6: 2-3 tuần sau khi vững routing/switching

**Chứng chỉ liên quan** để định hướng học: JNCIA-Junos (cơ bản) → JNCIS-ENT/SP (switching/routing) → JNCIP-SP (MPLS/VPN nâng cao).

---

## GIAI ĐOẠN BỔ SUNG 1: HIGH AVAILABILITY (VRRP, GRES, NSR)

### A.1 VRRP (Virtual Router Redundancy Protocol)

**Lý thuyết:** VRRP (RFC 5798) cho phép 2 (hoặc nhiều) router chia sẻ **1 địa chỉ IP ảo (VIP)** làm default gateway chung. Router có priority cao nhất trở thành **Master** (trả lời ARP cho VIP), các router còn lại ở trạng thái **Backup**, sẵn sàng nhận vai trò Master nếu Master hiện tại chết (mất heartbeat).

**Mục đích:** Loại bỏ single point of failure ở tầng default gateway — nếu không có VRRP, PC chỉ cấu hình 1 gateway IP duy nhất, router đó chết là toàn bộ VLAN mất Internet dù có router dự phòng vật lý.

**Thực tế áp dụng:** VLAN Kế toán (192.168.10.0/24) có 2 switch Layer 3 (SW1, SW2) cùng chạy IRB — PC chỉ cần trỏ gateway về 192.168.10.1 (VIP), còn việc SW1 hay SW2 đang thực sự xử lý traffic là "vô hình" với PC.

```
# set interfaces irb unit 10 family inet address 192.168.10.2/24 vrrp-group 1 virtual-address 192.168.10.1
# set interfaces irb unit 10 family inet address 192.168.10.2/24 vrrp-group 1 priority 200
# set interfaces irb unit 10 family inet address 192.168.10.2/24 vrrp-group 1 preempt
# set interfaces irb unit 10 family inet address 192.168.10.2/24 vrrp-group 1 accept-data
```

Kiểm tra:
```
> show vrrp
> show vrrp detail
```

**Ưu điểm:**
- Failover default gateway hoàn toàn trong suốt với thiết bị đầu cuối (không cần cấu hình lại DHCP/gateway trên PC).
- Hội tụ nhanh (mặc định advertise 1s, có thể tùy chỉnh xuống mili-giây).

**Nhược điểm:**
- Chỉ 1 router active tại 1 thời điểm cho mỗi VRRP group → lãng phí tài nguyên router Backup (không như VRRP load-balancing nâng cao hoặc MC-LAG).
- Cấu hình sai priority hoặc quên preempt có thể khiến router yếu hơn "giữ" vai trò Master không mong muốn sau khi Master chính phục hồi.

---

### A.2 GRES & NSR (Graceful Restart / Nonstop Active Routing)

**Lý thuyết:** Trên các router có 2 Routing Engine (RE0/RE1 - dual RE), **GRES (Graceful Restart Switchover)** đồng bộ trạng thái kernel giữa 2 RE để khi RE Master chết, RE Backup tiếp quản mà **không cần reset lại forwarding**. **NSR (Nonstop Active Routing)** đi xa hơn — đồng bộ luôn cả trạng thái giao thức định tuyến (OSPF/BGP session) giữa 2 RE, nên khi switchover, session BGP/OSPF **không bị rớt**, hàng xóm mạng không hề biết có sự cố xảy ra.

**Mục đích:** Đảm bảo router chassis lớn (core/backbone) không downtime dù RE chính gặp sự cố phần cứng/phần mềm — cực kỳ quan trọng cho SLA 99.999% ("5 nines") của ISP.

**Thực tế áp dụng:** Router core MPLS của ISP có 2 RE — khi RE Master bị lỗi phần cứng, NSR giúp toàn bộ BGP/OSPF session (có thể hàng nghìn) không bị flap, tránh gây rung lắc (churn) toàn mạng.

```
# set chassis redundancy graceful-switchover
# set routing-options nonstop-routing
# set system commit synchronize
```

**Ưu điểm:**
- Chuyển đổi RE gần như 0 downtime cho control-plane, không ảnh hưởng session giao thức đang chạy.
- Bắt buộc phải có cho các thiết bị core/backbone yêu cầu SLA cao.

**Nhược điểm:**
- Chỉ áp dụng được trên phần cứng có dual RE (chi phí đầu tư cao hơn).
- Cấu hình/troubleshoot NSR phức tạp hơn, và một số tính năng/giao thức không hỗ trợ đầy đủ NSR (cần kiểm tra compatibility matrix của Juniper).

---

## GIAI ĐOẠN BỔ SUNG 2: SECURITY CƠ BẢN TRÊN ROUTER

### B.1 Firewall Filter (ACL trên Junos)

**Lý thuyết:** Firewall filter là cơ chế lọc gói tin dựa trên điều kiện (source/destination IP, port, protocol...) và hành động (accept/discard/reject/count/log), áp dụng theo `term` xử lý tuần tự từ trên xuống, tương tự cấu trúc routing-policy nhưng tác động lên traffic thay vì route.

**Mục đích:** Kiểm soát traffic nào được phép đi qua interface, hoặc quan trọng hơn — **bảo vệ chính router** khỏi traffic độc hại nhắm vào control-plane (CPU) của router.

**Thực tế áp dụng:** Chặn traffic SSH/Telnet quản trị router chỉ cho phép từ dải IP quản trị nội bộ, chặn mọi nguồn khác — giảm bề mặt tấn công (attack surface).

```
# set firewall family inet filter PROTECT-RE term ALLOW-MGMT from source-address 10.0.0.0/24
# set firewall family inet filter PROTECT-RE term ALLOW-MGMT from protocol tcp
# set firewall family inet filter PROTECT-RE term ALLOW-MGMT from destination-port ssh
# set firewall family inet filter PROTECT-RE term ALLOW-MGMT then accept
# set firewall family inet filter PROTECT-RE term DENY-ALL then discard
# set interfaces lo0 unit 0 family inet filter input PROTECT-RE
```

**Ưu điểm:**
- Bảo vệ trực tiếp control-plane router (lo0 filter) — chống DoS nhắm vào CPU router, một trong những kỹ thuật bảo mật quan trọng nhất cho router biên/Internet-facing.
- Có thể log/count traffic để phân tích, không chỉ chặn/cho qua.

**Nhược điểm:**
- Filter càng nhiều term càng ảnh hưởng hiệu năng xử lý (dù Junos xử lý filter ở ASIC/hardware nên tác động thường nhỏ).
- Cấu hình sai thứ tự term (default là deny-all cuối) dễ tự khóa quyền quản trị của chính mình từ xa — luôn test bằng `commit confirmed`.

### B.2 Unicast RPF (Reverse Path Forwarding)

**Lý thuyết:** uRPF kiểm tra gói tin đến có "hợp lý" không bằng cách so sánh source IP của gói với bảng định tuyến — nếu router không có route để **đi ngược lại** tới địa chỉ nguồn đó qua chính interface nhận gói, gói sẽ bị loại bỏ.

**Mục đích:** Chống **IP spoofing** — kỹ thuật giả mạo địa chỉ nguồn thường dùng trong tấn công DDoS (ví dụ DNS amplification).

**Thực tế áp dụng:** ISP bắt buộc bật uRPF (strict mode) trên interface khách hàng để đảm bảo khách hàng không thể gửi gói tin giả mạo IP nguồn không thuộc dải được cấp, tránh trở thành nguồn tấn công DDoS ra Internet.

```
# set interfaces ge-0/0/5 unit 0 family inet rpf-check
```

**Ưu điểm:**
- Ngăn chặn hiệu quả 1 lớp lớn tấn công DDoS dạng spoofing ngay tại nguồn (gần khách hàng), tốt hơn nhiều so với chặn ở xa.

**Nhược điểm:**
- Strict mode có thể gây false-positive (chặn nhầm) trong mạng có nhiều đường đi bất đối xứng (asymmetric routing) — cần dùng loose mode trong trường hợp này.

---

## GIAI ĐOẠN BỔ SUNG 3: QoS / CoS (CLASS OF SERVICE)

**Lý thuyết:** QoS (gọi là CoS trên Junos) phân loại traffic thành các lớp (forwarding class) dựa trên DSCP/CoS bit/EXP bit (MPLS), sau đó áp dụng scheduler (băng thông, hàng đợi ưu tiên) và policer (giới hạn tốc độ) khác nhau cho từng lớp khi có nghẽn (congestion).

**Mục đích:** Đảm bảo traffic quan trọng/nhạy cảm với độ trễ (voice, video call) được ưu tiên xử lý trước traffic ít quan trọng (file download, backup) khi băng thông không đủ cho tất cả cùng lúc — mạng không nghẽn thì QoS gần như "vô hình", QoS chỉ thực sự phát huy tác dụng khi có tắc nghẽn.

**Thực tế áp dụng:** Văn phòng có 1 đường Internet 100Mbps dùng chung cho gọi điện Zoom và đồng bộ file lên cloud — nếu không có QoS, lúc ai đó upload file lớn, cuộc gọi Zoom sẽ bị giật/đứt quãng vì gói tin voice bị xếp hàng chờ chung với gói tin file.

```
# set class-of-service classifiers dscp DSCP-CLASSIFIER forwarding-class EF loss-priority low code-points 101110
# set class-of-service interfaces ge-0/0/0 unit 0 classifiers dscp DSCP-CLASSIFIER
# set class-of-service forwarding-classes class EF queue-num 5
# set class-of-service schedulers VOICE-SCHED transmit-rate percent 30
# set class-of-service schedulers VOICE-SCHED priority strict-high
# set class-of-service scheduler-maps WAN-MAP forwarding-class EF scheduler VOICE-SCHED
# set class-of-service interfaces ge-0/0/1 scheduler-map WAN-MAP
```

Kiểm tra:
```
> show class-of-service interface ge-0/0/1
> show interfaces queue ge-0/0/1
```

**Ưu điểm:**
- Đảm bảo trải nghiệm dịch vụ nhạy cảm độ trễ (voice/video) ổn định ngay cả khi mạng gần bão hòa băng thông.
- Cho phép ISP bán nhiều gói dịch vụ khác cấp độ (Gold/Silver/Bronze) trên cùng hạ tầng vật lý.

**Nhược điểm:**
- Cấu hình phức tạp (classifier, forwarding-class, scheduler, rewrite rule) — nhiều lớp khái niệm dễ nhầm lẫn với người mới.
- QoS không "tạo thêm" băng thông — nếu tổng nhu cầu vượt xa dung lượng đường truyền trong thời gian dài, QoS chỉ giảm nhẹ tác động chứ không giải quyết được gốc rễ (vẫn cần nâng cấp băng thông).

---

## GIAI ĐOẠN BỔ SUNG 4: IPv6

**Lý thuyết:** IPv6 dùng địa chỉ 128-bit (thay vì 32-bit của IPv4), giải quyết vấn đề cạn kiệt địa chỉ IPv4 toàn cầu, đồng thời đơn giản hóa header và tích hợp sẵn cơ chế auto-configuration (SLAAC), bỏ NAT (theo thiết kế ban đầu là mỗi thiết bị có IP public riêng).

**Mục đích:** Hầu hết ISP/doanh nghiệp lớn hiện nay đều chạy **dual-stack** (song song cả IPv4 và IPv6) vì địa chỉ IPv4 công cộng đã cạn kiệt từ lâu, trong khi nhiều thiết bị/dịch vụ mới (mobile, IoT) yêu cầu hỗ trợ IPv6.

**Thực tế áp dụng:** ISP cấp cho khách hàng cả dải IPv4 (thường qua NAT/CGNAT vì thiếu IPv4) và dải IPv6 thật (không NAT), nên các thiết bị mạng (router CE/PE) đều phải cấu hình song song cả 2 family trên cùng interface.

```
# set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8::1/64
# set protocols ospf3 area 0.0.0.0 interface ge-0/0/0.0
# set protocols bgp group EBGP-V6 family inet6 unicast
# set routing-options rib inet6.0 static route ::/0 next-hop 2001:db8::254
```

Kiểm tra:
```
> show ipv6 neighbors
> show route table inet6.0
> ping6 2001:db8::2
```

**Ưu điểm:**
- Không gian địa chỉ gần như vô hạn, không cần NAT phức tạp cho end-to-end connectivity.
- SLAAC giúp thiết bị tự động nhận địa chỉ mà không cần DHCP (dù DHCPv6 vẫn tồn tại cho trường hợp cần kiểm soát chặt).

**Nhược điểm:**
- Đội ngũ vận hành cần học thêm khái niệm mới (link-local, SLAAC, NDP thay ARP) — dual-stack nghĩa là **gấp đôi** công sức cấu hình/troubleshoot (2 giao thức OSPF/OSPFv3, 2 policy BGP...).
- Một số công cụ/thói quen bảo mật cũ (dựa vào NAT như 1 lớp che chắn) không còn áp dụng trực tiếp với IPv6 full end-to-end — cần firewall filter rõ ràng hơn cho IPv6.

---

## GIAI ĐOẠN BỔ SUNG 5: CÔNG NGHỆ NÂNG CAO (SAU KHI VỮNG NỀN TẢNG)

### C.1 EVPN-VXLAN

**Lý thuyết:** VXLAN (RFC 7348) là kỹ thuật encapsulation đóng gói Ethernet frame vào UDP, tạo ra "Layer 2 overlay" chạy trên nền Layer 3 network — cho phép kéo dài 1 VLAN qua nhiều Data Center dù hạ tầng vật lý bên dưới là thuần IP. EVPN (Ethernet VPN, dùng MP-BGP) là control-plane hiện đại để phân phối thông tin MAC/IP giữa các VTEP (VXLAN Tunnel Endpoint), thay thế cho flood-and-learn truyền thống kém hiệu quả.

**Mục đích:** Là công nghệ chuẩn hiện nay cho Data Center hiện đại (Data Center Fabric, Spine-Leaf), dần thay thế MPLS L2VPN/VPLS truyền thống cho nhu cầu kéo dài Layer 2 giữa các site.

**Thực tế áp dụng:** Data Center có kiến trúc Spine-Leaf (2 tầng switch), cần di chuyển máy ảo (VM) giữa 2 Leaf switch khác nhau mà giữ nguyên IP (live migration) — EVPN-VXLAN cho phép 1 VLAN "trải" ra toàn bộ fabric dù về vật lý mỗi Leaf switch chỉ kết nối L3 thuần với Spine.

```
# set protocols bgp group EVPN family evpn signaling
# set vlans VLAN100 vxlan vni 10100
# set switch-options vtep-source-interface lo0.0
# set protocols evpn encapsulation vxlan
# set protocols evpn extended-vni-list all
```

**Ưu điểm:**
- Không giới hạn bởi STP/VLAN 4094 (VXLAN VNI có 24-bit → 16 triệu segment).
- Kiến trúc Spine-Leaf với EVPN cho phép scale ngang dễ dàng, ECMP (multi-path) tận dụng hết băng thông thay vì block port như STP.

**Nhược điểm:**
- Đường cong học tập cao, đòi hỏi hiểu vững cả BGP, VXLAN encapsulation, và khái niệm overlay/underlay tách biệt.
- Troubleshoot phức tạp hơn nhiều so với VLAN truyền thống (phải kiểm tra cả underlay lẫn overlay khi có sự cố).

### C.2 Multicast (PIM - Protocol Independent Multicast)

**Lý thuyết:** Multicast cho phép 1 nguồn gửi dữ liệu đến **nhiều người nhận cùng lúc** hiệu quả (1-to-many), mà không cần gửi lặp lại từng bản riêng như unicast. PIM-SM (Sparse Mode) là chế độ phổ biến nhất, dùng Rendezvous Point (RP) làm điểm gặp giữa nguồn (source) và người nhận (receiver) trước khi chuyển sang cây phân phối tối ưu (Shortest Path Tree).

**Mục đích:** Dùng cho các dịch vụ phát 1 nguồn tới nhiều điểm: IPTV, hội nghị truyền hình nhiều điểm, phân phối dữ liệu thị trường chứng khoán real-time tới nhiều bàn giao dịch.

**Thực tế áp dụng:** Nhà đài truyền hình cáp phát 200 kênh tới hàng nghìn thuê bao qua hạ tầng ISP — dùng multicast để chỉ gửi **1 luồng dữ liệu duy nhất** mỗi kênh vào mạng lõi, thay vì phải nhân bản luồng cho từng thuê bao (sẽ làm nghẽn băng thông core nếu dùng unicast).

```
# set protocols pim interface ge-0/0/0.0 mode sparse
# set protocols pim rp static address 10.1.1.1
# set protocols igmp interface ge-0/0/1.0
```

**Ưu điểm:**
- Tiết kiệm băng thông cực lớn cho các dịch vụ 1-nguồn-nhiều-người-nhận (so với unicast phải nhân bản luồng).

**Nhược điểm:**
- Thiết kế/troubleshoot phức tạp (RP, Shortest Path Tree, Rendezvous Point Tree...) — đòi hỏi kiến thức chuyên sâu, thường chỉ thấy trong network ISP/Telco lớn hoặc Data Center tài chính, ít gặp trong mạng doanh nghiệp thông thường.

---

## CÂU HỎI TỰ KIỂM TRA THEO TỪNG GIAI ĐOẠN

> Trả lời được hết các câu này trước khi coi như "xong" 1 giai đoạn. Đáp án gợi ý nằm ngay trong phần lý thuyết tương ứng ở trên — hãy tự tìm lại nếu chưa chắc.

**Giai đoạn 1:**
1. Sự khác biệt giữa candidate config và active config là gì? Tại sao Junos thiết kế như vậy?
2. `commit confirmed 5` giải quyết vấn đề gì mà `commit` thường không giải quyết được?
3. Interface vật lý và logical unit khác nhau thế nào? Cho ví dụ khi nào cần nhiều unit trên 1 interface.

**Giai đoạn 2:**
1. Tại sao cần IRB thay vì chỉ dùng VLAN đơn thuần?
2. STP và LACP cùng giải quyết vấn đề dự phòng link, nhưng khác nhau ở điểm mấu chốt nào?
3. Virtual Chassis giải quyết được hạn chế gì của STP truyền thống?

**Giai đoạn 3:**
1. Vì sao OSPF hội tụ nhanh hơn nhưng lại không scale tốt cho toàn bộ Internet như BGP?
2. Phân biệt khi nào dùng `type internal` và `type external` trong cấu hình BGP.
3. Nếu quên term "accept" cuối cùng trong 1 policy-statement, điều gì sẽ xảy ra? Vì sao?

**Giai đoạn 4:**
1. MPLS label giải quyết vấn đề gì mà IP routing thuần không làm được (trong bối cảnh multi-tenant)?
2. Route Distinguisher (RD) và Route Target (RT) khác nhau ở vai trò gì trong L3VPN?
3. Vì sao cần Route Reflector khi mạng có nhiều hơn vài chục router chạy iBGP?

**Giai đoạn 5:**
1. Vì sao NTP quan trọng khi troubleshoot sự cố liên quan nhiều thiết bị?
2. `transfer-on-commit` giải quyết rủi ro gì trong việc backup cấu hình?
3. Phân biệt vai trò của Incident Management và Change Management.

**Giai đoạn 6:**
1. Vì sao NETCONF phù hợp cho automation hơn là "scrape" output CLI dạng text?
2. Khi nào nên chọn Ansible, khi nào nên chọn viết script PyEZ thuần?
3. Compliance check giải quyết được vấn đề gì mà backup thông thường không giải quyết được?

**Giai đoạn bổ sung (HA/Security/QoS/IPv6):**
1. VRRP và LACP cùng là kỹ thuật dự phòng nhưng dự phòng ở tầng nào khác nhau?
2. uRPF strict mode có thể gây ra vấn đề gì trong mạng có routing bất đối xứng?
3. QoS có "tạo thêm" băng thông cho mạng không? Nếu không thì nó thực sự làm gì?

---

## CASE STUDY TROUBLESHOOTING THỰC TẾ

> Đọc triệu chứng, tự chẩn đoán trước khi xem gợi ý — đây là cách luyện tư duy troubleshooting thực chiến thay vì học thuộc lệnh.

**Case 1:** Hai router chạy OSPF nhưng `show ospf neighbor` mãi ở trạng thái `Init`, không lên `Full`.
> *Gợi ý chẩn đoán:* Kiểm tra area-id 2 bên có khớp không, subnet mask/MTU interface có khớp không, và đặc biệt là **authentication** (nếu 1 bên bật MD5 mà bên kia không, sẽ kẹt ở Init/ExStart chứ không báo lỗi rõ ràng).

**Case 2:** BGP session giữa 2 router ở trạng thái `Active` mãi không lên `Established`.
> *Gợi ý chẩn đoán:* Kiểm tra reachability tầng IP trước (`ping` tới neighbor IP) — BGP cần TCP port 179 mở 2 chiều, kiểm tra firewall filter trên lo0 có vô tình chặn port 179 không, và kiểm tra `peer-as` cấu hình có đúng AS number thực tế của neighbor không (sai AS number là lỗi phổ biến nhất).

**Case 3:** VLAN10 và VLAN20 không ping được nhau dù đã cấu hình IRB đầy đủ.
> *Gợi ý chẩn đoán:* Kiểm tra `show vlans` xem VLAN đã gán đúng `l3-interface irb.x` chưa, kiểm tra PC có đúng default gateway trỏ về IP của IRB không, và kiểm tra firewall filter (nếu có) trên IRB có chặn traffic giữa 2 subnet không.

**Case 4:** Sau khi thêm 1 dây cáp mới vào trunk port giữa 2 switch, toàn bộ mạng bị "đơ", ping timeout hàng loạt dù trước đó vẫn ổn.
> *Gợi ý chẩn đoán:* Nghi ngờ đầu tiên là **broadcast storm/loop** — kiểm tra `show spanning-tree interface` xem port mới có bị stuck ở trạng thái `Forwarding` thay vì `Blocking` không (STP không chạy hoặc bridge-priority cấu hình sai khiến 2 đường cùng forwarding).

**Case 5:** Khách hàng L3VPN báo không ping được sang site khác của chính họ, dù cấu hình PE có vẻ đúng.
> *Gợi ý chẩn đoán:* Kiểm tra `vrf-target` (Route Target) ở 2 PE có khớp nhau không (import/export) — sai RT là nguyên nhân phổ biến nhất khiến route VPN không được trao đổi giữa các PE dù mọi thứ khác đều đúng.

**Case 6:** Sau khi upgrade Junos, router mất kết nối SSH quản trị, phải ra tận nơi mới truy cập được.
> *Gợi ý chẩn đoán:* Đây là lý do vì sao luôn cần đọc release notes trước khi upgrade — nghi ngờ default behavior của SSH/service bị thay đổi giữa version, hoặc firewall filter/lo0 filter cấu hình cũ không còn tương thích cú pháp mới. Bài học: luôn có kế hoạch out-of-band access (console server) trước khi upgrade thiết bị ở xa.

---

*Tài liệu này là khung nội dung học tập kết hợp lý thuyết và thực hành; luôn đối chiếu với tài liệu chính thức Juniper TechLibrary (juniper.net/documentation) vì cú pháp có thể thay đổi nhẹ giữa các phiên bản Junos.*

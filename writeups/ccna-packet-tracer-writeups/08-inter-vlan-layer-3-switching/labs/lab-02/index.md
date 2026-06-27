---
layout: page-toc
title: "CCNA 08.02 - 4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing"
permalink: /writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/
toc: true
---

[← Quay lại danh sách Inter-VLAN Và Layer 3 Switching](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/)

| Field | Value |
| --- | --- |
| Dạng lab | Inter-VLAN Và Layer 3 Switching |
| File lab | `4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Cấu hình MLS làm Layer 3 Switch, định tuyến IPv4/IPv6 giữa các VLAN và kiểm tra kết nối tới Cloud |

> **Ghi chú:** Bài này không dùng router-on-a-stick. Thiết bị định tuyến chính là **MLS**. MLS vừa tạo VLAN, vừa cấu hình SVI cho từng VLAN, vừa bật `ip routing` và `ipv6 unicast-routing` để route giữa các VLAN.

## 1. Mục Tiêu Bài Lab

- Cấu hình cổng routed port `G0/2` trên MLS để kết nối ra Cloud.
- Tạo VLAN 10, VLAN 20, VLAN 30 và VLAN 99 trên MLS.
- Cấu hình SVI cho VLAN 10, 20, 30, 99 để làm default gateway cho các VLAN.
- Cấu hình trunk giữa MLS và S1, đồng thời giữ native VLAN là VLAN 99.
- Bật IPv4 routing trên MLS bằng `ip routing`.
- Bật IPv6 routing trên MLS bằng `ipv6 unicast-routing`.
- Kiểm tra kết nối nội bộ VLAN, liên VLAN và kết nối ra Cloud.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/topology.png)

![Instructions lab 02](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/instructions.png)

## 2. Bảng Địa Chỉ IP

### 2.1. MLS

| Thiết bị | Interface | IPv4 / Prefix | IPv6 / Prefix | Ghi chú |
| --- | --- | --- | --- | --- |
| MLS | VLAN 10 | `192.168.10.254/24` | `2001:db8:acad:10::1/64` | Gateway VLAN 10 |
| MLS | VLAN 20 | `192.168.20.254/24` | `2001:db8:acad:20::1/64` | Gateway VLAN 20 |
| MLS | VLAN 30 | `192.168.30.254/24` | `2001:db8:acad:30::1/64` | Gateway VLAN 30 |
| MLS | VLAN 99 | `192.168.99.254/24` | Không yêu cầu | Management VLAN / native VLAN |
| MLS | G0/2 | `209.165.200.225/30` | `2001:db8:acad:a::1/64` | Routed port đi Cloud |

> **Lưu ý:** `G0/2` trên MLS phải được chuyển từ switchport Layer 2 sang routed port Layer 3 bằng lệnh `no switchport` trước khi gán IP.

### 2.2. PC Và Switch Quản Trị

| Thiết bị | Interface | IPv4 / Prefix | IPv6 / Prefix | Default Gateway |
| --- | --- | --- | --- | --- |
| PC0 | NIC | `192.168.10.1/24` | Không yêu cầu | `192.168.10.254` |
| PC1 | NIC | `192.168.20.1/24` | Không yêu cầu | `192.168.20.254` |
| PC2 | NIC | `192.168.30.1/24` | Không yêu cầu | `192.168.30.254` |
| PC3 | NIC | `192.168.10.2/24` | `2001:db8:acad:10::2/64` | `192.168.10.254` / `2001:db8:acad:10::1` |
| PC4 | NIC | `192.168.20.2/24` | `2001:db8:acad:20::2/64` | `192.168.20.254` / `2001:db8:acad:20::1` |
| PC5 | NIC | `192.168.30.2/24` | `2001:db8:acad:30::2/64` | `192.168.30.254` / `2001:db8:acad:30::1` |
| S1 | VLAN 99 | `192.168.99.1/24` | Không yêu cầu | `192.168.99.254` |
| S2 | VLAN 99 | `192.168.99.2/24` | Không yêu cầu | `192.168.99.254` |
| S3 | VLAN 99 | `192.168.99.3/24` | Không yêu cầu | `192.168.99.254` |

> **Lưu ý:** PC5 thuộc VLAN 30 nên IPv6 phải nằm trong prefix `2001:db8:acad:30::/64`. Nếu trong đề hiển thị nhầm sang `2001:db8:acad:10::2/64`, khi làm thực tế nên bám theo topology/VLAN 30 hoặc bảng chấm điểm trong file `.pka`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Core/Layer 3 | MLS | Định tuyến giữa VLAN 10, 20, 30, 99 và kết nối Cloud qua `G0/2` |
| Distribution/Access trung tâm | S1 | Kết nối trunk lên MLS và xuống các switch access |
| Access trái | S2, PC0, PC1, PC2 | Các PC thuộc VLAN 10, 20, 30 |
| Access phải | S3, PC3, PC4, PC5 | Các PC thuộc VLAN 10, 20, 30; PC3-PC5 dùng thêm IPv6 |
| External | Cloud | Dùng để kiểm tra routed port IPv4/IPv6 ra ngoài |

> **Điểm dễ sai:** Cấu hình SVI xong nhưng quên `ip routing` thì các VLAN vẫn chưa route được với nhau. Cấu hình IPv6 address xong nhưng quên `ipv6 unicast-routing` thì IPv6 inter-VLAN routing cũng không hoạt động đúng.

## 4. Part 1 - Configure Layer 3 Switching

### 4.1. Cấu hình `G0/2` trên MLS thành routed port

```text
MLS> enable
MLS# configure terminal

MLS(config)# interface gigabitethernet 0/2
MLS(config-if)# no switchport
MLS(config-if)# ip address 209.165.200.225 255.255.255.252
MLS(config-if)# description Routed link to Cloud
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

> **Lưu ý:** Nếu chưa có `no switchport`, MLS sẽ xem `G0/2` như cổng Layer 2 nên không gán được IPv4 trực tiếp lên interface.

### 4.2. Kiểm tra kết nối từ MLS tới Cloud

```text
MLS# ping 209.165.200.226

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 209.165.200.226, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5)
```

![Ping Cloud IPv4](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/ping-cloud-ipv4.png)

## 5. Part 2 - Configure IPv4 Inter-VLAN Routing

### 5.1. Tạo VLAN trên MLS

```text
MLS# configure terminal

MLS(config)# vlan 10
MLS(config-vlan)# name Staff
MLS(config-vlan)# exit

MLS(config)# vlan 20
MLS(config-vlan)# name Student
MLS(config-vlan)# exit

MLS(config)# vlan 30
MLS(config-vlan)# name Faculty
MLS(config-vlan)# exit

MLS(config)# vlan 99
MLS(config-vlan)# name Management
MLS(config-vlan)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

> **Lưu ý:** Packet Tracer có thể chấm phân biệt hoa/thường với tên VLAN. Nên nhập đúng `Staff`, `Student`, `Faculty`.

### 5.2. Cấu hình SVI IPv4 trên MLS

```text
MLS# configure terminal

MLS(config)# interface vlan 10
MLS(config-if)# ip address 192.168.10.254 255.255.255.0
MLS(config-if)# description Default gateway for VLAN 10 - Staff
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# interface vlan 20
MLS(config-if)# ip address 192.168.20.254 255.255.255.0
MLS(config-if)# description Default gateway for VLAN 20 - Student
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# interface vlan 30
MLS(config-if)# ip address 192.168.30.254 255.255.255.0
MLS(config-if)# description Default gateway for VLAN 30 - Faculty
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# interface vlan 99
MLS(config-if)# ip address 192.168.99.254 255.255.255.0
MLS(config-if)# description Management and native VLAN gateway
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

### 5.3. Cấu hình trunk trên MLS

```text
MLS# configure terminal

MLS(config)# interface gigabitethernet 0/1
MLS(config-if)# description Trunk link to S1
MLS(config-if)# switchport trunk encapsulation dot1q
MLS(config-if)# switchport mode trunk
MLS(config-if)# switchport trunk native vlan 99
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

> **Lưu ý:** Một số phiên bản Packet Tracer có thể không chấm hoặc không hỗ trợ đầy đủ `switchport trunk encapsulation dot1q`, nhưng với multilayer switch thì nên nhập lệnh này nếu IOS cho phép.

### 5.4. Cấu hình trunk và VLAN quản trị trên S1

```text
S1> enable
S1# configure terminal

S1(config)# interface gigabitethernet 0/1
S1(config-if)# description Trunk link to MLS
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk native vlan 99
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# interface vlan 99
S1(config-if)# ip address 192.168.99.1 255.255.255.0
S1(config-if)# description Management interface
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# ip default-gateway 192.168.99.254
S1(config)# end
S1# copy running-config startup-config
```

### 5.5. Cấu hình VLAN quản trị trên S2 và S3 nếu cần

```text
S2> enable
S2# configure terminal

S2(config)# interface vlan 99
S2(config-if)# ip address 192.168.99.2 255.255.255.0
S2(config-if)# description Management interface
S2(config-if)# no shutdown
S2(config-if)# exit

S2(config)# ip default-gateway 192.168.99.254
S2(config)# end
S2# copy running-config startup-config
```

```text
S3> enable
S3# configure terminal

S3(config)# interface vlan 99
S3(config-if)# ip address 192.168.99.3 255.255.255.0
S3(config-if)# description Management interface
S3(config-if)# no shutdown
S3(config-if)# exit

S3(config)# ip default-gateway 192.168.99.254
S3(config)# end
S3# copy running-config startup-config
```

> **Lưu ý:** Nếu S2/S3 đã được cấu hình sẵn trong file `.pka`, chỉ cần kiểm tra bằng `show ip interface brief` và `ping 192.168.99.254`.

### 5.6. Bật IPv4 routing trên MLS

```text
MLS# show ip route
! Trước khi bật ip routing, MLS chưa có đầy đủ bảng định tuyến Layer 3 giữa các VLAN.

MLS# configure terminal
MLS(config)# ip routing
MLS(config)# end
MLS# copy running-config startup-config

MLS# show ip route
```

Kết quả cần thấy:

```text
C    192.168.10.0/24 is directly connected, Vlan10
C    192.168.20.0/24 is directly connected, Vlan20
C    192.168.30.0/24 is directly connected, Vlan30
C    192.168.99.0/24 is directly connected, Vlan99
C    209.165.200.224/30 is directly connected, GigabitEthernet0/2
```

| Câu hỏi | Trả lời |
| --- | --- |
| Trước khi nhập `ip routing`, `show ip route` có route hoạt động không? | Chưa có đầy đủ route Layer 3 cho inter-VLAN routing. |
| Lệnh bật định tuyến IPv4 trên multilayer switch là gì? | `ip routing` |
| Ký hiệu `C` trong bảng định tuyến nghĩa là gì? | Connected route, mạng kết nối trực tiếp vào MLS. |

![Show IP route MLS](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/show-ip-route-mls.png)

### 5.7. Kiểm tra IPv4 inter-VLAN routing

```text
! Kiểm tra cùng VLAN 10
PC0> ping 192.168.10.2

! Kiểm tra cùng VLAN 20
PC1> ping 192.168.20.2

! Kiểm tra cùng VLAN 30
PC2> ping 192.168.30.2

! Kiểm tra VLAN quản trị
S1# ping 192.168.99.2
S1# ping 192.168.99.3
S1# ping 192.168.99.254

! Kiểm tra khác VLAN
PC0> ping 192.168.20.2
PC0> ping 192.168.30.2
PC1> ping 192.168.10.2
PC2> ping 192.168.20.2

! Kiểm tra ra Cloud
PC0> ping 209.165.200.226
```

![IPv4 inter VLAN ping](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/ipv4-inter-vlan-ping.png)

## 6. Part 3 - Configure IPv6 Inter-VLAN Routing

### 6.1. Bật IPv6 routing trên MLS

```text
MLS# configure terminal
MLS(config)# ipv6 unicast-routing
MLS(config)# end
MLS# copy running-config startup-config
```

> **Lưu ý:** `ipv6 address` chỉ gán địa chỉ IPv6 cho interface. Muốn MLS route IPv6 giữa các VLAN thì phải bật thêm `ipv6 unicast-routing`.

### 6.2. Cấu hình IPv6 cho các SVI trên MLS

```text
MLS# configure terminal

MLS(config)# interface vlan 10
MLS(config-if)# ipv6 address 2001:db8:acad:10::1/64
MLS(config-if)# exit

MLS(config)# interface vlan 20
MLS(config-if)# ipv6 address 2001:db8:acad:20::1/64
MLS(config-if)# exit

MLS(config)# interface vlan 30
MLS(config-if)# ipv6 address 2001:db8:acad:30::1/64
MLS(config-if)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

### 6.3. Cấu hình IPv6 cho routed port `G0/2`

```text
MLS# configure terminal

MLS(config)# interface gigabitethernet 0/2
MLS(config-if)# ipv6 address 2001:db8:acad:a::1/64
MLS(config-if)# no shutdown
MLS(config-if)# exit

MLS(config)# end
MLS# copy running-config startup-config
```

### 6.4. Kiểm tra bảng định tuyến IPv6

```text
MLS# show ipv6 route
```

Kết quả cần thấy:

```text
C   2001:DB8:ACAD:A::/64 [0/0]
    via ::, GigabitEthernet0/2
C   2001:DB8:ACAD:10::/64 [0/0]
    via ::, Vlan10
C   2001:DB8:ACAD:20::/64 [0/0]
    via ::, Vlan20
C   2001:DB8:ACAD:30::/64 [0/0]
    via ::, Vlan30
```

![Show IPv6 route MLS](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/show-ipv6-route-mls.png)

### 6.5. Kiểm tra IPv6 connectivity

```text
! PC3 kiểm tra gateway VLAN 10
PC3> ping 2001:db8:acad:10::1

! PC4 kiểm tra gateway VLAN 20
PC4> ping 2001:db8:acad:20::1

! PC5 kiểm tra gateway VLAN 30
PC5> ping 2001:db8:acad:30::1

! Kiểm tra IPv6 inter-VLAN
PC3> ping 2001:db8:acad:20::2
PC3> ping 2001:db8:acad:30::2
PC4> ping 2001:db8:acad:10::2

! Kiểm tra IPv6 ra Cloud
PC3> ping 2001:db8:acad:a::2
```

![IPv6 inter VLAN ping](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-02/ipv6-inter-vlan-ping.png)

## 7. Kiểm Tra Và Bằng Chứng

| Kiểm tra | Lệnh | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- | --- |
| VLAN đã tạo | `show vlan brief` | Có VLAN 10 Staff, 20 Student, 30 Faculty, 99 Management | `show-vlan-brief.png` |
| Trunk MLS-S1 | `show interfaces trunk` | `G0/1` trunk, native VLAN 99 | `show-trunk.png` |
| Routed port MLS | `show ip interface brief` | `G0/2` có `209.165.200.225`, trạng thái up/up | `show-ip-int-brief.png` |
| IPv4 routing | `show ip route` | Có connected route cho VLAN 10, 20, 30, 99 và Cloud | `show-ip-route-mls.png` |
| IPv6 routing | `show ipv6 route` | Có connected route IPv6 cho VLAN 10, 20, 30 và Cloud | `show-ipv6-route-mls.png` |
| Ping cùng VLAN | `ping` giữa 2 PC cùng VLAN | Thành công | `ping-same-vlan.png` |
| Ping khác VLAN IPv4 | PC0 ping PC4/PC5 | Thành công | `ipv4-inter-vlan-ping.png` |
| Ping khác VLAN IPv6 | PC3 ping PC4/PC5 IPv6 | Thành công | `ipv6-inter-vlan-ping.png` |
| Ping Cloud | Ping `209.165.200.226` và `2001:db8:acad:a::2` | Thành công | `ping-cloud.png` |

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC khác VLAN không ping được nhau | Chưa bật `ip routing` trên MLS | `show ip route` không có đủ connected route | Vào global config nhập `ip routing` |
| IPv6 khác VLAN không ping được | Chưa bật `ipv6 unicast-routing` | `show ipv6 route` thiếu route hoặc ping IPv6 fail | Nhập `ipv6 unicast-routing` |
| Không ping được Cloud IPv4 | `G0/2` chưa thành routed port hoặc sai IP | `show ip interface brief` không thấy IP trên `G0/2` | `interface g0/2`, `no switchport`, gán IP đúng |
| SVI VLAN bị down | VLAN chưa tồn tại hoặc không có port/trunk active trong VLAN | `show ip interface brief` thấy VLAN down/down | Tạo VLAN, kiểm tra trunk/access port |
| Trunk không chạy | Cổng MLS/S1 chưa `switchport mode trunk` hoặc sai native VLAN | `show interfaces trunk` không thấy cổng trunk | Cấu hình trunk và native VLAN 99 ở hai đầu |
| Ping cùng VLAN được nhưng khác VLAN fail | Gateway PC sai hoặc thiếu SVI | Kiểm tra IP Configuration trên PC | Đặt default gateway theo SVI của VLAN |
| PC5 IPv6 không ping đúng VLAN | IPv6 bị nhập nhầm prefix VLAN 10 | `ipconfig` trên PC5 thấy prefix không khớp VLAN 30 | Đặt `2001:db8:acad:30::2/64` và gateway `2001:db8:acad:30::1` |

## 9. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| MLS `G0/2` hoạt động Layer 3 | Ping được `209.165.200.226` | Hoàn thành |
| VLAN 10/20/30/99 | Tạo đúng VLAN và tên VLAN | Hoàn thành |
| SVI IPv4 | VLAN 10, 20, 30, 99 có gateway IPv4 | Hoàn thành |
| Trunk MLS-S1 | Trunk hoạt động, native VLAN 99 | Hoàn thành |
| IPv4 inter-VLAN routing | PC khác VLAN ping được nhau | Hoàn thành |
| IPv6 inter-VLAN routing | PC3, PC4, PC5 ping IPv6 qua VLAN khác | Hoàn thành |
| Kết nối Cloud | Ping IPv4/IPv6 tới Cloud thành công | Hoàn thành |
| Lưu cấu hình | `copy running-config startup-config` trên MLS/S1/S2/S3 | Hoàn thành |

Checklist ảnh minh chứng cần chèn:

- [ ] `topology.png`
- [ ] `show-vlan-brief.png`
- [ ] `show-trunk.png`
- [ ] `show-ip-int-brief.png`
- [ ] `show-ip-route-mls.png`
- [ ] `show-ipv6-route-mls.png`
- [ ] `ipv4-inter-vlan-ping.png`
- [ ] `ipv6-inter-vlan-ping.png`
- [ ] `ping-cloud.png`
- [ ] `check-results.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 4 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-01/">Lab 1: 4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/">Lab 3: 4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-04/">Lab 4: 4.5.1 Packet Tracer - Inter-VLAN Routing Challenge</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 05.06 - 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-06/` |
| Trạng thái | Chia subnet IPv6 liên tiếp từ `2001:db8:acad:00c8::/64`, cấu hình R1/R2, Auto Config PC và kiểm tra ping IPv6 |

> Bài này không chia IPv4 theo số host như VLSM truyền thống. Với IPv6, mỗi LAN vẫn dùng prefix `/64`. Phần cần làm là tăng subnet ID theo hệ thập lục phân: `00c8`, `00c9`, `00ca`, `00cb`, `00cc`.

## 1. Mục Tiêu Bài Lab

- Xác định các subnet IPv6 liên tiếp từ subnet ban đầu `2001:db8:acad:00c8::/64`.
- Gán subnet cho 4 LAN và 1 đường WAN point-to-point giữa `R1` và `R2`.
- Cấu hình IPv6 global unicast address cho các interface của `R1` và `R2`.
- Cấu hình link-local address theo yêu cầu: `R1` dùng `fe80::1`, `R2` dùng `fe80::2`.
- Bật IPv6 routing trên router.
- Cấu hình `Auto Config` cho `PC1`, `PC2`, `PC3`, `PC4`.
- Kiểm tra các PC ping IPv6 được nhau.

![Topology lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/topology.png)

![Topology lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/topology1.png)

## 2. Topology Và Yêu Cầu Subnet

| Khu vực | Thiết bị liên quan | Interface router | Subnet cần dùng | Ghi chú |
| --- | --- | --- | --- | --- |
| LAN PC1 | PC1, switch, R1 | R1 `G0/0` | Subnet đầu tiên | Đã cho sẵn `2001:db8:acad:00c8::/64` |
| LAN PC2 | PC2, switch, R1 | R1 `G0/1` | Subnet kế tiếp | Tăng `00c8` lên `00c9` |
| LAN PC3 | PC3, switch, R2 | R2 `G0/0` | Subnet kế tiếp | Tăng tiếp lên `00ca` |
| LAN PC4 | PC4, switch, R2 | R2 `G0/1` | Subnet kế tiếp | Tăng tiếp lên `00cb` |
| WAN R1-R2 | R1, R2 | `S0/0/0` | Subnet kế tiếp | Tăng tiếp lên `00cc` |

> **Lưu ý:** Trong IPv6, chữ `a`, `b`, `c`, `d`, `e`, `f` là số hợp lệ vì IPv6 viết theo hệ thập lục phân. Vì vậy sau `00c9` sẽ là `00ca`, không phải `00c10`.

## 3. Thiết Kế Subnet IPv6

### 3.1. Cách tăng subnet IPv6 trong bài này

Subnet ban đầu:

```text
2001:db8:acad:00c8::/64
```

IPv6 gồm các nhóm 16-bit, cách nhau bằng dấu `:`:

```text
2001 : db8 : acad : 00c8 : 0000 : 0000 : 0000 : 0000
```

Với prefix `/64`, 4 nhóm đầu là phần mạng:

```text
2001:db8:acad:00c8
```

Muốn tạo subnet tiếp theo, tăng nhóm thứ 4 lên 1 đơn vị theo hệ hex:

```text
00c8 → 00c9 → 00ca → 00cb → 00cc
```

### 3.2. Subnet Table

| Subnet | Address |
| --- | --- |
| R1 G0/0 LAN | `2001:db8:acad:00c8::/64` |
| R1 G0/1 LAN | `2001:db8:acad:00c9::/64` |
| R2 G0/0 LAN | `2001:db8:acad:00ca::/64` |
| R2 G0/1 LAN | `2001:db8:acad:00cb::/64` |
| R1 to R2 link network | `2001:db8:acad:00cc::/64` |

> **Lưu ý:** `::` là cách viết rút gọn các nhóm toàn số 0. Ví dụ `2001:db8:acad:00c8::/64` tương đương `2001:db8:acad:00c8:0000:0000:0000:0000/64`.

## 4. Bảng Địa Chỉ IPv6 Hoàn Chỉnh

| Device | Interface | IPv6 Address / Prefix | Link-local Address | Ghi chú |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:acad:00c8::1/64` | `fe80::1` | Gateway LAN PC1 |
| R1 | G0/1 | `2001:db8:acad:00c9::1/64` | `fe80::1` | Gateway LAN PC2 |
| R1 | S0/0/0 | `2001:db8:acad:00cc::1/64` | `fe80::1` | WAN sang R2 |
| R2 | G0/0 | `2001:db8:acad:00ca::1/64` | `fe80::2` | Gateway LAN PC3 |
| R2 | G0/1 | `2001:db8:acad:00cb::1/64` | `fe80::2` | Gateway LAN PC4 |
| R2 | S0/0/0 | `2001:db8:acad:00cc::2/64` | `fe80::2` | WAN sang R1 |
| PC1 | NIC | Auto Config | Tự nhận qua RA | Thuộc subnet `00c8::/64` |
| PC2 | NIC | Auto Config | Tự nhận qua RA | Thuộc subnet `00c9::/64` |
| PC3 | NIC | Auto Config | Tự nhận qua RA | Thuộc subnet `00ca::/64` |
| PC4 | NIC | Auto Config | Tự nhận qua RA | Thuộc subnet `00cb::/64` |

> **Lưu ý:** `fe80::1` trên R1 có thể dùng lặp lại ở nhiều interface vì link-local chỉ có hiệu lực trong phạm vi từng đường link. Tương tự, R2 có thể dùng `fe80::2` trên nhiều interface.

## 5. Cấu Hình Từng Part

## Part 1: Determine IPv6 Subnets and Addressing Scheme

### Step 1: Điền bảng subnet IPv6

| Subnet | Gán cho | Network / Prefix | Router IP |
| --- | --- | --- | --- |
| Subnet 1 | R1 G0/0 LAN | `2001:db8:acad:00c8::/64` | `2001:db8:acad:00c8::1/64` |
| Subnet 2 | R1 G0/1 LAN | `2001:db8:acad:00c9::/64` | `2001:db8:acad:00c9::1/64` |
| Subnet 3 | R2 G0/0 LAN | `2001:db8:acad:00ca::/64` | `2001:db8:acad:00ca::1/64` |
| Subnet 4 | R2 G0/1 LAN | `2001:db8:acad:00cb::/64` | `2001:db8:acad:00cb::1/64` |
| Subnet 5 | WAN R1-R2 | `2001:db8:acad:00cc::/64` | R1: `::1`, R2: `::2` |


## Part 2: Configure IPv6 Addressing on Routers

### Step 1: Cấu hình Router R1

```text
R1> enable
R1# configure terminal

R1(config)# ipv6 unicast-routing

R1(config)# interface gigabitethernet0/0
R1(config-if)# description LAN PC1 - 2001:db8:acad:00c8::/64
R1(config-if)# ipv6 address 2001:db8:acad:00c8::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface gigabitethernet0/1
R1(config-if)# description LAN PC2 - 2001:db8:acad:00c9::/64
R1(config-if)# ipv6 address 2001:db8:acad:00c9::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface serial0/0/0
R1(config-if)# description WAN to R2 - 2001:db8:acad:00cc::/64
R1(config-if)# ipv6 address 2001:db8:acad:00cc::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# ipv6 route 2001:db8:acad:00ca::/64 2001:db8:acad:00cc::2
R1(config)# ipv6 route 2001:db8:acad:00cb::/64 2001:db8:acad:00cc::2

R1(config)# end
R1# copy running-config startup-config
```

> `ipv6 unicast-routing` phải được bật để router gửi Router Advertisement cho PC Auto Config và định tuyến IPv6 giữa các interface.

### Step 2: Cấu hình Router R2

```text
R2> enable
R2# configure terminal

R2(config)# ipv6 unicast-routing

R2(config)# interface gigabitethernet0/0
R2(config-if)# description LAN PC3 - 2001:db8:acad:00ca::/64
R2(config-if)# ipv6 address 2001:db8:acad:00ca::1/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

R2(config)# interface gigabitethernet0/1
R2(config-if)# description LAN PC4 - 2001:db8:acad:00cb::/64
R2(config-if)# ipv6 address 2001:db8:acad:00cb::1/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

R2(config)# interface serial0/0/0
R2(config-if)# description WAN to R1 - 2001:db8:acad:00cc::/64
R2(config-if)# ipv6 address 2001:db8:acad:00cc::2/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

R2(config)# ipv6 route 2001:db8:acad:00c8::/64 2001:db8:acad:00cc::1
R2(config)# ipv6 route 2001:db8:acad:00c9::/64 2001:db8:acad:00cc::1

R2(config)# end
R2# copy running-config startup-config
```

> Nếu serial link vẫn `down/down` hoặc `up/down`, kiểm tra đầu DCE. Interface DCE cần thêm `clock rate 64000` trước lệnh `no shutdown`.

### Step 3: Kiểm tra router interfaces

```text
R1# show ipv6 interface brief
R2# show ipv6 interface brief

! Kết quả mong muốn: các cổng G0/0, G0/1, S0/0/0 đều up/up và có IPv6 đúng bảng
```

### Step 4: Kiểm tra IPv6 routing

```text
R1# show ipv6 route
R2# show ipv6 route

! R1 cần thấy static route đến 2001:db8:acad:00ca::/64 và 2001:db8:acad:00cb::/64
! R2 cần thấy static route đến 2001:db8:acad:00c8::/64 và 2001:db8:acad:00c9::/64
```


## Part 3: Configure IPv6 Addressing on PCs

### Step 1: Đặt Auto Config cho PC

| PC | Thao tác | Địa chỉ mong muốn |
| --- | --- | --- |
| PC1 | Desktop → IP Configuration → IPv6 → Auto Config | Thuộc `2001:db8:acad:00c8::/64` |
| PC2 | Desktop → IP Configuration → IPv6 → Auto Config | Thuộc `2001:db8:acad:00c9::/64` |
| PC3 | Desktop → IP Configuration → IPv6 → Auto Config | Thuộc `2001:db8:acad:00ca::/64` |
| PC4 | Desktop → IP Configuration → IPv6 → Auto Config | Thuộc `2001:db8:acad:00cb::/64` |

> **Lưu ý:** PC dùng Auto Config sẽ tự lấy prefix từ Router Advertisement của router. Vì vậy PC không cần nhập thủ công IPv6 address, nhưng router interface cùng LAN phải đang `up/up`.

![PC Auto Config lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/pc-auto-config.png)

### Step 2: Kiểm tra IPv6 trên PC

```text
PC> ipconfig

! PC1 cần nhận IPv6 thuộc 2001:db8:acad:00c8::/64
! PC2 cần nhận IPv6 thuộc 2001:db8:acad:00c9::/64
! PC3 cần nhận IPv6 thuộc 2001:db8:acad:00ca::/64
! PC4 cần nhận IPv6 thuộc 2001:db8:acad:00cb::/64
```

## Part 4: Verify IPv6 Connectivity

### Step 1: Ping gateway của từng PC

```text
! Từ PC1
PC> ping 2001:db8:acad:00c8::1

! Từ PC2
PC> ping 2001:db8:acad:00c9::1

! Từ PC3
PC> ping 2001:db8:acad:00ca::1

! Từ PC4
PC> ping 2001:db8:acad:00cb::1
```

### Step 2: Ping giữa các router qua WAN

```text
! Trên R1
R1# ping 2001:db8:acad:00cc::2

! Trên R2
R2# ping 2001:db8:acad:00cc::1
```

![WAN ping IPv6 lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/wan-ping-ipv6.png)

### Step 3: Ping giữa các PC

```text
! Trên PC1, ping sang các PC khác bằng IPv6 Auto Config của từng PC
PC> ping <IPv6-cua-PC2>
PC> ping <IPv6-cua-PC3>
PC> ping <IPv6-cua-PC4>

! Có thể xem IPv6 của từng PC bằng lệnh ipconfig trên chính PC đó
```

![PC to PC ping IPv6 lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/pc-to-pc-ping-ipv6.png)

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC không nhận IPv6 Auto Config | Router interface cùng LAN chưa up hoặc chưa bật IPv6 routing | `ipconfig` không có IPv6 global đúng prefix | Kiểm tra `no shutdown` và `ipv6 unicast-routing` |
| Router có IPv6 nhưng PC khác mạng không ping được | Thiếu route IPv6 giữa R1 và R2 | Ping gateway được nhưng ping PC khác LAN fail | Thêm static route IPv6 đến các subnet remote |
| Serial link không up | Một đầu serial shutdown hoặc thiếu clock rate ở đầu DCE | `show ipv6 interface brief` thấy Serial down/down hoặc up/down | `no shutdown`, thêm `clock rate 64000` nếu là DCE |
| Nhầm subnet `00c9`, `00ca`, `00cb`, `00cc` | Không tăng subnet theo hệ hex | Assessment báo sai IPv6 address | So lại bảng subnet IPv6 và sửa đúng interface |
| Nhập sai IPv6 nhưng không mất địa chỉ cũ | IPv6 cho phép nhiều địa chỉ trên một interface | `show ipv6 interface brief` thấy nhiều địa chỉ global không mong muốn | Dùng `no ipv6 address <địa-chỉ-sai>/64` |
| PC Auto Config nhưng chưa ping được ngay | PC chưa nhận RA hoặc bảng neighbor chưa cập nhật | Ping lần đầu fail rồi lần sau thành công | Chờ vài giây hoặc bấm Fast Forward trong Packet Tracer |

### Static Route Nhanh Nếu Ping Liên LAN Không Thành Công

```text
R1# configure terminal
R1(config)# ipv6 route 2001:db8:acad:00ca::/64 2001:db8:acad:00cc::2
R1(config)# ipv6 route 2001:db8:acad:00cb::/64 2001:db8:acad:00cc::2
R1(config)# end
R1# copy running-config startup-config

R2# configure terminal
R2(config)# ipv6 route 2001:db8:acad:00c8::/64 2001:db8:acad:00cc::1
R2(config)# ipv6 route 2001:db8:acad:00c9::/64 2001:db8:acad:00cc::1
R2(config)# end
R2# copy running-config startup-config
```

## 7. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| Subnet IPv6 | Có đủ 5 subnet liên tiếp từ `00c8` đến `00cc` |
| R1 G0/0 | `2001:db8:acad:00c8::1/64`, `fe80::1`, `up/up` |
| R1 G0/1 | `2001:db8:acad:00c9::1/64`, `fe80::1`, `up/up` |
| R1 S0/0/0 | `2001:db8:acad:00cc::1/64`, `fe80::1`, `up/up` |
| R2 G0/0 | `2001:db8:acad:00ca::1/64`, `fe80::2`, `up/up` |
| R2 G0/1 | `2001:db8:acad:00cb::1/64`, `fe80::2`, `up/up` |
| R2 S0/0/0 | `2001:db8:acad:00cc::2/64`, `fe80::2`, `up/up` |
| PC1-PC4 | Đều dùng Auto Config và nhận đúng prefix IPv6 |
| IPv6 routing | R1/R2 có route tới các mạng remote |
| Ping cuối cùng | Các PC ping IPv6 được nhau |

![PC to PC ping IPv6 lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/final.png)


---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 5</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 7 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 02.07 - 10.4.3 Packet Tracer - Basic Device Configuration"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `10.4.3 Packet Tracer - Basic Device Configuration.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-07/` |
| Trạng thái | Hoàn thành cấu hình cơ bản router, switch, IPv4/IPv6 cho host và kiểm tra end-to-end |

> **Ghi chú:** Bài này là dạng cấu hình tổng hợp. Topology có 1 router nối 2 LAN, 2 switch và 4 PC. Switch `Room-145` có thể không truy cập được theo đề, vì vậy phần cấu hình chính tập trung vào router `Floor14`, switch truy cập được và các PC host.

## 1. Mục Tiêu Bài Lab

- Hoàn thiện bảng địa chỉ IPv4/IPv6 dựa trên subnet trong topology.
- Đặt hostname cho router và switch được yêu cầu.
- Cấu hình password console, VTY và privileged EXEC.
- Bật mã hóa plaintext password.
- Cấu hình MOTD banner cảnh báo truy cập trái phép.
- Cấu hình IPv4/IPv6 trên các interface router.
- Cấu hình IP quản trị VLAN 1 cho switch.
- Cấu hình IPv4/IPv6 cho các PC host.
- Kiểm tra kết nối IPv4 và IPv6 giữa toàn bộ thiết bị.
- Lưu cấu hình vào NVRAM.

![Topology lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/topology.png)

## 2. Bảng Địa Chỉ IP

### IPv4 Addressing Table

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| Floor14 | G0/0 | `172.14.5.1` | `255.255.255.0` | N/A |
| Floor14 | G0/1 | `172.14.10.1` | `255.255.255.0` | N/A |
| Room-145 | VLAN 1 | `172.14.5.2` | `255.255.255.0` | `172.14.5.1` |
| Room-146 | VLAN 1 | `172.14.10.2` | `255.255.255.0` | `172.14.10.1` |
| Manager-A | NIC | `172.14.5.10` | `255.255.255.0` | `172.14.5.1` |
| Reception-A | NIC | `172.14.5.11` | `255.255.255.0` | `172.14.5.1` |
| Manager-B | NIC | `172.14.10.10` | `255.255.255.0` | `172.14.10.1` |
| Reception-B | NIC | `172.14.10.11` | `255.255.255.0` | `172.14.10.1` |

> **Lưu ý:** Nếu Packet Tracer random ra số host khác trong Addressing Table, giữ đúng subnet `172.14.5.0/24` và `172.14.10.0/24`, sau đó thay lại số cuối IP theo đề của file `.pka`.

### IPv6 Addressing Table

| Device | Interface | IPv6 Address | Prefix | Default Gateway |
| --- | --- | --- | --- | --- |
| Floor14 | G0/0 | `2001:DB8:CAFE:1::1` | `/64` | N/A |
| Floor14 | G0/0 | `FE80::1` | Link-local | N/A |
| Floor14 | G0/1 | `2001:DB8:CAFE:2::1` | `/64` | N/A |
| Floor14 | G0/1 | `FE80::1` | Link-local | N/A |
| Manager-A | NIC | `2001:DB8:CAFE:1::10` | `/64` | `FE80::1` |
| Reception-A | NIC | `2001:DB8:CAFE:1::11` | `/64` | `FE80::1` |
| Manager-B | NIC | `2001:DB8:CAFE:2::10` | `/64` | `FE80::1` |
| Reception-B | NIC | `2001:DB8:CAFE:2::11` | `/64` | `FE80::1` |

> **Lưu ý:** `FE80::1` được dùng lại trên hai interface router khác nhau vì link-local chỉ có hiệu lực trong phạm vi từng link.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN A | Floor14 G0/0, Room-145, Manager-A, Reception-A | Dùng IPv4 `172.14.5.0/24` và IPv6 `2001:DB8:CAFE:1::/64` |
| LAN B | Floor14 G0/1, Room-146, Manager-B, Reception-B | Dùng IPv4 `172.14.10.0/24` và IPv6 `2001:DB8:CAFE:2::/64` |
| Router | Floor14 | Đóng vai trò default gateway cho cả hai LAN |
| Switch | Room-145, Room-146 | Switch lớp 2, VLAN 1 dùng cho quản trị IPv4 |

> **Điểm dễ sai:** PC trong LAN A phải trỏ gateway về `172.14.5.1`, PC trong LAN B phải trỏ gateway về `172.14.10.1`. Nếu nhập nhầm gateway, ping cùng LAN vẫn có thể được nhưng ping khác LAN sẽ fail.

## 4. Part 1 - Hoàn Thiện Network Documentation

| Nội dung cần xác định | Kết quả |
| --- | --- |
| Router cần cấu hình | `Floor14` |
| Switch quản trị LAN A | `Room-145` |
| Switch quản trị LAN B | `Room-146` |
| IPv4 LAN A | `172.14.5.0/24` |
| IPv4 LAN B | `172.14.10.0/24` |
| IPv6 LAN A | `2001:DB8:CAFE:1::/64` |
| IPv6 LAN B | `2001:DB8:CAFE:2::/64` |
| Console/VTY password | `cisco` |
| Enable secret | `class` |

![Addressing table lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/addressing-table.png)

## 5. Part 2 - Cấu Hình Router Floor14

### Step 1: Cấu hình bảo mật cơ bản và IPv6 routing

```text
Router> enable
Router# configure terminal
Router(config)# hostname Floor14
Floor14(config)# no ip domain-lookup
Floor14(config)# enable secret class
Floor14(config)# service password-encryption
Floor14(config)# banner motd #Unauthorized access is strictly prohibited.#
Floor14(config)# line console 0
Floor14(config-line)# password cisco
Floor14(config-line)# login
Floor14(config-line)# exit
Floor14(config)# line vty 0 4
Floor14(config-line)# password cisco
Floor14(config-line)# login
Floor14(config-line)# exit
Floor14(config)# ipv6 unicast-routing
```

> **Lưu ý:** `ipv6 unicast-routing` phải bật trên router. Nếu thiếu lệnh này, router có thể có IPv6 trên interface nhưng không định tuyến IPv6 giữa hai LAN.

### Step 2: Cấu hình interface về LAN A và LAN B

```text
Floor14(config)# interface gigabitethernet 0/0
Floor14(config-if)# description LAN A connection to Room-145
Floor14(config-if)# ip address 172.14.5.1 255.255.255.0
Floor14(config-if)# ipv6 address FE80::1 link-local
Floor14(config-if)# ipv6 address 2001:DB8:CAFE:1::1/64
Floor14(config-if)# no shutdown
Floor14(config-if)# exit
Floor14(config)# interface gigabitethernet 0/1
Floor14(config-if)# description LAN B connection to Room-146
Floor14(config-if)# ip address 172.14.10.1 255.255.255.0
Floor14(config-if)# ipv6 address FE80::1 link-local
Floor14(config-if)# ipv6 address 2001:DB8:CAFE:2::1/64
Floor14(config-if)# no shutdown
Floor14(config-if)# exit
Floor14(config)# end
Floor14# copy running-config startup-config
Destination filename [startup-config]?
```

> **Lưu ý:** Nếu sau khi `no shutdown` vẫn thấy interface down/down, kiểm tra lại cáp giữa router và switch hoặc kiểm tra switch port đã up chưa.

### Kiểm tra trên Floor14

```text
Floor14# show ip interface brief
Floor14# show ipv6 interface brief
Floor14# show running-config
Floor14# show ip route
Floor14# show ipv6 route
```

```text
! Kiểm tra gateway IPv4 của LAN A
Floor14# ping 172.14.5.10

! Kiểm tra gateway IPv4 của LAN B
Floor14# ping 172.14.10.10

! Kiểm tra IPv6 host LAN A
Floor14# ping 2001:DB8:CAFE:1::10

! Kiểm tra IPv6 host LAN B
Floor14# ping 2001:DB8:CAFE:2::10
```

![Router verification lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/router-verification.png)

## 6. Part 3 - Cấu Hình Switch Room-146

### Step 1: Cấu hình bảo mật cơ bản

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Room-146
Room-146(config)# no ip domain-lookup
Room-146(config)# enable secret class
Room-146(config)# service password-encryption
Room-146(config)# banner motd #Unauthorized access is strictly prohibited.#
Room-146(config)# line console 0
Room-146(config-line)# password cisco
Room-146(config-line)# login
Room-146(config-line)# exit
Room-146(config)# line vty 0 15
Room-146(config-line)# password cisco
Room-146(config-line)# login
Room-146(config-line)# exit
```

### Step 2: Cấu hình VLAN 1 quản trị

```text
Room-146(config)# interface vlan 1
Room-146(config-if)# description Management interface for Room-146
Room-146(config-if)# ip address 172.14.10.2 255.255.255.0
Room-146(config-if)# no shutdown
Room-146(config-if)# exit
Room-146(config)# ip default-gateway 172.14.10.1
Room-146(config)# end
Room-146# copy running-config startup-config
Destination filename [startup-config]?
```

> **Lưu ý:** Switch layer 2 cần `ip default-gateway` để ping hoặc quản trị từ mạng khác subnet. Lệnh này không thay thế cho default gateway của PC.

### Nếu Room-145 được phép truy cập

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Room-145
Room-145(config)# no ip domain-lookup
Room-145(config)# enable secret class
Room-145(config)# service password-encryption
Room-145(config)# banner motd #Unauthorized access is strictly prohibited.#
Room-145(config)# line console 0
Room-145(config-line)# password cisco
Room-145(config-line)# login
Room-145(config-line)# exit
Room-145(config)# line vty 0 15
Room-145(config-line)# password cisco
Room-145(config-line)# login
Room-145(config-line)# exit
Room-145(config)# interface vlan 1
Room-145(config-if)# description Management interface for Room-145
Room-145(config-if)# ip address 172.14.5.2 255.255.255.0
Room-145(config-if)# no shutdown
Room-145(config-if)# exit
Room-145(config)# ip default-gateway 172.14.5.1
Room-145(config)# end
Room-145# copy running-config startup-config
Destination filename [startup-config]?
```

> **Lưu ý:** Nếu đề ghi không thể truy cập một switch, không cần ép cấu hình switch đó. Tập trung kiểm tra các thiết bị được phép cấu hình và kết nối end-to-end giữa PC.

### Kiểm tra trên switch

```text
Room-146# show running-config
Room-146# show ip interface brief
```

```text
! Kiểm tra gateway của switch Room-146
Room-146# ping 172.14.10.1
```

![Switch verification lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/switch-verification.png)

## 7. Part 4 - Cấu Hình Các PC Host

### IPv4 Configuration

| PC | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| Manager-A | `172.14.5.10` | `255.255.255.0` | `172.14.5.1` |
| Reception-A | `172.14.5.11` | `255.255.255.0` | `172.14.5.1` |
| Manager-B | `172.14.10.10` | `255.255.255.0` | `172.14.10.1` |
| Reception-B | `172.14.10.11` | `255.255.255.0` | `172.14.10.1` |

![PC IPv4 configuration lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/pc-ipv4-config.png)

### IPv6 Configuration

| PC | IPv6 Address | Prefix Length | IPv6 Default Gateway |
| --- | --- | --- | --- |
| Manager-A | `2001:DB8:CAFE:1::10` | `64` | `FE80::1` |
| Reception-A | `2001:DB8:CAFE:1::11` | `64` | `FE80::1` |
| Manager-B | `2001:DB8:CAFE:2::10` | `64` | `FE80::1` |
| Reception-B | `2001:DB8:CAFE:2::11` | `64` | `FE80::1` |

> **Lưu ý:** IPv6 default gateway trên PC nên dùng link-local của router (`FE80::1`), không dùng địa chỉ IPv6 của PC khác.

![PC IPv6 configuration lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/pc-ipv6-config.png)

## 8. Part 5 - Verify Connectivity Và Troubleshooting

### Kiểm tra từ PC Manager-A

```text
! Ping IPv4 sang PC cùng LAN
PC> ping 172.14.5.11

! Ping IPv4 sang PC khác LAN
PC> ping 172.14.10.10
PC> ping 172.14.10.11

! Ping IPv6 sang PC cùng LAN
PC> ping 2001:DB8:CAFE:1::11

! Ping IPv6 sang PC khác LAN
PC> ping 2001:DB8:CAFE:2::10
PC> ping 2001:DB8:CAFE:2::11
```

### Kiểm tra từ PC Reception-B

```text
! Ping IPv4 ngược về LAN A
PC> ping 172.14.5.10
PC> ping 172.14.5.11

! Ping IPv6 ngược về LAN A
PC> ping 2001:DB8:CAFE:1::10
PC> ping 2001:DB8:CAFE:1::11
```

![Ping result lab 07](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-07/ping-result.png)

### Kiểm tra nhanh bằng router

```text
Floor14# show ip interface brief
Floor14# show ipv6 interface brief
Floor14# show ip route
Floor14# show ipv6 route
```

| Dấu hiệu đúng | Ý nghĩa |
| --- | --- |
| G0/0 và G0/1 đều `up/up` | Router đã kết nối vật lý và logical với hai LAN |
| Có route `C 172.14.5.0/24` | Router biết mạng LAN A |
| Có route `C 172.14.10.0/24` | Router biết mạng LAN B |
| Có route IPv6 `2001:DB8:CAFE:1::/64` | Router biết IPv6 LAN A |
| Có route IPv6 `2001:DB8:CAFE:2::/64` | Router biết IPv6 LAN B |

## 9. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC cùng LAN ping được nhưng khác LAN không ping được | Sai default gateway trên PC | Kiểm tra lại gateway IPv4/IPv6 theo đúng LAN |
| IPv4 ping được nhưng IPv6 không ping được | Thiếu `ipv6 unicast-routing` trên router | Vào global config và bật `ipv6 unicast-routing` |
| Interface router vẫn down/down | Chưa `no shutdown` hoặc cáp chưa đúng | Kiểm tra `show ip interface brief`, cấu hình `no shutdown` |
| Switch ping ra ngoài không được | Thiếu `ip default-gateway` | Cấu hình gateway về IP router cùng LAN |
| Không vào được privileged EXEC | Nhập nhầm `enable secret` | Dùng password `class` |
| Vào console không hỏi password | Thiếu `login` dưới line console | Cấu hình `line console 0`, `password cisco`, `login` |
| Password vẫn hiện plaintext | Thiếu `service password-encryption` | Bật `service password-encryption` rồi kiểm tra lại `show run` |
| IPv6 default gateway trên PC không nhận | Nhập sai link-local hoặc sai prefix | Dùng `FE80::1`, prefix length `64` |

## 10. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| Hostname router | Hiển thị `Floor14` | Đạt |
| Hostname switch | Hiển thị đúng switch được yêu cầu | Đạt |
| Console/VTY password | Dùng `cisco` | Đạt |
| Enable secret | Dùng `class` | Đạt |
| Plaintext password | Được mã hóa sau `service password-encryption` | Đạt |
| MOTD banner | Hiển thị khi đăng nhập CLI | Đạt |
| IPv4 router interfaces | G0/0 và G0/1 có IP đúng, trạng thái `up/up` | Đạt |
| IPv6 router interfaces | Có global IPv6 và link-local đúng | Đạt |
| PC IPv4/IPv6 | Đúng IP, subnet/prefix và gateway | Đạt |
| Ping cùng LAN | Thành công | Đạt |
| Ping khác LAN | Thành công với IPv4 và IPv6 | Đạt |
| Save config | Đã copy running-config sang startup-config | Đạt |

Checklist ảnh minh chứng nên lưu trong thư mục `labs/lab-07/`:

- [ ] `topology.png` - ảnh topology tổng quan.
- [ ] `addressing-table.png` - bảng địa chỉ đã điền.
- [ ] `router-verification.png` - kết quả `show ip interface brief` và `show ipv6 interface brief` trên Floor14.
- [ ] `switch-verification.png` - kết quả kiểm tra switch.
- [ ] `pc-ipv4-config.png` - cấu hình IPv4 trên PC.
- [ ] `pc-ipv6-config.png` - cấu hình IPv6 trên PC.
- [ ] `ping-result.png` - kết quả ping IPv4/IPv6 end-to-end.
- [ ] `check-results.png` - điểm Check Results sau khi hoàn thành.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 6</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 8 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

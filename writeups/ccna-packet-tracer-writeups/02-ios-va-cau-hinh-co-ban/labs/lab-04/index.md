---
layout: page-toc
title: "CCNA 02.04 - 2.9.1 Packet Tracer - Basic Switch and End Device Configuration"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `2.9.1 Packet Tracer - Basic Switch and End Device Configuration.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Hoàn tất cấu hình hostname, mật khẩu, MOTD banner, IP VLAN 1 cho switch, IP cho PC, lưu cấu hình và kiểm tra kết nối |

> Bài này cấu hình một LAN nhỏ gồm 2 switch và 2 PC. Trọng tâm là cấu hình ban đầu cho switch Cisco IOS, đặt IP quản trị trên `VLAN 1`, cấu hình IP cho end device và kiểm tra ping giữa các thiết bị cùng subnet.

## 1. Mục Tiêu Bài Lab

- Truy cập từng switch bằng console connection.
- Đặt hostname cho 2 switch: `Class-A` và `Class-B`.
- Cấu hình password `xAw6k` cho console line và vty line.
- Cấu hình enable secret password là `6EBUp`.
- Mã hóa toàn bộ clear text password.
- Cấu hình MOTD banner cảnh báo truy cập trái phép.
- Cấu hình địa chỉ IP cho `VLAN 1` trên 2 switch.
- Cấu hình địa chỉ IP cho `Student-1` và `Student-2`.
- Lưu cấu hình vào NVRAM.
- Kiểm tra kết nối giữa các PC và switch trong cùng mạng.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/exam.png)
Ảnh topology
![Topology lab 04](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/topology.png)

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| Class-A | VLAN 1 | `128.107.20.10` | `255.255.255.0` | Không cấu hình trong bài |
| Class-B | VLAN 1 | `128.107.20.15` | `255.255.255.0` | Không cấu hình trong bài |
| Student-1 | NIC | `128.107.20.25` | `255.255.255.0` | Để trống |
| Student-2 | NIC | `128.107.20.30` | `255.255.255.0` | Để trống |

> **Lưu ý:** Tất cả thiết bị đều nằm trong mạng `128.107.20.0/24`. Vì bài không có router và chỉ kiểm tra kết nối nội bộ cùng subnet, PC không cần default gateway.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Bên trái | Student-1, Class-A | Student-1 kết nối vào switch Class-A |
| Trung tâm | Class-A ↔ Class-B | Hai switch kết nối trực tiếp với nhau để mở rộng LAN |
| Bên phải | Class-B, Student-2 | Student-2 kết nối vào switch Class-B |
| Quản trị switch | VLAN 1 trên Class-A và Class-B | Dùng để gán IP quản trị cho switch và kiểm tra ping |

> **Lưu ý:** Đây là bài cấu hình switch cơ bản, chưa cấu hình VLAN riêng. Các cổng mặc định vẫn thuộc `VLAN 1`, nên các thiết bị cùng subnet có thể ping nhau nếu IP đúng và link đang up.

## 4. Part 1 - Verify the Default Switch Configuration

### Step 1 - Vào privileged EXEC mode

```text
Switch> enable
Switch#
```

### Step 2 - Kiểm tra cấu hình mặc định

```text
Switch# show running-config
```

| Nội dung cần kiểm tra | Kết quả mong muốn |
| --- | --- |
| Hostname ban đầu | Thường là `Switch` |
| Interface mặc định | Các cổng switch ở trạng thái mặc định, chưa gán IP trên từng port vật lý |
| `interface vlan 1` | Chưa có IP address theo yêu cầu bài |
| Line console/vty | Chưa có password theo yêu cầu bài |
| Startup-config | Có thể chưa tồn tại nếu chưa từng lưu cấu hình |

Cắm dây console như lab cũ kết nối tới SW

![Default running config](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/default-running-config.png)

> **Lưu ý:** Switch layer 2 không gán IP trực tiếp trên cổng access như PC. IP quản trị thường đặt trên SVI, trong bài này là `interface vlan 1`.

## 5. Part 2 - Configure Class-A Switch

### Step 1 - Cấu hình hoàn chỉnh Class-A

```text
Switch> enable
Switch# configure terminal

! Đặt hostname cho switch
Switch(config)# hostname Class-A

! Cấu hình enable secret password
Class-A(config)# enable secret 6EBUp

! Cấu hình console password
Class-A(config)# line console 0
Class-A(config-line)# password xAw6k
Class-A(config-line)# login
Class-A(config-line)# exit

! Cấu hình vty password cho truy cập từ xa
Class-A(config)# line vty 0 15
Class-A(config-line)# password xAw6k
Class-A(config-line)# login
Class-A(config-line)# exit

! Cấu hình MOTD banner
Class-A(config)# banner motd "Authorized access only!"

! Mã hóa các password dạng clear text
Class-A(config)# service password-encryption

! Cấu hình IP quản trị trên VLAN 1
Class-A(config)# interface vlan 1
Class-A(config-if)# ip address 128.107.20.10 255.255.255.0
Class-A(config-if)# no shutdown
Class-A(config-if)# exit

Class-A(config)# end

! Lưu cấu hình vào NVRAM
Class-A# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

> **Lưu ý:** `login` bắt buộc phải có sau `password` trên console/vty line. Nếu thiếu `login`, switch không yêu cầu nhập mật khẩu khi truy cập line đó.

![Class-A configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/class-a-configuration.png)

### Step 2 - Kiểm tra nhanh Class-A

```text
Class-A# show running-config
Class-A# show ip interface brief
Class-A# show startup-config
```

| Hạng mục | Kết quả cần thấy |
| --- | --- |
| Hostname | `hostname Class-A` |
| Enable secret | `enable secret 5 ...` hoặc dạng hash tương tự |
| Console line | `line con 0`, có `password 7 ...` và `login` |
| VTY line | `line vty 0 4`, `line vty 5 15`, có password và `login` |
| Password encryption | Có dòng `service password-encryption` |
| VLAN 1 IP | `128.107.20.10` |
| Startup-config | Có cấu hình đã lưu |


## 6. Part 3 - Configure Class-B Switch

### Step 1 - Cấu hình hoàn chỉnh Class-B

```text
Switch> enable
Switch# configure terminal

! Đặt hostname cho switch
Switch(config)# hostname Class-B

! Cấu hình enable secret password
Class-B(config)# enable secret 6EBUp

! Cấu hình console password
Class-B(config)# line console 0
Class-B(config-line)# password xAw6k
Class-B(config-line)# login
Class-B(config-line)# exit

! Cấu hình vty password cho truy cập từ xa
Class-B(config)# line vty 0 15
Class-B(config-line)# password xAw6k
Class-B(config-line)# login
Class-B(config-line)# exit

! Cấu hình MOTD banner
Class-B(config)# banner motd "Authorized access only!"

! Mã hóa các password dạng clear text
Class-B(config)# service password-encryption

! Cấu hình IP quản trị trên VLAN 1
Class-B(config)# interface vlan 1
Class-B(config-if)# ip address 128.107.20.15 255.255.255.0
Class-B(config-if)# no shutdown
Class-B(config-if)# exit

Class-B(config)# end

! Lưu cấu hình vào NVRAM
Class-B# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

### Step 2 - Kiểm tra nhanh Class-B

```text
Class-B# show running-config
Class-B# show ip interface brief
Class-B# show startup-config
```

| Hạng mục | Kết quả cần thấy |
| --- | --- |
| Hostname | `hostname Class-B` |
| Enable secret | `enable secret 5 ...` hoặc dạng hash tương tự |
| Console line | `line con 0`, có `password 7 ...` và `login` |
| VTY line | `line vty 0 4`, `line vty 5 15`, có password và `login` |
| Password encryption | Có dòng `service password-encryption` |
| VLAN 1 IP | `128.107.20.15` |
| Startup-config | Có cấu hình đã lưu |


## 7. Part 4 - Configure End Devices

### Step 1 - Cấu hình IP cho Student-1

| Mục | Giá trị |
| --- | --- |
| IP Address | `128.107.20.25` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống |

![Student-1 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/student-1-ip-configuration.png)

### Step 2 - Cấu hình IP cho Student-2

| Mục | Giá trị |
| --- | --- |
| IP Address | `128.107.20.30` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống |

![Student-2 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/student-2-ip-configuration.png)

> **Lưu ý:** Trên Packet Tracer, vào `PC > Desktop > IP Configuration` để nhập IP cho end device.

## 8. Part 5 - Verify Connectivity

### Step 1 - Kiểm tra từ Student-1

```text
! Ping sang PC còn lại
ping 128.107.20.30

! Ping IP quản trị switch Class-A
ping 128.107.20.10

! Ping IP quản trị switch Class-B
ping 128.107.20.15
```

![Student-1 ping test](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/student-1-ping-test.png)

### Step 2 - Kiểm tra từ Student-2

```text
! Ping sang PC còn lại
ping 128.107.20.25

! Ping IP quản trị switch Class-A
ping 128.107.20.10

! Ping IP quản trị switch Class-B
ping 128.107.20.15
```

### Step 3 - Kiểm tra từ switch

```text
Class-A# ping 128.107.20.15
Class-A# ping 128.107.20.25
Class-A# ping 128.107.20.30

Class-B# ping 128.107.20.10
Class-B# ping 128.107.20.25
Class-B# ping 128.107.20.30
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Student-1 ping Student-2 | Thành công |
| Student-1 ping Class-A | Thành công |
| Student-1 ping Class-B | Thành công |
| Student-2 ping Student-1 | Thành công |
| Class-A ping Class-B | Thành công |
| Switch ping PC | Thành công |


## 9. Cấu Hình Tổng Hợp

### Class-A

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Class-A
Class-A(config)# enable secret 6EBUp
Class-A(config)# line console 0
Class-A(config-line)# password xAw6k
Class-A(config-line)# login
Class-A(config-line)# exit
Class-A(config)# line vty 0 15
Class-A(config-line)# password xAw6k
Class-A(config-line)# login
Class-A(config-line)# exit
Class-A(config)# banner motd "Authorized access only!"
Class-A(config)# service password-encryption
Class-A(config)# interface vlan 1
Class-A(config-if)# ip address 128.107.20.10 255.255.255.0
Class-A(config-if)# no shutdown
Class-A(config-if)# exit
Class-A(config)# end
Class-A# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

### Class-B

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Class-B
Class-B(config)# enable secret 6EBUp
Class-B(config)# line console 0
Class-B(config-line)# password xAw6k
Class-B(config-line)# login
Class-B(config-line)# exit
Class-B(config)# line vty 0 15
Class-B(config-line)# password xAw6k
Class-B(config-line)# login
Class-B(config-line)# exit
Class-B(config)# banner motd "Authorized access only!"
Class-B(config)# service password-encryption
Class-B(config)# interface vlan 1
Class-B(config-if)# ip address 128.107.20.15 255.255.255.0
Class-B(config-if)# no shutdown
Class-B(config-if)# exit
Class-B(config)# end
Class-B# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

## 10. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không ping được giữa 2 PC | Sai IP/subnet mask hoặc link chưa up | Kiểm tra lại IP trên PC, dây kết nối và trạng thái port |
| Ping được PC nhưng không ping được IP switch | Chưa cấu hình `interface vlan 1`, sai IP hoặc quên `no shutdown` | Vào `interface vlan 1`, đặt đúng IP và chạy `no shutdown` |
| Switch không hỏi password khi vào console | Thiếu lệnh `login` trong `line console 0` | Cấu hình lại `line console 0`, nhập `password xAw6k` và `login` |
| Không vào được privileged EXEC mode | Nhập sai enable secret hoặc nhầm chữ hoa/thường | Nhập đúng `6EBUp`, password có phân biệt hoa thường |
| Password vẫn hiện rõ trong `show running-config` | Chưa bật `service password-encryption` | Chạy `service password-encryption` trong global configuration mode |
| Mất cấu hình sau khi tắt/mở lại Packet Tracer | Chưa lưu cấu hình vào NVRAM | Chạy `copy running-config startup-config` trên từng switch |
| Packet Tracer Check Results chưa đạt 100% | Thiếu một yêu cầu nhỏ như banner, vty password hoặc save config | Đối chiếu lại từng dòng trong bảng kết quả cuối |

## 11. Kết Quả Cuối

| Hạng mục | Thiết bị | Kết quả mong muốn | Trạng thái |
| --- | --- | --- | --- |
| Hostname | Class-A | Prompt hiển thị `Class-A#` | Hoàn tất |
| Hostname | Class-B | Prompt hiển thị `Class-B#` | Hoàn tất |
| Console password | Class-A, Class-B | Console line dùng password `xAw6k` | Hoàn tất |
| VTY password | Class-A, Class-B | VTY line dùng password `xAw6k` | Hoàn tất |
| Enable secret | Class-A, Class-B | Privileged EXEC mode dùng `6EBUp` | Hoàn tất |
| Password encryption | Class-A, Class-B | Password thường hiển thị dạng `password 7 ...` | Hoàn tất |
| MOTD banner | Class-A, Class-B | Có banner cảnh báo khi truy cập CLI | Hoàn tất |
| VLAN 1 IP | Class-A | `128.107.20.10/24` | Hoàn tất |
| VLAN 1 IP | Class-B | `128.107.20.15/24` | Hoàn tất |
| PC IP | Student-1 | `128.107.20.25/24` | Hoàn tất |
| PC IP | Student-2 | `128.107.20.30/24` | Hoàn tất |
| Save config | Class-A, Class-B | `copy running-config startup-config` thành công | Hoàn tất |
| Connectivity | Toàn bộ thiết bị | Ping trong mạng `128.107.20.0/24` thành công | Hoàn tất |

![final](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-04/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

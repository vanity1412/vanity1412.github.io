---
layout: page-toc
title: "CCNA 05.04 - 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Thiết kế VLSM từ `192.168.203.0/24`, cấu hình địa chỉ cho router, switch, PC và kiểm tra kết nối |

> Bài này yêu cầu tự thiết kế VLSM theo số host trên topology: `32`, `21`, `19`, `14` và một đường WAN point-to-point giữa `East` - `West`. File Packet Tracer này chấm cố định subnet `192.168.203.64/27` cho `W1 LAN` và `192.168.203.96/27` cho `E2 LAN`. Hai LAN này đều dùng `/27`, nên đổi thứ tự vẫn đúng về mặt VLSM nhưng phải theo đúng đáp án PKA để được tick xanh.

## 1. Mục Tiêu Bài Lab

- Xác định số LAN và WAN cần chia subnet.
- Thiết kế VLSM từ mạng gốc `192.168.203.0/24`.
- Chọn subnet mask phù hợp theo số host yêu cầu.
- Gán IP cho router `East`, router `West`, các switch và các PC.
- Cấu hình địa chỉ IPv4 trên router, switch management VLAN và end device.
- Kiểm tra kết nối giữa toàn bộ thiết bị trong topology.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/topology.png)

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/topology1.png)

## 2. Topology Và Yêu Cầu Subnet

| Khu vực | Thiết bị liên quan | Số host cần | Interface router | Ghi chú |
| --- | --- | ---: | --- | --- |
| W2 LAN | West, WS-2, W2-87 | 32 | West `G0/1` | LAN lớn nhất, phải dùng `/26` |
| W1 LAN | West, WS-1, W1-201 | 19 | West `G0/0` | Dùng `/27`, file PKA gán subnet thứ hai cho LAN này |
| E2 LAN | East, ES-2, E2-47 | 21 | East `G0/1` | Dùng `/27`, file PKA gán subnet thứ ba cho LAN này |
| E1 LAN | East, ES-1, E1-22 | 14 | East `G0/0` | Dùng `/28` |
| WAN East-West | East `S0/0/0`, West `S0/0/0` | 2 | Serial `S0/0/0` | Link point-to-point, dùng `/30` |

> **Lưu ý:** Với `32 hosts`, không thể dùng `/27` vì `/27` chỉ có 30 địa chỉ host usable. Vì vậy W2 LAN bắt buộc phải dùng `/26`.

## 3. Thiết Kế VLSM

### 3.1. Số Subnet Cần Dùng

| Câu hỏi | Đáp án |
| --- | --- |
| Có bao nhiêu LAN trong topology? | 4 LAN |
| Có bao nhiêu WAN point-to-point? | 1 WAN |
| Tổng số subnet cần dùng | 5 subnet |

### 3.2. Chọn Subnet Mask Theo Số Host

| Khu vực | Host cần | Prefix phù hợp | Subnet mask | Usable host | Lý do |
| --- | ---: | --- | --- | ---: | --- |
| W2 LAN | 32 | `/26` | `255.255.255.192` | 62 | `/27` chỉ có 30 host nên không đủ |
| W1 LAN | 19 | `/27` | `255.255.255.224` | 30 | Đủ cho 19 host |
| E2 LAN | 21 | `/27` | `255.255.255.224` | 30 | Đủ cho 21 host |
| E1 LAN | 14 | `/28` | `255.255.255.240` | 14 | Vừa đủ 14 host |
| WAN East-West | 2 | `/30` | `255.255.255.252` | 2 | Vừa đủ 2 IP cho point-to-point |

> **Công thức nhớ nhanh:** số host dùng được = `2^h - 2`, trong đó `h` là số bit host. Ví dụ `/27` còn `5` bit host, nên có `2^5 - 2 = 30` host usable.

### 3.3. Cách Nhảy Block Địa Chỉ

| Prefix | Subnet mask | Block size | Dải địa chỉ trong bài |
| --- | --- | ---: | --- |
| `/26` | `255.255.255.192` | 64 | `.0 - .63` |
| `/27` | `255.255.255.224` | 32 | `.64 - .95`, `.96 - .127` |
| `/28` | `255.255.255.240` | 16 | `.128 - .143` |
| `/30` | `255.255.255.252` | 4 | `.144 - .147` |

> **Cách tính block size:** lấy `256 - số cuối của subnet mask`. Ví dụ `/27` có mask `255.255.255.224`, block size = `256 - 224 = 32`.

### 3.4. Subnet Table Theo Đáp Án PKA

| Thứ tự | Subnet Description | Host cần | Network Address/CIDR | First Usable Host | Second Usable Host | Last Usable Host | Broadcast |
| ---: | --- | ---: | --- | --- | --- | --- | --- |
| 1 | W2 LAN | 32 | `192.168.203.0/26` | `192.168.203.1` | `192.168.203.2` | `192.168.203.62` | `192.168.203.63` |
| 2 | W1 LAN | 19 | `192.168.203.64/27` | `192.168.203.65` | `192.168.203.66` | `192.168.203.94` | `192.168.203.95` |
| 3 | E2 LAN | 21 | `192.168.203.96/27` | `192.168.203.97` | `192.168.203.98` | `192.168.203.126` | `192.168.203.127` |
| 4 | E1 LAN | 14 | `192.168.203.128/28` | `192.168.203.129` | `192.168.203.130` | `192.168.203.142` | `192.168.203.143` |
| 5 | WAN East-West | 2 | `192.168.203.144/30` | `192.168.203.145` | N/A | `192.168.203.146` | `192.168.203.147` |

> **Quy tắc gán IP của bài:** router LAN dùng first usable, switch VLAN 1 dùng second usable, PC dùng last usable. Riêng WAN: `East` dùng first usable `.145`, `West` dùng last usable `.146`.

## 4. Bảng Địa Chỉ IP Hoàn Chỉnh

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| West | G0/0 | `192.168.203.65` | `255.255.255.224` | N/A |
| West | G0/1 | `192.168.203.1` | `255.255.255.192` | N/A |
| West | S0/0/0 | `192.168.203.146` | `255.255.255.252` | N/A |
| East | G0/0 | `192.168.203.129` | `255.255.255.240` | N/A |
| East | G0/1 | `192.168.203.97` | `255.255.255.224` | N/A |
| East | S0/0/0 | `192.168.203.145` | `255.255.255.252` | N/A |
| WS-1 | VLAN 1 | `192.168.203.66` | `255.255.255.224` | `192.168.203.65` |
| WS-2 | VLAN 1 | `192.168.203.2` | `255.255.255.192` | `192.168.203.1` |
| ES-1 | VLAN 1 | `192.168.203.130` | `255.255.255.240` | `192.168.203.129` |
| ES-2 | VLAN 1 | `192.168.203.98` | `255.255.255.224` | `192.168.203.97` |
| W1-201 | NIC | `192.168.203.94` | `255.255.255.224` | `192.168.203.65` |
| W2-87 | NIC | `192.168.203.62` | `255.255.255.192` | `192.168.203.1` |
| E1-22 | NIC | `192.168.203.142` | `255.255.255.240` | `192.168.203.129` |
| E2-47 | NIC | `192.168.203.126` | `255.255.255.224` | `192.168.203.97` |

> **Lưu ý:** Nếu file PKA hiển thị cổng `G0/0` và `G0/1` khác với hình, giữ nguyên subnet theo đúng LAN rồi đổi IP sang interface đang nối thực tế.

![VLSM design](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/topology11.png)

## 5. Cấu Hình Từng Part

## Part 1: Thiết Kế Và Gán Địa Chỉ

### Step 1: Điền bảng VLSM

| Subnet | Gán cho | Network | Router IP | Switch IP | PC IP |
| --- | --- | --- | --- | --- | --- |
| Subnet 1 | W2 LAN | `192.168.203.0/26` | `192.168.203.1` | `192.168.203.2` | `192.168.203.62` |
| Subnet 2 | W1 LAN | `192.168.203.64/27` | `192.168.203.65` | `192.168.203.66` | `192.168.203.94` |
| Subnet 3 | E2 LAN | `192.168.203.96/27` | `192.168.203.97` | `192.168.203.98` | `192.168.203.126` |
| Subnet 4 | E1 LAN | `192.168.203.128/28` | `192.168.203.129` | `192.168.203.130` | `192.168.203.142` |
| Subnet 5 | WAN East-West | `192.168.203.144/30` | East: `192.168.203.145` | N/A | West: `192.168.203.146` |

## Part 2: Assign IP Addresses to Routers

### Step 1: Cấu Hình Router West

```text
West> enable
West# configure terminal

West(config)# interface g0/0
West(config-if)# description W1 LAN - 19 hosts
West(config-if)# ip address 192.168.203.65 255.255.255.224
West(config-if)# no shutdown
West(config-if)# exit

West(config)# interface g0/1
West(config-if)# description W2 LAN - 32 hosts
West(config-if)# ip address 192.168.203.1 255.255.255.192
West(config-if)# no shutdown
West(config-if)# exit

West(config)# interface s0/0/0
West(config-if)# description WAN to East
West(config-if)# ip address 192.168.203.146 255.255.255.252
West(config-if)# no shutdown
West(config-if)# exit

West(config)# end
West# copy running-config startup-config
```

### Step 2: Cấu Hình Router East

```text
East> enable
East# configure terminal

East(config)# interface g0/0
East(config-if)# description E1 LAN - 14 hosts
East(config-if)# ip address 192.168.203.129 255.255.255.240
East(config-if)# no shutdown
East(config-if)# exit

East(config)# interface g0/1
East(config-if)# description E2 LAN - 21 hosts
East(config-if)# ip address 192.168.203.97 255.255.255.224
East(config-if)# no shutdown
East(config-if)# exit

East(config)# interface s0/0/0
East(config-if)# description WAN to West
East(config-if)# ip address 192.168.203.145 255.255.255.252
East(config-if)# clock rate 64000
East(config-if)# no shutdown
East(config-if)# exit

East(config)# end
East# copy running-config startup-config
```

> `clock rate 64000` chỉ nhập trên đầu serial có ký hiệu DCE. Nếu Packet Tracer báo lỗi ở lệnh này, bỏ qua lệnh `clock rate` và tiếp tục `no shutdown`.

### Step 3: Kiểm Tra Router Interfaces

```text
West# show ip interface brief
East# show ip interface brief

! Kết quả mong muốn: G0/0, G0/1 và S0/0/0 đều up/up
```

![Router verification lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/router-verification.png)

## Part 3: Assign IP Addresses to Switches

### Step 1: Cấu Hình Switch WS-1

```text
WS-1> enable
WS-1# configure terminal
WS-1(config)# interface vlan 1
WS-1(config-if)# ip address 192.168.203.66 255.255.255.224
WS-1(config-if)# no shutdown
WS-1(config-if)# exit
WS-1(config)# ip default-gateway 192.168.203.65
WS-1(config)# end
WS-1# copy running-config startup-config
```

![WS-1 switch config lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/ws-1-config.png)

### Step 2: Cấu Hình Switch WS-2

```text
WS-2> enable
WS-2# configure terminal
WS-2(config)# interface vlan 1
WS-2(config-if)# ip address 192.168.203.2 255.255.255.192
WS-2(config-if)# no shutdown
WS-2(config-if)# exit
WS-2(config)# ip default-gateway 192.168.203.1
WS-2(config)# end
WS-2# copy running-config startup-config
```

![WS-2 switch config lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/ws-2-config.png)

### Step 3: Cấu Hình Switch ES-1

```text
ES-1> enable
ES-1# configure terminal
ES-1(config)# interface vlan 1
ES-1(config-if)# ip address 192.168.203.130 255.255.255.240
ES-1(config-if)# no shutdown
ES-1(config-if)# exit
ES-1(config)# ip default-gateway 192.168.203.129
ES-1(config)# end
ES-1# copy running-config startup-config
```

![ES-1 switch config lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/es-1-config.png)

### Step 4: Cấu Hình Switch ES-2

```text
ES-2> enable
ES-2# configure terminal
ES-2(config)# interface vlan 1
ES-2(config-if)# ip address 192.168.203.98 255.255.255.224
ES-2(config-if)# no shutdown
ES-2(config-if)# exit
ES-2(config)# ip default-gateway 192.168.203.97
ES-2(config)# end
ES-2# copy running-config startup-config
```

> `ip default-gateway` trên switch Layer 2 giúp switch đi ra ngoài subnet quản trị của chính nó.

### Step 5: Kiểm Tra Switch Management IP

```text
WS-1# show ip interface brief
WS-2# show ip interface brief
ES-1# show ip interface brief
ES-2# show ip interface brief

! Kết quả mong muốn: VLAN 1 có IP đúng và trạng thái up/up
```

![Switch verification lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/switch-verification.png)

## Part 4: Assign IP Addresses to PCs

### Step 1: Cấu Hình IP Cho Các PC

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| W1-201 | `192.168.203.94` | `255.255.255.224` | `192.168.203.65` |
| W2-87 | `192.168.203.62` | `255.255.255.192` | `192.168.203.1` |
| E1-22 | `192.168.203.142` | `255.255.255.240` | `192.168.203.129` |
| E2-47 | `192.168.203.126` | `255.255.255.224` | `192.168.203.97` |

![PC IP configuration lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/pc-ip-config.png)

### Step 2: Kiểm Tra IP Trên PC

```text
C:\> ipconfig

! Kiểm tra từng PC có đúng IP, subnet mask và default gateway theo bảng
```

## Part 5: Verify Connectivity

### Step 1: Ping Từ Các PC Đến Default Gateway

```text
! Từ W1-201
C:\> ping 192.168.203.65

! Từ W2-87
C:\> ping 192.168.203.1

! Từ E1-22
C:\> ping 192.168.203.129

! Từ E2-47
C:\> ping 192.168.203.97
```

![Gateway ping lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/gateway-ping.png)

### Step 2: Ping Giữa Các LAN

```text
! Từ W1-201 ping sang các host khác
C:\> ping 192.168.203.62
C:\> ping 192.168.203.142
C:\> ping 192.168.203.126

! Từ E2-47 ping ngược lại West LAN
C:\> ping 192.168.203.94
C:\> ping 192.168.203.62
```

![Inter LAN ping lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/inter-lan-ping.png)

### Step 3: Kiểm Tra Routing Nếu Ping Liên LAN Không Thành Công

```text
West# show ip route
East# show ip route

! Mỗi router phải biết các mạng trực tiếp connected và các mạng remote qua WAN
```

> Nếu file PKA chưa có định tuyến sẵn, thêm static route cho các mạng remote ở mục lỗi thường gặp bên dưới.

![Routing check lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/routing-check.png)

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| W2 LAN không đủ host | Chia `32 hosts` bằng `/27` | PC/switch/router không đủ usable IP | Đổi W2 LAN sang `/26`, network `192.168.203.0/26` |
| W1 và E2 bị sai IP dù cùng `/27` | Gán nhầm `192.168.203.64/27` cho E2 và `192.168.203.96/27` cho W1 | Assessment báo sai IP nhưng mask đúng | W1 dùng `.64/27`, E2 dùng `.96/27` theo file PKA này |
| PC không ping được gateway | Sai IP, subnet mask hoặc default gateway của PC | Dùng `ipconfig`, ping gateway fail | So lại bảng IP và sửa đúng gateway là IP router cùng LAN |
| Switch không ping ra ngoài subnet | Thiếu `ip default-gateway` trên switch | `show running-config` không có default gateway | Thêm `ip default-gateway` trỏ về router cùng LAN |
| Serial link không up | Chưa `no shutdown` hoặc thiếu clock rate ở đầu DCE | `show ip interface brief` thấy serial down/down | `no shutdown`, nếu là DCE thì thêm `clock rate 64000` |
| G0/0 và G0/1 bị gán ngược | Nhìn nhầm cổng nối vào switch | PC ping gateway fail dù IP đúng subnet | Đổi IP sang đúng interface đang nối thực tế |
| Dùng sai subnet mask | Nhầm `/26`, `/27`, `/28`, `/30` | Ping chỉ được một phần hoặc fail chéo subnet | Sửa mask theo bảng VLSM |
| Không ping được giữa East và West LAN | Thiếu route đến mạng remote | `show ip route` thiếu subnet phía router còn lại | Thêm static route hoặc kiểm tra routing có sẵn trong file PKA |

### Static Route Nhanh Nếu File PKA Chưa Có Routing

```text
West# configure terminal
West(config)# ip route 192.168.203.96 255.255.255.224 192.168.203.145
West(config)# ip route 192.168.203.128 255.255.255.240 192.168.203.145
West(config)# end
West# copy running-config startup-config

East# configure terminal
East(config)# ip route 192.168.203.0 255.255.255.192 192.168.203.146
East(config)# ip route 192.168.203.64 255.255.255.224 192.168.203.146
East(config)# end
East# copy running-config startup-config
```

> Chỉ dùng phần static route nếu Packet Tracer chưa có định tuyến sẵn và ping giữa các LAN ở hai router bị fail.

## 7. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| VLSM từ `192.168.203.0/24` | Chia đủ 5 subnet theo nhu cầu host |
| W2 LAN | Dùng `192.168.203.0/26`, gateway `192.168.203.1` |
| W1 LAN | Dùng `192.168.203.64/27`, gateway `192.168.203.65` |
| E2 LAN | Dùng `192.168.203.96/27`, gateway `192.168.203.97` |
| E1 LAN | Dùng `192.168.203.128/28`, gateway `192.168.203.129` |
| WAN East-West | Dùng `192.168.203.144/30`, East `.145`, West `.146` |
| Router interfaces | Các cổng `G0/0`, `G0/1`, `S0/0/0` đều `up/up` |
| Switch VLAN 1 | Có IP management và default gateway đúng |
| PC IP configuration | PC dùng last usable của subnet và gateway đúng |
| Ping cuối cùng | Các PC ping được gateway, switch và host ở LAN khác |

![Final result lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

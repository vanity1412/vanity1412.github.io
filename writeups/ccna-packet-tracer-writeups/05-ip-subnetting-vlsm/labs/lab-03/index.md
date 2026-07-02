---
layout: page-toc
title: "CCNA 05.03 - 11.9.3 Packet Tracer - VLSM Design and Implementation Practice"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `11.9.3 Packet Tracer - VLSM Design and Implementation Practice.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Thiết kế VLSM từ `10.11.48.0/24`, hoàn thiện địa chỉ còn thiếu và kiểm tra kết nối |

> Bài này không dùng một subnet mask cố định cho toàn mạng. Mục tiêu chính là chia VLSM theo số host: `60`, `30`, `14`, `6` và một đường WAN giữa `Branch1` - `Branch2`.

## 1. Mục Tiêu Bài Lab

- Xác định số subnet cần dùng trong topology.
- Thiết kế VLSM từ mạng gốc `10.11.48.0/24`.
- Gán subnet theo thứ tự từ mạng cần nhiều host nhất đến ít host nhất.
- Điền bảng địa chỉ cho router, switch và PC.
- Cấu hình các địa chỉ còn thiếu trên `Branch1`, `Room-312` và `PC-D`.
- Kiểm tra kết nối từ `Branch1`, `Room-312` và `PC-D` đến toàn bộ địa chỉ trong bảng.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/topology.png)

![Ảnh](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/topology1.png)

## 2. Topology Và Yêu Cầu Subnet

| Khu vực | Thiết bị liên quan | Số host cần | Ghi chú |
| --- | --- | ---: | --- |
| Room-407 LAN | Branch2, Room-407, PC-D | 60 | LAN lớn nhất, cấp subnet đầu tiên |
| Room-279 LAN | Branch1, Room-279, PC-B | 30 | LAN lớn thứ hai |
| Room-114 LAN | Branch1, Room-114, PC-A | 14 | LAN cỡ nhỏ |
| Room-312 LAN | Branch2, Room-312, PC-C | 6 | LAN nhỏ nhất |
| WAN Branch1-Branch2 | Branch1 S0/0/0, Branch2 S0/0/0 | 2 | Dùng subnet `/30` |

> **Lưu ý:** VLSM luôn chia từ subnet cần nhiều host nhất trước. Nếu chia mạng nhỏ trước, các mạng lớn phía sau có thể không còn block địa chỉ đủ rộng.

## 3. Thiết Kế VLSM

### 3.1. Số Subnet Cần Dùng

| Câu hỏi | Đáp án |
| --- | --- |
| Có bao nhiêu LAN trong topology? | 4 LAN |
| Có bao nhiêu WAN point-to-point? | 1 WAN |
| Tổng số subnet cần dùng | 5 subnet |

### 3.2. Chọn Subnet Mask Theo Số Host

| Khu vực | Host cần | Prefix phù hợp | Subnet mask | Usable host |
| --- | ---: | --- | --- | ---: |
| Room-407 | 60 | `/26` | `255.255.255.192` | 62 |
| Room-279 | 30 | `/27` | `255.255.255.224` | 30 |
| Room-114 | 14 | `/28` | `255.255.255.240` | 14 |
| Room-312 | 6 | `/29` | `255.255.255.248` | 6 |
| WAN Branch1-Branch2 | 2 | `/30` | `255.255.255.252` | 2 |

### 3.3. Subnet Table

| Thứ tự | Subnet Description | Host cần | Network Address/CIDR | First Usable Host | Last Usable Host | Broadcast |
| ---: | --- | ---: | --- | --- | --- | --- |
| 1 | Room-407 LAN | 60 | `10.11.48.0/26` | `10.11.48.1` | `10.11.48.62` | `10.11.48.63` |
| 2 | Room-279 LAN | 30 | `10.11.48.64/27` | `10.11.48.65` | `10.11.48.94` | `10.11.48.95` |
| 3 | Room-114 LAN | 14 | `10.11.48.96/28` | `10.11.48.97` | `10.11.48.110` | `10.11.48.111` |
| 4 | Room-312 LAN | 6 | `10.11.48.112/29` | `10.11.48.113` | `10.11.48.118` | `10.11.48.119` |
| 5 | WAN Branch1-Branch2 | 2 | `10.11.48.120/30` | `10.11.48.121` | `10.11.48.122` | `10.11.48.123` |

> **Lưu ý:** Các subnet còn lại trong `10.11.48.0/24` vẫn có thể để dành cho mở rộng, bắt đầu từ `10.11.48.124` trở đi tùy cách chia tiếp theo.

## 4. Bảng Địa Chỉ IP Hoàn Chỉnh

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| Branch1 | G0/0 | `10.11.48.97` | `255.255.255.240` | N/A |
| Branch1 | G0/1 | `10.11.48.65` | `255.255.255.224` | N/A |
| Branch1 | S0/0/0 | `10.11.48.121` | `255.255.255.252` | N/A |
| Branch2 | G0/0 | `10.11.48.113` | `255.255.255.248` | N/A |
| Branch2 | G0/1 | `10.11.48.1` | `255.255.255.192` | N/A |
| Branch2 | S0/0/0 | `10.11.48.122` | `255.255.255.252` | N/A |
| Room-114 | VLAN 1 | `10.11.48.98` | `255.255.255.240` | `10.11.48.97` |
| Room-279 | VLAN 1 | `10.11.48.66` | `255.255.255.224` | `10.11.48.65` |
| Room-312 | VLAN 1 | `10.11.48.114` | `255.255.255.248` | `10.11.48.113` |
| Room-407 | VLAN 1 | `10.11.48.2` | `255.255.255.192` | `10.11.48.1` |
| PC-A | NIC | `10.11.48.110` | `255.255.255.240` | `10.11.48.97` |
| PC-B | NIC | `10.11.48.94` | `255.255.255.224` | `10.11.48.65` |
| PC-C | NIC | `10.11.48.118` | `255.255.255.248` | `10.11.48.113` |
| PC-D | NIC | `10.11.48.62` | `255.255.255.192` | `10.11.48.1` |

> **Lưu ý:** Bảng trên gán theo topology đang mở: `Branch1` nối `Room-114` và `Room-279`, `Branch2` nối `Room-312` và `Room-407`. Nếu file PKA của bạn gắn ngược cổng `G0/0` và `G0/1`, giữ nguyên IP theo đúng LAN rồi đổi sang đúng interface đang nối thực tế.

## 5. Cấu Hình Từng Part

## Part 1: Thiết Kế Và Gán Địa Chỉ

### Step 1: Điền bảng VLSM

| Subnet | Gán cho | Network | Gateway/router IP | Switch IP | PC IP |
| --- | --- | --- | --- | --- | --- |
| Subnet 1 | Room-407 | `10.11.48.0/26` | `10.11.48.1` | `10.11.48.2` | `10.11.48.62` |
| Subnet 2 | Room-279 | `10.11.48.64/27` | `10.11.48.65` | `10.11.48.66` | `10.11.48.94` |
| Subnet 3 | Room-114 | `10.11.48.96/28` | `10.11.48.97` | `10.11.48.98` | `10.11.48.110` |
| Subnet 4 | Room-312 | `10.11.48.112/29` | `10.11.48.113` | `10.11.48.114` | `10.11.48.118` |
| Subnet 5 | WAN | `10.11.48.120/30` | `10.11.48.121` | N/A | `10.11.48.122` |

![VLSM design lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/vlsm-design.png)

## Part 2: Assign IP Addresses to Network Devices

### Step 1: Cấu Hình LAN Interfaces Trên Branch1

```text
Branch1> enable
Branch1# configure terminal

Branch1(config)# interface g0/0
Branch1(config-if)# description Room-114 LAN
Branch1(config-if)# ip address 10.11.48.97 255.255.255.240
Branch1(config-if)# no shutdown
Branch1(config-if)# exit

Branch1(config)# interface g0/1
Branch1(config-if)# description Room-279 LAN
Branch1(config-if)# ip address 10.11.48.65 255.255.255.224
Branch1(config-if)# no shutdown
Branch1(config-if)# exit

Branch1(config)# interface s0/0/0
Branch1(config-if)# description WAN to Branch2
Branch1(config-if)# ip address 10.11.48.121 255.255.255.252
Branch1(config-if)# no shutdown
Branch1(config-if)# exit

Branch1(config)# end
Branch1# copy running-config startup-config
```

> **Lưu ý:** Nếu cổng LAN trong file của bạn bị ngược so với bảng, chỉ đổi IP giữa `G0/0` và `G0/1`; không đổi subnet đã thiết kế.

![Branch1 config lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/branch1-config.png)

### Step 2: Cấu Hình IP Management Cho Room-312 Switch

```text
Room-312> enable
Room-312# configure terminal
Room-312(config)# interface vlan 1
Room-312(config-if)# ip address 10.11.48.114 255.255.255.248
Room-312(config-if)# no shutdown
Room-312(config-if)# exit
Room-312(config)# ip default-gateway 10.11.48.113
Room-312(config)# end
Room-312# copy running-config startup-config
```

> `ip default-gateway` trên switch Layer 2 dùng để switch có thể đi ra ngoài subnet quản trị của chính nó.

![Room-312 config lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/room-312-config.png)

### Step 3: Cấu Hình IP Cho PC-D

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC-D | `10.11.48.62` | `255.255.255.192` | `10.11.48.1` |

![PC-D IP configuration lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/pc-d-ip-config.png)

## Part 3: Verify Connectivity

### Step 1: Kiểm Tra Trên Branch1

```text
Branch1# show ip interface brief

! Ping default gateway/router interfaces và các host trong bảng
Branch1# ping 10.11.48.110
Branch1# ping 10.11.48.94
Branch1# ping 10.11.48.114
Branch1# ping 10.11.48.62
Branch1# ping 10.11.48.122
```

![Branch1 verification lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/branch1-verification.png)

### Step 2: Kiểm Tra Trên Room-312

```text
Room-312# show ip interface brief
Room-312# ping 10.11.48.113
Room-312# ping 10.11.48.118
Room-312# ping 10.11.48.62
Room-312# ping 10.11.48.110
```

![Room-312 verification lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/room-312-verification.png)

### Step 3: Kiểm Tra Trên PC-D

```text
C:\> ipconfig
C:\> ping 10.11.48.1
C:\> ping 10.11.48.62
C:\> ping 10.11.48.110
C:\> ping 10.11.48.94
C:\> ping 10.11.48.118
```

![PC-D ping lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/pc-d-ping.png)

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC-D không ping được gateway | Sai IP/mask/gateway của PC-D | `ipconfig`, ping `10.11.48.1` fail | Cấu hình PC-D: `10.11.48.62/26`, gateway `10.11.48.1` |
| Room-312 không ping ra ngoài được | Thiếu default gateway trên switch | `show running-config` không có `ip default-gateway` | Thêm `ip default-gateway 10.11.48.113` |
| Branch1 LAN không up | Interface đang shutdown | `show ip interface brief` thấy `administratively down` | Vào interface và dùng `no shutdown` |
| Dùng sai subnet mask | Nhầm `/26`, `/27`, `/28`, `/29` | Ping chỉ hoạt động trong vài host hoặc fail chéo LAN | So lại bảng VLSM và sửa mask đúng từng subnet |
| Cổng G0/0 và G0/1 bị gán ngược | Nhìn topology khác với bảng tự thiết kế | Ping gateway của PC-A/PC-B fail | Đổi IP giữa hai interface LAN trên router |
| Không ping được toàn mạng dù IP đúng | Routing giữa Branch1 và Branch2 chưa hoạt động trong file | `show ip route` thiếu mạng remote | Kiểm tra dynamic/static route đã có sẵn trong PKA |

## 7. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| VLSM từ `10.11.48.0/24` | Chia đủ 5 subnet theo nhu cầu host |
| Room-407 | Dùng `10.11.48.0/26` |
| Room-279 | Dùng `10.11.48.64/27` |
| Room-114 | Dùng `10.11.48.96/28` |
| Room-312 | Dùng `10.11.48.112/29` |
| WAN Branch1-Branch2 | Dùng `10.11.48.120/30` |
| Branch1 LAN interfaces | Có IP đúng và trạng thái `up/up` |
| Room-312 VLAN 1 | Có IP `10.11.48.114/29`, gateway `10.11.48.113` |
| PC-D | Có IP `10.11.48.62/26`, gateway `10.11.48.1` |
| Ping cuối cùng | Ping được mọi IP trong Addressing Table |

![PC-D ping lab 03](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-03/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

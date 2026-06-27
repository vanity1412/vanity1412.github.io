---
layout: page-toc
title: "CCNA 05.02 - 11.7.5 Packet Tracer - Subnetting Scenario"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `11.7.5 Packet Tracer - Subnetting Scenario.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Hoàn thành thiết kế subnet `/27`, gán địa chỉ cho R1/R2/S1-S4/PC1-PC4 và kiểm tra kết nối |

> **Ghi chú:** Bài này không dùng VLSM. Toàn bộ các mạng con được chia đều từ `192.168.100.0/24`, mỗi LAN cần tối thiểu 25 host và cần thêm một subnet cho kết nối WAN R1-R2.

## 1. Mục Tiêu Bài Lab

- Chia mạng `192.168.100.0/24` thành số subnet phù hợp với topology.
- Đảm bảo mỗi LAN có tối thiểu 25 địa chỉ usable host.
- Gán subnet cho 4 LAN và 1 WAN link giữa R1-R2.
- Hoàn thiện bảng địa chỉ IP cho router, switch và PC.
- Cấu hình địa chỉ IP trên các thiết bị còn thiếu.
- Kiểm tra kết nối từ R1, S3 và PC4 đến toàn bộ địa chỉ trong bảng.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/topology.png)

## 2. Thiết Kế Subnet

| Yêu cầu | Giá trị |
| --- | --- |
| Network gốc | `192.168.100.0/24` |
| Số LAN cần cấp địa chỉ | 4 LAN |
| Số WAN link cần cấp địa chỉ | 1 WAN |
| Tổng số subnet tối thiểu | 5 subnet |
| Số host tối thiểu mỗi LAN | 25 host |
| Subnet mask được chọn | `/27` |
| Subnet mask dạng thập phân | `255.255.255.224` |
| Số subnet tạo được | 8 subnet |
| Số host usable mỗi subnet | 30 host |
| Block size | 32 |

> **Lưu ý:** `/26` chỉ tạo được 4 subnet nên không đủ cho 4 LAN + 1 WAN. `/28` tạo được nhiều subnet hơn nhưng chỉ có 14 host usable/subnet nên không đủ 25 host. Vì vậy `/27` là lựa chọn phù hợp nhất.

### Trả Lời Câu Hỏi Subnetting

| Câu hỏi | Đáp án |
| --- | --- |
| Based on the topology, how many subnets are needed? | `5` subnet |
| How many bits must be borrowed? | `3` bit |
| How many subnets does this create? | `2^3 = 8` subnet |
| How many usable hosts per subnet? | `2^5 - 2 = 30` host |
| New prefix | `/27` |
| New subnet mask | `255.255.255.224` |

### Bảng Binary Cho 5 Subnet Đầu

| Subnet | Network Address | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `192.168.100.0` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | `192.168.100.32` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | `192.168.100.64` | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `192.168.100.96` | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 4 | `192.168.100.128` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Bảng Subnet Đầy Đủ

| Subnet Number | Subnet Address | First Usable Host | Last Usable Host | Broadcast Address |
| --- | --- | --- | --- | --- |
| 0 | `192.168.100.0/27` | `192.168.100.1` | `192.168.100.30` | `192.168.100.31` |
| 1 | `192.168.100.32/27` | `192.168.100.33` | `192.168.100.62` | `192.168.100.63` |
| 2 | `192.168.100.64/27` | `192.168.100.65` | `192.168.100.94` | `192.168.100.95` |
| 3 | `192.168.100.96/27` | `192.168.100.97` | `192.168.100.126` | `192.168.100.127` |
| 4 | `192.168.100.128/27` | `192.168.100.129` | `192.168.100.158` | `192.168.100.159` |
| 5 | `192.168.100.160/27` | `192.168.100.161` | `192.168.100.190` | `192.168.100.191` |
| 6 | `192.168.100.192/27` | `192.168.100.193` | `192.168.100.222` | `192.168.100.223` |
| 7 | `192.168.100.224/27` | `192.168.100.225` | `192.168.100.254` | `192.168.100.255` |

### Gán Subnet Theo Topology

| Subnet | Khu vực | Network |
| --- | --- | --- |
| Subnet 0 | LAN R1 G0/0 - S1 - PC1 | `192.168.100.0/27` |
| Subnet 1 | LAN R1 G0/1 - S2 - PC2 | `192.168.100.32/27` |
| Subnet 2 | LAN R2 G0/0 - S3 - PC3 | `192.168.100.64/27` |
| Subnet 3 | LAN R2 G0/1 - S4 - PC4 | `192.168.100.96/27` |
| Subnet 4 | WAN R1 S0/0/0 ↔ R2 S0/0/0 | `192.168.100.128/27` |

## 3. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `192.168.100.1` | `255.255.255.224` | N/A |
| R1 | G0/1 | `192.168.100.33` | `255.255.255.224` | N/A |
| R1 | S0/0/0 | `192.168.100.129` | `255.255.255.224` | N/A |
| R2 | G0/0 | `192.168.100.65` | `255.255.255.224` | N/A |
| R2 | G0/1 | `192.168.100.97` | `255.255.255.224` | N/A |
| R2 | S0/0/0 | `192.168.100.158` | `255.255.255.224` | N/A |
| S1 | VLAN 1 | `192.168.100.2` | `255.255.255.224` | `192.168.100.1` |
| S2 | VLAN 1 | `192.168.100.34` | `255.255.255.224` | `192.168.100.33` |
| S3 | VLAN 1 | `192.168.100.66` | `255.255.255.224` | `192.168.100.65` |
| S4 | VLAN 1 | `192.168.100.98` | `255.255.255.224` | `192.168.100.97` |
| PC1 | NIC | `192.168.100.30` | `255.255.255.224` | `192.168.100.1` |
| PC2 | NIC | `192.168.100.62` | `255.255.255.224` | `192.168.100.33` |
| PC3 | NIC | `192.168.100.94` | `255.255.255.224` | `192.168.100.65` |
| PC4 | NIC | `192.168.100.126` | `255.255.255.224` | `192.168.100.97` |

> **Lưu ý:** Theo yêu cầu đề, router dùng first usable trên từng LAN, switch dùng second usable, PC dùng last usable. Riêng WAN link: R1 dùng first usable của subnet 4, R2 dùng last usable của subnet 4.

## 4. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 1 | R1 G0/0, S1, PC1 | Subnet 0: `192.168.100.0/27` |
| LAN 2 | R1 G0/1, S2, PC2 | Subnet 1: `192.168.100.32/27` |
| LAN 3 | R2 G0/0, S3, PC3 | Subnet 2: `192.168.100.64/27` |
| LAN 4 | R2 G0/1, S4, PC4 | Subnet 3: `192.168.100.96/27` |
| WAN | R1 S0/0/0, R2 S0/0/0 | Subnet 4: `192.168.100.128/27` |

> **Lưu ý:** Bài cho biết EIGRP đã được cấu hình sẵn giữa R1 và R2. Phần mình cần hoàn thiện chủ yếu là địa chỉ IP còn thiếu trên R1, S3 và PC4 theo yêu cầu trong Part 2.

## 5. Part 1 - Design an IP Addressing Scheme

### Step 1 - Xác Định Subnet Mask

| Tiêu chí | Kết quả |
| --- | --- |
| Network ban đầu | `192.168.100.0/24` |
| Cần tối thiểu | 5 subnet |
| Cần tối thiểu | 25 host/subnet |
| Borrow bit | 3 bit |
| Host bit còn lại | 5 bit |
| Prefix mới | `/27` |
| Mask mới | `255.255.255.224` |
| Usable host/subnet | 30 host |

### Step 2 - Chia Subnet Và Gán Cho Topology

| Thứ tự | Subnet | Gán cho |
| --- | --- | --- |
| 0 | `192.168.100.0/27` | R1 G0/0 LAN |
| 1 | `192.168.100.32/27` | R1 G0/1 LAN |
| 2 | `192.168.100.64/27` | R2 G0/0 LAN |
| 3 | `192.168.100.96/27` | R2 G0/1 LAN |
| 4 | `192.168.100.128/27` | WAN R1-R2 |

### Step 3 - Hoàn Thiện Addressing Table

![Addressing table lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/addressing-table.png)

## 6. Part 2 - Assign IP Addresses to Network Devices

### Step 1 - Configure R1 LAN Interfaces

```text
R1> enable
R1# configure terminal
!
interface gigabitEthernet 0/0
 ip address 192.168.100.1 255.255.255.224
 no shutdown
 exit
!
interface gigabitEthernet 0/1
 ip address 192.168.100.33 255.255.255.224
 no shutdown
 exit
!
interface serial 0/0/0
 ip address 192.168.100.129 255.255.255.224
 no shutdown
 exit
!
end
copy running-config startup-config
```

> **Lưu ý:** Trong Packet Tracer, phần WAN có thể đã được cấu hình sẵn. Nếu `S0/0/0` đã đúng IP thì chỉ cần kiểm tra lại bằng `show ip interface brief`.

![R1 config lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/r1-config.png)

### Step 2 - Configure S3 VLAN 1

```text
S3> enable
S3# configure terminal
!
interface vlan 1
 ip address 192.168.100.66 255.255.255.224
 no shutdown
 exit
!
ip default-gateway 192.168.100.65
end
copy running-config startup-config
```

> **Lưu ý:** Switch Layer 2 cần `ip default-gateway` để có thể được quản trị từ subnet khác. Default gateway của S3 là IP router R2 G0/0 trong cùng subnet.

![S3 config lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/s3-config.png)

### Step 3 - Configure PC4

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC4 | `192.168.100.126` | `255.255.255.224` | `192.168.100.97` |

![PC4 IP configuration lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/pc4-ip-config.png)

### Kiểm Tra Cuối Part 2

```text
R1# show ip interface brief

! Kỳ vọng chính
GigabitEthernet0/0    192.168.100.1      YES manual up up
GigabitEthernet0/1    192.168.100.33     YES manual up up
Serial0/0/0           192.168.100.129    YES manual up up
```

```text
S3# show ip interface brief

! Kỳ vọng chính
Vlan1                 192.168.100.66     YES manual up up
```

![Show IP interface brief lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/show-ip-interface-brief.png)

## 7. Part 2 - Các Địa Chỉ Còn Lại Trong Bài

### R2

```text
R2> enable
R2# show ip interface brief

! Kỳ vọng
GigabitEthernet0/0    192.168.100.65     YES manual up up
GigabitEthernet0/1    192.168.100.97     YES manual up up
Serial0/0/0           192.168.100.158    YES manual up up
```

### S1, S2, S4

```text
! S1
interface vlan 1
 ip address 192.168.100.2 255.255.255.224
 no shutdown
exit
ip default-gateway 192.168.100.1

! S2
interface vlan 1
 ip address 192.168.100.34 255.255.255.224
 no shutdown
exit
ip default-gateway 192.168.100.33

! S4
interface vlan 1
 ip address 192.168.100.98 255.255.255.224
 no shutdown
exit
ip default-gateway 192.168.100.97
```

> **Lưu ý:** Các thiết bị này thường đã được cấu hình một phần trong file `.pka`. Mình vẫn ghi lại để đối chiếu khi kiểm tra hoặc khi cần sửa lỗi.

### PC1, PC2, PC3

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `192.168.100.30` | `255.255.255.224` | `192.168.100.1` |
| PC2 | `192.168.100.62` | `255.255.255.224` | `192.168.100.33` |
| PC3 | `192.168.100.94` | `255.255.255.224` | `192.168.100.65` |

## 8. Part 2 - Verify Connectivity

### Kiểm Tra Từ R1

```text
R1# ping 192.168.100.1
R1# ping 192.168.100.30
R1# ping 192.168.100.33
R1# ping 192.168.100.62
R1# ping 192.168.100.65
R1# ping 192.168.100.94
R1# ping 192.168.100.97
R1# ping 192.168.100.126
R1# ping 192.168.100.158
```

![R1 ping result lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/r1-ping-result.png)

### Kiểm Tra Từ S3

```text
S3# ping 192.168.100.65
S3# ping 192.168.100.1
S3# ping 192.168.100.30
S3# ping 192.168.100.126
```

![S3 ping result lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/s3-ping-result.png)

### Kiểm Tra Từ PC4

```text
PC> ping 192.168.100.97
PC> ping 192.168.100.65
PC> ping 192.168.100.94
PC> ping 192.168.100.30
PC> ping 192.168.100.62
```

![PC4 ping result lab 02](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-02/pc4-ping-result.png)

## 9. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Chọn `/28` | `/28` chỉ có 14 usable host, không đủ 25 host/LAN | Chọn `/27` |
| Chọn `/26` | `/26` chỉ tạo 4 subnet, thiếu subnet cho WAN | Chọn `/27` |
| PC không ping được gateway | Sai default gateway hoặc sai subnet mask | Kiểm tra IP PC theo bảng địa chỉ |
| S3 không ping được ra ngoài | Thiếu `ip default-gateway` | Cấu hình `ip default-gateway 192.168.100.65` |
| Interface router down | Chưa `no shutdown` | Vào interface và bật `no shutdown` |
| Ping giữa các LAN fail | Sai IP router hoặc EIGRP chưa học route | Kiểm tra `show ip route`, `show ip interface brief` |
| Nhầm last usable với broadcast | Dùng `.31`, `.63`, `.95`, `.127`, `.159` cho host | Chỉ dùng địa chỉ trước broadcast làm last usable |

## 10. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| Subnet mask được chọn | `/27 - 255.255.255.224` |
| Số subnet tạo được | 8 subnet |
| Số host usable mỗi subnet | 30 host |
| LAN R1 G0/0 | `192.168.100.0/27` |
| LAN R1 G0/1 | `192.168.100.32/27` |
| LAN R2 G0/0 | `192.168.100.64/27` |
| LAN R2 G0/1 | `192.168.100.96/27` |
| WAN R1-R2 | `192.168.100.128/27` |
| R1 LAN interfaces | Up/up |
| S3 VLAN 1 | Có IP `192.168.100.66/27` |
| PC4 | Có IP `192.168.100.126/27`, gateway `192.168.100.97` |
| Kết nối cuối | R1, S3 và PC4 ping được các IP trong bảng |

Checklist ảnh minh chứng:

- [ ] `topology.png` - sơ đồ mạng của bài.
- [ ] `addressing-table.png` - bảng địa chỉ sau khi điền.
- [ ] `subnet-table.png` - bảng chia subnet `/27`.
- [ ] `r1-config.png` - cấu hình R1.
- [ ] `s3-config.png` - cấu hình S3.
- [ ] `pc4-ip-config.png` - cấu hình IP PC4.
- [ ] `show-ip-interface-brief.png` - kết quả kiểm tra interface.
- [ ] `r1-ping-result.png` - ping từ R1.
- [ ] `s3-ping-result.png` - ping từ S3.
- [ ] `pc4-ping-result.png` - ping từ PC4.
- [ ] `check-results.png` - điểm hoàn thành trong Packet Tracer.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

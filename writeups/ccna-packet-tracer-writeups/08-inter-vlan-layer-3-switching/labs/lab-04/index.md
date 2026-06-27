---
layout: page-toc
title: "CCNA 08.04 - 4.5.1 Packet Tracer - Inter-VLAN Routing Challenge"
permalink: /writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-04/
toc: true
---

[← Quay lại danh sách Inter-VLAN Và Layer 3 Switching](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/)

| Field | Value |
| --- | --- |
| Dạng lab | Inter-VLAN Và Layer 3 Switching |
| File lab | `4.5.1 Packet Tracer - Inter-VLAN Routing Challenge.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Hoàn thành khi R1, S1, PC1, PC2, PC3 ping được nhau và ping được Server `172.17.50.254` |

> **Đặc điểm bài lab:** Đây là bài challenge tổng hợp Router-on-a-Stick. Bài không chỉ yêu cầu tạo VLAN và trunk, mà còn phải cấu hình subinterface trên R1, native VLAN, management VLAN, disable port không dùng và bảo đảm các VLAN truy cập được Server phía HQ.

## 1. Mục Tiêu Bài Lab

- Cấu hình địa chỉ IPv4 cho R1 theo Addressing Table.
- Tạo và đặt tên VLAN trên S1 đúng theo VLAN and Port Assignments Table.
- Gán các port access vào VLAN 10, VLAN 20, VLAN 30.
- Cấu hình trunk giữa S1 và R1, dùng VLAN 88 làm native VLAN.
- Cấu hình SVI VLAN 99 để quản trị S1.
- Cấu hình Router-on-a-Stick trên R1 bằng các subinterface `G0/1.x`.
- Tắt các port switch không được sử dụng.
- Lưu cấu hình và kiểm tra kết nối đến Server.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/topology.png)

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| R1 | G0/0 | `172.17.25.2` | `255.255.255.252` | N/A | Kết nối về HQ/Server |
| R1 | G0/1.10 | `172.17.10.1` | `255.255.255.0` | N/A | Gateway VLAN 10 |
| R1 | G0/1.20 | `172.17.20.1` | `255.255.255.0` | N/A | Gateway VLAN 20 |
| R1 | G0/1.30 | `172.17.30.1` | `255.255.255.0` | N/A | Gateway VLAN 30 |
| R1 | G0/1.88 | `172.17.88.1` | `255.255.255.0` | N/A | Native VLAN |
| R1 | G0/1.99 | `172.17.99.1` | `255.255.255.0` | N/A | Management VLAN |
| S1 | VLAN 99 | `172.17.99.10` | `255.255.255.0` | `172.17.99.1` | Quản trị switch |
| PC1 | NIC | `172.17.10.21` | `255.255.255.0` | `172.17.10.1` | VLAN 10 |
| PC2 | NIC | `172.17.20.22` | `255.255.255.0` | `172.17.20.1` | VLAN 20 |
| PC3 | NIC | `172.17.30.23` | `255.255.255.0` | `172.17.30.1` | VLAN 30 |
| Server | NIC | `172.17.50.254` | `255.255.255.0` | `172.17.50.1` | Server phía HQ |

> **Lưu ý:** Các địa chỉ `172.17.10.1`, `172.17.20.1`, `172.17.30.1`, `172.17.88.1`, `172.17.99.1` không đặt trực tiếp trên interface vật lý `G0/1`, mà đặt trên các subinterface của R1.

## 3. VLAN Và Port Assignments

| VLAN | Name | Interface | Vai trò |
| --- | --- | --- | --- |
| 10 | `Faculty/Staff` | `F0/11-17` | VLAN của PC1 |
| 20 | `Students` | `F0/18-24` | VLAN của PC2 |
| 30 | `Guest(Default)` | `F0/6-10` | VLAN của PC3 |
| 88 | `Native` | `G0/1` | Native VLAN trên trunk |
| 99 | `Management` | `VLAN 99` | Quản trị S1 |

> **Lưu ý:** VLAN name trong bài này nên gõ đúng từng ký tự vì Packet Tracer có thể chấm case-sensitive.

## 4. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Access VLAN | PC1, PC2, PC3, S1 | Ba PC nằm ở ba VLAN khác nhau nên không ping nhau nếu chưa có inter-VLAN routing |
| Router-on-a-Stick | R1 G0/1 ↔ S1 G0/1 | Link này phải là trunk và R1 phải có subinterface tương ứng từng VLAN |
| Management | S1 VLAN 99 | S1 cần IP quản trị và default gateway trỏ về `172.17.99.1` |
| Native VLAN | VLAN 88 | Native VLAN phải khớp giữa S1 trunk và subinterface R1 |
| HQ/Server | R1 G0/0 ↔ HQ ↔ Server | R1 cần route tới mạng Server nếu chưa có route mặc định |

> **Điểm dễ sai:** Nếu S1 `G0/1` vẫn là access port VLAN 1, các gói tin VLAN 10/20/30 sẽ không tới được đúng subinterface trên R1.

## 5. Part 1 - Cấu Hình S1 Theo VLAN Và Port Assignment

### Step 1 - Tạo VLAN và đặt tên VLAN

```text
S1> enable
S1# configure terminal
S1(config)# hostname S1

S1(config)# vlan 10
S1(config-vlan)# name Faculty/Staff
S1(config-vlan)# exit

S1(config)# vlan 20
S1(config-vlan)# name Students
S1(config-vlan)# exit

S1(config)# vlan 30
S1(config-vlan)# name Guest(Default)
S1(config-vlan)# exit

S1(config)# vlan 88
S1(config-vlan)# name Native
S1(config-vlan)# exit

S1(config)# vlan 99
S1(config-vlan)# name Management
S1(config-vlan)# exit
```

### Step 2 - Gán port access vào VLAN

```text
S1(config)# interface range f0/11-17
S1(config-if-range)# description Access ports - VLAN 10 Faculty/Staff
S1(config-if-range)# switchport mode access
S1(config-if-range)# switchport access vlan 10
S1(config-if-range)# no shutdown
S1(config-if-range)# exit

S1(config)# interface range f0/18-24
S1(config-if-range)# description Access ports - VLAN 20 Students
S1(config-if-range)# switchport mode access
S1(config-if-range)# switchport access vlan 20
S1(config-if-range)# no shutdown
S1(config-if-range)# exit

S1(config)# interface range f0/6-10
S1(config-if-range)# description Access ports - VLAN 30 Guest
S1(config-if-range)# switchport mode access
S1(config-if-range)# switchport access vlan 30
S1(config-if-range)# no shutdown
S1(config-if-range)# exit
```

### Step 3 - Cấu hình trunk từ S1 lên R1

```text
S1(config)# interface g0/1
S1(config-if)# description Trunk link to R1 G0/1
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk native vlan 88
S1(config-if)# no shutdown
S1(config-if)# exit
```

> **Lưu ý:** Vì R1 dùng nhiều subinterface `G0/1.x`, port `G0/1` trên S1 bắt buộc phải chạy trunk để mang nhiều VLAN trên cùng một đường vật lý.

### Step 4 - Cấu hình IP quản trị cho S1

```text
S1(config)# interface vlan 99
S1(config-if)# description Management SVI
S1(config-if)# ip address 172.17.99.10 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# ip default-gateway 172.17.99.1
```

### Step 5 - Tắt các port không sử dụng

```text
S1(config)# interface range f0/1-5
S1(config-if-range)# description Unused ports
S1(config-if-range)# shutdown
S1(config-if-range)# exit

S1(config)# interface g0/2
S1(config-if)# description Unused port
S1(config-if)# shutdown
S1(config-if)# exit

S1(config)# end
S1# copy running-config startup-config
```

> **Lưu ý:** Các port nằm trong dải đã gán VLAN không nên shutdown vì Packet Tracer có thể đang dùng một trong các port đó cho PC.

### Kiểm tra trên S1

```text
S1# show vlan brief

! Kỳ vọng:
! VLAN 10 có các port F0/11-17
! VLAN 20 có các port F0/18-24
! VLAN 30 có các port F0/6-10
! VLAN 88 và VLAN 99 tồn tại đúng tên
```

```text
S1# show interfaces trunk

! Kỳ vọng:
! G0/1 xuất hiện trong danh sách trunk
! Native VLAN là 88
! VLAN 10,20,30,88,99 được phép đi qua trunk
```

![S1 VLAN brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/s1-show-vlan-brief.png)
![S1 trunk](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/s1-show-interfaces-trunk.png)

## 6. Part 2 - Cấu Hình Router-on-a-Stick Trên R1

### Step 1 - Cấu hình interface vật lý ra HQ/Server

```text
R1> enable
R1# configure terminal
R1(config)# hostname R1

R1(config)# interface g0/0
R1(config-if)# description WAN link to HQ and Server network
R1(config-if)# ip address 172.17.25.2 255.255.255.252
R1(config-if)# no shutdown
R1(config-if)# exit
```

### Step 2 - Bật interface vật lý nối xuống S1

```text
R1(config)# interface g0/1
R1(config-if)# description Trunk link to S1 G0/1
R1(config-if)# no ip address
R1(config-if)# no shutdown
R1(config-if)# exit
```

> **Lưu ý:** Interface vật lý `G0/1` chỉ đóng vai trò đường trunk. IP gateway của từng VLAN đặt trên subinterface `G0/1.10`, `G0/1.20`, `G0/1.30`, `G0/1.88`, `G0/1.99`.

### Step 3 - Tạo subinterface cho từng VLAN

```text
R1(config)# interface g0/1.10
R1(config-subif)# description Gateway for VLAN 10 Faculty/Staff
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 172.17.10.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface g0/1.20
R1(config-subif)# description Gateway for VLAN 20 Students
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 172.17.20.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface g0/1.30
R1(config-subif)# description Gateway for VLAN 30 Guest
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 172.17.30.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface g0/1.88
R1(config-subif)# description Native VLAN 88
R1(config-subif)# encapsulation dot1Q 88 native
R1(config-subif)# ip address 172.17.88.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface g0/1.99
R1(config-subif)# description Gateway for VLAN 99 Management
R1(config-subif)# encapsulation dot1Q 99
R1(config-subif)# ip address 172.17.99.1 255.255.255.0
R1(config-subif)# exit
```

### Step 4 - Cấu hình route tới mạng Server

```text
R1(config)# ip route 172.17.50.0 255.255.255.0 172.17.25.1
R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** Nếu mô hình Packet Tracer đã cấu hình sẵn default route trên R1 thì lệnh route này có thể không bắt buộc. Nếu PC ping được gateway nhưng không ping được Server `172.17.50.254`, cần kiểm tra route từ R1 về mạng Server và route chiều ngược lại ở HQ.

### Kiểm tra trên R1

```text
R1# show ip interface brief

! Kỳ vọng:
! GigabitEthernet0/0      172.17.25.2    up/up
! GigabitEthernet0/1      unassigned     up/up
! GigabitEthernet0/1.10   172.17.10.1    up/up
! GigabitEthernet0/1.20   172.17.20.1    up/up
! GigabitEthernet0/1.30   172.17.30.1    up/up
! GigabitEthernet0/1.88   172.17.88.1    up/up
! GigabitEthernet0/1.99   172.17.99.1    up/up
```

```text
R1# show ip route

! Kỳ vọng có các route connected:
! C 172.17.10.0/24 is directly connected, GigabitEthernet0/1.10
! C 172.17.20.0/24 is directly connected, GigabitEthernet0/1.20
! C 172.17.30.0/24 is directly connected, GigabitEthernet0/1.30
! C 172.17.88.0/24 is directly connected, GigabitEthernet0/1.88
! C 172.17.99.0/24 is directly connected, GigabitEthernet0/1.99
! C 172.17.25.0/30 is directly connected, GigabitEthernet0/0
! S 172.17.50.0/24 [1/0] via 172.17.25.1
```

![R1 show ip interface brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/r1-show-ip-interface-brief.png)
![R1 show ip route](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/r1-show-ip-route.png)

## 7. Part 3 - Cấu Hình IP Cho PC Và Server

| Thiết bị | IP Address | Subnet Mask | Default Gateway | VLAN |
| --- | --- | --- | --- | --- |
| PC1 | `172.17.10.21` | `255.255.255.0` | `172.17.10.1` | VLAN 10 |
| PC2 | `172.17.20.22` | `255.255.255.0` | `172.17.20.1` | VLAN 20 |
| PC3 | `172.17.30.23` | `255.255.255.0` | `172.17.30.1` | VLAN 30 |
| Server | `172.17.50.254` | `255.255.255.0` | `172.17.50.1` | Server network |

![PC1 IP configuration](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/pc1-ip-config.png)
![PC2 IP configuration](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/pc2-ip-config.png)
![PC3 IP configuration](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/pc3-ip-config.png)

> **Lưu ý:** Default gateway của PC phải là IP subinterface cùng VLAN trên R1. PC1 không dùng gateway của VLAN 20 hoặc VLAN 30.

## 8. Part 4 - Kiểm Tra Kết Nối

### Kiểm tra từ PC1

```text
PC1> ping 172.17.10.1
! Ping gateway VLAN 10

PC1> ping 172.17.20.22
! Ping PC2 khác VLAN

PC1> ping 172.17.30.23
! Ping PC3 khác VLAN

PC1> ping 172.17.99.10
! Ping S1 management VLAN

PC1> ping 172.17.50.254
! Ping Server phía HQ
```

### Kiểm tra từ PC2

```text
PC2> ping 172.17.20.1
! Ping gateway VLAN 20

PC2> ping 172.17.10.21
! Ping PC1 khác VLAN

PC2> ping 172.17.30.23
! Ping PC3 khác VLAN

PC2> ping 172.17.50.254
! Ping Server phía HQ
```

### Kiểm tra từ PC3

```text
PC3> ping 172.17.30.1
! Ping gateway VLAN 30

PC3> ping 172.17.10.21
! Ping PC1 khác VLAN

PC3> ping 172.17.20.22
! Ping PC2 khác VLAN

PC3> ping 172.17.50.254
! Ping Server phía HQ
```

### Kiểm tra từ S1

```text
S1# ping 172.17.99.1
! Ping gateway quản trị trên R1

S1# ping 172.17.10.21
! Ping PC1

S1# ping 172.17.20.22
! Ping PC2

S1# ping 172.17.30.23
! Ping PC3

S1# ping 172.17.50.254
! Ping Server
```

![Ping inter VLAN](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/ping-inter-vlan.png)
![Ping server](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-04/ping-server.png)

## 9. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC ping gateway thất bại | Port access gán sai VLAN hoặc port bị shutdown | Kiểm tra `show vlan brief`, bật lại port và gán đúng VLAN |
| PC cùng VLAN khác port range không hoạt động | Dải port VLAN bị gán thiếu | Kiểm tra lại `F0/11-17`, `F0/18-24`, `F0/6-10` |
| PC khác VLAN không ping nhau | Thiếu subinterface trên R1 hoặc subinterface sai `encapsulation dot1Q` | Kiểm tra `show ip interface brief` và cấu hình lại `G0/1.x` |
| Trunk không hoạt động | S1 `G0/1` chưa cấu hình trunk | Dùng `switchport mode trunk` và kiểm tra `show interfaces trunk` |
| Native VLAN mismatch | S1 native VLAN khác R1 subinterface native | S1 dùng `switchport trunk native vlan 88`, R1 dùng `encapsulation dot1Q 88 native` |
| S1 không ping được thiết bị khác | Thiếu IP VLAN 99 hoặc thiếu default gateway | Cấu hình `interface vlan 99` và `ip default-gateway 172.17.99.1` |
| PC ping được R1 nhưng không ping được Server | R1 thiếu route tới mạng `172.17.50.0/24` hoặc HQ thiếu route chiều ngược | Thêm static route trên R1, kiểm tra route phía HQ nếu được phép |
| Check Results thiếu điểm disable port | Chưa shutdown các port không thuộc bảng VLAN/Trunk | Shutdown `F0/1-5` và `G0/2` |

## 10. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| VLAN trên S1 | Có VLAN 10, 20, 30, 88, 99 đúng tên |
| Access port | `F0/11-17` VLAN 10, `F0/18-24` VLAN 20, `F0/6-10` VLAN 30 |
| Trunk S1-R1 | `G0/1` trunk, native VLAN 88 |
| R1 subinterfaces | `G0/1.10`, `.20`, `.30`, `.88`, `.99` up/up và đúng IP |
| S1 management | VLAN 99 IP `172.17.99.10/24`, gateway `172.17.99.1` |
| Inter-VLAN routing | PC1, PC2, PC3 ping được nhau |
| Server connectivity | PC1, PC2, PC3, S1, R1 ping được `172.17.50.254` |
| Save config | R1 và S1 đã `copy running-config startup-config` |

- [ ] Ảnh topology bài lab.
- [ ] Ảnh `show vlan brief` trên S1.
- [ ] Ảnh `show interfaces trunk` trên S1.
- [ ] Ảnh `show ip interface brief` trên R1.
- [ ] Ảnh `show ip route` trên R1.
- [ ] Ảnh PC1 ping PC2/PC3/Server.
- [ ] Ảnh Check Results hoàn thành.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 4 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-01/">Lab 1: 4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/">Lab 2: 4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/">Lab 3: 4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 4.5.1 Packet Tracer - Inter-VLAN Routing Challenge (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

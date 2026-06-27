---
layout: page-toc
title: "CCNA 08.03 - 4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing"
permalink: /writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/
toc: true
---

[← Quay lại danh sách Inter-VLAN Và Layer 3 Switching](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/)

| Field | Value |
| --- | --- |
| Dạng lab | Inter-VLAN Và Layer 3 Switching |
| File lab | `4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Troubleshoot router-on-a-stick để PC1 VLAN 10 và PC3 VLAN 30 ping được nhau |

> Bài này không phải cấu hình mới hoàn toàn. Trọng tâm là kiểm tra VLAN, access port, trunk port, subinterface trên router và sửa các lỗi làm inter-VLAN routing không hoạt động.

## 1. Mục Tiêu Bài Lab

- Kiểm tra lỗi kết nối giữa hai VLAN khác nhau.
- Xác minh VLAN 10 và VLAN 30 trên switch S1.
- Kiểm tra cổng access nối PC1 và PC3.
- Kiểm tra trunk giữa S1 và R1.
- Kiểm tra subinterface router-on-a-stick trên R1.
- Sửa lỗi cấu hình và xác minh PC1 ping được PC3.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/topology.png)

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway | VLAN |
| --- | --- | --- | --- | --- | --- |
| R1 | G0/1.10 | 172.17.10.1 | 255.255.255.0 | N/A | VLAN 10 |
| R1 | G0/1.30 | 172.17.30.1 | 255.255.255.0 | N/A | VLAN 30 |
| PC1 | NIC | 172.17.10.10 | 255.255.255.0 | 172.17.10.1 | VLAN 10 |
| PC3 | NIC | 172.17.30.10 | 255.255.255.0 | 172.17.30.1 | VLAN 30 |

> **Lưu ý:** Default gateway của mỗi PC phải trỏ về IP subinterface tương ứng trên R1. PC1 dùng `172.17.10.1`, PC3 dùng `172.17.30.1`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| VLAN 10 | PC1, S1 F0/11, R1 G0/1.10 | PC1 thuộc mạng `172.17.10.0/24` |
| VLAN 30 | PC3, S1 F0/6, R1 G0/1.30 | PC3 thuộc mạng `172.17.30.0/24` |
| Trunk | S1 G0/1 ↔ R1 G0/1 | Phải mang được VLAN 10 và VLAN 30 |
| Router-on-a-stick | R1 G0/1.10 và G0/1.30 | Mỗi VLAN dùng một subinterface riêng |

> **Điểm dễ sai:** Cấu hình IP trên subinterface đúng vẫn chưa đủ. Nếu cổng `S1 G0/1` không phải trunk hoặc cổng `R1 G0/1` chưa `no shutdown`, PC khác VLAN vẫn không ping được nhau.

## 4. Part 1 - Locate Network Problems

### Kiểm tra nhanh từ PC

```text
PC1> ping 172.17.10.1
! Kiểm tra PC1 ping default gateway VLAN 10

PC3> ping 172.17.30.1
! Kiểm tra PC3 ping default gateway VLAN 30

PC1> ping 172.17.30.10
! Kiểm tra inter-VLAN routing từ PC1 sang PC3
```

![Ping test before fix](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/ping-before-fix.png)

### Kiểm tra trên R1

```text
R1# show ip interface brief
R1# show interface g0/1.10
R1# show interface g0/1.30
R1# show running-config | section interface GigabitEthernet0/1
```

| Nội dung cần kiểm tra | Trạng thái đúng |
| --- | --- |
| `G0/1` | Up/Up sau khi bật `no shutdown` |
| `G0/1.10` | IP `172.17.10.1/24`, encapsulation dot1Q 10 |
| `G0/1.30` | IP `172.17.30.1/24`, encapsulation dot1Q 30 |
| Physical interface | Không đặt IP trực tiếp trên `G0/1` khi dùng router-on-a-stick |

![R1 show ip interface brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/r1-show-ip-interface-brief.png)

### Kiểm tra trên S1

```text
S1# show vlan brief
S1# show interfaces trunk
S1# show running-config interface f0/11
S1# show running-config interface f0/6
S1# show running-config interface g0/1
```

| Nội dung cần kiểm tra | Trạng thái đúng |
| --- | --- |
| VLAN 10 | Tồn tại trên S1 |
| VLAN 30 | Tồn tại trên S1 |
| F0/11 | Access port thuộc VLAN 10 |
| F0/6 | Access port thuộc VLAN 30 |
| G0/1 | Trunk port, cho phép VLAN 10 và VLAN 30 đi qua |

![S1 show vlan brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/s1-show-vlan-brief.png)

### Documentation Table

| Problems | Solutions |
| --- | --- |
| PC1 và PC3 không ping được nhau | Kiểm tra đủ 3 phần: access VLAN, trunk, router subinterface |
| VLAN 10 hoặc VLAN 30 chưa tồn tại trên S1 | Tạo lại VLAN bằng `vlan 10` và `vlan 30` |
| F0/11 bị gán sai VLAN | Cấu hình `switchport access vlan 10` |
| F0/6 bị gán sai VLAN | Cấu hình `switchport access vlan 30` |
| G0/1 của S1 chưa ở chế độ trunk | Cấu hình `switchport mode trunk` |
| R1 subinterface sai encapsulation | Cấu hình `encapsulation dot1Q 10` và `encapsulation dot1Q 30` đúng VLAN |
| R1 subinterface sai IP | Gán đúng `172.17.10.1/24` và `172.17.30.1/24` |
| Physical interface R1 G0/1 bị shutdown | Vào `interface g0/1` và dùng `no shutdown` |

> **Lưu ý:** Documentation Table trong bài troubleshoot nên ghi theo dạng “lỗi phát hiện được” và “cách sửa”. Khi làm thật trong Packet Tracer, mình đối chiếu output hiện tại rồi đánh dấu lỗi nào đang tồn tại.

## 5. Part 2 - Implement the Solution

### Cấu hình sửa lỗi trên R1

```text
R1> enable
R1# configure terminal

R1(config)# interface gigabitEthernet 0/1
R1(config-if)# no ip address
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface gigabitEthernet 0/1.10
R1(config-subif)# description Default gateway for VLAN 10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 172.17.10.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface gigabitEthernet 0/1.30
R1(config-subif)# description Default gateway for VLAN 30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 172.17.30.1 255.255.255.0
R1(config-subif)# exit

R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** `encapsulation dot1Q` là phần bắt buộc để router hiểu frame đi vào thuộc VLAN nào. Nếu VLAN tag trên router không khớp với VLAN trên switch, inter-VLAN routing sẽ lỗi.

### Cấu hình sửa lỗi trên S1

```text
S1> enable
S1# configure terminal

S1(config)# vlan 10
S1(config-vlan)# name VLAN10
S1(config-vlan)# exit

S1(config)# vlan 30
S1(config-vlan)# name VLAN30
S1(config-vlan)# exit

S1(config)# interface fastEthernet 0/11
S1(config-if)# description Access port to PC1 - VLAN 10
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 10
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# interface fastEthernet 0/6
S1(config-if)# description Access port to PC3 - VLAN 30
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 30
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# interface gigabitEthernet 0/1
S1(config-if)# description Trunk to R1 G0/1
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk allowed vlan 10,30
S1(config-if)# no shutdown
S1(config-if)# exit

S1(config)# end
S1# copy running-config startup-config
```

> **Lưu ý:** Trunk port sẽ không còn xuất hiện như một access port trong `show vlan brief`. Muốn kiểm tra trunk phải dùng `show interfaces trunk`.

## 6. Part 3 - Verify Network Connectivity

### Kiểm tra R1

```text
R1# show ip interface brief

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/1     unassigned      YES unset  up                    up
GigabitEthernet0/1.10  172.17.10.1     YES manual up                    up
GigabitEthernet0/1.30  172.17.30.1     YES manual up                    up
```

![R1 interfaces after fix](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/r1-interfaces-after-fix.png)

### Kiểm tra S1

```text
S1# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
10   VLAN10                           active    Fa0/11
30   VLAN30                           active    Fa0/6
```

```text
S1# show interfaces trunk

Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gi0/1       10,30
```

![S1 trunk after fix](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/s1-trunk-after-fix.png)

### Kiểm tra ping cuối cùng

```text
PC1> ping 172.17.10.1
! PC1 ping default gateway VLAN 10: thành công

PC3> ping 172.17.30.1
! PC3 ping default gateway VLAN 30: thành công

PC1> ping 172.17.30.10
! PC1 ping PC3 khác VLAN: thành công

PC3> ping 172.17.10.10
! PC3 ping PC1 khác VLAN: thành công
```

![Final ping test](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-03/final-ping-test.png)

## 7. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC ping gateway không được | Access port sai VLAN hoặc subinterface router sai IP | Kiểm tra `show vlan brief`, `show ip interface brief` |
| PC cùng VLAN không ổn định | Cổng access chưa đúng VLAN hoặc dây/cổng sai | Sửa `switchport mode access` và `switchport access vlan` |
| PC khác VLAN ping thất bại | Trunk chưa bật hoặc subinterface dot1Q sai | Kiểm tra `show interfaces trunk` và `show interface g0/1.x` |
| `G0/1.10` và `G0/1.30` down/down | Physical interface `G0/1` đang shutdown | Vào `interface g0/1`, dùng `no shutdown` |
| `show vlan brief` không thấy G0/1 trong VLAN 10/30 | G0/1 đang là trunk port | Đây là bình thường, kiểm tra bằng `show interfaces trunk` |
| PC dùng sai default gateway | Gateway không trỏ về subinterface cùng VLAN | PC1 dùng `172.17.10.1`, PC3 dùng `172.17.30.1` |

## 8. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| VLAN 10 | Có trên S1, chứa F0/11 |
| VLAN 30 | Có trên S1, chứa F0/6 |
| Trunk S1 G0/1 | Trunking, allowed VLAN 10,30 |
| R1 G0/1.10 | `172.17.10.1/24`, dot1Q 10, up/up |
| R1 G0/1.30 | `172.17.30.1/24`, dot1Q 30, up/up |
| PC1 → Gateway | Ping `172.17.10.1` thành công |
| PC3 → Gateway | Ping `172.17.30.1` thành công |
| PC1 ↔ PC3 | Ping qua lại thành công |
| Check Results | Hoàn thành sau khi sửa đúng lỗi cấu hình |

- [ ] Ảnh topology: `topology.png`
- [ ] Ảnh `show vlan brief` trên S1
- [ ] Ảnh `show interfaces trunk` trên S1
- [ ] Ảnh `show ip interface brief` trên R1
- [ ] Ảnh ping PC1 sang PC3 thành công
- [ ] Ảnh Check Results hoàn thành

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 4 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-01/">Lab 1: 4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/">Lab 2: 4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-04/">Lab 4: 4.5.1 Packet Tracer - Inter-VLAN Routing Challenge</a></li>
    </ul>
  </details>
</div>

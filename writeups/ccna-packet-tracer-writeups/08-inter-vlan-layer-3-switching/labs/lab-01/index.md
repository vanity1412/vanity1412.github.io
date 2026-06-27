---
layout: page-toc
title: "CCNA 08.01 - 4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing"
permalink: /writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-01/
toc: true
---

[← Quay lại danh sách Inter-VLAN Và Layer 3 Switching](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/)

| Field | Value |
| --- | --- |
| Dạng lab | Inter-VLAN Và Layer 3 Switching |
| File lab | `4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành VLAN 10, VLAN 30, router-on-a-stick, trunk G0/1 và kiểm tra ping liên VLAN |

> **Ghi chú:** Bài này là dạng cấu hình Inter-VLAN Routing bằng router-on-a-stick. Switch S1 chia PC vào VLAN 10 và VLAN 30, còn R1 dùng subinterface `G0/0.10` và `G0/0.30` làm default gateway cho từng VLAN.

## 1. Mục Tiêu Bài Lab

- Tạo VLAN 10 và VLAN 30 trên switch S1.
- Gán cổng access cho PC1 và PC3 đúng VLAN.
- Cấu hình subinterface trên R1 với chuẩn đóng gói 802.1Q.
- Bật interface vật lý `G0/0` trên R1 để các subinterface hoạt động.
- Cấu hình trunk trên cổng `G0/1` của S1 nối lên R1.
- Kiểm tra PC1 ping được PC3 thông qua Inter-VLAN Routing.
- Lưu cấu hình trên router và switch.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/topology.png)

## 2. Bảng Địa Chỉ IPv4

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0.10 | 172.17.10.1 | 255.255.255.0 | N/A |
| R1 | G0/0.30 | 172.17.30.1 | 255.255.255.0 | N/A |
| PC1 | NIC | 172.17.10.10 | 255.255.255.0 | 172.17.10.1 |
| PC3 | NIC | 172.17.30.10 | 255.255.255.0 | 172.17.30.1 |

> **Lưu ý:** Trong một số bản đề, bảng địa chỉ có thể ghi nhầm `PC2`, nhưng topology và yêu cầu kiểm tra dùng máy ở VLAN 30 là `PC3`. Mình cấu hình máy bên phải là `PC3` với IP `172.17.30.10/24`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| VLAN 10 | PC1, S1 F0/11 | PC1 nằm trong mạng `172.17.10.0/24`, gateway là `172.17.10.1` |
| VLAN 30 | PC3, S1 F0/6 | PC3 nằm trong mạng `172.17.30.0/24`, gateway là `172.17.30.1` |
| Trunk link | S1 G0/1 ↔ R1 G0/0 | Cần trunk để mang traffic VLAN 10 và VLAN 30 lên router |
| Router-on-a-stick | R1 G0/0.10, G0/0.30 | Mỗi subinterface đại diện cho một VLAN và một default gateway |

> **Điểm dễ sai:** Tạo subinterface trên router chưa đủ. Nếu quên `no shutdown` trên `G0/0` hoặc quên trunk `G0/1` trên switch thì PC khác VLAN vẫn không ping được nhau.

## 4. Part 1 - Add VLANs to a Switch

### Step 1 - Tạo VLAN 10 và VLAN 30 trên S1

```text
S1> enable
S1# configure terminal
S1(config)# vlan 10
S1(config-vlan)# name VLAN0010
S1(config-vlan)# exit
S1(config)# vlan 30
S1(config-vlan)# name VLAN0030
S1(config-vlan)# exit
S1(config)# end
S1# show vlan brief
```

> `vlan 10` và `vlan 30` chỉ tạo VLAN trong database của switch. Muốn PC thuộc VLAN nào thì vẫn phải gán cổng switch vào VLAN đó.

![S1 VLAN created](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/s1-vlan-created.png)

### Step 2 - Gán cổng access cho PC1 và PC3

```text
S1# configure terminal
S1(config)# interface fastEthernet 0/11
S1(config-if)# description Access port to PC1 - VLAN 10
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 10
S1(config-if)# exit
S1(config)# interface fastEthernet 0/6
S1(config-if)# description Access port to PC3 - VLAN 30
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 30
S1(config-if)# exit
S1(config)# end
S1# show vlan brief
```

| Cổng trên S1 | Thiết bị nối vào | VLAN | Vai trò |
| --- | --- | --- | --- |
| F0/11 | PC1 | VLAN 10 | Access port |
| F0/6 | PC3 | VLAN 30 | Access port |
| G0/1 | R1 G0/0 | Trunk | Chưa cấu hình ở bước này |

Kết quả `show vlan brief` cần thấy `Fa0/11` nằm trong VLAN 10 và `Fa0/6` nằm trong VLAN 30.

```text
S1# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/12, Fa0/13, Fa0/14
                                                Fa0/15, Fa0/16, Fa0/17, Fa0/18
                                                Fa0/19, Fa0/20, Fa0/21, Fa0/22
                                                Fa0/23, Fa0/24, Gig0/1, Gig0/2
10   VLAN0010                         active    Fa0/11
30   VLAN0030                         active    Fa0/6
```

![S1 show vlan brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/s1-show-vlan-brief.png)

### Step 3 - Kiểm tra ping trước khi cấu hình Inter-VLAN Routing

```text
PC1> ping 172.17.30.10

Pinging 172.17.30.10 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.
```

| Câu hỏi | Trả lời |
| --- | --- |
| Ping từ PC1 sang PC3 có thành công không? | Không thành công |
| Vì sao? | PC1 và PC3 nằm ở hai VLAN/subnet khác nhau. Switch Layer 2 không tự định tuyến giữa VLAN 10 và VLAN 30. Cần router hoặc Layer 3 switch làm Inter-VLAN Routing. |

![PC1 ping PC3 before routing](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/pc1-ping-pc3-before-routing.png)

## 5. Part 2 - Configure Subinterfaces

### Step 1 - Cấu hình subinterface trên R1

```text
R1> enable
R1# configure terminal
R1(config)# interface gigabitEthernet 0/0.10
R1(config-subif)# description Default gateway for VLAN 10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 172.17.10.1 255.255.255.0
R1(config-subif)# exit
R1(config)# interface gigabitEthernet 0/0.30
R1(config-subif)# description Default gateway for VLAN 30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 172.17.30.1 255.255.255.0
R1(config-subif)# exit
R1(config)# interface gigabitEthernet 0/0
R1(config-if)# description Trunk link to S1 G0/1
R1(config-if)# no shutdown
R1(config-if)# end
R1# copy running-config startup-config
```

> `encapsulation dot1Q 10` giúp subinterface `G0/0.10` nhận frame thuộc VLAN 10. Tương tự, `encapsulation dot1Q 30` dùng cho VLAN 30.
>
> **Lưu ý:** Subinterface phụ thuộc vào interface vật lý. Nếu `G0/0` còn `administratively down`, cả `G0/0.10` và `G0/0.30` cũng không hoạt động.

![R1 subinterfaces configured](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/r1-subinterfaces-configured.png)

### Step 2 - Kiểm tra subinterface trên R1

```text
R1# show ip interface brief

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up
GigabitEthernet0/0.10  172.17.10.1     YES manual up                    up
GigabitEthernet0/0.30  172.17.30.1     YES manual up                    up
```

| Interface | Kết quả đúng | Ghi chú |
| --- | --- | --- |
| G0/0 | up/up | Interface vật lý đã được bật bằng `no shutdown` |
| G0/0.10 | up/up | Gateway của VLAN 10 |
| G0/0.30 | up/up | Gateway của VLAN 30 |

![R1 show ip interface brief](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/r1-show-ip-interface-brief.png)

## 6. Part 3 - Test Connectivity with Inter-VLAN Routing

### Step 1 - Ping lại sau khi cấu hình subinterface

```text
PC1> ping 172.17.30.10

Pinging 172.17.30.10 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.
```

| Câu hỏi | Trả lời |
| --- | --- |
| Ping lúc này đã thành công chưa? | Vẫn có thể chưa thành công |
| Vì sao? | Router đã có subinterface nhưng cổng S1 nối lên router vẫn đang là access port VLAN 1. Traffic VLAN 10 và VLAN 30 chưa được trunk lên R1. |

### Step 2 - Kiểm tra VLAN của G0/1 trước khi trunk

```text
S1# show vlan brief
```

| Câu hỏi | Trả lời |
| --- | --- |
| G0/1 đang thuộc VLAN nào trước khi cấu hình trunk? | VLAN 1 |
| Nhận biết bằng `show vlan brief` như thế nào? | Trước khi trunk, `Gig0/1` xuất hiện trong danh sách port của VLAN 1. Sau khi trunk, trunk port sẽ không còn hiển thị như một access port trong bảng VLAN thông thường. |

### Step 3 - Bật trunk trên S1 G0/1

```text
S1# configure terminal
S1(config)# interface gigabitEthernet 0/1
S1(config-if)# description Trunk link to R1 G0/0
S1(config-if)# switchport mode trunk
S1(config-if)# exit
S1(config)# end
S1# show interfaces trunk
S1# copy running-config startup-config
```

> Với router-on-a-stick, đường nối từ switch lên router phải là trunk để mang nhiều VLAN qua cùng một cổng vật lý.

Kết quả kiểm tra trunk cần thấy `Gi0/1` ở trạng thái trunking.

```text
S1# show interfaces trunk

Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gi0/1       1-1005
```

![S1 show interfaces trunk](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/s1-show-interfaces-trunk.png)

### Step 4 - Cấu hình IP trên PC

| PC | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | 172.17.10.10 | 255.255.255.0 | 172.17.10.1 |
| PC3 | 172.17.30.10 | 255.255.255.0 | 172.17.30.1 |

![PC1 IP configuration](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/pc1-ip-configuration.png)

![PC3 IP configuration](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/pc3-ip-configuration.png)

### Step 5 - Kiểm tra ping sau khi hoàn tất trunk

```text
PC1> ping 172.17.10.1
! PC1 ping default gateway VLAN 10

PC1> ping 172.17.30.1
! PC1 ping default gateway VLAN 30 trên router

PC1> ping 172.17.30.10
! PC1 ping PC3 khác VLAN

PC3> ping 172.17.30.1
! PC3 ping default gateway VLAN 30

PC3> ping 172.17.10.10
! PC3 ping PC1 khác VLAN
```

| Câu hỏi | Trả lời |
| --- | --- |
| PC1 dùng default gateway nào? | `172.17.10.1` |
| PC3 dùng default gateway nào? | `172.17.30.1` |
| Khi cấu hình đúng, PC1 và PC3 có ping được nhau không? | Có |

![PC1 ping PC3 success](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/pc1-ping-pc3-success.png)

## 7. Cấu Hình Hoàn Chỉnh

### S1

```text
S1> enable
S1# configure terminal
S1(config)# vlan 10
S1(config-vlan)# name VLAN0010
S1(config-vlan)# exit
S1(config)# vlan 30
S1(config-vlan)# name VLAN0030
S1(config-vlan)# exit
S1(config)# interface fastEthernet 0/11
S1(config-if)# description Access port to PC1 - VLAN 10
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 10
S1(config-if)# exit
S1(config)# interface fastEthernet 0/6
S1(config-if)# description Access port to PC3 - VLAN 30
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 30
S1(config-if)# exit
S1(config)# interface gigabitEthernet 0/1
S1(config-if)# description Trunk link to R1 G0/0
S1(config-if)# switchport mode trunk
S1(config-if)# exit
S1(config)# end
S1# copy running-config startup-config
```

### R1

```text
R1> enable
R1# configure terminal
R1(config)# interface gigabitEthernet 0/0.10
R1(config-subif)# description Default gateway for VLAN 10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 172.17.10.1 255.255.255.0
R1(config-subif)# exit
R1(config)# interface gigabitEthernet 0/0.30
R1(config-subif)# description Default gateway for VLAN 30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 172.17.30.1 255.255.255.0
R1(config-subif)# exit
R1(config)# interface gigabitEthernet 0/0
R1(config-if)# description Trunk link to S1 G0/1
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# end
R1# copy running-config startup-config
```

## 8. Kiểm Tra Và Bằng Chứng

| Kiểm tra | Lệnh | Kết quả mong muốn |
| --- | --- | --- |
| VLAN đã tạo | `show vlan brief` | Có VLAN 10 và VLAN 30 |
| PC đúng VLAN | `show vlan brief` | `Fa0/11` thuộc VLAN 10, `Fa0/6` thuộc VLAN 30 |
| Trunk hoạt động | `show interfaces trunk` | `Gi0/1` ở trạng thái trunking |
| Subinterface hoạt động | `show ip interface brief` | `G0/0.10` và `G0/0.30` up/up |
| PC ping gateway | `ping 172.17.10.1`, `ping 172.17.30.1` | Thành công |
| Ping liên VLAN | PC1 ping `172.17.30.10` | Thành công |
| Lưu cấu hình | `copy running-config startup-config` | `[OK]` |

![Check results lab 01](/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/labs/lab-01/check-results.png)

## 9. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC1 không ping được PC3 trước khi cấu hình router | Hai PC nằm ở hai VLAN/subnet khác nhau | Cấu hình router-on-a-stick trên R1 |
| `G0/0.10` và `G0/0.30` down/down hoặc administratively down | Interface vật lý `G0/0` chưa bật | Vào `interface g0/0` và nhập `no shutdown` |
| PC vẫn không ping được sau khi cấu hình subinterface | Cổng S1 G0/1 chưa trunk | Cấu hình `switchport mode trunk` trên `G0/1` |
| PC ping gateway không được | Sai IP/default gateway trên PC hoặc sai VLAN trên cổng access | Kiểm tra IP PC và `show vlan brief` |
| Trunk không thấy trong `show interfaces trunk` | Cấu hình nhầm interface hoặc chưa nhập `switchport mode trunk` | Kiểm tra đúng cổng nối router là `G0/1` |
| Packet Tracer chưa lên ping ngay lần đầu | ARP đang học MAC address | Ping lại lần hai hoặc chờ vài giây |

## 10. Kết Quả Cuối

| Hạng mục | Trạng thái |
| --- | --- |
| VLAN 10 được tạo | Hoàn thành |
| VLAN 30 được tạo | Hoàn thành |
| F0/11 gán cho VLAN 10 | Hoàn thành |
| F0/6 gán cho VLAN 30 | Hoàn thành |
| R1 G0/0.10 cấu hình đúng IP và dot1Q VLAN 10 | Hoàn thành |
| R1 G0/0.30 cấu hình đúng IP và dot1Q VLAN 30 | Hoàn thành |
| S1 G0/1 trunk lên R1 | Hoàn thành |
| PC1 ping được PC3 | Hoàn thành |
| Cấu hình đã lưu vào NVRAM | Hoàn thành |

Checklist ảnh minh chứng cần chụp:

- [ ] `topology.png` - sơ đồ lab.
- [ ] `s1-show-vlan-brief.png` - VLAN 10, VLAN 30 và port access.
- [ ] `r1-show-ip-interface-brief.png` - subinterface up/up.
- [ ] `s1-show-interfaces-trunk.png` - trunk G0/1 hoạt động.
- [ ] `pc1-ip-configuration.png` - IP và gateway của PC1.
- [ ] `pc3-ip-configuration.png` - IP và gateway của PC3.
- [ ] `pc1-ping-pc3-success.png` - ping liên VLAN thành công.
- [ ] `check-results.png` - điểm hoàn thành trong Packet Tracer.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 4 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 4.2.7 Packet Tracer - Configure Router-on-a-Stick Inter-VLAN Routing (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-02/">Lab 2: 4.3.8 Packet Tracer - Configure Layer 3 Switching and Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-03/">Lab 3: 4.4.8 Packet Tracer - Troubleshoot Inter-VLAN Routing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/lab-04/">Lab 4: 4.5.1 Packet Tracer - Inter-VLAN Routing Challenge</a></li>
    </ul>
  </details>
</div>

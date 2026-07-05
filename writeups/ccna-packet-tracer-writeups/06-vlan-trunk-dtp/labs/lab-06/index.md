---
layout: page-toc
title: "CCNA 06.06 - 3.6.1 Packet Tracer - Implement VLANs and Trunking"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.6.1 Packet Tracer - Implement VLANs and Trunking.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-06/` |
| Trạng thái | Hoàn thành VLAN, access port, voice VLAN, SVI quản trị, static trunk và dynamic trunk |

> **Ghi chú:** Bài này là bài tổng hợp cuối của phần VLAN/Trunk/DTP. Cần cấu hình đủ VLAN trên cả 3 switch, gán access port cho SWB/SWC, tạo SVI VLAN 99 để quản trị, cấu hình native VLAN 100 cho trunk và kiểm tra kết nối theo từng VLAN.

---

## 1. Mục Tiêu Bài Lab

- Tạo và đặt tên VLAN 10, 20, 30, 40, 99, 100 trên SWA, SWB và SWC
- Gán các cổng access trên SWB và SWC vào đúng VLAN theo Addressing Table
- Cấu hình cổng voice VLAN cho PC7/IP Phone trên SWC
- Cấu hình SVI VLAN 99 cho 3 switch để quản trị
- Cấu hình static trunk giữa SWA và SWB, tắt DTP trên trunk tĩnh
- Cấu hình dynamic trunk giữa SWA và SWC bằng DTP
- Đổi native VLAN của các trunk sang VLAN 100 và xử lý native VLAN mismatch
- Kiểm tra kết nối giữa các thiết bị cùng VLAN và SVI quản trị

![Topology Implement VLANs and Trunking](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/topology.png)

![Instructions Implement VLANs and Trunking](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/instructions.png)

---

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Switchport | VLAN |
| --- | --- | --- | --- | --- | --- |
| PC1 | NIC | 192.168.10.10 | 255.255.255.0 | SWB F0/1 | VLAN 10 |
| PC2 | NIC | 192.168.20.20 | 255.255.255.0 | SWB F0/2 | VLAN 20 |
| PC3 | NIC | 192.168.30.30 | 255.255.255.0 | SWB F0/3 | VLAN 30 |
| PC4 | NIC | 192.168.10.11 | 255.255.255.0 | SWC F0/1 | VLAN 10 |
| PC5 | NIC | 192.168.20.21 | 255.255.255.0 | SWC F0/2 | VLAN 20 |
| PC6 | NIC | 192.168.30.31 | 255.255.255.0 | SWC F0/3 | VLAN 30 |
| PC7 | NIC | 192.168.10.12 | 255.255.255.0 | SWC F0/4 | VLAN 10 + Voice VLAN 40 |
| SWA | SVI VLAN 99 | 192.168.99.252 | 255.255.255.0 | N/A | VLAN 99 |
| SWB | SVI VLAN 99 | 192.168.99.253 | 255.255.255.0 | N/A | VLAN 99 |
| SWC | SVI VLAN 99 | 192.168.99.254 | 255.255.255.0 | N/A | VLAN 99 |

> **Lưu ý:** Bài này không cấu hình router hoặc multilayer switch nên các PC khác VLAN sẽ không ping được nhau. Trunk chỉ giúp cùng một VLAN đi qua nhiều switch, không định tuyến giữa VLAN.

---

## 3. VLAN Table Và Topology Overview

### VLAN Table

| VLAN | Name | Vai trò |
| --- | --- | --- |
| 10 | Admin | User VLAN cho nhóm Admin |
| 20 | Accounts | User VLAN cho nhóm Accounts |
| 30 | HR | User VLAN cho nhóm HR |
| 40 | Voice | Voice VLAN cho IP Phone |
| 99 | Management | VLAN quản trị switch qua SVI |
| 100 | Native | Native VLAN cho trunk |

### Topology Overview

| Khu vực | Thiết bị/Cổng | Nhận xét |
| --- | --- | --- |
| Core/Distribution | SWA | Switch trung tâm, nối xuống SWB và SWC |
| Static trunk | SWA G0/1 ↔ SWB G0/1 | Cấu hình trunk tĩnh, tắt DTP bằng `switchport nonegotiate` |
| Dynamic trunk | SWA G0/2 ↔ SWC G0/2 | SWA dùng `dynamic desirable` để đàm phán trunk với SWC |
| Access VLAN trên SWB | F0/1, F0/2, F0/3 | Lần lượt thuộc VLAN 10, 20, 30 |
| Access VLAN trên SWC | F0/1, F0/2, F0/3, F0/4 | F0/4 vừa dùng data VLAN 10 vừa dùng voice VLAN 40 |
| Management VLAN | VLAN 99 | Dùng để gán IP quản trị cho SWA, SWB, SWC |
| Native VLAN | VLAN 100 | Dùng làm native VLAN trên các trunk để tránh dùng VLAN 1 mặc định |

> **Điểm dễ sai:** VLAN phải tồn tại trên switch thì mới được xem là active trên trunk. Nếu quên tạo VLAN 10/20/30 trên SWA, trunk có thể up nhưng traffic của PC cùng VLAN vẫn không đi qua đầy đủ.

---

## 4. Part 1: Configure VLANs

### Step 1: Tạo VLAN trên SWA

```text
enable
configure terminal

vlan 10
 name Admin
 exit
vlan 20
 name Accounts
 exit
vlan 30
 name HR
 exit
vlan 40
 name Voice
 exit
vlan 99
 name Management
 exit
vlan 100
 name Native
 exit

end
copy running-config startup-config
```

### Step 2: Tạo VLAN trên SWB

```text
enable
configure terminal

vlan 10
 name Admin
 exit
vlan 20
 name Accounts
 exit
vlan 30
 name HR
 exit
vlan 40
 name Voice
 exit
vlan 99
 name Management
 exit
vlan 100
 name Native
 exit

end
copy running-config startup-config
```

### Step 3: Tạo VLAN trên SWC

```text
enable
configure terminal

vlan 10
 name Admin
 exit
vlan 20
 name Accounts
 exit
vlan 30
 name HR
 exit
vlan 40
 name Voice
 exit
vlan 99
 name Management
 exit
vlan 100
 name Native
 exit

end
copy running-config startup-config
```

### Step 4: Kiểm tra VLAN

Trên cả 3 switch:

```text
show vlan brief
```

Kết quả mong muốn:

```text
VLAN Name                             Status
---- -------------------------------- ---------
1    default                          active
10   Admin                            active
20   Accounts                         active
30   HR                               active
40   Voice                            active
99   Management                       active
100  Native                           active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

![Verify VLANs](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/show-vlan-created.png)

---

## 5. Part 2: Assign Ports to VLANs

### Step 1: Gán access port trên SWB

```text
enable
configure terminal

interface fastEthernet0/1
 switchport mode access
 switchport access vlan 10
 exit

interface fastEthernet0/2
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/3
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

### Step 2: Gán access port và voice VLAN trên SWC

```text
enable
configure terminal

interface fastEthernet0/1
 switchport mode access
 switchport access vlan 10
 exit

interface fastEthernet0/2
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/3
 switchport mode access
 switchport access vlan 30
 exit

interface fastEthernet0/4
 switchport mode access
 switchport access vlan 10
 mls qos trust cos
 switchport voice vlan 40
 exit

end
copy running-config startup-config
```

> **Lưu ý:** `switchport access vlan 10` dùng cho data traffic của PC7. `switchport voice vlan 40` dùng cho voice traffic của IP Phone. Lệnh `mls qos trust cos` cho phép switch tin giá trị CoS từ IP Phone để ưu tiên lưu lượng thoại.

### Step 3: Cấu hình SVI VLAN 99 trên SWA

```text
enable
configure terminal

interface vlan 99
 ip address 192.168.99.252 255.255.255.0
 no shutdown
 exit

end
copy running-config startup-config
```

### Step 4: Cấu hình SVI VLAN 99 trên SWB

```text
enable
configure terminal

interface vlan 99
 ip address 192.168.99.253 255.255.255.0
 no shutdown
 exit

end
copy running-config startup-config
```

### Step 5: Cấu hình SVI VLAN 99 trên SWC

```text
enable
configure terminal

interface vlan 99
 ip address 192.168.99.254 255.255.255.0
 no shutdown
 exit

end
copy running-config startup-config
```

> **Lưu ý:** Sau khi mới tạo SVI nhưng chưa cấu hình trunk, các switch chưa ping được nhau qua VLAN 99 vì VLAN 99 chưa được truyền qua liên kết giữa các switch.

### Step 6: Kiểm tra access port và SVI

Trên SWB:

```text
show vlan brief
show ip interface brief
```

Kết quả mong muốn trên SWB:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
10   Admin                            active    Fa0/1
20   Accounts                         active    Fa0/2
30   HR                               active    Fa0/3
99   Management                       active
100  Native                           active

Interface              IP-Address      OK? Method Status                Protocol
Vlan99                 192.168.99.253  YES manual up                    up
```

Trên SWC:

```text
show vlan brief
show ip interface brief
show interfaces fastEthernet0/4 switchport
```

Kết quả mong muốn trên SWC:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
10   Admin                            active    Fa0/1, Fa0/4
20   Accounts                         active    Fa0/2
30   HR                               active    Fa0/3
40   Voice                            active
99   Management                       active
100  Native                           active

Voice VLAN: 40
Access Mode VLAN: 10 (Admin)
```

![Access VLAN and SVI verification](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/access-svi-verification.png)

---

## 6. Part 3: Configure Static Trunking

### Step 1: Cấu hình static trunk trên SWA G0/1

```text
enable
configure terminal

interface gigabitEthernet0/1
 switchport mode trunk
 switchport nonegotiate
 switchport trunk native vlan 100
 exit

end
copy running-config startup-config
```

### Step 2: Cấu hình static trunk trên SWB G0/1

```text
enable
configure terminal

interface gigabitEthernet0/1
 switchport mode trunk
 switchport nonegotiate
 switchport trunk native vlan 100
 exit

end
copy running-config startup-config
```

> **Lưu ý:** Static trunk phải thống nhất ở cả hai đầu. Vì dùng `switchport nonegotiate`, hai đầu trunk không gửi DTP frame nữa, nên không nên để một đầu là `dynamic auto`.

### Step 3: Kiểm tra static trunk

Trên SWA và SWB:

```text
show interfaces trunk
show interfaces gigabitEthernet0/1 switchport
```

Kết quả mong muốn:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      100

Administrative Mode: trunk
Operational Mode: trunk
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 100 (Native)
```

![Static trunk verification](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/static-trunk-verification.png)

---

## 7. Part 4: Configure Dynamic Trunking

### Step 1: Cấu hình SWA G0/2 dùng DTP dynamic desirable

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport mode dynamic desirable
 switchport trunk native vlan 100
 exit

end
copy running-config startup-config
```

> **Lưu ý:** `dynamic desirable` chủ động gửi DTP để đề nghị tạo trunk. Khi đầu còn lại để mặc định `dynamic auto`, trunk vẫn có thể được đàm phán thành công.

### Step 2: Cấu hình native VLAN trên SWC G0/2

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport trunk native vlan 100
 exit

end
copy running-config startup-config
```

> **Lưu ý:** Nếu Packet Tracer yêu cầu cấu hình tĩnh ở đầu SWC, có thể bổ sung `switchport mode trunk` trên `G0/2`. Tuy nhiên theo yêu cầu dynamic trunking, SWA dùng `dynamic desirable` và SWC có thể giữ trạng thái mặc định để DTP thương lượng trunk.

### Step 3: Kiểm tra dynamic trunk

Trên SWA:

```text
show interfaces trunk
show dtp
show interfaces gigabitEthernet0/2 switchport
```

Kết quả mong muốn trên SWA:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      100
Gi0/2       desirable    n-802.1q       trunking      100

Global DTP information
  Sending DTP Hello packets every 30 seconds
  Dynamic Trunk timeout is 300 seconds
  1 interfaces using DTP

Administrative Mode: dynamic desirable
Operational Mode: trunk
Negotiation of Trunking: On
Trunking Native Mode VLAN: 100 (Native)
```

Trên SWC:

```text
show interfaces trunk
show interfaces gigabitEthernet0/2 switchport
```

Kết quả mong muốn trên SWC:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/2       auto         n-802.1q       trunking      100

Administrative Mode: dynamic auto
Operational Mode: trunk
Negotiation of Trunking: On
Trunking Native Mode VLAN: 100 (Native)
```

> Nếu đã cấu hình thêm `switchport mode trunk` trên SWC G0/2, output có thể hiển thị `Mode on`, `Encapsulation 802.1q`, `Negotiation of Trunking: On/Off` tùy phiên bản Packet Tracer.

![Dynamic trunk verification](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/dynamic-trunk-verification.png)

---

## 8. Kiểm Tra Kết Nối

### Step 1: Kiểm tra trunk active VLAN

Trên SWA, SWB và SWC:

```text
show interfaces trunk
```

Kết quả mong muốn:

```text
Port        Vlans allowed on trunk
Gi0/1       1-1005
Gi0/2       1-1005

Port        Vlans allowed and active in management domain
Gi0/1       1,10,20,30,40,99,100
Gi0/2       1,10,20,30,40,99,100

Port        Vlans in spanning tree forwarding state and not pruned
Gi0/1       1,10,20,30,40,99,100
Gi0/2       1,10,20,30,40,99,100
```

> **Lưu ý:** Nếu thiếu VLAN 10/20/30 trên SWA, phần `Vlans allowed and active in management domain` trên trunk có thể không có đủ VLAN user, làm PC cùng VLAN ở hai switch không ping được nhau.

### Step 2: Kiểm tra ping giữa SVI quản trị

Trên SWA:

```text
ping 192.168.99.253     ! SWA → SWB VLAN 99
ping 192.168.99.254     ! SWA → SWC VLAN 99
```

Trên SWB:

```text
ping 192.168.99.252     ! SWB → SWA VLAN 99
ping 192.168.99.254     ! SWB → SWC VLAN 99
```

![SVI management ping](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/svi-management-ping.png)

### Step 3: Kiểm tra ping giữa PC cùng VLAN

```text
PC1> ping 192.168.10.11     ! PC1 → PC4, cùng VLAN 10
PC1> ping 192.168.10.12     ! PC1 → PC7, cùng VLAN 10
PC2> ping 192.168.20.21     ! PC2 → PC5, cùng VLAN 20
PC3> ping 192.168.30.31     ! PC3 → PC6, cùng VLAN 30
```

![Same VLAN PC ping](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/same-vlan-ping.png)

### Step 4: Kiểm tra ping khác VLAN

```text
PC1> ping 192.168.30.31     ! PC1 → PC6, khác VLAN/subnet: fail nếu chưa có inter-VLAN routing
PC3> ping 192.168.10.11     ! PC3 → PC4, khác VLAN/subnet: fail nếu chưa có inter-VLAN routing
```

> **Lưu ý:** Nếu đề yêu cầu kiểm tra `PC1 → PC6` hoặc `PC3 → PC4`, đây là kiểm tra khác VLAN. Trong topology này chưa có router-on-a-stick hoặc multilayer switch định tuyến giữa VLAN, nên kết quả đúng là **không thành công**.

---

## 9. Đáp Án Câu Hỏi Trong Lab

| Câu hỏi | Trả lời |
| --- | --- |
| Vì sao sau khi cấu hình SVI, các switch chưa ping được nhau? | Vì lúc đó trunk giữa các switch chưa được cấu hình, VLAN 99 chưa được truyền qua các uplink. |
| Static trunk giữa SWA và SWB cần cấu hình gì? | Cấu hình `switchport mode trunk`, `switchport nonegotiate`, `switchport trunk native vlan 100` ở cả SWA G0/1 và SWB G0/1. |
| Dynamic trunk giữa SWA và SWC cần cấu hình gì? | SWA G0/2 dùng `switchport mode dynamic desirable`; đầu SWC có thể để `dynamic auto` để DTP thương lượng trunk, đồng thời đặt native VLAN 100. |
| Native VLAN của trunk cần là VLAN nào? | VLAN 100, tên `Native`. |
| Vì sao phải đổi native VLAN ở cả hai đầu trunk? | Nếu chỉ đổi một đầu, switch sẽ báo native VLAN mismatch và có thể gây lỗi truyền untagged frame. |
| Vì sao PC cùng VLAN có thể ping qua switch khác nhau? | Vì trunk mang VLAN tag qua uplink, giúp VLAN 10/20/30 tồn tại xuyên suốt giữa SWB, SWA và SWC. |
| Vì sao PC khác VLAN không ping được nhau? | Vì bài này chưa cấu hình inter-VLAN routing. Switch layer 2 không tự định tuyến giữa các VLAN. |
| Cổng nào dùng voice VLAN? | SWC F0/4, vừa là access VLAN 10 cho PC7 vừa là voice VLAN 40 cho IP Phone. |

---

## 10. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC cùng VLAN không ping được qua switch khác | Uplink chưa trunk hoặc VLAN chưa active trên trunk | Kiểm tra `show interfaces trunk`, tạo đủ VLAN trên SWA/SWB/SWC |
| Switch báo native VLAN mismatch | Hai đầu trunk dùng native VLAN khác nhau | Đặt `switchport trunk native vlan 100` ở cả hai đầu |
| Static trunk không lên | Một đầu trunk, một đầu để dynamic auto và DTP bị tắt | Cấu hình static trunk đồng nhất ở cả hai đầu |
| `Negotiation of Trunking` không đúng | Dùng sai mode trunk/DTP | Kiểm tra bằng `show interfaces switchport` |
| SVI VLAN 99 down | VLAN 99 chưa tồn tại hoặc không có port/trunk active trong VLAN 99 | Tạo VLAN 99, cấu hình trunk, kiểm tra trạng thái link |
| PC7/IP Phone không đúng VLAN | Quên `switchport voice vlan 40` hoặc gán sai access VLAN | Cấu hình lại SWC F0/4: access VLAN 10, voice VLAN 40 |
| PC khác VLAN không ping được | Đây là hành vi đúng khi chưa có inter-VLAN routing | Cần router-on-a-stick hoặc multilayer switch nếu muốn định tuyến giữa VLAN |
| Native VLAN vẫn là 1 | Chỉ đổi VLAN trên một switch hoặc sai interface trunk | Kiểm tra đúng cổng G0/1/G0/2 và đặt native VLAN 100 |

---

## 11. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| VLAN trên SWA/SWB/SWC | Có VLAN 10 Admin, 20 Accounts, 30 HR, 40 Voice, 99 Management, 100 Native |
| SWB F0/1 | Access VLAN 10 |
| SWB F0/2 | Access VLAN 20 |
| SWB F0/3 | Access VLAN 30 |
| SWC F0/1 | Access VLAN 10 |
| SWC F0/2 | Access VLAN 20 |
| SWC F0/3 | Access VLAN 30 |
| SWC F0/4 | Access VLAN 10 + Voice VLAN 40 |
| SWA VLAN 99 | 192.168.99.252/24, up/up |
| SWB VLAN 99 | 192.168.99.253/24, up/up |
| SWC VLAN 99 | 192.168.99.254/24, up/up |
| SWA G0/1 ↔ SWB G0/1 | Static trunk, native VLAN 100, DTP off |
| SWA G0/2 ↔ SWC G0/2 | Dynamic/desirable trunk, native VLAN 100 |
| SWA/SWB/SWC SVI ping | Ping được qua VLAN 99 sau khi trunk hoàn tất |
| PC1 → PC4/PC7 | Thành công, cùng VLAN 10 |
| PC2 → PC5 | Thành công, cùng VLAN 20 |
| PC3 → PC6 | Thành công, cùng VLAN 30 |
| PC1 → PC6 | Không thành công nếu chưa có inter-VLAN routing |
| PC3 → PC4 | Không thành công nếu chưa có inter-VLAN routing |

- [ ] Ảnh `show vlan brief` trên SWA/SWB/SWC
- [ ] Ảnh `show interfaces trunk` trên SWA/SWB/SWC
- [ ] Ảnh `show interfaces g0/1 switchport` hoặc `g0/2 switchport`
- [ ] Ảnh ping giữa các SVI VLAN 99
- [ ] Ảnh ping PC cùng VLAN thành công
- [ ] Ảnh kiểm tra khác VLAN thất bại nếu đề yêu cầu
- [ ] Ảnh Check Results hoàn thành

![Final Check Results](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-06/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 5</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/">Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/">Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/">Lab 3: 3.3.12 Packet Tracer - VLAN Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/">Lab 4: 3.4.5 Packet Tracer - Configure Trunks</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/">Lab 5: 3.5.5 Packet Tracer - Configure DTP</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 06.03 - 3.3.12 Packet Tracer - VLAN Configuration"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.3.12 Packet Tracer - VLAN Configuration.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Hoàn thành tạo VLAN, đặt tên VLAN, gán access port và cấu hình voice VLAN |

> **Ghi chú:** Bài này tập trung vào thao tác VLAN cơ bản trên switch: xem VLAN mặc định, tạo VLAN mới, gán port vào VLAN phù hợp và kiểm tra vì sao PC cùng subnet nhưng khác switch vẫn chưa ping được khi chưa cấu hình trunk.

---

## 1. Mục Tiêu Bài Lab

- Kiểm tra trạng thái VLAN mặc định trên switch bằng `show vlan brief`
- Tạo và đặt tên các VLAN 10, 20, 30, 99 và 150 trên S1, S2, S3
- Gán các cổng access trên S2 và S3 vào đúng VLAN
- Cấu hình VLAN thoại cho cổng kết nối IP Phone trên S3
- Kiểm tra lại kết nối giữa các PC cùng mạng sau khi gán VLAN
- Giải thích nguyên nhân mất kết nối khi các liên kết giữa switch chưa được cấu hình trunk

![Topology VLAN Configuration](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/topology.png)

![Instructions VLAN Configuration](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/instructions.png)

---

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | VLAN |
| --- | --- | --- | --- | --- |
| PC1 | NIC | 172.17.10.21 | 255.255.255.0 | 10 |
| PC2 | NIC | 172.17.20.22 | 255.255.255.0 | 20 |
| PC3 | NIC | 172.17.30.23 | 255.255.255.0 | 30 |
| PC4 | NIC | 172.17.10.24 | 255.255.255.0 | 10 |
| PC5 | NIC | 172.17.20.25 | 255.255.255.0 | 20 |
| PC6 | NIC | 172.17.30.26 | 255.255.255.0 | 30 |

> **Lưu ý:** Các PC cùng subnet phải nằm cùng VLAN thì mới giao tiếp Layer 2 được. Nếu cùng subnet nhưng đường đi giữa các switch chưa mang VLAN đó qua trunk, ping vẫn thất bại.

---

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| VLAN 10 | PC1, PC4 | Nhóm Faculty/Staff, dùng mạng 172.17.10.0/24 |
| VLAN 20 | PC2, PC5 | Nhóm Students, dùng mạng 172.17.20.0/24 |
| VLAN 30 | PC3, PC6 | Nhóm Guest(Default), dùng mạng 172.17.30.0/24 |
| VLAN 99 | Management&Native | VLAN quản trị/native, được tạo nhưng chưa gán access port trong bài này |
| VLAN 150 | VOICE | VLAN thoại, dùng cho IP Phone trên S3 F0/11 |
| S2 access ports | F0/11, F0/18, F0/6 | Lần lượt gán vào VLAN 10, VLAN 20, VLAN 30 |
| S3 access ports | F0/11, F0/18, F0/6 | Lần lượt gán vào VLAN 10, VLAN 20, VLAN 30 |
| Inter-switch links | Gig0/1, Gig0/2 hoặc cổng uplink liên quan | Ban đầu vẫn nằm trong VLAN 1, chưa phải trunk |

> **Điểm dễ sai:** Tạo VLAN giống nhau trên nhiều switch chưa đủ để PC khác switch giao tiếp. Các liên kết giữa switch phải được cấu hình trunk để mang VLAN 10/20/30 đi qua.

---

## 4. Part 1: Verify the Default VLAN Configuration

### Step 1: Hiển thị VLAN hiện tại trên S1

```text
S1> enable
S1# show vlan brief
```

Kết quả ban đầu cần thấy:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                Gig0/1, Gig0/2
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

![S1 default VLAN brief](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/s1-default-vlan-brief.png)

> **Lưu ý:** Mặc định tất cả port trên switch đều thuộc VLAN 1. Các VLAN 1002–1005 là VLAN mặc định dùng cho FDDI/Token Ring, không cần cấu hình trong bài này.

### Step 2: Kiểm tra kết nối ban đầu giữa các PC cùng subnet

```text
! PC1 -> PC4, cùng mạng 172.17.10.0/24
ping 172.17.10.24

! PC2 -> PC5, cùng mạng 172.17.20.0/24
ping 172.17.20.25

! PC3 -> PC6, cùng mạng 172.17.30.0/24
ping 172.17.30.26
```

![Initial ping same subnet](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/initial-ping-same-subnet.png)

| Câu hỏi | Trả lời |
| --- | --- |
| What benefits can VLANs provide to the network? | VLAN giúp chia mạng thành các nhóm logic, giảm broadcast, tăng bảo mật, dễ quản trị người dùng theo phòng ban và hỗ trợ di chuyển/thay đổi thiết bị linh hoạt hơn. |

---

## 5. Part 2: Configure VLANs

### Step 1: Tạo và đặt tên VLAN trên S1

```text
S1> enable
S1# configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

end
copy running-config startup-config
```

> **Lưu ý:** Tên VLAN có phân biệt chữ hoa/chữ thường trong yêu cầu bài. Nên nhập đúng `Faculty/Staff`, `Students`, `Guest(Default)`, `Management&Native`, `VOICE`.

### Step 2: Kiểm tra VLAN trên S1

```text
S1# show vlan brief
```

Kết quả cần có:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                Gig0/1, Gig0/2
10   Faculty/Staff                    active
20   Students                         active
30   Guest(Default)                   active
99   Management&Native                active
150  VOICE                            active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

![S1 VLAN created](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/s1-vlan-created.png)

| Câu hỏi | Trả lời |
| --- | --- |
| Which command will only display the VLAN name, status, and associated ports on a switch? | `show vlan brief` |

### Step 3: Tạo và đặt tên VLAN trên S2

```text
S2> enable
S2# configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

end
copy running-config startup-config
```

### Step 4: Tạo và đặt tên VLAN trên S3

```text
S3> enable
S3# configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

end
copy running-config startup-config
```

### Step 5: Kiểm tra VLAN trên S2 và S3

```text
S2# show vlan brief
S3# show vlan brief
```

![S2 S3 VLAN created](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/s2-s3-vlan-created.png)

---

## 6. Part 3: Assign VLANs to Ports

### Step 1: Gán VLAN cho active ports trên S2

```text
S2> enable
S2# configure terminal

interface fastEthernet0/11
 switchport mode access
 switchport access vlan 10
 exit

interface fastEthernet0/18
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/6
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

| Port S2 | Mode | VLAN | Nhóm |
| --- | --- | --- | --- |
| F0/11 | Access | 10 | Faculty/Staff |
| F0/18 | Access | 20 | Students |
| F0/6 | Access | 30 | Guest(Default) |

### Step 2: Gán VLAN cho active ports trên S3

```text
S3> enable
S3# configure terminal

interface fastEthernet0/11
 switchport mode access
 switchport access vlan 10
 exit

interface fastEthernet0/18
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/6
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

| Port S3 | Mode | VLAN | Nhóm |
| --- | --- | --- | --- |
| F0/11 | Access | 10 | Faculty/Staff / PC4 |
| F0/18 | Access | 20 | Students / PC5 |
| F0/6 | Access | 30 | Guest(Default) / PC6 |

### Step 3: Gán VOICE VLAN cho F0/11 trên S3

```text
S3> enable
S3# configure terminal

interface fastEthernet0/11
 mls qos trust cos
 switchport voice vlan 150
 exit

end
copy running-config startup-config
```

> **Lưu ý:** S3 F0/11 vừa mang dữ liệu của PC4 ở VLAN 10, vừa mang voice traffic của IP Phone ở VLAN 150. Lệnh `mls qos trust cos` cho switch tin giá trị CoS do IP Phone đánh dấu để ưu tiên lưu lượng thoại.

### Step 4: Kiểm tra VLAN sau khi gán port

```text
S2# show vlan brief
```

Kết quả trên S2 cần thấy:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/12, Fa0/13, Fa0/14
                                                Fa0/15, Fa0/16, Fa0/17, Fa0/19
                                                Fa0/20, Fa0/21, Fa0/22, Fa0/23
                                                Fa0/24, Gig0/1, Gig0/2
10   Faculty/Staff                    active    Fa0/11
20   Students                         active    Fa0/18
30   Guest(Default)                   active    Fa0/6
99   Management&Native                active
150  VOICE                            active
```

```text
S3# show vlan brief
```

Kết quả trên S3 cần thấy:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/12, Fa0/13, Fa0/14
                                                Fa0/15, Fa0/16, Fa0/17, Fa0/19
                                                Fa0/20, Fa0/21, Fa0/22, Fa0/23
                                                Fa0/24, Gig0/1, Gig0/2
10   Faculty/Staff                    active    Fa0/11
20   Students                         active    Fa0/18
30   Guest(Default)                   active    Fa0/6
99   Management&Native                active
150  VOICE                            active
```

![Show VLAN brief S2 S3 after access assignment](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/show-vlan-brief-s2-s3-after-access.png)

> **Điểm cần chú ý:** Trong output của S2, `Gig0/1` vẫn nằm ở VLAN 1. Đây là lý do quan trọng làm PC ở VLAN 10 trên switch khác nhau chưa giao tiếp được.

### Step 5: Kiểm tra ping giữa PC1 và PC4

```text
! PC1 -> PC4
ping 172.17.10.24
```

![Ping PC1 to PC4 failed before trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/ping-pc1-pc4-failed-before-trunk.png)

| Câu hỏi | Trả lời |
| --- | --- |
| Although the access ports are assigned to the appropriate VLANs, were the pings successful? Explain. | Không. Ping PC1 → PC4 thất bại vì access port của PC1 và PC4 đã thuộc VLAN 10, nhưng liên kết giữa các switch vẫn đang ở VLAN 1 và chưa được cấu hình trunk để mang VLAN 10 đi qua. |
| What could be done to resolve this issue? | Cấu hình các liên kết giữa switch thành trunk port và cho phép VLAN 10, 20, 30, 99, 150 đi qua trunk. |

---

## 7. Cấu Hình Tổng Hợp

### S1

```text
enable
configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

end
copy running-config startup-config
```

### S2

```text
enable
configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

interface fastEthernet0/11
 switchport mode access
 switchport access vlan 10
 exit

interface fastEthernet0/18
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/6
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

### S3

```text
enable
configure terminal

vlan 10
 name Faculty/Staff
 exit

vlan 20
 name Students
 exit

vlan 30
 name Guest(Default)
 exit

vlan 99
 name Management&Native
 exit

vlan 150
 name VOICE
 exit

interface fastEthernet0/11
 switchport mode access
 switchport access vlan 10
 mls qos trust cos
 switchport voice vlan 150
 exit

interface fastEthernet0/18
 switchport mode access
 switchport access vlan 20
 exit

interface fastEthernet0/6
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

---

## 8. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Tên VLAN không đúng yêu cầu | Gõ sai chữ hoa/thường hoặc thiếu ký tự `/`, `&`, `()` | Xóa/sửa lại tên bằng `vlan <id>` rồi `name <đúng tên>` |
| Port không xuất hiện trong VLAN mong muốn | Chưa gán `switchport access vlan` hoặc gán nhầm port | Dùng `show vlan brief`, vào đúng interface và gán lại VLAN |
| PC1 không ping được PC4 sau khi gán VLAN | Uplink giữa switch chưa cấu hình trunk nên VLAN 10 không đi qua | Cấu hình trunk ở bài tiếp theo hoặc trên các uplink liên quan |
| IP Phone không nhận voice VLAN | Thiếu `switchport voice vlan 150` trên S3 F0/11 | Cấu hình lại S3 F0/11 với access VLAN 10 và voice VLAN 150 |
| Lệnh QoS không chạy | Gõ sai interface hoặc model Packet Tracer chưa hỗ trợ đầy đủ | Kiểm tra đúng switch/interface; trong bài này dùng đúng `mls qos trust cos` trên S3 F0/11 |
| Ping khác VLAN thất bại | Chưa có thiết bị định tuyến inter-VLAN | Đây là hành vi đúng nếu không có router/L3 switch định tuyến giữa VLAN |

---

## 9. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| S1 VLAN database | Có VLAN 10, 20, 30, 99, 150 với đúng tên |
| S2 VLAN database | Có VLAN 10, 20, 30, 99, 150 với đúng tên |
| S3 VLAN database | Có VLAN 10, 20, 30, 99, 150 với đúng tên |
| S2 F0/11 | Access VLAN 10 |
| S2 F0/18 | Access VLAN 20 |
| S2 F0/6 | Access VLAN 30 |
| S3 F0/11 | Access VLAN 10 và Voice VLAN 150 |
| S3 F0/18 | Access VLAN 20 |
| S3 F0/6 | Access VLAN 30 |
| `show vlan brief` | Hiển thị đúng VLAN name, status và port liên quan |
| PC1 → PC4 | Ping thất bại sau khi gán VLAN vì uplink chưa trunk |
| Cách khắc phục | Cấu hình trunk giữa các switch để mang VLAN qua uplink |

- [ ] Ảnh topology
- [ ] Ảnh instructions
- [ ] Ảnh `show vlan brief` mặc định trên S1
- [ ] Ảnh VLAN đã tạo trên S1/S2/S3
- [ ] Ảnh port đã gán VLAN trên S2/S3
- [ ] Ảnh ping PC1 → PC4 thất bại trước khi cấu hình trunk
- [ ] Ảnh Check Results hoàn thành

![Final result VLAN Configuration](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-03/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/">Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/">Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 3.3.12 Packet Tracer - VLAN Configuration (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/">Lab 4: 3.4.5 Packet Tracer - Configure Trunks</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/">Lab 5: 3.5.5 Packet Tracer - Configure DTP</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/">Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking</a></li>
    </ul>
  </details>
</div>

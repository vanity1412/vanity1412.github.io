---
layout: page-toc
title: "CCNA 06.05 - 3.5.5 Packet Tracer - Configure DTP"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.5.5 Packet Tracer - Configure DTP.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Hoàn thành tạo VLAN, gán access port, cấu hình trunk, kiểm tra DTP và ping cùng VLAN thành công |

> **Ghi chú:** Bài này tập trung vào cách trunk được hình thành bằng **DTP** và cách cấu hình **static trunk**. Điểm dễ sai nhất là chỉ tạo VLAN 10/20/30 trên S2, S3 nhưng quên tạo trên S1, làm trunk không chuyển được VLAN người dùng qua switch trung tâm.

---

## 1. Mục Tiêu Bài Lab

- Kiểm tra VLAN mặc định đang có trên S1, S2, S3
- Tạo thêm VLAN 10, VLAN 20, VLAN 30 trên S2 và S3
- Gán các dải port access vào đúng VLAN
- Cấu hình trunk bằng DTP giữa S1 và S2
- Cấu hình static trunk giữa S1 và S3
- Đổi native VLAN của trunk sang VLAN 999
- Sửa lỗi VLAN chưa active trên S1
- Kiểm tra kết nối end-to-end giữa các PC cùng VLAN

![Topology Configure DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/topology.png)

![Instructions Configure DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/instructions.png)

---

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask |
| --- | --- | --- | --- |
| PC1 | NIC | 192.168.10.1 | 255.255.255.0 |
| PC2 | NIC | 192.168.20.1 | 255.255.255.0 |
| PC3 | NIC | 192.168.30.1 | 255.255.255.0 |
| PC4 | NIC | 192.168.30.2 | 255.255.255.0 |
| PC5 | NIC | 192.168.20.2 | 255.255.255.0 |
| PC6 | NIC | 192.168.10.2 | 255.255.255.0 |
| S1 | VLAN 99 | 192.168.99.1 | 255.255.255.0 |
| S2 | VLAN 99 | 192.168.99.2 | 255.255.255.0 |
| S3 | VLAN 99 | 192.168.99.3 | 255.255.255.0 |

> **Lưu ý:** Các PC không cấu hình default gateway trong bài này vì chỉ kiểm tra kết nối **cùng subnet, cùng VLAN**. Bài chưa yêu cầu định tuyến liên VLAN.

---

## 3. Topology Overview

| Thành phần | Thiết bị / cổng | Nhận xét |
| --- | --- | --- |
| Switch trung tâm | S1 | Nối xuống S2 qua G0/1, nối xuống S3 qua G0/2 |
| Nhánh trái | S2 | Chứa PC1, PC2, PC3 theo VLAN 10/20/30 |
| Nhánh phải | S3 | Chứa PC6, PC5, PC4 theo VLAN 10/20/30 |
| Management VLAN | VLAN 99 | Dùng cho SVI quản trị của S1, S2, S3 |
| Native VLAN | VLAN 999 | Dùng làm native VLAN cho các trunk |
| User VLAN | VLAN 10, 20, 30 | Cần tồn tại trên các switch đi qua trunk |

| VLAN | Name | Network | Port assignment |
| --- | --- | --- | --- |
| 10 | Red | 192.168.10.0/24 | S2 F0/1-8, S3 F0/1-8 |
| 20 | Blue | 192.168.20.0/24 | S2 F0/9-16, S3 F0/9-16 |
| 30 | Yellow | 192.168.30.0/24 | S2 F0/17-24, S3 F0/17-24 |
| 99 | Management | 192.168.99.0/24 | SVI quản trị |
| 999 | Native | Không gán PC | Native VLAN cho trunk |

> **Lưu ý:** VLAN 10/20/30 phải được tạo trên **S1, S2, S3**. Nếu S1 chưa có các VLAN này, trunk vẫn lên nhưng danh sách `Vlans allowed and active in management domain` trên S1 sẽ không có VLAN 10/20/30.

---

## 4. Part 1: Verify VLAN Configuration

### Step 1: Kiểm tra VLAN hiện có trên S1, S2, S3

```text
enable
show vlan brief
```

Kết quả ban đầu trên các switch có các VLAN sau:

| VLAN | Name | Trạng thái |
| --- | --- | --- |
| 1 | default | active |
| 99 | Management | active |
| 999 | Native | active |
| 1002 | fddi-default | active |
| 1003 | token-ring-default | active |
| 1004 | fddinet-default | active |
| 1005 | trnet-default | active |

**Question: What VLANs are configured on the switches?**

| Câu trả lời | Giải thích |
| --- | --- |
| VLAN 99 và VLAN 999 đã được cấu hình thêm trên các switch. Ngoài ra vẫn có VLAN mặc định 1 và các VLAN legacy 1002-1005. | VLAN 1 và VLAN 1002-1005 là VLAN mặc định của switch Cisco. VLAN 99 và VLAN 999 là VLAN được chuẩn bị sẵn cho bài lab. |

![Show VLAN brief initial](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/show-vlan-initial.png)

---

## 5. Part 2: Create Additional VLANs on S2 and S3

### Step 1: Tạo VLAN 10, 20, 30 trên S2

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

end
copy running-config startup-config
```

---

### Step 2: Tạo VLAN 10, 20, 30 trên S3

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

end
copy running-config startup-config
```

---

### Step 3: Kiểm tra VLAN trên S2 và S3

```text
show vlan brief
```

Kết quả cần có trên S2 và S3:

```text
VLAN Name                             Status
---- -------------------------------- ---------
1    default                          active
10   Red                              active
20   Blue                             active
30   Yellow                           active
99   Management                       active
999  Native                           active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

**Question: In addition to the default VLANs, which VLANs are configured on S2?**

| Câu trả lời |
| --- |
| VLAN 10 `Red`, VLAN 20 `Blue`, VLAN 30 `Yellow`, VLAN 99 `Management`, VLAN 999 `Native`. |

![Show VLAN S2 S3 after creating VLANs](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/show-vlan-s2-s3.png)

---

## 6. Part 3: Assign VLANs to Ports

### Step 1: Gán access port trên S2

```text
enable
configure terminal

interface range fastEthernet0/1 - 8
 switchport mode access
 switchport access vlan 10
 exit

interface range fastEthernet0/9 - 16
 switchport mode access
 switchport access vlan 20
 exit

interface range fastEthernet0/17 - 24
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

---

### Step 2: Gán access port trên S3

```text
enable
configure terminal

interface range fastEthernet0/1 - 8
 switchport mode access
 switchport access vlan 10
 exit

interface range fastEthernet0/9 - 16
 switchport mode access
 switchport access vlan 20
 exit

interface range fastEthernet0/17 - 24
 switchport mode access
 switchport access vlan 30
 exit

end
copy running-config startup-config
```

---

### Step 3: Kiểm tra port đã vào đúng VLAN

```text
show vlan brief
```

| Switch | VLAN | Port cần nằm trong VLAN |
| --- | --- | --- |
| S2 | 10 | Fa0/1 - Fa0/8 |
| S2 | 20 | Fa0/9 - Fa0/16 |
| S2 | 30 | Fa0/17 - Fa0/24 |
| S3 | 10 | Fa0/1 - Fa0/8 |
| S3 | 20 | Fa0/9 - Fa0/16 |
| S3 | 30 | Fa0/17 - Fa0/24 |

![Access ports assigned to VLANs](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/access-port-vlan.png)

---

### Step 4: Kiểm tra ping PC1 đến PC6

```text
PC1> ping 192.168.10.2
```

**Question: Was the ping successful? Explain.**

| Kết quả | Giải thích |
| --- | --- |
| Không thành công | PC1 và PC6 cùng VLAN 10 nhưng nằm ở hai switch khác nhau. Các link giữa switch hiện chưa trunk đúng cách nên traffic VLAN 10 chưa đi được qua S1. |

> **Lưu ý:** Gán đúng access port chỉ xử lý được đoạn PC → switch. Muốn cùng VLAN liên lạc qua nhiều switch, các uplink giữa switch phải là trunk và VLAN đó phải active trên các switch trung gian.

![Ping PC1 to PC6 failed before trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/ping-pc1-pc6-fail-before-trunk.png)

---

## 7. Part 4: Configure Trunks on S1, S2, and S3

### Step 1: Cấu hình DTP dynamic desirable trên S1 G0/1

```text
enable
configure terminal

interface gigabitEthernet0/1
 switchport mode dynamic desirable
 exit

end
copy running-config startup-config
```

**Question: What will be the result of trunk negotiation between S1 and S2?**

| Câu trả lời | Giải thích |
| --- | --- |
| Trunk sẽ được hình thành giữa S1 G0/1 và S2 G0/1. | S1 ở chế độ `dynamic desirable`, S2 mặc định là `dynamic auto`, nên hai bên có thể thương lượng trunk bằng DTP. |

---

### Step 2: Kiểm tra trunk trên S2

```text
show interfaces trunk
```

Kết quả cần chú ý trên S2:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      auto         n-802.1q       trunking      1
```

**Question: What is the mode and status for this port?**

| Interface | Mode | Status |
| --- | --- | --- |
| S2 G0/1 | auto | trunking |

![S2 show interfaces trunk dynamic auto](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/s2-show-trunk-auto.png)

---

### Step 3: Cấu hình static trunk trên S1 G0/2 và tắt DTP

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport mode trunk
 switchport nonegotiate
 exit

end
copy running-config startup-config
```

> **Lưu ý:** `switchport nonegotiate` dùng để tắt gửi DTP. Khi một đầu tắt DTP, đầu còn lại nên được cấu hình static trunk để tránh lỗi negotiation.

---

### Step 4: Kiểm tra DTP trên S1

```text
show dtp
```

Kết quả mong muốn:

```text
Global DTP information
    Sending DTP Hello packets every 30 seconds
    Dynamic Trunk timeout is 300 seconds
    1 interfaces using DTP
```

| Ý nghĩa | Nhận xét |
| --- | --- |
| `1 interfaces using DTP` | Chỉ còn S1 G0/1 dùng DTP. S1 G0/2 đã tắt DTP bằng `switchport nonegotiate`. |

![S1 show DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/s1-show-dtp.png)

---

### Step 5: Kiểm tra trunk hiện tại trên S1

```text
show interfaces trunk
```

Kết quả trước khi đổi native VLAN:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      desirable    n-802.1q       trunking      1
Gig0/2      on           802.1q         trunking      1
```

**Question: What is the native VLAN for these trunks currently?**

| Câu trả lời |
| --- |
| Native VLAN hiện tại là VLAN 1. |

---

### Step 6: Đổi native VLAN trên S1 sang VLAN 999

```text
enable
configure terminal

interface range gigabitEthernet0/1 - 2
 switchport trunk native vlan 999
 exit

end
copy running-config startup-config
```

**Question: What messages did you receive on S1? How would you correct it?**

| Nội dung | Giải thích |
| --- | --- |
| S1 báo `%CDP-4-NATIVE_VLAN_MISMATCH` | S1 đã dùng native VLAN 999 nhưng S2/S3 vẫn đang dùng native VLAN 1. |
| Cách sửa | Cấu hình native VLAN 999 trên trunk port tương ứng của S2 và S3. |

Ví dụ thông báo có thể thấy:

```text
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (999), with S2 GigabitEthernet0/1 (1).

%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/2 (999), with S3 GigabitEthernet0/2 (1).
```

![Native VLAN mismatch message](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/native-vlan-mismatch.png)

---

### Step 7: Cấu hình native VLAN 999 trên S2 và S3

Trên S2:

```text
enable
configure terminal

interface gigabitEthernet0/1
 switchport mode dynamic auto
 switchport trunk native vlan 999
 exit

end
copy running-config startup-config
```

Trên S3:

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport mode trunk
 switchport trunk native vlan 999
 exit

end
copy running-config startup-config
```

> **Lưu ý:** S2 G0/1 vẫn có thể để `dynamic auto` để minh họa DTP với S1 G0/1. S3 G0/2 nên cấu hình static trunk vì S1 G0/2 đã là static trunk và đã tắt DTP.

---

### Step 8: Kiểm tra trunk và ping giữa các SVI VLAN 99

```text
show interfaces trunk
```

Sau khi sửa native VLAN, trunk cần hiển thị native VLAN 999:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      desirable    n-802.1q       trunking      999
Gig0/2      on           802.1q         trunking      999
```

Kiểm tra SVI VLAN 99:

```text
S1# ping 192.168.99.2
S1# ping 192.168.99.3
```

![Ping SVI VLAN 99](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/ping-svi-vlan99.png)

---

### Step 9: Kiểm tra lại ping PC1 đến PC6 và sửa VLAN thiếu trên S1

```text
PC1> ping 192.168.10.2
```

**Question: Why was the ping unsuccessful?**

| Nguyên nhân | Cách nhận biết |
| --- | --- |
| S1 chưa có VLAN 10, VLAN 20, VLAN 30 | `show vlan brief` trên S1 chỉ có VLAN 1, 99, 999 và 1002-1005. |
| VLAN 10 chưa active trong trunk qua S1 | `show interfaces trunk` trên S1 chỉ hiển thị `1,99,999` ở phần `Vlans allowed and active in management domain`. |

Cấu hình sửa trên S1:

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

end
copy running-config startup-config
```

Kiểm tra lại trunk trên S1:

```text
show interfaces trunk
```

Kết quả cần có:

```text
Port        Vlans allowed and active in management domain
Gig0/1      1,10,20,30,99,999
Gig0/2      1,10,20,30,99,999
```

![S1 VLANs active on trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/s1-vlans-active-trunk.png)

---

## 8. Part 5: Reconfigure Trunk on S3

### Step 1: Kiểm tra trunk trên S3

```text
show interfaces trunk
```

**Question: What is the mode and encapsulation on G0/2?**

| Interface | Mode | Encapsulation |
| --- | --- | --- |
| S3 G0/2 | on | 802.1q |

---

### Step 2: Cấu hình S3 G0/2 khớp với S1 G0/2

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport nonegotiate
 exit

end
copy running-config startup-config
```

**Question: What is the mode and encapsulation on G0/2 after the change?**

| Interface | Mode | Encapsulation |
| --- | --- | --- |
| S3 G0/2 | on | 802.1q |

> **Lưu ý:** Mode và encapsulation không đổi. Lệnh `switchport nonegotiate` chỉ làm trạng thái negotiation chuyển sang `Off`.

---

### Step 3: Kiểm tra trạng thái negotiation của S3 G0/2

```text
show interfaces gigabitEthernet0/2 switchport
```

Kết quả cần chú ý:

```text
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Trunking Native Mode VLAN: 999 (Native)
```

**Question: What is the ‘Negotiation of Trunking’ state displayed?**

| Câu trả lời |
| --- |
| `Off` |

![S3 show interface G0-2 switchport](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/s3-g02-switchport.png)

---

## 9. Part 6: Verify End-to-End Connectivity

### Step 1: Ping giữa các PC cùng VLAN

```text
PC1> ping 192.168.10.2
! PC1 VLAN 10 → PC6 VLAN 10

PC2> ping 192.168.20.2
! PC2 VLAN 20 → PC5 VLAN 20

PC3> ping 192.168.30.2
! PC3 VLAN 30 → PC4 VLAN 30
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC1 → PC6 | Success |
| PC2 → PC5 | Success |
| PC3 → PC4 | Success |
| S1 → S2 VLAN 99 | Success |
| S1 → S3 VLAN 99 | Success |

![Final ping PC1 PC6](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/ping-pc1-pc6-success.png)

![Final ping PC2 PC5](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/ping-pc2-pc5-success.png)

![Final ping PC3 PC4](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/ping-pc3-pc4-success.png)

---

## 10. Cấu Hình Hoàn Chỉnh

### S1

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

interface gigabitEthernet0/1
 switchport mode dynamic desirable
 switchport trunk native vlan 999
 exit

interface gigabitEthernet0/2
 switchport mode trunk
 switchport trunk native vlan 999
 switchport nonegotiate
 exit

end
copy running-config startup-config
```

---

### S2

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

interface range fastEthernet0/1 - 8
 switchport mode access
 switchport access vlan 10
 exit

interface range fastEthernet0/9 - 16
 switchport mode access
 switchport access vlan 20
 exit

interface range fastEthernet0/17 - 24
 switchport mode access
 switchport access vlan 30
 exit

interface gigabitEthernet0/1
 switchport mode dynamic auto
 switchport trunk native vlan 999
 exit

end
copy running-config startup-config
```

---

### S3

```text
enable
configure terminal

vlan 10
 name Red
 exit

vlan 20
 name Blue
 exit

vlan 30
 name Yellow
 exit

interface range fastEthernet0/1 - 8
 switchport mode access
 switchport access vlan 10
 exit

interface range fastEthernet0/9 - 16
 switchport mode access
 switchport access vlan 20
 exit

interface range fastEthernet0/17 - 24
 switchport mode access
 switchport access vlan 30
 exit

interface gigabitEthernet0/2
 switchport mode trunk
 switchport trunk native vlan 999
 switchport nonegotiate
 exit

end
copy running-config startup-config
```

---

## 11. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC1 không ping được PC6 | Chưa có trunk giữa các switch | Kiểm tra `show interfaces trunk` trên S1, S2, S3 |
| Trunk lên nhưng PC cùng VLAN vẫn không ping được | S1 chưa có VLAN 10/20/30 | Tạo VLAN 10, 20, 30 trên S1 |
| Có thông báo native VLAN mismatch | Hai đầu trunk dùng native VLAN khác nhau | Cấu hình `switchport trunk native vlan 999` ở cả hai đầu trunk |
| S3 G0/2 không giống S1 G0/2 | Chưa tắt DTP trên S3 | Thêm `switchport nonegotiate` trên S3 G0/2 |
| `show dtp` trên S1 có nhiều hơn 1 interface dùng DTP | Chưa tắt DTP trên static trunk | Kiểm tra lại `switchport nonegotiate` trên G0/2 |
| Gán port xong nhưng VLAN không tồn tại | Chưa tạo VLAN trước khi gán access port | Tạo VLAN bằng `vlan <id>` rồi kiểm tra `show vlan brief` |
| Nhầm PC cùng VLAN | PC1 cùng VLAN với PC6, PC2 cùng VLAN với PC5, PC3 cùng VLAN với PC4 | Đối chiếu lại bảng địa chỉ và VLAN |

---

## 12. Kết Quả Cuối

| Hạng mục | Kết quả đúng |
| --- | --- |
| S1 có VLAN 10, 20, 30, 99, 999 | Đạt |
| S2 có VLAN 10, 20, 30, 99, 999 | Đạt |
| S3 có VLAN 10, 20, 30, 99, 999 | Đạt |
| S2 F0/1-8 | VLAN 10 |
| S2 F0/9-16 | VLAN 20 |
| S2 F0/17-24 | VLAN 30 |
| S3 F0/1-8 | VLAN 10 |
| S3 F0/9-16 | VLAN 20 |
| S3 F0/17-24 | VLAN 30 |
| S1 G0/1 | Dynamic desirable, trunking, native VLAN 999 |
| S2 G0/1 | Dynamic auto, trunking, native VLAN 999 |
| S1 G0/2 | Static trunk, nonegotiate, native VLAN 999 |
| S3 G0/2 | Static trunk, nonegotiate, native VLAN 999 |
| PC1 → PC6 | Ping thành công |
| PC2 → PC5 | Ping thành công |
| PC3 → PC4 | Ping thành công |

- [ ] Ảnh topology
- [ ] Ảnh `show vlan brief` ban đầu
- [ ] Ảnh VLAN 10/20/30 trên S2 và S3
- [ ] Ảnh access port đã gán VLAN
- [ ] Ảnh ping fail trước khi trunk
- [ ] Ảnh `show interfaces trunk`
- [ ] Ảnh native VLAN mismatch
- [ ] Ảnh S1 có VLAN 10/20/30 active trên trunk
- [ ] Ảnh `show interfaces g0/2 switchport` trên S3
- [ ] Ảnh ping thành công cuối bài

![Final result Configure DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-05/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 6 →</a></div>
  </div>

  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/">Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/">Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/">Lab 3: 3.3.12 Packet Tracer - VLAN Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/">Lab 4: 3.4.5 Packet Tracer - Configure Trunks</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 3.5.5 Packet Tracer - Configure DTP (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/">Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking</a></li>
    </ul>
  </details>
</div>

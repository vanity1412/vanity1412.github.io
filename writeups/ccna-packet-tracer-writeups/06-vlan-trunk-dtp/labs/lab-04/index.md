---
layout: page-toc
title: "CCNA 06.04 - 3.4.5 Packet Tracer - Configure Trunks"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.4.5 Packet Tracer - Configure Trunks.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Hoàn thành trunk giữa S1-S2-S3, sửa native VLAN mismatch và kiểm tra kết nối cùng VLAN |

> **Ghi chú:** Các VLAN và access port đã được cấu hình từ lab trước. Nhiệm vụ chính của bài này là kiểm tra VLAN hiện có, cấu hình trunk trên uplink giữa các switch và đổi native VLAN từ VLAN 1 sang VLAN 99.

---

## 1. Mục Tiêu Bài Lab

- Kiểm tra VLAN đang tồn tại trên S1, S2 và S3
- Xác nhận lỗi mất kết nối giữa các PC cùng VLAN nhưng nằm trên switch khác nhau
- Cấu hình trunk trên các cổng uplink giữa S1, S2 và S3
- Cấu hình VLAN 99 làm native VLAN trên trunk
- Kiểm tra lại trunk, native VLAN và kết nối giữa các PC cùng VLAN

![Topology Configure Trunks](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/topology.png)

![Instructions Configure Trunks](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/instructions.png)

---

## 2. Bảng Địa Chỉ Và VLAN

| Device | Interface | IP Address | Subnet Mask | Switch Port | VLAN |
| --- | --- | --- | --- | --- | --- |
| PC1 | NIC | 172.17.10.21 | 255.255.255.0 | S2 F0/11 | 10 |
| PC2 | NIC | 172.17.20.22 | 255.255.255.0 | S2 F0/18 | 20 |
| PC3 | NIC | 172.17.30.23 | 255.255.255.0 | S2 F0/6 | 30 |
| PC4 | NIC | 172.17.10.24 | 255.255.255.0 | S3 F0/11 | 10 |
| PC5 | NIC | 172.17.20.25 | 255.255.255.0 | S3 F0/18 | 20 |
| PC6 | NIC | 172.17.30.26 | 255.255.255.0 | S3 F0/6 | 30 |

> **Lưu ý:** PC1 và PC4 cùng VLAN 10, PC2 và PC5 cùng VLAN 20, PC3 và PC6 cùng VLAN 30. Muốn các PC cùng VLAN nhưng nằm trên switch khác nhau ping được nhau thì đường nối giữa các switch phải là trunk.

---

## 3. Topology Overview

| Thành phần | Thiết bị / Cổng | Nhận xét |
| --- | --- | --- |
| Switch trung tâm | S1 G0/1, S1 G0/2 | Hai cổng uplink cần cấu hình trunk |
| Switch chứa PC1-PC3 | S2 G0/1 | Kết nối lên S1, cần dùng native VLAN 99 |
| Switch chứa PC4-PC6 | S3 G0/2 | Kết nối lên S1, cần dùng native VLAN 99 |
| VLAN dữ liệu | VLAN 10, VLAN 20, VLAN 30 | Dùng cho các PC theo từng nhóm mạng |
| VLAN native | VLAN 99 | Dùng làm native VLAN trên trunk |
| VLAN voice | VLAN 150 | Có thể đã được tạo từ lab VLAN Configuration trước đó |

> **Điểm dễ sai:** `show vlan brief` chỉ hiển thị các port ở chế độ access. Khi G0/1 hoặc G0/2 chuyển sang trunk, các port này sẽ không còn nằm trong danh sách port của VLAN 1 ở output `show vlan brief`.

---

## 4. Part 1: Verify VLANs

### Step 1: Kiểm tra VLAN trên S1

Trên S1:

```text
enable
show vlan brief
```

Kết quả cần kiểm tra:

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
```

> **Lưu ý:** Nếu file Packet Tracer của bạn có biến thể dùng VLAN 88 thay cho VLAN 150 thì output có thể hiển thị VLAN 88. Với chuỗi lab đang làm ở đây, VLAN voice là VLAN 150.

![S1 show vlan brief](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s1-show-vlan-brief.png)

---

### Step 2: Kiểm tra VLAN và access port trên S2

Trên S2:

```text
enable
show vlan brief
```

Kết quả cần kiểm tra:

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

![S2 show vlan brief before trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s2-show-vlan-before-trunk.png)

---

### Step 3: Kiểm tra VLAN và access port trên S3

Trên S3:

```text
enable
show vlan brief
```

Kết quả cần kiểm tra:

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

![S3 show vlan brief before trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s3-show-vlan-before-trunk.png)

---

### Step 4: Kiểm tra kết nối trước khi cấu hình trunk

Trên PC1, PC2 và PC3:

```text
ping 172.17.10.24     ! PC1 → PC4, cùng VLAN 10 nhưng khác switch
ping 172.17.20.25     ! PC2 → PC5, cùng VLAN 20 nhưng khác switch
ping 172.17.30.26     ! PC3 → PC6, cùng VLAN 30 nhưng khác switch
```

Kết quả trước khi cấu hình trunk:

| Kiểm tra | Kết quả | Nguyên nhân |
| --- | --- | --- |
| PC1 → PC4 | Fail | Uplink giữa switch vẫn đang ở VLAN 1 |
| PC2 → PC5 | Fail | VLAN 20 chưa được mang qua đường trunk |
| PC3 → PC6 | Fail | VLAN 30 chưa được mang qua đường trunk |

> **Lưu ý:** Các PC có cùng VLAN và cùng subnet vẫn không ping được nhau nếu VLAN đó không được truyền qua uplink giữa các switch.

![Ping before trunk failed](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/ping-before-trunk-failed.png)

---

## 5. Part 2: Configure Trunks

### Step 1: Cấu hình trunk trên S1

Trên S1:

```text
enable
configure terminal

interface range gigabitEthernet0/1 - 2
 switchport mode trunk
 switchport trunk native vlan 99
 exit

end
copy running-config startup-config
```

> `switchport mode trunk` chuyển cổng từ access/dynamic sang trunk. `switchport trunk native vlan 99` đặt VLAN 99 làm native VLAN thay cho VLAN 1.

Sau khi cấu hình S1, Packet Tracer có thể hiện thông báo:

```text
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/2 (99), with S3 GigabitEthernet0/2 (1).
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (99), with S2 GigabitEthernet0/1 (1).
```

> **Giải thích:** S1 đã dùng native VLAN 99, nhưng đầu còn lại trên S2/S3 vẫn đang dùng native VLAN mặc định là VLAN 1.

![S1 configure trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s1-configure-trunk.png)

---

### Step 2: Kiểm tra trunk trên S1

Trên S1:

```text
show interfaces trunk
```

Kết quả mong muốn:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      99
Gi0/2       on           802.1q         trunking      99

Port        Vlans allowed on trunk
Gi0/1       1-1005
Gi0/2       1-1005

Port        Vlans allowed and active in management domain
Gi0/1       1,10,20,30,99,150
Gi0/2       1,10,20,30,99,150
```

> **Lưu ý:** Nếu phiên bản lab của bạn dùng VLAN 88 thay cho VLAN 150, dòng active VLAN có thể là `1,10,20,30,88,99`.

![S1 show interfaces trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s1-show-interfaces-trunk.png)

---

### Step 3: Trả lời câu hỏi native VLAN mismatch

| Câu hỏi | Trả lời |
| --- | --- |
| Although you have a native VLAN mismatch, pings between PCs on the same VLAN are now successful. Explain. | Vì trunk đã hoạt động nên traffic của VLAN 10, VLAN 20 và VLAN 30 được gắn thẻ 802.1Q khi đi qua uplink. Native VLAN mismatch chủ yếu ảnh hưởng đến traffic không gắn thẻ/native VLAN và tạo cảnh báo CDP, còn traffic VLAN dữ liệu đang được tag nên ping cùng VLAN vẫn thành công. |

---

### Step 4: Kiểm tra trunk được DTP thương lượng trên S2 và S3

Trên S2:

```text
show interfaces trunk
```

Kết quả cần thấy:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       auto         802.1q         trunking      1
```

Trên S3:

```text
show interfaces trunk
```

Kết quả cần thấy:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/2       auto         802.1q         trunking      1
```

| Câu hỏi | Trả lời |
| --- | --- |
| Which active VLANs are allowed to cross the trunk? | Trong file lab này: `1,10,20,30,99,150`. Nếu file dùng biến thể VLAN 88 thì sẽ là `1,10,20,30,88,99`. |

> **Lưu ý:** S1 đã ép mode trunk, còn S2/S3 có thể tự chuyển sang trunk nhờ DTP. Tuy nhiên native VLAN trên S2/S3 vẫn đang là VLAN 1 nên cần sửa về VLAN 99.

![S2 S3 show interfaces trunk mismatch](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s2-s3-show-trunk-mismatch.png)

---

### Step 5: Sửa native VLAN mismatch trên S2

Trên S2:

```text
enable
configure terminal

interface gigabitEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
 exit

end
copy running-config startup-config
```

![S2 configure native vlan 99](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s2-native-vlan-99.png)

---

### Step 6: Sửa native VLAN mismatch trên S3

Trên S3:

```text
enable
configure terminal

interface gigabitEthernet0/2
 switchport mode trunk
 switchport trunk native vlan 99
 exit

end
copy running-config startup-config
```

![S3 configure native vlan 99](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s3-native-vlan-99.png)

---

### Step 7: Kiểm tra lại trunk trên S2 và S3

Trên S2:

```text
show interfaces trunk
show interfaces gigabitEthernet0/1 switchport
```

Kết quả cần kiểm tra:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      99

Name: Gi0/1
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Trunking Native Mode VLAN: 99
```

Trên S3:

```text
show interfaces trunk
show interfaces gigabitEthernet0/2 switchport
```

Kết quả cần kiểm tra:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gi0/2       on           802.1q         trunking      99

Name: Gi0/2
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Trunking Native Mode VLAN: 99
```

![Verify native vlan 99](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/verify-native-vlan-99.png)

---

### Step 8: Kiểm tra `show vlan brief` sau khi trunk

Trên S2:

```text
show vlan brief
```

Kết quả cần chú ý:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/12, Fa0/13, Fa0/14
                                                Fa0/15, Fa0/16, Fa0/17, Fa0/19
                                                Fa0/20, Fa0/21, Fa0/22, Fa0/23
                                                Fa0/24, Gig0/2
10   Faculty/Staff                    active    Fa0/11
20   Students                         active    Fa0/18
30   Guest(Default)                   active    Fa0/6
99   Management&Native                active
150  VOICE                            active
```

| Câu hỏi | Trả lời |
| --- | --- |
| Why is port G0/1 on S2 no longer assigned to VLAN 1? | Vì G0/1 đã chuyển sang trunk port. `show vlan brief` chỉ liệt kê access port trong từng VLAN, không liệt kê trunk port như một port access của VLAN 1. |

![S2 show vlan after trunk](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/s2-show-vlan-after-trunk.png)

---

### Step 9: Kiểm tra kết nối sau khi trunk

Trên PC1, PC2 và PC3:

```text
ping 172.17.10.24     ! PC1 → PC4, VLAN 10
ping 172.17.20.25     ! PC2 → PC5, VLAN 20
ping 172.17.30.26     ! PC3 → PC6, VLAN 30
```

Kết quả sau khi cấu hình trunk:

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC1 → PC4 | Successful |
| PC2 → PC5 | Successful |
| PC3 → PC6 | Successful |

![Ping after trunk successful](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/ping-after-trunk-successful.png)

---

## 6. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC cùng VLAN nhưng khác switch không ping được | Uplink giữa switch chưa trunk | Cấu hình `switchport mode trunk` trên cổng uplink |
| Có cảnh báo `%CDP-4-NATIVE_VLAN_MISMATCH` | Hai đầu trunk dùng native VLAN khác nhau | Cấu hình cùng `switchport trunk native vlan 99` ở cả hai đầu |
| `show vlan brief` không thấy G0/1 trong VLAN 1 | G0/1 đã là trunk port | Kiểm tra bằng `show interfaces trunk` hoặc `show interfaces g0/1 switchport` |
| Trunk chưa lên ngay sau khi cấu hình | STP cần thời gian chuyển trạng thái | Dùng Fast Forward Time trong Packet Tracer |
| Active VLAN trên trunk thiếu VLAN cần dùng | VLAN chưa được tạo trên switch hoặc bị giới hạn allowed VLAN | Kiểm tra `show vlan brief` và `show interfaces trunk` |
| Dùng sai cổng uplink | S2 dùng G0/1, S3 dùng G0/2 trong topology này | Kiểm tra sơ đồ dây hoặc rê chuột lên cổng trong Packet Tracer |

---

## 7. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| S1 G0/1 | Trunking, native VLAN 99 |
| S1 G0/2 | Trunking, native VLAN 99 |
| S2 G0/1 | Trunking, native VLAN 99 |
| S3 G0/2 | Trunking, native VLAN 99 |
| VLAN allowed and active | `1,10,20,30,99,150` |
| PC1 → PC4 | Ping successful |
| PC2 → PC5 | Ping successful |
| PC3 → PC6 | Ping successful |
| Native VLAN mismatch | Không còn cảnh báo mismatch sau khi sửa S2/S3 |

- [ ] Ảnh topology
- [ ] Ảnh `show vlan brief` trên S1, S2, S3 trước trunk
- [ ] Ảnh ping fail trước trunk
- [ ] Ảnh cấu hình trunk trên S1
- [ ] Ảnh `show interfaces trunk` trên S1, S2, S3
- [ ] Ảnh sửa native VLAN trên S2/S3
- [ ] Ảnh ping thành công sau trunk
- [ ] Ảnh Check Results / Completion

![Final result Configure Trunks](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-04/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>

  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/">Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/">Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/">Lab 3: 3.3.12 Packet Tracer - VLAN Configuration</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 3.4.5 Packet Tracer - Configure Trunks (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/">Lab 5: 3.5.5 Packet Tracer - Configure DTP</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/">Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking</a></li>
    </ul>
  </details>
</div>

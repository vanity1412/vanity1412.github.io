---
layout: page-toc
title: "CCNA 04.02 - 2.8.1 Video Activity - Test the Interface Assignment"
permalink: /writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/
toc: true
---

[← Quay lại danh sách Kết Nối Vật Lý](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/)

| Field | Value |
| --- | --- |
| Dạng lab | Kết Nối Vật Lý |
| File lab | `2.8.1 Video Activity - Test the Interface Assignment.pkt` |
| Loại file | `PKT` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Kiểm tra đúng cổng kết nối, địa chỉ IP và ping thông suốt giữa các thiết bị |

> **Ghi chú:** Bài này tập trung vào việc quan sát topology, xác định đúng cổng interface đang được sử dụng và kiểm tra kết nối trong cùng mạng `192.168.1.0/24`. Các thiết bị đã nằm trong cùng một LAN nên không cần default gateway để ping nội bộ.

## 1. Mục Tiêu Bài Lab

- Xác định đúng interface kết nối giữa PC-A, S1, S2 và PC-B.
- Kiểm tra địa chỉ IP của PC và switch trong mạng `192.168.1.0/24`.
- Dùng lệnh `show` trên switch để kiểm tra trạng thái interface.
- Dùng lệnh `ping` để kiểm tra kết nối đầu cuối.
- Ghi lại lỗi thường gặp khi xác định sai cổng hoặc nhập sai địa chỉ IP.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-02/topology.png)

## 2. Bảng Địa Chỉ IP

| Thiết bị | Interface | Địa chỉ IP | Subnet Mask | Ghi chú |
| --- | --- | --- | --- | --- |
| S1 | VLAN 1 | `192.168.1.2` | `255.255.255.0` | IP quản trị switch S1 |
| S2 | VLAN 1 | `192.168.1.3` | `255.255.255.0` | IP quản trị switch S2 |
| PC-A | FastEthernet0 | `192.168.1.10` | `255.255.255.0` | Máy tính bên trái |
| PC-B | FastEthernet0 | `192.168.1.11` | `255.255.255.0` | Máy tính bên phải |

> **Lưu ý:** Tất cả thiết bị nằm cùng subnet `/24`, vì vậy PC-A có thể ping PC-B, S1 và S2 trực tiếp mà không cần router.

## 3. Topology Overview

| Khu vực | Thiết bị / Interface | Nhận xét |
| --- | --- | --- |
| Nhánh trái | PC-A `Fa0` ↔ S1 `Fa0/6` | PC-A kết nối trực tiếp vào switch S1 |
| Liên kết giữa switch | S1 `Fa0/1` ↔ S2 `Fa0/1` | Đường kết nối chính giữa hai switch |
| Nhánh phải | S2 `Fa0/18` ↔ PC-B `Fa0` | PC-B kết nối trực tiếp vào switch S2 |
| Mạng quản trị | S1 VLAN 1, S2 VLAN 1 | Switch có IP để kiểm tra và quản trị từ xa |

> **Điểm dễ sai:** Trong Packet Tracer, tên cổng trên dây có thể nằm sát thiết bị nên dễ nhầm `Fa0/1` với `Fa0/6` hoặc `Fa0/18`. Khi làm bài này cần nhìn đúng nhãn interface ở hai đầu dây.

## 4. Part 1 - Kiểm Tra Interface Assignment Trên Switch

### Step 1: Kiểm tra nhanh trên S1

```text
S1> enable
S1# show ip interface brief

! Kết quả cần chú ý
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  192.168.1.2     YES manual up                    up
FastEthernet0/1        unassigned      YES unset  up                    up
FastEthernet0/6        unassigned      YES unset  up                    up
```

```text
S1# show interfaces status

! Các cổng đang dùng trên S1
Port      Name               Status       Vlan       Duplex  Speed Type
Fa0/1                        connected    1          auto    auto  10/100BaseTX
Fa0/6                        connected    1          auto    auto  10/100BaseTX
```

> **Lưu ý:** `Fa0/1` của S1 nối sang S2, còn `Fa0/6` của S1 nối xuống PC-A.

![S1 interface status](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-02/s1-interface-status.png)

### Step 2: Kiểm tra nhanh trên S2

```text
S2> enable
S2# show ip interface brief

! Kết quả cần chú ý
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  192.168.1.3     YES manual up                    up
FastEthernet0/1        unassigned      YES unset  up                    up
FastEthernet0/18       unassigned      YES unset  up                    up
```

```text
S2# show interfaces status

! Các cổng đang dùng trên S2
Port      Name               Status       Vlan       Duplex  Speed Type
Fa0/1                        connected    1          auto    auto  10/100BaseTX
Fa0/18                       connected    1          auto    auto  10/100BaseTX
```

> **Lưu ý:** `Fa0/1` của S2 nối sang S1, còn `Fa0/18` của S2 nối xuống PC-B.


## 5. Part 2 - Kiểm Tra IP Configuration Trên PC

### Step 1: Kiểm tra PC-A

| Trường | Giá trị |
| --- | --- |
| IP Address | `192.168.1.10` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống hoặc không bắt buộc trong bài này |


### Step 2: Kiểm tra PC-B

| Trường | Giá trị |
| --- | --- |
| IP Address | `192.168.1.11` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống hoặc không bắt buộc trong bài này |

![PC-B IP configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-02/pc-b-ip-configuration.png)

> **Lưu ý:** Default gateway chỉ cần khi PC muốn đi ra mạng khác. Bài này toàn bộ thiết bị cùng mạng `192.168.1.0/24`, nên trọng tâm là kiểm tra IP, subnet mask và cổng kết nối.

## 6. Part 3 - Kiểm Tra Kết Nối Bằng Ping

### Step 1: Ping từ PC-A

```text
PC-A> ping 192.168.1.11
! Kiểm tra PC-A đến PC-B

PC-A> ping 192.168.1.2
! Kiểm tra PC-A đến IP quản trị S1

PC-A> ping 192.168.1.3
! Kiểm tra PC-A đến IP quản trị S2
```


### Step 2: Ping từ PC-B

```text
PC-B> ping 192.168.1.10
! Kiểm tra PC-B đến PC-A

PC-B> ping 192.168.1.2
! Kiểm tra PC-B đến IP quản trị S1

PC-B> ping 192.168.1.3
! Kiểm tra PC-B đến IP quản trị S2
```


> **Lưu ý:** Nếu lần ping đầu tiên chưa đạt 100%, chạy lại lần thứ hai. Lần đầu có thể mất gói do thiết bị cần học ARP/MAC address trước khi truyền ổn định.

## 7. Bảng Tổng Hợp Interface Assignment

| Kết nối | Interface đầu 1 | Interface đầu 2 | Trạng thái mong muốn |
| --- | --- | --- | --- |
| PC-A ↔ S1 | PC-A `Fa0` | S1 `Fa0/6` | Link up / ping được |
| S1 ↔ S2 | S1 `Fa0/1` | S2 `Fa0/1` | Link up / truyền được giữa hai switch |
| S2 ↔ PC-B | S2 `Fa0/18` | PC-B `Fa0` | Link up / ping được |

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Ping PC-A sang PC-B thất bại | Sai IP hoặc subnet mask trên PC | Kiểm tra lại `192.168.1.10/24` và `192.168.1.11/24` |
| Không ping được IP của switch | VLAN 1 chưa up hoặc switch chưa có IP đúng | Dùng `show ip interface brief` để kiểm tra trạng thái VLAN 1 |
| Nhầm cổng trên S1 | Nhìn sai nhãn interface trong topology | Ghi nhớ S1 dùng `Fa0/1` nối S2 và `Fa0/6` nối PC-A |
| Nhầm cổng trên S2 | Dễ nhầm `Fa0/1` với `Fa0/18` | Ghi nhớ S2 dùng `Fa0/1` nối S1 và `Fa0/18` nối PC-B |
| Ping lần đầu chỉ đạt 80% | ARP/MAC table chưa học xong | Ping lại lần thứ hai để xác nhận |

## 9. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC-A `192.168.1.10/24` | Đúng IP, đúng subnet mask |
| PC-B `192.168.1.11/24` | Đúng IP, đúng subnet mask |
| S1 VLAN 1 `192.168.1.2/24` | Interface VLAN 1 up/up |
| S2 VLAN 1 `192.168.1.3/24` | Interface VLAN 1 up/up |
| S1 `Fa0/1` ↔ S2 `Fa0/1` | Hai đầu link đều up |
| S1 `Fa0/6` ↔ PC-A `Fa0` | Hai đầu link đều up |
| S2 `Fa0/18` ↔ PC-B `Fa0` | Hai đầu link đều up |
| Ping PC-A ↔ PC-B | Thành công |
| Ping PC đến S1/S2 | Thành công |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/">Lab 1: 2.7.6 Packet Tracer - Implement Basic Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 2.8.1 Video Activity - Test the Interface Assignment (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/">Lab 3: 2.8.2 Video Activity - Test End-to-End Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/">Lab 4: 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/">Lab 5: 4.7.1 Packet Tracer - Connect the Physical Layer</a></li>
    </ul>
  </details>
</div>

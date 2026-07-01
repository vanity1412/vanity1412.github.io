---
layout: page-toc
title: "CCNA 04.03 - 2.8.2 Video Activity - Test End-to-End Connectivity"
permalink: /writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/
toc: true
---

[← Quay lại danh sách Kết Nối Vật Lý](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/)

| Field | Value |
| --- | --- |
| Dạng lab | Kết Nối Vật Lý |
| File lab | `2.8.2 Video Activity - Test End-to-End Connectivity.pkt` |
| Loại file | `PKT` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Kiểm tra kết nối end-to-end giữa PC-A, PC-B và IP quản trị của hai switch |

> **Ghi chú:** Bài này tập trung vào kiểm tra kết nối đầu cuối. Các thiết bị cùng nằm trong mạng `192.168.1.0/24`, nên PC-A có thể ping PC-B trực tiếp qua switch mà không cần router.

## 1. Mục Tiêu Bài Lab

- Xác định đúng địa chỉ IP của PC-A, PC-B, S1 và S2.
- Kiểm tra trạng thái các cổng kết nối vật lý giữa PC và switch.
- Kiểm tra trạng thái interface VLAN 1 trên S1 và S2.
- Dùng lệnh `ping` để kiểm tra kết nối end-to-end.
- Xác định lỗi thường gặp khi ping không thành công.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-03/topology.png)

## 2. Bảng Địa Chỉ IPv4

| Thiết bị | Interface | Địa chỉ IPv4 | Subnet Mask | Ghi chú |
| --- | --- | --- | --- | --- |
| PC-A | Fa0 | `192.168.1.10` | `255.255.255.0` | Máy đầu cuối bên trái |
| PC-B | Fa0 | `192.168.1.11` | `255.255.255.0` | Máy đầu cuối bên phải |
| S1 | VLAN 1 | `192.168.1.2` | `255.255.255.0` | IP quản trị switch S1 |
| S2 | VLAN 1 | `192.168.1.3` | `255.255.255.0` | IP quản trị switch S2 |

> **Lưu ý:** Tất cả địa chỉ đều thuộc cùng subnet `192.168.1.0/24`, vì vậy bài này không cần cấu hình default gateway để kiểm tra ping trong cùng mạng LAN.

## 3. Topology Overview

| Kết nối | Cổng thiết bị 1 | Cổng thiết bị 2 | Trạng thái mong muốn |
| --- | --- | --- | --- |
| PC-A ↔ S1 | PC-A `Fa0` | S1 `Fa0/6` | Up |
| S1 ↔ S2 | S1 `Fa0/1` | S2 `Fa0/1` | Up |
| S2 ↔ PC-B | S2 `Fa0/18` | PC-B `Fa0` | Up |

> **Điểm dễ sai:** Nhãn `192.168.1.2/24` và `192.168.1.3/24` trên topology là IP quản trị của switch trên `VLAN 1`, không phải IP của cổng vật lý `Fa0/1`, `Fa0/6` hay `Fa0/18`.

## 4. Kiểm Tra Cấu Hình Trên PC

### PC-A

| Mục | Giá trị cần đúng |
| --- | --- |
| IP Address | `192.168.1.10` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống hoặc không bắt buộc trong bài này |

### PC-B

| Mục | Giá trị cần đúng |
| --- | --- |
| IP Address | `192.168.1.11` |
| Subnet Mask | `255.255.255.0` |
| Default Gateway | Để trống hoặc không bắt buộc trong bài này |


## 5. Kiểm Tra Trên Switch

### S1

```text
S1> enable
S1# show ip interface brief
S1# show interfaces status
S1# show mac address-table dynamic
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `Vlan1` | IP `192.168.1.2`, trạng thái `up/up` |
| `Fa0/1` | Kết nối sang S2, trạng thái connected/up |
| `Fa0/6` | Kết nối sang PC-A, trạng thái connected/up |
| MAC address table | Học được MAC của PC-A và thiết bị phía S2 |


### S2

```text
S2> enable
S2# show ip interface brief
S2# show interfaces status
S2# show mac address-table dynamic
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `Vlan1` | IP `192.168.1.3`, trạng thái `up/up` |
| `Fa0/1` | Kết nối sang S1, trạng thái connected/up |
| `Fa0/18` | Kết nối sang PC-B, trạng thái connected/up |
| MAC address table | Học được MAC của PC-B và thiết bị phía S1 |


> **Lưu ý:** Nếu `Vlan1` có IP đúng nhưng trạng thái chưa `up/up`, hãy kiểm tra xem ít nhất một cổng switch trong VLAN 1 đã có link hoạt động hay chưa.

## 6. Cấu Hình Tham Khảo Nếu IP Quản Trị Chưa Đúng

### S1

```text
S1> enable
S1# configure terminal
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.2 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# exit
S1(config)# end
S1# copy running-config startup-config
```

> `no shutdown` dùng để bật interface VLAN 1. Nếu interface bị shutdown, switch vẫn chuyển frame Layer 2 được nhưng không ping được IP quản trị của switch.

### S2

```text
S2> enable
S2# configure terminal
S2(config)# interface vlan 1
S2(config-if)# ip address 192.168.1.3 255.255.255.0
S2(config-if)# no shutdown
S2(config-if)# exit
S2(config)# end
S2# copy running-config startup-config
```

## 7. Kiểm Tra End-to-End Connectivity

### Từ PC-A

```text
PC> ping 192.168.1.11
! Kiểm tra PC-A ping PC-B

PC> ping 192.168.1.2
! Kiểm tra PC-A ping IP quản trị S1

PC> ping 192.168.1.3
! Kiểm tra PC-A ping IP quản trị S2
```


### Từ PC-B

```text
PC> ping 192.168.1.10
! Kiểm tra PC-B ping PC-A

PC> ping 192.168.1.2
! Kiểm tra PC-B ping IP quản trị S1

PC> ping 192.168.1.3
! Kiểm tra PC-B ping IP quản trị S2
```


### Từ S1 và S2

```text
S1# ping 192.168.1.3
! S1 ping S2

S1# ping 192.168.1.10
! S1 ping PC-A

S1# ping 192.168.1.11
! S1 ping PC-B

S2# ping 192.168.1.2
! S2 ping S1

S2# ping 192.168.1.10
! S2 ping PC-A

S2# ping 192.168.1.11
! S2 ping PC-B
```

> **Lưu ý:** Nếu lần ping đầu tiên bị mất 1 gói, chạy lại lệnh ping. Trường hợp này thường xảy ra do thiết bị cần học ARP/MAC trước khi truyền ổn định.

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC-A không ping được PC-B | Sai IP/subnet mask hoặc cổng kết nối chưa up | Kiểm tra IP trên PC, kiểm tra đèn link và `show interfaces status` |
| Ping được PC cùng mạng nhưng không ping được switch | IP VLAN 1 sai hoặc interface VLAN 1 đang shutdown | Kiểm tra `show ip interface brief`, cấu hình lại `interface vlan 1`, dùng `no shutdown` |
| S1 không ping được S2 | Link giữa S1 `Fa0/1` và S2 `Fa0/1` chưa hoạt động | Kiểm tra dây nối, đúng cổng, trạng thái interface |
| MAC address table chưa có địa chỉ của PC | Chưa có traffic đi qua switch | Thực hiện ping rồi kiểm tra lại `show mac address-table dynamic` |
| Ping lần đầu chỉ đạt 80% | Thiết bị đang học ARP/MAC | Ping lại lần thứ hai để xác nhận kết nối |

## 9. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| PC-A ping PC-B `192.168.1.11` | Thành công | Đạt |
| PC-B ping PC-A `192.168.1.10` | Thành công | Đạt |
| PC-A ping S1 `192.168.1.2` | Thành công | Đạt |
| PC-A ping S2 `192.168.1.3` | Thành công | Đạt |
| PC-B ping S1 `192.168.1.2` | Thành công | Đạt |
| PC-B ping S2 `192.168.1.3` | Thành công | Đạt |
| `show ip interface brief` trên S1 | `Vlan1` up/up, IP `192.168.1.2` | Đạt |
| `show ip interface brief` trên S2 | `Vlan1` up/up, IP `192.168.1.3` | Đạt |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/">Lab 1: 2.7.6 Packet Tracer - Implement Basic Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/">Lab 2: 2.8.1 Video Activity - Test the Interface Assignment</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 2.8.2 Video Activity - Test End-to-End Connectivity (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/">Lab 4: 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/">Lab 5: 4.7.1 Packet Tracer - Connect the Physical Layer</a></li>
    </ul>
  </details>
</div>

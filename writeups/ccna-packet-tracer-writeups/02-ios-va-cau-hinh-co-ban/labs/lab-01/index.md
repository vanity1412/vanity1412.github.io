---
layout: page-toc
title: "CCNA 02.01 - 1.4.7 Packet Tracer - Configure Router Interfaces"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `1.4.7 Packet Tracer - Configure Router Interfaces.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành cấu hình IPv4, IPv6 và kiểm tra kết nối |

> **Ghi chú:** Serial interface đã được cấu hình sẵn. Nhiệm vụ chính là cấu hình cổng LAN của R1/R2, gán IP cho PC và kiểm tra kết nối bằng `ping`.

---

## 1. Mục Tiêu Bài Lab

- Cấu hình IPv4 cho interface LAN trên R1 và các PC1, PC2
- Cấu hình IPv6 cho interface LAN trên R2 và các PC3, PC4
- Kiểm tra trạng thái interface bằng `show ip interface brief` / `show ipv6 interface brief`
- Kiểm tra kết nối giữa các LAN và Dual Stack Server bằng `ping`

![Topology Configure Router Interfaces](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/topology.png)

![yeu cau de](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/instructions.png)

---

## 2. Bảng Địa Chỉ IP

### IPv4

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | 172.16.20.1 | 255.255.255.128 (/25) | N/A |
| R1 | G0/1 | 172.16.20.129 | 255.255.255.128 (/25) | N/A |
| R1 | S0/0/0 | 209.165.200.225 | /30 | N/A |
| PC1 | NIC | 172.16.20.10 | 255.255.255.128 | 172.16.20.1 |
| PC2 | NIC | 172.16.20.138 | 255.255.255.128 | 172.16.20.129 |
| Dual Stack Server | NIC | 64.100.1.1 | — | — |

### IPv6

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R2 | G0/0 | 2001:db8:c0de:12::1/64 | N/A |
| R2 | G0/1 | 2001:db8:c0de:13::1/64 | N/A |
| R2 | S0/0/1 | 2001:db8:c0de:11::1/64 | N/A |
| R2 | G0/0, G0/1 link-local | fe80::2 | N/A |
| PC3 | NIC | 2001:db8:c0de:12::a/64 | fe80::2 |
| PC4 | NIC | 2001:db8:c0de:13::a/64 | fe80::2 |
| Dual Stack Server | NIC | 2001:db8:100:1::a | — |

> **Lưu ý:** PC3 và PC4 dùng `fe80::2` làm default gateway — cần cấu hình link-local address `fe80::2` trên **cả hai** cổng LAN của R2. Link-local chỉ có hiệu lực trong phạm vi từng liên kết nên có thể dùng cùng một địa chỉ trên nhiều interface.

---

## 3. Part 1: Configure IPv4 Addressing

### Step 1: Cấu hình R1

```text
enable
configure terminal

interface gigabitEthernet0/0
 ip address 172.16.20.1 255.255.255.128
 no shutdown
 exit

interface gigabitEthernet0/1
 ip address 172.16.20.129 255.255.255.128
 no shutdown
 exit

end
copy running-config startup-config
```

---

### Step 2: Cấu hình PC1

Vào **PC1 → Desktop → IP Configuration**:

| Field | Value |
| --- | --- |
| IP Address | 172.16.20.10 |
| Subnet Mask | 255.255.255.128 |
| Default Gateway | 172.16.20.1 |

![PC1 IPv4 Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/pc1-ipv4.png)

---

### Step 3: Cấu hình PC2

Vào **PC2 → Desktop → IP Configuration**:

| Field | Value |
| --- | --- |
| IP Address | 172.16.20.138 |
| Subnet Mask | 255.255.255.128 |
| Default Gateway | 172.16.20.129 |

![PC2 IPv4 Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/pc2-ipv4.png)

---

### Step 4: Kiểm tra IPv4

Trên R1:

```text
show ip interface brief
```

Kết quả mong muốn:

```text
Interface              IP-Address       OK? Method Status     Protocol
GigabitEthernet0/0     172.16.20.1      YES manual up         up
GigabitEthernet0/1     172.16.20.129    YES manual up         up
Serial0/0/0            209.165.200.225  YES manual up         up
```

> Nếu interface hiển thị `administratively down` → vào lại interface đó, nhập `no shutdown`.

Trên PC1 và PC2 (**Desktop → Command Prompt**):

```text
ping 172.16.20.138     ! PC1 → PC2
ping 64.100.1.1        ! PC1/PC2 → Dual Stack Server
```

![Ping PC1 to PC2 and server](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/ping-pc1-pc2-server.png)

---

## 4. Part 2: Configure IPv6 Addressing

### Step 1: Cấu hình R2

```text
enable
configure terminal

ipv6 unicast-routing

interface gigabitEthernet0/0
 ipv6 address 2001:db8:c0de:12::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit

interface gigabitEthernet0/1
 ipv6 address 2001:db8:c0de:13::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit

end
copy running-config startup-config
```

> `ipv6 unicast-routing` phải bật trước — nếu thiếu, router sẽ không định tuyến IPv6 giữa các mạng.

---

### Step 2: Cấu hình PC3

Vào **PC3 → Desktop → IP Configuration**:

| Field | Value |
| --- | --- |
| IPv6 Address | 2001:db8:c0de:12::a |
| Prefix Length | 64 |
| IPv6 Gateway | fe80::2 |

![PC3 IPv6 Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/pc3-ipv6.png)

---

### Step 3: Cấu hình PC4

Vào **PC4 → Desktop → IP Configuration**:

| Field | Value |
| --- | --- |
| IPv6 Address | 2001:db8:c0de:13::a |
| Prefix Length | 64 |
| IPv6 Gateway | fe80::2 |

![PC4 IPv6 Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/pc4-ipv6.png)

---

### Step 4: Kiểm tra IPv6

Trên R2:

```text
show ipv6 interface brief
```

Kết quả mong muốn:

```text
GigabitEthernet0/0        [up/up]
    FE80::2
    2001:DB8:C0DE:12::1

GigabitEthernet0/1        [up/up]
    FE80::2
    2001:DB8:C0DE:13::1

Serial0/0/1               [up/up]
    2001:DB8:C0DE:11::1
```

Trên PC3 và PC4 (**Desktop → Command Prompt**):

```text
ping 2001:db8:c0de:13::a    ! PC3 → PC4
ping 2001:db8:100:1::a      ! PC3/PC4 → Dual Stack Server
```

![Ping PC3 to PC4 and server](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/ping-pc3-pc4-server.png)


---

## 5. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC1 không ping được PC2 | Sai IP, subnet mask hoặc gateway | Kiểm tra lại IP Configuration của PC1/PC2 |
| R1 interface `administratively down` | Thiếu `no shutdown` | Vào interface, nhập `no shutdown` |
| PC1/PC2 không ping được server | Sai gateway hoặc interface chưa up | Kiểm tra gateway và `show ip interface brief` |
| PC3 không ping được PC4 | Sai IPv6 address hoặc gateway | Kiểm tra IPv6 Configuration trên PC3/PC4 |
| PC3/PC4 không ping được server | Thiếu `ipv6 unicast-routing` hoặc sai gateway | Kiểm tra R2 bằng `show ipv6 interface brief` |
| Gateway IPv6 không hoạt động | Thiếu `fe80::2 link-local` trên cổng LAN của R2 | Cấu hình link-local trên cả G0/0 và G0/1 |
| Sai tên interface | Tên cổng trong Packet Tracer có thể khác thiết bị thật | Dùng `show ip interface brief` để xem tên cổng đúng |

---

## 6. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| R1 G0/0 | 172.16.20.1/25 — up/up |
| R1 G0/1 | 172.16.20.129/25 — up/up |
| PC1 | Ping được PC2 và Dual Stack Server |
| PC2 | Ping được PC1 và Dual Stack Server |
| R2 G0/0 | 2001:db8:c0de:12::1/64 — up/up |
| R2 G0/1 | 2001:db8:c0de:13::1/64 — up/up |
| PC3 | Ping được PC4 và Dual Stack Server |
| PC4 | Ping được PC3 và Dual Stack Server |

![ket qua xong lab](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/final.png)

![alt text](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-01/final1.png)

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
      <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces (Đang đọc)</strong></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>
---
layout: page-toc
title: "CCNA 05.07 - 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-07/` |
| Trạng thái | Hoàn thiện bảng địa chỉ PC, kiểm tra ping IPv4/IPv6 và xác định đường đi bằng `tracert` |

> **Ghi chú:** Đây là lab kiểm tra dual-stack IPv4/IPv6. Router đã được cấu hình sẵn, nhiệm vụ chính là thu thập thông tin IP trên PC, kiểm tra kết nối và ghi lại đường đi của gói tin.

## 1. Mục Tiêu Bài Lab

- Hoàn thiện bảng địa chỉ IPv4 và IPv6 cho PC1, PC2.
- Kiểm tra kết nối IPv4 bằng `ping`.
- Kiểm tra kết nối IPv6 bằng `ping`.
- Dùng `tracert` để xác định đường đi từ PC1 đến PC2 và ngược lại.
- Liên hệ từng địa chỉ trong kết quả `tracert` với đúng interface trên router.

![Topology lab 07](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/topology.png)

## 2. Bảng Địa Chỉ IP

### 2.1. IPv4 Addressing Table

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `10.10.1.97` | `255.255.255.224` | N/A |
| R1 | S0/0/1 | `10.10.1.6` | `255.255.255.252` | N/A |
| R2 | S0/0/0 | `10.10.1.5` | `255.255.255.252` | N/A |
| R2 | S0/0/1 | `10.10.1.9` | `255.255.255.252` | N/A |
| R3 | S0/0/1 | `10.10.1.10` | `255.255.255.252` | N/A |
| R3 | G0/0 | `10.10.1.17` | `255.255.255.240` | N/A |
| PC1 | NIC | `10.10.1.126` | `255.255.255.224` | `10.10.1.97` |
| PC2 | NIC | `10.10.1.20` | `255.255.255.240` | `10.10.1.17` |

> **Lưu ý:** PC1 thuộc mạng `10.10.1.96/27`, gateway là R1 G0/0. PC2 thuộc mạng `10.10.1.16/28`, gateway là R3 G0/0.

### 2.2. IPv6 Addressing Table

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:1:1::1/64` | N/A |
| R1 | S0/0/1 | `2001:db8:1:2::2/64` | N/A |
| R1 | S0/0/1 | `fe80::1` | N/A |
| R2 | S0/0/0 | `2001:db8:1:2::1/64` | N/A |
| R2 | S0/0/1 | `2001:db8:1:3::1/64` | N/A |
| R2 | S0/0/1 | `fe80::2` | N/A |
| R3 | S0/0/1 | `2001:db8:1:3::2/64` | N/A |
| R3 | S0/0/1 | `fe80::3` | N/A |
| R3 | G0/0 | `2001:db8:1:4::1/64` | N/A |
| PC1 | NIC | `2001:db8:1:1::a/64` | `fe80::1` |
| PC2 | NIC | `2001:db8:1:4::a/64` | `fe80::3` |

> **Lưu ý:** Với IPv6, default gateway của PC thường là địa chỉ link-local của router trên cùng LAN. Trong bài này PC1 đi ra R1, PC2 đi ra R3.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN trái | PC1, S1, R1 G0/0 | Mạng IPv4 `10.10.1.96/27`, mạng IPv6 `2001:db8:1:1::/64` |
| Link R1-R2 | R1 S0/0/1, R2 S0/0/0 | IPv4 `10.10.1.4/30`, IPv6 `2001:db8:1:2::/64` |
| Link R2-R3 | R2 S0/0/1, R3 S0/0/1 | IPv4 `10.10.1.8/30`, IPv6 `2001:db8:1:3::/64` |
| LAN phải | R3 G0/0, S2, PC2 | Mạng IPv4 `10.10.1.16/28`, mạng IPv6 `2001:db8:1:4::/64` |

> **Điểm dễ sai:** Đừng nhầm mạng LAN của PC2 là `/27`. Theo topology, LAN phải dùng `10.10.1.16/28`, nên gateway của PC2 là `10.10.1.17`.

## 4. Part 1 - Complete the Addressing Table Documentation

### Step 1: Kiểm tra IPv4 trên PC1 và PC2

Trên PC1:

```text
PC> ipconfig /all

IPv4 Address......................: 10.10.1.126
Subnet Mask.......................: 255.255.255.224
Default Gateway...................: 10.10.1.97
```

![PC1 IPv4 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc1-ipconfig-ipv4.png)

Trên PC2:

```text
PC> ipconfig /all

IPv4 Address......................: 10.10.1.20
Subnet Mask.......................: 255.255.255.240
Default Gateway...................: 10.10.1.17
```

![PC2 IPv4 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc2-ipconfig-ipv4.png)

### Step 2: Kiểm tra IPv6 trên PC1 và PC2

Trên PC1:

```text
PC> ipv6config /all

IPv6 Address......................: 2001:db8:1:1::a/64
Default Gateway...................: fe80::1
```

![PC1 IPv6 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc1-ipv6config.png)

Trên PC2:

```text
PC> ipv6config /all

IPv6 Address......................: 2001:db8:1:4::a/64
Default Gateway...................: fe80::3
```

![PC2 IPv6 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc2-ipv6config.png)

## 5. Part 2 - Test Connectivity Using Ping

### Step 1: Kiểm tra IPv4 từ PC1 sang PC2

```text
PC> ping 10.10.1.20

Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC1 ping được IPv4 của PC2. |

![Ping IPv4 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/ping-ipv4-pc1-to-pc2.png)

### Step 2: Kiểm tra IPv4 từ PC2 sang PC1

```text
PC> ping 10.10.1.126

Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC2 ping được IPv4 của PC1. |

![Ping IPv4 PC2 to PC1](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/ping-ipv4-pc2-to-pc1.png)

### Step 3: Kiểm tra IPv6 hai chiều

```text
! PC1 ping PC2 IPv6
PC> ping 2001:db8:1:4::a

! PC2 ping PC1 IPv6
PC> ping 2001:db8:1:1::a
```

| Kiểm tra | Kết quả |
| --- | --- |
| PC1 ping `2001:db8:1:4::a` | Successful |
| PC2 ping `2001:db8:1:1::a` | Successful |

![Ping IPv6 test](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/ping-ipv6.png)

## 6. Part 3 - Discover the Path by Tracing the Route

### Step 1: Traceroute IPv4 từ PC1 đến PC2

```text
PC> tracert 10.10.1.20

1   10.10.1.97
2   10.10.1.5
3   10.10.1.10
4   10.10.1.20
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `10.10.1.97` | R1 G0/0 |
| 2 | `10.10.1.5` | R2 S0/0/0 |
| 3 | `10.10.1.10` | R3 S0/0/1 |
| 4 | `10.10.1.20` | PC2 NIC |

![Traceroute IPv4 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv4-pc1-to-pc2.png)

### Step 2: Traceroute IPv4 từ PC2 đến PC1

```text
PC> tracert 10.10.1.126

1   10.10.1.17
2   10.10.1.9
3   10.10.1.6
4   10.10.1.126
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `10.10.1.17` | R3 G0/0 |
| 2 | `10.10.1.9` | R2 S0/0/1 |
| 3 | `10.10.1.6` | R1 S0/0/1 |
| 4 | `10.10.1.126` | PC1 NIC |

![Traceroute IPv4 PC2 to PC1](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv4-pc2-to-pc1.png)

### Step 3: Traceroute IPv6 từ PC1 đến PC2

```text
PC> tracert 2001:db8:1:4::a

1   2001:db8:1:1::1
2   2001:db8:1:2::1
3   2001:db8:1:3::2
4   2001:db8:1:4::a
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `2001:db8:1:1::1` | R1 G0/0 |
| 2 | `2001:db8:1:2::1` | R2 S0/0/0 |
| 3 | `2001:db8:1:3::2` | R3 S0/0/1 |
| 4 | `2001:db8:1:4::a` | PC2 NIC |

![Traceroute IPv6 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv6-pc1-to-pc2.png)

### Step 4: Traceroute IPv6 từ PC2 đến PC1

```text
PC> tracert 2001:db8:1:1::a

1   2001:db8:1:4::1
2   2001:db8:1:3::1
3   2001:db8:1:2::2
4   2001:db8:1:1::a
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `2001:db8:1:4::1` | R3 G0/0 |
| 2 | `2001:db8:1:3::1` | R2 S0/0/1 |
| 3 | `2001:db8:1:2::2` | R1 S0/0/1 |
| 4 | `2001:db8:1:1::a` | PC1 NIC |

![Traceroute IPv6 PC2 to PC1](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv6-pc2-to-pc1.png)

## 7. Kiểm Tra Và Bằng Chứng

| Kiểm tra | Lệnh | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- | --- |
| Xem IPv4 PC1 | `ipconfig /all` | PC1 có IP `10.10.1.126/27`, gateway `10.10.1.97` | `pc1-ipconfig-ipv4.png` |
| Xem IPv4 PC2 | `ipconfig /all` | PC2 có IP `10.10.1.20/28`, gateway `10.10.1.17` | `pc2-ipconfig-ipv4.png` |
| Xem IPv6 PC1 | `ipv6config /all` | PC1 có IPv6 `2001:db8:1:1::a/64` | `pc1-ipv6config.png` |
| Xem IPv6 PC2 | `ipv6config /all` | PC2 có IPv6 `2001:db8:1:4::a/64` | `pc2-ipv6config.png` |
| Ping IPv4 | `ping 10.10.1.20`, `ping 10.10.1.126` | Hai chiều thành công | `ping-ipv4-*.png` |
| Ping IPv6 | `ping 2001:db8:1:4::a`, `ping 2001:db8:1:1::a` | Hai chiều thành công | `ping-ipv6.png` |
| Traceroute IPv4 | `tracert` | Đi qua R1, R2, R3 đúng thứ tự | `tracert-ipv4-*.png` |
| Traceroute IPv6 | `tracert` | Đi qua R1, R2, R3 đúng thứ tự | `tracert-ipv6-*.png` |

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC không ping được thiết bị bên kia | Sai IPv4 address, subnet mask hoặc default gateway | Kiểm tra lại bằng `ipconfig /all` |
| Ping IPv4 được nhưng IPv6 không được | Sai IPv6 address hoặc IPv6 default gateway | Kiểm tra bằng `ipv6config /all` |
| `tracert` không đi qua đủ router | Routing hoặc gateway không đúng | Kiểm tra gateway của PC và routing trên router |
| Nhầm subnet PC1 và PC2 | PC1 dùng `/27`, PC2 dùng `/28` | Đối chiếu lại topology và bảng địa chỉ |
| Ghi sai IPv6 prefix | Thiếu `/64` hoặc sai subnet `1:1`, `1:4` | Ghi đúng dạng `2001:db8:1:x::/64` |

## 9. Kết Quả Cuối

| Nội dung | Kết quả |
| --- | --- |
| Bảng địa chỉ PC1/PC2 | Đã hoàn thiện IPv4 và IPv6 |
| Ping IPv4 PC1 ↔ PC2 | Thành công |
| Ping IPv6 PC1 ↔ PC2 | Thành công |
| Traceroute IPv4 | Xác định đúng đường đi qua R1, R2, R3 |
| Traceroute IPv6 | Xác định đúng đường đi qua R1, R2, R3 |
| Trạng thái lab | Hoàn thành |

- [ ] Chụp topology và lưu `topology.png`.
- [ ] Chụp `ipconfig /all` trên PC1, PC2.
- [ ] Chụp `ipv6config /all` trên PC1, PC2.
- [ ] Chụp ping IPv4 hai chiều.
- [ ] Chụp ping IPv6 hai chiều.
- [ ] Chụp traceroute IPv4.
- [ ] Chụp traceroute IPv6.
- [ ] Chụp Check Results hoàn thành.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 6</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

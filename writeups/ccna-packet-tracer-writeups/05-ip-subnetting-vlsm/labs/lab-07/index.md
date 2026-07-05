---
layout: page-toc
title: "CCNA 05.07 - 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM, Dual-stack Verification |
| File lab | `13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-07/` |
| Trạng thái | Hoàn thiện bảng địa chỉ PC, kiểm tra `ping` IPv4/IPv6 và xác định đường đi bằng `tracert` |

> Bài này không yêu cầu cấu hình router từ đầu. Nhiệm vụ chính là kiểm tra hệ thống dual-stack IPv4/IPv6 đã có sẵn, dùng `ipconfig /all`, `ipv6config /all`, `ping` và `tracert` để hoàn thiện bảng địa chỉ, xác nhận kết nối và phân tích từng hop trên đường đi.

## 1. Mục Tiêu Bài Lab

- Thu thập thông tin IPv4 của `PC1` và `PC2` bằng `ipconfig /all`.
- Thu thập thông tin IPv6 của `PC1` và `PC2` bằng `ipv6config /all`.
- Hoàn thiện Addressing Table cho hai PC.
- Kiểm tra kết nối IPv4 hai chiều giữa `PC1` và `PC2`.
- Kiểm tra kết nối IPv6 hai chiều giữa `PC1` và `PC2`.
- Dùng `tracert` để xác định đường đi của gói tin IPv4 và IPv6.
- Mapping từng địa chỉ trong kết quả `tracert` với đúng interface trên router.

![Topology lab 07](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/topology.png)

![Topology lab 07](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/topology1.png)


## 2. Topology Overview

| Khu vực | Thiết bị | IPv4 network | IPv6 prefix | Nhận xét |
| --- | --- | --- | --- | --- |
| LAN trái | PC1, S1, R1 G0/0 | `10.10.1.96/27` | `2001:db8:1:1::/64` | PC1 đi ra ngoài qua R1 G0/0 |
| Link R1-R2 | R1 S0/0/1, R2 S0/0/0 | `10.10.1.4/30` | `2001:db8:1:2::/64` | WAN point-to-point thứ nhất |
| Link R2-R3 | R2 S0/0/1, R3 S0/0/1 | `10.10.1.8/30` | `2001:db8:1:3::/64` | WAN point-to-point thứ hai |
| LAN phải | R3 G0/0, S2, PC2 | `10.10.1.16/28` | `2001:db8:1:4::/64` | PC2 đi ra ngoài qua R3 G0/0 |

> **Lưu ý:** Đây là mô hình dual-stack, nghĩa là cùng một thiết bị có thể chạy đồng thời IPv4 và IPv6. Khi kiểm tra phải làm riêng IPv4 và IPv6, không được lấy kết quả của giao thức này thay cho giao thức còn lại.

## 3. Bảng Địa Chỉ IP Hoàn Chỉnh

### 3.1. IPv4 Addressing Table

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `10.10.1.97` | `255.255.255.224` | N/A |
| R1 | S0/0/1 | `10.10.1.6` | `255.255.255.252` | N/A |
| R2 | S0/0/0 | `10.10.1.5` | `255.255.255.252` | N/A |
| R2 | S0/0/1 | `10.10.1.9` | `255.255.255.252` | N/A |
| R3 | G0/0 | `10.10.1.17` | `255.255.255.240` | N/A |
| R3 | S0/0/1 | `10.10.1.10` | `255.255.255.252` | N/A |
| PC1 | NIC | `10.10.1.126` | `255.255.255.224` | `10.10.1.97` |
| PC2 | NIC | `10.10.1.20` | `255.255.255.240` | `10.10.1.17` |

> **Lưu ý:** `PC1` thuộc subnet `10.10.1.96/27`, usable range là `10.10.1.97` đến `10.10.1.126`. `PC2` thuộc subnet `10.10.1.16/28`, usable range là `10.10.1.17` đến `10.10.1.30`.

### 3.2. IPv6 Addressing Table

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:1:1::1/64` | N/A |
| R1 | S0/0/1 | `2001:db8:1:2::2/64` | N/A |
| R1 | S0/0/1 | `fe80::1` | N/A |
| R2 | S0/0/0 | `2001:db8:1:2::1/64` | N/A |
| R2 | S0/0/1 | `2001:db8:1:3::1/64` | N/A |
| R2 | S0/0/1 | `fe80::2` | N/A |
| R3 | G0/0 | `2001:db8:1:4::1/64` | N/A |
| R3 | S0/0/1 | `2001:db8:1:3::2/64` | N/A |
| R3 | S0/0/1 | `fe80::3` | N/A |
| PC1 | NIC | `2001:db8:1:1::a/64` | `fe80::1` |
| PC2 | NIC | `2001:db8:1:4::a/64` | `fe80::3` |

> **Lưu ý:** IPv6 default gateway trên PC thường là địa chỉ link-local của router cùng LAN. Vì vậy `PC1` dùng `fe80::1`, còn `PC2` dùng `fe80::3`.

## 4. Part 1: Complete the Addressing Table Documentation

### Step 1: Use `ipconfig /all` to verify IPv4 addressing

Trên `PC1`:

```text
PC> ipconfig /all

IPv4 Address......................: 10.10.1.126
Subnet Mask.......................: 255.255.255.224
Default Gateway...................: 10.10.1.97
```

![PC1 IPv4 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc1-ipconfig-ipv4.png)

Trên `PC2`:

```text
PC> ipconfig /all

IPv4 Address......................: 10.10.1.20
Subnet Mask.......................: 255.255.255.240
Default Gateway...................: 10.10.1.17
```

![PC2 IPv4 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc2-ipconfig-ipv4.png)

| PC | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `10.10.1.126` | `255.255.255.224` | `10.10.1.97` |
| PC2 | `10.10.1.20` | `255.255.255.240` | `10.10.1.17` |

### Step 2: Use `ipv6config /all` to verify IPv6 addressing

Trên `PC1`:

```text
PC> ipv6config /all

IPv6 Address......................: 2001:db8:1:1::a/64
Default Gateway...................: fe80::1
```

Trên `PC2`:

```text
PC> ipv6config /all

IPv6 Address......................: 2001:db8:1:4::a/64
Default Gateway...................: fe80::3
```



| PC | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- |
| PC1 | `2001:db8:1:1::a/64` | `fe80::1` |
| PC2 | `2001:db8:1:4::a/64` | `fe80::3` |


![PC2 IPv6 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/pc2-ipv6config.png)

## 5. Part 2: Test Connectivity Using Ping

### Step 1: Use `ping` to verify IPv4 connectivity

Từ `PC1` ping đến IPv4 của `PC2`:

```text
PC> ping 10.10.1.20

Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
Reply from 10.10.1.20: bytes=32 time<1ms TTL=125
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC1 ping IPv4 đến PC2 thành công. |

![Ping IPv4 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/ping-ipv4-pc1-to-pc2.png)

Từ `PC2` ping đến IPv4 của `PC1`:

```text
PC> ping 10.10.1.126

Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
Reply from 10.10.1.126: bytes=32 time<1ms TTL=125
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC2 ping IPv4 đến PC1 thành công. |
### Step 2: Use `ping` to verify IPv6 connectivity

Từ `PC1` ping đến IPv6 của `PC2`:

```text
PC> ping 2001:db8:1:4::a

Reply from 2001:DB8:1:4::A: time<1ms
Reply from 2001:DB8:1:4::A: time<1ms
Reply from 2001:DB8:1:4::A: time<1ms
Reply from 2001:DB8:1:4::A: time<1ms
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC1 ping IPv6 đến PC2 thành công. |

Từ `PC2` ping đến IPv6 của `PC1`:

```text
PC> ping 2001:db8:1:1::a

Reply from 2001:DB8:1:1::A: time<1ms
Reply from 2001:DB8:1:1::A: time<1ms
Reply from 2001:DB8:1:1::A: time<1ms
Reply from 2001:DB8:1:1::A: time<1ms
```

| Câu hỏi | Trả lời |
| --- | --- |
| Was the result successful? | Có. PC2 ping IPv6 đến PC1 thành công. |

![Ping IPv6 test](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/ping-ipv6.png)

## 6. Part 3: Discover the Path by Tracing the Route

### Step 1: Use `tracert` to discover the IPv4 path

Từ `PC1` trace route đến `PC2`:

```text
PC> tracert 10.10.1.20

1   10.10.1.97
2   10.10.1.5
3   10.10.1.10
4   10.10.1.20
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `10.10.1.97` | R1 `G0/0` |
| 2 | `10.10.1.5` | R2 `S0/0/0` |
| 3 | `10.10.1.10` | R3 `S0/0/1` |
| 4 | `10.10.1.20` | PC2 `NIC` |

![Traceroute IPv4 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv4-pc1-to-pc2.png)

Từ `PC2` trace route đến `PC1`:

```text
PC> tracert 10.10.1.126

1   10.10.1.17
2   10.10.1.9
3   10.10.1.6
4   10.10.1.126
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `10.10.1.17` | R3 `G0/0` |
| 2 | `10.10.1.9` | R2 `S0/0/1` |
| 3 | `10.10.1.6` | R1 `S0/0/1` |
| 4 | `10.10.1.126` | PC1 `NIC` |


> **Lưu ý:** `tracert` hiển thị từng hop mà gói tin đi qua. Hop đầu tiên thường là default gateway của PC nguồn. Hop cuối cùng là thiết bị đích.

### Step 2: Use `tracert` to discover the IPv6 path

Từ `PC1` trace route đến IPv6 của `PC2`:

```text
PC> tracert 2001:db8:1:4::a

1   2001:db8:1:1::1
2   2001:db8:1:2::1
3   2001:db8:1:3::2
4   2001:db8:1:4::a
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `2001:db8:1:1::1` | R1 `G0/0` |
| 2 | `2001:db8:1:2::1` | R2 `S0/0/0` |
| 3 | `2001:db8:1:3::2` | R3 `S0/0/1` |
| 4 | `2001:db8:1:4::a` | PC2 `NIC` |

![Traceroute IPv6 PC1 to PC2](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv6-pc1-to-pc2.png)

Từ `PC2` trace route đến IPv6 của `PC1`:

```text
PC> tracert 2001:db8:1:1::a

1   2001:db8:1:4::1
2   2001:db8:1:3::1
3   2001:db8:1:2::2
4   2001:db8:1:1::a
```

| Hop | Địa chỉ gặp trên đường đi | Interface tương ứng |
| --- | --- | --- |
| 1 | `2001:db8:1:4::1` | R3 `G0/0` |
| 2 | `2001:db8:1:3::1` | R2 `S0/0/1` |
| 3 | `2001:db8:1:2::2` | R1 `S0/0/1` |
| 4 | `2001:db8:1:1::a` | PC1 `NIC` |

![Traceroute IPv6 PC2 to PC1](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-07/tracert-ipv6-pc2-to-pc1.png)

> **Lưu ý:** Với IPv6, địa chỉ trong kết quả `tracert` là địa chỉ global unicast của từng interface. Default gateway IPv6 trên PC có thể là link-local, nhưng khi trace route, router thường trả lời bằng địa chỉ global unicast của interface liên quan.

## 7. Bảng Tổng Hợp Đường Đi

| Kiểm tra | Đường đi |
| --- | --- |
| IPv4 PC1 → PC2 | PC1 → R1 G0/0 `10.10.1.97` → R2 S0/0/0 `10.10.1.5` → R3 S0/0/1 `10.10.1.10` → PC2 `10.10.1.20` |
| IPv4 PC2 → PC1 | PC2 → R3 G0/0 `10.10.1.17` → R2 S0/0/1 `10.10.1.9` → R1 S0/0/1 `10.10.1.6` → PC1 `10.10.1.126` |
| IPv6 PC1 → PC2 | PC1 → R1 G0/0 `2001:db8:1:1::1` → R2 S0/0/0 `2001:db8:1:2::1` → R3 S0/0/1 `2001:db8:1:3::2` → PC2 `2001:db8:1:4::a` |
| IPv6 PC2 → PC1 | PC2 → R3 G0/0 `2001:db8:1:4::1` → R2 S0/0/1 `2001:db8:1:3::1` → R1 S0/0/1 `2001:db8:1:2::2` → PC1 `2001:db8:1:1::a` |

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không ping được IPv4 | Sai IPv4 address, subnet mask hoặc default gateway trên PC | Kiểm tra lại bằng `ipconfig /all` |
| Ping IPv4 được nhưng IPv6 không được | Sai IPv6 address hoặc IPv6 default gateway | Kiểm tra lại bằng `ipv6config /all` |
| Nhầm gateway PC1 | PC1 thuộc mạng `10.10.1.96/27` | Gateway IPv4 đúng là `10.10.1.97` |
| Nhầm gateway PC2 | PC2 thuộc mạng `10.10.1.16/28` | Gateway IPv4 đúng là `10.10.1.17` |
| Ghi sai hop trong `tracert` | Nhầm chiều đi PC1→PC2 và PC2→PC1 | Đối chiếu theo bảng tổng hợp đường đi |
| Nhầm IPv6 link-local với global unicast | Default gateway có thể là `fe80::`, nhưng `tracert` thường hiện global unicast | Ghi đúng loại địa chỉ theo từng mục kiểm tra |

## 9. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| Addressing Table PC1 | Hoàn thiện IPv4 `10.10.1.126/27`, IPv6 `2001:db8:1:1::a/64` |
| Addressing Table PC2 | Hoàn thiện IPv4 `10.10.1.20/28`, IPv6 `2001:db8:1:4::a/64` |
| Ping IPv4 PC1 ↔ PC2 | Thành công hai chiều |
| Ping IPv6 PC1 ↔ PC2 | Thành công hai chiều |
| Tracert IPv4 | Xác định đúng đường đi qua R1, R2, R3 |
| Tracert IPv6 | Xác định đúng đường đi qua R1, R2, R3 |
| Mapping interface | Mỗi hop được gắn đúng với interface tương ứng |
| Trạng thái lab | Hoàn thành |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 6</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span style="padding: 0.5rem 1rem; display: inline-block;">Hoàn thành nhóm lab</span></div>
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

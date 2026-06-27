---
layout: page-toc
title: "CCNA 10.03 - 16.3.1 Packet Tracer - Troubleshoot Static and Default Routes"
permalink: /writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-03/
toc: true
---

[← Quay lại danh sách Static Và Default Routing](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/)

| Field | Value |
| --- | --- |
| Dạng lab | Static Và Default Routing |
| File lab | `16.3.1 Packet Tracer - Troubleshoot Static and Default Routes.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Troubleshoot static/default route IPv4 + IPv6 để PC1, PC2 và Server thông nhau |

> **Ghi chú:** Bài này không phải dựng topology từ đầu. Các thiết bị đã có cấu hình sẵn nhưng có lỗi ở static/default route. Mục tiêu là kiểm tra bảng định tuyến, xác định route sai và sửa đúng theo addressing table.

## 1. Mục Tiêu Bài Lab

- Kiểm tra địa chỉ IPv4/IPv6 trên R1, R2, R3 và các host.
- Xác định lỗi static route/default route làm các LAN không thông nhau.
- Sửa static route IPv4 cho LAN 1, LAN 2, LAN 3.
- Sửa default route IPv4 trên router biên LAN.
- Sửa static route IPv6 và default route IPv6.
- Kiểm tra end-to-end connectivity giữa PC1, PC2 và Server.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/topology.png)

## 2. Bảng Địa Chỉ IP

### IPv4 Addressing Table

| Thiết bị | Interface | IPv4 / Prefix | Vai trò |
| --- | --- | --- | --- |
| R1 | G0/0 | `172.31.1.1/25` | Default gateway LAN 1 |
| R1 | S0/0/0 | `172.31.1.194/30` | Link R1 ↔ R2 |
| R2 | G0/0 | `172.31.0.1/24` | Default gateway LAN 2 |
| R2 | S0/0/0 | `172.31.1.193/30` | Link R2 ↔ R1 |
| R2 | S0/0/1 | `172.31.1.197/30` | Link R2 ↔ R3 |
| R3 | G0/0 | `172.31.1.129/26` | Default gateway LAN 3 |
| R3 | S0/0/1 | `172.31.1.198/30` | Link R3 ↔ R2 |
| PC1 | NIC | `172.31.1.126/25` | Host LAN 1 |
| PC2 | NIC | `172.31.0.254/24` | Host LAN 2 |
| Server | NIC | `172.31.1.190/26` | Host LAN 3 |

> **Lưu ý:** LAN 1 là `172.31.1.0/25`, LAN 2 là `172.31.0.0/24`, LAN 3 là `172.31.1.128/26`. Hai mạng serial là `172.31.1.192/30` và `172.31.1.196/30`.

### IPv6 Addressing Table

| Thiết bị | Interface | IPv6 / Prefix | Vai trò |
| --- | --- | --- | --- |
| R1 | G0/0 | `2001:DB8:1::1/64` | Gateway IPv6 LAN 1 |
| R1 | S0/0/0 | `2001:DB8:2::194/64` | Link R1 ↔ R2 |
| R2 | G0/0 | `2001:DB8:3::1/64` | Gateway IPv6 LAN 2 |
| R2 | S0/0/0 | `2001:DB8:2::193/64` | Link R2 ↔ R1 |
| R2 | S0/0/1 | `2001:DB8:4::197/64` | Link R2 ↔ R3 |
| R3 | G0/0 | `2001:DB8:5::1/64` | Gateway IPv6 LAN 3 |
| R3 | S0/0/1 | `2001:DB8:4::198/64` | Link R3 ↔ R2 |
| PC1 | NIC | `2001:DB8:1::126/64` | Host LAN 1 |
| PC2 | NIC | `2001:DB8:3::254/64` | Host LAN 2 |
| Server | NIC | `2001:DB8:5::190/64` | Host LAN 3 |

> **Lưu ý:** Trên router Cisco, muốn định tuyến IPv6 phải có `ipv6 unicast-routing`. Thiếu lệnh này thì router có địa chỉ IPv6 nhưng không route IPv6 giữa các mạng.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 1 | PC1, S1, R1 G0/0 | IPv4 dùng `/25`, IPv6 dùng `2001:DB8:1::/64` |
| LAN 2 | PC2, S2, R2 G0/0 | IPv4 dùng `172.31.0.0/24`, IPv6 dùng `2001:DB8:3::/64` |
| LAN 3 | Server, S3, R3 G0/0 | IPv4 dùng `/26`, IPv6 dùng `2001:DB8:5::/64` |
| WAN R1-R2 | R1 S0/0/0, R2 S0/0/0 | IPv4 `172.31.1.192/30`, IPv6 `2001:DB8:2::/64` |
| WAN R2-R3 | R2 S0/0/1, R3 S0/0/1 | IPv4 `172.31.1.196/30`, IPv6 `2001:DB8:4::/64` |

> **Điểm dễ sai:** LAN 1 và LAN 3 đều nằm trong dải `172.31.1.x`, nhưng subnet mask khác nhau. LAN 1 là `/25`, LAN 3 là `/26`, nên khi viết static route phải dùng đúng subnet mask.

## 4. Part 1 - Locate And Document The Problems

### Step 1: Kiểm tra nhanh interface và route trên từng router

```text
R1> enable
Password: class
R1# show ip interface brief
R1# show ipv6 interface brief
R1# show ip route
R1# show ipv6 route
R1# show running-config | include ip route
R1# show running-config | include ipv6 route
```

```text
R2> enable
Password: class
R2# show ip interface brief
R2# show ipv6 interface brief
R2# show ip route
R2# show ipv6 route
R2# show running-config | include ip route
R2# show running-config | include ipv6 route
```

```text
R3> enable
Password: class
R3# show ip interface brief
R3# show ipv6 interface brief
R3# show ip route
R3# show ipv6 route
R3# show running-config | include ip route
R3# show running-config | include ipv6 route
```

> **Lưu ý:** Khi troubleshoot static route, không chỉ nhìn `show ip route`. Cần đối chiếu cả `show running-config | include ip route` vì có route sai cú pháp hoặc sai next-hop nhưng không xuất hiện trong routing table.

![Route check lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/route-check.png)

### Step 2: Documentation Table

| Location | Problem cần kiểm tra | Solution đúng |
| --- | --- | --- |
| R1 | Default route IPv4 không trỏ về R2 | `ip route 0.0.0.0 0.0.0.0 172.31.1.193` |
| R1 | Default route IPv6 không trỏ về R2 | `ipv6 route ::/0 2001:DB8:2::193` |
| R2 | Static route IPv4 tới LAN 1 sai network/mask/next-hop | `ip route 172.31.1.0 255.255.255.128 172.31.1.194` |
| R2 | Static route IPv4 tới LAN 3 sai network/mask/next-hop | `ip route 172.31.1.128 255.255.255.192 172.31.1.198` |
| R2 | Static route IPv6 tới LAN 1 sai next-hop | `ipv6 route 2001:DB8:1::/64 2001:DB8:2::194` |
| R2 | Static route IPv6 tới LAN 3 sai next-hop | `ipv6 route 2001:DB8:5::/64 2001:DB8:4::198` |
| R3 | Default route IPv4 không trỏ về R2 | `ip route 0.0.0.0 0.0.0.0 172.31.1.197` |
| R3 | Default route IPv6 không trỏ về R2 | `ipv6 route ::/0 2001:DB8:4::197` |

## 5. Part 2 - Implement The Solutions

### Step 1: Sửa route trên R1

```text
R1# configure terminal
R1(config)# ipv6 unicast-routing
R1(config)# ip route 0.0.0.0 0.0.0.0 172.31.1.193
R1(config)# ipv6 route ::/0 2001:DB8:2::193
R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** R1 chỉ có một đường đi ra ngoài qua R2, nên dùng default route là hợp lý nhất. Với IPv6, `::/0` tương đương default route.

### Step 2: Sửa route trên R2

```text
R2# configure terminal
R2(config)# ipv6 unicast-routing
R2(config)# ip route 172.31.1.0 255.255.255.128 172.31.1.194
R2(config)# ip route 172.31.1.128 255.255.255.192 172.31.1.198
R2(config)# ipv6 route 2001:DB8:1::/64 2001:DB8:2::194
R2(config)# ipv6 route 2001:DB8:5::/64 2001:DB8:4::198
R2(config)# end
R2# copy running-config startup-config
```

> **Lưu ý:** R2 là router trung tâm. R2 đã trực tiếp kết nối LAN 2 nên chỉ cần static route tới LAN 1 qua R1 và LAN 3 qua R3.

### Step 3: Sửa route trên R3

```text
R3# configure terminal
R3(config)# ipv6 unicast-routing
R3(config)# ip route 0.0.0.0 0.0.0.0 172.31.1.197
R3(config)# ipv6 route ::/0 2001:DB8:4::197
R3(config)# end
R3# copy running-config startup-config
```

> **Lưu ý:** R3 chỉ có một đường đi ra ngoài qua R2, nên dùng default route về R2 thay vì viết từng static route riêng lẻ.

### Step 4: Nếu trong cấu hình có route sai thì xóa route sai

```text
! Xem route đang bị cấu hình trong running-config
show running-config | include ip route
show running-config | include ipv6 route

! Xóa đúng dòng route sai đang thấy trong running-config
! no ip route <network-sai> <mask-sai> <next-hop-sai>
! no ipv6 route <prefix-sai> <next-hop-sai>
```

> **Lưu ý:** Không xóa route đúng. Chỉ xóa những dòng sai network, sai mask hoặc sai next-hop so với addressing table.

## 6. Part 3 - Verify Network Connectivity

### Step 1: Kiểm tra routing table IPv4

```text
R1# show ip route

! Kết quả cần thấy trên R1
S* 0.0.0.0/0 [1/0] via 172.31.1.193
```

```text
R2# show ip route

! Kết quả cần thấy trên R2
S 172.31.1.0/25 [1/0] via 172.31.1.194
S 172.31.1.128/26 [1/0] via 172.31.1.198
```

```text
R3# show ip route

! Kết quả cần thấy trên R3
S* 0.0.0.0/0 [1/0] via 172.31.1.197
```

![IPv4 route result lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/ipv4-route-result.png)

### Step 2: Kiểm tra routing table IPv6

```text
R1# show ipv6 route

! Kết quả cần thấy trên R1
S   ::/0 [1/0]
     via 2001:DB8:2::193
```

```text
R2# show ipv6 route

! Kết quả cần thấy trên R2
S   2001:DB8:1::/64 [1/0]
     via 2001:DB8:2::194
S   2001:DB8:5::/64 [1/0]
     via 2001:DB8:4::198
```

```text
R3# show ipv6 route

! Kết quả cần thấy trên R3
S   ::/0 [1/0]
     via 2001:DB8:4::197
```

![IPv6 route result lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/ipv6-route-result.png)

### Step 3: Ping kiểm tra IPv4 từ PC1

```text
PC1> ping 172.31.0.254
PC1> ping 172.31.1.190
```

| Lệnh kiểm tra | Kết quả mong muốn |
| --- | --- |
| `ping 172.31.0.254` | PC1 ping được PC2 |
| `ping 172.31.1.190` | PC1 ping được Server |

![PC1 IPv4 ping lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/pc1-ipv4-ping.png)

### Step 4: Ping kiểm tra IPv6 từ PC1

```text
PC1> ping 2001:DB8:3::254
PC1> ping 2001:DB8:5::190
```

| Lệnh kiểm tra | Kết quả mong muốn |
| --- | --- |
| `ping 2001:DB8:3::254` | PC1 ping được PC2 bằng IPv6 |
| `ping 2001:DB8:5::190` | PC1 ping được Server bằng IPv6 |

![PC1 IPv6 ping lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/pc1-ipv6-ping.png)

### Step 5: Ping kiểm tra ngược từ Server

```text
Server> ping 172.31.1.126
Server> ping 172.31.0.254
Server> ping 2001:DB8:1::126
Server> ping 2001:DB8:3::254
```

> **Lưu ý:** Ping một chiều thành công chưa đủ. Với static route, phải kiểm tra cả chiều đi và chiều về vì route hồi đáp sai cũng làm ping fail.

![Server ping result lab 03](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-03/server-ping-result.png)

## 7. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC1 ping PC2 fail | R1 thiếu default route hoặc R2 thiếu route về LAN 1 | Kiểm tra `show ip route` trên R1/R2 |
| PC1 ping Server fail | R2 thiếu static route tới LAN 3 hoặc R3 thiếu default route | Sửa route trên R2 và R3 |
| IPv4 chạy nhưng IPv6 fail | Thiếu `ipv6 unicast-routing` hoặc sai IPv6 next-hop | Bật IPv6 routing và sửa `ipv6 route` |
| Route không hiện trong routing table | Next-hop không reachable hoặc interface down | Kiểm tra `show ip interface brief` / `show ipv6 interface brief` |
| Route đúng nhưng ping vẫn fail | Default gateway host sai | Kiểm tra IP configuration trên PC/Server |
| Nhầm LAN 1 với LAN 3 | Cùng dải `172.31.1.x` nhưng mask khác nhau | Dùng đúng `/25` cho LAN 1 và `/26` cho LAN 3 |

## 8. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| R1 có default route IPv4 | `S* 0.0.0.0/0 via 172.31.1.193` |
| R1 có default route IPv6 | `S ::/0 via 2001:DB8:2::193` |
| R2 có route tới LAN 1 IPv4/IPv6 | Route đi qua R1 |
| R2 có route tới LAN 3 IPv4/IPv6 | Route đi qua R3 |
| R3 có default route IPv4 | `S* 0.0.0.0/0 via 172.31.1.197` |
| R3 có default route IPv6 | `S ::/0 via 2001:DB8:4::197` |
| PC1 ping PC2 | Thành công |
| PC1 ping Server | Thành công |
| PC1 ping PC2/Server bằng IPv6 | Thành công |

Checklist ảnh minh chứng:

- [ ] `topology.png`
- [ ] `route-check.png`
- [ ] `ipv4-route-result.png`
- [ ] `ipv6-route-result.png`
- [ ] `pc1-ipv4-ping.png`
- [ ] `pc1-ipv6-ping.png`
- [ ] `server-ping-result.png`
- [ ] `check-results.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 3 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-01/">Lab 1: 1.5.10 Packet Tracer - Verify Directly Connected Networks</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-02/">Lab 2: 15.6.1 Packet Tracer - Configure IPv4 and IPv6 Static and Default Routes</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 16.3.1 Packet Tracer - Troubleshoot Static and Default Routes (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

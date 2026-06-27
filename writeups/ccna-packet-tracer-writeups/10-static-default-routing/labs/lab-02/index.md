---
layout: page-toc
title: "CCNA 10.02 - 15.6.1 Packet Tracer - Configure IPv4 and IPv6 Static and Default Routes"
permalink: /writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-02/
toc: true
---

[← Quay lại danh sách Static Và Default Routing](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/)

| Field | Value |
| --- | --- |
| Dạng lab | Static Và Default Routing |
| File lab | `15.6.1 Packet Tracer - Configure IPv4 and IPv6 Static and Default Routes.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Cấu hình static route, default route, floating static route và host route cho IPv4/IPv6 |

> **Ghi chú:** Bài này không tập trung cấu hình IP trên interface. Các địa chỉ đã được cho sẵn trong topology, nhiệm vụ chính là thêm route tĩnh để LAN nội bộ đi ra Server qua ISP1, đồng thời có đường dự phòng qua ISP2 với administrative distance `5`.

## 1. Mục Tiêu Bài Lab

- Xác định đúng các mạng LAN nội bộ, mạng WAN và mạng Server.
- Cấu hình IPv4 default static route trên `Edge_Router` qua `ISP1`.
- Cấu hình IPv4 floating default route trên `Edge_Router` qua `ISP2`.
- Cấu hình IPv6 default static route và floating default route.
- Cấu hình static route từ `ISP1` quay về các LAN nội bộ.
- Cấu hình host route IPv4/IPv6 tới `Customer Server`.
- Kiểm tra routing table, ping và traceroute để xác nhận đường đi.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/topology.png)

## 2. Bảng Địa Chỉ IP

### 2.1. IPv4 Addressing

| Device | Interface | IPv4 Address/Prefix | Network | Ghi chú |
| --- | --- | --- | --- | --- |
| Edge_Router | S0/0/0 | `10.10.10.2/30` | `10.10.10.0/30` | Kết nối ISP1 |
| Edge_Router | S0/0/1 | `10.10.10.6/30` | `10.10.10.4/30` | Kết nối ISP2 |
| Edge_Router | G0/0 | `192.168.10.17/28` | `192.168.10.16/28` | Gateway LAN 1 |
| Edge_Router | G0/1 | `192.168.11.33/27` | `192.168.11.32/27` | Gateway LAN 2 |
| ISP1 | S0/0/0 | `10.10.10.1/30` | `10.10.10.0/30` | Primary ISP |
| ISP1 | G0/0 | `198.0.0.1/24` | `198.0.0.0/24` | ISP LAN |
| ISP2 | S0/0/1 | `10.10.10.5/30` | `10.10.10.4/30` | Backup ISP |
| ISP2 | G0/0 | `198.0.0.2/24` | `198.0.0.0/24` | ISP LAN |
| PC-A | NIC | `192.168.10.19/28` | `192.168.10.16/28` | LAN 1 |
| PC-B | NIC | `192.168.11.45/27` | `192.168.11.32/27` | LAN 2 |
| Customer Server | NIC | `198.0.0.10/24` | `198.0.0.0/24` | Server đích |

> **Lưu ý:** LAN 2 là `192.168.11.32/27`, nên host hợp lệ nằm trong khoảng `192.168.11.33 - 192.168.11.62`. Khi kiểm tra PC-B, cần bảo đảm địa chỉ PC nằm cùng subnet với gateway `192.168.11.33`.

### 2.2. IPv6 Addressing

| Device | Interface | IPv6 Address/Prefix | Network | Ghi chú |
| --- | --- | --- | --- | --- |
| Edge_Router | S0/0/0 | `2001:db8:a:1::2/64` | `2001:db8:a:1::/64` | Kết nối ISP1 |
| Edge_Router | S0/0/1 | `2001:db8:a:2::2/64` | `2001:db8:a:2::/64` | Kết nối ISP2 |
| Edge_Router | G0/0 | `2001:db8:1:10::1/64` | `2001:db8:1:10::/64` | Gateway IPv6 LAN 1 |
| Edge_Router | G0/1 | `2001:db8:1:11::1/64` | `2001:db8:1:11::/64` | Gateway IPv6 LAN 2 |
| ISP1 | S0/0/0 | `2001:db8:a:1::1/64` | `2001:db8:a:1::/64` | Primary ISP |
| ISP1 | G0/0 | `2001:db8:f:f::1/64` | `2001:db8:f:f::/64` | ISP LAN |
| ISP2 | S0/0/1 | `2001:db8:a:2::1/64` | `2001:db8:a:2::/64` | Backup ISP |
| ISP2 | G0/0 | `2001:db8:f:f::2/64` | `2001:db8:f:f::/64` | ISP LAN |
| PC-A | NIC | `2001:db8:1:10::19/64` | `2001:db8:1:10::/64` | LAN 1 |
| PC-B | NIC | `2001:db8:1:11::45/64` | `2001:db8:1:11::/64` | LAN 2 |
| Customer Server | NIC | `2001:db8:f:f::10/64` | `2001:db8:f:f::/64` | Server đích |

> **Lưu ý:** IPv4 host route dùng `/32`; IPv6 host route dùng `/128`. Đây là route trỏ chính xác đến một host, không phải cả network.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Corporate Network | `Edge_Router`, `LAN_1`, `LAN_2`, `PC-A`, `PC-B` | Hai LAN nội bộ đi ra ISP qua Edge_Router |
| Primary WAN | `Edge_Router S0/0/0 ↔ ISP1 S0/0/0` | Đường chính cho default route |
| Backup WAN | `Edge_Router S0/0/1 ↔ ISP2 S0/0/1` | Đường dự phòng dùng AD `5` |
| ISP LAN | `ISP1`, `ISP2`, `Customer Server` | Mạng server `198.0.0.0/24` và `2001:db8:f:f::/64` |
| Server đích | `Customer Server` | Được truy cập bằng host route IPv4/IPv6 |

> **Điểm dễ sai:** Floating static route vẫn được cấu hình trong running-config nhưng không xuất hiện trong routing table khi route chính còn hoạt động.

## 4. Part 1 - Cấu Hình IPv4 Static Và Floating Default Routes

### 4.1. Cấu hình trên Edge_Router

```text
Edge_Router> enable
Edge_Router# configure terminal
!
! Default route IPv4 chính đi qua ISP1
Edge_Router(config)# ip route 0.0.0.0 0.0.0.0 serial0/0/0
!
! Floating default route IPv4 dự phòng đi qua ISP2, AD = 5
Edge_Router(config)# ip route 0.0.0.0 0.0.0.0 serial0/0/1 5
Edge_Router(config)# end
Edge_Router# copy running-config startup-config
```

> **Lưu ý:** Route có administrative distance nhỏ hơn sẽ được ưu tiên. Static route mặc định có AD `1`, floating route đặt AD `5` nên chỉ được dùng khi đường chính không còn hợp lệ.

### 4.2. Kiểm tra IPv4 default route

```text
Edge_Router# show ip route static
Edge_Router# show ip route 0.0.0.0
Edge_Router# ping 198.0.0.10
```

![Edge Router IPv4 default route](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/edge-ipv4-default-route.png)

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `show ip route static` | Có route `S* 0.0.0.0/0` qua `Serial0/0/0` |
| `ping 198.0.0.10` | Ping tới Customer Server thành công |
| Tắt đường ISP1 để test dự phòng | Route floating qua `Serial0/0/1` được dùng |

## 5. Part 2 - Cấu Hình IPv6 Static Và Floating Default Routes

### 5.1. Cấu hình trên Edge_Router

```text
Edge_Router> enable
Edge_Router# configure terminal
!
! Default route IPv6 chính đi qua ISP1 bằng next-hop
Edge_Router(config)# ipv6 route ::/0 2001:db8:a:1::1
!
! Floating default route IPv6 dự phòng đi qua ISP2, AD = 5
Edge_Router(config)# ipv6 route ::/0 2001:db8:a:2::1 5
Edge_Router(config)# end
Edge_Router# copy running-config startup-config
```

> **Lưu ý:** Với IPv6 static route, dùng next-hop global unicast giúp output `show ipv6 route` rõ ràng hơn và dễ kiểm tra hơn.

### 5.2. Kiểm tra IPv6 default route

```text
Edge_Router# show ipv6 route static
Edge_Router# ping 2001:db8:f:f::10
```

![Edge Router IPv6 default route](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/edge-ipv6-default-route.png)

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `show ipv6 route static` | Có route `S ::/0` qua `2001:db8:a:1::1` |
| `ping 2001:db8:f:f::10` | Ping IPv6 tới Customer Server thành công |
| Đường ISP1 bị down | Floating route qua `2001:db8:a:2::1` được chọn |

## 6. Part 3 - Cấu Hình IPv4 Static Và Floating Static Routes Tới LAN Nội Bộ

### 6.1. Cấu hình trên ISP1

```text
ISP1> enable
ISP1# configure terminal
!
! Static route chính từ ISP1 quay về LAN 1 qua Edge_Router
ISP1(config)# ip route 192.168.10.16 255.255.255.240 10.10.10.2
!
! Static route chính từ ISP1 quay về LAN 2 qua Edge_Router
ISP1(config)# ip route 192.168.11.32 255.255.255.224 10.10.10.2
!
! Floating static route dự phòng tới LAN 1 qua phía ISP2, AD = 5
ISP1(config)# ip route 192.168.10.16 255.255.255.240 gigabitethernet0/0 5
!
! Floating static route dự phòng tới LAN 2 qua phía ISP2, AD = 5
ISP1(config)# ip route 192.168.11.32 255.255.255.224 gigabitethernet0/0 5
ISP1(config)# end
ISP1# copy running-config startup-config
```

> **Lưu ý:** Đề yêu cầu floating route IPv4 dạng directly connected, nên dùng exit-interface `GigabitEthernet0/0`. Trong mạng thật, với cổng Ethernet multi-access thường nên dùng next-hop để tránh ARP không cần thiết.

### 6.2. Kiểm tra route IPv4 trên ISP1

```text
ISP1# show ip route static
ISP1# ping 192.168.10.19
ISP1# ping 192.168.11.45
```

![ISP1 IPv4 static routes](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/isp1-ipv4-static-routes.png)

| Route | Kết quả mong muốn |
| --- | --- |
| `192.168.10.16/28` | Đi chính qua `10.10.10.2` |
| `192.168.11.32/27` | Đi chính qua `10.10.10.2` |
| Floating route AD `5` | Chỉ dùng khi route chính mất |

## 7. Part 4 - Cấu Hình IPv6 Static Và Floating Static Routes Tới LAN Nội Bộ

### 7.1. Cấu hình trên ISP1

```text
ISP1> enable
ISP1# configure terminal
!
! Static route IPv6 chính tới LAN 1 qua Edge_Router
ISP1(config)# ipv6 route 2001:db8:1:10::/64 2001:db8:a:1::2
!
! Static route IPv6 chính tới LAN 2 qua Edge_Router
ISP1(config)# ipv6 route 2001:db8:1:11::/64 2001:db8:a:1::2
!
! Floating static route IPv6 tới LAN 1 qua ISP2, AD = 5
ISP1(config)# ipv6 route 2001:db8:1:10::/64 2001:db8:f:f::2 5
!
! Floating static route IPv6 tới LAN 2 qua ISP2, AD = 5
ISP1(config)# ipv6 route 2001:db8:1:11::/64 2001:db8:f:f::2 5
ISP1(config)# end
ISP1# copy running-config startup-config
```

### 7.2. Kiểm tra route IPv6 trên ISP1

```text
ISP1# show ipv6 route static
ISP1# ping 2001:db8:1:10::19
ISP1# ping 2001:db8:1:11::45
```

![ISP1 IPv6 static routes](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/isp1-ipv6-static-routes.png)

| Route | Kết quả mong muốn |
| --- | --- |
| `2001:db8:1:10::/64` | Đi chính qua `2001:db8:a:1::2` |
| `2001:db8:1:11::/64` | Đi chính qua `2001:db8:a:1::2` |
| Floating route AD `5` | Dự phòng qua `2001:db8:f:f::2` |

## 8. Part 5 - Cấu Hình Host Routes Tới Customer Server

### 8.1. IPv4 host route trên Edge_Router

```text
Edge_Router> enable
Edge_Router# configure terminal
!
! Host route IPv4 chính tới Customer Server qua ISP1
Edge_Router(config)# ip route 198.0.0.10 255.255.255.255 serial0/0/0
!
! Floating host route IPv4 tới Customer Server qua ISP2, AD = 5
Edge_Router(config)# ip route 198.0.0.10 255.255.255.255 serial0/0/1 5
Edge_Router(config)# end
Edge_Router# copy running-config startup-config
```

### 8.2. IPv6 host route trên Edge_Router

```text
Edge_Router> enable
Edge_Router# configure terminal
!
! Host route IPv6 chính tới Customer Server qua ISP1
Edge_Router(config)# ipv6 route 2001:db8:f:f::10/128 2001:db8:a:1::1
!
! Floating host route IPv6 tới Customer Server qua ISP2, AD = 5
Edge_Router(config)# ipv6 route 2001:db8:f:f::10/128 serial0/0/1 5
Edge_Router(config)# end
Edge_Router# copy running-config startup-config
```

> **Lưu ý:** Host route cụ thể hơn default route, nên khi truy cập đúng Server `198.0.0.10` hoặc `2001:db8:f:f::10`, router sẽ ưu tiên host route trước.

### 8.3. Kiểm tra host route

```text
Edge_Router# show ip route 198.0.0.10
Edge_Router# show ipv6 route 2001:db8:f:f::10
Edge_Router# ping 198.0.0.10
Edge_Router# ping 2001:db8:f:f::10
```

![Edge host routes](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/edge-host-routes.png)

## 9. Kiểm Tra Kết Nối Cuối Bài

```text
! Trên PC-A
ping 198.0.0.10
ping 2001:db8:f:f::10
tracert 198.0.0.10

! Trên PC-B
ping 198.0.0.10
ping 2001:db8:f:f::10
tracert 198.0.0.10

! Trên Edge_Router
show ip route static
show ipv6 route static
show running-config | include ip route|ipv6 route
```

![PC-A ping server](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/pca-ping-server.png)
![PC-B ping server](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/pcb-ping-server.png)
![Show static routes](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-02/show-static-routes.png)

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
| PC-A ping IPv4 Server | Thành công tới `198.0.0.10` | `pca-ping-server.png` |
| PC-B ping IPv4 Server | Thành công tới `198.0.0.10` | `pcb-ping-server.png` |
| PC-A ping IPv6 Server | Thành công tới `2001:db8:f:f::10` | `pca-ping-server.png` |
| PC-B ping IPv6 Server | Thành công tới `2001:db8:f:f::10` | `pcb-ping-server.png` |
| Edge_Router static route | Có default route và host route chính | `show-static-routes.png` |
| Floating route | Không ưu tiên khi route chính còn hoạt động | `show-static-routes.png` |

## 10. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC-A/PC-B không ping được Server | Thiếu default route trên Edge_Router | Cấu hình `ip route 0.0.0.0 0.0.0.0 s0/0/0` và `ipv6 route ::/0 ...` |
| Server reply không quay về LAN nội bộ | ISP1 thiếu route quay về `192.168.10.16/28`, `192.168.11.32/27` | Thêm static route trên ISP1 về next-hop Edge_Router |
| Floating route không xuất hiện trong `show ip route` | Route chính vẫn còn hoạt động | Kiểm tra bằng `show running-config`; floating chỉ active khi route chính down |
| Ping IPv6 fail nhưng IPv4 thành công | Thiếu IPv6 route hoặc sai prefix IPv6 | Kiểm tra `show ipv6 route static` và địa chỉ next-hop |
| PC-B không đi được gateway | PC-B đặt sai subnet IPv4 | Bảo đảm PC-B thuộc `192.168.11.32/27`, gateway là `192.168.11.33` |
| Host route không được ưu tiên | Sai mask `/32` hoặc `/128` | IPv4 dùng `255.255.255.255`, IPv6 dùng `/128` |
| Cấu hình đúng nhưng mất sau reload | Chưa lưu cấu hình | Chạy `copy running-config startup-config` trên các router đã cấu hình |

## 11. Kết Quả Cuối

| Hạng mục | Trạng thái mong muốn |
| --- | --- |
| IPv4 default route trên Edge_Router | Route chính qua ISP1, route dự phòng qua ISP2 |
| IPv6 default route trên Edge_Router | Route chính qua ISP1, route dự phòng qua ISP2 |
| IPv4 route từ ISP1 về LAN nội bộ | Có route tới LAN 1 và LAN 2 |
| IPv6 route từ ISP1 về LAN nội bộ | Có route tới LAN 1 và LAN 2 |
| Host route tới Customer Server | Có IPv4 `/32` và IPv6 `/128` |
| PC-A/PC-B truy cập Server | Ping IPv4 và IPv6 thành công |
| Cấu hình đã lưu | Đã chạy `copy running-config startup-config` |

- [ ] Chụp topology hoàn chỉnh: `topology.png`
- [ ] Chụp route IPv4 trên Edge_Router: `edge-ipv4-default-route.png`
- [ ] Chụp route IPv6 trên Edge_Router: `edge-ipv6-default-route.png`
- [ ] Chụp route IPv4 trên ISP1: `isp1-ipv4-static-routes.png`
- [ ] Chụp route IPv6 trên ISP1: `isp1-ipv6-static-routes.png`
- [ ] Chụp host routes trên Edge_Router: `edge-host-routes.png`
- [ ] Chụp PC-A ping Server: `pca-ping-server.png`
- [ ] Chụp PC-B ping Server: `pcb-ping-server.png`
- [ ] Chụp Check Results hoàn thành nếu có: `check-results.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 3 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-01/">Lab 1: 1.5.10 Packet Tracer - Verify Directly Connected Networks</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 15.6.1 Packet Tracer - Configure IPv4 and IPv6 Static and Default Routes (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-03/">Lab 3: 16.3.1 Packet Tracer - Troubleshoot Static and Default Routes</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 18.03 - 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Dùng ICMP `ping` và `trace/tracert` để khoanh vùng lỗi, sửa cấu hình sai và khôi phục kết nối end-to-end |

> **Ghi chú:** Đây là lab troubleshooting. Mục tiêu không phải cấu hình mới toàn bộ từ đầu, mà là dùng ICMP để xác định đoạn mạng bị lỗi, so sánh với bảng địa chỉ, sửa lỗi cấu hình và kiểm tra lại toàn mạng.

## 1. Mục Tiêu Bài Lab

- Kiểm tra kết nối giữa các host bằng ICMP `ping`.
- Dùng `tracert` trên PC hoặc `traceroute` trên router để tìm điểm dừng cuối cùng của gói tin.
- Đối chiếu địa chỉ IPv4/IPv6, subnet mask/prefix và default gateway với Addressing Table.
- Kiểm tra trạng thái interface và bảng định tuyến trên các router.
- Sửa lỗi cấu hình đơn giản làm mất kết nối mạng.
- Xác nhận tất cả host có thể truy cập các host khác và Corporate Server.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-03/topology.png)

## 2. Bảng Địa Chỉ IP

### 2.1. Router

| Device | Interface | IPv4 Address | Mask | IPv6 Address | Prefix |
| --- | --- | --- | --- | --- | --- |
| RTR-1 | G0/0/0 | 192.168.1.1 | 255.255.255.0 | 2001:db8:4::1 | /64 |
| RTR-1 | S0/1/0 | 10.10.2.2 | 255.255.255.252 | 2001:db8:2::2 | /126 |
| RTR-1 | S0/1/1 | 10.10.3.1 | 255.255.255.252 | 2001:db8:3::1 | /126 |
| RTR-2 | G0/0/0 | 10.10.1.1 | 255.255.255.0 | - | - |
| RTR-2 | G0/0/1 | - | - | 2001:db8:1::1 | /64 |
| RTR-2 | S0/1/0 | 10.10.2.1 | 255.255.255.252 | 2001:db8:2::1 | /126 |
| RTR-3 | G0/0/0 | 10.10.5.1 | 255.255.255.0 | - | - |
| RTR-3 | G0/0/1 | - | - | 2001:db8:5::1 | /64 |
| RTR-3 | S0/1/0 | 10.10.3.2 | 255.255.255.252 | 2001:db8:3::2 | /126 |

> **Lưu ý:** Một số LAN chỉ dùng IPv4, một số LAN chỉ dùng IPv6. Khi troubleshoot, cần kiểm tra đúng giao thức đang được dùng trên từng nhánh mạng.

### 2.2. End Devices

| Device | Interface | Address | Mask/Prefix | Default Gateway |
| --- | --- | --- | --- | --- |
| PC-1 | NIC | 10.10.1.10 | 255.255.255.0 | 10.10.1.1 |
| Laptop A | NIC | 10.10.1.20 | 255.255.255.0 | 10.10.1.1 |
| PC-2 | NIC | 2001:db8:1::10 | /64 | fe80::1 |
| PC-3 | NIC | 2001:db8:1::20 | /64 | fe80::1 |
| PC-4 | NIC | 10.10.5.10 | 255.255.255.0 | 10.10.5.1 |
| Server 1 | NIC | 10.10.5.20 | 255.255.255.0 | 10.10.5.1 |
| Laptop B | NIC | 2001:db8:5::10 | /64 | fe80::1 |
| Laptop C | NIC | 2001:db8:5::20 | /64 | fe80::1 |
| Corporate Server | NIC | 203.0.113.100 | 255.255.255.0 | 203.0.113.1 |
| Corporate Server | NIC | 2001:db8:acad::100 | /64 | fe80::1 |

> **Lưu ý:** Với IPv6, default gateway có thể là địa chỉ link-local `fe80::1`. Địa chỉ link-local chỉ có ý nghĩa trên cùng một liên kết cục bộ.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| IPv4 LAN bên trái | PC-1, Laptop A, SW-1, RTR-2 G0/0/0 | Mạng `10.10.1.0/24`, gateway là `10.10.1.1` |
| IPv6 LAN bên trái | PC-2, PC-3, SW-2, RTR-2 G0/0/1 | Mạng `2001:db8:1::/64`, gateway là `fe80::1` |
| WAN RTR-2 ↔ RTR-1 | RTR-2 S0/1/0, RTR-1 S0/1/0 | IPv4 `10.10.2.0/30`, IPv6 `2001:db8:2::/126` |
| WAN RTR-1 ↔ RTR-3 | RTR-1 S0/1/1, RTR-3 S0/1/0 | IPv4 `10.10.3.0/30`, IPv6 `2001:db8:3::/126` |
| IPv4 LAN bên phải | PC-4, Server 1, SW-3, RTR-3 G0/0/0 | Mạng `10.10.5.0/24`, gateway là `10.10.5.1` |
| IPv6 LAN bên phải | Laptop B, Laptop C, SW-4, RTR-3 G0/0/1 | Mạng `2001:db8:5::/64`, gateway là `fe80::1` |
| Corporate | RTR-1, Corporate Cloud, Corporate Server | Đích cần kiểm tra cuối cùng là `203.0.113.100` và `2001:db8:acad::100` |

> **Điểm dễ sai:** Nếu ping cùng LAN thành công nhưng ping khác LAN thất bại, lỗi thường nằm ở default gateway, route, hoặc interface WAN giữa các router.

## 4. Part 1 - Dùng ICMP Để Khoanh Vùng Lỗi

### 4.1. Kiểm tra thông tin IP trên host

```text
! Trên các PC IPv4
PC> ipconfig /all

! Trên các PC IPv6
PC> ipv6config /all
```

| Host | Kiểm tra | Giá trị đúng cần thấy |
| --- | --- | --- |
| PC-1 | IPv4 / Gateway | `10.10.1.10/24`, gateway `10.10.1.1` |
| Laptop A | IPv4 / Gateway | `10.10.1.20/24`, gateway `10.10.1.1` |
| PC-2 | IPv6 / Gateway | `2001:db8:1::10/64`, gateway `fe80::1` |
| PC-3 | IPv6 / Gateway | `2001:db8:1::20/64`, gateway `fe80::1` |
| PC-4 | IPv4 / Gateway | `10.10.5.10/24`, gateway `10.10.5.1` |
| Server 1 | IPv4 / Gateway | `10.10.5.20/24`, gateway `10.10.5.1` |
| Laptop B | IPv6 / Gateway | `2001:db8:5::10/64`, gateway `fe80::1` |
| Laptop C | IPv6 / Gateway | `2001:db8:5::20/64`, gateway `fe80::1` |

![Host addressing check](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-03/host-addressing-check.png)

### 4.2. Test local connectivity trước

```text
! IPv4 LAN bên trái
PC-1> ping 10.10.1.20

! IPv4 LAN bên phải
PC-4> ping 10.10.5.20

! IPv6 LAN bên trái
PC-2> ping 2001:db8:1::20

! IPv6 LAN bên phải
LaptopB> ping 2001:db8:5::20
```

| Test | Kết quả mong muốn | Nếu fail thì kiểm tra |
| --- | --- | --- |
| PC-1 → Laptop A | Reply thành công | IP, subnet mask, NIC, switch port |
| PC-4 → Server 1 | Reply thành công | IP, subnet mask, gateway local |
| PC-2 → PC-3 | Reply thành công | IPv6 address, prefix `/64` |
| Laptop B → Laptop C | Reply thành công | IPv6 address, gateway link-local |

> **Lưu ý:** Không nên kiểm tra remote trước khi local chưa ổn. Nếu local fail, lỗi chưa chắc nằm ở router.

### 4.3. Test default gateway

```text
! IPv4 gateway
PC-1> ping 10.10.1.1
PC-4> ping 10.10.5.1

! IPv6 gateway link-local hoặc global router interface
PC-2> ping 2001:db8:1::1
LaptopB> ping 2001:db8:5::1
```

![Gateway ping test](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-03/gateway-ping-test.png)

### 4.4. Test end-to-end connectivity

```text
! IPv4 end-to-end
PC-1> ping 10.10.5.10
PC-1> ping 10.10.5.20
PC-1> ping 203.0.113.100

! IPv6 end-to-end
PC-2> ping 2001:db8:5::10
PC-2> ping 2001:db8:5::20
PC-2> ping 2001:db8:acad::100
```

| Test | Mục đích |
| --- | --- |
| PC-1 → PC-4 | Kiểm tra IPv4 routing từ nhánh RTR-2 sang RTR-3 |
| PC-1 → Corporate Server | Kiểm tra IPv4 đi qua RTR-1 tới Corporate |
| PC-2 → Laptop B | Kiểm tra IPv6 routing từ nhánh RTR-2 sang RTR-3 |
| PC-2 → Corporate Server | Kiểm tra IPv6 đi tới Corporate |

## 5. Part 2 - Dùng Trace Để Xác Định Điểm Đứt

### 5.1. Trace IPv4

```text
! Trên PC-1, tìm đường tới mạng IPv4 bên RTR-3
PC-1> tracert 10.10.5.10

! Trên PC-4, tìm đường ngược về mạng IPv4 bên RTR-2
PC-4> tracert 10.10.1.10
```

| Trace | Hop đúng thường gặp |
| --- | --- |
| PC-1 → PC-4 | `10.10.1.1` → `10.10.2.2` → `10.10.3.2` → `10.10.5.10` |
| PC-4 → PC-1 | `10.10.5.1` → `10.10.3.1` → `10.10.2.1` → `10.10.1.10` |

> **Lưu ý:** Hop cuối cùng thành công cho biết gói tin đi được tới đâu. Hop sau đó fail thường là nơi cần kiểm tra interface hoặc route kế tiếp.

### 5.2. Trace IPv6

```text
! Trên PC-2, trace tới IPv6 LAN bên RTR-3
PC-2> tracert 2001:db8:5::10

! Trên Laptop B, trace ngược về IPv6 LAN bên RTR-2
LaptopB> tracert 2001:db8:1::10
```

| Trace | Hop đúng thường gặp |
| --- | --- |
| PC-2 → Laptop B | `2001:db8:1::1` → `2001:db8:2::2` → `2001:db8:3::2` → `2001:db8:5::10` |
| Laptop B → PC-2 | `2001:db8:5::1` → `2001:db8:3::1` → `2001:db8:2::1` → `2001:db8:1::10` |

![Traceroute result](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-03/traceroute-result.png)

## 6. Part 3 - Kiểm Tra Router Bằng Show Commands

### 6.1. Kiểm tra interface trên RTR-1

```text
RTR-1> enable
Password: class
RTR-1# show ip interface brief
RTR-1# show ipv6 interface brief
RTR-1# show ip route
RTR-1# show ipv6 route
```

| Interface | Giá trị đúng cần thấy |
| --- | --- |
| G0/0/0 | IPv4 `192.168.1.1`, IPv6 `2001:db8:4::1`, trạng thái `up/up` |
| S0/1/0 | IPv4 `10.10.2.2`, IPv6 `2001:db8:2::2`, trạng thái `up/up` |
| S0/1/1 | IPv4 `10.10.3.1`, IPv6 `2001:db8:3::1`, trạng thái `up/up` |

### 6.2. Kiểm tra interface trên RTR-2

```text
RTR-2> enable
Password: class
RTR-2# show ip interface brief
RTR-2# show ipv6 interface brief
RTR-2# show ip route
RTR-2# show ipv6 route
```

| Interface | Giá trị đúng cần thấy |
| --- | --- |
| G0/0/0 | IPv4 `10.10.1.1`, trạng thái `up/up` |
| G0/0/1 | IPv6 `2001:db8:1::1`, trạng thái `up/up` |
| S0/1/0 | IPv4 `10.10.2.1`, IPv6 `2001:db8:2::1`, trạng thái `up/up` |

### 6.3. Kiểm tra interface trên RTR-3

```text
RTR-3> enable
Password: class
RTR-3# show ip interface brief
RTR-3# show ipv6 interface brief
RTR-3# show ip route
RTR-3# show ipv6 route
```

| Interface | Giá trị đúng cần thấy |
| --- | --- |
| G0/0/0 | IPv4 `10.10.5.1`, trạng thái `up/up` |
| G0/0/1 | IPv6 `2001:db8:5::1`, trạng thái `up/up` |
| S0/1/0 | IPv4 `10.10.3.2`, IPv6 `2001:db8:3::2`, trạng thái `up/up` |

> **Lưu ý:** Nếu interface hiển thị `administratively down`, cần vào interface đó và dùng lệnh `no shutdown`.

## 7. Part 4 - Cấu Hình Chuẩn Để Đối Chiếu Khi Sửa Lỗi

> **Lưu ý:** Trong Packet Tracer này, không nhất thiết phải nhập lại toàn bộ cấu hình. Dùng các block bên dưới để đối chiếu và sửa đúng phần đang sai.

### 7.1. RTR-1

```text
enable
configure terminal
hostname RTR-1
ipv6 unicast-routing

interface g0/0/0
 description Link to Corporate network
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:4::1/64
 no shutdown
 exit

interface s0/1/0
 description Link to RTR-2
 ip address 10.10.2.2 255.255.255.252
 ipv6 address 2001:db8:2::2/126
 no shutdown
 exit

interface s0/1/1
 description Link to RTR-3
 ip address 10.10.3.1 255.255.255.252
 ipv6 address 2001:db8:3::1/126
 no shutdown
 exit

! Route về các LAN IPv4 phía RTR-2 và RTR-3 nếu bị thiếu
ip route 10.10.1.0 255.255.255.0 10.10.2.1
ip route 10.10.5.0 255.255.255.0 10.10.3.2

! Route về các LAN IPv6 phía RTR-2 và RTR-3 nếu bị thiếu
ipv6 route 2001:db8:1::/64 2001:db8:2::1
ipv6 route 2001:db8:5::/64 2001:db8:3::2

end
copy running-config startup-config
```

### 7.2. RTR-2

```text
enable
configure terminal
hostname RTR-2
ipv6 unicast-routing

interface g0/0/0
 description IPv4 LAN - PC-1 and Laptop A
 ip address 10.10.1.1 255.255.255.0
 no shutdown
 exit

interface g0/0/1
 description IPv6 LAN - PC-2 and PC-3
 ipv6 address 2001:db8:1::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit

interface s0/1/0
 description Link to RTR-1
 ip address 10.10.2.1 255.255.255.252
 ipv6 address 2001:db8:2::1/126
 no shutdown
 exit

! Route mặc định về RTR-1 nếu bị thiếu
ip route 0.0.0.0 0.0.0.0 10.10.2.2
ipv6 route ::/0 2001:db8:2::2

end
copy running-config startup-config
```

### 7.3. RTR-3

```text
enable
configure terminal
hostname RTR-3
ipv6 unicast-routing

interface g0/0/0
 description IPv4 LAN - PC-4 and Server 1
 ip address 10.10.5.1 255.255.255.0
 no shutdown
 exit

interface g0/0/1
 description IPv6 LAN - Laptop B and Laptop C
 ipv6 address 2001:db8:5::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit

interface s0/1/0
 description Link to RTR-1
 ip address 10.10.3.2 255.255.255.252
 ipv6 address 2001:db8:3::2/126
 no shutdown
 exit

! Route mặc định về RTR-1 nếu bị thiếu
ip route 0.0.0.0 0.0.0.0 10.10.3.1
ipv6 route ::/0 2001:db8:3::1

end
copy running-config startup-config
```

### 7.4. Cấu hình IP trên host

| Host | IPv4/IPv6 | Gateway |
| --- | --- | --- |
| PC-1 | `10.10.1.10 / 255.255.255.0` | `10.10.1.1` |
| Laptop A | `10.10.1.20 / 255.255.255.0` | `10.10.1.1` |
| PC-2 | `2001:db8:1::10/64` | `fe80::1` |
| PC-3 | `2001:db8:1::20/64` | `fe80::1` |
| PC-4 | `10.10.5.10 / 255.255.255.0` | `10.10.5.1` |
| Server 1 | `10.10.5.20 / 255.255.255.0` | `10.10.5.1` |
| Laptop B | `2001:db8:5::10/64` | `fe80::1` |
| Laptop C | `2001:db8:5::20/64` | `fe80::1` |

![PC IP configuration](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-03/pc-ip-configuration.png)

## 8. Documentation Table

| Vị trí | Dấu hiệu lỗi | Cách kiểm tra | Cách sửa |
| --- | --- | --- | --- |
| Host IPv4 | Ping cùng LAN fail | `ipconfig /all` | Sửa IP, mask hoặc default gateway |
| Host IPv6 | Ping cùng LAN IPv6 fail | `ipv6config /all` | Sửa IPv6 address, prefix hoặc gateway `fe80::1` |
| Router interface | Trace dừng ở router trước đó | `show ip interface brief`, `show ipv6 interface brief` | Sửa IP/prefix hoặc `no shutdown` |
| Router route | Ping gateway được nhưng ping remote fail | `show ip route`, `show ipv6 route` | Thêm hoặc sửa static/default route |
| WAN link | Hai router kề nhau không ping được | Ping IP serial đối diện | Sửa IP WAN, prefix `/30` hoặc `/126`, bật interface |
| Corporate Server | LAN ping nhau được nhưng không tới server | Ping/tracert tới `203.0.113.100` hoặc `2001:db8:acad::100` | Kiểm tra route về Corporate và gateway server |

## 9. Kiểm Tra Và Bằng Chứng

```text
! Kiểm tra IPv4 từ LAN trái sang LAN phải
PC-1> ping 10.10.5.10
PC-1> ping 10.10.5.20

! Kiểm tra IPv6 từ LAN trái sang LAN phải
PC-2> ping 2001:db8:5::10
PC-2> ping 2001:db8:5::20

! Kiểm tra tới Corporate Server
PC-1> ping 203.0.113.100
PC-2> ping 2001:db8:acad::100

! Trace kiểm tra đường đi
PC-1> tracert 10.10.5.10
PC-2> tracert 2001:db8:5::10
```

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
| Local IPv4 LAN | PC-1 ping Laptop A thành công | `local-ipv4-ping.png` |
| Local IPv6 LAN | PC-2 ping PC-3 thành công | `local-ipv6-ping.png` |
| Remote IPv4 | PC-1 ping PC-4/Server 1 thành công | `remote-ipv4-ping.png` |
| Remote IPv6 | PC-2 ping Laptop B/Laptop C thành công | `remote-ipv6-ping.png` |
| Corporate IPv4 | Ping `203.0.113.100` thành công | `corporate-ipv4-ping.png` |
| Corporate IPv6 | Ping `2001:db8:acad::100` thành công | `corporate-ipv6-ping.png` |
| Router status | Interface liên quan đều `up/up` | `router-show-brief.png` |

## 10. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Ping cùng LAN fail | Host sai IP/mask | `ipconfig /all` | Sửa lại đúng Addressing Table |
| Ping gateway fail | Router LAN interface shutdown hoặc sai IP | `show ip interface brief` | Sửa IP và `no shutdown` |
| Ping khác LAN fail | Thiếu route hoặc route sai next-hop | `show ip route` | Sửa static/default route |
| IPv6 ping fail dù IPv4 chạy | Chưa bật `ipv6 unicast-routing` | `show running-config` | Thêm `ipv6 unicast-routing` |
| IPv6 gateway sai | Host dùng sai link-local gateway | `ipv6config /all` | Sửa gateway thành `fe80::1` |
| Trace dừng ở router giữa | Router thiếu đường đi tiếp | `tracert`, `show ip route` | Thêm route tới mạng đích |
| Interface serial không hoạt động | Sai IP/prefix hoặc port down | `show interfaces serial ...` | Sửa IP, prefix và bật cổng |

## 11. Kết Quả Cuối

| Hạng mục | Trạng thái mong muốn |
| --- | --- |
| Host cùng LAN ping nhau | Thành công |
| Host khác LAN ping nhau | Thành công |
| Host truy cập Corporate Server | Thành công |
| Router interface | Đúng IP/IPv6 và `up/up` |
| Bảng route IPv4 | Có route tới các mạng remote cần thiết |
| Bảng route IPv6 | Có route tới các prefix remote cần thiết |
| Check Results | Đạt yêu cầu sau khi sửa toàn bộ lỗi |

Checklist ảnh minh chứng:

- [ ] `topology.png`
- [ ] `host-addressing-check.png`
- [ ] `gateway-ping-test.png`
- [ ] `traceroute-result.png`
- [ ] `router-show-brief.png`
- [ ] `remote-ipv4-ping.png`
- [ ] `remote-ipv6-ping.png`
- [ ] `corporate-ipv4-ping.png`
- [ ] `corporate-ipv6-ping.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/">Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/">Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/">Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/">Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/">Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge</a></li>
    </ul>
  </details>
</div>

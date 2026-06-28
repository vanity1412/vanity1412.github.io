---
layout: page-toc
title: "CCNA 18.06 - 17.8.3 Packet Tracer - Troubleshooting Challenge"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `17.8.3 Packet Tracer - Troubleshooting Challenge.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-06/` |
| Trạng thái | Hoàn tất checklist xử lý sự cố IPv4, IPv6, SSH và truy cập Web Server |

> **Đặc điểm bài:** Đây là bài troubleshooting tổng hợp. Thiết bị đã được cấu hình trước nhưng có một số lỗi sai sau khi cập nhật mạng. Mục tiêu là kiểm tra từng lớp kết nối, sửa cấu hình sai và xác nhận toàn bộ PC truy cập được Web server, R1 và switch management.

## 1. Mục Tiêu Bài Lab

- Kiểm tra kết nối IPv4 và IPv6 từ các PC nội bộ đến Web server.
- Xác minh địa chỉ IP, subnet mask/prefix, default gateway và link-local gateway.
- Kiểm tra kết nối từ các PC đến R1 và các switch quản trị S1/S2/S3.
- Kiểm tra SSH từ các PC vào R1 bằng tài khoản quản trị đã cho.
- Ghi lại lỗi, nguyên nhân, cách phát hiện và cấu hình sửa lỗi.

![Topology lab 06](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-06/topology.png)

## 2. Topology Và Quan Sát Ban Đầu

| Khu vực | Thiết bị | Mạng IPv4 | Mạng IPv6 | Nhận xét |
| --- | --- | --- | --- | --- |
| IT | IT, S1, R1 G0/0 | `172.16.1.0/26` | `2001:db8:cafe::/64` | Gateway IPv4 là `172.16.1.62`, gateway IPv6 là `fe80::1` |
| Marketing | Marketing, S2, R1 G0/1 | `172.16.1.64/26` | `2001:db8:cafe:1::/64` | Gateway IPv4 là `172.16.1.126`, gateway IPv6 là `fe80::1` |
| R&D | R&D, S3, R1 G0/2 | `172.16.1.128/25` | `2001:db8:cafe:2::/64` | Gateway IPv4 là `172.16.1.254`, gateway IPv6 là `fe80::1` |
| WAN nội bộ | R1 ↔ Main | `10.0.0.0/30` | `2001:db8:2::/64` | R1 đi ra ngoài qua Main |
| WAN Internet | Main ↔ ISP | `209.165.200.224/30` | `2001:db8:1::/64` | Main kết nối về ISP/Internet |
| Server | Web | `64.100.0.3/29` | `2001:db8:acad::3/64` | Đích kiểm tra cuối cùng |

> **Lưu ý:** Các mạng IPv4 nội bộ được chia theo VLSM. IT và Marketing dùng `/26`; R&D dùng `/25`. Nếu PC dùng sai mask hoặc sai default gateway thì ping nội bộ có thể được, nhưng ping ra ngoài sẽ lỗi.

## 3. Bảng Địa Chỉ IP

### 3.1 Router

| Device | Interface | IPv4 / Prefix | IPv6 / Prefix | Link-local | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| R1 | G0/0 | `172.16.1.62/26` | `2001:db8:cafe::1/64` | `fe80::1` | Gateway mạng IT |
| R1 | G0/1 | `172.16.1.126/26` | `2001:db8:cafe:1::1/64` | `fe80::1` | Gateway mạng Marketing |
| R1 | G0/2 | `172.16.1.254/25` | `2001:db8:cafe:2::1/64` | `fe80::1` | Gateway mạng R&D |
| R1 | S0/0/1 | `10.0.0.2/30` | `2001:db8:2::1/64` | `fe80::1` | Kết nối đến Main |
| Main | S0/0/0 | `209.165.200.226/30` | `2001:db8:1::1/64` | `fe80::2` | Kết nối ISP |
| Main | S0/0/1 | `10.0.0.1/30` | `2001:db8:2::2/64` | `fe80::2` | Kết nối R1 |

### 3.2 Switch Management

| Device | Interface | IPv4 / Prefix | Default Gateway |
| --- | --- | --- | --- |
| S1 | VLAN 1 | `172.16.1.61/26` | `172.16.1.62` |
| S2 | VLAN 1 | `172.16.1.125/26` | `172.16.1.126` |
| S3 | VLAN 1 | `172.16.1.253/25` | `172.16.1.254` |

### 3.3 End Devices

| Device | IPv4 / Prefix | IPv4 Gateway | IPv6 / Prefix | IPv6 Gateway | Link-local |
| --- | --- | --- | --- | --- | --- |
| IT | `172.16.1.1/26` | `172.16.1.62` | `2001:db8:cafe::2/64` | `fe80::1` | `fe80::2` |
| Marketing | `172.16.1.65/26` | `172.16.1.126` | `2001:db8:cafe:1::2/64` | `fe80::1` | `fe80::2` |
| R&D | `172.16.1.129/25` | `172.16.1.254` | `2001:db8:cafe:2::2/64` | `fe80::1` | `fe80::2` |
| Web | `64.100.0.3/29` | `64.100.0.1` | `2001:db8:acad::3/64` | `fe80::1` | `fe80::2` |

> **Lưu ý:** Trong đề có dòng Web IPv6 gateway dễ bị ghi nhầm thành `fe0::1`. Giá trị đúng để host dùng router link-local làm gateway là `fe80::1`.

## 4. Kế Hoạch Troubleshooting

| Bước | Việc cần làm | Lệnh / vị trí kiểm tra |
| --- | --- | --- |
| 1 | Kiểm tra địa chỉ trên PC | `ipconfig /all`, `ipv6config /all` |
| 2 | Ping gateway cùng LAN | `ping <default-gateway>` |
| 3 | Ping R1 theo IPv4/IPv6 | Ping địa chỉ G0/0, G0/1, G0/2 tương ứng |
| 4 | Ping switch management | Ping S1/S2/S3 VLAN 1 theo subnet tương ứng |
| 5 | Ping Web server | `ping 64.100.0.3`, `ping 2001:db8:acad::3` |
| 6 | Traceroute nếu ping lỗi | `tracert`, `traceroute` |
| 7 | Kiểm tra router/switch | `show ip interface brief`, `show ipv6 interface brief`, `show ip route`, `show ipv6 route` |
| 8 | Kiểm tra SSH vào R1 | `ssh -l Admin1 <R1-IP>` |

## 5. Documentation Table

| Vị trí | Vấn đề cần kiểm tra | Dấu hiệu | Cách sửa / giá trị đúng |
| --- | --- | --- | --- |
| IT PC | Sai IPv4, mask hoặc gateway | Ping `172.16.1.62` lỗi | Đặt `172.16.1.1/26`, gateway `172.16.1.62` |
| Marketing PC | Sai IPv4, mask hoặc gateway | Ping `172.16.1.126` lỗi | Đặt `172.16.1.65/26`, gateway `172.16.1.126` |
| R&D PC | Sai IPv4, mask hoặc gateway | Ping `172.16.1.254` lỗi | Đặt `172.16.1.129/25`, gateway `172.16.1.254` |
| PC IPv6 | Sai IPv6 gateway | Ping IPv6 ra Web lỗi | Gateway IPv6 phải là `fe80::1` |
| S1/S2/S3 | Sai VLAN 1 hoặc default gateway | PC ping switch không được | Cấu hình đúng IP VLAN 1 và `ip default-gateway` |
| R1 LAN interfaces | Interface shutdown hoặc sai địa chỉ | Gateway không trả lời ping | Sửa IP/IPv6 đúng bảng và `no shutdown` |
| R1/Main route | Thiếu default route hoặc route ngược | Ping gateway được nhưng không ping Web | R1 cần default route về Main; Main cần route về LAN nội bộ |
| Web server | Sai default gateway IPv6 | IPv4 OK nhưng IPv6 Web lỗi | IPv6 gateway của Web nên là `fe80::1` |
| SSH vào R1 | VTY/username/SSH sai | Ping R1 được nhưng SSH lỗi | Kiểm tra `username Admin1`, `transport input ssh`, `login local` |

## 6. Cấu Hình Chuẩn Tham Chiếu

### 6.1 R1

```text
R1# configure terminal
!
interface g0/0
 description IT LAN - S1
 ip address 172.16.1.62 255.255.255.192
 ipv6 address 2001:db8:cafe::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit
!
interface g0/1
 description Marketing LAN - S2
 ip address 172.16.1.126 255.255.255.192
 ipv6 address 2001:db8:cafe:1::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit
!
interface g0/2
 description R&D LAN - S3
 ip address 172.16.1.254 255.255.255.128
 ipv6 address 2001:db8:cafe:2::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit
!
interface s0/0/1
 description WAN to Main
 ip address 10.0.0.2 255.255.255.252
 ipv6 address 2001:db8:2::1/64
 ipv6 address fe80::1 link-local
 no shutdown
 exit
!
ip route 0.0.0.0 0.0.0.0 10.0.0.1
ipv6 unicast-routing
ipv6 route ::/0 2001:db8:2::2
end
copy running-config startup-config
```

> **Lưu ý:** Nếu route đã có sẵn nhưng sai next-hop, xóa route sai trước bằng `no ip route ...` hoặc `no ipv6 route ...`, sau đó nhập lại route đúng.

### 6.2 Main

```text
Main# configure terminal
!
interface s0/0/1
 description WAN to R1
 ip address 10.0.0.1 255.255.255.252
 ipv6 address 2001:db8:2::2/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit
!
interface s0/0/0
 description WAN to ISP
 ip address 209.165.200.226 255.255.255.252
 ipv6 address 2001:db8:1::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit
!
ip route 172.16.1.0 255.255.255.0 10.0.0.2
ipv6 unicast-routing
ipv6 route 2001:db8:cafe::/64 2001:db8:2::1
ipv6 route 2001:db8:cafe:1::/64 2001:db8:2::1
ipv6 route 2001:db8:cafe:2::/64 2001:db8:2::1
end
copy running-config startup-config
```

> **Lưu ý:** Nếu bài không cho quyền sửa Main hoặc ISP thì chỉ ghi nhận lỗi route/ISP và escalate. Trong Packet Tracer challenge này, ưu tiên sửa các thiết bị được phép truy cập.

### 6.3 S1, S2, S3

```text
! S1 - IT management
S1# configure terminal
interface vlan 1
 ip address 172.16.1.61 255.255.255.192
 no shutdown
 exit
ip default-gateway 172.16.1.62
end
copy running-config startup-config
```

```text
! S2 - Marketing management
S2# configure terminal
interface vlan 1
 ip address 172.16.1.125 255.255.255.192
 no shutdown
 exit
ip default-gateway 172.16.1.126
end
copy running-config startup-config
```

```text
! S3 - R&D management
S3# configure terminal
interface vlan 1
 ip address 172.16.1.253 255.255.255.128
 no shutdown
 exit
ip default-gateway 172.16.1.254
end
copy running-config startup-config
```

### 6.4 SSH trên R1

```text
R1# show running-config | section username
R1# show running-config | section line vty
R1# show ip ssh
```

```text
! Cấu hình tham chiếu nếu SSH bị sai
R1# configure terminal
ip domain-name ccna.local
username Admin1 secret Admin1pa55
crypto key generate rsa modulus 1024
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
end
copy running-config startup-config
```

> **Thông tin đăng nhập đã cho:** Enable password `Ciscoenpa55`, console password `Ciscoconpa55`, SSH `Admin1/Admin1pa55`.

## 7. Cấu Hình PC Và Server

| Thiết bị | Thao tác trong Packet Tracer |
| --- | --- |
| IT | Desktop → IP Configuration → nhập IPv4 `172.16.1.1`, mask `255.255.255.192`, gateway `172.16.1.62`; IPv6 `2001:db8:cafe::2/64`, gateway `fe80::1` |
| Marketing | IPv4 `172.16.1.65`, mask `255.255.255.192`, gateway `172.16.1.126`; IPv6 `2001:db8:cafe:1::2/64`, gateway `fe80::1` |
| R&D | IPv4 `172.16.1.129`, mask `255.255.255.128`, gateway `172.16.1.254`; IPv6 `2001:db8:cafe:2::2/64`, gateway `fe80::1` |
| Web | IPv4 `64.100.0.3/29`, gateway `64.100.0.1`; IPv6 `2001:db8:acad::3/64`, gateway `fe80::1` |

![PC IP Configuration lab 06](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-06/pc-ip-configuration.png)

## 8. Kiểm Tra Sau Khi Sửa

### 8.1 Kiểm tra địa chỉ trên PC

```text
PC> ipconfig /all
PC> ipv6config /all
```

| Thiết bị | Kết quả cần thấy |
| --- | --- |
| IT | IPv4 `172.16.1.1/26`, gateway `172.16.1.62`, IPv6 `2001:db8:cafe::2/64`, gateway `fe80::1` |
| Marketing | IPv4 `172.16.1.65/26`, gateway `172.16.1.126`, IPv6 `2001:db8:cafe:1::2/64`, gateway `fe80::1` |
| R&D | IPv4 `172.16.1.129/25`, gateway `172.16.1.254`, IPv6 `2001:db8:cafe:2::2/64`, gateway `fe80::1` |

### 8.2 Kiểm tra router và route

```text
R1# show ip interface brief
R1# show ipv6 interface brief
R1# show ip route
R1# show ipv6 route
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `show ip interface brief` | G0/0, G0/1, G0/2, S0/0/1 đều `up/up` |
| `show ipv6 interface brief` | Mỗi interface có global IPv6 và link-local đúng |
| `show ip route` | Có các route connected và default route `S* 0.0.0.0/0` |
| `show ipv6 route` | Có các route connected và default route `S ::/0` |

![R1 show commands lab 06](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-06/r1-show-commands.png)

### 8.3 Kiểm tra ping IPv4/IPv6

```text
! Từ IT
PC> ping 172.16.1.62
PC> ping 172.16.1.65
PC> ping 172.16.1.129
PC> ping 64.100.0.3
PC> ping 2001:db8:cafe:1::2
PC> ping 2001:db8:cafe:2::2
PC> ping 2001:db8:acad::3
```

```text
! Từ Marketing
PC> ping 172.16.1.1
PC> ping 172.16.1.129
PC> ping 64.100.0.3
PC> ping 2001:db8:cafe::2
PC> ping 2001:db8:cafe:2::2
PC> ping 2001:db8:acad::3
```

```text
! Từ R&D
PC> ping 172.16.1.1
PC> ping 172.16.1.65
PC> ping 64.100.0.3
PC> ping 2001:db8:cafe::2
PC> ping 2001:db8:cafe:1::2
PC> ping 2001:db8:acad::3
```

![Ping results lab 06](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-06/ping-results.png)

### 8.4 Kiểm tra SSH vào R1

```text
! Từ PC bất kỳ trong LAN
PC> ssh -l Admin1 172.16.1.62
Password: Admin1pa55
```

```text
! Có thể thử bằng địa chỉ gateway cùng LAN
PC> ssh -l Admin1 172.16.1.126
PC> ssh -l Admin1 172.16.1.254
```

| Thiết bị kiểm tra | Địa chỉ SSH nên thử |
| --- | --- |
| IT | `172.16.1.62` |
| Marketing | `172.16.1.126` |
| R&D | `172.16.1.254` |

![SSH verification lab 06](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-06/ssh-verification.png)

## 9. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Ping gateway lỗi | PC sai IP/mask/gateway hoặc R1 interface down | `ipconfig`, `show ip interface brief` | Sửa IP PC, sửa interface R1 và `no shutdown` |
| IPv4 ping giữa LAN lỗi | Thiếu route hoặc sai mask VLSM | `tracert`, `show ip route` | Sửa default route trên R1 hoặc route ngược trên Main |
| IPv6 ping lỗi nhưng IPv4 OK | Sai IPv6 global/gateway link-local hoặc chưa bật IPv6 routing | `ipv6config`, `show ipv6 route` | Sửa IPv6, gateway `fe80::1`, bật `ipv6 unicast-routing` |
| Ping switch management lỗi | SVI VLAN 1 sai IP hoặc thiếu default gateway | `show ip interface brief`, `show running-config` | Cấu hình đúng `interface vlan 1` và `ip default-gateway` |
| SSH vào R1 lỗi | Sai username/password, VTY chưa `login local`, chưa bật SSH | `show ip ssh`, `show run | section line vty` | Cấu hình `username Admin1 secret Admin1pa55`, `transport input ssh` |
| Web IPv6 lỗi | Web server sai default gateway IPv6 | Ping IPv4 Web OK, ping IPv6 Web lỗi | Sửa gateway IPv6 của Web thành `fe80::1` |
| Check Results chưa 100% | Quên lưu cấu hình hoặc sai chính tả | Activity Check Results | Sửa đúng bảng địa chỉ, `copy run start` |

## 10. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| IT ping Marketing/R&D | Thành công IPv4 và IPv6 |
| Marketing ping IT/R&D | Thành công IPv4 và IPv6 |
| R&D ping IT/Marketing | Thành công IPv4 và IPv6 |
| Tất cả PC ping Web | Thành công IPv4 `64.100.0.3` và IPv6 `2001:db8:acad::3` |
| Tất cả PC ping R1 | Thành công đến gateway cùng LAN |
| Tất cả PC ping switch | Thành công đến S1/S2/S3 management nếu policy cho phép |
| SSH vào R1 | Thành công bằng `Admin1/Admin1pa55` |
| Cấu hình lưu | Đã `copy running-config startup-config` |
| Check Results | Đạt 100% sau khi sửa toàn bộ lỗi |

Checklist ảnh minh chứng:

- [ ] `topology.png` - ảnh topology ban đầu.
- [ ] `pc-ip-configuration.png` - IP Configuration của IT/Marketing/R&D.
- [ ] `r1-show-commands.png` - output `show ip interface brief`, `show ipv6 interface brief`, route.
- [ ] `ping-results.png` - ping IPv4/IPv6 đến Web và các LAN.
- [ ] `ssh-verification.png` - SSH vào R1 thành công.
- [ ] `check-results.png` - kết quả hoàn thành 100%.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 5</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/">Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/">Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/">Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/">Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/">Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

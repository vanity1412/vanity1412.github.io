---
layout: page-toc
title: "CCNA 02.08 - 14.3.5 Packet Tracer - Basic Router Configuration Review"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `14.3.5 Packet Tracer - Basic Router Configuration Review.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-08/` |
| Trạng thái | Cấu hình R2, PC3, PC4, SSH, IPv4/IPv6 và kiểm tra end-to-end connectivity |

> Lab này là bài review tổng hợp về router: cấu hình địa chỉ IPv4/IPv6, bảo mật CLI, SSH remote access, lưu cấu hình và dùng các lệnh `show` để kiểm tra trạng thái thiết bị.

## 1. Mục Tiêu Bài Lab

- Hoàn thiện địa chỉ IPv4 và IPv6 cho PC3, PC4.
- Cấu hình hostname, password, banner và SSH trên router R2.
- Cấu hình IPv4, IPv6 global unicast và IPv6 link-local cho các interface của R2.
- Bật IPv6 routing trên R2.
- Lưu running-config vào startup-config.
- Kiểm tra kết nối IPv4/IPv6 giữa các PC, R1, R2 và ISP.
- Dùng các lệnh `show` để kiểm tra version, running-config, routing table và interface status.

![Topology lab 08](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/topology.png)

## 2. Bảng Địa Chỉ IP

### 2.1. Router R2

| Device | Interface | IPv4 Address / Prefix | IPv6 Address / Prefix | IPv6 Link-local | Default Gateway |
| --- | --- | --- | --- | --- | --- |
| R2 | G0/0/0 | `10.0.4.1/24` | `2001:db8:acad:4::1/64` | `fe80::2:a` | N/A |
| R2 | G0/0/1 | `10.0.5.1/24` | `2001:db8:acad:5::1/64` | `fe80::2:b` | N/A |
| R2 | S0/1/0 | `10.0.3.2/24` | `2001:db8:acad:3::2/64` | `fe80::1:c` | N/A |
| R2 | S0/1/1 | `209.165.200.225/30` | `2001:db8:feed:224::1/64` | `fe80::1:d` | N/A |

> **Lưu ý:** IPv6 link-local phải cấu hình kèm từ khóa `link-local`, ví dụ `ipv6 address fe80::2:a link-local`.

### 2.2. End Devices

| Device | Interface | IPv4 Address / Prefix | IPv4 Default Gateway | IPv6 Address / Prefix | IPv6 Default Gateway |
| --- | --- | --- | --- | --- | --- |
| PC1 | NIC | `10.0.1.10/24` | `10.0.1.1` | `2001:db8:acad:1::10/64` | `fe80::1:a` |
| PC2 | NIC | `10.0.2.10/24` | `10.0.2.1` | `2001:db8:acad:2::10/64` | `fe80::1:b` |
| PC3 | NIC | `10.0.4.10/24` | `10.0.4.1` | `2001:db8:acad:4::10/64` | `fe80::2:a` |
| PC4 | NIC | `10.0.5.10/24` | `10.0.5.1` | `2001:db8:acad:5::10/64` | `fe80::2:b` |

> PC1 và PC2 đã được cấu hình sẵn ở phía R1. Phần cần làm chính là PC3, PC4 và router R2.

### 2.3. Public/ISP Test Address

| Khu vực | IPv4 | IPv6 | Ghi chú |
| --- | --- | --- | --- |
| ISP/Public | `64.100.1.1` | `2001:db8:dead:1::1` | Địa chỉ dùng để kiểm tra kết nối ra ngoài |
| R2 - ISP link | `209.165.200.225/30` | `2001:db8:feed:224::1/64` | Interface S0/1/1 của R2 |

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 1 | PC1 - S1 - R1 | Mạng `10.0.1.0/24`, IPv6 `2001:db8:acad:1::/64`, đã cấu hình sẵn |
| LAN 2 | PC2 - S2 - R1 | Mạng `10.0.2.0/24`, IPv6 `2001:db8:acad:2::/64`, đã cấu hình sẵn |
| WAN R1-R2 | R1 - R2 | Mạng `10.0.3.0/24`, IPv6 `2001:db8:acad:3::/64` |
| LAN 3 | R2 - S3 - PC3 | Mạng `10.0.4.0/24`, IPv6 `2001:db8:acad:4::/64`, cần cấu hình trên R2 và PC3 |
| LAN 4 | R2 - S4 - PC4 | Mạng `10.0.5.0/24`, IPv6 `2001:db8:acad:5::/64`, cần cấu hình trên R2 và PC4 |
| ISP | R2 - Internet | Mạng `209.165.200.224/30`, IPv6 `2001:db8:feed:224::/64` |

> **Điểm dễ sai:** Default gateway IPv6 trên PC thường dùng địa chỉ link-local của router, không phải địa chỉ IPv6 global unicast.

## 4. Part 1 - Configure Devices and Verify Connectivity

### 4.1. Cấu hình IP cho PC3

| Tab | Field | Value |
| --- | --- | --- |
| Desktop > IP Configuration | IPv4 Address | `10.0.4.10` |
| Desktop > IP Configuration | Subnet Mask | `255.255.255.0` |
| Desktop > IP Configuration | Default Gateway | `10.0.4.1` |
| Desktop > IP Configuration | IPv6 Address | `2001:db8:acad:4::10` |
| Desktop > IP Configuration | IPv6 Prefix | `64` |
| Desktop > IP Configuration | IPv6 Gateway | `fe80::2:a` |

![PC3 IP Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/pc3-ip-configuration.png)

### 4.2. Cấu hình IP cho PC4

| Tab | Field | Value |
| --- | --- | --- |
| Desktop > IP Configuration | IPv4 Address | `10.0.5.10` |
| Desktop > IP Configuration | Subnet Mask | `255.255.255.0` |
| Desktop > IP Configuration | Default Gateway | `10.0.5.1` |
| Desktop > IP Configuration | IPv6 Address | `2001:db8:acad:5::10` |
| Desktop > IP Configuration | IPv6 Prefix | `64` |
| Desktop > IP Configuration | IPv6 Gateway | `fe80::2:b` |

![PC4 IP Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/pc4-ip-configuration.png)

### 4.3. Cấu hình cơ bản, SSH và interface cho R2

```text
Router> enable
Router# configure terminal
!
! Đặt hostname
hostname R2
!
! Mật khẩu privileged EXEC dạng mã hóa
enable secret c1sco1234
!
! Domain name dùng để tạo RSA key cho SSH
ip domain-name ccna-lab.com
!
! Tránh router cố resolve lệnh gõ sai thành hostname
no ip domain-lookup
!
! Mã hóa các password dạng clear text
service password-encryption
!
! Local user dùng để SSH
username SSHadmin secret 55Hadm!n
!
! Tạo RSA key 1024-bit cho SSH
crypto key generate rsa general-keys modulus 1024
!
! Bật SSH version 2
ip ssh version 2
!
! Cấu hình console
line console 0
 password cisco
 exec-timeout 6 0
 login
 logging synchronous
 exit
!
! Cấu hình VTY chỉ cho phép SSH
line vty 0 15
 password cisco
 exec-timeout 6 0
 transport input ssh
 login local
 exit
!
! Banner cảnh báo truy cập trái phép
banner motd #Unauthorized access is prohibited.#
!
! Bật định tuyến IPv6
ipv6 unicast-routing
!
! LAN kết nối S3/PC3
interface gigabitEthernet 0/0/0
 description LAN connection to S3 and PC3
 ip address 10.0.4.1 255.255.255.0
 ipv6 address 2001:db8:acad:4::1/64
 ipv6 address fe80::2:a link-local
 no shutdown
 exit
!
! LAN kết nối S4/PC4
interface gigabitEthernet 0/0/1
 description LAN connection to S4 and PC4
 ip address 10.0.5.1 255.255.255.0
 ipv6 address 2001:db8:acad:5::1/64
 ipv6 address fe80::2:b link-local
 no shutdown
 exit
!
! WAN kết nối R1
interface serial 0/1/0
 description WAN connection to R1
 ip address 10.0.3.2 255.255.255.0
 ipv6 address 2001:db8:acad:3::2/64
 ipv6 address fe80::1:c link-local
 no shutdown
 exit
!
! WAN kết nối ISP/Internet
interface serial 0/1/1
 description WAN connection to ISP
 ip address 209.165.200.225 255.255.255.252
 ipv6 address 2001:db8:feed:224::1/64
 ipv6 address fe80::1:d link-local
 no shutdown
 exit
!
! Route bổ sung để bảo đảm full connectivity nếu file chưa có định tuyến sẵn
ip route 10.0.1.0 255.255.255.0 10.0.3.1
ip route 10.0.2.0 255.255.255.0 10.0.3.1
ip route 0.0.0.0 0.0.0.0 209.165.200.226
ipv6 route 2001:db8:acad:1::/64 2001:db8:acad:3::1
ipv6 route 2001:db8:acad:2::/64 2001:db8:acad:3::1
ipv6 route ::/0 2001:db8:feed:224::2
!
end
copy running-config startup-config
```

> **Lưu ý:** Một số file Packet Tracer đã cấu hình sẵn route ở thiết bị khác. Phần static route phía trên giúp kiểm tra được end-to-end connectivity đầy đủ nếu trong file chưa có định tuyến sẵn.

![R2 CLI Configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/r2-cli-configuration.png)

### 4.4. Kiểm tra kết nối sau cấu hình

```text
! Từ PC3 ping PC4 bằng IPv4
C:\> ping 10.0.5.10

! Từ PC3 ping PC4 bằng IPv6
C:\> ping 2001:db8:acad:5::10

! Từ R2 ping R1 trên link Serial bằng IPv4
R2# ping 10.0.3.1

! Từ R2 ping R1 trên link Serial bằng IPv6
R2# ping 2001:db8:acad:3::1

! Từ PC3 ping ISP gần R2
C:\> ping 209.165.200.226

! Từ PC3 ping public test address
C:\> ping 64.100.1.1
```

| Câu hỏi kiểm tra | Kết quả |
| --- | --- |
| PC3 ping PC4 IPv4/IPv6 có thành công không? | Thành công nếu PC3, PC4, R2 G0/0/0 và G0/0/1 cấu hình đúng |
| R2 ping R1 S0/1/1 IPv4/IPv6 có thành công không? | Thành công nếu R2 S0/1/0 đúng IP và `no shutdown` |
| PC3 ping `209.165.200.226` có thành công không? | Thành công nếu link R2-ISP hoạt động |
| PC3 ping `64.100.1.1` có thành công không? | Thành công nếu có route ra ISP |

![Ping Verification](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/ping-verification.png)

### 4.5. Kiểm tra SSH từ PC3 vào R2

```text
C:\> ssh -l SSHadmin 10.0.4.1
Password: 55Hadm!n

R2>
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| SSH bằng user `SSHadmin` | Đăng nhập thành công |
| SSH tới `10.0.4.1` | Truy cập được R2 qua G0/0/0 |
| Password `55Hadm!n` | Được chấp nhận |

![SSH Verification](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/ssh-verification.png)

## 5. Part 2 - Display Router Information

### 5.1. Kiểm tra hardware và software bằng `show version`

```text
R2# show version
```

| Câu hỏi | Cách lấy thông tin | Ghi chú |
| --- | --- | --- |
| IOS image router đang chạy là gì? | Xem dòng `System image file is ...` | Giá trị phụ thuộc model router trong Packet Tracer |
| Router có bao nhiêu NVRAM? | Xem dòng chứa `non-volatile configuration memory` | Ghi đúng số hiển thị trong output |
| Router có bao nhiêu Flash? | Xem dòng chứa `bytes of flash memory` | Ghi đúng số hiển thị trong output |

```text
R2# show version | include register
```

| Câu hỏi | Đáp án |
| --- | --- |
| Boot process ở lần reload tiếp theo là gì? | Nếu hiển thị `Configuration register is 0x2102`, router sẽ boot IOS từ flash và load startup-config từ NVRAM theo cơ chế mặc định |

![Show Version](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/show-version.png)

### 5.2. Kiểm tra running-config và password

```text
R2# show running-config | include password
R2# show running-config | begin vty
```

| Câu hỏi | Đáp án |
| --- | --- |
| Password được hiển thị như thế nào trong running-config? | Các password không còn hiện plain text trực tiếp; `enable secret` và `username secret` hiển thị dạng hash, password line được mã hóa do có `service password-encryption` |
| `show running-config \| begin vty` cho kết quả gì? | Hiển thị running-config bắt đầu từ phần cấu hình `line vty` đến cuối file |

![Show Running Config Password](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/show-run-password.png)

### 5.3. Kiểm tra routing table

```text
R2# show ip route
R2# show ipv6 route
```

| Câu hỏi | Đáp án |
| --- | --- |
| Code nào chỉ directly connected network trong routing table? | `C` |
| Có bao nhiêu route IPv4 được đánh dấu `C` trên R2? | 4 route: `10.0.3.0/24`, `10.0.4.0/24`, `10.0.5.0/24`, `209.165.200.224/30` |
| Nếu thiếu route tới LAN phía R1 hoặc ISP thì xử lý thế nào? | Kiểm tra static route/default route hoặc định tuyến động nếu file lab dùng routing protocol |

![Show IP Route](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/show-ip-route.png)

### 5.4. Kiểm tra trạng thái interface

```text
R2# show ip interface brief
R2# show ip interface brief | exclude unassigned
R2# show ipv6 interface brief
```

| Câu hỏi | Đáp án |
| --- | --- |
| Lệnh nào đưa Gigabit Ethernet từ `administratively down` sang `up`? | `no shutdown` |
| Lệnh lọc chỉ hiển thị interface có địa chỉ IP? | `show ip interface brief \| exclude unassigned` |
| `[up/up]` trong `show ipv6 interface brief` nghĩa là gì? | Interface up ở Layer 1 và line protocol up ở Layer 2 |

![Show Interface Brief](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-08/show-interface-brief.png)

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC3 không ping được PC4 | Sai IP/default gateway trên PC hoặc interface R2 chưa `no shutdown` | Kiểm tra PC3/PC4 IP Configuration và `show ip interface brief` |
| Ping IPv6 fail nhưng IPv4 được | Thiếu `ipv6 unicast-routing`, sai IPv6 gateway hoặc thiếu IPv6 link-local | Bật `ipv6 unicast-routing`, kiểm tra `show ipv6 interface brief` |
| SSH không vào được R2 | Thiếu domain name, thiếu RSA key, sai user/password, VTY chưa `login local` | Kiểm tra `ip domain-name`, `crypto key generate rsa`, `username`, `line vty` |
| Console bị ngắt hoặc khó gõ lệnh vì log chen vào | Thiếu `logging synchronous` | Thêm `logging synchronous` dưới `line console 0` |
| Password vẫn hiện plain text | Thiếu `service password-encryption` | Thêm `service password-encryption` trong global config |
| Ping được gateway nhưng không ping được mạng xa | Thiếu route về các mạng khác | Kiểm tra `show ip route`, thêm static/default route nếu cần |
| Interface vẫn down/down | Sai cáp, cổng đầu bên kia chưa up, hoặc interface chưa bật | Kiểm tra topology, bật `no shutdown`, chờ vài giây cho line protocol up |

## 7. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| PC3 IPv4/IPv6 | Đúng theo Addressing Table |
| PC4 IPv4/IPv6 | Đúng theo Addressing Table |
| R2 hostname | `R2` |
| Privileged EXEC password | `enable secret c1sco1234` |
| Local SSH user | `SSHadmin / 55Hadm!n` |
| SSH | Chỉ cho phép SSH trên VTY |
| IPv6 routing | Đã bật bằng `ipv6 unicast-routing` |
| Interface R2 | 4 interface có IP và trạng thái up/up |
| Routing table | Có route connected cho các mạng trực tiếp |
| End-to-end connectivity | PC3 ping được PC4, R1, ISP và public test address nếu định tuyến đầy đủ |
| Save config | Đã lưu bằng `copy running-config startup-config` |

- [ ] Ảnh topology: `topology.png`
- [ ] Ảnh cấu hình IP PC3: `pc3-ip-configuration.png`
- [ ] Ảnh cấu hình IP PC4: `pc4-ip-configuration.png`
- [ ] Ảnh cấu hình CLI R2: `r2-cli-configuration.png`
- [ ] Ảnh kiểm tra ping: `ping-verification.png`
- [ ] Ảnh kiểm tra SSH: `ssh-verification.png`
- [ ] Ảnh `show version`: `show-version.png`
- [ ] Ảnh `show running-config | include password`: `show-run-password.png`
- [ ] Ảnh `show ip route`: `show-ip-route.png`
- [ ] Ảnh `show ip interface brief`: `show-interface-brief.png`
- [ ] Ảnh Check Results đạt yêu cầu: `check-results.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 7</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

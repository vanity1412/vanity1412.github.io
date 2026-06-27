---
layout: page-toc
title: "CCNA 10.01 - 1.5.10 Packet Tracer - Verify Directly Connected Networks"
permalink: /writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-01/
toc: true
---

[← Quay lại danh sách Static Và Default Routing](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/)

| Field | Value |
| --- | --- |
| Dạng lab | Static Và Default Routing |
| File lab | `1.5.10 Packet Tracer - Verify Directly Connected Networks.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Verify IPv4/IPv6 directly connected networks, sửa lỗi địa chỉ/cổng nếu có và kiểm tra ping end-to-end |

> **Ghi chú:** Bài này không bắt đầu từ cấu hình trắng. Router, PC và server đã có cấu hình một phần; nhiệm vụ chính là dùng lệnh `show`, đối chiếu Addressing Table, sửa lỗi sai và xác nhận kết nối.

## 1. Mục Tiêu Bài Lab

- Kiểm tra trạng thái interface IPv4 trên R1.
- Đối chiếu địa chỉ IPv4 của R1, PC1 và PC2 theo bảng địa chỉ.
- Kiểm tra bảng định tuyến IPv4 và gateway of last resort.
- Kiểm tra trạng thái interface IPv6 trên R2.
- Sửa địa chỉ IPv6 sai nếu phát hiện trên interface của R2.
- Kiểm tra kết nối từ các PC đến nhau và đến Dual Stack Server.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/topology.png)

## 2. Bảng Địa Chỉ IP

### IPv4

| Device | Interface | IP Address / Prefix | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0/0 | `172.16.20.1/25` | `255.255.255.128` | N/A |
| R1 | G0/0/1 | `172.16.20.129/25` | `255.255.255.128` | N/A |
| R1 | S0/1/0 | `209.165.200.225/30` | `255.255.255.252` | N/A |
| PC1 | NIC | `172.16.20.10/25` | `255.255.255.128` | `172.16.20.1` |
| PC2 | NIC | `172.16.20.138/25` | `255.255.255.128` | `172.16.20.129` |
| Dual Stack Server | NIC | `64.100.1.10` | Theo cấu hình server | Theo cấu hình server |

> **Lưu ý:** `172.16.20.0/25` và `172.16.20.128/25` là hai mạng khác nhau. PC1 dùng gateway `172.16.20.1`, còn PC2 dùng gateway `172.16.20.129`.

### IPv6

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R2 | G0/0/0 | `2001:db8:c0de:12::1/64` | N/A |
| R2 | G0/0/1 | `2001:db8:c0de:13::1/64` | N/A |
| R2 | S0/1/1 | `2001:db8:c0de:11::1/64` | N/A |
| R2 | S0/1/1 | `fe80::2` | N/A |
| PC3 | NIC | `2001:db8:c0de:12::a/64` | `fe80::2` |
| PC4 | NIC | `2001:db8:c0de:13::a/64` | `fe80::2` |
| Dual Stack Server | NIC | `2001:db8:100:1::a` | Theo cấu hình server |

> **Lưu ý:** Với IPv6, default gateway trên PC thường dùng địa chỉ link-local của router. Cùng một địa chỉ link-local như `fe80::2` có thể được dùng trên nhiều interface khác nhau vì link-local chỉ có ý nghĩa trong từng liên kết.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN IPv4 1 | PC1 - SW1 - R1 G0/0/0 | Mạng `172.16.20.0/25` |
| LAN IPv4 2 | PC2 - SW2 - R1 G0/0/1 | Mạng `172.16.20.128/25` |
| WAN IPv4 | R1 S0/1/0 - Internet | Mạng `209.165.200.224/30`, R1 dùng `.225`, Internet dùng `.226` |
| LAN IPv6 1 | PC3 - SW3 - R2 G0/0/0 | Mạng `2001:db8:c0de:12::/64` |
| LAN IPv6 2 | PC4 - SW4 - R2 G0/0/1 | Mạng `2001:db8:c0de:13::/64` |
| WAN IPv6 | R2 S0/1/1 - Internet | Mạng `2001:db8:c0de:11::/64` |
| Server | Dual Stack Server | Có cả IPv4 `64.100.1.10` và IPv6 `2001:db8:100:1::a` |

> **Điểm dễ sai:** PC1 và PC2 cùng bắt đầu bằng `172.16.20.x` nhưng không cùng subnet vì dùng `/25`, không phải `/24`.

## 4. Part 1 - Verify IPv4 Directly Connected Networks

### Step 1 - Kiểm tra interface IPv4 trên R1

```text
R1> enable
Password: class
R1# show ip interface brief | exclude unassigned
```

| Interface | Kết quả đúng |
| --- | --- |
| GigabitEthernet0/0/0 | `172.16.20.1`, trạng thái `up/up` |
| GigabitEthernet0/0/1 | `172.16.20.129`, trạng thái `up/up` |
| Serial0/1/0 | `209.165.200.225`, trạng thái `up/up` |

![R1 show ip interface brief](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r1-show-ip-interface-brief.png)

### Step 2 - Sửa lỗi địa chỉ hoặc trạng thái cổng nếu có

```text
R1# configure terminal
!
interface g0/0/0
 description LAN to SW1 - 172.16.20.0/25
 ip address 172.16.20.1 255.255.255.128
 no shutdown
 exit
!
interface g0/0/1
 description LAN to SW2 - 172.16.20.128/25
 ip address 172.16.20.129 255.255.255.128
 no shutdown
 exit
!
interface s0/1/0
 description WAN to Internet - 209.165.200.224/30
 ip address 209.165.200.225 255.255.255.252
 no shutdown
 exit
end
copy running-config startup-config
```

> **Lưu ý:** Chỉ nhập lại phần cấu hình bị sai trong file Packet Tracer. Nếu địa chỉ đã đúng thì không cần thay đổi.

### Step 3 - Kiểm tra routing table IPv4

```text
R1# show ip route | begin Gate
```

| Câu hỏi | Trả lời |
| --- | --- |
| Gateway of last resort là gì? | `209.165.200.226` nếu default route về Internet đã được cấu hình đúng |
| Route connected cần thấy | `172.16.20.0/25`, `172.16.20.128/25`, `209.165.200.224/30` |
| Nếu không ping được server IPv4 | Kiểm tra default route hoặc next-hop về Internet |

```text
R1# configure terminal
ip route 0.0.0.0 0.0.0.0 209.165.200.226
end
copy running-config startup-config
```

![R1 show ip route](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r1-show-ip-route.png)

### Step 4 - Kiểm tra description và thông tin interface

```text
R1# show interface | include Desc|conn
R1# show interface g0/0/0 | include duplex|media
```

| Câu hỏi | Trả lời |
| --- | --- |
| Circuit ID nằm ở đâu? | Nằm trong dòng `Description` của interface, ghi đúng theo output thực tế trong Packet Tracer |
| Duplex / speed / media type của G0/0/0 | Thường hiển thị dạng `Full-duplex`, tốc độ link, `media type is RJ45` |

![R1 interface detail](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r1-interface-detail.png)

### Kiểm tra cuối Part 1

```text
! Trên PC1
ping 172.16.20.138
ping 64.100.1.10

! Trên PC2
ping 172.16.20.10
ping 64.100.1.10
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC1 ping PC2 | Thành công |
| PC2 ping PC1 | Thành công |
| PC1 ping Dual Stack Server IPv4 | Thành công |
| PC2 ping Dual Stack Server IPv4 | Thành công |

![PC IPv4 ping test](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/pc-ipv4-ping-test.png)

## 5. Part 2 - Verify IPv6 Directly Connected Networks

### Step 1 - Kiểm tra interface IPv6 trên R2

```text
R2> enable
Password: class
R2# show ipv6 interface brief
```

| Interface | Kết quả đúng |
| --- | --- |
| GigabitEthernet0/0/0 | `2001:DB8:C0DE:12::1/64`, trạng thái `up/up` |
| GigabitEthernet0/0/1 | `2001:DB8:C0DE:13::1/64`, trạng thái `up/up` |
| Serial0/1/1 | `2001:DB8:C0DE:11::1/64`, trạng thái `up/up` |

![R2 show ipv6 interface brief](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r2-show-ipv6-interface-brief.png)

### Step 2 - Sửa địa chỉ IPv6 sai nếu có

```text
R2# configure terminal
ipv6 unicast-routing
!
interface g0/0/0
 description LAN to SW3 - 2001:db8:c0de:12::/64
 ipv6 address 2001:db8:c0de:12::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit
!
interface g0/0/1
 description LAN to SW4 - 2001:db8:c0de:13::/64
 no ipv6 address 2001:db8:c0de:14::1/64
 ipv6 address 2001:db8:c0de:13::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit
!
interface s0/1/1
 description WAN to Internet - 2001:db8:c0de:11::/64
 ipv6 address 2001:db8:c0de:11::1/64
 ipv6 address fe80::2 link-local
 no shutdown
 exit
end
copy running-config startup-config
```

> **Lưu ý:** Khi sửa IPv6, cần gỡ địa chỉ sai bằng `no ipv6 address ...` vì một interface có thể giữ nhiều IPv6 address cùng lúc.

### Step 3 - Kiểm tra bảng định tuyến IPv6

```text
R2# show ipv6 route
```

| Route cần thấy | Ý nghĩa |
| --- | --- |
| `C 2001:DB8:C0DE:12::/64` | Directly connected qua LAN PC3 |
| `C 2001:DB8:C0DE:13::/64` | Directly connected qua LAN PC4 |
| `C 2001:DB8:C0DE:11::/64` | Directly connected qua đường WAN tới Internet |
| `S ::/0` | Default route IPv6 ra Internet nếu đã được cấu hình |

```text
R2# configure terminal
ipv6 route ::/0 2001:db8:c0de:11::2
end
copy running-config startup-config
```

![R2 show ipv6 route](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r2-show-ipv6-route.png)

### Step 4 - Lọc running-config để kiểm tra IPv6

```text
R2# show running-config | include ipv6|interface
```

| Câu hỏi | Trả lời |
| --- | --- |
| Mỗi Gigabit interface có bao nhiêu IPv6 address? | 2 địa chỉ: 1 global unicast `2001:.../64` và 1 link-local `fe80::2` |
| Trạng thái interface đúng là gì? | `[up/up]` trong `show ipv6 interface brief` |

![R2 IPv6 running config filter](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/r2-ipv6-running-config-filter.png)

### Kiểm tra cuối Part 2

```text
! Trên PC3
ping 2001:db8:c0de:13::a
ping 2001:db8:100:1::a

! Trên PC4
ping 2001:db8:c0de:12::a
ping 2001:db8:100:1::a
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC3 ping PC4 IPv6 | Thành công |
| PC4 ping PC3 IPv6 | Thành công |
| PC3 ping Dual Stack Server IPv6 | Thành công |
| PC4 ping Dual Stack Server IPv6 | Thành công |

![PC IPv6 ping test](/writeups/ccna-packet-tracer-writeups/10-static-default-routing/labs/lab-01/pc-ipv6-ping-test.png)

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Interface trên router bị `administratively down` | Thiếu `no shutdown` | `show ip interface brief`, `show ipv6 interface brief` | Vào interface và nhập `no shutdown` |
| PC1 không ping được PC2 | Sai subnet mask `/25` hoặc sai default gateway | Kiểm tra IP Configuration trên PC | PC1 dùng `172.16.20.1`, PC2 dùng `172.16.20.129` |
| R1 không ping được server IPv4 | Thiếu default route ra Internet | `show ip route | begin Gate` | Thêm `ip route 0.0.0.0 0.0.0.0 209.165.200.226` nếu lab yêu cầu |
| R2 vẫn giữ địa chỉ IPv6 sai | Chỉ thêm địa chỉ mới mà chưa xóa địa chỉ cũ | `show running-config | include ipv6|interface` | Dùng `no ipv6 address <địa-chỉ-sai>` |
| PC3/PC4 không ping được IPv6 gateway | Sai link-local gateway hoặc sai IPv6 trên R2 | `show ipv6 interface brief` và IP Configuration trên PC | Đặt gateway PC là `fe80::2`, kiểm tra link-local trên R2 |
| PC3/PC4 không ping được server IPv6 | Thiếu default route IPv6 hoặc interface WAN sai | `show ipv6 route` | Thêm `ipv6 route ::/0 2001:db8:c0de:11::2` nếu lab yêu cầu |

## 7. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| R1 IPv4 interfaces | Đúng IP và `up/up` | Đạt |
| R1 IPv4 routing table | Có connected routes và gateway of last resort nếu cần ra Internet | Đạt |
| PC1 ↔ PC2 | Ping thành công | Đạt |
| PC1/PC2 → Dual Stack Server IPv4 | Ping thành công | Đạt |
| R2 IPv6 interfaces | Đúng IPv6 và `up/up` | Đạt |
| R2 IPv6 routing table | Có connected routes và default route nếu cần ra Internet | Đạt |
| PC3 ↔ PC4 | Ping IPv6 thành công | Đạt |
| PC3/PC4 → Dual Stack Server IPv6 | Ping thành công | Đạt |

Checklist ảnh minh chứng:

- [ ] `topology.png`
- [ ] `r1-show-ip-interface-brief.png`
- [ ] `r1-show-ip-route.png`
- [ ] `r1-interface-detail.png`
- [ ] `pc-ipv4-ping-test.png`
- [ ] `r2-show-ipv6-interface-brief.png`
- [ ] `r2-show-ipv6-route.png`
- [ ] `r2-ipv6-running-config-filter.png`
- [ ] `pc-ipv6-ping-test.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 3 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 1.5.10 Packet Tracer - Verify Directly Connected Networks (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-02/">Lab 2: 15.6.1 Packet Tracer - Configure IPv4 and IPv6 Static and Default Routes</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/lab-03/">Lab 3: 16.3.1 Packet Tracer - Troubleshoot Static and Default Routes</a></li>
    </ul>
  </details>
</div>

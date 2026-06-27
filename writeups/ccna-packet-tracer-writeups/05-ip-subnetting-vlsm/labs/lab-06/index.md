---
layout: page-toc
title: "CCNA 05.06 - 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-06/` |
| Trạng thái | Hoàn thành khi PC1, PC2, PC3, PC4 ping IPv6 được nhau |

> **Ghi chú:** Lab này tập trung vào chia các subnet IPv6 liên tiếp từ prefix ban đầu `2001:db8:acad:00c8::/64`, sau đó cấu hình IPv6 trên R1, R2 và để PC tự lấy địa chỉ bằng Auto Config.

## 1. Mục Tiêu Bài Lab

- Xác định 5 subnet IPv6 liên tiếp cho 4 LAN và 1 WAN link.
- Cấu hình IPv6 global unicast và link-local address trên R1, R2.
- Bật IPv6 routing trên các router.
- Cấu hình PC ở chế độ Auto Config.
- Bổ sung route IPv6 giữa R1 và R2 để các LAN liên thông.
- Kiểm tra kết nối IPv6 end-to-end giữa các PC.

![Topology lab 06](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/topology.png)

## 2. Bảng Subnet IPv6

| Khu vực | IPv6 Subnet |
| --- | --- |
| R1 G0/0 LAN | `2001:db8:acad:00c8::/64` |
| R1 G0/1 LAN | `2001:db8:acad:00c9::/64` |
| R2 G0/0 LAN | `2001:db8:acad:00ca::/64` |
| R2 G0/1 LAN | `2001:db8:acad:00cb::/64` |
| R1 ↔ R2 WAN link | `2001:db8:acad:00cc::/64` |

> **Lưu ý:** IPv6 subnet được tăng theo hệ thập lục phân: `00c8`, `00c9`, `00ca`, `00cb`, `00cc`.

## 3. Bảng Địa Chỉ IPv6

| Device | Interface | IPv6 Address / Prefix | Link-local Address | Ghi chú |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:acad:00c8::1/64` | `fe80::1` | Gateway LAN PC1 |
| R1 | G0/1 | `2001:db8:acad:00c9::1/64` | `fe80::1` | Gateway LAN PC2 |
| R1 | S0/0/0 | `2001:db8:acad:00cc::1/64` | `fe80::1` | WAN sang R2 |
| R2 | G0/0 | `2001:db8:acad:00ca::1/64` | `fe80::2` | Gateway LAN PC3 |
| R2 | G0/1 | `2001:db8:acad:00cb::1/64` | `fe80::2` | Gateway LAN PC4 |
| R2 | S0/0/0 | `2001:db8:acad:00cc::2/64` | `fe80::2` | WAN sang R1 |
| PC1 | NIC | Auto Config | Auto từ RA | LAN `00c8::/64` |
| PC2 | NIC | Auto Config | Auto từ RA | LAN `00c9::/64` |
| PC3 | NIC | Auto Config | Auto từ RA | LAN `00ca::/64` |
| PC4 | NIC | Auto Config | Auto từ RA | LAN `00cb::/64` |

> **Lưu ý:** Link-local `fe80::1` có thể dùng lặp lại trên nhiều interface của R1 vì link-local chỉ có hiệu lực trong phạm vi từng link.

## 4. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN PC1 | PC1 - Switch - R1 G0/0 | Dùng subnet `2001:db8:acad:00c8::/64` |
| LAN PC2 | PC2 - Switch - R1 G0/1 | Dùng subnet `2001:db8:acad:00c9::/64` |
| LAN PC3 | PC3 - Switch - R2 G0/0 | Dùng subnet `2001:db8:acad:00ca::/64` |
| LAN PC4 | PC4 - Switch - R2 G0/1 | Dùng subnet `2001:db8:acad:00cb::/64` |
| WAN | R1 S0/0/0 ↔ R2 S0/0/0 | Dùng subnet `2001:db8:acad:00cc::/64` |

> **Điểm dễ sai:** Chỉ cấu hình địa chỉ IPv6 trên router chưa đủ. Muốn các PC ở hai phía R1/R2 ping được nhau thì phải có IPv6 routing và route tới các mạng remote.

## 5. Cấu Hình R1

```text
R1> enable
R1# configure terminal

! Bật định tuyến IPv6 trên router
R1(config)# ipv6 unicast-routing

! LAN PC1 - subnet 2001:db8:acad:00c8::/64
R1(config)# interface gigabitEthernet0/0
R1(config-if)# description LAN to PC1
R1(config-if)# ipv6 address 2001:db8:acad:00c8::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

! LAN PC2 - subnet 2001:db8:acad:00c9::/64
R1(config)# interface gigabitEthernet0/1
R1(config-if)# description LAN to PC2
R1(config-if)# ipv6 address 2001:db8:acad:00c9::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

! WAN link sang R2 - subnet 2001:db8:acad:00cc::/64
R1(config)# interface serial0/0/0
R1(config-if)# description WAN link to R2
R1(config-if)# ipv6 address 2001:db8:acad:00cc::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

! Static route tới các LAN phía R2
R1(config)# ipv6 route 2001:db8:acad:00ca::/64 2001:db8:acad:00cc::2
R1(config)# ipv6 route 2001:db8:acad:00cb::/64 2001:db8:acad:00cc::2

R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** Nếu cổng serial của R1 là DCE và trạng thái line protocol vẫn down, cấu hình thêm `clock rate 64000` trên interface serial DCE.

### Kiểm tra trên R1

```text
R1# show ipv6 interface brief
R1# show ipv6 route

! Ping địa chỉ serial của R2
R1# ping 2001:db8:acad:00cc::2

! Ping thử LAN phía R2 sau khi PC đã Auto Config
R1# ping 2001:db8:acad:00ca::1
R1# ping 2001:db8:acad:00cb::1
```

![R1 IPv6 brief](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/r1-show-ipv6-brief.png)
![R1 IPv6 route](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/r1-show-ipv6-route.png)

## 6. Cấu Hình R2

```text
R2> enable
R2# configure terminal

! Bật định tuyến IPv6 trên router
R2(config)# ipv6 unicast-routing

! LAN PC3 - subnet 2001:db8:acad:00ca::/64
R2(config)# interface gigabitEthernet0/0
R2(config-if)# description LAN to PC3
R2(config-if)# ipv6 address 2001:db8:acad:00ca::1/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

! LAN PC4 - subnet 2001:db8:acad:00cb::/64
R2(config)# interface gigabitEthernet0/1
R2(config-if)# description LAN to PC4
R2(config-if)# ipv6 address 2001:db8:acad:00cb::1/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

! WAN link sang R1 - subnet 2001:db8:acad:00cc::/64
R2(config)# interface serial0/0/0
R2(config-if)# description WAN link to R1
R2(config-if)# ipv6 address 2001:db8:acad:00cc::2/64
R2(config-if)# ipv6 address fe80::2 link-local
R2(config-if)# no shutdown
R2(config-if)# exit

! Static route tới các LAN phía R1
R2(config)# ipv6 route 2001:db8:acad:00c8::/64 2001:db8:acad:00cc::1
R2(config)# ipv6 route 2001:db8:acad:00c9::/64 2001:db8:acad:00cc::1

R2(config)# end
R2# copy running-config startup-config
```

### Kiểm tra trên R2

```text
R2# show ipv6 interface brief
R2# show ipv6 route

! Ping địa chỉ serial của R1
R2# ping 2001:db8:acad:00cc::1

! Ping thử LAN phía R1
R2# ping 2001:db8:acad:00c8::1
R2# ping 2001:db8:acad:00c9::1
```

![R2 IPv6 brief](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/r2-show-ipv6-brief.png)
![R2 IPv6 route](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/r2-show-ipv6-route.png)

## 7. Cấu Hình PC

| PC | Cách cấu hình | Kết quả mong muốn |
| --- | --- | --- |
| PC1 | Desktop → IP Configuration → IPv6 → Auto Config | Nhận địa chỉ thuộc `2001:db8:acad:00c8::/64` |
| PC2 | Desktop → IP Configuration → IPv6 → Auto Config | Nhận địa chỉ thuộc `2001:db8:acad:00c9::/64` |
| PC3 | Desktop → IP Configuration → IPv6 → Auto Config | Nhận địa chỉ thuộc `2001:db8:acad:00ca::/64` |
| PC4 | Desktop → IP Configuration → IPv6 → Auto Config | Nhận địa chỉ thuộc `2001:db8:acad:00cb::/64` |

> **Lưu ý:** PC chỉ Auto Config đúng khi router interface cùng LAN đã `no shutdown` và router đã bật `ipv6 unicast-routing`.

![PC Auto Config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/pc-auto-config.png)

## 8. Kiểm Tra Kết Nối

```text
! Trên PC1 - kiểm tra sang các LAN khác
PC> ping 2001:db8:acad:00c9::1
PC> ping 2001:db8:acad:00ca::1
PC> ping 2001:db8:acad:00cb::1

! Trên PC1 ping PC2, PC3, PC4 bằng địa chỉ IPv6 đã Auto Config
PC> ping <IPv6-cua-PC2>
PC> ping <IPv6-cua-PC3>
PC> ping <IPv6-cua-PC4>
```

![Ping PC1 to PC4](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-06/ping-pc1-pc4.png)

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
| `show ipv6 interface brief` trên R1 | G0/0, G0/1, S0/0/0 có IPv6 đúng và trạng thái up/up | `r1-show-ipv6-brief.png` |
| `show ipv6 interface brief` trên R2 | G0/0, G0/1, S0/0/0 có IPv6 đúng và trạng thái up/up | `r2-show-ipv6-brief.png` |
| `show ipv6 route` trên R1 | Có route connected và static route tới `00ca`, `00cb` | `r1-show-ipv6-route.png` |
| `show ipv6 route` trên R2 | Có route connected và static route tới `00c8`, `00c9` | `r2-show-ipv6-route.png` |
| PC Auto Config | PC nhận IPv6 đúng subnet | `pc-auto-config.png` |
| PC1 ping PC4 | Ping thành công | `ping-pc1-pc4.png` |

## 9. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC không nhận IPv6 Auto Config | Router interface chưa bật hoặc chưa có RA | Kiểm tra `no shutdown`, `ipv6 unicast-routing` |
| Router có IPv6 nhưng PC khác mạng không ping được | Thiếu static route giữa R1 và R2 | Thêm `ipv6 route` tới các LAN remote |
| Serial link không up | Một đầu serial shutdown hoặc thiếu clock rate ở DCE | `no shutdown`, thêm `clock rate 64000` nếu cần |
| Gõ sai subnet `00c8`, `00c9`, `00ca`, `00cb`, `00cc` | Nhầm hệ hex khi tăng subnet | Đối chiếu lại bảng subnet IPv6 |
| Có nhiều IPv6 sai trên cùng interface | Chưa xoá IPv6 cũ trước khi cấu hình lại | Dùng `no ipv6 address <địa-chỉ-sai>/64` |

## 10. Kết Quả Cuối

| Hạng mục | Trạng thái mong muốn |
| --- | --- |
| Chia subnet IPv6 | 5 subnet liên tiếp từ `00c8` đến `00cc` |
| R1 | Cấu hình IPv6 đầy đủ trên G0/0, G0/1, S0/0/0 |
| R2 | Cấu hình IPv6 đầy đủ trên G0/0, G0/1, S0/0/0 |
| PC1-PC4 | Đặt IPv6 Auto Config |
| Routing | R1 và R2 có route tới mạng remote |
| Connectivity | Tất cả PC ping IPv6 được nhau |

- [ ] Chụp topology sau khi hoàn thành.
- [ ] Chụp bảng Auto Config của ít nhất một PC.
- [ ] Chụp `show ipv6 interface brief` trên R1.
- [ ] Chụp `show ipv6 interface brief` trên R2.
- [ ] Chụp `show ipv6 route` trên R1/R2.
- [ ] Chụp ping PC1 sang PC4 thành công.
- [ ] Chụp Check Results nếu Packet Tracer có chấm điểm.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 5</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 7 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

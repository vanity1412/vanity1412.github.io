---
layout: page-toc
title: "CCNA 05.05 - 12.6.6 Packet Tracer - Configure IPv6 Addressing"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `12.6.6 Packet Tracer - Configure IPv6 Addressing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Cấu hình IPv6 cho router, server, client và kiểm tra thông suốt |

> **Ghi chú:** Bài này tập trung vào IPv6. Router R1 cần bật `ipv6 unicast-routing`, sau đó cấu hình IPv6 global unicast và link-local trên từng interface. Các máy trạm dùng `fe80::1` làm default gateway.

## 1. Mục Tiêu Bài Lab

- Bật khả năng định tuyến IPv6 trên router R1.
- Cấu hình IPv6 cho các interface `G0/0`, `G0/1`, `S0/0/0` của R1.
- Cấu hình IPv6 cho các server Accounting và CAD.
- Cấu hình IPv6 cho các client Sales, Billing, Design và Engineering.
- Kiểm tra truy cập web server bằng địa chỉ IPv6.
- Kiểm tra ping IPv6 từ các client đến ISP.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/topology.png)

## 2. Bảng Địa Chỉ IPv6

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:1:1::1/64` | N/A |
| R1 | G0/0 | `fe80::1` | N/A |
| R1 | G0/1 | `2001:db8:1:2::1/64` | N/A |
| R1 | G0/1 | `fe80::1` | N/A |
| R1 | S0/0/0 | `2001:db8:1:a001::2/64` | N/A |
| R1 | S0/0/0 | `fe80::1` | N/A |
| Sales | NIC | `2001:db8:1:1::2/64` | `fe80::1` |
| Billing | NIC | `2001:db8:1:1::3/64` | `fe80::1` |
| Accounting | NIC | `2001:db8:1:1::4/64` | `fe80::1` |
| Design | NIC | `2001:db8:1:2::2/64` | `fe80::1` |
| Engineering | NIC | `2001:db8:1:2::3/64` | `fe80::1` |
| CAD | NIC | `2001:db8:1:2::4/64` | `fe80::1` |
| ISP | S0/0/0 | `2001:db8:1:a001::1/64` | N/A |

> **Lưu ý:** `fe80::1` là địa chỉ link-local của R1 trên từng LAN. Client có thể dùng link-local này làm default gateway vì gateway chỉ cần reachable trong cùng local link.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN trái | Sales, Billing, Accounting, S1 | Dùng prefix `2001:db8:1:1::/64`, gateway là R1 `G0/0` |
| LAN phải | Design, Engineering, CAD, S2 | Dùng prefix `2001:db8:1:2::/64`, gateway là R1 `G0/1` |
| WAN | R1 ↔ ISP | Dùng prefix `2001:db8:1:a001::/64` |
| Router trung tâm | R1 | Cần bật IPv6 routing trước khi router chuyển tiếp gói IPv6 |

> **Điểm dễ sai:** Cấu hình IPv6 đúng trên interface nhưng quên `ipv6 unicast-routing` thì router vẫn không forward IPv6 giữa các mạng.

## 4. Part 1 - Configure IPv6 Addressing on R1

### Bước 1: Bật IPv6 routing và cấu hình các interface

```text
R1> enable
R1# configure terminal
R1(config)# ipv6 unicast-routing

R1(config)# interface gigabitethernet0/0
R1(config-if)# description LAN 2001:db8:1:1::/64 - Sales Billing Accounting
R1(config-if)# ipv6 address 2001:db8:1:1::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface gigabitethernet0/1
R1(config-if)# description LAN 2001:db8:1:2::/64 - Design Engineering CAD
R1(config-if)# ipv6 address 2001:db8:1:2::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface serial0/0/0
R1(config-if)# description WAN connection to ISP
R1(config-if)# ipv6 address 2001:db8:1:a001::2/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** Khi nhập sai IPv6 address, cần xóa địa chỉ sai bằng `no ipv6 address <address>/<prefix>`, vì một interface có thể giữ nhiều IPv6 address cùng lúc.

### Kiểm tra cấu hình IPv6 trên R1

```text
R1# show ipv6 interface brief

GigabitEthernet0/0        [up/up]
    FE80::1
    2001:DB8:1:1::1
GigabitEthernet0/1        [up/up]
    FE80::1
    2001:DB8:1:2::1
Serial0/0/0               [up/up]
    FE80::1
    2001:DB8:1:A001::2
```

![R1 IPv6 brief](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/r1-show-ipv6-brief.png)

## 5. Part 2 - Configure IPv6 Addressing on Servers

| Server | IPv6 Address | Prefix | Default Gateway |
| --- | --- | --- | --- |
| Accounting | `2001:db8:1:1::4` | `/64` | `fe80::1` |
| CAD | `2001:db8:1:2::4` | `/64` | `fe80::1` |

![Accounting IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/accounting-ipv6-config.png)

![CAD IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/cad-ipv6-config.png)

> **Lưu ý:** Accounting nằm cùng mạng với Sales/Billing. CAD nằm cùng mạng với Design/Engineering.

## 6. Part 3 - Configure IPv6 Addressing on Clients

| Client | IPv6 Address | Prefix | Default Gateway |
| --- | --- | --- | --- |
| Sales | `2001:db8:1:1::2` | `/64` | `fe80::1` |
| Billing | `2001:db8:1:1::3` | `/64` | `fe80::1` |
| Design | `2001:db8:1:2::2` | `/64` | `fe80::1` |
| Engineering | `2001:db8:1:2::3` | `/64` | `fe80::1` |

![Sales IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/sales-ipv6-config.png)

![Billing IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/billing-ipv6-config.png)

![Design IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/design-ipv6-config.png)

![Engineering IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/engineering-ipv6-config.png)

## 7. Part 4 - Test and Verify Network Connectivity

### Bước 1: Kiểm tra truy cập web server bằng IPv6

| Thiết bị test | URL nhập trong Web Browser | Kết quả mong muốn |
| --- | --- | --- |
| Sales | `2001:db8:1:1::4` | Mở được website Accounting |
| Sales | `2001:db8:1:2::4` | Mở được website CAD |
| Billing | `2001:db8:1:1::4` | Mở được website Accounting |
| Billing | `2001:db8:1:2::4` | Mở được website CAD |
| Design | `2001:db8:1:1::4` | Mở được website Accounting |
| Engineering | `2001:db8:1:2::4` | Mở được website CAD |

![Sales access Accounting](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/sales-access-accounting.png)

![Sales access CAD](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/sales-access-cad.png)

### Bước 2: Kiểm tra ping đến ISP

```text
PC> ping 2001:db8:1:a001::1

Pinging 2001:db8:1:a001::1 with 32 bytes of data:
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
```

![Client ping ISP IPv6](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/client-ping-isp-ipv6.png)

### Bước 3: Kiểm tra route IPv6 trên R1

```text
R1# show ipv6 route
```

| Route cần thấy | Ý nghĩa |
| --- | --- |
| `C 2001:DB8:1:1::/64` | LAN Sales/Billing/Accounting kết nối trực tiếp |
| `C 2001:DB8:1:2::/64` | LAN Design/Engineering/CAD kết nối trực tiếp |
| `C 2001:DB8:1:A001::/64` | WAN R1 ↔ ISP kết nối trực tiếp |

![R1 IPv6 route](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/r1-show-ipv6-route.png)

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Client không ping được mạng khác | Quên bật `ipv6 unicast-routing` trên R1 | `show running-config` không có dòng `ipv6 unicast-routing` | Vào global config và nhập `ipv6 unicast-routing` |
| Interface R1 không up | Chưa nhập `no shutdown` | `show ipv6 interface brief` thấy `[administratively down/down]` | Vào interface và nhập `no shutdown` |
| Client không đi ra được khỏi LAN | Sai default gateway IPv6 | IP Configuration của PC không phải `fe80::1` | Sửa IPv6 Gateway thành `fe80::1` |
| Server không truy cập được từ client khác LAN | Server sai IPv6 hoặc sai prefix | Ping cùng LAN hoặc khác LAN đều fail | Sửa IPv6 đúng bảng địa chỉ |
| R1 có nhiều địa chỉ IPv6 không mong muốn | Nhập sai địa chỉ nhưng chưa xóa | `show ipv6 interface brief` hiện nhiều địa chỉ global trên cùng interface | Dùng `no ipv6 address <địa-chỉ-sai>/<prefix>` |

## 9. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| R1 bật IPv6 routing | Có dòng `ipv6 unicast-routing` | Hoàn thành |
| R1 G0/0 | `2001:db8:1:1::1/64`, `fe80::1`, trạng thái up/up | Hoàn thành |
| R1 G0/1 | `2001:db8:1:2::1/64`, `fe80::1`, trạng thái up/up | Hoàn thành |
| R1 S0/0/0 | `2001:db8:1:a001::2/64`, `fe80::1`, trạng thái up/up | Hoàn thành |
| Accounting/CAD | Đúng IPv6 và gateway `fe80::1` | Hoàn thành |
| Sales/Billing/Design/Engineering | Đúng IPv6 và gateway `fe80::1` | Hoàn thành |
| Web test | Client mở được Accounting và CAD bằng IPv6 | Hoàn thành |
| Ping ISP | Client ping được `2001:db8:1:a001::1` | Hoàn thành |

Checklist ảnh minh chứng cần chụp:

- [ ] `topology.png` - sơ đồ tổng quan.
- [ ] `r1-show-ipv6-brief.png` - trạng thái IPv6 trên R1.
- [ ] `accounting-ipv6-config.png` - IP Configuration của Accounting.
- [ ] `cad-ipv6-config.png` - IP Configuration của CAD.
- [ ] `sales-ipv6-config.png` - IP Configuration của Sales.
- [ ] `billing-ipv6-config.png` - IP Configuration của Billing.
- [ ] `design-ipv6-config.png` - IP Configuration của Design.
- [ ] `engineering-ipv6-config.png` - IP Configuration của Engineering.
- [ ] `sales-access-accounting.png` - truy cập Accounting web bằng IPv6.
- [ ] `sales-access-cad.png` - truy cập CAD web bằng IPv6.
- [ ] `client-ping-isp-ipv6.png` - ping ISP IPv6 thành công.
- [ ] `r1-show-ipv6-route.png` - bảng định tuyến IPv6 trên R1.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 6 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 05.05 - 12.6.6 Packet Tracer - Configure IPv6 Addressing"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IPv6 Addressing |
| File lab | `12.6.6 Packet Tracer - Configure IPv6 Addressing.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Cấu hình IPv6 cho router, server, client và kiểm tra kết nối bằng web/ping |

> Bài này tập trung vào IPv6. Điểm quan trọng nhất là R1 phải bật `ipv6 unicast-routing`, mỗi interface router có một địa chỉ IPv6 global unicast và một địa chỉ link-local `fe80::1`. Các server/client dùng `fe80::1` làm default gateway.

## 1. Mục Tiêu Bài Lab

- Bật IPv6 routing trên router `R1`.
- Cấu hình IPv6 cho `G0/0`, `G0/1` và `S0/0/0` trên `R1`.
- Cấu hình IPv6 cho hai server `Accounting` và `CAD`.
- Cấu hình IPv6 cho các client `Sales`, `Billing`, `Design` và `Engineering`.
- Kiểm tra truy cập website Accounting/CAD bằng IPv6.
- Kiểm tra ping từ client đến ISP bằng IPv6.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/topology.png)

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/topology1.png)

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
| ISP | S0/0/0 | `2001:db8:1:a001::1/64` | Đã cấu hình sẵn |

> **Lưu ý:** `2001:db8:...` là địa chỉ global unicast dùng để định danh thiết bị trong mạng IPv6. `fe80::1` là địa chỉ link-local của R1 trên từng đường kết nối, dùng làm gateway cho máy trạm trong cùng LAN.

## 3. Topology Overview

| Khu vực | Thiết bị | Prefix sử dụng | Gateway |
| --- | --- | --- | --- |
| LAN trái | Sales, Billing, Accounting, S1 | `2001:db8:1:1::/64` | R1 `G0/0` - `fe80::1` |
| LAN phải | Design, Engineering, CAD, S2 | `2001:db8:1:2::/64` | R1 `G0/1` - `fe80::1` |
| WAN | R1 ↔ ISP | `2001:db8:1:a001::/64` | R1 `S0/0/0` ↔ ISP `S0/0/0` |
| Router trung tâm | R1 | Định tuyến giữa các IPv6 prefix | Cần bật `ipv6 unicast-routing` |

> **Điểm dễ sai:** Cấu hình IPv6 trên interface chưa đủ để router định tuyến IPv6. Nếu thiếu `ipv6 unicast-routing`, R1 có địa chỉ IPv6 nhưng không chuyển tiếp gói tin IPv6 giữa các mạng.

## 4. Giải Thích Nhanh Cách Nhìn Bài IPv6 Này

| Thành phần | Ý nghĩa trong bài |
| --- | --- |
| `2001:db8:1:1::/64` | Mạng IPv6 của LAN trái: Sales, Billing, Accounting |
| `2001:db8:1:2::/64` | Mạng IPv6 của LAN phải: Design, Engineering, CAD |
| `2001:db8:1:a001::/64` | Mạng IPv6 của đường WAN giữa R1 và ISP |
| `::1`, `::2`, `::3`, `::4` | Cách viết rút gọn phần host trong địa chỉ IPv6 |
| `/64` | Prefix phổ biến cho LAN IPv6, tương tự phần network của subnet |
| `fe80::1` | Gateway link-local của R1 trên từng interface |

> **Lưu ý:** Cùng là `fe80::1` nhưng không bị trùng lỗi vì link-local chỉ có hiệu lực trong phạm vi từng link/interface. R1 có thể dùng `fe80::1` trên nhiều interface khác nhau.

## 5. Part 1 - Configure IPv6 Addressing on R1

### Step 1: Bật IPv6 routing và cấu hình các interface

```text
R1> enable
R1# configure terminal
R1(config)# ipv6 unicast-routing

R1(config)# interface g0/0
R1(config-if)# description LAN 2001:db8:1:1::/64 - Sales Billing Accounting
R1(config-if)# ipv6 address 2001:db8:1:1::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface g0/1
R1(config-if)# description LAN 2001:db8:1:2::/64 - Design Engineering CAD
R1(config-if)# ipv6 address 2001:db8:1:2::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface s0/0/0
R1(config-if)# description WAN to ISP
R1(config-if)# ipv6 address 2001:db8:1:a001::2/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** Nếu nhập sai IPv6 address, phải xóa địa chỉ sai bằng `no ipv6 address <address>/<prefix>`. Nếu chỉ nhập địa chỉ đúng thêm vào, interface có thể giữ cả địa chỉ sai và địa chỉ đúng.

### Step 2: Kiểm tra IPv6 trên R1

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

## 6. Part 2 - Configure IPv6 Addressing on Servers

### Step 1: Cấu hình IPv6 cho Accounting và CAD

| Server | IPv6 Address | Prefix | Default Gateway |
| --- | --- | --- | --- |
| Accounting | `2001:db8:1:1::4` | `/64` | `fe80::1` |
| CAD | `2001:db8:1:2::4` | `/64` | `fe80::1` |

![Accounting IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/accounting-ipv6-config.png)

![CAD IPv6 config](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/cad-ipv6-config.png)

> Accounting nằm ở LAN trái nên dùng prefix `2001:db8:1:1::/64`. CAD nằm ở LAN phải nên dùng prefix `2001:db8:1:2::/64`.

## 7. Part 3 - Configure IPv6 Addressing on Clients

### Step 1: Cấu hình IPv6 cho các client

| Client | IPv6 Address | Prefix | Default Gateway |
| --- | --- | --- | --- |
| Sales | `2001:db8:1:1::2` | `/64` | `fe80::1` |
| Billing | `2001:db8:1:1::3` | `/64` | `fe80::1` |
| Design | `2001:db8:1:2::2` | `/64` | `fe80::1` |
| Engineering | `2001:db8:1:2::3` | `/64` | `fe80::1` |


> Client ở LAN nào thì IPv6 global unicast phải cùng prefix với LAN đó. Gateway vẫn là `fe80::1` vì đó là link-local của R1 trên cùng LAN.

## 8. Part 4 - Test and Verify Network Connectivity

### Step 1: Kiểm tra truy cập web server bằng IPv6

| Thiết bị test | URL nhập trong Web Browser | Kết quả mong muốn |
| --- | --- | --- |
| Sales | `2001:db8:1:1::4` | Mở được website Accounting |
| Sales | `2001:db8:1:2::4` | Mở được website CAD |
| Billing | `2001:db8:1:1::4` | Mở được website Accounting |
| Billing | `2001:db8:1:2::4` | Mở được website CAD |
| Design | `2001:db8:1:1::4` | Mở được website Accounting |
| Design | `2001:db8:1:2::4` | Mở được website CAD |
| Engineering | `2001:db8:1:1::4` | Mở được website Accounting |
| Engineering | `2001:db8:1:2::4` | Mở được website CAD |


![Sales access CAD](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/sales-access-cad.png)

### Step 2: Kiểm tra ping đến ISP

```text
! Thực hiện trên một client bất kỳ
PC> ping 2001:db8:1:a001::1

Pinging 2001:db8:1:a001::1 with 32 bytes of data:
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
Reply from 2001:db8:1:a001::1: time<1ms
```

![Client ping ISP IPv6](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/client-ping-isp-ipv6.png)

### Step 3: Kiểm tra bảng định tuyến IPv6 trên R1

```text
R1# show ipv6 route
```

| Route cần thấy | Ý nghĩa |
| --- | --- |
| `C 2001:DB8:1:1::/64` | LAN trái kết nối trực tiếp vào R1 G0/0 |
| `C 2001:DB8:1:2::/64` | LAN phải kết nối trực tiếp vào R1 G0/1 |
| `C 2001:DB8:1:A001::/64` | WAN R1 ↔ ISP kết nối trực tiếp |

![R1 IPv6 route](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/r1-show-ipv6-route.png)

## 9. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Client không ping được mạng khác | Quên bật `ipv6 unicast-routing` trên R1 | `show running-config` không có dòng `ipv6 unicast-routing` | Vào global config và nhập `ipv6 unicast-routing` |
| Interface R1 không up | Chưa nhập `no shutdown` | `show ipv6 interface brief` thấy `[administratively down/down]` | Vào interface và nhập `no shutdown` |
| Client không đi ra ngoài LAN | Sai IPv6 gateway | IP Configuration không phải `fe80::1` | Sửa IPv6 Gateway thành `fe80::1` |
| Server không mở được web từ client khác LAN | Server sai IPv6/prefix/gateway | Ping hoặc Web Browser fail | Sửa IPv6 theo đúng bảng địa chỉ |
| R1 có nhiều IPv6 global address không mong muốn | Nhập sai địa chỉ nhưng chưa xóa | `show ipv6 interface brief` hiện nhiều địa chỉ trên cùng interface | Dùng `no ipv6 address <địa-chỉ-sai>/<prefix>` |
| Ping ISP fail dù LAN ping được gateway | Serial R1 chưa up hoặc sai IPv6 WAN | `show ipv6 interface brief` thấy `S0/0/0` down/sai IP | Sửa `S0/0/0`, nhập `no shutdown` |

## 10. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| R1 bật IPv6 routing | Có dòng `ipv6 unicast-routing` |
| R1 G0/0 | `2001:db8:1:1::1/64`, `fe80::1`, trạng thái `up/up` |
| R1 G0/1 | `2001:db8:1:2::1/64`, `fe80::1`, trạng thái `up/up` |
| R1 S0/0/0 | `2001:db8:1:a001::2/64`, `fe80::1`, trạng thái `up/up` |
| Accounting | `2001:db8:1:1::4/64`, gateway `fe80::1` |
| CAD | `2001:db8:1:2::4/64`, gateway `fe80::1` |
| Sales/Billing | Thuộc prefix `2001:db8:1:1::/64`, gateway `fe80::1` |
| Design/Engineering | Thuộc prefix `2001:db8:1:2::/64`, gateway `fe80::1` |
| Web test | Client mở được website Accounting và CAD bằng IPv6 |
| Ping ISP | Client ping được `2001:db8:1:a001::1` |

![result](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-05/final.png)

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

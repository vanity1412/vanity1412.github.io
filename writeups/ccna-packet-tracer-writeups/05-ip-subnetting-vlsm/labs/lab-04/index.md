---
layout: page-toc
title: "CCNA 05.04 - 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Hoàn thành thiết kế VLSM, cấu hình router/switch/host và kiểm tra ping end-to-end |

> **Ghi chú:** Lab này không cho sẵn bảng địa chỉ hoàn chỉnh. Trọng tâm là tự thiết kế VLSM từ mạng `192.168.203.0/24`, sau đó gán IP cho HQ, Remote, các switch quản trị VLAN 1 và các host.

## 1. Mục Tiêu Bài Lab

- Thiết kế sơ đồ địa chỉ VLSM cho 4 LAN và 1 liên kết WAN.
- Chia subnet theo đúng số host yêu cầu: `32`, `21`, `19`, `14` và WAN point-to-point.
- Gán địa chỉ IP cho router HQ, router Remote, switch và host.
- Cấu hình địa chỉ IPv4 trên router, switch VLAN 1 và PC.
- Kiểm tra toàn bộ thiết bị có thể ping qua lại sau khi cấu hình.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/topology.png)

## 2. Bảng Yêu Cầu Host Và Subnet Mask

| Khu vực | Số host yêu cầu | Subnet mask phù hợp | Số host usable | Ghi chú |
| --- | ---: | --- | ---: | --- |
| Remote-1 LAN | 32 | `/26` - `255.255.255.192` | 62 | LAN lớn nhất |
| HQ-1 LAN | 21 | `/27` - `255.255.255.224` | 30 | LAN lớn thứ hai |
| Remote-2 LAN | 19 | `/27` - `255.255.255.224` | 30 | Cùng mask với HQ-1 |
| HQ-2 LAN | 14 | `/28` - `255.255.255.240` | 14 | Vừa đủ 14 host |
| HQ ↔ Remote WAN | 2 | `/30` - `255.255.255.252` | 2 | Point-to-point |

> **Lưu ý:** VLSM luôn chia từ subnet cần nhiều host nhất đến ít host nhất để tránh lãng phí và tránh bị chồng lấn địa chỉ.

## 3. Bảng Thiết Kế VLSM

| Subnet Description | Number of Hosts Needed | Network Address/CIDR | First Usable Host Address | Last Usable Host Address | Broadcast Address |
| --- | ---: | --- | --- | --- | --- |
| Remote-1 LAN | 32 | `192.168.203.0/26` | `192.168.203.1` | `192.168.203.62` | `192.168.203.63` |
| HQ-1 LAN | 21 | `192.168.203.64/27` | `192.168.203.65` | `192.168.203.94` | `192.168.203.95` |
| Remote-2 LAN | 19 | `192.168.203.96/27` | `192.168.203.97` | `192.168.203.126` | `192.168.203.127` |
| HQ-2 LAN | 14 | `192.168.203.128/28` | `192.168.203.129` | `192.168.203.142` | `192.168.203.143` |
| HQ ↔ Remote WAN | 2 | `192.168.203.144/30` | `192.168.203.145` | `192.168.203.146` | `192.168.203.147` |

## 4. Bảng Địa Chỉ Hoàn Chỉnh

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| HQ | G0/0 | `192.168.203.129` | `255.255.255.240` | N/A |
| HQ | G0/1 | `192.168.203.65` | `255.255.255.224` | N/A |
| HQ | S0/0/0 | `192.168.203.145` | `255.255.255.252` | N/A |
| Remote | G0/0 | `192.168.203.97` | `255.255.255.224` | N/A |
| Remote | G0/1 | `192.168.203.1` | `255.255.255.192` | N/A |
| Remote | S0/0/0 | `192.168.203.146` | `255.255.255.252` | N/A |
| HQ-2 | VLAN 1 | `192.168.203.130` | `255.255.255.240` | `192.168.203.129` |
| HQ-1 | VLAN 1 | `192.168.203.66` | `255.255.255.224` | `192.168.203.65` |
| Remote-2 | VLAN 1 | `192.168.203.98` | `255.255.255.224` | `192.168.203.97` |
| Remote-1 | VLAN 1 | `192.168.203.2` | `255.255.255.192` | `192.168.203.1` |
| WS145 | NIC | `192.168.203.142` | `255.255.255.240` | `192.168.203.129` |
| WS116 | NIC | `192.168.203.94` | `255.255.255.224` | `192.168.203.65` |
| WS234 | NIC | `192.168.203.126` | `255.255.255.224` | `192.168.203.97` |
| WS203 | NIC | `192.168.203.62` | `255.255.255.192` | `192.168.203.1` |

> **Quy ước gán IP:** Router dùng first usable, switch dùng second usable, host dùng last usable. Riêng WAN: HQ dùng first usable, Remote dùng last usable.

## 5. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| HQ-2 LAN | HQ G0/0, switch HQ-2, WS145 | LAN 14 hosts dùng subnet `/28` |
| HQ-1 LAN | HQ G0/1, switch HQ-1, WS116 | LAN 21 hosts dùng subnet `/27` |
| Remote-2 LAN | Remote G0/0, switch Remote-2, WS234 | LAN 19 hosts dùng subnet `/27` |
| Remote-1 LAN | Remote G0/1, switch Remote-1, WS203 | LAN 32 hosts dùng subnet `/26` |
| WAN | HQ S0/0/0 ↔ Remote S0/0/0 | Liên kết point-to-point dùng subnet `/30` |

> **Lưu ý:** Nếu trong file Packet Tracer cổng LAN bị đảo so với bảng này, giữ nguyên subnet đã thiết kế và chỉ đổi IP sang đúng interface đang nối với LAN tương ứng.

## 6. Cấu Hình Router HQ

### Cấu hình interface và route

```text
HQ> enable
HQ# configure terminal
HQ(config)# hostname HQ

HQ(config)# interface gigabitethernet 0/0
HQ(config-if)# description LAN HQ-2 - 14 hosts
HQ(config-if)# ip address 192.168.203.129 255.255.255.240
HQ(config-if)# no shutdown
HQ(config-if)# exit

HQ(config)# interface gigabitethernet 0/1
HQ(config-if)# description LAN HQ-1 - 21 hosts
HQ(config-if)# ip address 192.168.203.65 255.255.255.224
HQ(config-if)# no shutdown
HQ(config-if)# exit

HQ(config)# interface serial 0/0/0
HQ(config-if)# description WAN to Remote
HQ(config-if)# ip address 192.168.203.145 255.255.255.252
HQ(config-if)# no shutdown
HQ(config-if)# exit

! Route tới các LAN phía Remote
HQ(config)# ip route 192.168.203.0 255.255.255.192 192.168.203.146
HQ(config)# ip route 192.168.203.96 255.255.255.224 192.168.203.146

HQ(config)# end
HQ# copy running-config startup-config
```

> **Lưu ý:** Nếu serial trên HQ là đầu DCE thì cần thêm `clock rate 64000` trên interface serial.

### Kiểm tra trên HQ

```text
HQ# show ip interface brief
HQ# show ip route
HQ# ping 192.168.203.146
HQ# ping 192.168.203.62
HQ# ping 192.168.203.126
```

![HQ verification](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/hq-verification.png)

## 7. Cấu Hình Router Remote

### Cấu hình interface và route

```text
Remote> enable
Remote# configure terminal
Remote(config)# hostname Remote

Remote(config)# interface gigabitethernet 0/0
Remote(config-if)# description LAN Remote-2 - 19 hosts
Remote(config-if)# ip address 192.168.203.97 255.255.255.224
Remote(config-if)# no shutdown
Remote(config-if)# exit

Remote(config)# interface gigabitethernet 0/1
Remote(config-if)# description LAN Remote-1 - 32 hosts
Remote(config-if)# ip address 192.168.203.1 255.255.255.192
Remote(config-if)# no shutdown
Remote(config-if)# exit

Remote(config)# interface serial 0/0/0
Remote(config-if)# description WAN to HQ
Remote(config-if)# ip address 192.168.203.146 255.255.255.252
Remote(config-if)# no shutdown
Remote(config-if)# exit

! Route tới các LAN phía HQ
Remote(config)# ip route 192.168.203.64 255.255.255.224 192.168.203.145
Remote(config)# ip route 192.168.203.128 255.255.255.240 192.168.203.145

Remote(config)# end
Remote# copy running-config startup-config
```

### Kiểm tra trên Remote

```text
Remote# show ip interface brief
Remote# show ip route
Remote# ping 192.168.203.145
Remote# ping 192.168.203.94
Remote# ping 192.168.203.142
```

![Remote verification](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/remote-verification.png)

## 8. Cấu Hình Switch VLAN 1

### Switch HQ-2

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname HQ-2
HQ-2(config)# interface vlan 1
HQ-2(config-if)# ip address 192.168.203.130 255.255.255.240
HQ-2(config-if)# no shutdown
HQ-2(config-if)# exit
HQ-2(config)# ip default-gateway 192.168.203.129
HQ-2(config)# end
HQ-2# copy running-config startup-config
```

### Switch HQ-1

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname HQ-1
HQ-1(config)# interface vlan 1
HQ-1(config-if)# ip address 192.168.203.66 255.255.255.224
HQ-1(config-if)# no shutdown
HQ-1(config-if)# exit
HQ-1(config)# ip default-gateway 192.168.203.65
HQ-1(config)# end
HQ-1# copy running-config startup-config
```

### Switch Remote-2

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Remote-2
Remote-2(config)# interface vlan 1
Remote-2(config-if)# ip address 192.168.203.98 255.255.255.224
Remote-2(config-if)# no shutdown
Remote-2(config-if)# exit
Remote-2(config)# ip default-gateway 192.168.203.97
Remote-2(config)# end
Remote-2# copy running-config startup-config
```

### Switch Remote-1

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname Remote-1
Remote-1(config)# interface vlan 1
Remote-1(config-if)# ip address 192.168.203.2 255.255.255.192
Remote-1(config-if)# no shutdown
Remote-1(config-if)# exit
Remote-1(config)# ip default-gateway 192.168.203.1
Remote-1(config)# end
Remote-1# copy running-config startup-config
```

![Switch VLAN 1 configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/switch-vlan1.png)

## 9. Cấu Hình PC

| PC | IP Address | Subnet Mask | Default Gateway | Ghi chú |
| --- | --- | --- | --- | --- |
| WS145 | `192.168.203.142` | `255.255.255.240` | `192.168.203.129` | HQ-2 LAN |
| WS116 | `192.168.203.94` | `255.255.255.224` | `192.168.203.65` | HQ-1 LAN |
| WS234 | `192.168.203.126` | `255.255.255.224` | `192.168.203.97` | Remote-2 LAN |
| WS203 | `192.168.203.62` | `255.255.255.192` | `192.168.203.1` | Remote-1 LAN |

![PC IP configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/pc-ip-configuration.png)

## 10. Kiểm Tra Kết Nối

### Kiểm tra từ router

```text
HQ# show ip interface brief
HQ# show ip route
HQ# ping 192.168.203.146
HQ# ping 192.168.203.62
HQ# ping 192.168.203.126

Remote# show ip interface brief
Remote# show ip route
Remote# ping 192.168.203.145
Remote# ping 192.168.203.94
Remote# ping 192.168.203.142
```

### Kiểm tra từ PC

```text
! Từ WS145
ping 192.168.203.129
ping 192.168.203.94
ping 192.168.203.62
ping 192.168.203.126

! Từ WS203
ping 192.168.203.1
ping 192.168.203.142
ping 192.168.203.94
ping 192.168.203.126
```

![End-to-end ping](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-04/end-to-end-ping.png)

## 11. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC ping gateway không được | Router interface hoặc PC IP sai subnet | `ipconfig`, `show ip interface brief` | Kiểm tra IP/mask/default gateway, bật `no shutdown` |
| Ping cùng LAN được nhưng khác LAN không được | Thiếu route giữa HQ và Remote | `show ip route` | Thêm static route đến subnet phía bên kia |
| Switch VLAN 1 không ping được từ mạng khác | Thiếu `ip default-gateway` trên switch | `show running-config` | Cấu hình gateway là IP router cùng LAN |
| WAN không lên | Serial chưa `no shutdown` hoặc thiếu clock rate đầu DCE | `show controllers serial`, `show ip interface brief` | Bật interface và thêm `clock rate 64000` nếu cần |
| Chồng lấn subnet | Chia VLSM không theo thứ tự lớn đến nhỏ | So lại bảng network/broadcast | Chia lại từ subnet lớn nhất trước |

## 12. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| VLSM | Chia đủ 5 subnet từ `192.168.203.0/24` |
| Router HQ | Các interface LAN/WAN up/up, có route tới LAN Remote |
| Router Remote | Các interface LAN/WAN up/up, có route tới LAN HQ |
| Switch | VLAN 1 có IP quản trị và default gateway đúng |
| Host | Tất cả host có IP/mask/default gateway đúng |
| Connectivity | Các host và switch có thể ping qua lại end-to-end |

- [ ] Chụp topology sau khi hoàn thành.
- [ ] Chụp bảng VLSM / Addressing Table đã điền.
- [ ] Chụp `show ip interface brief` trên HQ.
- [ ] Chụp `show ip interface brief` trên Remote.
- [ ] Chụp `show ip route` trên hai router.
- [ ] Chụp cấu hình IP của từng PC.
- [ ] Chụp ping giữa các host ở hai phía HQ và Remote.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/">Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

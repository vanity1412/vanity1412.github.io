---
layout: page-toc
title: "CCNA 05.01 - 11.5.5 Packet Tracer - Subnet an IPv4 Network"
permalink: /writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-01/
toc: true
---

[← Quay lại danh sách IP Addressing, Subnetting, VLSM](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/)

| Field | Value |
| --- | --- |
| Dạng lab | IP Addressing, Subnetting, VLSM |
| File lab | `11.5.5 Packet Tracer - Subnet an IPv4 Network.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành subnet `192.168.0.0/24` thành các mạng `/26`, cấu hình router, switch, PC và kiểm tra ping nội bộ |

> Lab này tập trung vào chia subnet IPv4 cố định cho hai LAN khách hàng. Không dùng VLSM, nên tất cả subnet trong mạng `192.168.0.0/24` phải dùng cùng một subnet mask.

## 1. Mục Tiêu Bài Lab

- Thiết kế sơ đồ chia subnet từ mạng gốc `192.168.0.0/24`.
- Đảm bảo LAN-A có tối thiểu 50 host và LAN-B có tối thiểu 40 host.
- Dự phòng thêm ít nhất 2 subnet chưa dùng cho mở rộng sau này.
- Điền đầy đủ bảng địa chỉ cho router, switch và PC.
- Cấu hình hostname, password, interface và địa chỉ IP trên `CustomerRouter`.
- Cấu hình IP quản trị VLAN 1 và default gateway trên `LAN-A Switch`, `LAN-B Switch`.
- Cấu hình IPv4 cho `PC-A`, `PC-B`.
- Kiểm tra `PC-A` ping gateway, `PC-B` ping gateway và `PC-A` ping `PC-B`.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/topology.png)

Ảnh
![anh](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/topology1.png)

## 2. Bảng Tính Subnet

| Yêu cầu | Giá trị |
| --- | --- |
| Network gốc | `192.168.0.0/24` |
| LAN-A cần tối thiểu | 50 host |
| LAN-B cần tối thiểu | 40 host |
| Subnet mở rộng cần thêm | 2 subnet |
| Tổng subnet tối thiểu | 4 subnet |
| Mask được chọn | `/26` |
| Subnet mask | `255.255.255.192` |
| Host usable mỗi subnet | 62 host |
| Số subnet tạo được từ `/24` | 4 subnet |

> **Lưu ý:** `/25` đủ host nhưng chỉ tạo được 2 subnet, không đủ yêu cầu mở rộng. `/27` tạo được nhiều subnet hơn nhưng chỉ có 30 host/subnet, không đủ cho LAN-A và LAN-B. Vì vậy `/26` là lựa chọn phù hợp nhất.

### Trả Lời Các Câu Hỏi Subnetting

| Câu hỏi | Đáp án |
| --- | --- |
| Cần bao nhiêu host trong subnet lớn nhất? | 50 host |
| Số subnet tối thiểu cần có? | 4 subnet |
| `/24` ở dạng binary là gì? | `11111111.11111111.11111111.00000000` |
| Bit `1` trong subnet mask biểu diễn gì? | Phần network/subnet |
| Bit `0` trong subnet mask biểu diễn gì? | Phần host |

| Prefix | Binary phần octet cuối | Subnet mask | Số subnet | Host usable/subnet | Đánh giá |
| --- | --- | --- | --- | --- | --- |
| `/25` | `10000000` | `255.255.255.128` | 2 | 126 | Đủ host, thiếu subnet |
| `/26` | `11000000` | `255.255.255.192` | 4 | 62 | Đủ cả host và subnet |
| `/27` | `11100000` | `255.255.255.224` | 8 | 30 | Thiếu host |
| `/28` | `11110000` | `255.255.255.240` | 16 | 14 | Thiếu host |
| `/29` | `11111000` | `255.255.255.248` | 32 | 6 | Thiếu host |
| `/30` | `11111100` | `255.255.255.252` | 64 | 2 | Thiếu host |

| Câu hỏi | Đáp án |
| --- | --- |
| Mask nào đáp ứng số host tối thiểu? | `/25`, `/26` |
| Mask nào đáp ứng số subnet tối thiểu? | `/26`, `/27`, `/28`, `/29`, `/30` |
| Mask nào đáp ứng cả host và subnet? | `/26` |

### Danh Sách Subnet Tạo Được

| Subnet | Prefix | Subnet Mask | Usable Host Range | Broadcast | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| `192.168.0.0` | `/26` | `255.255.255.192` | `192.168.0.1 - 192.168.0.62` | `192.168.0.63` | LAN-A |
| `192.168.0.64` | `/26` | `255.255.255.192` | `192.168.0.65 - 192.168.0.126` | `192.168.0.127` | LAN-B |
| `192.168.0.128` | `/26` | `255.255.255.192` | `192.168.0.129 - 192.168.0.190` | `192.168.0.191` | Dự phòng |
| `192.168.0.192` | `/26` | `255.255.255.192` | `192.168.0.193 - 192.168.0.254` | `192.168.0.255` | Dự phòng |

## 3. Bảng Địa Chỉ Hoàn Chỉnh

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| CustomerRouter | G0/0 | `192.168.0.1` | `255.255.255.192` | N/A |
| CustomerRouter | G0/1 | `192.168.0.65` | `255.255.255.192` | N/A |
| CustomerRouter | S0/1/0 | `209.165.201.2` | `255.255.255.252` | N/A |
| LAN-A Switch | VLAN 1 | `192.168.0.2` | `255.255.255.192` | `192.168.0.1` |
| LAN-B Switch | VLAN 1 | `192.168.0.66` | `255.255.255.192` | `192.168.0.65` |
| PC-A | NIC | `192.168.0.62` | `255.255.255.192` | `192.168.0.1` |
| PC-B | NIC | `192.168.0.126` | `255.255.255.192` | `192.168.0.65` |
| ISPRouter | G0/0 | `209.165.200.225` | `255.255.255.224` | N/A |
| ISPRouter | S0/1/0 | `209.165.201.1` | `255.255.255.252` | N/A |
| ISPSwitch | VLAN 1 | `209.165.200.226` | `255.255.255.224` | `209.165.200.225` |
| ISP Workstation | NIC | `209.165.200.235` | `255.255.255.224` | `209.165.200.225` |
| ISP Server | NIC | `209.165.200.240` | `255.255.255.224` | `209.165.200.225` |

> **Lưu ý:** LAN-A dùng subnet đầu tiên, LAN-B dùng subnet thứ hai. Trên mỗi LAN, router lấy IP đầu tiên, switch lấy IP thứ hai, PC lấy IP cuối cùng trong dải usable.

## 4. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN-A | `PC-A`, `LAN-A Switch`, `CustomerRouter G0/0` | Dùng subnet `192.168.0.0/26`, cần tối thiểu 50 host |
| LAN-B | `PC-B`, `LAN-B Switch`, `CustomerRouter G0/1` | Dùng subnet `192.168.0.64/26`, cần tối thiểu 40 host |
| WAN | `CustomerRouter S0/1/0` ↔ `ISPRouter S0/1/0` | Dùng mạng `209.165.201.0/30` |
| ISP LAN | `ISPSwitch`, `ISP Workstation`, `ISP Server` | Đã có địa chỉ mẫu theo đề |


## 5. Cấu Hình CustomerRouter

```text
Router> enable
Router# configure terminal
Router(config)# hostname CustomerRouter
CustomerRouter(config)# enable secret Class123
CustomerRouter(config)# line console 0
CustomerRouter(config-line)# password Cisco123
CustomerRouter(config-line)# login
CustomerRouter(config-line)# exit
CustomerRouter(config)# interface gigabitethernet 0/0
CustomerRouter(config-if)# description LAN-A gateway
CustomerRouter(config-if)# ip address 192.168.0.1 255.255.255.192
CustomerRouter(config-if)# no shutdown
CustomerRouter(config-if)# exit
CustomerRouter(config)# interface gigabitethernet 0/1
CustomerRouter(config-if)# description LAN-B gateway
CustomerRouter(config-if)# ip address 192.168.0.65 255.255.255.192
CustomerRouter(config-if)# no shutdown
CustomerRouter(config-if)# exit
CustomerRouter(config)# interface serial 0/1/0
CustomerRouter(config-if)# description WAN link to ISPRouter
CustomerRouter(config-if)# ip address 209.165.201.2 255.255.255.252
CustomerRouter(config-if)# no shutdown
CustomerRouter(config-if)# exit
CustomerRouter(config)# end
CustomerRouter# copy running-config startup-config
```

> **Lưu ý:** Nếu serial `S0/1/0` đã được cấu hình sẵn trong file Packet Tracer thì chỉ cần kiểm tra lại bằng `show ip interface brief`, không nhất thiết nhập lại.

![CustomerRouter interfaces](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/customerrouter-show-ip-interface-brief.png)

## 6. Cấu Hình LAN-A Switch

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname LAN-A-Switch
LAN-A-Switch(config)# interface vlan 1
LAN-A-Switch(config-if)# ip address 192.168.0.2 255.255.255.192
LAN-A-Switch(config-if)# no shutdown
LAN-A-Switch(config-if)# exit
LAN-A-Switch(config)# ip default-gateway 192.168.0.1
LAN-A-Switch(config)# end
LAN-A-Switch# copy running-config startup-config
```

![LAN-A switch VLAN 1](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/lan-a-switch-vlan1.png)

## 7. Cấu Hình LAN-B Switch

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname LAN-B-Switch
LAN-B-Switch(config)# interface vlan 1
LAN-B-Switch(config-if)# ip address 192.168.0.66 255.255.255.192
LAN-B-Switch(config-if)# no shutdown
LAN-B-Switch(config-if)# exit
LAN-B-Switch(config)# ip default-gateway 192.168.0.65
LAN-B-Switch(config)# end
LAN-B-Switch# copy running-config startup-config
```


## 8. Cấu Hình PC

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC-A | `192.168.0.62` | `255.255.255.192` | `192.168.0.1` |
| PC-B | `192.168.0.126` | `255.255.255.192` | `192.168.0.65` |

![PC-A IP Configuration](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/pc-a-ip-configuration.png)


## 9. Kiểm Tra Cấu Hình

### Kiểm tra trên CustomerRouter

```text
CustomerRouter# show ip interface brief

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.0.1     YES manual up                    up
GigabitEthernet0/1     192.168.0.65    YES manual up                    up
Serial0/1/0            209.165.201.2   YES manual up                    up
```

```text
CustomerRouter# show running-config
! kiểm tra hostname, enable secret, console password và IP trên G0/0, G0/1
```


### Kiểm tra ping từ PC-A

```text
PC-A> ping 192.168.0.1
! ping default gateway LAN-A

PC-A> ping 192.168.0.126
! ping PC-B khác subnet
```


### Kiểm tra ping từ PC-B

```text
PC-B> ping 192.168.0.65
! ping default gateway LAN-B

PC-B> ping 192.168.0.62
! ping PC-A khác subnet
```

![PC-B ping results](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/pc-b-ping-results.png)

## 10. Trả Lời Câu Hỏi Kiểm Tra

| Câu hỏi | Đáp án |
| --- | --- |
| PC-A ping được default gateway không? | Có, nếu `PC-A` dùng `192.168.0.62/26` và gateway `192.168.0.1` |
| PC-B ping được default gateway không? | Có, nếu `PC-B` dùng `192.168.0.126/26` và gateway `192.168.0.65` |
| PC-A ping được PC-B không? | Có, sau khi hai interface `G0/0`, `G0/1` trên `CustomerRouter` đều up/up |
| Nếu ping fail thì kiểm tra gì trước? | IP address, subnet mask, default gateway, trạng thái interface router |

## 11. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Chọn `/27` cho LAN-A/LAN-B | `/27` chỉ có 30 usable host, không đủ 50 và 40 host | Dùng `/26` |
| Chọn `/25` | Có 126 usable host nhưng chỉ tạo được 2 subnet | Dùng `/26` để có 4 subnet |
| PC-A dùng sai gateway | Gateway phải là IP router trong cùng subnet LAN-A | Đặt gateway `192.168.0.1` |
| PC-B dùng sai gateway | Gateway phải là IP router trong cùng subnet LAN-B | Đặt gateway `192.168.0.65` |
| Switch không ping được gateway | Thiếu `ip default-gateway` hoặc VLAN 1 chưa `no shutdown` | Cấu hình `ip default-gateway` và bật `interface vlan 1` |
| Router interface down | Chưa nhập `no shutdown` | Bật `no shutdown` trên `G0/0`, `G0/1` |
| PC-A không ping được PC-B | Sai subnet mask hoặc router interface chưa up | Kiểm tra `/26`, gateway và `show ip interface brief` |

## 12. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| Subnet mask được chọn | `/26` - `255.255.255.192` |
| LAN-A | `192.168.0.0/26` |
| LAN-B | `192.168.0.64/26` |
| Subnet dự phòng | `192.168.0.128/26`, `192.168.0.192/26` |
| CustomerRouter G0/0 | `192.168.0.1/26`, up/up |
| CustomerRouter G0/1 | `192.168.0.65/26`, up/up |
| LAN-A Switch VLAN 1 | `192.168.0.2/26`, gateway `192.168.0.1` |
| LAN-B Switch VLAN 1 | `192.168.0.66/26`, gateway `192.168.0.65` |
| PC-A | `192.168.0.62/26`, gateway `192.168.0.1` |
| PC-B | `192.168.0.126/26`, gateway `192.168.0.65` |
| Ping PC-A → gateway | Thành công |
| Ping PC-B → gateway | Thành công |
| Ping PC-A ↔ PC-B | Thành công |

![results](/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/labs/lab-01/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 7 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 11.5.5 Packet Tracer - Subnet an IPv4 Network (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-02/">Lab 2: 11.7.5 Packet Tracer - Subnetting Scenario</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-03/">Lab 3: 11.9.3 Packet Tracer - VLSM Design and Implementation Practice</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-04/">Lab 4: 11.10.1 Packet Tracer - Design and Implement a VLSM Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-05/">Lab 5: 12.6.6 Packet Tracer - Configure IPv6 Addressing</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-06/">Lab 6: 12.9.1 Packet Tracer - Implement a Subnetted IPv6 Addressing Scheme</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/lab-07/">Lab 7: 13.2.6 Packet Tracer - Verify IPv4 and IPv6 Addressing</a></li>
    </ul>
  </details>
</div>

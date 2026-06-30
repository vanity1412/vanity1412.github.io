---
layout: page-toc
title: "CCNA 04.01 - 2.7.6 Packet Tracer - Implement Basic Connectivity"
permalink: /writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/
toc: true
---

[← Quay lại danh sách Kết Nối Vật Lý](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/)

| Field | Value |
| --- | --- |
| Dạng lab | Kết Nối Vật Lý / Basic Connectivity |
| File lab | `2.7.6 Packet Tracer - Implement Basic Connectivity.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành cấu hình cơ bản switch, IP quản trị VLAN 1, IP cho PC và kiểm tra ping thành công |

> Lab này đã có sẵn 2 switch và 2 PC trong cùng mạng `192.168.1.0/24`. Nhiệm vụ chính là cấu hình bảo mật cơ bản trên switch, gán địa chỉ IP cho PC, cấu hình IP quản trị trên VLAN 1 của switch và kiểm tra kết nối bằng `ping`.

## 1. Mục Tiêu Bài Lab

- Cấu hình hostname cho `S1` và `S2`.
- Cấu hình mật khẩu console là `cisco`.
- Cấu hình mật khẩu privileged EXEC mode là `class`.
- Cấu hình banner cảnh báo truy cập trái phép.
- Lưu cấu hình từ RAM xuống NVRAM.
- Gán địa chỉ IPv4 cho `PC1` và `PC2`.
- Cấu hình địa chỉ IP quản trị trên `interface vlan 1` của `S1` và `S2`.
- Kiểm tra cấu hình bằng `show ip interface brief`, `show running-config` và `ping`.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/topology.png)

## 2. Bảng Địa Chỉ IPv4

| Thiết bị | Interface | Địa chỉ IP | Subnet Mask |
| --- | --- | --- | --- |
| S1 | VLAN 1 | `192.168.1.253` | `255.255.255.0` |
| S2 | VLAN 1 | `192.168.1.254` | `255.255.255.0` |
| PC1 | NIC | `192.168.1.1` | `255.255.255.0` |
| PC2 | NIC | `192.168.1.2` | `255.255.255.0` |

> **Lưu ý:** Tất cả thiết bị đều nằm trong cùng subnet `192.168.1.0/24`, nên không cần default gateway để kiểm tra ping nội bộ trong bài này.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Nhánh trái | `PC1` nối với `S1` | PC1 dùng IP `192.168.1.1/24` để kiểm tra kết nối |
| Liên kết trung tâm | `S1` nối với `S2` | Hai switch chuyển tiếp frame Layer 2 trong cùng LAN |
| Nhánh phải | `S2` nối với `PC2` | PC2 dùng IP `192.168.1.2/24` để kiểm tra end-to-end |
| Quản trị switch | `VLAN 1` trên S1/S2 | Cần IP quản trị để ping, SSH/Telnet hoặc quản lý switch từ xa |

> **Điểm dễ nhầm:** Switch Layer 2 vẫn chuyển tiếp dữ liệu khi chưa có IP. Tuy nhiên, muốn ping tới switch hoặc quản trị switch qua mạng thì phải cấu hình IP trên interface VLAN quản trị.

## 4. Part 1 - Cấu Hình Cơ Bản Trên S1 Và S2

### Step 1-4 - Cấu hình cơ bản trên S1

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname S1
S1(config)# enable secret class
S1(config)# line console 0
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
S1(config)# service password-encryption
S1(config)# banner motd #Authorized access only. Violators will be prosecuted to the full extent of the law.#
S1(config)# end
S1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

> `enable secret class` dùng để đặt mật khẩu vào privileged EXEC mode ở dạng mã hóa. `service password-encryption` giúp mã hóa các password dạng line như console password trong file cấu hình.

| Câu hỏi | Trả lời |
| --- | --- |
| Làm sao kiểm tra console password và privileged EXEC password đã đúng? | Thoát khỏi phiên CLI, vào lại console để kiểm tra password `cisco`, sau đó dùng lệnh `enable` để kiểm tra mật khẩu `class`. Có thể dùng thêm `show running-config` để xem phần `enable secret` và `line console 0`. |
| Lệnh nào dùng để lưu cấu hình xuống NVRAM? | `copy running-config startup-config` |

### Step 5 - Cấu hình cơ bản trên S2

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname S2
S2(config)# enable secret class
S2(config)# line console 0
S2(config-line)# password cisco
S2(config-line)# login
S2(config-line)# exit
S2(config)# service password-encryption
S2(config)# banner motd #Authorized access only. Violators will be prosecuted to the full extent of the law.#
S2(config)# end
S2# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

![S1 basic configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/s1-basic-config.png)
![S2 basic configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/s2-basic-config.png)

### Kiểm tra Part 1

```text
S1# show running-config
hostname S1
enable secret 5 <encrypted-password>
service password-encryption
banner motd ^CAuthorized access only. Violators will be prosecuted to the full extent of the law.^C
line con 0
 password 7 <encrypted-password>
 login
```

```text
S2# show running-config
hostname S2
enable secret 5 <encrypted-password>
service password-encryption
banner motd ^CAuthorized access only. Violators will be prosecuted to the full extent of the law.^C
line con 0
 password 7 <encrypted-password>
 login
```

![Verify basic configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/verify-basic-config.png)

## 5. Part 2 - Cấu Hình IP Cho PC

### Step 1 - Cấu hình IP cho PC1 và PC2

| PC | Desktop > IP Configuration | Giá trị cần nhập |
| --- | --- | --- |
| PC1 | IP Address | `192.168.1.1` |
| PC1 | Subnet Mask | `255.255.255.0` |
| PC2 | IP Address | `192.168.1.2` |
| PC2 | Subnet Mask | `255.255.255.0` |

![PC1 IP Configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/pc1-ip-config.png)
![PC2 IP Configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/pc2-ip-config.png)

### Step 2 - Kiểm tra ping tới switch trước khi cấu hình IP quản trị

```text
PC> ping 192.168.1.253

Pinging 192.168.1.253 with 32 bytes of data:

Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 192.168.1.253:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
```

| Câu hỏi | Trả lời |
| --- | --- |
| Ping từ PC1 tới S1 có thành công không? | Chưa thành công nếu `S1` chưa được cấu hình IP trên `interface vlan 1`. Switch vẫn chuyển frame Layer 2, nhưng chưa có địa chỉ IP quản trị để trả lời ping. |

![Ping before SVI IP](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/ping-before-svi-ip.png)

## 6. Part 3 - Cấu Hình Switch Management Interface

### Step 1 - Cấu hình IP quản trị cho S1

```text
S1> enable
Password:
S1# configure terminal
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.253 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# exit
S1(config)# end
S1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

> `no shutdown` dùng để bật interface VLAN 1. Nếu interface ở trạng thái shutdown, switch sẽ không phản hồi ping tới IP quản trị.

| Câu hỏi | Trả lời |
| --- | --- |
| Vì sao cần cấu hình IP cho switch nếu switch vẫn hoạt động dạng plug-and-play? | IP quản trị giúp kiểm tra kết nối bằng `ping` và quản lý switch từ xa qua các dịch vụ như SSH/Telnet/SNMP. |
| Vì sao phải nhập lệnh `no shutdown`? | Để bật interface VLAN 1, giúp SVI chuyển sang trạng thái hoạt động khi có ít nhất một cổng switch đang up trong VLAN đó. |

### Step 2 - Cấu hình IP quản trị cho S2

```text
S2> enable
Password:
S2# configure terminal
S2(config)# interface vlan 1
S2(config-if)# ip address 192.168.1.254 255.255.255.0
S2(config-if)# no shutdown
S2(config-if)# exit
S2(config)# end
S2# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

![S1 VLAN 1 IP configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/s1-vlan1-ip.png)
![S2 VLAN 1 IP configuration](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/s2-vlan1-ip.png)

### Step 3-4 - Kiểm tra IP và lưu cấu hình

```text
S1# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  192.168.1.253   YES manual up                    up
FastEthernet0/1        unassigned      YES unset  up                    up
FastEthernet0/2        unassigned      YES unset  up                    up
```

```text
S2# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  192.168.1.254   YES manual up                    up
FastEthernet0/1        unassigned      YES unset  up                    up
FastEthernet0/2        unassigned      YES unset  up                    up
```

```text
S1# copy running-config startup-config
S2# copy running-config startup-config
```

| Câu hỏi | Trả lời |
| --- | --- |
| Lệnh nào lưu file cấu hình trong RAM sang NVRAM? | `copy running-config startup-config` |

![Show IP interface brief](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/show-ip-interface-brief.png)

### Step 5 - Kiểm tra kết nối toàn mạng

```text
PC> ping 192.168.1.2
! PC1 ping PC2

PC> ping 192.168.1.253
! PC1 ping S1

PC> ping 192.168.1.254
! PC1 ping S2

PC> ping 192.168.1.1
! PC2 ping PC1

PC> ping 192.168.1.253
! PC2 ping S1

PC> ping 192.168.1.254
! PC2 ping S2
```

> Nếu lần ping đầu tiên chỉ đạt khoảng `80%`, chạy lại lệnh ping. Gói đầu có thể mất do thiết bị cần học MAC hoặc xử lý ARP trước khi gửi ICMP thành công.

![Final ping test](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-01/final-ping-test.png)

## 7. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC ping switch không thành công | Chưa cấu hình IP trên `interface vlan 1` | Vào `interface vlan 1`, cấu hình đúng IP và subnet mask |
| `Vlan1` bị `administratively down` | Chưa nhập `no shutdown` | Nhập `no shutdown` trong interface VLAN 1 |
| `Vlan1` vẫn down/down | Không có cổng vật lý nào trong VLAN 1 đang up | Kiểm tra dây nối, cổng switch và trạng thái link |
| Không vào được privileged EXEC mode | Sai mật khẩu `class` hoặc chưa cấu hình `enable secret` | Cấu hình lại `enable secret class` |
| Không yêu cầu console password | Thiếu lệnh `login` dưới `line console 0` | Thêm `password cisco` và `login` |
| Mất cấu hình sau khi khởi động lại | Chưa lưu cấu hình xuống NVRAM | Chạy `copy running-config startup-config` |
| Ping PC1 đến PC2 thất bại | Sai IP, subnet mask hoặc cáp kết nối | Kiểm tra IP Configuration và trạng thái link |

## 8. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| Hostname S1 | CLI hiển thị `S1` | Đạt |
| Hostname S2 | CLI hiển thị `S2` | Đạt |
| Console password | Vào console cần nhập `cisco` | Đạt |
| Privileged EXEC password | Lệnh `enable` cần nhập `class` | Đạt |
| Banner MOTD | Hiển thị cảnh báo truy cập trái phép | Đạt |
| IP PC1 | `192.168.1.1/24` | Đạt |
| IP PC2 | `192.168.1.2/24` | Đạt |
| IP VLAN 1 S1 | `192.168.1.253/24`, trạng thái `up/up` | Đạt |
| IP VLAN 1 S2 | `192.168.1.254/24`, trạng thái `up/up` | Đạt |
| Ping PC1 ↔ PC2 | Thành công | Đạt |
| Ping PC tới S1/S2 | Thành công | Đạt |
| Lưu cấu hình | `copy running-config startup-config` hoàn tất | Đạt |

- [ ] Ảnh topology ban đầu
- [ ] Ảnh cấu hình hostname/password/banner trên S1
- [ ] Ảnh cấu hình hostname/password/banner trên S2
- [ ] Ảnh IP Configuration của PC1
- [ ] Ảnh IP Configuration của PC2
- [ ] Ảnh `show ip interface brief` trên S1/S2
- [ ] Ảnh ping từ PC1 tới PC2, S1, S2
- [ ] Ảnh Check Results đạt 100%

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
      <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 2.7.6 Packet Tracer - Implement Basic Connectivity (Đang đọc)</strong></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/">Lab 2: 2.8.1 Video Activity - Test the Interface Assignment</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/">Lab 3: 2.8.2 Video Activity - Test End-to-End Connectivity</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/">Lab 4: 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/">Lab 5: 4.7.1 Packet Tracer - Connect the Physical Layer</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "JNCIA Junos - Lý thuyết trọng tâm"
permalink: /writeups/learn-juniper/jncia-junos/
toc: true
---
# TỔNG HỢP LÝ THUYẾT TRỌNG TÂM JNCIA-JUNOS

> Bản rút gọn trọng tâm: bỏ phần diễn giải dài dòng, giữ lại khái niệm, nguyên lý, cấu trúc cấu hình và lệnh cần nhớ.

---

## MỤC LỤC

1. Kiến trúc Junos OS
2. CLI Junos và mô hình cấu hình
3. Cấu hình ban đầu thiết bị
4. Interface trong Junos
5. Cấu hình hệ thống phụ trợ
6. Giám sát và bảo trì thiết bị
7. Routing Fundamentals
8. Static Route
9. OSPF cơ bản
10. Routing Policy
11. Firewall Filters
12. Class of Service
13. Cheat Sheet lệnh trọng tâm
14. Checklist ôn cuối

---

# 1. KIẾN TRÚC JUNOS OS

## 1.1. Junos OS là gì?

Junos OS là hệ điều hành mạng của Juniper Networks, dùng trên router, switch và security gateway.

Đặc điểm chính:

- **Modular OS**: chức năng được chia thành nhiều process riêng.
- **Protected memory**: mỗi process chạy trong vùng nhớ riêng.
- **Single source code base**: nhiều platform dùng cùng nền mã nguồn.
- **FreeBSD-based**: Junos kernel dựa trên FreeBSD UNIX.
- **Control plane và forwarding plane tách riêng**.

---

## 1.2. Control Plane và Forwarding Plane

| Thành phần | Vị trí | Vai trò |
|---|---|---|
| Control Plane | Routing Engine - RE | Chạy routing protocol, quản lý hệ thống, giữ routing table, bridging table, forwarding table chính, cung cấp CLI/J-Web |
| Forwarding Plane | Packet Forwarding Engine - PFE | Forward packet dựa trên forwarding table cục bộ |
| Internal Link | Giữa RE và PFE | RE gửi forwarding table xuống PFE, PFE gửi exception traffic lên RE khi cần |

Ghi nhớ:

- **RE** xử lý điều khiển, quản trị, routing protocol.
- **PFE** xử lý chuyển tiếp packet.
- Forwarding table được RE tạo và đồng bộ xuống PFE.

---

## 1.3. Transit Traffic và Exception Traffic

| Loại traffic | Định nghĩa | Xử lý |
|---|---|---|
| Transit traffic | Traffic đi xuyên qua thiết bị, vào một interface và ra interface khác | PFE xử lý |
| Exception traffic | Traffic gửi tới chính thiết bị hoặc cần xử lý đặc biệt | PFE hoặc RE xử lý tùy loại |

Ví dụ exception traffic:

- SSH/Telnet vào router.
- Ping tới router.
- Routing protocol packet: OSPF, BGP.
- Packet có IP options.
- Packet cần sinh ICMP error như TTL expired, destination unreachable.

---

## 1.4. Nhóm thiết bị Junos

| Nhóm | Dòng thiết bị |
|---|---|
| Routing | ACX, M, MX, PTX, T Series |
| Switching | EX, QFX Series |
| Security/Services | SRX, J Series |

---

# 2. CLI JUNOS VÀ MÔ HÌNH CẤU HÌNH

## 2.1. Cách truy cập CLI

Các cách truy cập:

- Console out-of-band.
- SSH/Telnet qua network.
- Management Ethernet port.
- J-Web qua HTTP/HTTPS.

Root login thường vào UNIX shell trước:

```bash
root@router% cli
root@router>
```

---

## 2.2. Các prompt cần nhớ

| Prompt | Mode | Chức năng |
|---|---|---|
| `user@router>` | Operational mode | show, ping, traceroute, monitor, clear, request |
| `user@router#` | Configuration mode | set, delete, edit, commit, rollback |
| `root@router%` | UNIX shell | Shell hệ thống, cần gõ `cli` để vào Junos CLI |

---

## 2.3. Operational Mode

Dùng để xem trạng thái, kiểm tra, troubleshooting.

Lệnh thường dùng:

```bash
show version
show system uptime
show chassis alarms
show interfaces terse
show route
ping 8.8.8.8 count 5
traceroute 8.8.8.8
monitor traffic interface ge-0/0/0 no-resolve
```

---

## 2.4. Configuration Mode

Vào configuration mode:

```bash
configure
```

Vào chế độ exclusive:

```bash
configure exclusive
```

Vào chế độ private:

```bash
configure private
```

Thoát:

```bash
exit
exit configuration-mode
```

---

## 2.5. Active Configuration và Candidate Configuration

| Loại cấu hình | Ý nghĩa |
|---|---|
| Active configuration | Cấu hình đang chạy trên thiết bị |
| Candidate configuration | Cấu hình tạm thời đang chỉnh sửa |

Quy trình:

```bash
configure
set system host-name R1
show | compare
commit check
commit
```

Ghi nhớ:

- Junos không áp dụng cấu hình ngay sau lệnh `set`.
- Phải `commit` để candidate config thành active config.
- `commit check` chỉ kiểm tra cú pháp.

---

## 2.6. Commit và Rollback

```bash
commit check
commit
commit comment "Configure hostname"
commit confirmed 5
rollback 0
rollback 1
show | compare
show system rollback
```

Ý nghĩa:

| Lệnh | Ý nghĩa |
|---|---|
| `commit check` | Kiểm tra cấu hình, không áp dụng |
| `commit` | Áp dụng cấu hình |
| `commit confirmed 5` | Commit tạm, tự rollback sau 5 phút nếu không xác nhận |
| `rollback 0` | Hủy thay đổi chưa commit |
| `rollback 1` | Quay về bản cấu hình trước lần commit gần nhất |
| `show | compare` | So sánh candidate với active config |

---

## 2.7. Điều hướng configuration hierarchy

| Lệnh | Ý nghĩa |
|---|---|
| `edit system` | Vào nhánh system |
| `edit interfaces ge-0/0/0` | Vào nhánh interface |
| `up` | Lên 1 cấp |
| `up 2` | Lên 2 cấp |
| `top` | Về đầu cây `[edit]` |
| `exit` | Thoát cấp hiện tại hoặc thoát configuration mode |
| `run <command>` | Chạy lệnh operational trong configuration mode |

Ví dụ:

```bash
edit interfaces ge-0/0/0
up
top
run show interfaces terse
```

---

## 2.8. Hiển thị cấu hình

```bash
show
show system services
show | display set
show | compare
show | no-more
show | match ssh
show | except inactive
show | find ospf
```

| Pipe | Ý nghĩa |
|---|---|
| `| display set` | Hiển thị dạng lệnh set |
| `| compare` | So sánh thay đổi |
| `| match` | Lọc dòng có từ khóa |
| `| except` | Loại dòng có từ khóa |
| `| find` | Hiển thị từ vị trí match |
| `| count` | Đếm dòng |
| `| no-more` | Hiển thị toàn bộ, không phân trang |

---

## 2.9. Chỉnh sửa cấu hình

```bash
set system services ssh
delete system services telnet
deactivate interfaces ge-0/0/1
activate interfaces ge-0/0/1
copy interfaces ge-0/0/0 to ge-0/0/1
rename interfaces ge-0/0/1 to ge-0/0/2
replace pattern OLD with NEW
wildcard delete interfaces ge-1/*
```

| Lệnh | Ý nghĩa |
|---|---|
| `set` | Thêm/sửa cấu hình |
| `delete` | Xóa cấu hình |
| `deactivate` | Tắt tạm cấu hình nhưng giữ lại trong file |
| `activate` | Bật lại cấu hình đã deactivate |
| `copy` | Copy nhánh cấu hình |
| `rename` | Đổi tên object |
| `replace pattern` | Thay chuỗi |
| `wildcard delete` | Xóa theo mẫu |

---

## 2.10. Load và Save Configuration

```bash
save /var/tmp/backup.conf
load override /var/tmp/config.conf
load merge /var/tmp/config-part.conf
load set /var/tmp/config-set.txt
load merge terminal
commit check
commit
```

| Lệnh | Ý nghĩa |
|---|---|
| `save` | Lưu cấu hình ra file |
| `load override` | Thay toàn bộ candidate config |
| `load merge` | Gộp cấu hình vào candidate |
| `load replace` | Thay phần có marker replace |
| `load set` | Nạp file dạng set/delete |

---

# 3. CẤU HÌNH BAN ĐẦU THIẾT BỊ

## 3.1. Root Password

```bash
configure
set system root-authentication plain-text-password
commit
```

Ghi nhớ:

- Junos yêu cầu root authentication trước khi commit cấu hình trên thiết bị mới/factory default.
- `plain-text-password`: nhập password dạng thường, Junos tự mã hóa khi lưu.
- `encrypted-password`: nhập chuỗi hash có sẵn.

---

## 3.2. Hostname, Domain, DNS

```bash
set system host-name R1
set system domain-name lab.local
set system name-server 8.8.8.8
set system name-server 1.1.1.1
commit
```

---

## 3.3. User Account và Login Class

```bash
set system login user netadmin class super-user authentication plain-text-password
set system login user noc class read-only authentication plain-text-password
commit
```

| Class | Quyền |
|---|---|
| `super-user` | Toàn quyền |
| `operator` | Quyền vận hành, hạn chế cấu hình |
| `read-only` | Chỉ xem |
| `unauthorized` | Không có quyền thao tác đáng kể |

---

## 3.4. SSH, Telnet, J-Web, NETCONF

```bash
set system services ssh
set system services netconf ssh
set system services web-management https system-generated-certificate
set system services telnet
commit
```

Ghi nhớ:

- SSH dùng cho CLI bảo mật.
- Telnet truyền cleartext.
- NETCONF over SSH dùng cho automation.
- J-Web dùng HTTP/HTTPS.

---

## 3.5. Management Interface

Tên management interface tùy platform: `fxp0`, `me0`, `em0`.

```bash
set interfaces fxp0 unit 0 family inet address 192.168.100.10/24
set routing-options static route 192.168.200.0/24 next-hop 192.168.100.1
commit
```

---

## 3.6. Rescue Configuration

Lưu rescue config:

```bash
request system configuration rescue save
```

Khôi phục rescue config:

```bash
configure
rollback rescue
commit
```

Xóa rescue config:

```bash
request system configuration rescue delete
```

---

# 4. INTERFACE TRONG JUNOS

## 4.1. Cấu trúc tên interface

Dạng tổng quát:

```text
<type>-<FPC>/<PIC>/<port>.<unit>
```

Ví dụ:

```text
ge-0/0/0.0
xe-0/0/1.0
lo0.0
fxp0.0
```

| Thành phần                  | Ý nghĩa               |
| --------------------------- | --------------------- |
| `ge`, `xe`, `et`, `fe`      | Loại interface vật lý |
| `0/0/0`                     | Vị trí FPC/PIC/port   |
| `.0`                        | Logical unit          |
| `family inet`               | IPv4                  |
| `family inet6`              | IPv6                  |
| `family ethernet-switching` | Layer 2 switching     |
| `family mpls`               | MPLS                  |

---

## 4.2. Physical Interface và Logical Interface

| Loại | Ví dụ | Ý nghĩa |
|---|---|---|
| Physical interface | `ge-0/0/0` | Cổng vật lý |
| Logical interface | `ge-0/0/0.0` | Unit logic dùng để cấu hình protocol family/IP |

Cấu hình IPv4:

```bash
set interfaces ge-0/0/0 description "Link-to-R2"
set interfaces ge-0/0/0 unit 0 family inet address 10.0.12.1/30
commit
```

Cấu hình IPv6:

```bash
set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8:1::1/64
commit
```

---

## 4.3. Các loại interface thường gặp

| Loại | Ví dụ | Chức năng |
|---|---|---|
| Network interface | `ge-0/0/0`, `xe-0/0/0`, `et-0/0/0` | Kết nối mạng |
| Management interface | `fxp0`, `me0`, `em0` | Quản trị thiết bị |
| Loopback | `lo0.0` | Router ID, quản trị, filter RE |
| Tunnel/services | `gr`, `ip`, `ls`, `sp` | Tunnel/dịch vụ đặc biệt |
| Internal | `fxp1`, `em0` | Giao tiếp nội bộ platform |

---

## 4.4. Disable/Bật lại Interface

Disable:

```bash
set interfaces ge-0/0/0 disable
commit
```

Bật lại:

```bash
delete interfaces ge-0/0/0 disable
commit
```

---

## 4.5. Lệnh kiểm tra interface

```bash
show interfaces terse
show interfaces ge-0/0/0 terse
show interfaces ge-0/0/0 extensive
show interfaces descriptions
show interfaces diagnostics optics
monitor interface ge-0/0/0
monitor interface traffic
clear interfaces statistics ge-0/0/0
```

| Lệnh | Ý nghĩa |
|---|---|
| `show interfaces terse` | Xem nhanh admin/link/protocol/IP |
| `show interfaces extensive` | Xem chi tiết counters/errors |
| `show interfaces descriptions` | Xem mô tả interface |
| `show interfaces diagnostics optics` | Xem thông số quang nếu hỗ trợ |
| `monitor interface traffic` | Xem lưu lượng realtime |
| `clear interfaces statistics` | Xóa counters |

---

# 5. CẤU HÌNH HỆ THỐNG PHỤ TRỢ

## 5.1. Authentication: Local, RADIUS, TACACS+

| Cơ chế | Ý nghĩa |
|---|---|
| Local | User/password lưu trên thiết bị |
| RADIUS | Xác thực tập trung qua RADIUS server |
| TACACS+ | Xác thực và phân quyền tập trung chi tiết |

Ví dụ TACACS+:

```bash
set system authentication-order [ tacplus password ]
set system tacplus-server 10.10.10.10 secret "SECRET"
set system login user backup-admin class super-user authentication plain-text-password
commit
```

---

## 5.2. Login Class và Permission

```bash
set system login class NOC permissions [ view network trace ]
set system login user noc1 class NOC authentication plain-text-password
commit
```

Permission thường gặp:

- `view`
- `network`
- `configure`
- `admin`
- `maintenance`
- `trace`
- `firewall`
- `routing`

---

## 5.3. Syslog

Cấu hình:

```bash
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog host 192.168.100.50 any notice
set system syslog user * any emergency
commit
```

Lệnh xem log:

```bash
show log messages
show log messages | last 50
show log messages | match ssh
show log interactive-commands
```

Severity syslog:

| Mức | Tên |
|---|---|
| 0 | emergency |
| 1 | alert |
| 2 | critical |
| 3 | error |
| 4 | warning |
| 5 | notice |
| 6 | info |
| 7 | debug |

---

## 5.4. Tracing

Tracing dùng để ghi chi tiết hoạt động của process/protocol.

Ví dụ OSPF trace:

```bash
set protocols ospf traceoptions file ospf.log size 1m files 3
set protocols ospf traceoptions flag error
set protocols ospf traceoptions flag event
commit
show log ospf.log
```

Tắt tracing:

```bash
delete protocols ospf traceoptions
commit
```

---

## 5.5. NTP

Cấu hình:

```bash
set system time-zone Asia/Ho_Chi_Minh
set system ntp server 192.168.100.10 prefer
set system ntp server 192.168.100.11
commit
```

Kiểm tra:

```bash
show ntp associations
show ntp status
show system uptime
```

---

## 5.6. Backup cấu hình tự động

Backup mỗi lần commit:

```bash
set system archival configuration transfer-on-commit
set system archival configuration archive-sites "scp://backup@192.168.100.20:/backup/junos" password "PASSWORD"
commit
```

Backup theo chu kỳ:

```bash
set system archival configuration transfer-interval 1440
```

---

## 5.7. SNMP

Cấu hình cơ bản:

```bash
set snmp location "DataCenter-Rack01"
set snmp contact "noc@example.com"
set snmp community MONITOR authorization read-only
set snmp trap-group NMS targets 192.168.100.30
commit
```

Kiểm tra:

```bash
show snmp statistics
show configuration snmp
```

Khái niệm:

| Thành phần | Ý nghĩa |
|---|---|
| SNMP manager | Hệ thống giám sát |
| SNMP agent | Thiết bị Junos |
| MIB/OID | Cây thông tin quản lý |
| Trap/Inform | Cảnh báo gửi từ thiết bị tới manager |

---

# 6. GIÁM SÁT VÀ BẢO TRÌ THIẾT BỊ

## 6.1. Kiểm tra hệ thống

```bash
show version
show system uptime
show system users
show system storage
show system memory
show system processes extensive
show chassis hardware
show chassis environment
show chassis alarms
show system alarms
```

| Lệnh | Ý nghĩa |
|---|---|
| `show version` | Phiên bản Junos/platform |
| `show system uptime` | Uptime |
| `show system storage` | Dung lượng disk |
| `show system processes extensive` | Process, CPU, memory |
| `show chassis hardware` | Inventory phần cứng |
| `show chassis environment` | Nguồn, quạt, nhiệt độ |
| `show chassis alarms` | Alarm phần cứng |
| `show system alarms` | Alarm hệ thống |

---

## 6.2. Kiểm tra interface và traffic

```bash
show interfaces terse
show interfaces descriptions
show interfaces ge-0/0/0 extensive
show interfaces diagnostics optics
monitor interface ge-0/0/0
monitor interface traffic
```

Counters cần chú ý:

- Input errors.
- Output errors.
- CRC errors.
- Drops.
- Framing errors.
- Carrier transitions.

---

## 6.3. Ping và Traceroute

```bash
ping 8.8.8.8 count 5
ping 8.8.8.8 rapid count 20
ping 8.8.8.8 source 192.168.1.1 count 5
traceroute 8.8.8.8
traceroute 8.8.8.8 source 192.168.1.1
```

---

## 6.4. Monitor Traffic

```bash
monitor traffic interface ge-0/0/0 no-resolve
monitor traffic interface ge-0/0/0 matching "host 10.1.1.1" no-resolve
monitor traffic interface ge-0/0/0 matching "icmp" no-resolve
monitor traffic interface ge-0/0/0 matching "port 22" no-resolve
monitor traffic interface ge-0/0/0 write-file /var/tmp/capture.pcap size 10m
```

---

## 6.5. Software Upgrade

```bash
show version
show system storage
file checksum md5 /var/tmp/junos-install.tgz
request system software add /var/tmp/junos-install.tgz reboot
```

Sau reboot kiểm tra:

```bash
show version
show interfaces terse
show route
show chassis alarms
show system alarms
```

Dọn storage:

```bash
request system storage cleanup
```

Reboot/halt:

```bash
request system reboot
request system halt
```

Zeroize:

```bash
request system zeroize
```

---

# 7. ROUTING FUNDAMENTALS

## 7.1. Routing là gì?

Routing là quá trình chuyển dữ liệu giữa các mạng Layer 3.

Điều kiện để routing hoạt động:

1. Có đường truyền end-to-end.
2. Thiết bị Layer 3 có thông tin định tuyến phù hợp.
3. Host có default gateway đúng khi đi ngoài subnet.
4. Cả chiều đi và chiều về đều có route.

---

## 7.2. Routing Table và Forwarding Table

| Bảng | Vai trò | Lệnh kiểm tra |
|---|---|---|
| Routing table | Chứa route học từ direct, local, static, OSPF, BGP... | `show route` |
| Forwarding table | Chứa thông tin PFE dùng để forward packet | `show route forwarding-table` |

Ghi nhớ:

- Routing table nằm ở RE.
- Forwarding table được cài xuống PFE.
- Active route thường được đưa vào forwarding table.

---

## 7.3. Route Sources và Route Preference

Preference càng thấp càng ưu tiên.

| Route source | Default preference |
|---|---:|
| Direct | 0 |
| Local | 0 |
| Static | 5 |
| OSPF internal | 10 |
| RIP | 100 |
| OSPF external | 150 |
| BGP | 170 |

Ví dụ:

- Static route preference 5 tốt hơn OSPF internal preference 10.
- Direct/local route luôn rất ưu tiên.

---

## 7.4. Active, Holddown, Hidden Route

| Loại route | Ý nghĩa |
|---|---|
| Active | Route được chọn để forward |
| Holddown | Route đang ở trạng thái chờ |
| Hidden | Route không dùng được do next-hop invalid hoặc policy |

Lệnh:

```bash
show route
show route hidden
show route protocol ospf
show route 10.10.10.0/24 exact
```

---

## 7.5. Longest Prefix Match

Khi packet match nhiều route, Junos chọn prefix cụ thể nhất.

| Route có trong bảng | Packet đích | Route được chọn |
|---|---|---|
| `0.0.0.0/0`, `10.0.0.0/8`, `10.1.1.0/24` | `10.1.1.50` | `10.1.1.0/24` |
| `0.0.0.0/0`, `10.0.0.0/8` | `10.2.2.2` | `10.0.0.0/8` |
| `0.0.0.0/0` | `8.8.8.8` | `0.0.0.0/0` |

---

## 7.6. Routing Tables phổ biến

| Routing table | Chức năng |
|---|---|
| `inet.0` | IPv4 unicast |
| `inet6.0` | IPv6 unicast |
| `inet.1` | Multicast forwarding cache |
| `inet.2` | MBGP routes cho RPF check |
| `inet.3` | MPLS path information |
| `mpls.0` | MPLS next-hops |

---

## 7.7. Routing Instances

Routing instance là không gian định tuyến logic riêng trong một thiết bị Junos.

| Loại instance | Chức năng |
|---|---|
| `master` | Instance mặc định |
| `virtual-router` | Router logic không liên quan VPN |
| `vrf` | Layer 3 VPN |
| `vpls` | LAN multipoint trong VPN |
| `l2vpn` | Layer 2 VPN |
| `forwarding` | Filter-based forwarding |
| `no-forwarding` | Tách routing cho mục đích quản trị |

Cấu hình:

```bash
set routing-instances CUST-A instance-type virtual-router
set routing-instances CUST-A interface ge-0/0/1.0
set routing-instances CUST-A routing-options static route 0.0.0.0/0 next-hop 10.10.10.1
commit
```

Kiểm tra:

```bash
show route instance
show route table CUST-A.inet.0
ping 8.8.8.8 routing-instance CUST-A
traceroute 8.8.8.8 routing-instance CUST-A
```

---

# 8. STATIC ROUTE

## 8.1. Cấu hình Static Route

Default route:

```bash
set routing-options static route 0.0.0.0/0 next-hop 172.30.25.1
```

Route cụ thể:

```bash
set routing-options static route 10.10.10.0/24 next-hop 192.168.1.2
```

IPv6 static route:

```bash
set routing-options rib inet6.0 static route ::/0 next-hop 2001:db8:1::1
```

Kiểm tra:

```bash
show route protocol static
show route 0.0.0.0/0
show route 10.10.10.0/24 exact
```

---

## 8.2. Next-hop, Reject, Discard

| Next-hop type | Ý nghĩa |
|---|---|
| `next-hop <ip>` | Forward tới router kế tiếp |
| `discard` | Drop im lặng |
| `reject` | Drop và gửi ICMP unreachable |

Ví dụ:

```bash
set routing-options static route 203.0.113.0/24 discard
set routing-options static route 198.51.100.0/24 reject
commit
```

---

## 8.3. Indirect Next-hop và Resolve

Mặc định Junos yêu cầu next-hop static route reachable qua direct route.

Dùng `resolve` khi next-hop không trực tiếp connected:

```bash
set routing-options static route 172.20.3.0/24 next-hop 172.25.1.6 resolve
commit
```

---

## 8.4. Qualified Next-hop

Dùng để đặt preference riêng cho từng next-hop.

```bash
set routing-options static route 0.0.0.0/0 next-hop 172.30.25.1
set routing-options static route 0.0.0.0/0 qualified-next-hop 172.30.25.5 preference 7
commit
```

Ghi nhớ:

- Static route mặc định preference 5.
- Preference thấp hơn được ưu tiên.
- Qualified next-hop thường dùng cho primary/backup static route.

---

# 9. OSPF CƠ BẢN

## 9.1. OSPF là gì?

OSPF là Interior Gateway Protocol dạng link-state.

Khái niệm chính:

| Thuật ngữ | Ý nghĩa |
|---|---|
| LSA | Link-State Advertisement |
| LSDB | Link-State Database |
| SPF/Dijkstra | Thuật toán tính đường đi ngắn nhất |
| Area | Vùng OSPF logic |
| Backbone area | Area 0.0.0.0 |
| Cost/Metric | Chi phí đường đi |
| Router ID | Định danh router trong OSPF |

---

## 9.2. OSPF Area

- Area 0.0.0.0 là backbone area.
- Các area khác cần kết nối về backbone.
- Router nằm trong nhiều area gọi là ABR.
- Mỗi area có LSDB riêng.

---

## 9.3. Cấu hình OSPF cơ bản

```bash
set interfaces lo0 unit 0 family inet address 192.168.100.1/32
set routing-options router-id 192.168.100.1
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
set protocols ospf area 0.0.0.0 interface ge-0/0/1.0
set protocols ospf area 0.0.0.0 interface lo0.0 passive
commit
```

Ghi nhớ:

- Junos cấu hình OSPF trên logical interface như `ge-0/0/0.0`.
- `passive` quảng bá network nhưng không hình thành neighbor.
- `area 0` có thể hiển thị lại thành `0.0.0.0`.

---

## 9.4. Kiểm tra OSPF

```bash
show ospf neighbor
show ospf neighbor detail
show ospf interface
show ospf interface detail
show ospf database
show ospf database detail
show route protocol ospf
show ospf log
```

Field trong `show ospf neighbor`:

| Field | Ý nghĩa |
|---|---|
| Address | IP neighbor |
| Interface | Interface reach neighbor |
| State | Trạng thái neighbor |
| ID | Router ID neighbor |
| Pri | Priority bầu DR/BDR |
| Dead | Thời gian còn lại trước khi neighbor down |

---

## 9.5. Trạng thái OSPF Neighbor

| State | Ý nghĩa |
|---|---|
| Down | Chưa nhận hello |
| Init | Đã nhận hello nhưng chưa thấy mình trong hello |
| 2-Way | Hai bên thấy nhau |
| ExStart | Bắt đầu thương lượng trao đổi database |
| Exchange | Đang trao đổi DBD |
| Loading | Đang yêu cầu/nhận thêm LSA |
| Full | LSDB đồng bộ, adjacency hoàn tất |

---

## 9.6. Checklist lỗi OSPF

- Interface up/up chưa.
- IP/mask hai đầu cùng subnet chưa.
- Đúng logical interface chưa.
- Area hai đầu giống nhau chưa.
- Có bị passive nhầm không.
- Firewall filter có chặn OSPF không.
- MTU mismatch không.
- Hello/dead timer mismatch không.
- Authentication mismatch không.
- Router ID bị trùng không.

---

# 10. ROUTING POLICY

## 10.1. Routing Policy là gì?

Routing policy kiểm soát thông tin định tuyến.

Chức năng:

- Accept/reject route.
- Import route vào routing table.
- Export route ra protocol khác.
- Chỉnh attribute của route.
- Lọc route theo prefix/protocol/next-hop/attribute.

---

## 10.2. Import Policy và Export Policy

| Loại | Áp dụng | Ảnh hưởng |
|---|---|---|
| Import policy | Khi route đi từ protocol/neighbor vào routing table | Có thể ảnh hưởng route selection local |
| Export policy | Khi route đi từ routing table ra protocol/neighbor | Chỉ export active route |

Ghi nhớ:

- Export policy không export inactive route.
- OSPF internal route không bị import policy chặn theo kiểu phá LSDB.
- Muốn redistribute route vào OSPF cần export policy.

---

## 10.3. Cấu trúc Policy Statement

```bash
policy-options {
    policy-statement EXPORT-STATIC {
        term STATIC-ROUTES {
            from protocol static;
            then accept;
        }
        term REJECT-OTHERS {
            then reject;
        }
    }
}
```

Cấu trúc:

| Thành phần | Ý nghĩa |
|---|---|
| `policy-statement` | Tên policy |
| `term` | Điều kiện + hành động |
| `from` | Điều kiện match |
| `then` | Hành động |
| `accept` | Cho route qua |
| `reject` | Chặn route |

---

## 10.4. Logic Match trong `from`

- Nhiều giá trị cùng một tiêu chí: OR.
- Nhiều tiêu chí khác nhau: AND.
- Không có `from`: match tất cả.

Ví dụ:

```bash
from protocol [ static direct ]
```

Nghĩa là static OR direct.

```bash
from protocol static
from route-filter 10.0.0.0/8 orlonger
```

Nghĩa là static AND thuộc 10.0.0.0/8 hoặc subnet dài hơn.

---

## 10.5. Prefix-list

```bash
set policy-options prefix-list MGMT-NETS 192.168.100.0/24
set policy-options prefix-list MGMT-NETS 192.168.200.0/24
set policy-options policy-statement ACCEPT-MGMT term T1 from prefix-list MGMT-NETS
set policy-options policy-statement ACCEPT-MGMT term T1 then accept
```

---

## 10.6. Route-filter

| Match type | Ý nghĩa |
|---|---|
| `exact` | Match đúng prefix và mask |
| `longer` | Match subnet dài hơn, không match prefix gốc |
| `orlonger` | Match prefix gốc và subnet dài hơn |
| `upto /x` | Match từ prefix gốc đến tối đa /x |
| `prefix-length-range /x-/y` | Match độ dài prefix trong khoảng /x đến /y |

Ví dụ:

```bash
set policy-options policy-statement EXPORT-10 term T1 from route-filter 10.0.0.0/8 orlonger
set policy-options policy-statement EXPORT-10 term T1 then accept
set policy-options policy-statement EXPORT-10 term REJECT then reject
```

---

## 10.7. Apply Policy vào Protocol

Export static vào OSPF:

```bash
set policy-options policy-statement EXPORT-STATIC term STATIC from protocol static
set policy-options policy-statement EXPORT-STATIC term STATIC then accept
set policy-options policy-statement EXPORT-STATIC term REJECT then reject
set protocols ospf export EXPORT-STATIC
commit
```

Apply vào BGP group/neighbor:

```bash
set protocols bgp group EBGP export EXPORT-POLICY
set protocols bgp group EBGP import IMPORT-POLICY
```

---

## 10.8. Action thường dùng

```bash
then accept
then reject
then next term
then next policy
then preference 100
then metric 50
then community add COMMUNITY-NAME
```

| Action | Ý nghĩa |
|---|---|
| `accept` | Chấp nhận route |
| `reject` | Từ chối route |
| `next term` | Sang term tiếp theo |
| `next policy` | Sang policy tiếp theo |
| `preference` | Chỉnh preference |
| `metric` | Chỉnh metric |
| `community add` | Gắn BGP community |

---

# 11. FIREWALL FILTERS

## 11.1. Firewall Filter là gì?

Firewall filter trong Junos là stateless packet filter.

Đặc điểm:

- Xử lý packet theo từng term từ trên xuống.
- Match điều kiện trong `from`.
- Thực hiện action trong `then`.
- Nếu không match term nào, mặc định discard.
- Có thể apply input/output trên interface.
- Có thể apply vào `lo0` để bảo vệ RE.

---

## 11.2. Cấu trúc Firewall Filter

```bash
firewall {
    family inet {
        filter PROTECT-RE {
            term ALLOW-SSH {
                from {
                    source-address {
                        192.168.100.0/24;
                    }
                    protocol tcp;
                    destination-port ssh;
                }
                then accept;
            }
            term DENY-OTHER {
                then discard;
            }
        }
    }
}
```

---

## 11.3. Match Condition thường dùng

| Match | Ý nghĩa |
|---|---|
| `source-address` | Địa chỉ nguồn |
| `destination-address` | Địa chỉ đích |
| `protocol` | Protocol: tcp, udp, icmp, ospf |
| `source-port` | Source port |
| `destination-port` | Destination port |
| `tcp-flags` | TCP flags |
| `icmp-type` | ICMP type |
| `icmp-code` | ICMP code |
| `packet-length` | Kích thước packet |

---

## 11.4. Action thường dùng

| Action | Ý nghĩa |
|---|---|
| `accept` | Cho packet đi tiếp |
| `discard` | Drop im lặng |
| `reject` | Drop và gửi phản hồi |
| `count` | Tăng counter |
| `log` | Ghi log local |
| `syslog` | Gửi syslog |
| `next term` | Tiếp tục kiểm tra term sau |
| `policer` | Giới hạn traffic |
| `forwarding-class` | Gán forwarding class |
| `loss-priority` | Gán loss priority |

---

## 11.5. Apply Firewall Filter

Input filter:

```bash
set interfaces ge-0/0/0 unit 0 family inet filter input FILTER-IN
```

Output filter:

```bash
set interfaces ge-0/0/0 unit 0 family inet filter output FILTER-OUT
```

Filter bảo vệ Routing Engine:

```bash
set interfaces lo0 unit 0 family inet filter input PROTECT-RE
commit confirmed 5
```

---

## 11.6. Filter bảo vệ Routing Engine mẫu

```bash
set firewall family inet filter PROTECT-RE term ALLOW-SSH from source-address 192.168.100.0/24
set firewall family inet filter PROTECT-RE term ALLOW-SSH from protocol tcp
set firewall family inet filter PROTECT-RE term ALLOW-SSH from destination-port ssh
set firewall family inet filter PROTECT-RE term ALLOW-SSH then accept

set firewall family inet filter PROTECT-RE term ALLOW-OSPF from protocol ospf
set firewall family inet filter PROTECT-RE term ALLOW-OSPF then accept

set firewall family inet filter PROTECT-RE term ALLOW-ICMP from protocol icmp
set firewall family inet filter PROTECT-RE term ALLOW-ICMP then accept

set firewall family inet filter PROTECT-RE term DENY-OTHER then discard
set interfaces lo0 unit 0 family inet filter input PROTECT-RE
commit confirmed 5
```

Kiểm tra:

```bash
show firewall
show firewall filter PROTECT-RE
show configuration firewall | display set
show configuration interfaces lo0 | display set
```

---

## 11.7. Unicast RPF

Unicast Reverse Path Forwarding kiểm tra đường ngược về source IP dựa trên routing table.

Mục đích:

- Chống source spoofing.
- Drop packet có source không hợp lệ.

Ghi nhớ:

- Strict uRPF yêu cầu đường về source đi qua đúng interface nhận packet.
- Loose uRPF chỉ yêu cầu có route về source.
- Asymmetric routing có thể gây drop nhầm với strict uRPF.

---

# 12. CLASS OF SERVICE

## 12.1. CoS là gì?

Class of Service dùng để phân loại và ưu tiên traffic khi có congestion.

Ghi nhớ:

- CoS không tăng băng thông vật lý.
- CoS quyết định traffic nào được ưu tiên khi congestion.
- CoS thường dựa trên queue, scheduler, classifier, rewrite rule, policer.

---

## 12.2. Thành phần CoS

| Thành phần | Ý nghĩa |
|---|---|
| Forwarding class | Nhóm dịch vụ/queue |
| Loss priority | Mức ưu tiên khi drop |
| Classifier | Phân loại packet |
| BA classifier | Phân loại dựa trên DSCP, IP precedence, MPLS EXP, 802.1p |
| Multifield classifier | Phân loại dựa trên nhiều trường packet bằng firewall filter |
| Rewrite rule | Đánh dấu lại packet khi đi ra |
| Policer | Giới hạn tốc độ traffic |
| Scheduler | Điều khiển queue, bandwidth, buffer, priority |
| Scheduler map | Gắn scheduler vào forwarding class |

---

## 12.3. Quy trình CoS

1. Packet vào interface.
2. Classifier phân loại packet.
3. Packet được gán forwarding class và loss priority.
4. Policer xử lý nếu vượt ngưỡng.
5. Packet vào queue tương ứng.
6. Scheduler quyết định queue được gửi.
7. Rewrite rule đánh dấu packet khi đi ra.

---

## 12.4. Lệnh kiểm tra CoS

```bash
show class-of-service interface
show interfaces queue
show interfaces ge-0/0/0 extensive | match queue
show configuration class-of-service
```

---

# 13. CHEAT SHEET LỆNH TRỌNG TÂM

## 13.1. Cấu hình an toàn

```bash
configure
show | compare
commit check
commit confirmed 5
commit
rollback 1
commit
exit
```

---

## 13.2. Kiểm tra thiết bị

```bash
show version
show system uptime
show chassis alarms
show system alarms
show chassis hardware
show chassis environment
show system storage
show system processes extensive
show log messages | last 50
```

---

## 13.3. Kiểm tra interface

```bash
show interfaces terse
show interfaces descriptions
show interfaces ge-0/0/0 extensive
show interfaces diagnostics optics
monitor interface traffic
clear interfaces statistics ge-0/0/0
```

---

## 13.4. Kiểm tra routing

```bash
show route
show route 0.0.0.0/0
show route 8.8.8.8
show route protocol direct
show route protocol local
show route protocol static
show route protocol ospf
show route forwarding-table
show route hidden
```

---

## 13.5. Static route

```bash
set routing-options static route 0.0.0.0/0 next-hop 192.168.1.254
set routing-options static route 10.10.10.0/24 next-hop 192.168.1.2
set routing-options static route 203.0.113.0/24 discard
set routing-options static route 198.51.100.0/24 reject
show route protocol static
```

---

## 13.6. OSPF

```bash
set protocols ospf area 0 interface ge-0/0/0.0
set protocols ospf area 0 interface lo0.0 passive
show ospf neighbor
show ospf interface
show ospf database
show route protocol ospf
show log messages | match OSPF
```

---

## 13.7. Routing policy

```bash
set policy-options policy-statement EXPORT-STATIC term STATIC from protocol static
set policy-options policy-statement EXPORT-STATIC term STATIC then accept
set policy-options policy-statement EXPORT-STATIC term REJECT then reject
set protocols ospf export EXPORT-STATIC
show configuration policy-options | display set
```

---

## 13.8. Firewall filter

```bash
show firewall
show firewall filter PROTECT-RE
show configuration firewall | display set
show configuration interfaces lo0 | display set
clear firewall filter PROTECT-RE
```

---

## 13.9. Syslog, NTP, SNMP

```bash
show log messages
show log interactive-commands
show ntp associations
show ntp status
show snmp statistics
show system connections
show system users
```

---

## 13.10. Ping, traceroute, packet capture

```bash
ping 8.8.8.8 count 5
ping 8.8.8.8 source 192.168.1.1 count 5
traceroute 8.8.8.8
traceroute 8.8.8.8 source 192.168.1.1
monitor traffic interface ge-0/0/0 no-resolve
monitor traffic interface ge-0/0/0 matching "icmp" no-resolve
```

---


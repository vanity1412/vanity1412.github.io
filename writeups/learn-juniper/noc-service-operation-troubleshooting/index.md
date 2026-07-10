---
layout: page-toc
title: "Juniper Junos cho NOC / Service Operation"
permalink: /writeups/learn-juniper/noc-service-operation-troubleshooting/
toc: true
---
# JUNIPER JUNOS CHO NOC / SERVICE OPERATION

Tài liệu tổng hợp các lệnh cấu hình, kiểm tra và troubleshooting Juniper Junos dành cho hướng **NOC/Service Operation**, đặc biệt phù hợp với môi trường ISP, Data Center và hệ thống mạng doanh nghiệp.

---

## 1. Quản lý cấu hình Junos

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `configure` | Vào Configuration Mode để chỉnh cấu hình. Dấu nhắc chuyển từ `>` sang `#`. |
| `show configuration` | Xem toàn bộ cấu hình hiện tại của thiết bị. |
| `show configuration \| display set` | Hiển thị cấu hình dưới dạng từng lệnh `set`, dễ sao lưu và sao chép. |
| `show \| compare` | So sánh cấu hình đang sửa với cấu hình đang chạy. Luôn kiểm tra trước khi commit. |
| `commit check` | Kiểm tra cú pháp và tính hợp lệ của cấu hình nhưng chưa áp dụng. |
| `commit` | Áp dụng cấu hình mới. |
| `commit confirmed 5` | Áp dụng tạm thời trong 5 phút. Nếu mất kết nối và không commit lại, thiết bị tự rollback. Rất nên dùng khi cấu hình từ xa. |
| `commit confirmed 10` | Tương tự nhưng thời gian chờ là 10 phút. |
| `rollback 0` | Hủy toàn bộ thay đổi chưa commit. |
| `rollback 1` | Nạp lại cấu hình của lần commit trước. |
| `show system commit` | Xem lịch sử commit, thời gian và tài khoản thực hiện. |
| `request system configuration rescue save` | Lưu cấu hình hiện tại làm cấu hình cứu hộ. |
| `rollback rescue` | Khôi phục cấu hình rescue khi cấu hình hiện tại gặp lỗi nghiêm trọng. |
| `exit` | Thoát khỏi cấp cấu hình hiện tại hoặc thoát Configuration Mode. |

---

## 2. Kiểm tra nhanh tình trạng thiết bị

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `show system alarms` | Xem cảnh báo hệ thống như lỗi license, cấu hình hoặc hệ điều hành. |
| `show chassis alarms` | Xem cảnh báo phần cứng: nguồn, quạt, nhiệt độ, card. |
| `show chassis hardware` | Kiểm tra model, serial, FPC, PIC, module và transceiver. |
| `show chassis environment` | Kiểm tra nhiệt độ, trạng thái quạt và nguồn. |
| `show chassis routing-engine` | Kiểm tra CPU, RAM, nhiệt độ và trạng thái Routing Engine. |
| `show system uptime` | Xem thời gian thiết bị hoạt động và lần reboot gần nhất. |
| `show system users` | Xem tài khoản nào đang đăng nhập. |
| `show system processes extensive` | Kiểm tra tiến trình sử dụng CPU hoặc RAM cao. |
| `show system storage` | Kiểm tra dung lượng ổ đĩa. Dùng khi thiết bị không lưu log hoặc không nâng cấp được Junos. |
| `show version` | Kiểm tra model thiết bị và phiên bản Junos. |
| `request support information` | Thu thập thông tin tổng thể phục vụ phân tích hoặc gửi TAC. Output rất dài. |

### Quy trình kiểm tra nhanh

```bash
show system alarms
show chassis alarms
show chassis environment
show chassis routing-engine
show system storage
show interfaces terse
```

---

## 3. Interface và đường truyền

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `show interfaces terse` | Xem nhanh trạng thái Admin và Link của tất cả interface. |
| `show interfaces descriptions` | Xem trạng thái interface cùng phần mô tả kết nối. |
| `show interfaces ge-0/0/0` | Xem thông tin cơ bản của một cổng. |
| `show interfaces ge-0/0/0 extensive` | Xem chi tiết traffic, error, drop, flap và queue. |
| `show interfaces ge-0/0/0 extensive \| match error` | Lọc các dòng liên quan lỗi interface. |
| `show interfaces ge-0/0/0 statistics` | Xem số lượng packet và byte vào/ra. |
| `show interfaces diagnostics optics ge-0/0/0` | Xem công suất quang Tx/Rx, nhiệt độ module, điện áp và ngưỡng cảnh báo. |
| `show interfaces queue ge-0/0/0` | Kiểm tra packet drop theo từng hàng đợi QoS. |
| `show log messages \| match ge-0/0/0` | Kiểm tra lịch sử up/down hoặc lỗi liên quan cổng. |
| `clear interfaces statistics ge-0/0/0` | Xóa bộ đếm để theo dõi lỗi mới phát sinh. Cần ghi nhận số liệu trước khi xóa. |
| `set interfaces ge-0/0/0 description "UPLINK"` | Đặt mô tả cho interface. |
| `set interfaces ge-0/0/0 disable` | Tắt cổng bằng cấu hình. |
| `delete interfaces ge-0/0/0 disable` | Mở lại cổng đã bị disable. |
| `set interfaces ge-0/0/0 unit 0 family inet address 10.1.1.1/30` | Gán địa chỉ IPv4 cho interface Layer 3. |
| `delete interfaces ge-0/0/0 unit 0 family inet address 10.1.1.1/30` | Xóa địa chỉ IP khỏi interface. |

### Ý nghĩa trạng thái

| Admin | Link | Ý nghĩa |
|---|---|---|
| `up` | `up` | Interface hoạt động bình thường. |
| `up` | `down` | Cổng đã bật nhưng mất kết nối vật lý hoặc thiết bị đầu bên kia down. |
| `down` | `down` | Interface đang bị disable bằng cấu hình. |
| `up` | `up` nhưng không ping được | Có thể lỗi VLAN, IP, ARP, routing, firewall hoặc MTU. |

### Khi interface `up/down`

```bash
show interfaces terse
show interfaces ge-0/0/0 extensive
show interfaces diagnostics optics ge-0/0/0
show log messages | match ge-0/0/0
show lldp neighbors interface ge-0/0/0
```

Kiểm tra lần lượt:

1. Cáp hoặc module quang.
2. Thiết bị đầu bên kia.
3. Công suất Rx quá thấp.
4. Sai tốc độ hoặc negotiation.
5. Cổng bị err-disable ở đầu đối diện.
6. Link vừa flap nhiều lần.

---

## 4. VLAN và Access Port

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set vlans USERS vlan-id 10` | Tạo VLAN 10 với tên `USERS`. |
| `show vlans` | Xem danh sách VLAN và các interface thành viên. |
| `show vlans USERS` | Xem chi tiết VLAN cụ thể. |
| `set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access` | Đặt cổng ở chế độ access. |
| `set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members USERS` | Gán access port vào VLAN USERS. |
| `show ethernet-switching interfaces` | Kiểm tra mode và VLAN của từng switchport. |
| `show ethernet-switching table` | Xem bảng MAC address. |
| `show ethernet-switching table interface ge-0/0/1` | Kiểm tra MAC được học trên một cổng. |
| `clear ethernet-switching table interface ge-0/0/1` | Xóa MAC học trên cổng để kiểm tra học lại. |

### Troubleshooting Access Port

```bash
show interfaces ge-0/0/1 terse
show ethernet-switching interfaces ge-0/0/1
show ethernet-switching table interface ge-0/0/1
show vlans
```

Nếu không có MAC address:

- Máy đầu cuối chưa gửi traffic.
- Sai VLAN.
- Cáp hoặc NIC lỗi.
- Interface bị disable.
- Port security hoặc filter đang chặn.

---

## 5. Trunk Port

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set interfaces ge-0/0/2 unit 0 family ethernet-switching interface-mode trunk` | Đặt interface thành trunk. |
| `set interfaces ge-0/0/2 unit 0 family ethernet-switching vlan members USERS` | Cho VLAN USERS đi qua trunk. |
| `set interfaces ge-0/0/2 unit 0 family ethernet-switching vlan members [ USERS SERVER ]` | Cho phép nhiều VLAN đi qua trunk. |
| `set interfaces ge-0/0/2 native-vlan-id 10` | Đặt native VLAN cho traffic không gắn thẻ, tùy dòng thiết bị. |
| `show ethernet-switching interfaces ge-0/0/2` | Xem mode trunk và VLAN được phép. |
| `show vlans` | Kiểm tra VLAN đã được gán vào trunk chưa. |

### Khi VLAN không đi qua trunk

```bash
show ethernet-switching interfaces ge-0/0/2
show vlans
show ethernet-switching table
show interfaces ge-0/0/2 extensive
```

Kiểm tra:

- VLAN đã được tạo chưa.
- Hai đầu trunk có cho phép cùng VLAN không.
- Native VLAN hai đầu có giống nhau không.
- Interface có thật sự ở mode trunk không.
- MAC có được học ở đúng VLAN không.

---

## 6. LLDP và phát hiện thiết bị lân cận

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `show lldp neighbors` | Xem thiết bị lân cận, cổng local và remote. |
| `show lldp neighbors detail` | Xem chi tiết hostname, model, IP quản trị và port description. |
| `show lldp neighbors interface ge-0/0/0` | Xem neighbor trên một interface cụ thể. |
| `set protocols lldp interface all` | Bật LLDP trên tất cả interface. |
| `set protocols lldp-med interface all` | Bật LLDP-MED, thường dùng với IP Phone. |

LLDP hữu ích khi cần xác định cổng đang kết nối tới thiết bị nào mà không cần kiểm tra vật lý trực tiếp.

---

## 7. STP và chống loop Layer 2

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set protocols rstp interface all` | Bật RSTP trên toàn bộ switchport. |
| `show spanning-tree bridge` | Xem Root Bridge, Bridge ID và trạng thái STP. |
| `show spanning-tree interface` | Xem trạng thái Forwarding, Blocking hoặc Discarding của port. |
| `show spanning-tree interface ge-0/0/1 detail` | Xem chi tiết cost, role và trạng thái một cổng. |
| `show spanning-tree statistics interface ge-0/0/1` | Kiểm tra số lượng BPDU và topology change. |
| `set protocols rstp interface ge-0/0/1 edge` | Đặt access port thành edge port để chuyển nhanh sang forwarding. |
| `set protocols rstp interface ge-0/0/1 no-root-port` | Hạn chế cổng trở thành root port. |

### Khi port bị block

```bash
show spanning-tree bridge
show spanning-tree interface
show spanning-tree interface ge-0/0/1 detail
```

Port bị block thường không phải lỗi. STP đang ngăn loop. Cần kiểm tra topology trước khi thay đổi.

---

## 8. LACP và Aggregated Ethernet

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set chassis aggregated-devices ethernet device-count 4` | Cho phép tạo các interface `ae0` đến `ae3`. |
| `set interfaces ge-0/0/0 ether-options 802.3ad ae0` | Gán interface vật lý vào bundle `ae0`. |
| `set interfaces ge-0/0/1 ether-options 802.3ad ae0` | Gán member thứ hai vào `ae0`. |
| `set interfaces ae0 aggregated-ether-options lacp active` | Bật LACP active trên bundle. |
| `set interfaces ae0 aggregated-ether-options minimum-links 1` | Bundle vẫn hoạt động nếu còn ít nhất một member. |
| `show interfaces ae0 terse` | Xem trạng thái logical interface `ae0`. |
| `show lacp interfaces` | Kiểm tra member link, collecting và distributing. |
| `show lacp interfaces ae0 extensive` | Xem chi tiết Actor và Partner LACP. |
| `show interfaces ae0 extensive` | Kiểm tra traffic và lỗi trên bundle. |
| `show interfaces ge-0/0/0 extensive` | Kiểm tra riêng từng member vật lý. |

### Trạng thái LACP bình thường

```text
Collecting: Yes
Distributing: Yes
Synchronization: In Sync
```

Nếu member không vào bundle:

- Hai đầu không cùng LACP mode.
- Một đầu dùng static aggregation.
- Sai bundle ID.
- Speed khác nhau.
- Cổng vật lý down.
- Cấu hình VLAN hai đầu không tương thích.

---

## 9. ARP và MAC Address

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `show arp` | Xem bảng ánh xạ IPv4 sang MAC address. |
| `show arp no-resolve` | Xem ARP mà không phân giải tên DNS, kết quả nhanh hơn. |
| `show arp interface ge-0/0/0.0` | Xem ARP trên interface cụ thể. |
| `show arp hostname 10.1.1.2` | Tìm ARP của một địa chỉ IP cụ thể. |
| `clear arp hostname 10.1.1.2` | Xóa ARP của một IP để thiết bị học lại. |
| `show ethernet-switching table` | Kiểm tra MAC ở Layer 2. |
| `show ethernet-switching table vlan USERS` | Xem MAC trong một VLAN. |
| `show ethernet-switching table mac-address aa:bb:cc:dd:ee:ff` | Tìm MAC cụ thể đang nằm ở interface nào. |

### Phân tích nhanh

- Có MAC nhưng không có ARP: Có kết nối Layer 2 nhưng có thể sai IP hoặc host không trả lời ARP.
- Không có MAC: Kiểm tra port, VLAN và thiết bị đầu cuối.
- ARP ở trạng thái incomplete: Router gửi ARP nhưng không nhận được phản hồi.

---

## 10. Static Route và Routing Table

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set routing-options static route 10.10.10.0/24 next-hop 192.168.1.2` | Tạo static route qua next-hop. |
| `set routing-options static route 0.0.0.0/0 next-hop 192.168.1.1` | Tạo default route. |
| `show route` | Xem toàn bộ bảng định tuyến. |
| `show route terse` | Xem routing table dạng rút gọn. |
| `show route 10.10.10.0/24 exact` | Kiểm tra đúng một prefix. |
| `show route 10.10.10.0/24 extensive` | Xem protocol, preference, metric và next-hop chi tiết. |
| `show route protocol static` | Chỉ xem static route. |
| `show route forwarding-table` | Xem bảng forwarding thực tế đã được cài xuống phần cứng. |
| `show route forwarding-table destination 10.10.10.10` | Kiểm tra thiết bị sẽ forward traffic đi đâu. |
| `show route hidden` | Xem các route bị ẩn hoặc không đủ điều kiện sử dụng. |

### Ký hiệu quan trọng

| Ký hiệu | Ý nghĩa |
|---|---|
| `*` | Route đang active. |
| `+` | Route được chọn để forwarding. |
| `-` | Route được dùng gần nhất hoặc route phụ tùy output. |
| `Hidden` | Route không hợp lệ hoặc bị loại. |

Khi route không active, kiểm tra:

- Next-hop có reachable không.
- Route preference.
- Import policy.
- Next-hop có được resolve không.
- Có route tốt hơn từ protocol khác không.

---

## 11. OSPF

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set routing-options router-id 1.1.1.1` | Cấu hình Router ID. |
| `set protocols ospf area 0.0.0.0 interface ge-0/0/0.0` | Bật OSPF trên interface và đưa vào area 0. |
| `set protocols ospf area 0.0.0.0 interface lo0.0 passive` | Quảng bá loopback nhưng không hình thành neighbor. |
| `set protocols ospf area 0.0.0.0 interface ge-0/0/0.0 interface-type p2p` | Đặt interface OSPF thành point-to-point. |
| `set protocols ospf area 0.0.0.0 interface ge-0/0/0.0 metric 10` | Cấu hình OSPF cost. |
| `show ospf neighbor` | Xem trạng thái neighbor. |
| `show ospf neighbor detail` | Xem Router ID, priority, dead timer và interface. |
| `show ospf interface` | Xem area, network type, DR/BDR, hello/dead timer. |
| `show ospf database` | Xem Link-State Database. |
| `show ospf route` | Xem route được OSPF tính toán. |
| `show route protocol ospf` | Xem OSPF route đã vào routing table. |
| `show log messages \| match OSPF` | Kiểm tra log neighbor up/down. |

### Trạng thái OSPF

| Trạng thái | Ý nghĩa |
|---|---|
| `Down` | Chưa nhận Hello. |
| `Init` | Đã nhận Hello nhưng router chưa thấy Router ID của mình trong Hello phía bên kia. |
| `2-Way` | Hai bên nhận diện nhau; bình thường trên mạng broadcast với DROther. |
| `ExStart` | Đang thương lượng Master/Slave và sequence number. |
| `Exchange` | Đang trao đổi Database Description. |
| `Loading` | Đang yêu cầu LSA còn thiếu. |
| `Full` | Adjacency hoàn chỉnh. |

### OSPF không lên Full

```bash
show ospf neighbor detail
show ospf interface
show interfaces terse
show configuration protocols ospf
show log messages | match OSPF
ping <neighbor-ip>
```

Kiểm tra:

- IP và subnet.
- Area ID.
- Hello/dead timer.
- Authentication.
- MTU.
- Network type.
- Interface passive.
- Firewall filter.

---

## 12. BGP

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set routing-options autonomous-system 65001` | Cấu hình ASN local. |
| `set protocols bgp group EBGP type external` | Tạo nhóm eBGP. |
| `set protocols bgp group EBGP peer-as 65002` | Cấu hình ASN phía neighbor. |
| `set protocols bgp group EBGP neighbor 192.168.12.2` | Khai báo BGP neighbor. |
| `set protocols bgp group IBGP type internal` | Tạo nhóm iBGP. |
| `set protocols bgp group IBGP local-address 1.1.1.1` | Chỉ định địa chỉ source khi kết nối BGP. |
| `set protocols bgp group EBGP import IMPORT-POLICY` | Áp policy vào route nhận từ neighbor. |
| `set protocols bgp group EBGP export EXPORT-POLICY` | Áp policy cho route gửi ra neighbor. |
| `show bgp summary` | Xem nhanh trạng thái tất cả BGP neighbor và số prefix nhận được. |
| `show bgp neighbor 192.168.12.2` | Xem chi tiết một neighbor. |
| `show route protocol bgp` | Xem BGP route trong routing table. |
| `show route receive-protocol bgp 192.168.12.2` | Xem route nhận từ neighbor trước khi policy xử lý. |
| `show route advertising-protocol bgp 192.168.12.2` | Xem route đang quảng bá cho neighbor. |
| `show route hidden protocol bgp` | Xem BGP route bị hidden. |
| `clear bgp neighbor 192.168.12.2 soft` | Refresh route nhẹ, hạn chế reset toàn bộ phiên BGP. |
| `clear bgp neighbor 192.168.12.2` | Reset phiên BGP. Có thể gây gián đoạn, phải thận trọng. |

### Trạng thái BGP

| Trạng thái | Ý nghĩa |
|---|---|
| `Idle` | Chưa bắt đầu hoặc có lỗi cấu hình. |
| `Connect` | Đang thiết lập TCP. |
| `Active` | TCP thất bại và đang thử lại. |
| `OpenSent` | Đã gửi BGP OPEN. |
| `OpenConfirm` | Đang chờ KEEPALIVE. |
| `Established` | Phiên BGP hoạt động bình thường. |

### BGP ở trạng thái Active

```bash
show bgp summary
show bgp neighbor 192.168.12.2
show route 192.168.12.2 exact
ping 192.168.12.2 source 192.168.12.1
show system connections | match 179
show log messages | match BGP
```

Kiểm tra:

- Có route tới neighbor không.
- Sai ASN.
- Sai local-address.
- TCP port 179 bị chặn.
- MD5 authentication không giống nhau.
- eBGP multihop chưa cấu hình.
- Interface hoặc loopback down.

---

## 13. Routing Policy

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set policy-options prefix-list CUSTOMER 10.10.0.0/16` | Tạo danh sách prefix. |
| `set policy-options policy-statement EXPORT-CUSTOMER term 1 from prefix-list CUSTOMER` | Match prefix trong policy. |
| `set policy-options policy-statement EXPORT-CUSTOMER term 1 then accept` | Cho phép route match được export. |
| `set policy-options policy-statement EXPORT-CUSTOMER term REJECT then reject` | Từ chối tất cả route còn lại. |
| `set policy-options policy-statement SET-LP term 1 then local-preference 200` | Đặt Local Preference. |
| `set policy-options policy-statement PREPEND term 1 then as-path-prepend "65001 65001"` | Thực hiện AS Path prepend. |
| `show configuration policy-options` | Xem toàn bộ policy. |
| `show configuration protocols bgp \| display set` | Kiểm tra policy đã được gắn vào group chưa. |
| `show route receive-protocol bgp <neighbor>` | Xem route nhận trước import policy. |
| `show route advertising-protocol bgp <neighbor>` | Xem route sau export policy. |
| `show route hidden` | Tìm route bị policy loại hoặc next-hop lỗi. |

Lỗi phổ biến:

- Có policy nhưng chưa gắn vào BGP group.
- Thiếu `then accept`.
- Term reject đặt trước term accept.
- Prefix-list không đúng subnet mask.
- Route chưa tồn tại trong routing table nên không export được.

---

## 14. IS-IS

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set interfaces lo0 unit 0 family iso address 49.0001.0000.0000.0001.00` | Cấu hình NET cho IS-IS. |
| `set interfaces ge-0/0/0 unit 0 family iso` | Bật family ISO trên interface. |
| `set protocols isis interface ge-0/0/0.0 point-to-point` | Bật IS-IS và đặt link point-to-point. |
| `set protocols isis interface lo0.0 passive` | Quảng bá loopback nhưng không tạo adjacency. |
| `set protocols isis level 1 disable` | Chỉ chạy Level 2. |
| `show isis adjacency` | Kiểm tra adjacency IS-IS. |
| `show isis adjacency detail` | Xem level, holdtime và trạng thái chi tiết. |
| `show isis interface` | Kiểm tra interface tham gia IS-IS. |
| `show isis database` | Xem LSP database. |
| `show route protocol isis` | Xem route học từ IS-IS. |
| `show log messages \| match IS-IS` | Kiểm tra log adjacency. |

IS-IS không lên thường do:

- Chưa bật `family iso`.
- NET sai hoặc trùng.
- Level không tương thích.
- Authentication sai.
- Interface type không giống nhau.
- MTU hoặc encapsulation lỗi.

---

## 15. VRRP

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.2/24 vrrp-group 1 virtual-address 192.168.1.1` | Tạo Virtual IP cho VRRP group 1. |
| `set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.2/24 vrrp-group 1 priority 150` | Đặt priority. Số cao hơn thường làm master. |
| `set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.2/24 vrrp-group 1 preempt` | Cho router lấy lại vai trò master khi hoạt động trở lại. |
| `set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.2/24 vrrp-group 1 track interface ge-0/0/1 priority-cost 100` | Giảm priority khi uplink bị down. |
| `show vrrp` | Xem trạng thái Master hoặc Backup. |
| `show vrrp detail` | Xem priority, Virtual IP, timer và tracking. |
| `show log messages \| match VRRP` | Kiểm tra lịch sử chuyển trạng thái VRRP. |

Khi cả hai router đều là Master:

- Hai router không nhận VRRP advertisement của nhau.
- VLAN hoặc trunk lỗi.
- Firewall chặn VRRP protocol 112.
- Hai bên dùng khác VRRP group.
- Subnet hoặc Virtual IP không giống nhau.

---

## 16. Virtual Chassis

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `show virtual-chassis` | Xem member, role, priority và trạng thái. |
| `show virtual-chassis status` | Xem trạng thái tổng thể Virtual Chassis. |
| `show virtual-chassis vc-port` | Kiểm tra các cổng VCP. |
| `show virtual-chassis protocol adjacency` | Kiểm tra adjacency giữa các member. |
| `show chassis hardware` | Xác định FPC/member đang hiện diện. |
| `request virtual-chassis vc-port set pic-slot 1 port 0` | Chuyển cổng hỗ trợ thành VCP, tùy model. |
| `request virtual-chassis vc-port delete pic-slot 1 port 0` | Xóa cấu hình VCP trên cổng. |
| `request virtual-chassis renumber member 1 new-member-id 0` | Đổi member ID. Cần kiểm tra kỹ trước khi thực hiện. |

### Trạng thái thường gặp

| Trạng thái | Ý nghĩa |
|---|---|
| `Master` | Member đang điều khiển Virtual Chassis. |
| `Backup` | Member dự phòng cho Master. |
| `Linecard` | Member chỉ chuyển mạch. |
| `Inactive` | Member có mặt nhưng chưa tham gia hoạt động. |
| `NotPrsnt` | Cấu hình có member nhưng thiết bị vật lý không hiện diện. |

---

## 17. Firewall Filter

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set firewall family inet filter INPUT term ALLOW-SSH from protocol tcp` | Match TCP. |
| `set firewall family inet filter INPUT term ALLOW-SSH from destination-port ssh` | Match cổng SSH 22. |
| `set firewall family inet filter INPUT term ALLOW-SSH then count SSH-COUNT` | Tạo counter để kiểm tra traffic có match rule không. |
| `set firewall family inet filter INPUT term ALLOW-SSH then accept` | Cho phép traffic. |
| `set firewall family inet filter INPUT term DEFAULT then discard` | Chặn traffic còn lại. |
| `set interfaces ge-0/0/0 unit 0 family inet filter input INPUT` | Gắn filter chiều vào interface. |
| `show firewall` | Xem toàn bộ filter và counter. |
| `show firewall filter INPUT` | Xem counter của filter cụ thể. |
| `clear firewall filter INPUT` | Xóa counter để đo traffic mới. |

Khi traffic bị chặn:

```bash
show configuration firewall
show configuration interfaces ge-0/0/0
show firewall filter INPUT
```

Counter tăng ở term `discard` chứng tỏ traffic đang match rule chặn.

---

## 18. Ping và Traceroute

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `ping 8.8.8.8` | Kiểm tra kết nối cơ bản. |
| `ping 8.8.8.8 count 10` | Gửi đúng 10 packet. |
| `ping 8.8.8.8 rapid count 100` | Kiểm tra packet loss nhanh. |
| `ping 8.8.8.8 source 192.168.1.1` | Ping với source IP cụ thể. Rất hữu ích khi thiết bị có nhiều interface. |
| `ping 8.8.8.8 do-not-fragment size 1472` | Kiểm tra MTU và fragmentation. |
| `traceroute 8.8.8.8` | Xác định đường đi và hop bị gián đoạn. |
| `traceroute 8.8.8.8 source 192.168.1.1` | Traceroute với source cụ thể. |
| `show route 8.8.8.8` | Kiểm tra route trước khi kết luận lỗi kết nối. |
| `show arp` | Kiểm tra next-hop Layer 2. |

### Quy trình ping không được

```bash
show interfaces terse
show arp
show route <destination>
ping <next-hop>
ping <destination> source <source-ip>
traceroute <destination> source <source-ip>
show firewall
```

---

## 19. Packet Capture trên Junos

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `monitor traffic interface ge-0/0/0` | Xem packet đi qua interface. |
| `monitor traffic interface ge-0/0/0 no-resolve` | Không phân giải DNS, hiển thị nhanh hơn. |
| `monitor traffic interface ge-0/0/0 matching "host 10.1.1.10"` | Lọc packet theo host. |
| `monitor traffic interface ge-0/0/0 matching "port 179"` | Lọc traffic BGP TCP 179. |
| `monitor traffic interface ge-0/0/0 extensive` | Hiển thị chi tiết header packet. |

Cẩn thận khi dùng trên thiết bị production vì capture quá rộng có thể làm tăng CPU Routing Engine.

---

## 20. Log

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `show log messages` | Xem file log hệ thống chính. |
| `show log messages \| last 50` | Xem 50 dòng cuối. |
| `show log messages \| match error` | Lọc log chứa từ `error`. |
| `show log messages \| match ge-0/0/0` | Lọc log của interface. |
| `show log messages \| match OSPF` | Lọc sự kiện OSPF. |
| `show log messages \| match BGP` | Lọc sự kiện BGP. |
| `monitor start messages` | Theo dõi log thời gian thực. |
| `monitor stop` | Dừng theo dõi log. |
| `show log interactive-commands` | Xem lịch sử lệnh người dùng, nếu thiết bị đã cấu hình log này. |

---

## 21. NTP, SNMP và Syslog

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set system ntp server 10.10.10.10` | Cấu hình NTP server. |
| `show ntp associations` | Kiểm tra trạng thái đồng bộ NTP. |
| `show system uptime` | Đối chiếu thời gian thiết bị. |
| `set system syslog host 10.10.10.20 any info` | Gửi log mức info trở lên tới Syslog Server. |
| `show configuration system syslog` | Kiểm tra cấu hình gửi log. |
| `set snmp community NMS authorization read-only` | Tạo SNMP community read-only. |
| `set snmp trap-group NMS targets 10.10.10.30` | Gửi SNMP trap tới NMS. |
| `show snmp statistics` | Kiểm tra số request, response và lỗi SNMP. |
| `show system connections` | Kiểm tra kết nối từ thiết bị tới dịch vụ quản trị. |

Nếu NMS không nhận SNMP:

- Kiểm tra route tới NMS.
- Community hoặc SNMP version.
- Firewall filter.
- Source address.
- UDP 161 và 162.
- Routing instance.

---

## 22. SSH và quản trị từ xa

| Lệnh | Công dụng và troubleshooting |
|---|---|
| `set system services ssh` | Bật SSH. |
| `set system services netconf ssh` | Bật NETCONF over SSH. |
| `show system connections \| match 22` | Kiểm tra kết nối SSH. |
| `show system users` | Xem người đang đăng nhập. |
| `show log messages \| match ssh` | Kiểm tra lỗi đăng nhập SSH. |
| `show configuration system login` | Xem tài khoản và quyền người dùng. |
| `show configuration system services` | Kiểm tra SSH hoặc NETCONF đã bật chưa. |

---

## 23. RPM Probe

| Lệnh cấu hình / kiểm tra | Công dụng và troubleshooting |
|---|---|
| `set services rpm probe INTERNET test PING target address 8.8.8.8` | Tạo probe kiểm tra một địa chỉ. |
| `set services rpm probe INTERNET test PING probe-type icmp-ping` | Sử dụng ICMP ping. |
| `set services rpm probe INTERNET test PING probe-count 5` | Mỗi lần kiểm tra gửi 5 probe. |
| `set services rpm probe INTERNET test PING test-interval 10` | Chạy bài kiểm tra mỗi 10 giây. |
| `show services rpm probe-results` | Xem packet loss, RTT và kết quả probe. |
| `show services rpm history-results` | Xem lịch sử kết quả. |

RPM phù hợp để giám sát latency, jitter và packet loss giữa các điểm mạng.

---

# BẢNG XỬ LÝ SỰ CỐ THEO TÌNH HUỐNG

## Mất kết nối mạng

| Lệnh | Mục đích |
|---|---|
| `show system alarms` | Kiểm tra cảnh báo tổng thể. |
| `show interfaces terse` | Xác định interface down. |
| `show interfaces <interface> extensive` | Kiểm tra error, drop và flap. |
| `show interfaces diagnostics optics <interface>` | Kiểm tra tín hiệu quang. |
| `show arp` | Kiểm tra next-hop. |
| `show route <destination>` | Kiểm tra đường đi. |
| `ping <next-hop>` | Kiểm tra hop kế tiếp. |
| `traceroute <destination>` | Xác định vị trí gián đoạn. |
| `show firewall` | Kiểm tra ACL/filter. |
| `show log messages \| last 50` | Kiểm tra sự kiện gần nhất. |

## OSPF Neighbor Down

| Lệnh | Mục đích |
|---|---|
| `show ospf neighbor` | Xem trạng thái neighbor. |
| `show ospf interface` | So sánh area, timer và network type. |
| `show interfaces terse` | Kiểm tra interface. |
| `ping <neighbor-ip>` | Kiểm tra kết nối IP. |
| `show configuration protocols ospf` | Kiểm tra cấu hình OSPF. |
| `show log messages \| match OSPF` | Tìm thời điểm và nguyên nhân down. |

## BGP Neighbor Down

| Lệnh | Mục đích |
|---|---|
| `show bgp summary` | Xác định trạng thái BGP. |
| `show bgp neighbor <ip>` | Xem lỗi chi tiết. |
| `show route <neighbor-ip>` | Kiểm tra route tới neighbor. |
| `ping <neighbor-ip> source <local-ip>` | Kiểm tra đúng source address. |
| `show system connections \| match 179` | Kiểm tra TCP 179. |
| `show configuration protocols bgp` | So sánh ASN, IP và policy. |
| `show log messages \| match BGP` | Tìm lỗi phiên BGP. |

## CPU cao

| Lệnh | Mục đích |
|---|---|
| `show chassis routing-engine` | Xác nhận CPU và RAM cao. |
| `show system processes extensive` | Xác định tiến trình chiếm tài nguyên. |
| `show task memory` | Kiểm tra memory theo routing task. |
| `show system users` | Kiểm tra số người đang thao tác. |
| `show log messages \| last 100` | Tìm event hoặc protocol flap. |
| `show interfaces extensive` | Kiểm tra storm, packet hoặc error bất thường. |

## Disk đầy

| Lệnh | Mục đích |
|---|---|
| `show system storage` | Xác định phân vùng đầy. |
| `file list /var/log detail` | Kiểm tra file log lớn. |
| `request system storage cleanup dry-run` | Xem trước file có thể xóa. |
| `request system storage cleanup` | Dọn file không cần thiết. Phải kiểm tra trước khi chạy. |
| `show log messages` | Kiểm tra log có tăng bất thường không. |

## LACP Member Down

| Lệnh | Mục đích |
|---|---|
| `show lacp interfaces` | Kiểm tra member và trạng thái bundle. |
| `show interfaces ae0 terse` | Kiểm tra interface tổng. |
| `show interfaces ge-0/0/0 extensive` | Kiểm tra member vật lý. |
| `show lldp neighbors` | Xác định kết nối đầu đối diện. |
| `show log messages \| match ae0` | Xem lịch sử bundle flap. |

---

# BỘ LỆNH KIỂM TRA NOC HẰNG NGÀY

```bash
show system alarms
show chassis alarms
show chassis environment
show chassis routing-engine
show system storage
show interfaces terse
show interfaces descriptions
show ospf neighbor
show bgp summary
show isis adjacency
show lacp interfaces
show virtual-chassis
show ntp associations
show log messages | last 50
```

---

# THỨ TỰ TROUBLESHOOTING NÊN NHỚ

```text
Alarm
→ Physical Interface
→ Optical/Error
→ VLAN/MAC/ARP
→ Routing Table
→ OSPF/BGP/IS-IS
→ Ping/Traceroute
→ Firewall Filter
→ Log
→ Escalation kèm evidence
```

---

# GỢI Ý CÁCH HỌC

Nên học và lab theo thứ tự:

1. Junos CLI, commit và rollback.
2. Interface, cáp quang, log và alarm.
3. VLAN, trunk, MAC, ARP và LLDP.
4. STP và LACP.
5. Static route và routing table.
6. OSPF.
7. BGP và routing policy.
8. IS-IS.
9. VRRP và Virtual Chassis.
10. Firewall filter.
11. SNMP, Syslog, NTP và RPM.
12. Tổng hợp các tình huống troubleshooting.

---

# LƯU Ý KHI THAO TÁC TRÊN THIẾT BỊ PRODUCTION

- Luôn chạy `show | compare` trước khi commit.
- Luôn chạy `commit check`.
- Nên dùng `commit confirmed 5` khi cấu hình từ xa.
- Không reset BGP hoặc clear interface khi chưa xác định phạm vi ảnh hưởng.
- Ghi nhận số liệu trước khi clear counter.
- Hạn chế dùng packet capture quá rộng.
- Mọi thay đổi nên có ticket, kế hoạch rollback và thời gian thực hiện.
- Khi escalation, phải gửi kèm log, output lệnh, thời gian sự cố và phạm vi ảnh hưởng.

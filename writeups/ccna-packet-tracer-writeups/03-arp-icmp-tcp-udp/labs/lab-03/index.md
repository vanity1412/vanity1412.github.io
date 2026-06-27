---
layout: page-toc
title: "CCNA 03.03 - 9.2.9 Packet Tracer - Examine the ARP Table"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/
toc: true
---

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `9.2.9 Packet Tracer - Examine the ARP Table.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Hoàn thành quan sát ARP Request, MAC Address Table và ARP khi đi qua router |

> Bài này không yêu cầu cấu hình IP mới. Trọng tâm là dùng **Simulation Mode**, `arp -a`, `arp -d`, `ping`, `show mac-address-table` và `show arp` để thấy rõ cách thiết bị học địa chỉ MAC/IP.

## 1. Mục Tiêu Bài Lab

- Xóa ARP cache trên PC để tạo lại quá trình ARP từ đầu.
- Quan sát ARP Request khi hai host nằm cùng mạng LAN `172.16.31.0`.
- Kiểm tra cách switch học địa chỉ MAC bằng lệnh `show mac-address-table`.
- Quan sát ARP khi host cần liên lạc với mạng từ xa `10.10.10.0`.
- Xác định lúc nào địa chỉ MAC thay đổi và lúc nào địa chỉ IP giữ nguyên.
- Ghi lại lỗi thường gặp khi đọc ARP/MAC table trong Packet Tracer Simulation Mode.

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/topology.png)

## 2. Bảng Địa Chỉ MAC Theo Đề

| Thiết bị | Interface | MAC Address | Switch Interface |
| --- | --- | --- | --- |
| Router0 | G0/0 | `0001.6458.2501` | `G0/1` |
| Router0 | S0/0/0 | N/A | N/A |
| Router1 | G0/0 | `00E0.F7B1.8901` | `G0/1` |
| Router1 | S0/0/0 | N/A | N/A |
| 10.10.10.2 | Wireless | `0060.2F84.4AB6` | `F0/2` |
| 10.10.10.3 | Wireless | `0060.4706.572B` | `F0/2` |
| 172.16.31.2 | F0 | `000C.85CC.1DA7` | `F0/1` |
| 172.16.31.3 | F0 | `0060.7036.2849` | `F0/2` |
| 172.16.31.4 | G0 | `0002.1640.8D75` | `F0/3` |

> **Lưu ý:** MAC trong bảng là dữ liệu theo file lab mẫu. Nếu bấm **Reset Activity**, một số giá trị có thể thay đổi theo file Packet Tracer mới.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 10.10.10.0 | Router0, Switch0, Access Point, 10.10.10.2, 10.10.10.3 | Hai laptop đi qua Access Point nên trên Switch0 có thể thấy nhiều MAC cùng học qua một port |
| LAN 172.16.31.0 | Router1, Switch1, Hub, 172.16.31.2, 172.16.31.3, 172.16.31.4 | Hub không học MAC, còn Switch1 học MAC theo port nhận frame |
| Kết nối giữa router | Router0 ↔ Router1 | Khi gói đi qua router, MAC nguồn/đích sẽ được thay đổi theo từng chặng |

> **Điểm dễ nhầm:** IP nguồn và IP đích của gói ICMP thường giữ nguyên từ đầu đến cuối, nhưng MAC nguồn và MAC đích thay đổi khi gói đi qua router.

## 4. Part 1 - Examine an ARP Request

### Step 1 - Tạo ARP Request từ `172.16.31.2` đến `172.16.31.3`

```text
PC> arp -d
PC> ping 172.16.31.3
```

> `arp -d` dùng để xóa ARP cache, giúp mình quan sát lại quá trình hỏi MAC từ đầu.

![Clear ARP and ping](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part1-clear-arp-ping.png)

| Nội dung quan sát | Giá trị / nhận xét |
| --- | --- |
| Thiết bị gửi ARP Request | `172.16.31.2` |
| IP cần tìm MAC | `172.16.31.3` |
| Source MAC | `000C.85CC.1DA7` |
| Destination MAC của ARP Request | `FFFF.FFFF.FFFF` |
| Destination MAC này có trong bảng đề không? | Không. Đây là broadcast MAC |
| ICMP PDU ban đầu | Tạm thời biến mất / chờ ARP Reply |

### Step 2 - Theo dõi ARP Request qua Switch1

| Câu hỏi | Trả lời |
| --- | --- |
| Switch1 tạo bao nhiêu bản copy của ARP Request? | Thường là 2 bản copy ra các port còn lại trong LAN |
| Thiết bị nào chấp nhận PDU? | `172.16.31.3` |
| Các thiết bị không phải đích xử lý thế nào? | Nhận frame broadcast nhưng loại bỏ nếu Target IP không khớp |

![ARP request at Switch1](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part1-arp-request-switch1.png)

### Step 3 - Quan sát ARP Reply

| Giai đoạn | Source MAC | Destination MAC | Nhận xét |
| --- | --- | --- | --- |
| ARP Request | `000C.85CC.1DA7` | `FFFF.FFFF.FFFF` | PC `172.16.31.2` hỏi broadcast |
| ARP Reply | `0060.7036.2849` | `000C.85CC.1DA7` | PC `172.16.31.3` trả lời unicast |

| Câu hỏi | Trả lời |
| --- | --- |
| Source và destination MAC thay đổi thế nào? | ARP Reply đảo chiều MAC: nguồn là MAC của `172.16.31.3`, đích là MAC của `172.16.31.2` |
| Switch tạo bao nhiêu bản copy trong ARP Reply? | Thường là 0 bản copy nếu switch đã biết MAC đích nằm cùng port hub |

> **Lưu ý:** Hub vẫn flood tín hiệu ra các cổng, nhưng hub không có MAC table. Switch mới là thiết bị quyết định học/chuyển frame theo MAC.

### Step 4 - ICMP tiếp tục sau khi ARP hoàn tất

| Kiểm tra | Kết quả |
| --- | --- |
| MAC nguồn/đích trong ICMP có khớp IP nguồn/đích không? | Có |
| Source IP | `172.16.31.2` |
| Destination IP | `172.16.31.3` |
| Source MAC | `000C.85CC.1DA7` |
| Destination MAC | `0060.7036.2849` |

```text
PC> arp -a
```

| Câu hỏi | Trả lời |
| --- | --- |
| MAC entry mới tương ứng với IP nào? | `172.16.31.3` |
| Khi nào end device gửi ARP Request? | Khi cần gửi đến một IPv4 next-hop nhưng chưa biết MAC tương ứng trong ARP cache |

![ARP table after local ping](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part1-arp-a-local.png)

## 5. Part 2 - Examine a Switch MAC Address Table

### Step 1 - Tạo thêm traffic để switch học MAC

```text
! Từ PC 172.16.31.2
PC> ping 172.16.31.4

! Từ laptop 10.10.10.2
PC> ping 10.10.10.3
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Ping `172.16.31.2` → `172.16.31.4` | Reply thành công |
| Ping `10.10.10.2` → `10.10.10.3` | Reply thành công |
| Số reply gửi/nhận | 4 sent, 4 received trong mỗi lần ping thành công |

![Generate traffic for MAC table](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part2-generate-traffic.png)

### Step 2 - Kiểm tra MAC Address Table trên Switch1

```text
Switch1> enable
Switch1# show mac-address-table
```

| MAC dự kiến | Port dự kiến | Thiết bị |
| --- | --- | --- |
| `00E0.F7B1.8901` | `G0/1` | Router1 G0/0 |
| `000C.85CC.1DA7` | `F0/1` hoặc port nối hub tùy file | 172.16.31.2 |
| `0060.7036.2849` | Port nối hub | 172.16.31.3 |
| `0002.1640.8D75` | `F0/3` | 172.16.31.4 |

| Câu hỏi | Trả lời |
| --- | --- |
| Các entry có tương ứng bảng đề không? | Có, MAC học được phải khớp với MAC của thiết bị trong bảng đề |

![Switch1 MAC address table](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part2-switch1-mac-table.png)

### Step 3 - Kiểm tra MAC Address Table trên Switch0

```text
Switch0> enable
Switch0# show mac-address-table
```

| MAC dự kiến | Port dự kiến | Thiết bị |
| --- | --- | --- |
| `0001.6458.2501` | `G0/1` | Router0 G0/0 |
| `0060.2F84.4AB6` | `F0/2` | 10.10.10.2 |
| `0060.4706.572B` | `F0/2` | 10.10.10.3 |

| Câu hỏi | Trả lời |
| --- | --- |
| Các entry có tương ứng bảng đề không? | Có |
| Vì sao có hai MAC cùng nằm trên một port? | Vì `10.10.10.2` và `10.10.10.3` đi qua Access Point, còn Access Point nối vào Switch0 bằng cùng một cổng |

![Switch0 MAC address table](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part2-switch0-mac-table.png)

## 6. Part 3 - Examine the ARP Process in Remote Communications

### Step 1 - Ping từ `172.16.31.2` đến mạng từ xa `10.10.10.1`

```text
PC> ping 10.10.10.1
PC> arp -a
```

| Câu hỏi | Trả lời |
| --- | --- |
| IP của ARP entry mới là gì? | `172.16.31.1` hoặc địa chỉ gateway của LAN `172.16.31.0` |
| Vì sao không phải `10.10.10.1`? | Vì `10.10.10.1` ở mạng khác, PC chỉ cần biết MAC của default gateway để gửi gói ra ngoài LAN |

> **Lưu ý:** Khi gửi đến mạng từ xa, host không ARP trực tiếp địa chỉ IP đích. Host ARP địa chỉ **default gateway** trong cùng LAN.

![Remote ping ARP entry](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part3-remote-arp-entry.png)

### Step 2 - Xóa ARP và quan sát lại trong Simulation Mode

```text
PC> arp -d
PC> ping 10.10.10.1
```

| Câu hỏi | Trả lời |
| --- | --- |
| Có bao nhiêu PDU xuất hiện? | 2 PDU: ARP và ICMP |
| Target IP của ARP Request là gì? | `172.16.31.1` hoặc default gateway của PC |
| Vì sao Target IP không phải `10.10.10.1`? | Vì thiết bị đích nằm ở remote network, next-hop đầu tiên là router gateway |

![Remote ARP request in Simulation Mode](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part3-remote-arp-request.png)

### Step 3 - Kiểm tra trên Router1

```text
Router1> enable
Router1# show mac-address-table
Router1# show arp
```

| Câu hỏi | Trả lời |
| --- | --- |
| `show mac-address-table` trên router có bao nhiêu MAC? | Thường không có bảng MAC như switch, hoặc không trả về bảng học MAC động |
| Vì sao? | Router dùng bảng định tuyến và ARP table, không dùng MAC address table để switch frame trong LAN như switch |
| `show arp` có entry cho `172.16.31.2` không? | Có, sau khi PC gửi traffic đến router |
| Điều gì xảy ra với ping đầu tiên khi router phải trả lời ARP? | Ping đầu tiên có thể timeout vì thiết bị đang xử lý ARP trước, các gói sau mới thành công |

![Router1 ARP table](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-03/part3-router1-show-arp.png)

## 7. Tổng Hợp Đáp Án Nhanh

| Nội dung | Đáp án |
| --- | --- |
| Destination MAC của ARP Request | `FFFF.FFFF.FFFF` |
| Destination MAC broadcast có trong bảng đề không? | Không |
| Thiết bị chấp nhận ARP Request local | `172.16.31.3` |
| ARP Reply dùng broadcast hay unicast? | Unicast |
| Entry ARP sau ping local | IP `172.16.31.3` ↔ MAC `0060.7036.2849` |
| Khi nào host gửi ARP? | Khi cần biết MAC của IP next-hop trong cùng LAN |
| Vì sao nhiều MAC cùng một port trên Switch0? | Do nhiều wireless client đi qua Access Point nối cùng một port |
| Khi ping remote network, PC ARP IP nào? | Default gateway `172.16.31.1` |
| MAC có thay đổi khi qua router không? | Có |
| IP nguồn/đích có thay đổi khi qua router không? | Không, với gói ICMP thông thường trong lab này |

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không thấy ARP Request mới | ARP cache vẫn còn entry cũ | Chạy `arp -d` trước khi ping |
| Không thấy PDU chạy từng bước | Đang ở Realtime Mode | Chuyển sang Simulation Mode và dùng Capture/Forward |
| Nhầm MAC broadcast với MAC của thiết bị thật | ARP Request dùng `FFFF.FFFF.FFFF` | Kiểm tra cột Destination MAC trong PDU Details |
| Nghĩ host ARP trực tiếp IP remote | Chưa phân biệt local network và remote network | Với remote network, host ARP MAC của default gateway |
| Không hiểu vì sao Switch0 có 2 MAC trên 1 port | Hai wireless client đi qua Access Point | Quan sát port nối Access Point trên Switch0 |
| Gõ sai lệnh xóa ARP | Nhầm dấu `-` trong `arp -d` | Dùng đúng `arp -d` trên PC Command Prompt |

## 9. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| ARP Request local `172.16.31.2` → `172.16.31.3` | Thấy broadcast MAC `FFFF.FFFF.FFFF` |
| ARP Reply local | Thấy unicast MAC từ `172.16.31.3` về `172.16.31.2` |
| `arp -a` trên PC | Có entry tương ứng sau khi ping |
| `show mac-address-table` trên Switch1 | Học được MAC của các thiết bị LAN `172.16.31.0` |
| `show mac-address-table` trên Switch0 | Học được MAC của router và các wireless client |
| Ping remote `172.16.31.2` → `10.10.10.1` | PC ARP default gateway trước |
| `show arp` trên Router1 | Có entry của host `172.16.31.2` |

Checklist ảnh minh chứng nên chụp:

- [ ] `topology.png` - sơ đồ tổng quan lab.
- [ ] `part1-clear-arp-ping.png` - xóa ARP và ping local.
- [ ] `part1-arp-request-switch1.png` - ARP Request tại Switch1.
- [ ] `part1-arp-a-local.png` - ARP table sau ping local.
- [ ] `part2-switch1-mac-table.png` - MAC table trên Switch1.
- [ ] `part2-switch0-mac-table.png` - MAC table trên Switch0.
- [ ] `part3-remote-arp-entry.png` - ARP entry khi ping mạng từ xa.
- [ ] `part3-router1-show-arp.png` - ARP table trên Router1.
- [ ] `check-results.png` - kết quả Check Results nếu cần.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/">Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/">Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/">Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/">Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications</a></li>
    </ul>
  </details>
</div>

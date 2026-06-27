---
layout: page-toc
title: "CCNA 03.04 - 9.3.4 Packet Tracer - IPv6 Neighbor Discovery"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/
toc: true
---

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `9.3.4 Packet Tracer - IPv6 Neighbor Discovery.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Quan sát được quá trình IPv6 Neighbor Discovery trong cùng LAN và khác LAN |

> **Ghi chú:** Bài này không chấm điểm cấu hình. Thiết bị đã được cấu hình sẵn, trọng tâm là dùng **Simulation Mode** để quan sát ICMPv6, NDP, Neighbor Solicitation, Neighbor Advertisement và cách thiết bị tìm MAC address trong IPv6.

## 1. Mục Tiêu Bài Lab

- Quan sát quá trình IPv6 Neighbor Discovery khi 2 host nằm cùng LAN.
- Quan sát quá trình IPv6 Neighbor Discovery khi host truy cập sang LAN khác.
- Phân biệt cách thiết bị chọn MAC đích khi gửi nội bộ và khi gửi qua default gateway.
- Kiểm tra bảng IPv6 neighbor trên router bằng `show ipv6 neighbors`.
- Ghi lại các PDU quan trọng trong Simulation Mode để làm bằng chứng.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/topology.png)

## 2. Bảng Địa Chỉ IPv6

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| RTA | G0/0/0 | `2001:db8:acad:1::1/64` | N/A |
| RTA | G0/0/1 | `2001:db8:acad:2::1/64` | N/A |
| PCA1 | NIC | `2001:db8:acad:1::A/64` | `fe80::1` |
| PCA2 | NIC | `2001:db8:acad:1::B/64` | `fe80::1` |
| PCB1 | NIC | `2001:db8:acad:2::A/64` | `fe80::1` |

> **Lưu ý:** Theo topology, LAN bên trái là `2001:db8:acad:1::/64`, LAN bên phải là `2001:db8:acad:2::/64`. Vì vậy interface RTA nối sang SwitchB phải thuộc mạng `2001:db8:acad:2::/64`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN trái | PCA1, PCA2, SwitchA, RTA G0/0/0 | PCA1 và PCA2 cùng mạng `2001:db8:acad:1::/64` |
| LAN phải | PCB1, SwitchB, RTA G0/0/1 | PCB1 thuộc mạng `2001:db8:acad:2::/64` |
| Router | RTA | Đóng vai trò default gateway cho cả hai LAN |
| Thiết bị Layer 2 | SwitchA, SwitchB | Chỉ chuyển frame, không định tuyến IPv6 |

> **Điểm dễ sai:** Với IPv6, host không dùng ARP. Thiết bị dùng **NDP** để tìm MAC address tương ứng với IPv6 address hoặc MAC của default gateway.

## 4. Part 1 - IPv6 Neighbor Discovery Local Network

### Step 1 - Kiểm tra và xóa bảng neighbor trên RTA

```text
RTA> enable
RTA# show ipv6 neighbors
RTA# clear ipv6 neighbors
RTA# show ipv6 neighbors
```

> `clear ipv6 neighbors` giúp xóa neighbor cache để khi ping lại, Packet Tracer sinh ra NDP PDU mới và dễ quan sát hơn.

![RTA show IPv6 neighbors empty](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/rta-show-ipv6-neighbors-empty.png)

### Step 2 - Ping từ PCA1 sang PCA2 trong cùng LAN

Trên PCA1, mở **Desktop > Command Prompt**:

```text
ping -n 1 2001:db8:acad:1::b
```

Trong Simulation Mode:

| Thao tác | Giá trị cần chọn |
| --- | --- |
| Mode | Simulation |
| Event List Filters | Clear All trước |
| IPv6 Filters | Chọn `ICMPv6` và `NDP` |
| Nút chạy | Capture/Forward |

![Simulation filter ICMPv6 NDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/simulation-filter-icmpv6-ndp.png)

### Step 3 - Quan sát ICMPv6 Echo Request đầu tiên

| Câu hỏi | Trả lời |
| --- | --- |
| Vì sao có ND PDU? | PCA1 muốn ping PCA2 nhưng chưa biết MAC address của PCA2, nên phải dùng IPv6 Neighbor Discovery để tìm MAC trước. |
| ICMPv6 Message Type đầu tiên là gì? | `Echo Request`, thường hiển thị là ICMPv6 Type `128`. |
| Vì sao chưa có Layer 2 address? | PCA1 mới có IPv6 đích, chưa biết MAC đích nên chưa đóng gói Ethernet hoàn chỉnh được. |

![First ICMPv6 event at PCA1](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/first-icmpv6-pca1.png)

### Step 4 - Quan sát NDP tại PCA1

| Trường cần quan sát | Giá trị / ý nghĩa |
| --- | --- |
| IPv6 Source | IPv6 của PCA1, ví dụ `2001:db8:acad:1::a` |
| IPv6 Destination | Solicited-node multicast của PCA2, thường có dạng `ff02::1:ff00:b` |
| Ethernet Source | MAC của PCA1 |
| Ethernet Destination | Multicast MAC IPv6, thường có dạng `33:33:ff:00:00:0b` |
| NDP Message | Neighbor Solicitation |

> **Lưu ý:** IPv6 Neighbor Discovery không broadcast như ARP. Nó dùng solicited-node multicast để giảm số lượng host phải xử lý gói tin.

![NDP event at PCA1](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/ndp-event-pca1.png)

### Step 5 - Quan sát NDP tại SwitchA, PCA2 và RTA

| Vị trí PDU | Kết quả quan sát |
| --- | --- |
| SwitchA | Layer 2 gần như không thay đổi, switch chỉ forward frame theo cổng phù hợp. |
| PCA2 | PCA2 nhận Neighbor Solicitation và gửi Neighbor Advertisement trả lời PCA1. |
| RTA | RTA không phải IPv6 đích của Neighbor Solicitation nên không có Out Layers để forward tiếp. |

![NDP event at PCA2](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/ndp-event-pca2.png)

### Step 6 - Thông tin PDU trả lời từ PCA2

| Trường | Giá trị / ý nghĩa |
| --- | --- |
| Ethernet II DEST ADDR | MAC của PCA1 |
| Ethernet II SRC ADDR | MAC của PCA2 |
| IPv6 SRC IP | `2001:db8:acad:1::b` |
| IPv6 DST IP | `2001:db8:acad:1::a` |
| Loại bản tin | Neighbor Advertisement |

> Sau khi nhận Neighbor Advertisement, PCA1 đã biết MAC của PCA2 và có đủ thông tin để gửi ICMPv6 Echo Request thật sự.

### Step 7 - Kiểm tra ICMPv6 Echo Reply

| Câu hỏi | Trả lời |
| --- | --- |
| PCA1 đã đủ thông tin để giao tiếp với PCA2 chưa? | Có. PCA1 đã học được MAC address của PCA2 qua Neighbor Advertisement. |
| ICMPv6 Echo Message Type cuối cùng là gì? | `Echo Reply`, thường hiển thị là ICMPv6 Type `129`. |
| Vì sao ping lại lần 2 không thấy NDP? | Vì neighbor cache đã có thông tin MAC của PCA2, nên PCA1 không cần hỏi lại bằng NDP. |

```text
ping -n 1 2001:db8:acad:1::b
```

![ICMPv6 echo reply PCA1 PCA2](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/icmpv6-echo-reply-local.png)

## 5. Part 2 - IPv6 Neighbor Discovery Remote Network

### Step 1 - Reset Simulation và xóa neighbor cache

```text
RTA> enable
RTA# clear ipv6 neighbors
RTA# show ipv6 neighbors
```

Trên PCA1:

```text
ping -n 1 2001:db8:acad:2::a
```

> Đích lần này là PCB1 ở mạng khác. PCA1 sẽ không tìm MAC của PCB1 trực tiếp, mà tìm MAC của default gateway trước.

![Remote ping PCA1 to PCB1](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/remote-ping-pca1-pcb1.png)

### Step 2 - Quan sát NDP tại PCA1 khi đi remote LAN

| Câu hỏi | Trả lời |
| --- | --- |
| Source IP trong inbound PDU tại PCA1 là gì? | Link-local address của RTA trên LAN trái, thường là `fe80::1`. |
| Vì sao dùng link-local? | Default gateway của PCA1 được cấu hình là `fe80::1`, nên PCA1 cần biết MAC của địa chỉ link-local này. |
| MAC đích của ICMPv6 sau khi PCA1 học xong là gì? | MAC của interface RTA nối với LAN trái, không phải MAC của PCB1. |

> **Lưu ý:** Khi gửi sang mạng khác, host chỉ cần biết MAC của default gateway. IPv6 đích vẫn là PCB1, nhưng Ethernet destination MAC là MAC của router.

![NDP to default gateway](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/ndp-default-gateway.png)

### Step 3 - Quan sát RTA xử lý gói đi sang LAN phải

| Vị trí | Kết quả quan sát |
| --- | --- |
| RTA nhận từ PCA1 | Inbound Layer 2 có MAC đích là MAC của RTA |
| RTA định tuyến | Router giữ IPv6 source/destination, nhưng thay frame Layer 2 cho chặng tiếp theo |
| RTA gửi sang PCB1 | Nếu chưa biết MAC của PCB1, RTA phải dùng NDP trên LAN phải |

![RTA forwards IPv6 packet](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/rta-forward-ipv6.png)

### Step 4 - Quan sát PCB1 trả lời về PCA1

| Câu hỏi | Trả lời |
| --- | --- |
| PCB1 thiếu thông tin gì trong outbound Layer 2? | MAC đích của default gateway trên LAN phải. |
| Khi ping lại sau khi cache đã học, còn NDP không? | Không, hoặc gần như không còn NDP cho cùng cặp giao tiếp vì neighbor cache đã có sẵn. |
| Destination MAC trong event của PCB1 tương ứng với thiết bị nào? | MAC của interface RTA nối với SwitchB/LAN phải. |
| Vì sao PCB1 dùng MAC của router? | Vì PCA1 nằm ở mạng khác, PCB1 phải gửi Echo Reply về default gateway trước. |

![PCB1 reply through router](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/pcb1-reply-router-mac.png)

## 6. Kiểm Tra Bảng IPv6 Neighbor Trên Router

### Step 1 - Xem neighbor sau khi ping remote

```text
RTA# show ipv6 neighbors
```

| Câu hỏi | Trả lời |
| --- | --- |
| Có bao nhiêu địa chỉ được liệt kê? | Thường có các host mà RTA đã giao tiếp trực tiếp, ví dụ PCA1 và PCB1. Số dòng có thể thay đổi theo trạng thái cache trong Packet Tracer. |
| Các địa chỉ đó gắn với thiết bị nào? | PCA1 ở LAN trái và PCB1 ở LAN phải. |
| Có entry của PCA2 không? | Không, nếu RTA chưa trực tiếp giao tiếp với PCA2 sau khi xóa neighbor cache. |

![RTA neighbors after remote ping](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/rta-neighbors-after-remote.png)

### Step 2 - Ping PCA2 từ router và kiểm tra lại

```text
RTA# ping 2001:db8:acad:1::b
RTA# show ipv6 neighbors
```

| Câu hỏi | Trả lời |
| --- | --- |
| Sau khi ping PCA2, có entry cho PCA2 không? | Có. RTA phải học MAC của PCA2 để gửi ICMPv6 trực tiếp trong LAN trái. |

![RTA neighbors after ping PCA2](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-04/rta-neighbors-after-pca2.png)

## 7. Tổng Hợp Đáp Án Reflection Questions

| Câu hỏi | Trả lời ngắn gọn |
| --- | --- |
| Khi nào thiết bị cần IPv6 Neighbor Discovery? | Khi cần gửi frame nhưng chưa biết MAC address của next-hop IPv6 trên cùng link. |
| Router giúp giảm NDP traffic như thế nào? | Host ở LAN này không cần học MAC của host ở LAN khác, chỉ cần học MAC của default gateway. |
| IPv6 giảm ảnh hưởng của ND lên host bằng cách nào? | Dùng solicited-node multicast thay vì broadcast toàn mạng như ARP. |
| Khác nhau giữa local LAN và remote LAN? | Local LAN tìm MAC của host đích; remote LAN tìm MAC của default gateway, sau đó router tìm MAC ở chặng tiếp theo. |

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không thấy NDP event | Chưa xóa neighbor cache hoặc chưa Reset Simulation | Dùng `clear ipv6 neighbors`, bấm Reset Simulation rồi ping lại |
| Event List quá nhiều giao thức | Chưa lọc đúng protocol | Vào Edit Filters, chọn IPv6, chỉ bật `ICMPv6` và `NDP` |
| Ping lần 2 không thấy NDP | Neighbor cache đã học MAC từ lần ping trước | Đây là hành vi đúng; muốn thấy lại thì xóa cache |
| Nhầm MAC đích khi ping remote | Tưởng PCA1 gửi trực tiếp tới MAC của PCB1 | Với remote LAN, MAC đích là MAC của default gateway |
| Không thấy PCA2 trong `show ipv6 neighbors` trên RTA | RTA chưa giao tiếp trực tiếp với PCA2 | Ping PCA2 từ RTA rồi kiểm tra lại |

## 9. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PCA1 ping PCA2 | Thành công, có NDP ở lần đầu nếu cache trống |
| PCA1 ping PCB1 | Thành công, PCA1 học MAC của default gateway |
| RTA `show ipv6 neighbors` | Hiển thị các neighbor đã giao tiếp trực tiếp |
| Ping lại cùng địa chỉ | Không tạo NDP mới nếu neighbor cache còn hiệu lực |
| Simulation Mode | Quan sát được ICMPv6 và NDP theo từng thiết bị |

Checklist ảnh minh chứng:

- [ ] `topology.png` - ảnh topology tổng quan
- [ ] `simulation-filter-icmpv6-ndp.png` - bộ lọc ICMPv6/NDP
- [ ] `first-icmpv6-pca1.png` - ICMPv6 Echo Request đầu tiên
- [ ] `ndp-event-pca1.png` - Neighbor Solicitation tại PCA1
- [ ] `ndp-event-pca2.png` - Neighbor Advertisement tại PCA2
- [ ] `icmpv6-echo-reply-local.png` - Echo Reply trong cùng LAN
- [ ] `ndp-default-gateway.png` - PCA1 học MAC default gateway khi ping remote LAN
- [ ] `rta-neighbors-after-remote.png` - bảng neighbor sau khi ping remote
- [ ] `rta-neighbors-after-pca2.png` - bảng neighbor sau khi RTA ping PCA2

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/">Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/">Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/">Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/">Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications</a></li>
    </ul>
  </details>
</div>

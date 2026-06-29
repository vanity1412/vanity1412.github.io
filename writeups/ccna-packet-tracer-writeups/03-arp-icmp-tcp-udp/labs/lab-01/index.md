---
layout: page-toc
title: "CCNA 03.01 - 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/
toc: true
---

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Quan sát HTTP, DNS, TCP trong Simulation Mode và đối chiếu với OSI/TCP-IP model |

> Bài này không yêu cầu cấu hình IP hay CLI. Mục tiêu chính là dùng **Simulation Mode** để nhìn quá trình đóng gói dữ liệu khi Web Client truy cập `www.osi.local` trên Web Server.

## 1. Mục Tiêu Bài Lab

- Chuyển Packet Tracer từ **Realtime Mode** sang **Simulation Mode**.
- Lọc sự kiện để quan sát riêng HTTP traffic.
- Tạo HTTP request từ Web Client đến `www.osi.local`.
- Mở PDU để xem dữ liệu ở từng lớp OSI.
- Đối chiếu thông tin trong **OSI Model tab** với **Outbound/Inbound PDU Details**.
- Quan sát thêm DNS, TCP và ARP trong TCP/IP protocol suite.
- Xác định port dịch vụ HTTP và DNS trên Web Server.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/topology.png)

Ảnh topology
![Topology lab 01](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/topology1.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Client | Web Client | Máy dùng Web Browser để truy cập `www.osi.local` |
| Server | Web Server | Cung cấp dịch vụ Web và DNS trong bài lab |
| Kết nối | Web Client ↔ Web Server | Kết nối trực tiếp trong cùng LAN, dùng để quan sát PDU |
| Chế độ làm bài | Simulation Mode | Dùng Event List để xem từng bước truyền dữ liệu |

> **Lưu ý:** Bài này tập trung vào quan sát PDU, không phải cấu hình địa chỉ IP. Nếu Event List trống, thường là do chưa bấm **Go** trong Web Browser hoặc chưa bấm **Capture/Forward**.

## 3. Kế Hoạch Làm Bài

| Bước | Việc cần làm | Ghi chú |
| --- | --- | --- |
| 1 | Chuyển sang Simulation Mode | Nút ở góc dưới bên phải Packet Tracer |
| 2 | Lọc sự kiện HTTP | Edit Filters → bỏ chọn tất cả → chọn HTTP |
| 3 | Truy cập web từ Web Client | Desktop → Web Browser → nhập `www.osi.local` |
| 4 | Bấm Capture/Forward | Bấm nhiều lần để tạo HTTP event |
| 5 | Mở từng PDU | Xem OSI Model, Inbound PDU Details, Outbound PDU Details |
| 6 | Bật lại Show All | Quan sát thêm DNS, TCP, ARP nếu có |
| 7 | Ghi lại port và thông tin các layer | HTTP port 80, DNS port 53 |

## 4. Part 1 - Examine HTTP Web Traffic

### Step 1 - Chuyển sang Simulation Mode và lọc HTTP

| Thao tác | Kết quả cần đạt |
| --- | --- |
| Chọn Simulation Mode | Thời gian mô phỏng dừng lại, Event List sẵn sàng ghi sự kiện |
| Edit Filters | Có thể bật/tắt các loại protocol cần quan sát |
| Chỉ chọn HTTP | Event List chỉ hiển thị HTTP event |

![HTTP filter](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/http-filter.png)

> **Lưu ý:** Nếu đang chọn quá nhiều protocol, Event List sẽ rất rối. Khi làm Part 1 nên chỉ giữ HTTP để dễ đọc luồng request/response.

### Step 2 - Tạo HTTP traffic từ Web Client

| Thao tác | Giá trị |
| --- | --- |
| Thiết bị thao tác | Web Client |
| Ứng dụng | Desktop → Web Browser |
| URL cần nhập | `www.osi.local` |
| Nút mô phỏng | Capture/Forward |
| Số HTTP event mong muốn | 4 event sau khi bấm Capture/Forward 4 lần |

![Web Browser](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/web-browser-osi-local.png)

| Câu hỏi | Trả lời |
| --- | --- |
| Web Client web browser page có thay đổi không? | Có. Sau khi HTTP request/response hoàn tất, trang web từ Web Server được tải về Web Client. |

### Step 3 - Quan sát HTTP PDU tại Web Client

| Vị trí quan sát | Thông tin ghi nhận |
| --- | --- |
| Event đầu tiên | PDU bắt đầu từ Web Client |
| Tab xuất hiện | OSI Model và Outbound PDU Details |
| Lý do chưa có Inbound PDU Details | Đây là điểm bắt đầu gửi dữ liệu, Web Client chưa nhận phản hồi |

| Layer | Câu hỏi | Trả lời |
| --- | --- | --- |
| Layer 7 | Thông tin trong numbered steps là gì? | HTTP client tạo HTTP request để gửi đến Web Server. |
| Layer 4 | Dst Port là gì? | `80` |
| Layer 3 | Dest. IP là gì? | IP của Web Server, thường là `192.168.1.254` trong bài này |
| Layer 2 | Hiển thị thông tin gì? | Source MAC và Destination MAC dùng cho Ethernet frame |

> **Lưu ý:** Layer 7 là HTTP, Layer 4 là TCP, Layer 3 là IP, Layer 2 là Ethernet. Cùng một gói tin nhưng Packet Tracer cho xem ở hai góc nhìn: OSI Model và PDU Details.

### Step 4 - Đối chiếu OSI Model với Outbound PDU Details

| Khu vực trong PDU Details | Thông tin chung với OSI Model | Layer tương ứng |
| --- | --- | --- |
| Ethernet II | Source MAC, Destination MAC | Layer 2 - Data Link |
| IP | Source IP, Destination IP | Layer 3 - Network |
| TCP | Source Port, Destination Port | Layer 4 - Transport |
| HTTP | Host `www.osi.local` và HTTP request | Layer 7 - Application |

| Câu hỏi | Trả lời |
| --- | --- |
| Host trong HTTP section là gì? | `www.osi.local` |
| Host này thuộc layer nào trong OSI Model? | Layer 7 - Application |

![Outbound PDU Details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/outbound-pdu-details.png)

### Step 5 - So sánh In Layers và Out Layers tại Web Server

| Nội dung so sánh | In Layers | Out Layers |
| --- | --- | --- |
| Hướng dữ liệu | Client → Server | Server → Client |
| IP | Source là Web Client, Destination là Web Server | Source là Web Server, Destination là Web Client |
| TCP port | Destination port là `80` | Source port là `80` |
| Layer 7 | HTTP request | HTTP response |
| Layer 2 | MAC nguồn/đích theo chiều nhận | MAC nguồn/đích đảo lại theo chiều gửi |

| Câu hỏi | Trả lời |
| --- | --- |
| Khác biệt lớn giữa In Layers và Out Layers là gì? | Chiều truyền bị đảo lại: request đi vào server, response đi ra từ server về client. IP, MAC và TCP port nguồn/đích cũng đổi vai trò. |


### Step 6 - Quan sát event cuối cùng của HTTP stream

| Câu hỏi | Trả lời |
| --- | --- |
| Có bao nhiêu tab được hiển thị ở event cuối? | 2 tab |
| Giải thích | Vì đây là điểm cuối của luồng HTTP tại Web Client, PDU chỉ còn chiều đi vào thiết bị nên thường chỉ có OSI Model và Inbound PDU Details. |


## 5. Part 2 - Display Elements of the TCP/IP Protocol Suite

### Step 1 - Hiển thị thêm các event khác

| Thao tác | Kết quả |
| --- | --- |
| Đóng các cửa sổ PDU đang mở | Tránh nhầm event |
| Event List Filters → Show All/None | Hiện thêm các protocol khác |
| Quan sát Event List | Thấy DNS, TCP, HTTP và có thể có ARP tùy trạng thái cache |

| Câu hỏi | Trả lời |
| --- | --- |
| Additional Event Types nào được hiển thị? | DNS, TCP, HTTP; ARP có thể xuất hiện nếu thiết bị cần phân giải MAC. |

> **Lưu ý:** DNS xuất hiện trước HTTP vì Web Client cần đổi tên `www.osi.local` thành IP. TCP xuất hiện để thiết lập phiên trước khi HTTP truyền dữ liệu.

### Step 2 - Quan sát DNS query và DNS answer

| DNS event | Thông tin cần xem | Kết quả |
| --- | --- | --- |
| First DNS event | DNS QUERY → NAME | `www.osi.local` |
| Last DNS event | PDU captured at | Web Client |
| Last DNS event | DNS ANSWER → ADDRESS | IP của Web Server, thường là `192.168.1.254` |

![DNS query](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/dns-query.png)
![DNS answer](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-01/dns-answer.png)

### Step 3 - Quan sát TCP session

| TCP event | Layer quan sát | Ý nghĩa |
| --- | --- | --- |
| TCP event sau HTTP đầu tiên | Layer 4 | TCP connection được thiết lập thành công |
| Last TCP event | Layer 4 | TCP session được đóng sau khi truyền dữ liệu xong |

| Câu hỏi | Trả lời |
| --- | --- |
| Items 4 và 5 ở TCP event cho biết gì? | TCP connection đã được chấp nhận và trạng thái phiên chuyển sang **ESTABLISHED**. |
| Mục đích của TCP event cuối là gì? | Đóng/kết thúc phiên TCP giữa Web Client và Web Server. |

## 6. Challenge Questions

| Câu hỏi | Trả lời |
| --- | --- |
| Web Server lắng nghe web request trên port nào? | TCP port `80` |
| Web Server lắng nghe DNS request trên port nào? | UDP port `53` |

> **Lưu ý:** HTTP dùng port 80 ở Layer 4. DNS thường dùng UDP port 53 cho truy vấn phân giải tên miền thông thường.

## 7. Tổng Hợp Quan Sát Theo OSI Và TCP/IP

| OSI Layer | TCP/IP Model | Protocol/Thông tin thấy trong lab | Ví dụ quan sát |
| --- | --- | --- | --- |
| Layer 7 - Application | Application | HTTP, DNS | `www.osi.local`, HTTP request, DNS query |
| Layer 4 - Transport | Transport | TCP, UDP port | HTTP TCP/80, DNS UDP/53 |
| Layer 3 - Network | Internet | IP address | Source IP, Destination IP |
| Layer 2 - Data Link | Network Access | Ethernet frame | Source MAC, Destination MAC |
| Layer 1 - Physical | Network Access | Bit truyền trên đường link | Frame được đưa ra khỏi buffer lên đường truyền |

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Event List không có gì | Chưa bấm Go trong Web Browser hoặc chưa bấm Capture/Forward | Nhập `www.osi.local`, bấm Go, sau đó bấm Capture/Forward |
| Không thấy HTTP event | Filter chưa chọn HTTP | Edit Filters → chọn HTTP trong danh sách protocol |
| Event List quá nhiều dòng | Đang bật quá nhiều protocol | Part 1 chỉ chọn HTTP, Part 2 mới bật Show All |
| Không thấy DNS event | Đang lọc chỉ HTTP hoặc DNS đã được cache | Bật Show All, có thể Reset Simulation rồi chạy lại |
| Nhầm port HTTP với DNS | Chưa kiểm tra Layer 4 | HTTP là TCP/80, DNS là UDP/53 |
| Nhầm In Layers và Out Layers | Không để ý hướng mũi tên | In Layers là chiều gói tin đi vào thiết bị, Out Layers là chiều thiết bị gửi ra |

## 9. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| Web Client truy cập `www.osi.local` | Trang web được tải thành công |
| HTTP filter | Event List hiển thị HTTP event |
| HTTP Layer 4 | Destination port là `80` |
| HTTP Layer 7 | Host là `www.osi.local` |
| DNS query | NAME là `www.osi.local` |
| DNS answer | ADDRESS là IP Web Server |
| TCP session | Có trạng thái established và closing |
| Challenge | HTTP port `80`, DNS port `53` |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/">Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/">Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/">Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/">Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications</a></li>
    </ul>
  </details>
</div>

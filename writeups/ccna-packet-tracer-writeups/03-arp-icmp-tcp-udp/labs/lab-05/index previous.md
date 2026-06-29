---
layout: page-toc
title: "CCNA 03.05 - 14.8.1 Packet Tracer - TCP and UDP Communications"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/
toc: true
---

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `14.8.1 Packet Tracer - TCP and UDP Communications.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Quan sát HTTP, FTP, DNS, Email trong Simulation Mode; phân biệt TCP và UDP qua PDU, port, sequence/acknowledgement |

> Bài này không tập trung cấu hình thiết bị. Trọng tâm là tạo nhiều loại traffic, lọc event trong Simulation Mode và đọc PDU để thấy TCP/UDP hoạt động như thế nào.

## 1. Mục Tiêu Bài Lab

- Tạo traffic HTTP, FTP, DNS và Email trong Packet Tracer Simulation Mode.
- Quan sát quá trình nhiều ứng dụng cùng truyền dữ liệu qua một mạng LAN.
- Xác định dịch vụ nào dùng TCP, dịch vụ nào dùng UDP.
- Đọc port nguồn, port đích, sequence number, acknowledgement number và TCP flag trong PDU.
- So sánh cơ chế truyền tin của TCP và UDP.
- Ghi lại bằng chứng từ Event List, OSI Model và PDU Details.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/topology.png)

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/topology.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Server | MultiServer | Cung cấp nhiều dịch vụ trên cùng một thiết bị: HTTP, FTP, DNS, SMTP/POP3 |
| Client | HTTP Client | Dùng Web Browser để tạo HTTP traffic |
| Client | FTP Client | Dùng Command Prompt để tạo FTP traffic |
| Client | DNS Client | Dùng `nslookup` để tạo DNS traffic |
| Client | E-Mail Client | Dùng ứng dụng E-Mail để tạo SMTP/POP3 traffic |
| Trung gian | Switch | Chuyển tiếp frame trong cùng LAN, không cần cấu hình trong bài này |

> **Lưu ý:** Bài này dùng một MultiServer chạy nhiều dịch vụ. Khi nhìn Event List, cần phân biệt protocol theo màu PDU và cột Type, không chỉ nhìn đường đi vật lý trên topology.

## 3. Bảng Dịch Vụ Và Port Cần Quan Sát

| Dịch vụ | Ứng dụng tạo traffic | Giao thức tầng Transport | Port server thường gặp | Ý nghĩa trong bài |
| --- | --- | --- | --- | --- |
| HTTP | Web Browser | TCP | 80 | Truy cập web server bằng địa chỉ `192.168.1.254` |
| FTP | Command Prompt `ftp` | TCP | 21 | Thiết lập phiên FTP tới MultiServer |
| DNS | Command Prompt `nslookup` | UDP | 53 | Phân giải `multiserver.pt.ptu` sang IP |
| SMTP | E-Mail Client Send | TCP | 25 | Gửi email tới server |
| POP3 | E-Mail Client Receive | TCP | 110 | Nhận email từ server |

> **Lưu ý:** TCP có sequence number, acknowledgement number và flags. UDP không có các trường này vì UDP không thiết lập phiên kết nối như TCP.

## 4. Part 1 - Generate Network Traffic In Simulation Mode

### Step 1: Tạo ARP trước để giảm traffic nhiễu

```text
MultiServer > Desktop > Command Prompt

ping -n 1 192.168.1.255
```

| Lệnh | Mục đích |
| --- | --- |
| `ping -n 1 192.168.1.255` | Gửi 1 gói ICMP tới broadcast address để các host phản hồi và bảng ARP được học trước |

![ARP warmup](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/arp-warmup.png)

### Step 2: Tạo HTTP traffic

```text
HTTP Client > Desktop > Web Browser

URL: 192.168.1.254
Go
```

| Quan sát | Giá trị cần ghi |
| --- | --- |
| Client tạo traffic | HTTP Client |
| Server đích | MultiServer `192.168.1.254` |
| Protocol chính | HTTP + TCP |
| Port đích | TCP/80 |

![HTTP traffic generated](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/http-traffic.png)

### Step 3: Tạo FTP traffic

```text
FTP Client > Desktop > Command Prompt

ftp 192.168.1.254
```

| Quan sát | Giá trị cần ghi |
| --- | --- |
| Client tạo traffic | FTP Client |
| Server đích | MultiServer `192.168.1.254` |
| Protocol chính | FTP + TCP |
| Port đích | TCP/21 |

![FTP traffic generated](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/ftp-traffic.png)

### Step 4: Tạo DNS traffic

```text
DNS Client > Desktop > Command Prompt

nslookup multiserver.pt.ptu
```

| Quan sát | Giá trị cần ghi |
| --- | --- |
| Client tạo traffic | DNS Client |
| Tên miền cần phân giải | `multiserver.pt.ptu` |
| IP trả về | `192.168.1.254` |
| Protocol chính | DNS + UDP |
| Port đích | UDP/53 |

![DNS traffic generated](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/dns-traffic.png)

### Step 5: Tạo Email traffic

| Trường | Giá trị nhập |
| --- | --- |
| To | `user@multiserver.pt.ptu` |
| Subject | Có thể tự đặt |
| Body | Có thể tự đặt |
| Hành động | Click `Send` |

![Email traffic generated](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/email-traffic.png)

### Step 6: Kiểm tra Event List đã có đủ traffic

| Client | Traffic mong muốn xuất hiện |
| --- | --- |
| HTTP Client | HTTP/TCP |
| FTP Client | FTP/TCP |
| DNS Client | DNS/UDP |
| E-Mail Client | SMTP/POP3/TCP |

![Simulation event list all traffic](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/event-list-all-traffic.png)

### Step 7: Quan sát multiplexing

| Câu hỏi | Trả lời |
| --- | --- |
| Khi nhiều PDU từ nhiều host cùng đi qua mạng, hiện tượng này gọi là gì? | Multiplexing |
| Ý nghĩa của các màu PDU khác nhau trong Event List là gì? | Mỗi màu đại diện cho một loại PDU/protocol/event khác nhau, giúp phân biệt HTTP, FTP, DNS, TCP, UDP, SMTP, POP3... |

> **Lưu ý:** Trên một đường link, tại một thời điểm chỉ có một PDU đi theo một chiều. Simulation Mode giúp thấy rõ nhiều luồng ứng dụng được ghép chung qua cùng hạ tầng mạng.

## 5. Part 2 - Examine TCP And UDP Protocols

### Step 1: Quan sát HTTP chạy trên TCP

```text
Simulation Panel > Reset Simulation
Edit Filters > Show All/None
Chọn: HTTP, TCP

HTTP Client > Web Browser
URL: 192.168.1.254
Go
```

| Câu hỏi | Trả lời |
| --- | --- |
| Vì sao mất một lúc HTTP PDU mới xuất hiện? | Vì TCP phải thiết lập kết nối trước bằng quá trình three-way handshake rồi HTTP mới bắt đầu truyền dữ liệu |
| Section cần xem trong Outbound PDU Details là gì? | `TCP` |
| HTTP có đáng tin cậy không? | Có, vì HTTP sử dụng TCP |
| TCP flag ở PDU đầu tiên thường là gì? | `SYN` |
| Port đích của HTTP request | `80` |

```text
HTTP Client -> MultiServer
TCP SYN
SRC PORT: ephemeral/random
DEST PORT: 80
SEQUENCE NUM: tùy phiên mô phỏng
ACK NUM: thường là 0 ở gói SYN đầu tiên
FLAGS: SYN
```

![HTTP TCP SYN](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/http-tcp-syn.png)

| PDU | Port | Sequence/Ack | Ý nghĩa |
| --- | --- | --- | --- |
| Client → Server | Src ephemeral, Dst 80 | Client khởi tạo sequence | Bắt đầu kết nối TCP bằng SYN |
| Server → Client | Src 80, Dst ephemeral | Server trả sequence riêng, ack sequence của client | SYN-ACK phản hồi |
| Client → Server | Src ephemeral, Dst 80 | Ack sequence của server | Hoàn tất three-way handshake |
| HTTP data | Src ephemeral, Dst 80 | Có sequence/ack hợp lệ | Bắt đầu gửi HTTP request |

> **Lưu ý:** Source port, sequence number và acknowledgement number có thể thay đổi theo từng lần chạy mô phỏng. Port đích HTTP vẫn là `80`.

### Step 2: Quan sát FTP chạy trên TCP

```text
Simulation Panel > Reset Simulation
Edit Filters > Show All/None
Chọn: FTP, TCP

FTP Client > Command Prompt
ftp 192.168.1.254
```

| Câu hỏi | Trả lời |
| --- | --- |
| FTP có dùng truyền thông đáng tin cậy không? | Có, vì FTP sử dụng TCP |
| Port đích của phiên FTP control | `21` |
| TCP flag ở PDU đầu tiên thường là gì? | `SYN` |
| Message server gửi về sau khi kết nối FTP bắt đầu | Thông điệp chào FTP dạng `220 ...` |

```text
FTP Client -> MultiServer
TCP SYN
SRC PORT: ephemeral/random
DEST PORT: 21
SEQUENCE NUM: tùy phiên mô phỏng
ACK NUM: thường là 0 ở gói SYN đầu tiên
FLAGS: SYN
```

![FTP TCP details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/ftp-tcp-details.png)

| PDU | Điểm khác biệt cần ghi |
| --- | --- |
| PDU đi từ client | Destination port là `21` |
| PDU trả về từ server | Source port là `21`, destination port là ephemeral port của client |
| PDU FTP greeting | Có nội dung phản hồi từ FTP server, thường bắt đầu bằng mã `220` |

### Step 3: Quan sát DNS chạy trên UDP

```text
Simulation Panel > Reset Simulation
Edit Filters > Show All/None
Chọn: DNS, UDP

DNS Client > Command Prompt
nslookup multiserver.pt.ptu
```

| Câu hỏi | Trả lời |
| --- | --- |
| Layer 4 protocol của DNS là gì? | UDP |
| DNS trong bài có được xem là reliable như TCP không? | Không, UDP không thiết lập kết nối và không có ACK/sequence như TCP |
| Port đích DNS query | `53` |
| Vì sao không có sequence và acknowledgement number? | Vì UDP header không có các trường sequence/acknowledgement number |
| Section cuối của DNS response là gì? | DNS Answer |
| IP của `multiserver.pt.ptu` | `192.168.1.254` |

```text
DNS Client -> MultiServer
UDP
SRC PORT: ephemeral/random
DEST PORT: 53
NAME: multiserver.pt.ptu

MultiServer -> DNS Client
UDP
SRC PORT: 53
DEST PORT: ephemeral/random
ANSWER: 192.168.1.254
```

![DNS UDP details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/dns-udp-details.png)

> **Lưu ý:** DNS thường dùng UDP/53 cho truy vấn thông thường. Khi phản hồi quay về, port nguồn và port đích đảo chiều so với gói query ban đầu.

### Step 4: Quan sát Email traffic chạy trên TCP

```text
Simulation Panel > Reset Simulation
Edit Filters > Show All/None
Chọn: POP3, SMTP, TCP

E-Mail Client > Desktop > E Mail
Compose > Send
```

| Câu hỏi | Trả lời |
| --- | --- |
| Email traffic dùng giao thức tầng Transport nào? | TCP |
| Email traffic có reliable không? | Có, vì SMTP và POP3 đều chạy trên TCP |
| TCP flag ở PDU đầu tiên thường là gì? | `SYN` |
| Protocol gắn với TCP port 25 | SMTP |
| Protocol gắn với TCP port 110 | POP3 |

```text
E-Mail Client -> MultiServer
TCP SYN
SRC PORT: ephemeral/random
DEST PORT: 25 hoặc 110 tùy luồng SMTP/POP3 đang quan sát
SEQUENCE NUM: tùy phiên mô phỏng
ACK NUM: thường là 0 ở gói SYN đầu tiên
FLAGS: SYN
```

![Email TCP details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-05/email-tcp-details.png)

| Luồng | Port server | Vai trò |
| --- | --- | --- |
| SMTP | TCP/25 | Gửi email từ client lên server |
| POP3 | TCP/110 | Client lấy thư từ mail server |

## 6. Tổng Hợp Câu Trả Lời Nhanh

| Nội dung hỏi | Đáp án |
| --- | --- |
| Hiện tượng nhiều luồng ứng dụng cùng đi qua mạng | Multiplexing |
| Ý nghĩa màu PDU | Phân biệt protocol/event type trong Simulation Mode |
| HTTP dùng TCP hay UDP | TCP |
| FTP dùng TCP hay UDP | TCP |
| DNS dùng TCP hay UDP trong bài này | UDP |
| Email SMTP/POP3 dùng TCP hay UDP | TCP |
| HTTP port | TCP/80 |
| FTP control port | TCP/21 |
| DNS port | UDP/53 |
| SMTP port | TCP/25 |
| POP3 port | TCP/110 |
| TCP có sequence/ack không | Có |
| UDP có sequence/ack không | Không |
| TCP flag bắt đầu kết nối | SYN |
| IP của MultiServer | `192.168.1.254` |
| Tên miền của MultiServer | `multiserver.pt.ptu` |

## 7. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Event List quá nhiều loại PDU | Chưa lọc protocol trong Edit Filters | Chọn `Show All/None`, sau đó chỉ tick protocol cần quan sát như HTTP/TCP hoặc DNS/UDP |
| Không thấy HTTP PDU ngay | TCP đang thực hiện handshake trước | Tiếp tục bấm `Capture/Forward` đến khi HTTP PDU xuất hiện |
| Không thấy DNS response | Gõ sai domain | Dùng đúng `nslookup multiserver.pt.ptu` |
| Không thấy email traffic | Chưa bấm `Send` hoặc đóng cửa sổ email quá sớm | Compose email rồi bấm `Send`, chỉ minimize cửa sổ |
| Không ghi được port/sequence chính xác | Mở sai tab PDU | Dùng `Outbound PDU Details` cho gói đi, `Inbound PDU Details` cho gói về |
| Nhầm TCP với UDP | Chỉ nhìn application, không nhìn Layer 4 | Luôn kiểm tra mục TCP hoặc UDP trong PDU Details |

## 8. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| Tạo đủ HTTP traffic | Event List có HTTP/TCP PDU |
| Tạo đủ FTP traffic | Event List có FTP/TCP PDU |
| Tạo đủ DNS traffic | Event List có DNS/UDP PDU |
| Tạo đủ Email traffic | Event List có SMTP/POP3/TCP PDU |
| Quan sát TCP | Thấy port, sequence number, acknowledgement number, flag |
| Quan sát UDP | Thấy source port, destination port; không có sequence/ack |
| Phân giải DNS | `multiserver.pt.ptu` trả về `192.168.1.254` |
| Kết luận | TCP dùng cho HTTP/FTP/Email; UDP dùng cho DNS query trong bài |

Checklist ảnh minh chứng nên chụp:

- [ ] `topology.png` - sơ đồ MultiServer và các client.
- [ ] `arp-warmup.png` - lệnh ping broadcast từ MultiServer.
- [ ] `event-list-all-traffic.png` - Event List có nhiều loại traffic.
- [ ] `http-tcp-syn.png` - TCP details của HTTP.
- [ ] `ftp-tcp-details.png` - TCP details của FTP.
- [ ] `dns-udp-details.png` - UDP details của DNS.
- [ ] `email-tcp-details.png` - TCP details của Email.
- [ ] `final-check.png` - ảnh tổng hợp hoặc ghi chú hoàn thành bài quan sát.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/">Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/">Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/">Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/">Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

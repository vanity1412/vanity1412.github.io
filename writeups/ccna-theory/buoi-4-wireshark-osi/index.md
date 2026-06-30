---
layout: page-toc
title: "Buổi 4: Wireshark và OSI"
permalink: /writeups/ccna-theory/buoi-4-wireshark-osi/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Wireshark và OSI

## Mục tiêu học tập

- Nắm vai trò của Wireshark và OSI trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Wireshark, OSI/TCP-IP, Encapsulation, IP/MAC, Default Gateway và phân tích gói tin

| Thông tin | Nội dung |
| --- | --- |
| Nguồn chính | Transcript/ghi chú Buổi 4 do người học cung cấp |
| Chủ đề | Wireshark, OSI/TCP-IP, đóng gói dữ liệu, IP/MAC, default gateway, Packet Tracer |
| Mục tiêu | Hiểu luồng dữ liệu mạng và biết dùng Wireshark để phân tích packet cơ bản |
| Nguồn học thêm từ Glasp | Glasp có tổng hợp video Jeremy’s IT Lab liên quan OSI Model & TCP/IP Suite, OSI Model Lab và The Life of a Packet. |

## 2. Định nghĩa học thuật

Wireshark là công cụ phân tích giao thức mạng, cho phép bắt, hiển thị và phân tích packet/frame đi qua card mạng hoặc được lưu trong file capture như .pcap, .pcapng.

## 3. Ví dụ trong buổi học

Giảng viên mở file capture mẫu từ PacketLife, phân tích HTTP và dùng chức năng Export Objects để trích xuất lại file ảnh PNG từ các packet HTTP đã bắt được.

- Một trang web, file ảnh hay email khi truyền qua mạng đều được chia thành nhiều packet.
- Nếu bắt đúng packet và biết đọc giao thức, mình có thể hiểu dữ liệu đã được truyền như thế nào.
- Wireshark đặc biệt hữu ích ch...

## 4. PacketLife và file capture mẫu

PacketLife là nguồn cung cấp các file capture mẫu để người học tải về và mở bằng Wireshark. Các file này thường có định dạng .pcap hoặc .pcapng.

| Khi học giao thức | Có thể quan sát gì trong file capture? |
| --- | --- |
| HTTP | Client gửi GET/POST gì, server phản hồi gì, có object nào được truyền |
| TCP | Bắt tay ba bước, sequence number, ACK, port nguồn/đích |
| DNS | Tên miền được hỏi là gì, DNS server trả về IP nào |
| ARP | Thiết bị hỏi MAC của IP nào, ai trả lời |
| ICMP | Echo Request/Echo Reply khi ping |

## 5. So sánh mô hình OSI và TCP/IP

| Tầng OSI | Tên tầng | Chức năng chính | Ví dụ/Giao thức liên quan |
| --- | --- | --- | --- |
| 7 | Application | Cung cấp dịch vụ mạng cho ứng dụng người dùng | HTTP, HTTPS, DNS, SMTP, FTP |
| 6 | Presentation | Định dạng, mã hóa, nén, chuyển đổi dữ liệu | PNG, JPG, MP4, TLS/SSL, encoding |
| 5 | Session | Thiết lập, duy trì, kết thúc phiên làm việc | Session giữa client và server |
| 4 | Transport | Chia nhỏ, vận chuyển, kiểm soát luồng dữ liệu | TCP, UDP, port |
| 3 | Network | Định tuyến và xử lý địa chỉ IP | IPv4, IPv6, router |
| 2 | Data Link | Đóng frame, xử lý MAC, truyền trong cùng mạng | Ethernet, Wi-Fi, switch, ARP |
| 1 | Physical | Truyền bit qua môi trường vật lý | Cáp mạng, sóng Wi-Fi, cáp quang |

| TCP/IP Model | Tương ứng OSI | Ý nghĩa |

## 6. Application Layer - Tầng ứng dụng

Đây là tầng gần người dùng nhất. Nó định nghĩa các dịch vụ mạng mà ứng dụng sử dụng, ví dụ trình duyệt web dùng HTTP/HTTPS, email dùng SMTP/POP3/IMAP, phân giải tên miền dùng DNS.

## 7. Presentation Layer - Tầng trình bày

Tầng này xử lý dữ liệu được biểu diễn dưới định dạng nào, có cần nén, mã hóa hay chuyển đổi không. Ví dụ ảnh .png, .jpg; video .mp4, .avi; văn bản có encoding.

## 8. Checklist thực hành

- Đọc yêu cầu lab và xác định phần kiến thức liên quan.
- Vẽ hoặc quan sát topology trước khi cấu hình.
- Ghi lại IP/subnet/VLAN/interface cần dùng.
- Cấu hình theo từng cụm nhỏ, tránh nhập toàn bộ một lần.
- Kiểm tra trạng thái interface và bảng liên quan sau mỗi bước.
- Dùng `ping`, `traceroute` hoặc lệnh `show` phù hợp để xác minh.
- Nếu lỗi, quay lại kiểm tra từ Layer 1/2 trước rồi mới lên Layer 3.
- Lưu cấu hình và ghi chú nguyên nhân lỗi nếu có.

## 9. Bảng tham chiếu nhanh

| Thông tin | Nội dung |
| --- | --- |
| Nguồn chính | Transcript/ghi chú Buổi 4 do người học cung cấp |
| Chủ đề | Wireshark, OSI/TCP-IP, đóng gói dữ liệu, IP/MAC, default gateway, Packet Tracer |
| Mục tiêu | Hiểu luồng dữ liệu mạng và biết dùng Wireshark để phân tích packet cơ bản |
| Nguồn học thêm từ Glasp | Glasp có tổng hợp video Jeremy’s IT Lab liên quan OSI Model & TCP/IP Suite, OSI Model Lab và The Life of a Packet. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Wireshark và OSI |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Wireshark và OSI giải quyết vấn đề gì trong mạng?
2. Các thành phần hoặc trạng thái quan trọng nhất của chủ đề này là gì?
3. Khi nào cần dùng kiến thức này trong lab CCNA?
4. Dấu hiệu nào cho thấy cấu hình hoặc thiết kế đang sai?

### Bài tập

1. Dựng một topology nhỏ trong Packet Tracer có liên quan đến bài học.
2. Cấu hình theo yêu cầu, sau đó ghi lại lệnh kiểm tra chính.
3. Tạo một lỗi thường gặp, quan sát triệu chứng và sửa lại.
4. Viết checklist 5 bước để tự kiểm tra trước khi nộp lab.

## 11. Thuật ngữ quan trọng

| Thuật ngữ | Tiếng Việt | Giải thích |
| --- | --- | --- |
| OSI | Mô hình 7 tầng | Khung phân tích quá trình truyền dữ liệu qua mạng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Wireshark và OSI nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

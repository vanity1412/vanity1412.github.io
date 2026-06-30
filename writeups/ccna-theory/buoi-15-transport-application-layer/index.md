---
layout: page-toc
title: "Buổi 15: Transport và Application Layer"
permalink: /writeups/ccna-theory/buoi-15-transport-application-layer/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Transport và Application Layer

## Mục tiêu học tập

- Nắm vai trò của Transport và Application Layer trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

TCP/UDP; Port Number; Three-Way Handshake; DNS; HTTP/HTTPS; Email

| --- | --- |
| Buổi số | Buổi 15 |
| Link video | https://www.youtube.com/watch?v=b8hU8E2E_fE |

Sau buổi học này, sinh viên sẽ:

Hiểu vị trí và vai trò của Transport Layer trong mô hình TCP/IP và OSI.

Phân biệt được TCP và UDP theo độ tin cậy, tốc độ, cách thiết lập kết nối và ứng dụng thực tế.

## 2. Bối cảnh buổi học: hoàn thiện các tầng TCP/IP

Khái niệm chính: Buổi học chuyển từ các nội dung về IP, IPv6 và ICMP sang hai tầng còn lại trong bộ giao thức TCP/IP: Transport Layer và Application Layer.

Ví dụ thực tế: Khi mở trình duyệt để truy cập website, IP giúp tìm đúng máy chủ, còn TCP/UDP và các giao thức ứng dụng quyết định cách dữ liệu web được gửi, nhận, kiểm tra và hiển thị.

- Buổi này liên kết kiến thức IP với ứng dụng thực tế.
- Transport Layer là cầu nối giữa IP và ứng dụng.
- Application Layer là nơi người dùng trực tiếp tương tác qua trình duyệt, email, DNS...

## 3. Transport Layer là gì?

Khái niệm chính: Transport Layer là tầng chịu trách nhiệm vận chuyển dữ liệu logic giữa các tiến trình ứng dụng chạy trên các host khác nhau. Tầng này nằm trên IP Layer và dưới Application Layer.

Ví dụ thực tế: Máy tính của bạn chạy Web Browser kết nối đến Web Server. Transport Layer giúp dữ liệu từ trình duyệt đi đến đúng dịch vụ web trên server, thay vì lẫn với email, DNS hoặc ứng dụng khác.

- Transport Layer không thay thế IP
- nó hoạt động bên trên IP.
- Tầng này quản lý các cuộc hội thoại/phiên truyền dữ liệu giữa ứng dụng.
- Hai giao thức đại diện quan trọng nhất là TCP và UDP.

Các nhiệm vụ chính của Transport Layer:

## 4. TCP và UDP

Khái niệm chính: TCP (Transmission Control Protocol) là giao thức hướng kết nối, có kiểm soát lỗi, xác nhận và truyền lại. UDP (User Datagram Protocol) là giao thức không hướng kết nối, nhẹ hơn, ít kiểm soát hơn và th...

Ví dụ thực tế: Tải file, web, email thường dùng TCP vì cần đủ dữ liệu. Gọi video/âm thanh thời gian thực, DNS query hoặc một số dịch vụ streaming có thể dùng UDP vì cần nhanh.

- TCP ưu tiên độ tin cậy.
- UDP ưu tiên tốc độ và độ nhẹ.
- TCP header lớn hơn UDP header, vì chứa nhiều trường điều khiển hơn.

| Tiêu chí | TCP | UDP |
| --- | --- | --- |

## 5. TCP/UDP Header, Port Number và Socket

Khái niệm chính: Port Number là số định danh dịch vụ ở Transport Layer. Source Port xác định cổng phía gửi, Destination Port xác định dịch vụ phía nhận. Socket Pair là cặp thông tin gồm IP nguồn, port nguồn, IP đích v...

Ví dụ thực tế: Khi bạn truy cập web, máy bạn mở một source port tạm thời như 51524, kết nối đến destination port 443 của server HTTPS. Nhờ vậy server biết đây là kết nối web bảo mật.

- Port giúp dữ liệu đến đúng dịch vụ.
- Source Port thường là cổng tạm thời phía client.
- Destination Port thường là cổng dịch vụ phía server.

Một số trường quan trọng trong TCP header:

| Trường | Ý nghĩa | Ghi nhớ nhanh |

## 6. TCP Three-Way Handshake

Khái niệm chính: TCP three-way handshake là quá trình thiết lập kết nối TCP gồm ba bước: SYN, SYN-ACK và ACK. Quá trình này giúp hai bên thống nhất rằng cả hai đều sẵn sàng gửi/nhận dữ liệu.

Ví dụ thực tế: Khi trình duyệt mở kết nối HTTPS đến web server, TCP thường phải bắt tay ba bước trước, sau đó mới truyền HTTP/HTTPS data.

- Bước 1: Client gửi SYN.
- Bước 2: Server trả SYN + ACK.
- Bước 3: Client gửi ACK.
- Sau đó dữ liệu mới được truyền trong phiên TCP.

Quy trình bắt tay ba bước:

## 7. Ngắt kết nối TCP

Khái niệm chính: Ngắt kết nối TCP là quá trình hai bên dùng cờ FIN và ACK để đóng phiên làm việc một cách có kiểm soát.

Ví dụ thực tế: Khi tải xong file hoặc đóng tab trình duyệt, kết nối TCP có thể được đóng bằng các gói FIN/ACK.

- FIN dùng để yêu cầu kết thúc.
- ACK dùng để xác nhận đã nhận yêu cầu.
- Đóng kết nối có kiểm soát giúp tránh mất dữ liệu còn đang truyền.

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

| --- | --- |
| Buổi số | Buổi 15 |
| Link video | https://www.youtube.com/watch?v=b8hU8E2E_fE |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Transport và Application Layer |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Transport và Application Layer giải quyết vấn đề gì trong mạng?
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
| Transport và Application Layer | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Transport và Application Layer nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

---
layout: page-toc
title: "Buổi 3: Mô hình mạng và giao thức"
permalink: /writeups/ccna-theory/buoi-3-giao-thuc-va-mo-hinh-mang/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Mô hình mạng và giao thức

## Mục tiêu học tập

- Nắm vai trò của Mô hình mạng và giao thức trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP MẠNG MÁY TÍNH

Biên soạn từ transcript bài giảng

| Tên bài | Buổi 3 |
| --- | --- |
| Chủ đề chính | Cisco IOS cơ bản, quy tắc truyền tin, TCP/IP, OSI, Packet Tracer |
| Nguồn video | https://www.youtube.com/watch?v=e-KLYN1UD1U |

Sau khi học xong buổi này, sinh viên cần đạt được các mục tiêu sau:

Ôn lại cách truy cập và cấu hình cơ bản thiết bị Cisco bằng Cisco IOS.

## 2. Ôn tập Cisco IOS và truy cập thiết bị Cisco

Khái niệm chính:

Cisco IOS là hệ điều hành chạy trên nhiều thiết bị Cisco như router và switch. Người quản trị tương tác với Cisco IOS chủ yếu thông qua giao diện dòng lệnh (CLI - Command Line Interface).

Ví dụ thực tế:

Khi mới mua một switch Cisco, quản trị viên chưa thể cấu hình bằng giao diện web như nhiều thiết bị dân dụng. Họ thường cắm cáp console, mở terminal, truy cập Cisco IOS và đặt các thông số cơ bản như hostname, mật khẩ...

## 3. Các chế độ dòng lệnh trên Cisco IOS

Khái niệm chính:

Cisco IOS chia CLI thành nhiều mode khác nhau. Mỗi mode có quyền hạn và phạm vi lệnh riêng. Các mode phổ biến gồm User EXEC mode, Privileged EXEC mode, Global Configuration mode, Line Configuration mode và Interface C...

Ví dụ thực tế:

Dấu nhắc `Router>` thường thể hiện User mode. Khi gõ `enable`, dấu nhắc thành `Router#`, tức Privileged mode. Khi gõ `configure terminal`, ta vào chế độ cấu hình tổng thể để sửa cấu hình thiết bị.

| Mode | Dấu nhắc thường gặp | Mục đích | Ví dụ lệnh chuyển vào |
| --- | --- | --- | --- |

## 4. Cấu trúc lệnh và lưu cấu hình

Khái niệm chính:

Lệnh trong Cisco IOS thường gồm command, keyword và argument. Sau khi cấu hình xong, cần lưu cấu hình đang chạy (running-config) vào cấu hình khởi động (startup-config).

Ví dụ thực tế:

Lệnh `copy running-config startup-config` có thể hiểu như thao tác “Save” trong Word. Nếu chỉ cấu hình mà không save, khi tắt/mở lại thiết bị, thay đổi có thể không còn.

## 5. IPv4, Subnet Mask và Default Gateway

Khái niệm chính:

IPv4 address là địa chỉ 32 bit dùng để định danh thiết bị trong mạng. Subnet mask cũng dài 32 bit, dùng để phân biệt phần network và phần host. Default gateway là địa chỉ thiết bị trung gian giúp máy tính đi ra mạng k...

Ví dụ thực tế:

Máy tính PC0 có IP 192.168.1.2/24. Nếu muốn truy cập ra ngoài mạng 192.168.1.0/24, PC0 cần biết default gateway, ví dụ 192.168.1.1, để gửi gói tin ra ngoài.

## 6. Phân biệt Port và Interface

Khái niệm chính:

Port thường chỉ cổng vật lý trên thiết bị mạng, nơi cắm dây mạng. Interface là khái niệm rộng hơn, có thể là cổng vật lý hoặc giao diện logic được dùng để cấu hình và truyền thông.

Port là “lỗ cắm dây”. Interface là “đối tượng cấu hình” gắn với cổng hoặc một giao diện logic. Khi nói cấu hình địa chỉ IP, bật/tắt cổng, chia sub-interface hoặc gom nhiều cổng, ta thường dùng khái niệm interface.

Ví dụ thực tế:

Trên switch Cisco, các cổng như FastEthernet0/1, FastEthernet0/2 có thể được gọi là port. Nhưng khi cấu hình, ta vào `interface fa0/1`. Ngoài ra switch có thể có `interface VLAN 1` là interface logic để đặt IP quản tr...

| Tiêu chí | Port | Interface |

## 7. Vì sao cần học giao thức và mô hình truyền tin?

Khái niệm chính:

Protocol là bộ quy tắc quy định cách các thiết bị truyền, nhận, định dạng, kiểm tra và xử lý dữ liệu. Communication model là mô hình mô tả cách dữ liệu đi qua các tầng hoặc các bước truyền tin.

Ví dụ thực tế:

Khi bạn mở website, trình duyệt và web server phải thống nhất dùng HTTP/HTTPS, TCP, IP và công nghệ mạng bên dưới. Nếu mỗi bên làm theo một kiểu riêng thì dữ liệu sẽ không thể hiểu được.

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

| Tên bài | Buổi 3 |
| --- | --- |
| Chủ đề chính | Cisco IOS cơ bản, quy tắc truyền tin, TCP/IP, OSI, Packet Tracer |
| Nguồn video | https://www.youtube.com/watch?v=e-KLYN1UD1U |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Mô hình mạng và giao thức |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Mô hình mạng và giao thức giải quyết vấn đề gì trong mạng?
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
| Mô hình mạng và giao thức | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Mô hình mạng và giao thức nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

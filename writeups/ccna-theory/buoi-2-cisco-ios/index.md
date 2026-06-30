---
layout: page-toc
title: "Buổi 2: Cisco IOS"
permalink: /writeups/ccna-theory/buoi-2-cisco-ios/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Cisco IOS

## Mục tiêu học tập

- Nắm vai trò của Cisco IOS trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP

Tài liệu học tập biên soạn từ transcript bài giảng

THÔNG TIN BÀI HỌC Title: Buổi 2 URL: https://www.youtube.com/watch?v=M-cZF_6OV3Y Chủ đề chính: Làm quen thiết bị Cisco, Cisco IOS, cáp console, các chế độ CLI, cấu hình cơ bản và lưu cấu hình.

## 2. Mẹo ghi nhớ nhanh

Sau buổi học này, sinh viên cần đạt được các mục tiêu sau:

Hiểu thiết bị mạng Cisco cũng cần có hệ điều hành riêng để hoạt động, gọi là Cisco IOS.

Phân biệt được các cách tương tác với hệ điều hành: GUI và CLI, trong đó thiết bị Cisco thường cấu hình bằng CLI.

Biết cách kết nối PC với switch/router Cisco bằng cáp console trong Cisco Packet Tracer.

Nhận biết và chuyển đổi giữa các chế độ lệnh quan trọng: User mode, Privileged EXEC mode, Global Configuration mode, Line Configuration mode và Interface Configuration mode.

Biết dùng các công cụ hỗ trợ gõ lệnh như dấu hỏi chấm (?) và phím Tab.

## 3. Giới thiệu buổi học và thiết bị Cisco

Khái niệm chính: Buổi học giới thiệu cách làm quen với thiết bị mạng Cisco, đặc biệt là những bước đầu tiên khi sinh viên tiếp xúc với switch/router mới và cần cấu hình cơ bản.

Giải thích dễ hiểu: Khi bạn mua một thiết bị mạng như switch, router hoặc access point, thiết bị đó không tự “hiểu” bạn muốn nó hoạt động ra sao. Người quản trị mạng phải truy cập vào thiết bị và cấu hình các thông ti...

Điểm cần nhớ:

Thiết bị Cisco trong bài học chủ yếu gồm switch và router.

## 4. Hệ điều hành và Cisco IOS

Khái niệm chính: Thiết bị Cisco là phần cứng, muốn hoạt động cần có hệ điều hành. Hệ điều hành của thiết bị Cisco được gọi là Cisco IOS.

Operating System (Hệ điều hành)

| Khái niệm | Operating System (Hệ điều hành) |
| --- | --- |
| Định nghĩa học thuật | Là phần mềm hệ thống quản lý tài nguyên phần cứng và cung cấp môi trường để các chương trình, dịch vụ hoạt động. |
| Ví dụ thực tế | Máy tính cần Windows/Linux để chạy; switch Cisco cần Cisco IOS để xử lý lệnh và chuyển mạch. |

Kernel (Nhân hệ điều hành)

## 5. GUI và CLI – hai cách tương tác với hệ điều hành

Khái niệm chính: Người dùng có thể tương tác với hệ điều hành qua giao diện đồ họa GUI hoặc giao diện dòng lệnh CLI.

GUI – Graphic User Interface

| Khái niệm | GUI – Graphic User Interface |
| --- | --- |
| Định nghĩa học thuật | Là giao diện người dùng đồ họa, cho phép thao tác bằng cửa sổ, biểu tượng, menu và chuột. |
| Ví dụ thực tế | Trên máy tính, bạn mở thư mục bằng cách double-click vào biểu tượng thư mục. |

CLI – Command Line Interface

## 6. Kết nối PC với thiết bị Cisco bằng cáp console

Khái niệm chính: Để cấu hình ban đầu cho switch/router Cisco, người quản trị thường kết nối máy tính với thiết bị bằng cáp console, sau đó mở terminal hoặc phần mềm như PuTTY để truy cập CLI.

Console Cable (Cáp console)

| Khái niệm | Console Cable (Cáp console) |
| --- | --- |
| Định nghĩa học thuật | Là loại cáp dùng để kết nối trực tiếp máy tính quản trị với cổng console trên thiết bị mạng nhằm cấu hình thiết bị qua CLI. |
| Ví dụ thực tế | Trong Packet Tracer, nối PC cổng RS232 sang switch cổng Console bằng dây console màu xanh nhạt. |

Giải thích dễ hiểu: Khi switch mới chưa có địa chỉ IP, bạn chưa thể SSH/Telnet từ xa vào nó. Vì vậy, cách cơ bản nhất là cắm dây console trực tiếp từ máy tính vào switch để cấu hình ban đầu.

## 7. Các chế độ hoạt động trong Cisco IOS

Khái niệm chính: Cisco IOS chia CLI thành nhiều chế độ. Mỗi chế độ cho phép dùng một nhóm lệnh khác nhau. Muốn gõ đúng lệnh, trước tiên phải vào đúng chế độ.

| Chế độ | Dấu nhắc lệnh | Mục đích | Lệnh vào | Lệnh thoát |
| --- | --- | --- | --- | --- |
| User EXEC mode | Switch> | Xem thông tin cơ bản, quyền hạn hạn chế | Mặc định khi mới đăng nhập | exit |
| Privileged EXEC mode | Switch# | Xem nhiều thông tin hơn, thực hiện lệnh quản trị như show, copy, reload | enable | exit |
| Global Configuration mode | Switch(config)# | Cấu hình tổng quát cho thiết bị | configure terminal | exit / end |
| Line Configuration mode | Switch(config-line)# | Cấu hình đường truy cập console/VTY | line console 0 hoặc line vty 0 15 | exit |
| Interface Configuration mode | Switch(config-if)# | Cấu hình cổng/interface cụ thể | interface vlan 1 hoặc interface fa0/1 | exit |
| Ví dụ di chuyển giữa các chế độ: Switch> enable Switch# configure terminal Switch(config)# line console 0 Switch(config-line)# exit Switch(config)# interface vlan 1 Switch(config-if)# exit Switch(config)# end Switch# exit | Ví dụ di chuyển giữa các chế độ: Switch> enable Switch# configure terminal Switch(config)# line console 0 Switch(config-line)# exit Switch(config)# interface vlan 1 Switch(config-if)# exit Switch(config)# end Switch# exit | Ví dụ di chuyển giữa các chế độ: Switch> enable Switch# configure terminal Switch(config)# line console 0 Switch(config-line)# exit Switch(config)# interface vlan 1 Switch(config-if)# exit Switch(config)# end Switch# exit | Ví dụ di chuyển giữa các chế độ: Switch> enable Switch# configure terminal Switch(config)# line console 0 Switch(config-line)# exit Switch(config)# interface vlan 1 Switch(config-if)# exit Switch(config)# end Switch# exit | Ví dụ di chuyển giữa các chế độ: Switch> enable Switch# configure terminal Switch(config)# line console 0 Switch(config-line)# exit Switch(config)# interface vlan 1 Switch(config-if)# exit Switch(config)# end Switch# exit |

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

| Phần | Nội dung chính | Ý nghĩa học tập |
| --- | --- | --- |
| 1 | Thiết bị Cisco và Cisco IOS | Hiểu switch/router là phần cứng cần hệ điều hành để hoạt động. |
| 2 | GUI, CLI và Kernel | Hiểu cách người dùng tương tác với hệ điều hành và phần cứng. |
| 3 | Cáp console và Packet Tracer | Biết cách kết nối PC với thiết bị Cisco để cấu hình ban đầu. |
| 4 | Các chế độ lệnh | Biết đang ở chế độ nào và lệnh nào được phép sử dụng. |
| 5 | Cú pháp lệnh Cisco IOS | Biết dùng command, keyword, argument, dấu ? và Tab. |
| 6 | Cấu hình bảo mật cơ bản | Đặt hostname, password, enable secret, line console, line VTY. |
| 7 | Mã hóa mật khẩu, banner và lưu cấu hình | Giúp cấu hình an toàn hơn và không bị mất sau khi khởi động lại. |
| 8 | Bài thực hành Packet Tracer | Luyện lại các lệnh vừa học qua bài 2.2.5.5. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Cisco IOS |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Cisco IOS giải quyết vấn đề gì trong mạng?
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
| IOS | Hệ điều hành Cisco | Môi trường CLI dùng để cấu hình router/switch Cisco. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Cisco IOS nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

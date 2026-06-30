---
layout: page-toc
title: "Buổi 8: Switch, MAC, ARP và SSH"
permalink: /writeups/ccna-theory/buoi-8-switch-mac-arp-ssh/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Switch, MAC, ARP và SSH

## Mục tiêu học tập

- Nắm vai trò của Switch, MAC, ARP và SSH trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

TÀI LIỆU HỌC TẬP BUỔI 8 Switch, MAC Address Table, ARP, Interface VLAN và SSH

| --- | --- |
| Buổi số | Buổi 8 |
| Ngày | Chưa xác định trong transcript |
| Nguồn | Transcript video: https://www.youtube.com/watch?v=pcdoiG-n0Co |

## 2. MỤC LỤC

| Nội dung | Mục |
| --- | --- |
| 1. Mục tiêu buổi học | 1 |
| 2. Tổng quan nội dung | 2 |
| 3. Nội dung chi tiết | 3 |
| 4. Bảng so sánh các khái niệm dễ nhầm | 4 |
| 5. Quy trình / Flow cần nắm | 5 |
| 6. Ví dụ minh họa mở rộng | 6 |
| 7. Kiến thức trọng tâm cần nhớ | 7 |
| 8. Bảng thuật ngữ | 8 |

## 3. Bối cảnh buổi học và môi trường thực hành

Do lịch học cuối tuần bị trùng với lịch công tác và kỳ thi của sinh viên, buổi học được tổ chức trong tuần với mục tiêu review kiến thức và giải đáp thắc mắc từ các bài tập thực hành trước đó. Các bài tập được nhắc lạ...

Trước khi cấu hình thiết bị thật trong doanh nghiệp, sinh viên cần luyện trên phần mềm để quen thao tác, hiểu lệnh và quan sát được gói tin.

Ví dụ thực tế: Cisco Packet Tracer cho phép kéo thả PC, switch, router và cấu hình bằng CLI. Wireshark dùng để bắt và phân tích gói tin như ARP, ICMP, TCP, DNS trong mạng thật hoặc lab.

| Công cụ | Vai trò trong học mạng | Khi nào nên dùng |
| --- | --- | --- |
| Cisco Packet Tracer | Mô phỏng thiết bị Cisco, cấu hình switch/router, quan sát trạng thái port và packet flow. | Khi học CCNA, làm lab VLAN, routing, switching, SSH, DHCP, ACL. |
| Wireshark | Bắt và phân tích gói tin thật, đọc header, xem ARP/ICMP/TCP/DNS. | Khi cần hiểu packet đi qua mạng như thế nào hoặc điều tra sự cố. |

## 4. Cấu hình switch/router bằng Console

Trong Packet Tracer, để cấu hình switch hoặc router từ đầu, sinh viên thường dùng kết nối Console. Máy tính PC có cổng RS232, switch/router có cổng Console. Sau khi nối cáp Console, mở Terminal trên PC để truy cập gia...

Ví dụ thực tế: Kỹ thuật viên mạng mới nhận một switch Cisco từ kho. Switch chưa có địa chỉ IP quản trị. Kỹ thuật viên cần cắm cáp Console từ laptop vào switch để đặt hostname, IP quản trị, mật khẩu và bật SSH.

## 5. Vào CLI để cấu hình thiết bị.

Console không yêu cầu thiết bị phải có IP. SSH/Telnet thì yêu cầu thiết bị phải có IP quản trị và cấu hình truy cập từ xa.

Muốn cấu hình thiết bị mới hoặc thiết bị chưa có IP, dùng Console. Sau khi cấu hình IP và SSH, có thể quản trị từ xa.

## 6. Vì sao cổng switch chuyển từ màu cam sang xanh chậm?

Giảng viên đặt câu hỏi: khi nối PC vào switch, đèn cổng thường màu cam một lúc lâu rồi mới chuyển sang xanh. Trong khi đó nếu nối PC vào hub thì đèn xanh gần như ngay lập tức. Nguyên nhân nằm ở bản chất hoạt động của...

Switch không “đẩy tín hiệu ngay lập tức” như hub. Nó phải kiểm tra, lắng nghe và học xem thiết bị đang nối vào là gì, có nguy cơ loop không, rồi mới cho cổng chuyển sang trạng thái hoạt động ổn định.

Ví dụ thực tế: Trong doanh nghiệp, nếu hai switch được nối vòng sai cách, mạng có thể bị broadcast storm. Vì vậy switch cần cơ chế như Spanning Tree Protocol (STP) để tránh loop. Quá trình này khiến cổng mất một khoản...

| Thiết bị | Mức độ thông minh | Khi cắm cáp | Khả năng học MAC |
| --- | --- | --- | --- |
| Hub | Thiết bị đơn giản, chủ yếu lặp tín hiệu. | Thường sáng nhanh vì không kiểm tra phức tạp. | Không học MAC, không biết máy nào ở cổng nào. |
| Switch | Thiết bị thông minh, có hệ điều hành và bảng MAC. | Có thể qua các trạng thái listening/learning trước khi forwarding. | Học MAC nguồn và ánh xạ với cổng tương ứng. |

## 7. Spanning Tree PortFast cho cổng nối máy tính

Giảng viên giới thiệu một lệnh giúp cổng switch nối PC chuyển sang xanh nhanh hơn: cấu hình PortFast trên các cổng access dành cho máy tính. Trong transcript, lệnh được nhắc là “spanning ... fast”; khi chuẩn hóa theo...

Khi đã chắc cổng này chỉ cắm máy tính, không cắm switch khác, ta cho switch “bỏ qua thời gian chờ dài” để cổng dùng được nhanh hơn.

Ví dụ thực tế: Văn phòng có 20 máy tính nhân viên cắm vào switch access. Nếu không bật PortFast, mỗi lần máy khởi động hoặc cắm dây mạng, máy có thể phải chờ lâu hơn mới lấy IP hoặc vào mạng. Bật PortFast trên cổng ac...

Chỉ nên bật PortFast trên cổng nối thiết bị đầu cuối như PC, laptop, printer. Không bật tùy tiện trên cổng nối giữa switch với switch nếu chưa hiểu rõ, vì có thể gây rủi ro loop.

PortFast giúp cổng access lên nhanh. Đây là lệnh hữu ích trong lab và thực tế, nhưng phải dùng đúng vị trí.

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
| Buổi số | Buổi 8 |
| Ngày | Chưa xác định trong transcript |
| Nguồn | Transcript video: https://www.youtube.com/watch?v=pcdoiG-n0Co |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Switch, MAC, ARP và SSH |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Switch, MAC, ARP và SSH giải quyết vấn đề gì trong mạng?
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
| Switch | Bộ chuyển mạch | Thiết bị Layer 2 chuyển frame dựa vào MAC address. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Switch, MAC, ARP và SSH nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

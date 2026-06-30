---
layout: page-toc
title: "Buổi 14: ICMP, Ping và Traceroute"
permalink: /writeups/ccna-theory/buoi-14-icmp-ping-traceroute/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# ICMP, Ping và Traceroute

## Mục tiêu học tập

- Nắm vai trò của ICMP, Ping và Traceroute trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Hiểu vì sao IP là giao thức phi kết nối (connectionless) và vì sao cần ICMP để phản hồi lỗi/chẩn đoán.

Nắm được vai trò của ICMP trong IPv4 và ICMPv6 trong IPv6.

Phân biệt Echo Request, Echo Reply, Time Exceeded, Router Advertisement, Router Solicitation, Neighbor Solicitation và Neighbor Advertisement.

Hiểu nguyên lý của lệnh ping, tracert/traceroute và vai trò của TTL/Time To Live.

Biết quy trình kiểm tra lỗi kết nối IPv4/IPv6 trong Packet Tracer bằng ipconfig, ping, tracert và các lệnh show trên router.

Hình thành tư duy xử lý sự cố mạng: kiểm tra từ máy người dùng, xác định chặng lỗi, sửa cấu hình rồi kiểm tra lại.

## 2. Ôn tập IPv6 và giới thiệu ICMP

Khái niệm chính: ICMP (Internet Control Message Protocol) là giao thức dùng để gửi thông điệp điều khiển, báo lỗi và hỗ trợ chẩn đoán trong mạng IP.

Ví dụ thực tế: Khi dùng lệnh ping đến 8.8.8.8, máy gửi không truyền dữ liệu ứng dụng mà gửi một thông điệp kiểm tra xem máy đích có phản hồi hay không.

- ICMP không phải là giao thức truyền dữ liệu ứng dụng như HTTP, FTP.
- ICMP thường đi kèm với IP để báo lỗi, phản hồi trạng thái và hỗ trợ kiểm tra kết nối.
- Buổi 14 nối tiếp kiến thức IPv6 của Buổi 13 và chuyển sang...

- Nắm tên giao thức ICMP và vai trò báo lỗi/chẩn đoán.
- ICMP gắn trực tiếp với các công cụ ping và traceroute.

## 3. IP là giao thức phi kết nối (connectionless)

Khái niệm chính: IP là giao thức phi kết nối, nghĩa là trước khi gửi gói tin, nó không thiết lập sẵn một phiên/kênh truyền đảm bảo giữa nguồn và đích.

Ví dụ thực tế: Một PC gửi gói tin đến server. Nếu router trên đường đi không chuyển tiếp được, router có thể gửi lại ICMP để báo lỗi cho PC nguồn.

- IP không tự đảm bảo gói tin chắc chắn đến đích.
- Khi có lỗi, ICMP giúp phản hồi tình trạng cho nguồn gửi.
- Không nên hiểu ICMP làm cho IP trở thành giao thức tin cậy
- ICMP chỉ báo hiệu/chẩn đoán.

- IP gửi trước, không bắt tay trước.

## 4. Ping và cặp thông điệp Echo Request / Echo Reply

Khái niệm chính: Ping là công cụ kiểm tra khả năng đến được của một host bằng cách gửi ICMP Echo Request và chờ ICMP Echo Reply.

Ví dụ thực tế: Khi ping 8.8.8.8 và thấy “Reply from 8.8.8.8”, điều đó cho thấy host đích có phản hồi ở mức mạng.

- Echo Request là bản tin hỏi.
- Echo Reply là bản tin trả lời.
- Ping thành công không khẳng định mọi dịch vụ đều chạy
- nó chỉ cho biết kết nối ICMP có phản hồi.

- Ping là bài kiểm tra nhanh nhất để xem host có phản hồi hay không.

## 5. ICMPv4, ICMPv6 và thông điệp Time Exceeded

Khái niệm chính: ICMP có phiên bản cho IPv4 và ICMPv6 cho IPv6. Ngoài báo lỗi, ICMPv6 còn tham gia nhiều chức năng nền của IPv6 như neighbor discovery và router discovery.

Ví dụ thực tế: Khi TTL (Time To Live) của gói tin giảm về 0 tại một router, router sẽ hủy gói và gửi ICMP Time Exceeded về máy nguồn.

- TTL giúp tránh việc gói tin chạy vòng lặp mãi trong mạng.
- Time Exceeded là thông điệp quan trọng giúp traceroute xác định từng chặng.
- ICMPv6 quan trọng hơn trong IPv6 vì liên quan đến RA/RS và NS/NA.

- ICMPv4: hay gặp khi ping/báo lỗi.
- ICMPv6: vừa báo lỗi, vừa hỗ trợ hoạt động nền của IPv6.

## 6. Tracert / Traceroute và nguyên lý TTL tăng dần

Khái niệm chính: Traceroute là công cụ dò đường đi đến đích bằng cách gửi các gói tin với TTL tăng dần, khiến từng router trung gian lần lượt phản hồi ICMP Time Exceeded.

Ví dụ thực tế: Trên Windows dùng lệnh tracert, trên router hoặc một số hệ thống dùng traceroute. Nếu một router không phản hồi ICMP, kết quả có thể hiện request timed out nhưng không có nghĩa chắc chắn đường truyền đã...

- Ping kiểm tra có đến được đích hay không.
- Traceroute kiểm tra đường đi qua những chặng nào.
- Traceroute dựa vào TTL và ICMP Time Exceeded.

- TTL=1 làm router đầu tiên phản hồi.
- TTL=2 làm router thứ hai phản hồi.

## 7. Verify IPv4/IPv6 bằng ipconfig, ping và traceroute trong Packet Tracer

Khái niệm chính: Verify connectivity là quá trình kiểm tra cấu hình địa chỉ, gateway và khả năng kết nối giữa các thiết bị trong mạng.

- Trước khi sửa lỗi, cần xác nhận máy đang có đúng IP chưa, gateway đúng chưa, ping được gateway chưa, rồi mới kiểm tra xa hơn.

Ví dụ thực tế: Trong bài 13.2.6 và 13.2.7, sinh viên kiểm tra PC1, PC2, router R1/R2/R3 bằng ipconfig, ping, tracert và các lệnh show để xác định sai IP hoặc sai default gateway.

- Luôn kiểm tra IP local trước khi nghi ngờ router xa.
- Ping gateway là bước kiểm tra rất quan trọng.
- show ip interface brief và show ipv6 interface brief giúp kiểm tra nhanh cấu hình router.

- Verify là kiểm tra đúng/sai trước khi sửa.

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

| Tiêu chí | Ping | Traceroute / Tracert |
| --- | --- | --- |
| Mục đích | Kiểm tra host đích có phản hồi hay không | Xác định đường đi qua các router trung gian |
| Thông điệp chính | ICMP Echo Request và Echo Reply | ICMP Time Exceeded từ từng chặng và phản hồi từ đích |
| TTL | Dùng TTL mặc định của hệ điều hành | Bắt đầu TTL=1, sau đó tăng dần |
| Kết quả đọc được | Reply, timeout, unreachable | Danh sách hop/chặng, thời gian phản hồi, timeout tại một số chặng |
| Khi dùng | Kiểm tra nhanh kết nối | Khoanh vùng chặng gây lỗi |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | ICMP, Ping và Traceroute |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. ICMP, Ping và Traceroute giải quyết vấn đề gì trong mạng?
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
| ICMP | Giao thức thông báo lỗi | Hỗ trợ ping, traceroute và báo lỗi IP. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 ICMP, Ping và Traceroute nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

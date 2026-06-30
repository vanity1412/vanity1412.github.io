---
layout: page-toc
title: "Buổi 34: OSPF Advanced"
permalink: /writeups/ccna-theory/buoi-34-ospf-advanced-pointtopoint-passive-drbdr/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# OSPF Advanced

## Mục tiêu học tập

- Nắm vai trò của OSPF Advanced trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP MẠNG MÁY TÍNH

Tài liệu học tập từ transcript: Single-Area OSPF nâng cao, tối ưu bản tin định tuyến và kiểm tra OSPF trong Packet Tracer

| Thông tin | Nội dung |
| --- | --- |
| Tên video | Buổi 34 |
| URL | https://www.youtube.com/watch?v=o0rkx-yeZ6Y |
| Chủ đề chính | OSPF nâng cao: point-to-point, passive-interface, DR/BDR, metric/cost, loopback và default-information originate |
| Mục tiêu | Biết tối ưu cấu hình OSPF, giảm gói tin thừa, kiểm tra neighbor/route và triển khai default route qua OSPF. |

## 2. Nguồn và ghi chú

nhanh Buổi này không chỉ cấu hình OSPF chạy được, mà còn học cách tối ưu OSPF: cổng nào nên im lặng, link nào không cần DR/BDR, đường nào nên có cost thấp hơn, và làm sao phát default route cho toàn miền OSPF.

## 3. Ôn lại router ảo/HSRP trước khi vào OSPF

Đầu buổi học có phần hỏi lại về “router ảo”. Ý chính: router ảo không phải thiết bị vật lý mới, mà là một Virtual IP được nhiều router cùng tham gia nắm giữ theo từng thời điểm. Máy trạm chỉ cần trỏ default gateway về...

## 4. Point-to-point network

Point-to-point là kiểu kết nối chỉ có hai router ở hai đầu link, thường thấy với serial link trong Packet Tracer. Vì chỉ có hai router, OSPF không cần bầu DR/BDR trên link này.

## 5. Passive interface

Khi một interface hướng xuống LAN người dùng, router vẫn cần quảng bá network đó cho các router khác biết. Tuy nhiên, các PC/switch layer 2 không cần nhận OSPF Hello, nên interface đó nên để passive.

`passive-interface` không có nghĩa là bỏ quảng bá network. Nó chỉ chặn OSPF Hello ra interface đó, giúp giảm gói tin thừa và hạn chế neighbor không mong muốn.

## 6. DR/BDR trong mạng multi-access

Trong môi trường multi-access như Ethernet có switch ở giữa, nếu nhiều router đều thiết lập adjacency đầy đủ với nhau thì số quan hệ neighbor và bản tin LSA sẽ tăng nhanh. OSPF dùng DR/BDR để giảm lượng trao đổi: DR l...

| Khái niệm | Ý nghĩa |
| --- | --- |
| DR - Designated Router | Router chủ trong segment multi-access, làm đầu mối trao đổi LSA. |
| BDR - Backup Designated Router | Router dự phòng; nếu DR lỗi thì BDR lên thay. |
| DROTHER | Các router còn lại, không phải DR/BDR. |
| Priority | Giá trị ưu tiên trên interface. Cao hơn thì ưu tiên làm DR/BDR. Priority = 0 thì không được bầu. |
| Router ID | Nếu priority bằng nhau, router ID cao hơn được ưu tiên. |

## 7. Loopback interface

Loopback là interface ảo trên router. Nó không phụ thuộc vào một cổng vật lý cụ thể, nên thường dùng để định danh router hoặc giả lập một mạng/host để test định tuyến.

Trong bài, thầy dùng loopback để giả lập một mạng đích hoặc một gateway bên ngoài thay vì phải kéo thêm router/PC mới. Khi định tuyến đúng, router khác có thể ping đến địa chỉ loopback này.

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
| Tên video | Buổi 34 |
| URL | https://www.youtube.com/watch?v=o0rkx-yeZ6Y |
| Chủ đề chính | OSPF nâng cao: point-to-point, passive-interface, DR/BDR, metric/cost, loopback và default-information originate |
| Mục tiêu | Biết tối ưu cấu hình OSPF, giảm gói tin thừa, kiểm tra neighbor/route và triển khai default route qua OSPF. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | OSPF Advanced |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. OSPF Advanced giải quyết vấn đề gì trong mạng?
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
| OSPF | Giao thức định tuyến động | Link-state routing protocol dùng area và cost. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 OSPF Advanced nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

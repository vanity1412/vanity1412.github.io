---
layout: page-toc
title: "Buổi 32: Floating Static Route"
permalink: /writeups/ccna-theory/buoi-32-static-route-floating-route/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Floating Static Route

## Mục tiêu học tập

- Nắm vai trò của Floating Static Route trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Tài liệu học tập CCNA - biên soạn từ transcript bài giảng

Sơ đồ tổng quan: đường chính và đường dự phòng bằng Floating Static Route

| Nguồn video | https://www.youtube.com/watch?v=Sy7D3xMMOQw |
| --- | --- |
| Chủ đề | Static route, default route, floating static route, AD, IPv4/IPv6 |
| Mục tiêu | Hiểu cách router chọn đường, cấu hình tuyến dự phòng và kiểm tra bảng định tuyến |
| Ghi chú Glasp | Đã tìm Glasp nhưng không thấy highlight trực tiếp phù hợp cho video này |

## 2. Ôn lại 3 kiểu static route

Trong buổi này, thầy nhắc lại rằng static route có thể gõ theo nhiều cách. Cách nào cũng nhằm mục tiêu là giúp router biết phải đưa gói tin ra đâu khi muốn đến một mạng đích nhất định.

Ba kiểu khai báo static route: next-hop, exit-interface và fully specified

## 3. Next-hop static route

Next-hop là địa chỉ IP của router kế tiếp, thường là địa chỉ nằm đối diện với router hiện tại trên đường kết nối giữa hai router.

## 4. Exit-interface static route

Exit-interface là cổng mà router sẽ dùng để đẩy gói tin ra ngoài. Cách này dễ hình dung trong đường point-to-point, nhưng trên Ethernet có thể gây nhập nhằng nếu không chỉ rõ next-hop.

## 5. Fully specified static route

Fully specified route ghi cả exit-interface và next-hop. Cách này rõ ràng hơn, đặc biệt hữu ích với IPv6 khi next-hop là link-local address.

## 6. Administrative Distance và Floating Static Route

Administrative Distance (AD) là độ tin cậy/độ ưu tiên của nguồn tuyến đường. Trên Cisco, static route mặc định có AD = 1. Route nào có AD thấp hơn sẽ được ưu tiên đưa vào bảng định tuyến.

AD quyết định route nào được ưu tiên nếu nhiều route cùng đến một đích

Floating static route làm đường dự phòng khi primary route bị down

## 7. Cấu hình floating static route IPv4

Trong demo, R1 có một đường chính đi qua R2 và một đường dự phòng đi qua R3. Đường dự phòng được gõ thêm số AD cao hơn, ví dụ 5.

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

| Nguồn video | https://www.youtube.com/watch?v=Sy7D3xMMOQw |
| --- | --- |
| Chủ đề | Static route, default route, floating static route, AD, IPv4/IPv6 |
| Mục tiêu | Hiểu cách router chọn đường, cấu hình tuyến dự phòng và kiểm tra bảng định tuyến |
| Ghi chú Glasp | Đã tìm Glasp nhưng không thấy highlight trực tiếp phù hợp cho video này |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Floating Static Route |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Floating Static Route giải quyết vấn đề gì trong mạng?
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
| Floating Static Route | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Floating Static Route nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

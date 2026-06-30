---
layout: page-toc
title: "Buổi 18: VLAN và Trunk"
permalink: /writeups/ccna-theory/buoi-18-switching-vlan-trunk/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# VLAN và Trunk

## Mục tiêu học tập

- Nắm vai trò của VLAN và Trunk trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Ghi chú học tập CCNA – Kỳ 2: Switching, Routing & Wireless

| Thông tin | Nội dung |
| --- | --- |
| Title | Buổi 18 |
| URL | https://www.youtube.com/watch?v=cJ03XmYIMQo |
| Chủ đề | Switching, MAC/CAM table, collision/broadcast domain, VLAN, access port, trunk port |

## 2. Tổng quan buổi học

Buổi học mở đầu nội dung kỳ 2 của chương trình CCNA, tập trung vào ba nhóm kiến thức chính: switching, routing và wireless. Trong buổi này, trọng tâm đặt vào switching trong mạng LAN và cách switch xử lý frame.

Switching là quá trình thiết bị switch nhận frame từ một cổng vào, xác định nơi cần gửi tiếp và forward frame ra cổng phù hợp.

Routing sẽ được học ở phần sau, chủ yếu là định tuyến tĩnh trong giai đoạn đầu.

Wireless sẽ đi vào các mô hình mạng không dây và nguyên lý vận hành cơ bản.

Buổi 18 đặt nền móng cho VLAN, trunk và cách tổ chức mạng LAN trong môi trường doanh nghiệp.

Kỳ 1 giúp nắm TCP/IP, địa chỉ IP và giao thức nền. Sang kỳ 2, người học bắt đầu đi vào cách thiết bị thật trong LAN hoạt động: switch học địa chỉ, chia VLAN và nối các VLAN qua nhiều switch.

## 3. Switching và frame forwarding

Switching không đơn giản là “nhận frame rồi gửi đại đi”. Switch phải dựa trên cổng nhận frame, địa chỉ MAC đích và bảng MAC/CAM table để quyết định forward frame ra đâu.

| Khái niệm | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| Ingress | Hướng frame đi vào một interface của switch. | Frame từ PC1 đi vào F0/1. |
| Egress | Hướng frame đi ra khỏi một interface. | Switch gửi frame ra F0/2 đến PC2. |
| MAC đích | Thông tin switch dùng để quyết định frame đi đâu. | MAC của PC2 nằm sau port F0/2. |
| Không forward ngược | Switch không gửi frame quay lại đúng port vừa nhận. | Frame vào F0/1 thì không gửi lại F0/1. |

Switch hoạt động chủ yếu ở Layer 2, nên quyết định chuyển tiếp frame dựa trên địa chỉ MAC, không dựa vào IP như router.

## 4. MAC/CAM table: học địa chỉ và chuyển tiếp frame

Mỗi khi switch nhận frame, nó đọc MAC nguồn của frame đó và ghi nhận MAC này đang nằm phía sau port nào. Quá trình này gọi là learning. Sau đó, switch tra MAC đích để quyết định chuyển tiếp frame.

| Tình huống | Hành động của switch | Kết quả |
| --- | --- | --- |
| MAC nguồn chưa có trong bảng | Thêm MAC nguồn + ingress port vào MAC table. | Switch học được vị trí của thiết bị gửi. |
| MAC đích đã có trong bảng | Forward frame đúng port tương ứng. | Known unicast forwarding. |
| MAC đích chưa có trong bảng | Flood frame ra tất cả port còn lại, trừ port nhận vào. | Unknown unicast flooding. |
| Frame broadcast | Flood trong cùng broadcast domain/VLAN. | Tất cả host trong VLAN nhận được. |

## 5. Store-and-forward và cut-through switching

Switch có thể xử lý frame theo hai hướng chính: lưu toàn bộ frame rồi kiểm tra trước khi chuyển tiếp, hoặc đọc đủ phần cần thiết rồi chuyển tiếp ngay để giảm độ trễ.

| Tiêu chí | Store-and-forward | Cut-through |
| --- | --- | --- |
| Cách xử lý | Nhận toàn bộ frame, kiểm tra rồi mới gửi. | Đọc MAC đích xong là chuyển tiếp nhanh. |
| Ưu điểm | Có thể kiểm tra lỗi frame tốt hơn. | Độ trễ thấp, tốc độ chuyển tiếp nhanh. |
| Nhược điểm | Chậm hơn, dùng bộ nhớ nhiều hơn. | Có thể chuyển tiếp cả frame lỗi. |
| Cách nhớ | Kiểm hàng xong mới giao. | Thấy địa chỉ là chuyển liền. |

## 6. Collision domain và broadcast domain

| Khái niệm | Bản chất | Thiết bị liên quan |
| --- | --- | --- |
| Collision domain | Miền có khả năng xảy ra va chạm khi nhiều thiết bị cùng truyền. | Hub tạo collision domain lớn; switch chia nhỏ theo port. |
| Broadcast domain | Miền mà gói broadcast có thể lan tới tất cả host. | Router/Layer 3 device chia tách broadcast domain. |
| Switch port | Mỗi port switch thường giảm va chạm so với hub. | Mỗi port là một vùng collision riêng. |
| Router port | Mỗi interface router thường là ranh giới broadcast domain. | Broadcast không đi xuyên router mặc định. |

Switch giảm collision domain, nhưng nếu chưa chia VLAN thì toàn bộ các port trong cùng VLAN vẫn thuộc cùng một broadcast domain.

## 7. VLAN là gì và vì sao phải chia VLAN?

Mỗi VLAN có thể xem như một broadcast domain riêng.

Thiết bị trong cùng VLAN có thể giao tiếp Layer 2 với nhau nếu cùng hệ thống kết nối phù hợp.

Thiết bị khác VLAN mặc định bị cách ly, dù có thể đang cắm chung một switch vật lý.

VLAN giúp giảm broadcast, tăng tính tổ chức và tăng an toàn giữa các phòng ban.

| Ví dụ VLAN | Ý nghĩa tổ chức | Lý do nên tách |
| --- | --- | --- |

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
| Title | Buổi 18 |
| URL | https://www.youtube.com/watch?v=cJ03XmYIMQo |
| Chủ đề | Switching, MAC/CAM table, collision/broadcast domain, VLAN, access port, trunk port |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | VLAN và Trunk |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. VLAN và Trunk giải quyết vấn đề gì trong mạng?
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
| VLAN | Mạng LAN ảo | Chia switch thành nhiều broadcast domain logic. |
| Trunk | Liên kết mang nhiều VLAN | Dùng 802.1Q tag để vận chuyển nhiều VLAN qua một link. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 VLAN và Trunk nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

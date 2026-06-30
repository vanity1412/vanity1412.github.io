---
layout: page-toc
title: "Buổi 37: NAT, PAT và WAN"
permalink: /writeups/ccna-theory/buoi-37-nat-pat-wan-concepts/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# NAT, PAT và WAN

## Mục tiêu học tập

- Nắm vai trò của NAT, PAT và WAN trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

NAT/PAT Lab Review & WAN Concepts

URL: https://www.youtube.com/watch?v=USxb7nBoRLw

## 2. ACL trong bài NAT không phải ACL lọc traffic

Trong bài NAT/PAT, ACL standard thường được dùng để chọn nguồn nào được phép dịch địa chỉ. Nó không nhất thiết là ACL gắn trực tiếp vào interface theo chiều in/out để chặn hoặc cho phép traffic.

ip access-list standard R2NAT permit 192.168.10.0 0.0.0.255 permit 192.168.20.0 0.0.0.255 permit 192.168.30.0 0.0.0.255 ! ip nat inside source list R2NAT interface g0/1 overload ! interface g0/0 ip nat inside interfac...

## 3. Lệnh kiểm tra khi NAT/PAT chưa chạy

show ip nat translations show ip nat statistics show running-config | include ip nat|access-list ping <outside-ip> traceroute <outside-ip> clear ip nat translation *

## 4. WAN là gì và vì sao cần WAN?

LAN chỉ phục vụ một khu vực nhỏ như nhà, phòng lab, văn phòng hoặc một tòa nhà. Khi cần nối các LAN ở nhiều vị trí địa lý khác nhau, tổ chức phải dùng WAN. Hạ tầng WAN thường thuộc ISP/carrier, còn doanh nghiệp thuê d...

## 5. Các WAN topology thường gặp

| Topology | Cách hiểu | Khi dùng |
| --- | --- | --- |
| Point-to-point | Hai site nối trực tiếp với nhau. | Dễ hiểu, ổn định nhưng tốn chi phí nếu có nhiều site. |
| Hub-and-spoke | Các chi nhánh đi qua một hub trung tâm. | Phổ biến khi cần tiết kiệm kết nối và quản lý tập trung. |
| Dual-homed | Một site có hai đường/nhà cung cấp để dự phòng. | Tăng tính sẵn sàng, tránh mất kết nối khi một đường hỏng. |
| Full mesh | Site nào cũng nối với site còn lại. | Dự phòng tốt nhưng rất đắt và khó quản trị. |
| Partial mesh | Chỉ một số site quan trọng được nối chéo. | Cân bằng giữa chi phí và khả năng dự phòng. |

## 6. WAN operation: Layer 1, Layer 2 và serial connection

WAN không chỉ là router. Nó bao gồm lớp vật lý truyền dẫn, lớp liên kết dữ liệu, thiết bị chuyển đổi, thiết bị carrier và dịch vụ thuê từ ISP. Trong Packet Tracer, khi dùng serial link, thường cần lưu ý đầu DCE cấp cl...

interface s0/0/0 ip address 192.168.1.1 255.255.255.252 clock rate 64000 ! chỉ cần trên đầu DCE trong lab no shutdown

## 7. Traditional WAN

Các khái niệm truyền thống gồm leased line/dedicated line, PSTN, circuit switching, packet switching cũ như Frame Relay/ATM. Những công nghệ này giúp hiểu lịch sử phát triển WAN nhưng nhiều mô hình hiện nay đã thay bằ...

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

| Topology | Cách hiểu | Khi dùng |
| --- | --- | --- |
| Point-to-point | Hai site nối trực tiếp với nhau. | Dễ hiểu, ổn định nhưng tốn chi phí nếu có nhiều site. |
| Hub-and-spoke | Các chi nhánh đi qua một hub trung tâm. | Phổ biến khi cần tiết kiệm kết nối và quản lý tập trung. |
| Dual-homed | Một site có hai đường/nhà cung cấp để dự phòng. | Tăng tính sẵn sàng, tránh mất kết nối khi một đường hỏng. |
| Full mesh | Site nào cũng nối với site còn lại. | Dự phòng tốt nhưng rất đắt và khó quản trị. |
| Partial mesh | Chỉ một số site quan trọng được nối chéo. | Cân bằng giữa chi phí và khả năng dự phòng. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | NAT, PAT và WAN |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. NAT, PAT và WAN giải quyết vấn đề gì trong mạng?
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
| NAT | Chuyển đổi địa chỉ | Dịch private IP sang public IP khi ra ngoài. |
| PAT | NAT overload | Nhiều host dùng chung một public IP bằng port. |
| WAN | Mạng diện rộng | Kết nối các LAN ở nhiều địa điểm khác nhau. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 NAT, PAT và WAN nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

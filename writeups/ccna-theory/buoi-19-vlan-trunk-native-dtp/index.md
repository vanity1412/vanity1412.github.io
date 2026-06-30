---
layout: page-toc
title: "Buổi 19: Native VLAN và DTP"
permalink: /writeups/ccna-theory/buoi-19-vlan-trunk-native-dtp/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Native VLAN và DTP

## Mục tiêu học tập

- Nắm vai trò của Native VLAN và DTP trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

VLAN nâng cao: Native VLAN, Trunk Allowed VLAN và DTP

Ghi chú học tập CCNA - Switching, Routing & Wireless Essentials

## 2. Ôn lại VLAN từ Buổi 18

VLAN là cách chia một switch vật lý thành nhiều mạng logic nhỏ hơn. Khi chia VLAN, mỗi nhóm port có thể được tách thành một broadcast domain riêng. Điều này giúp giảm broadcast, dễ quản lý người dùng theo phòng ban và...

| Khái niệm | Ý nghĩa | Lệnh/ghi nhớ |
| --- | --- | --- |
| VLAN | Mạng LAN ảo, chia switch thành các miền logic | vlan 2, vlan 3... |
| Access port | Port thuộc một VLAN duy nhất, thường nối PC/printer/server | switchport mode access |
| Trunk port | Port cho nhiều VLAN đi qua cùng một link, thường nối switch-switch | switchport mode trunk |
| VLAN 1 | VLAN mặc định của switch Cisco | Mặc định toàn bộ port nằm ở VLAN 1 |
| show vlan brief | Kiểm tra VLAN và port thuộc VLAN nào | Lệnh cần nhớ khi troubleshoot |

## 3. Default VLAN

Default VLAN là VLAN mặc định có sẵn trên switch. Với switch Cisco, VLAN mặc định thường là VLAN 1. Khi switch mới được bật lên, các port chưa cấu hình gì sẽ thuộc VLAN 1. Đây là lý do khi chạy show vlan brief, ta thấ...

Điểm quan trọng: VLAN 1 là VLAN mặc định nên không xóa được và không đổi tên theo cách thông thường. Trong thiết kế thực tế, không nên dùng VLAN 1 cho traffic quan trọng nếu có thể tách riêng VLAN quản lý.

## 4. Data VLAN

Data VLAN là VLAN dành cho dữ liệu người dùng thông thường như truy cập web, gửi email, sử dụng phần mềm nội bộ hoặc truyền file. Ví dụ: VLAN 10 cho sinh viên, VLAN 20 cho giáo viên, VLAN 30 cho phòng tài vụ.

## 5. Management VLAN

Management VLAN là VLAN dùng để quản trị thiết bị mạng. Các địa chỉ IP quản trị của switch/router, SSH hoặc Telnet quản trị từ xa nên được đặt trong VLAN riêng. Cách này giúp người dùng thông thường không truy cập trự...

## 6. Voice VLAN

Voice VLAN dành cho thoại/video, tức traffic cần độ trễ thấp và ổn định. Trong thực tế, hệ thống IP Phone, video call hoặc livestream nội bộ có thể cần VLAN riêng để dễ áp dụng ưu tiên QoS.

VLAN không chỉ là câu lệnh chia port. VLAN là tư duy phân vùng mạng theo mục đích sử dụng: người dùng, quản trị, thoại, server hoặc phòng ban.

## 7. Trunk link và VLAN Tagging

Khi một switch có nhiều VLAN và muốn các VLAN đó kéo dài sang switch khác, ta không thể dùng một sợi dây riêng cho mỗi VLAN nếu số VLAN lớn. Vì vậy cần trunk link. Trunk là đường kết nối cho phép nhiều VLAN đi qua cùn...

Vấn đề đặt ra là: nếu nhiều VLAN cùng đi chung một đường, làm sao switch bên kia biết frame này thuộc VLAN 2 hay VLAN 3? Câu trả lời là VLAN tag. Khi frame đi vào trunk, switch gắn thêm VLAN ID để đánh dấu frame thuộc...

| Trường hợp | Switch xử lý thế nào | Kết quả |
| --- | --- | --- |
| Frame từ VLAN 2 đi vào trunk | Gắn tag VLAN ID = 2 | Switch bên kia trả frame về đúng VLAN 2 |
| Frame từ VLAN 3 đi vào trunk | Gắn tag VLAN ID = 3 | Switch bên kia trả frame về đúng VLAN 3 |
| Frame đi ra access port | Gỡ tag trước khi gửi đến PC | PC không cần biết VLAN tag |

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

| Khái niệm | Ý nghĩa | Lệnh/ghi nhớ |
| --- | --- | --- |
| VLAN | Mạng LAN ảo, chia switch thành các miền logic | vlan 2, vlan 3... |
| Access port | Port thuộc một VLAN duy nhất, thường nối PC/printer/server | switchport mode access |
| Trunk port | Port cho nhiều VLAN đi qua cùng một link, thường nối switch-switch | switchport mode trunk |
| VLAN 1 | VLAN mặc định của switch Cisco | Mặc định toàn bộ port nằm ở VLAN 1 |
| show vlan brief | Kiểm tra VLAN và port thuộc VLAN nào | Lệnh cần nhớ khi troubleshoot |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Native VLAN và DTP |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Native VLAN và DTP giải quyết vấn đề gì trong mạng?
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
| VLAN | Mạng LAN ảo | Chia switch thành nhiều broadcast domain logic. |
| Trunk | Liên kết mang nhiều VLAN | Dùng 802.1Q tag để vận chuyển nhiều VLAN qua một link. |
| NAT | Chuyển đổi địa chỉ | Dịch private IP sang public IP khi ra ngoài. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Native VLAN và DTP nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

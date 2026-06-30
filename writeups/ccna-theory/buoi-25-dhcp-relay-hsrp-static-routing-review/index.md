---
layout: page-toc
title: "Buổi 25: DHCP Relay, HSRP và Static Routing"
permalink: /writeups/ccna-theory/buoi-25-dhcp-relay-hsrp-static-routing-review/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# DHCP Relay, HSRP và Static Routing

## Mục tiêu học tập

- Nắm vai trò của DHCP Relay, HSRP và Static Routing trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

DHCP cùng mạng/khác mạng, Packet Tracer 7.4.1, ip helper-address, FHRP/HSRP và định tuyến tĩnh

| Thông tin bài học | Thông tin bài học |
| --- | --- |
| Tiêu đề video | Buổi 25 |
| URL | https://www.youtube.com/watch?v=sE7bp1kT7Yo |
| Chủ đề | DHCP Relay, Packet Tracer DHCPv4, FHRP/HSRP recap, static route |
| Mục tiêu | Nắm được cách cấp IP tự động trong cùng LAN, khác LAN và cách xử lý lab khi thiếu route. |

nhanh: DHCP trong cùng LAN có thể broadcast trực tiếp. DHCP ở mạng khác cần router chuyển tiếp bằng ip helper-address. Với FHRP/HSRP, PC trỏ default gateway về virtual IP thay vì IP thật của từng router.

## 2. DHCP Discover và Offer hoạt động như thế nào?

Trong phần đầu buổi học, giảng viên nhắc lại một chi tiết dễ nhầm: client ban đầu chưa có IP nên nó dùng DHCP Discover dạng broadcast để tìm DHCP Server. Tuy nhiên, khi server phản hồi, server có thể dựa vào thông tin...

| Bản tin | Ý nghĩa | Ghi chú dễ nhớ |
| --- | --- | --- |
| DHCP Discover | Client phát broadcast để hỏi “ai là DHCP Server?” | Dùng khi client chưa có IP hợp lệ. |
| DHCP Offer | Server đề nghị một địa chỉ IP và thông số mạng. | Offer chứa IP, subnet mask, gateway, DNS, lease time. |
| DHCP Request | Client chấp nhận và yêu cầu dùng địa chỉ IP được đề nghị. | Nếu có nhiều DHCP Server, client chọn một offer. |
| DHCP ACK | Server xác nhận cấp phát thành công. | Sau ACK, client dùng IP trong thời gian lease. |

## 3. Bốn tình huống DHCP cần phân biệt

DHCP cùng mạng LAN: client và server ở cùng broadcast domain nên gói Discover có thể tới server trực tiếp.

DHCP khác mạng LAN: broadcast không đi qua router, vì vậy phải có DHCP Relay hoặc lệnh ip helper-address.

Một DHCP Server cấp cho nhiều LAN/VLAN: server phải có nhiều pool, mỗi pool đúng với network/default gateway/DNS của từng LAN.

Trong lab nhỏ: router, switch Layer 3 hoặc firewall cũng có thể đóng vai trò DHCP Server để cấp IP tự động.

## 4. Hiểu đúng các thông số trong DHCP Pool

Một điểm quan trọng trong buổi học là không được nhầm default gateway trong DHCP pool với gateway của chính DHCP Server. Thông số trong pool là thông số mà server sẽ cấp cho client thuộc subnet đó.

| Thông số | Ý nghĩa đúng | Lỗi hay gặp |
| --- | --- | --- |
| Pool Name | Tên nhóm cấp phát, ví dụ R1_LAN, R3_LAN, VLAN2. | Đặt tên lung tung khiến khó quản lý khi có nhiều pool. |
| Network | Dải mạng mà pool cấp phát, ví dụ 192.168.10.0/24. | Khai báo sai network hoặc subnet mask làm client nhận sai dải. |
| Default Router | Gateway của client trong LAN đó. | Nhầm với gateway của DHCP Server. |
| DNS Server | DNS mà client sẽ dùng. | Bỏ trống khiến client có IP nhưng khó phân giải tên miền. |
| Start IP / Excluded Address | Khoảng IP cấp phát hoặc các IP không cấp động. | Không loại trừ IP router/server dẫn đến xung đột địa chỉ. |

## 5. Lab Packet Tracer 7.4.1 - DHCP Server và DHCP Relay

Bài lab trong transcript tập trung vào mô hình R2 làm DHCP Server cho các LAN phía R1 và R3. Vì client ở các mạng khác R2, R1/R3 phải cấu hình DHCP Relay bằng ip helper-address.

## 6. R2 cũng có thể làm DHCP Client

Trong bài lab, một interface của R2 được cấu hình để nhận IP bằng DHCP. Khi đó interface cần lệnh ip address dhcp và no shutdown.

## 7. Checklist xử lý lỗi DHCP trong Packet Tracer

| Triệu chứng | Nguyên nhân thường gặp | Cách kiểm tra/sửa |
| --- | --- | --- |
| PC không nhận IP | Chưa bật DHCP trên PC hoặc pool chưa đúng. | Vào Desktop > IP Configuration > DHCP; kiểm tra ip dhcp pool. |
| PC nhận sai dải | Pool network/default-router khai báo sai. | So sánh network, mask, default-router với bảng địa chỉ. |
| PC khác LAN không nhận IP | Thiếu ip helper-address trên router gần client. | Cấu hình ip helper-address trên interface LAN của R1/R3. |
| Có IP nhưng ping không qua mạng khác | Thiếu route hoặc default route. | show ip route; thêm static route hoặc định tuyến động. |
| DNS không hoạt động | DNS server không được cấp hoặc DNS sai. | Kiểm tra trường dns-server trong DHCP pool. |

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

| Thông tin bài học | Thông tin bài học |
| --- | --- |
| Tiêu đề video | Buổi 25 |
| URL | https://www.youtube.com/watch?v=sE7bp1kT7Yo |
| Chủ đề | DHCP Relay, Packet Tracer DHCPv4, FHRP/HSRP recap, static route |
| Mục tiêu | Nắm được cách cấp IP tự động trong cùng LAN, khác LAN và cách xử lý lab khi thiếu route. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | DHCP Relay, HSRP và Static Routing |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. DHCP Relay, HSRP và Static Routing giải quyết vấn đề gì trong mạng?
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
| DHCP | Cấp phát IP tự động | Cấp IP, subnet mask, gateway và DNS cho host. |
| HSRP | Dự phòng gateway | Tạo virtual gateway để tăng tính sẵn sàng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 DHCP Relay, HSRP và Static Routing nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

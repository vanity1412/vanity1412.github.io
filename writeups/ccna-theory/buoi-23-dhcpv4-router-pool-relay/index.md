---
layout: page-toc
title: "Buổi 23: DHCPv4"
permalink: /writeups/ccna-theory/buoi-23-dhcpv4-router-pool-relay/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# DHCPv4

## Mục tiêu học tập

- Nắm vai trò của DHCPv4 trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

DORA, DHCP Pool trên Router, DHCP theo VLAN, Router-on-a-Stick và ip helper-address

| Thông tin bài học | Thông tin bài học |
| --- | --- |
| Nguồn | https://www.youtube.com/watch?v=Vk3UrtopJv0 |
| Chủ đề chính | DHCPv4, cơ chế cấp phát IP tự động, DHCP pool trên router, DHCP theo VLAN, DHCP Relay và ip helper-address. |
| Mục tiêu | Hiểu DORA, biết cấu hình DHCP trên router, biết vì sao DHCP request không tự đi qua router và biết dùng helper để trỏ về DHCP server tập trung. |
| Ghi chú Glasp | Đã tìm kiếm Glasp theo các từ khóa liên quan DHCPv4, Cisco Packet Tracer, DHCP Relay, ip helper-address nhưng không tìm thấy insight trực tiếp phù hợp để bổ sung. |

## 2. DHCP là gì và vì sao cần dùng?

DHCP (Dynamic Host Configuration Protocol) là giao thức cho phép thiết bị trong mạng tự động nhận các thông số cấu hình IP. Trong thực tế, nếu một lớp học, văn phòng hoặc doanh nghiệp có hàng chục đến hàng trăm máy, v...

| Thông tin DHCP thường cấp | Ý nghĩa |
| --- | --- |
| IP Address | Địa chỉ IP client sẽ sử dụng trong mạng. |
| Subnet Mask | Xác định phạm vi mạng con. |
| Default Gateway | Địa chỉ router để đi ra mạng khác/Internet. |
| DNS Server | Máy chủ phân giải tên miền. |
| Domain Name | Tên miền nội bộ hoặc domain tổ chức. |
| Lease Time | Thời gian client được thuê địa chỉ IP. |

## 3. Quy trình DHCP DORA

| Bước | Bản tin | Hướng truyền | Giải thích |
| --- | --- | --- | --- |
| 1 | DHCP Discover | Client → Broadcast | Client chưa có IP nên phát broadcast để tìm DHCP server. |
| 2 | DHCP Offer | Server → Client | Server đề nghị một địa chỉ IP và thông số cấu hình. |
| 3 | DHCP Request | Client → Server/Broadcast | Client yêu cầu sử dụng địa chỉ IP được đề nghị. |
| 4 | DHCP ACK | Server → Client | Server xác nhận client được dùng IP trong thời gian lease. |

DORA là trình tự nền tảng nhất của DHCP. Khi troubleshoot lỗi “PC không nhận IP”, cần nghĩ đến việc bản tin Discover có đi tới DHCP server được không và ACK có quay lại client được không.

## 4. Cấu hình DHCP pool trên Router Cisco

Trong bài giảng, giảng viên nhấn mạnh router có thể đóng vai trò DHCP server. Khi đó, ta tạo pool cho từng mạng/VLAN, khai báo dải network, default gateway, DNS server và domain name.

| Lệnh | Vai trò |
| --- | --- |
| ip dhcp pool <TEN_POOL> | Tạo pool DHCP. |
| network <network> <mask> | Khai báo dải IP mà pool sẽ cấp. |
| default-router <ip> | Cấp default gateway cho client. |
| dns-server <ip> | Cấp DNS server cho client. |
| domain-name <domain> | Cấp domain name cho client. |
| no ip dhcp pool <TEN_POOL> | Xóa pool DHCP khi muốn bỏ cấu hình cũ. |

## 5. DHCP trong mô hình Router-on-a-Stick

Với nhiều VLAN, router thường dùng subinterface để làm gateway cho từng VLAN. Trên switch, cổng nối lên router phải là trunk để mang nhiều VLAN. Trên router, mỗi subinterface cần encapsulation dot1q và IP gateway tươn...

## 6. DHCP theo VLAN trong bài lab mở rộng

Giảng viên mở rộng từ bài VLAN/Inter-VLAN trước đó: thay vì đặt nhiều DHCP server riêng cho từng VLAN, có thể xóa các server DHCP rời và cấu hình DHCP pool tập trung trên router. Cách này giúp bài lab gọn hơn và sát t...

| VLAN | Dải IP minh họa | Gateway/Default Router | DHCP Pool |
| --- | --- | --- | --- |
| VLAN 2 | 192.168.1.0/24 | 192.168.1.1 | VLAN2 |
| VLAN 3 | 10.0.0.0/24 | 10.0.0.1 | VLAN3 |
| VLAN 4 | 172.16.1.0/24 | 172.16.1.1 | VLAN4 |

## 7. DHCP Server tập trung và ip helper-address

Kịch bản cuối buổi là đưa DHCP server ra một mạng riêng, ví dụ 10.0.0.254. Khi client ở VLAN 1 hoặc VLAN 2 gửi DHCP Discover, bản tin này là broadcast. Router mặc định không chuyển broadcast sang mạng khác, nên client...

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
| Nguồn | https://www.youtube.com/watch?v=Vk3UrtopJv0 |
| Chủ đề chính | DHCPv4, cơ chế cấp phát IP tự động, DHCP pool trên router, DHCP theo VLAN, DHCP Relay và ip helper-address. |
| Mục tiêu | Hiểu DORA, biết cấu hình DHCP trên router, biết vì sao DHCP request không tự đi qua router và biết dùng helper để trỏ về DHCP server tập trung. |
| Ghi chú Glasp | Đã tìm kiếm Glasp theo các từ khóa liên quan DHCPv4, Cisco Packet Tracer, DHCP Relay, ip helper-address nhưng không tìm thấy insight trực tiếp phù hợp để bổ sung. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | DHCPv4 |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. DHCPv4 giải quyết vấn đề gì trong mạng?
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
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 DHCPv4 nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

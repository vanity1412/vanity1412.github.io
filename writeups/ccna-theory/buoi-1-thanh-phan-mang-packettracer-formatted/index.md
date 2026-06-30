---
layout: page-toc
title: "Buổi 1: Thành phần mạng và Packet Tracer"
permalink: /writeups/ccna-theory/buoi-1-thanh-phan-mang-packettracer-formatted/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Thành phần mạng và Packet Tracer

## Mục tiêu học tập

- Nắm vai trò của Thành phần mạng và Packet Tracer trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Hiểu mạng máy tính là gì và vì sao mạng quan trọng trong học tập, làm việc, liên lạc.

Nhận biết 4 thành phần chính của mạng: thiết bị đầu cuối, thiết bị trung gian, môi trường truyền dẫn và giao thức.

Biết dùng Cisco Packet Tracer ở mức cơ bản: kéo thả thiết bị, nối dây, ghi chú, đặt IP và quan sát gói tin.

Phân biệt vai trò của Switch, Hub, Router và Default Gateway.

Biết kiểm tra truyền tin cùng mạng/khác mạng bằng Simulation Mode và sửa các lỗi cơ bản.

## 2. Bốn thành phần của mạng máy tính

Một mạng máy tính không chỉ gồm máy tính và dây cáp. Để thiết bị có thể trao đổi dữ liệu, mạng cần có thiết bị gửi/nhận, thiết bị chuyển tiếp, môi trường truyền dẫn và bộ quy tắc giao tiếp chung.

| Thành phần | Nghĩa dễ hiểu | Ví dụ | Cần nhớ |
| --- | --- | --- | --- |
| End Device / Host | Nơi dữ liệu bắt đầu hoặc kết thúc. | PC, laptop, server, smartphone, printer. | Thường có địa chỉ IP. |
| Intermediary Device | Thiết bị điều phối/chuyển tiếp dữ liệu. | Switch, router, hub, firewall. | Giúp dữ liệu đi đúng hướng. |
| Network Media | Con đường để tín hiệu đi qua. | Cáp đồng, cáp quang, Wi-Fi, 4G/5G. | Chọn sai media có thể làm link không hoạt động. |
| Protocol | Luật/ngôn ngữ chung để thiết bị hiểu nhau. | TCP/IP, HTTP, DNS, ICMP. | Không có protocol thì thiết bị không giao tiếp được. |

## 3. Làm quen Cisco Packet Tracer

Cisco Packet Tracer là phòng lab ảo cho người học mạng. Thay vì mua router, switch và dây mạng thật, sinh viên có thể mô phỏng thiết bị, cấu hình IP và kiểm tra truyền dữ liệu ngay trên máy tính.

| Việc cần làm | Thao tác trong Packet Tracer | Lưu ý |
| --- | --- | --- |
| Bật hiển thị tên/cổng | Options -> Preferences -> Show Device Name, Always Show Port Labels | Giúp tránh nhầm cổng khi nối dây. |
| Kéo thả thiết bị | End Devices, Network Devices, Connections | Buổi này dùng PC, Laptop, Server, Switch 2960, Router 2911, Hub, WRT300N. |
| Kết nối thiết bị | Connections -> Automatically Choose Connection Type | Người mới nên để phần mềm tự chọn dây. |
| Ghi chú mô hình | Dùng công cụ Note | Nên ghi network, IP router, gateway. |
| Quan sát gói tin | Simulation Mode | Dễ hiểu đường đi của packet/frame. |

## 4. Cấu hình IP và Default Gateway

Địa chỉ IP là địa chỉ logic dùng để định danh thiết bị trong mạng. Nếu thiết bị muốn giao tiếp với mạng khác, nó cần Default Gateway - thường là IP của router trong cùng mạng.

| Thiết bị/Mạng | Địa chỉ ví dụ | Gateway ví dụ | Ý nghĩa |
| --- | --- | --- | --- |
| PC/Laptop/Server LAN trái | 192.168.1.2/24 - 192.168.1.x/24 | 192.168.1.1 | Các host cùng mạng gửi trực tiếp qua switch. |
| Router cổng LAN trái | 192.168.1.1/24 | Không cần | Làm gateway cho LAN trái. |
| PC LAN dưới | 172.16.1.2/24 | 172.16.1.1 | Muốn trả lời sang LAN khác phải có gateway. |
| Router cổng LAN dưới | 172.16.1.1/24 | Không cần | Làm gateway cho LAN dưới. |

Cùng mạng có thể truyền qua switch. Khác mạng phải đi qua router, vì vậy cả hai phía đều cần gateway đúng nếu muốn truyền thông hai chiều.

## 5. Truyền tin cùng mạng và khác mạng

| Tiêu chí | Cùng mạng | Khác mạng |
| --- | --- | --- |
| Ví dụ | PC0 -> Laptop0 cùng 192.168.1.0/24 | PC0 192.168.1.0/24 -> PC1 172.16.1.0/24 |
| Có cần router? | Không | Có |
| Có cần Default Gateway? | Không bắt buộc | Có |
| Đường đi | PC0 -> Switch -> Laptop0 | PC0 -> Switch -> Router -> Hub/Switch -> PC1 |
| Lỗi hay gặp | Sai IP/subnet trong cùng LAN | Thiếu gateway hoặc router interface chưa bật |

## 6. Switch, Hub và Router khác nhau như thế nào?

| Thiết bị | Vai trò chính | Cách hoạt động | Mẹo nhớ |
| --- | --- | --- | --- |
| Switch | Kết nối thiết bị trong cùng LAN. | Học MAC address và gửi frame đúng cổng đích. | Gửi đúng người, đúng cổng. |
| Hub | Kết nối thiết bị ở mức rất cơ bản. | Nhận tín hiệu rồi phát ra nhiều cổng. | Phát loa cho tất cả. |
| Router | Kết nối các mạng khác nhau. | Dựa vào IP/bảng định tuyến để chuyển packet sang mạng khác. | Dẫn đường giữa các khu vực. |

## 7. Quy trình thực hành Packet Tracer chuẩn

Bước 1: Mở Packet Tracer và bật hiển thị tên thiết bị/tên cổng.

Bước 2: Kéo thiết bị: PC, laptop, server, switch 2960, router 2911, hub, wireless router WRT300N.

Bước 3: Kết nối bằng Connections, người mới dùng Automatically Choose Connection Type.

Bước 4: Dùng Note ghi network, IP router, gateway lên sơ đồ.

Bước 5: Đặt IP/subnet mask cho PC, laptop, server.

Bước 6: Đặt IP cho từng interface router và bật On/no shutdown.

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

| Thành phần | Nghĩa dễ hiểu | Ví dụ | Cần nhớ |
| --- | --- | --- | --- |
| End Device / Host | Nơi dữ liệu bắt đầu hoặc kết thúc. | PC, laptop, server, smartphone, printer. | Thường có địa chỉ IP. |
| Intermediary Device | Thiết bị điều phối/chuyển tiếp dữ liệu. | Switch, router, hub, firewall. | Giúp dữ liệu đi đúng hướng. |
| Network Media | Con đường để tín hiệu đi qua. | Cáp đồng, cáp quang, Wi-Fi, 4G/5G. | Chọn sai media có thể làm link không hoạt động. |
| Protocol | Luật/ngôn ngữ chung để thiết bị hiểu nhau. | TCP/IP, HTTP, DNS, ICMP. | Không có protocol thì thiết bị không giao tiếp được. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Thành phần mạng và Packet Tracer |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Thành phần mạng và Packet Tracer giải quyết vấn đề gì trong mạng?
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
| Packet Tracer | Trình mô phỏng mạng | Dùng để dựng topology, cấu hình và kiểm tra lab CCNA. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Thành phần mạng và Packet Tracer nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

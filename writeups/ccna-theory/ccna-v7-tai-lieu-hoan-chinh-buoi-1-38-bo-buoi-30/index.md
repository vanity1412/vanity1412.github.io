---
layout: page-toc
title: "CCNA v7: Tài liệu buổi 1-38"
permalink: /writeups/ccna-theory/ccna-v7-tai-lieu-hoan-chinh-buoi-1-38-bo-buoi-30/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# CCNA v7 - Tài liệu buổi 1-38

## Mục tiêu học tập

- Nắm vai trò của CCNA v7 - Tài liệu buổi 1-38 trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. CCNA v7 Tai lieu hoan chinh Buoi 1 38 bo Buoi 30

TÀI LIỆU HỌC TẬP CCNA v7

Bản tổng hợp từ Buổi 1 đến Buổi 38, không bao gồm Buổi 30

Lộ trình nội dung

## 2. Phần 4 - Switching nâng cao: VLAN, trunk, Inter-VLAN routing, STP và EtherChannel.

Phần 5 - Dịch vụ mạng và bảo mật LAN: DHCP, HSRP/FHRP, AAA, 802.1X, port security, wireless.

Phần 6 - Routing và dịch vụ biên: static route, floating route, OSPF, ACL, NAT/PAT, WAN và final project.

## 3. Mục lục tổng quan

| Buổi | Chủ đề | File nguồn |
| --- | --- | --- |
| 1 | Thanh Phan Mang PacketTracer Formatted | BUỔI 1_Thanh_Phan_Mang_PacketTracer_Formatted.docx |
| 2 | Cisco IOS | BUỔI 2_Cisco_IOS.docx |
| 3 | Giao thuc va Mo hinh mang | BUỔI 3_Giao_thuc_va_Mo_hinh_mang.docx |
| 4 | Wireshark OSI | BUỔI 4_Wireshark_OSI.docx |
| 5 | Physical layer | BUỔI 5 - Physical_layer.docx |
| 6 | HỆ CƠ SỐ, PACKET TRACER VÀ WIRESHARK ICMP | BUỔI 6_HỆ CƠ SỐ, PACKET TRACER VÀ WIRESHARK ICMP.docx |
| 7 | Data Link Ethernet Switching Tai lieu hoc tap | BUỔI 7_Data_Link_Ethernet_Switching_Tai_lieu_hoc_tap.docx |
| 8 | Switch MAC ARP SSH | BUỔI 8_Switch_MAC_ARP_SSH.docx |

## 4. Bốn thành phần của mạng máy tính

Một mạng máy tính không chỉ gồm máy tính và dây cáp. Để thiết bị có thể trao đổi dữ liệu, mạng cần có thiết bị gửi/nhận, thiết bị chuyển tiếp, môi trường truyền dẫn và bộ quy tắc giao tiếp chung.

| Thành phần | Nghĩa dễ hiểu | Ví dụ | Cần nhớ |
| --- | --- | --- | --- |
| End Device / Host | Nơi dữ liệu bắt đầu hoặc kết thúc. | PC, laptop, server, smartphone, printer. | Thường có địa chỉ IP. |
| Intermediary Device | Thiết bị điều phối/chuyển tiếp dữ liệu. | Switch, router, hub, firewall. | Giúp dữ liệu đi đúng hướng. |
| Network Media | Con đường để tín hiệu đi qua. | Cáp đồng, cáp quang, Wi-Fi, 4G/5G. | Chọn sai media có thể làm link không hoạt động. |
| Protocol | Luật/ngôn ngữ chung để thiết bị hiểu nhau. | TCP/IP, HTTP, DNS, ICMP. | Không có protocol thì thiết bị không giao tiếp được. |

## 5. Làm quen Cisco Packet Tracer

Cisco Packet Tracer là phòng lab ảo cho người học mạng. Thay vì mua router, switch và dây mạng thật, sinh viên có thể mô phỏng thiết bị, cấu hình IP và kiểm tra truyền dữ liệu ngay trên máy tính.

| Việc cần làm | Thao tác trong Packet Tracer | Lưu ý |
| --- | --- | --- |
| Bật hiển thị tên/cổng | Options -> Preferences -> Show Device Name, Always Show Port Labels | Giúp tránh nhầm cổng khi nối dây. |
| Kéo thả thiết bị | End Devices, Network Devices, Connections | Buổi này dùng PC, Laptop, Server, Switch 2960, Router 2911, Hub, WRT300N. |
| Kết nối thiết bị | Connections -> Automatically Choose Connection Type | Người mới nên để phần mềm tự chọn dây. |
| Ghi chú mô hình | Dùng công cụ Note | Nên ghi network, IP router, gateway. |
| Quan sát gói tin | Simulation Mode | Dễ hiểu đường đi của packet/frame. |

## 6. Cấu hình IP và Default Gateway

Địa chỉ IP là địa chỉ logic dùng để định danh thiết bị trong mạng. Nếu thiết bị muốn giao tiếp với mạng khác, nó cần Default Gateway - thường là IP của router trong cùng mạng.

| Thiết bị/Mạng | Địa chỉ ví dụ | Gateway ví dụ | Ý nghĩa |
| --- | --- | --- | --- |
| PC/Laptop/Server LAN trái | 192.168.1.2/24 - 192.168.1.x/24 | 192.168.1.1 | Các host cùng mạng gửi trực tiếp qua switch. |
| Router cổng LAN trái | 192.168.1.1/24 | Không cần | Làm gateway cho LAN trái. |
| PC LAN dưới | 172.16.1.2/24 | 172.16.1.1 | Muốn trả lời sang LAN khác phải có gateway. |
| Router cổng LAN dưới | 172.16.1.1/24 | Không cần | Làm gateway cho LAN dưới. |

Cùng mạng có thể truyền qua switch. Khác mạng phải đi qua router, vì vậy cả hai phía đều cần gateway đúng nếu muốn truyền thông hai chiều.

## 7. Truyền tin cùng mạng và khác mạng

| Tiêu chí | Cùng mạng | Khác mạng |
| --- | --- | --- |
| Ví dụ | PC0 -> Laptop0 cùng 192.168.1.0/24 | PC0 192.168.1.0/24 -> PC1 172.16.1.0/24 |
| Có cần router? | Không | Có |
| Có cần Default Gateway? | Không bắt buộc | Có |
| Đường đi | PC0 -> Switch -> Laptop0 | PC0 -> Switch -> Router -> Hub/Switch -> PC1 |
| Lỗi hay gặp | Sai IP/subnet trong cùng LAN | Thiếu gateway hoặc router interface chưa bật |

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

| Buổi | Chủ đề | File nguồn |
| --- | --- | --- |
| 1 | Thanh Phan Mang PacketTracer Formatted | BUỔI 1_Thanh_Phan_Mang_PacketTracer_Formatted.docx |
| 2 | Cisco IOS | BUỔI 2_Cisco_IOS.docx |
| 3 | Giao thuc va Mo hinh mang | BUỔI 3_Giao_thuc_va_Mo_hinh_mang.docx |
| 4 | Wireshark OSI | BUỔI 4_Wireshark_OSI.docx |
| 5 | Physical layer | BUỔI 5 - Physical_layer.docx |
| 6 | HỆ CƠ SỐ, PACKET TRACER VÀ WIRESHARK ICMP | BUỔI 6_HỆ CƠ SỐ, PACKET TRACER VÀ WIRESHARK ICMP.docx |
| 7 | Data Link Ethernet Switching Tai lieu hoc tap | BUỔI 7_Data_Link_Ethernet_Switching_Tai_lieu_hoc_tap.docx |
| 8 | Switch MAC ARP SSH | BUỔI 8_Switch_MAC_ARP_SSH.docx |
| 9 | Network Layer Routing | BUỔI 9_Network_Layer_Routing.docx |
| 10 | Phan Giai Dia Chi ARP NDP | BUỔI 10_Phan_Giai_Dia_Chi_ARP_NDP.docx |
| 11 | IPv4 Subnetting | Buổi 11_IPv4_Subnetting.docx |
| 12 | VLSM Chia Mang Theo Nhu Cau | BUỔI 12_VLSM_Chia_Mang_Theo_Nhu_Cau.docx |
| 13 | IPv6 | BUỔI 13_IPv6.docx |
| 14 | ICMP Ping Traceroute | BUỔI 14_ICMP_Ping_Traceroute.docx |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | CCNA v7 - Tài liệu buổi 1-38 |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. CCNA v7 - Tài liệu buổi 1-38 giải quyết vấn đề gì trong mạng?
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
| CCNA v7 - Tài liệu buổi 1-38 | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 CCNA v7 - Tài liệu buổi 1-38 nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

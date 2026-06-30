---
layout: page-toc
title: "Buổi 38: Tổng kết CCNA và Final Project"
permalink: /writeups/ccna-theory/buoi-38-tong-ket-ccna-final-project/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Tổng kết CCNA và Final Project

## Mục tiêu học tập

- Nắm vai trò của Tổng kết CCNA và Final Project trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Ôn tập 3 kỳ học: Network Fundamentals - Switching/Routing/Wireless - OSPF/ACL/NAT/WAN

| Nguồn video | https://www.youtube.com/watch?v=hX4LBr2l86g |
| --- | --- |
| Trọng tâm | Tổng kết kiến thức CCNA và hướng dẫn project tích hợp |
| Đối tượng | Sinh viên ôn CCNA/Packet Tracer trước final exam |
| Ghi chú Glasp | Đã tìm Glasp nhưng không thấy highlight trực tiếp phù hợp cho video này |

## 2. Các nhóm kiến thức cần nắm

| Nhóm kiến thức | Cần nhớ | Lệnh/khái niệm gợi ý |
| --- | --- | --- |
| Network fundamentals | Thiết bị đầu cuối, thiết bị trung gian, media, protocol, OSI/TCP-IP. | end device, intermediary device, router, switch, NIC |
| Ethernet & switching | Ethernet frame, MAC address, switch học địa chỉ nguồn và forward theo CAM/MAC table. | show mac address-table, ARP table |
| ARP/NDP | IPv4 dùng ARP để tìm MAC; IPv6 dùng Neighbor Discovery. | arp -a, show ip arp, ICMPv6 NS/NA |
| IPv4/IPv6 & subnet | Chia mạng, prefix, default gateway, địa chỉ private/public. | /24, /26, /64, gateway |
| Transport/Application | TCP/UDP, port, 3-way handshake, HTTP/DNS/DHCP/SSH/FTP/SMTP. | TCP 80/443/22, UDP 53/67/68 |

## 3. Trọng tâm kỹ thuật

VLAN, trunk và inter-VLAN routing

Tạo VLAN để chia broadcast domain.

Trunk 802.1Q để mang nhiều VLAN qua một link.

Inter-VLAN có 3 cách: legacy, Router-on-a-Stick, switch Layer 3.

STP và EtherChannel

STP chống loop trong mạng switch dự phòng.

## 4. OSPF

OSPF là giao thức link-state: router học trạng thái liên kết, xây LSDB, chạy SPF rồi đưa route tốt nhất vào routing table.

Cần phân biệt neighbor table, topology/LSDB và routing table.

Cần nhớ router-id, wildcard mask, network command, passive-interface, DR/BDR và metric/cost.

## 5. ACL

Standard ACL lọc chủ yếu theo source IP, thường đặt gần đích.

Extended ACL lọc theo source, destination, protocol, port, thường đặt gần nguồn.

ACL đọc từ trên xuống; nếu không match dòng nào thì bị implicit deny ở cuối.

## 6. NAT/PAT

Static NAT ánh xạ 1 private IP sang 1 public IP cố định.

Dynamic NAT dùng pool public IP; ai dùng trước thì được cấp trước.

PAT/Overload cho nhiều inside hosts dùng chung một public IP bằng cách phân biệt theo port.

## 7. WAN

WAN kết nối nhiều LAN ở các vị trí địa lý khác nhau thông qua nhà cung cấp dịch vụ.

Topology thường gặp: point-to-point, hub-and-spoke, dual-homed, full mesh, partial mesh.

Thuật ngữ cần biết: DTE, DCE, CPE, CO, service provider, leased line, packet switching, MPLS, VPN.

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

| Nguồn video | https://www.youtube.com/watch?v=hX4LBr2l86g |
| --- | --- |
| Trọng tâm | Tổng kết kiến thức CCNA và hướng dẫn project tích hợp |
| Đối tượng | Sinh viên ôn CCNA/Packet Tracer trước final exam |
| Ghi chú Glasp | Đã tìm Glasp nhưng không thấy highlight trực tiếp phù hợp cho video này |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Tổng kết CCNA và Final Project |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Tổng kết CCNA và Final Project giải quyết vấn đề gì trong mạng?
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
| Tổng kết CCNA và Final Project | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Tổng kết CCNA và Final Project nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

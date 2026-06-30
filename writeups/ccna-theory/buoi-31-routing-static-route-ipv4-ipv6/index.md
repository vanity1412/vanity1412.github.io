---
layout: page-toc
title: "Buổi 31: Static Route IPv4 và IPv6"
permalink: /writeups/ccna-theory/buoi-31-routing-static-route-ipv4-ipv6/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Static Route IPv4 và IPv6

## Mục tiêu học tập

- Nắm vai trò của Static Route IPv4 và IPv6 trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Routing - Static Route IPv4/IPv6

Tài liệu học tập từ transcript video CCNA

| Thông tin | Nội dung |
| --- | --- |
| Tiêu đề video | Buổi 31 |
| URL | https://www.youtube.com/watch?v=XzzNjDm29GQ |
| Chủ đề chính | Định tuyến, bảng định tuyến, longest prefix match, static route IPv4/IPv6 |
| Mục tiêu tài liệu | Giúp ôn lý thuyết, nhớ lệnh và tự làm lab Packet Tracer |

## 2. Router định tuyến như thế nào?

Router có hai nhiệm vụ chính: xác định đường đi tốt nhất và forward packet ra đúng interface hoặc next-hop. Khi một packet đến router, router không tự đoán đường đi mà tra cứu bảng định tuyến.

## 3. Bảng định tuyến và Longest Prefix Match

Bảng định tuyến được xem bằng lệnh show ip route. Mỗi dòng trong bảng định tuyến là một route entry, thường gồm loại route, mạng đích, next-hop hoặc exit interface.

| Ký hiệu | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| C | Connected route - mạng gắn trực tiếp vào router | C 10.0.1.0/24 is directly connected, G0/1 |
| L | Local route - địa chỉ IP của chính interface router | L 10.0.1.1/32 is directly connected, G0/1 |
| S | Static route - tuyến đường cấu hình thủ công | S 10.0.4.0/24 [1/0] via 10.0.3.2 |
| S* | Default static route - tuyến mặc định | S* 0.0.0.0/0 via ... |

Quy tắc quan trọng nhất trong buổi này là longest prefix match: nếu nhiều route cùng khớp với địa chỉ đích, router chọn route có prefix dài nhất, tức route cụ thể nhất.

## 4. Connected, Remote và Default Route

| Loại route | Router biết bằng cách nào? | Khi nào dùng? |
| --- | --- | --- |
| Connected route | Tự có khi interface được đặt IP và trạng thái up/up. | Dùng cho các mạng gắn trực tiếp vào router. |
| Remote route | Router phải học qua static route hoặc dynamic routing. | Dùng để đi đến mạng nằm sau router khác. |
| Default route | Cấu hình thủ công, đại diện cho mọi mạng chưa biết. | Dùng để đẩy traffic ra ISP/Internet hoặc router upstream. |

Trong transcript, R1 ban đầu chỉ biết các mạng trực tiếp 10.0.1.0/24, 10.0.2.0/24 và 10.0.3.0/24. Muốn PC ở phía R1 ping sang mạng 10.0.4.0/24 hoặc 10.0.5.0/24 thì R1 phải có static route sang R2, đồng thời R2 cũng ph...

## 5. Lab IPv4 Static Route trong Packet Tracer

| Thiết bị | Interface / mạng | IP gợi ý |
| --- | --- | --- |
| R1 | G0/1 - LAN PC1 | 10.0.1.1/24 |
| R1 | G0/2 - LAN PC2 | 10.0.2.1/24 |
| R1 | G0/0 - kết nối R2 | 10.0.3.1/24 |
| R2 | G0/0 - kết nối R1 | 10.0.3.2/24 |
| R2 | G0/1 - LAN PC3 | 10.0.4.1/24 |
| R2 | G0/2 - LAN PC4 | 10.0.5.1/24 |
| R2 - ISP | Serial /30 | 209.165.200.225/30 - 209.165.200.226/30 |

## 6. Cấu hình IP cơ bản trên router

R1(config)# hostname R1 R1(config)# interface g0/1 R1(config-if)# ip address 10.0.1.1 255.255.255.0 R1(config-if)# no shutdown R1(config)# interface g0/2 R1(config-if)# ip address 10.0.2.1 255.255.255.0 R1(config-if)#...

## 7. DHCP pool trên router để cấp IP cho PC

R1(config)# ip dhcp pool PC1 R1(dhcp-config)# network 10.0.1.0 255.255.255.0 R1(dhcp-config)# default-router 10.0.1.1 R1(config)# ip dhcp pool PC2 R1(dhcp-config)# network 10.0.2.0 255.255.255.0 R1(dhcp-config)# defau...

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
| Tiêu đề video | Buổi 31 |
| URL | https://www.youtube.com/watch?v=XzzNjDm29GQ |
| Chủ đề chính | Định tuyến, bảng định tuyến, longest prefix match, static route IPv4/IPv6 |
| Mục tiêu tài liệu | Giúp ôn lý thuyết, nhớ lệnh và tự làm lab Packet Tracer |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Static Route IPv4 và IPv6 |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Static Route IPv4 và IPv6 giải quyết vấn đề gì trong mạng?
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
| IPv6 | Địa chỉ IP thế hệ mới | Địa chỉ 128 bit viết dạng hexadecimal. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Static Route IPv4 và IPv6 nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

---
layout: page-toc
title: "Buổi 17: Switching và Basic Device Config"
permalink: /writeups/ccna-theory/buoi-17-switching-basic-device-config/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Switching và Basic Device Config

## Mục tiêu học tập

- Nắm vai trò của Switching và Basic Device Config trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Chủ đề: Switching cơ bản, cấu hình thiết bị, DHCP Relay, quản trị Switch từ xa, Telnet/SSH, Duplex/Speed và Auto-MDIX

Nguồn transcript: YouTube Buổi 17

Learn more on Glasp: https://glasp.co/reader?url=https://www.youtube.com/watch?v=JjLPMA3W97E

## 2. Tổng quan nhanh Buổi 17

Buổi 17 mở đầu cho giai đoạn học mới của CCNA với trọng tâm là Switching, Routing và Wireless. Trong buổi này, giảng viên tập trung vào thiết bị Switch: cách Switch khởi động, cách đặt IP quản lý, cấu hình default gat...

## 3. Mở đầu kỳ 2: Switching, Routing và Wireless

Sau khi hoàn thành phần nền tảng về mô hình TCP/IP, địa chỉ IPv4/IPv6, ICMP, Transport Layer và Application Layer, buổi 17 chuyển sang nội dung thực hành hơn: cấu hình thiết bị mạng. Ba mảng chính của kỳ này gồm Switc...

| Mảng học | Trọng tâm | Ý nghĩa thực tế |
| --- | --- | --- |
| Switching | Chuyển mạch trong LAN, Switch, VLAN, cổng, quản trị từ xa. | Xây dựng mạng nội bộ cho phòng máy, văn phòng, doanh nghiệp nhỏ. |
| Routing | Định tuyến giữa các mạng, đặc biệt là định tuyến tĩnh ở giai đoạn đầu. | Giúp các subnet khác nhau giao tiếp được với nhau. |
| Wireless | Mạng không dây, Access Point, SSID và các vấn đề kết nối Wi-Fi. | Thiết kế mạng Wi-Fi cho lớp học, văn phòng, tòa nhà. |

## 4. Chuỗi khởi động của Cisco Switch

Switch không “chạy ngay” sau khi cắm điện. Nó trải qua một chuỗi khởi động để tự kiểm tra phần cứng, nạp chương trình khởi động, tìm hệ điều hành IOS và nạp cấu hình đã lưu. Nắm được chuỗi này giúp hiểu vì sao có thể...

Cần nhớ

POST nằm trong ROM và kiểm tra phần cứng cơ bản như CPU, RAM, Flash.

Boot Loader là chương trình nhỏ hỗ trợ quá trình khởi động.

IOS thường nằm trong Flash.

startup-config của Switch được lưu dưới dạng file config.text.

## 5. Đèn LED, trạng thái cổng và PoE

Mặt trước của Switch Cisco có nhiều đèn LED. Khi làm thực tế, chỉ cần nhìn đèn cũng có thể đoán được thiết bị có nguồn, cổng có link, tốc độ đang chạy hoặc PoE có hoạt động hay không.

| Loại LED | Ý nghĩa |
| --- | --- |
| System LED | Cho biết thiết bị đã nhận nguồn và hệ thống đang hoạt động. |
| Port Status | Cho biết trạng thái cổng: có link, đang hoạt động, có traffic hoặc lỗi. |
| Duplex | Cho biết chế độ truyền dữ liệu của cổng: full-duplex hoặc half-duplex. |
| Speed | Cho biết tốc độ cổng như 10/100/1000 Mbps. |
| PoE | Cho biết cổng có đang cấp nguồn qua Ethernet cho thiết bị như AP, IP phone, camera hay không. |

PoE là gì?

## 6. Console, VLAN 1 và VLAN quản lý

Để cấu hình ban đầu, người quản trị thường dùng dây console kết nối trực tiếp từ máy tính vào Switch. Theo mặc định, các cổng Switch nằm trong VLAN 1. Tuy nhiên trong thực tế, không nên dùng VLAN 1 làm VLAN quản lý lâ...

| Khái niệm | Vai trò | Lưu ý |
| --- | --- | --- |
| Console | Cấu hình trực tiếp thiết bị khi mới mua hoặc khi mất cấu hình mạng. | Không phụ thuộc IP, dùng khi chưa thể SSH/Telnet. |
| VLAN 1 | VLAN mặc định của Switch. | Không nên dùng làm VLAN quản lý trong môi trường thật. |
| Management VLAN | VLAN dành riêng cho quản trị thiết bị. | Có thể dùng VLAN 99 hoặc VLAN riêng theo quy chuẩn tổ chức. |
| SVI/interface VLAN | Interface logic để đặt IP quản lý cho Switch. | Ví dụ interface vlan 1 hoặc interface vlan 99. |

## 7. DHCP Server và DHCP Relay với ip helper-address

Trong demo, giảng viên dựng mô hình có một DHCP Server ở mạng 192.168.1.0/24 và một mạng khác 172.16.1.0/24. Máy ở mạng khác không thể tự gửi broadcast DHCP trực tiếp đến DHCP Server qua router, nên cần lệnh ip helper...

Câu lệnh mẫu

Router(config)# interface g0/1 Router(config-if)# ip helper-address 192.168.1.254

Trong đó 192.168.1.254 là địa chỉ của DHCP Server. Khi client ở mạng khác gửi DHCP Discover, router sẽ chuyển tiếp yêu cầu này đến DHCP Server.

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

| Mảng học | Trọng tâm | Ý nghĩa thực tế |
| --- | --- | --- |
| Switching | Chuyển mạch trong LAN, Switch, VLAN, cổng, quản trị từ xa. | Xây dựng mạng nội bộ cho phòng máy, văn phòng, doanh nghiệp nhỏ. |
| Routing | Định tuyến giữa các mạng, đặc biệt là định tuyến tĩnh ở giai đoạn đầu. | Giúp các subnet khác nhau giao tiếp được với nhau. |
| Wireless | Mạng không dây, Access Point, SSID và các vấn đề kết nối Wi-Fi. | Thiết kế mạng Wi-Fi cho lớp học, văn phòng, tòa nhà. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Switching và Basic Device Config |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Switching và Basic Device Config giải quyết vấn đề gì trong mạng?
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
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Switching và Basic Device Config nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

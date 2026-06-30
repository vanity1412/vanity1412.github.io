---
layout: page-toc
title: "Buổi 13: IPv6"
permalink: /writeups/ccna-theory/buoi-13-ipv6/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# IPv6

## Mục tiêu học tập

- Nắm vai trò của IPv6 trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

| --- | --- |
| Buổi số | 13 |
| Link video | https://www.youtube.com/watch?v=dMVQKf3GCxI |
| Trọng tâm | IPv6, prefix length, interface ID, global unicast, link-local, multicast, EUI-64, cấu hình IPv6 trên Router/PC |

Sau buổi học này, sinh viên sẽ:

Giải thích được vì sao IPv6 ra đời và điểm khác biệt lớn nhất so với IPv4.

Nhận diện được cấu trúc IPv6 gồm 128 bit, 8 hextet và cách biểu diễn bằng hệ thập lục phân.

## 2. Vì sao cần IPv6?

Định nghĩa học thuật: IPv6 (Internet Protocol version 6) là phiên bản giao thức IP sử dụng địa chỉ dài 128 bit, được thiết kế để thay thế IPv4 32 bit và mở rộng không gian định danh thiết bị trên Internet.

Ví dụ thực tế: Một gia đình hiện nay có thể có điện thoại, laptop, TV thông minh, camera, đồng hồ thông minh, cảm biến IoT. Nếu toàn thế giới đều có nhiều thiết bị như vậy, không gian IPv4 32 bit không đáp ứng lâu dài...

- IPv4 có 32 bit, tối đa lý thuyết khoảng 2^32 địa chỉ.
- IPv6 có 128 bit, tối đa lý thuyết là 2^128 địa chỉ.
- IPv6 giải quyết bài toán cạn kiệt IPv4 và phù hợp với thời đại IoT.

- IPv6 không chỉ là địa chỉ dài hơn
- nó thay đổi cách biểu diễn, cách tự cấu hình và cách một số cơ chế mạng hoạt động.

## 3. Cấu trúc địa chỉ IPv6

Định nghĩa học thuật: Địa chỉ IPv6 dài 128 bit, thường được biểu diễn bằng 8 nhóm hệ thập lục phân, mỗi nhóm gọi là hextet và có độ dài 16 bit. Các hextet được phân tách bằng dấu hai chấm (:).

Ví dụ thực tế: Địa chỉ dạng đầy đủ có thể viết như: 2001:0DB8:0000:0000:1111:2222:3333:4444. Trong đó mỗi cụm như 2001 hoặc 0DB8 là một hextet.

- IPv6 dùng hệ 16 (hexadecimal), gồm các ký tự 0-9 và A-F.
- IPv6 không phân biệt chữ hoa/thường, ví dụ DB8 và db8 có cùng ý nghĩa.
- Mỗi hextet = 16 bit
- 8 hextet = 128 bit.

- Khi nhìn IPv6, hãy đếm đủ 8 hextet nếu nó đang ở dạng đầy đủ.

## 4. Quy tắc rút gọn địa chỉ IPv6

Định nghĩa học thuật: Rút gọn địa chỉ IPv6 là việc biểu diễn địa chỉ 128 bit ngắn hơn bằng cách loại bỏ các số 0 đứng đầu trong từng hextet và thay thế một chuỗi hextet toàn 0 liên tục bằng ký hiệu ::.

- IPv6 dài nên người ta cho phép viết tắt. Có hai kiểu viết tắt: bỏ số 0 ở đầu mỗi cụm và dùng :: để thay cho nhiều cụm 0000 liền nhau.

Ví dụ thực tế:

2001:0DB8:0000:0000:0000:0000:0000:0001 có thể rút gọn thành 2001:DB8::1.

FE80:0000:0000:0000:1234:5678:9ABC:DEF0 có thể rút gọn thành FE80::1234:5678:9ABC:DEF0.

- Chỉ được dùng dấu :: một lần duy nhất trong một địa chỉ IPv6.

## 5. Các loại địa chỉ IPv6: Unicast, Multicast, Anycast

Định nghĩa học thuật: IPv6 có các kiểu địa chỉ chính gồm Unicast, Multicast và Anycast. Unicast định danh một giao diện; multicast định danh một nhóm giao diện; anycast định danh nhiều giao diện nhưng gói tin được chu...

- Unicast là gửi cho một người. Multicast là gửi cho một nhóm người. Anycast là nhiều nơi cùng dùng một địa chỉ, hệ thống mạng tự chọn nơi phù hợp nhất để gửi đến.

| Kiểu địa chỉ | Mục đích | Ví dụ | Ghi nhớ nhanh |
| --- | --- | --- | --- |
| Unicast | Gửi đến một giao diện cụ thể | Global Unicast, Link-Local | Một điểm nhận |
| Multicast | Gửi đến một nhóm thiết bị | FF02::1, FF02::2 | Một nhóm nhận |
| Anycast | Nhiều thiết bị dùng chung một địa chỉ, chọn thiết bị gần nhất | Thường dùng trong hạ tầng định tuyến/dịch vụ | Cùng địa chỉ, chọn gần nhất |

- Trong thực hành cơ bản, cần nắm chắc Unicast và Link-Local trước

## 6. Prefix Length, Global Routing Prefix, Subnet ID và Interface ID

Định nghĩa học thuật: Prefix length là số bit đầu của địa chỉ IPv6 dùng để xác định phần mạng. Trong IPv6, phần định danh giao diện thường gọi là Interface ID, phổ biến dài 64 bit. Một địa chỉ global unicast thường đư...

- Nếu IPv4 có subnet mask để biết phần mạng và phần host, thì IPv6 thường dùng /64, /48... để chỉ số bit thuộc phần mạng. Phần sau cùng không gọi là host như IPv4 nữa mà thường gọi là Interface ID.

Ví dụ thực tế: 2001:DB8:ACAD:1::10/64 nghĩa là 64 bit đầu là phần mạng/prefix, 64 bit sau là Interface ID. Nếu tổ chức được cấp một prefix lớn, họ có thể dùng một phần bit để chia subnet nội bộ.

| Thành phần | Vai trò | Ví dụ thường gặp | Ghi chú |
| --- | --- | --- | --- |
| Global Routing Prefix | Phần được ISP/tổ chức cấp để định tuyến toàn cầu | 2001:DB8:ACAD::/48 | Tương tự vùng địa chỉ chính của tổ chức |
| Subnet ID | Phần dùng để chia mạng con trong tổ chức | 16 bit sau /48 trong mô hình /64 | Tạo ra nhiều subnet |

## 7. Global Unicast Address và Link-Local Address

Định nghĩa học thuật: Global Unicast Address là địa chỉ IPv6 có thể định tuyến trên Internet, tương tự địa chỉ public IPv4. Link-Local Address là địa chỉ chỉ có phạm vi trong cùng một liên kết/mạng cục bộ, thường thuộ...

Ví dụ thực tế:

Global Unicast: 2001:DB8:ACAD:1::1/64.

Link-Local: FE80::1 hoặc FE80::A553:... chỉ dùng trong phạm vi local link.

Trên Windows, khi gõ ipconfig /all, thường thấy cả IPv6 global và IPv6 link-local.

| Tiêu chí | Global Unicast | Link-Local |

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

| --- | --- |
| Buổi số | 13 |
| Link video | https://www.youtube.com/watch?v=dMVQKf3GCxI |
| Trọng tâm | IPv6, prefix length, interface ID, global unicast, link-local, multicast, EUI-64, cấu hình IPv6 trên Router/PC |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | IPv6 |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. IPv6 giải quyết vấn đề gì trong mạng?
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

🔑 IPv6 nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

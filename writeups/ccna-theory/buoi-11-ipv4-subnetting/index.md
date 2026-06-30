---
layout: page-toc
title: "Buổi 11: IPv4 Subnetting"
permalink: /writeups/ccna-theory/buoi-11-ipv4-subnetting/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# IPv4 Subnetting

## Mục tiêu học tập

- Nắm vai trò của IPv4 Subnetting trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Mẹo ghi nhớ nhanh

Sau buổi học này, sinh viên sẽ:

Hiểu được cấu trúc của địa chỉ IPv4 gồm phần Network và phần Host.

Giải thích được vai trò của subnet mask và ký hiệu CIDR như /24, /25, /26.

Tính được địa chỉ mạng, địa chỉ broadcast, địa chỉ đầu tiên và địa chỉ cuối cùng của một subnet.

Phân biệt được địa chỉ hợp lệ để gán cho máy tính và địa chỉ không được gán như network/broadcast address.

Phân biệt được Unicast, Broadcast, Multicast trong IPv4.

## 2. Chuẩn bị kiến thức: đổi cơ số và vai trò của IPv4

Khái niệm chính: IPv4 là địa chỉ logic ở tầng Network dùng để định danh thiết bị trong môi trường mạng. Việc tính toán IPv4 phụ thuộc nhiều vào biểu diễn nhị phân của địa chỉ và subnet mask.

Ví dụ thực tế: Khi máy tính có địa chỉ 192.168.1.10/24, ta hiểu thiết bị này thuộc mạng 192.168.1.0 và bản thân thiết bị là một host trong mạng đó.

- IPv4 có 32 bit, thường được viết thành 4 octet thập phân.
- Subnetting yêu cầu chuyển đổi giữa thập phân và nhị phân.
- Không nắm nhị phân thì rất dễ sai khi tính /18, /22, /25, /26.

- Buổi học IPv4 không chỉ là nhớ địa chỉ, mà là hiểu cách bit network và bit host tạo ra mạng con.

## 3. Cấu trúc IPv4: Network portion và Host portion

Khái niệm chính: Một địa chỉ IPv4 gồm hai thành phần: Network portion dùng để xác định mạng, và Host portion dùng để xác định thiết bị cụ thể trong mạng đó. Subnet mask là giá trị dùng để phân biệt hai phần này.

Ví dụ thực tế: Với 192.168.10.10/24, ba octet đầu thường là phần mạng 192.168.10, còn octet cuối là phần host.

- IPv4 không thể hiểu đúng nếu thiếu subnet mask.
- Cùng một IP nhưng subnet mask khác nhau thì mạng chứa IP đó có thể khác nhau.
- Prefix /24 nghĩa là 24 bit đầu tiên thuộc phần network.

- IP trả lời câu hỏi “thiết bị là ai?”, còn subnet mask trả lời câu hỏi “thiết bị thuộc mạng nào?”.

## 4. Subnet Mask và ký hiệu CIDR

Khái niệm chính: Subnet mask là chuỗi 32 bit gồm các bit 1 liên tiếp từ trái sang phải để đánh dấu phần network, sau đó là các bit 0 để đánh dấu phần host. CIDR notation viết ngắn số bit network bằng dạng /x.

Ví dụ thực tế: /8 tương ứng 255.0.0.0, /16 tương ứng 255.255.0.0, /24 tương ứng 255.255.255.0, /25 tương ứng 255.255.255.128.

- Subnet mask luôn có các bit 1 liên tục từ trái sang phải
- không có dạng 11111111.00001111...
- CIDR /x cho biết có x bit network.
- Phép AND giữa IP và subnet mask cho ra network address.

- Nhìn /24, /25, /26 không phải để đọc cho vui

## 5. Network Address, Broadcast Address, First và Last Usable

Khái niệm chính: Trong một subnet, network address là địa chỉ có toàn bộ bit host bằng 0; broadcast address là địa chỉ có toàn bộ bit host bằng 1; first usable và last usable là hai địa chỉ host dùng được đầu và cuối...

Ví dụ thực tế: Với 192.168.10.10/24: network là 192.168.10.0, broadcast là 192.168.10.255, first usable là 192.168.10.1, last usable là 192.168.10.254.

- Network address không gán cho máy tính.
- Broadcast address không gán cho máy tính.
- Các địa chỉ host usable nằm từ network + 1 đến broadcast − 1.

- Khi đề bài hỏi “địa chỉ đầu/cuối”, phải hiểu là địa chỉ host dùng được, không phải network hoặc broadcast.

| Loại địa chỉ | Quy tắc bit host | Có gán cho máy tính không? | Ví dụ với 192.168.10.10/24 |

## 6. Ví dụ tính subnet: 172.16.1.5/22 và 192.168.1.100/18

Khái niệm chính: Khi tính subnet, cần xác định subnet mask, số bit host, block size/bước nhảy, sau đó suy ra network, broadcast, first usable và last usable.

Ví dụ thực tế: 172.16.1.5/22 có subnet mask 255.255.252.0. Bước nhảy ở octet thứ 3 là 4, nên octet 1 nằm trong khoảng 0–3. Vì vậy network là 172.16.0.0 và broadcast là 172.16.3.255.

- Bước nhảy thường tính ở octet “đang chia” bằng 256 − giá trị subnet mask của octet đó.
- Với /22, mạng nhảy theo 4 ở octet thứ 3.
- Với /18, mạng nhảy theo 64 ở octet thứ 3.

- Tính subnet là tìm khoảng. IP thuộc khoảng nào thì network là đầu khoảng, broadcast là cuối khoảng.

| Bài toán | Subnet mask | Network | First usable | Last usable | Broadcast |

## 7. Địa chỉ nào có thể gán cho máy tính?

Khái niệm chính: Một địa chỉ IPv4 chỉ có thể gán cho host nếu nó không phải network address và không phải broadcast address trong subnet đang xét.

- Một số địa chỉ nhìn “đẹp” như .128 hoặc .64 không chắc đã dùng được. Phải xem prefix bên cạnh mới biết nó có phải địa chỉ mạng hay không.

Ví dụ thực tế: 192.168.1.128/25 không gán được cho máy tính vì /25 chia 192.168.1.0/24 thành hai mạng: 192.168.1.0/25 và 192.168.1.128/25. Vì vậy 192.168.1.128 là network address của subnet thứ hai.

- Luôn kiểm tra phần host bit.
- Nếu toàn bộ host bit = 0 → địa chỉ mạng.
- Nếu toàn bộ host bit = 1 → địa chỉ broadcast.
- Hai loại này đều không gán cho PC.

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

| CIDR | Subnet mask dạng nhị phân rút gọn | Subnet mask thập phân | Số bit host |
| --- | --- | --- | --- |
| /8 | 11111111.00000000.00000000.00000000 | 255.0.0.0 | 24 |
| /16 | 11111111.11111111.00000000.00000000 | 255.255.0.0 | 16 |
| /24 | 11111111.11111111.11111111.00000000 | 255.255.255.0 | 8 |
| /25 | 11111111.11111111.11111111.10000000 | 255.255.255.128 | 7 |
| /26 | 11111111.11111111.11111111.11000000 | 255.255.255.192 | 6 |
| /27 | 11111111.11111111.11111111.11100000 | 255.255.255.224 | 5 |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | IPv4 Subnetting |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. IPv4 Subnetting giải quyết vấn đề gì trong mạng?
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
| Subnetting | Chia mạng con | Chia một network lớn thành nhiều subnet nhỏ. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 IPv4 Subnetting nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

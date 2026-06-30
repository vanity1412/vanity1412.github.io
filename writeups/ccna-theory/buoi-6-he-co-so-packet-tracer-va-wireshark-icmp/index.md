---
layout: page-toc
title: "Buổi 6: Hệ cơ số, Packet Tracer và ICMP"
permalink: /writeups/ccna-theory/buoi-6-he-co-so-packet-tracer-va-wireshark-icmp/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Hệ cơ số, Packet Tracer và ICMP

## Mục tiêu học tập

- Nắm vai trò của Hệ cơ số, Packet Tracer và ICMP trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP MẠNG MÁY TÍNH

Hệ cơ số, Packet Tracer và Wireshark ICMP

| --- | --- |
| Buổi số | 6 |
| Nguồn | Transcript video bài giảng |
| Link video | https://www.youtube.com/watch?v=v_ZmHOhM720 |
| Ngày | Chưa cung cấp trong transcript |

## 2. Mẹo ghi nhớ nhanh

Sau buổi học này, sinh viên cần đạt được các năng lực sau:

Ôn lại vai trò của Physical Layer trong mô hình OSI và mối liên hệ giữa bit 0/1 với đường truyền mạng.

Hiểu các hệ cơ số thường gặp trong mạng máy tính: Binary, Decimal, Hexadecimal và Octal.

Thành thạo chuyển đổi giữa nhị phân, thập phân và thập lục phân, đặc biệt trong phạm vi một octet IPv4.

Biết cách đọc địa chỉ IPv4 ở dạng decimal và hiểu bản chất nhị phân bên dưới.

Thực hành thêm module, chọn loại cáp và kiểm tra interface trong Cisco Packet Tracer.

## 3. Ôn lại Physical Layer trong mô hình OSI

Trong phần đầu, giảng viên nhắc lại nội dung Module 4: tầng vật lý là tầng thấp nhất trong mô hình OSI, chịu trách nhiệm truyền bit 0/1 qua môi trường truyền dẫn như cáp đồng, cáp quang hoặc sóng không dây.

| Lớp giải thích | Nội dung |
| --- | --- |
| Định nghĩa học thuật | Physical Layer là tầng thứ nhất của mô hình OSI, quy định cách biểu diễn và truyền tín hiệu bit qua môi trường vật lý. |
| Ví dụ thực tế | Khi hai máy tính trao đổi dữ liệu qua dây LAN, các bit 0/1 được chuyển thành tín hiệu điện trên cáp Ethernet. |

- Tầng vật lý không quan tâm nội dung dữ liệu là gì
- nó chỉ quan tâm cách đưa bit qua đường truyền.
- Các bài lab chọn cáp, module, cổng kết nối trong Packet Tracer chính là đang làm việc với tư duy của tầng vật lý.

## 4. Module 5 - Các hệ cơ số trong mạng máy tính

Trọng tâm của Module 5 là hệ cơ số. Trong máy tính và mạng máy tính, dữ liệu cuối cùng đều được biểu diễn bằng bit 0/1, nhưng con người thường đọc ở dạng thập phân hoặc thập lục phân cho dễ nhìn.

| Hệ cơ số | Tên tiếng Anh | Ký hiệu dùng | Chữ số hợp lệ | Vai trò trong mạng |
| --- | --- | --- | --- | --- |
| 2 | Binary | bin | 0, 1 | Biểu diễn bản chất dữ liệu máy tính và bit của địa chỉ IP. |
| 8 | Octal | oct | 0-7 | Ít dùng hơn trong nội dung bài này; nguyên lý tương tự nhóm bit. |
| 10 | Decimal | dec | 0-9 | Dạng con người thường đọc, ví dụ 192.168.1.1. |
| 16 | Hexadecimal | hex | 0-9, A-F | Dùng nhiều trong MAC address, IPv6 và biểu diễn byte gọn hơn. |

- Máy tính chỉ hiểu bit 0 và 1, còn decimal/hex là cách con người biểu diễn cho dễ đọc.

## 5. Chuyển đổi Binary sang Decimal

Khi học IPv4, mỗi octet gồm 8 bit. Vì vậy, khi đổi nhị phân sang thập phân trong mạng, ta thường dùng bảng trọng số gồm 8 vị trí: 128, 64, 32, 16, 8, 4, 2, 1.

| Vị trí bit từ trái sang phải | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trọng số | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| Ví dụ 10101000 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| Cộng giá trị | 128 | 0 | 32 | 0 | 8 | 0 | 0 | 0 |

Công thức tổng quát:

Giá trị decimal = b7×2^7 + b6×2^6 + b5×2^5 + ... + b1×2^1 + b0×2^0

## 6. Chuyển đổi Decimal sang Binary

Ngược lại, khi đổi thập phân sang nhị phân trong phạm vi một octet, ta dùng bảng trọng số 128-64-32-16-8-4-2-1 và so sánh từ trái sang phải.

## 7. Lặp lại cho đến trọng số cuối cùng là 1.

| Số decimal | Cách nhẩm | Kết quả binary 8 bit |
| --- | --- | --- |
| 192 | 192 >=128 -> 1, còn 64; 64 >=64 -> 1; còn lại 0 | 11000000 |
| 178 | 128 + 32 + 16 + 2 | 10110010 |
| 100 | 64 + 32 + 4 | 01100100 |
| 255 | 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 | 11111111 |

- Trong một octet 8 bit, giá trị lớn nhất là 255 vì tất cả 8 bit đều bằng 1.
- Nếu cần biểu diễn số 256 trở lên thì phải dùng 9 bit hoặc nhiều hơn, không còn nằm trong phạm vi một octet 8 bit.
- Khi học địa chỉ IPv4, mỗ...

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
| Buổi số | 6 |
| Nguồn | Transcript video bài giảng |
| Link video | https://www.youtube.com/watch?v=v_ZmHOhM720 |
| Ngày | Chưa cung cấp trong transcript |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Hệ cơ số, Packet Tracer và ICMP |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Hệ cơ số, Packet Tracer và ICMP giải quyết vấn đề gì trong mạng?
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
| ICMP | Giao thức thông báo lỗi | Hỗ trợ ping, traceroute và báo lỗi IP. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Hệ cơ số, Packet Tracer và ICMP nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

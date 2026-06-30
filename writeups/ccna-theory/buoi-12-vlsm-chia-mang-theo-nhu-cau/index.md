---
layout: page-toc
title: "Buổi 12: VLSM"
permalink: /writeups/ccna-theory/buoi-12-vlsm-chia-mang-theo-nhu-cau/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# VLSM

## Mục tiêu học tập

- Nắm vai trò của VLSM trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Mẹo ghi nhớ nhanh

Sau buổi học này, sinh viên sẽ:

Ôn lại cách xác định network address, broadcast address, first usable và last usable của một subnet.

Giải thích được khái niệm VLSM (Variable Length Subnet Mask) - chia mạng với subnet mask có độ dài khác nhau.

Biết chọn prefix phù hợp dựa trên số host yêu cầu của từng mạng.

Nắm nguyên tắc chia subnet theo thứ tự từ mạng cần nhiều host nhất đến mạng cần ít host nhất.

Thực hiện được bài toán chia IP theo nhu cầu và liệt kê đầy đủ subnet, usable host range, broadcast.

## 2. Ôn tập kiến thức chia IP từ buổi trước

Khái niệm chính: Subnetting là quá trình chia một block IP lớn thành nhiều subnet nhỏ hơn. Ở buổi trước, sinh viên đã học cách tìm địa chỉ mạng, địa chỉ quảng bá, địa chỉ đầu, địa chỉ cuối và chia đều một mạng thành 2...

- Trước khi học chia nâng cao, ta phải chắc lại cách đọc một dải IP: mạng bắt đầu ở đâu, kết thúc ở đâu, IP nào gán được cho máy, IP nào không được gán.

Ví dụ thực tế: Với 192.168.1.0/24 chia thành 8 mạng, ta mượn 3 bit, được /27, mỗi subnet có 32 địa chỉ và 30 địa chỉ usable.

- Buổi 11 là nền tảng bắt buộc để học Buổi 12.
- Nếu chưa tính được network/broadcast thì chưa nên làm VLSM.
- Chia đều subnet còn gọi là chia theo cùng kích thước subnet.

- Mọi bài VLSM đều bắt đầu từ kỹ năng subnetting cơ bản.

## 3. Vấn đề của cách chia đều subnet

Khái niệm chính: Chia đều subnet nghĩa là mọi subnet con có cùng kích thước và cùng subnet mask. Cách này dễ tính nhưng có thể gây lãng phí địa chỉ khi mỗi mạng con có nhu cầu host khác nhau.

Ví dụ thực tế: Một mạng chỉ cần 10 host nhưng được cấp subnet /26 có 62 host usable thì thừa hơn 50 địa chỉ IP.

- Chia đều dễ làm nhưng không tối ưu. Buổi 12 chuyển sang chia theo nhu cầu.

## 4. Bảng prefix /25 đến /30 và số host usable

Khái niệm chính: Khi tăng prefix từ /25 lên /30, số bit network tăng và số bit host giảm. Vì số host usable bằng 2^h - 2, prefix càng lớn thì số host dùng được trong mỗi subnet càng ít.

- Prefix càng lớn thì miếng bánh càng nhỏ. /25 là miếng lớn, /30 là miếng rất nhỏ chỉ đủ cho hai đầu kết nối.

Ví dụ thực tế: /27 có 5 bit host nên có 2^5 = 32 địa chỉ, usable host = 30. /30 có 2 bit host nên có 4 địa chỉ, usable host = 2.

- Công thức usable host: 2^(số bit host) - 2.
- Prefix mới càng lớn thì subnet càng nhỏ.
- /30 thường dùng cho kết nối point-to-point giữa hai router vì chỉ cần 2 địa chỉ usable.

- Để chọn prefix, hãy hỏi: mạng này cần bao nhiêu host usable?

## 5. VLSM - chia subnet theo nhu cầu

Khái niệm chính: VLSM (Variable Length Subnet Mask) là kỹ thuật chia một block IP thành các subnet có độ dài subnet mask khác nhau, nhằm cấp phát địa chỉ theo đúng nhu cầu host của từng mạng.

- VLSM là cách cắt miếng bánh IP không đều: mạng đông máy lấy phần lớn, mạng ít máy lấy phần nhỏ.

Ví dụ thực tế: Trong topology có các mạng LAN cần nhiều host và các đường kết nối router-router chỉ cần 2 host, VLSM cho phép dùng /27 cho LAN lớn và /30 cho kết nối point-to-point để tiết kiệm IP.

- VLSM giúp giảm lãng phí địa chỉ IPv4.
- Các subnet sau khi chia phải không chồng lấn nhau.
- Một block lớn có thể được chia tiếp thành nhiều block nhỏ hơn.

## 6. Nguyên tắc quan trọng: chia mạng lớn trước, mạng nhỏ sau

Khái niệm chính: Khi chia VLSM, cần sắp xếp các mạng theo số host yêu cầu từ lớn đến nhỏ, sau đó cấp phát subnet lớn trước, dùng phần còn lại để tiếp tục chia cho các mạng nhỏ hơn.

Ví dụ thực tế: Nếu có các mạng cần 110, 50, 20, 10, 2, 2 host thì phải cấp cho 110 host trước, sau đó 50, rồi 20, 10 và cuối cùng là các mạng 2 host.

- Luôn sắp xếp nhu cầu host giảm dần.
- Chọn subnet nhỏ nhất nhưng vẫn đủ usable host.
- Sau khi cấp một subnet, phần địa chỉ còn lại được dùng để chia tiếp.

- Sai thứ tự chia là lỗi phổ biến nhất trong VLSM.

## 7. Ví dụ mẫu: chia 192.168.1.0/24 theo nhu cầu

Khái niệm chính: Bài toán VLSM có thể giải bằng cách lặp lại ba việc: xác định số host cần, chọn số bit host phù hợp, cấp subnet đầu tiên còn trống theo đúng prefix.

- Ta lấy mạng gốc như một miếng bánh. Cấp phần đủ lớn cho mạng 110 host trước, rồi lấy phần còn lại chia tiếp cho 50 host, 20 host, 10 host và các mạng 2 host.

Ví dụ thực tế: Với 192.168.1.0/24: 110 host dùng /25, 50 host dùng /26, 20 host dùng /27, 10 host dùng /28, mỗi mạng 2 host dùng /30.

- 110 host cần 7 bit host vì 2^7 - 2 = 126.
- 50 host cần 6 bit host vì 2^6 - 2 = 62.
- 2 host cần 2 bit host vì 2^2 - 2 = 2.

- Cách làm không phải học thuộc đáp án, mà là hiểu cách lấy phần còn lại để chia tiếp.

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

| Tiêu chí | FLSM - chia đều | VLSM - chia theo nhu cầu |
| --- | --- | --- |
| Tên đầy đủ | Fixed Length Subnet Mask | Variable Length Subnet Mask |
| Subnet mask | Tất cả subnet cùng prefix | Các subnet có thể khác prefix |
| Cách chia | Chia thành các phần bằng nhau | Mạng lớn lấy phần lớn, mạng nhỏ lấy phần nhỏ |
| Ưu điểm | Dễ tính, dễ học ban đầu | Tiết kiệm IP, sát thực tế |
| Nhược điểm | Dễ lãng phí khi nhu cầu host khác nhau | Cần tính cẩn thận để tránh overlap |
| Ví dụ | Tất cả mạng đều /27 | 110 host /25, 50 host /26, 2 host /30 |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | VLSM |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. VLSM giải quyết vấn đề gì trong mạng?
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
| VLSM | Subnet mask biến đổi | Chia subnet theo nhu cầu host khác nhau. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 VLSM nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

---
layout: page-toc
title: "Buổi 35: ACL"
permalink: /writeups/ccna-theory/buoi-35-acl-access-control-list/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# ACL

## Mục tiêu học tập

- Nắm vai trò của ACL trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Lọc gói tin, inbound/outbound ACL, wildcard mask, standard/extended ACL và lab Packet Tracer

| Nguồn video | https://www.youtube.com/watch?v=OBv-gBj9brA |
| --- | --- |
| Mục tiêu | Hiểu ACL là gì, cách router xử lý ACL, wildcard mask, standard/extended ACL và cách apply ACL lên interface. |
| Phần thực hành | Packet Tracer: bài 5.1.8 và 5.1.9, làm quen với ACL cơ bản. |
| Ghi chú Glasp | Đã tìm Glasp theo yêu cầu nhưng không thấy highlight trực tiếp phù hợp cho video này. |

## 2. Tổng quan nhanh toàn buổi

Access Control List (ACL) là một chuỗi câu lệnh trên Cisco IOS dùng để lọc packet dựa trên thông tin trong header. Mặc định router không tự có ACL, nên nếu chưa cấu hình thì router chỉ định tuyến/forward theo bảng địn...

Khi ACL được apply vào interface, router sẽ kiểm tra packet theo danh sách permit/deny. Nếu được permit thì gói tin đi tiếp, nếu bị deny thì bị loại bỏ.

Một ACL có thể được áp theo hai chiều trên interface: inbound là gói tin đi vào router qua interface đó; outbound là gói tin đi ra khỏi router qua interface đó.

Router xử lý ACL theo thứ tự từ trên xuống. Khi gặp dòng đầu tiên match, router thực hiện permit hoặc deny và dừng kiểm tra. Nếu không dòng nào match, gói tin bị chặn bởi implicit deny ở cuối ACL.

Wildcard mask là giá trị dùng để xác định phần nào của địa chỉ IP cần so khớp. Trong wildcard mask: bit 0 nghĩa là phải khớp chính xác, bit 1 nghĩa là không cần quan tâm.

| Subnet | Subnet mask | Wildcard | Ý nghĩa |

## 3. Bảng lệnh ACL cần nhớ

| Mục đích | Lệnh | Ghi chú |
| --- | --- | --- |
| Tạo standard ACL theo số | access-list 10 permit 192.168.20.0 0.0.0.255 | ACL 10 cho phép mạng 192.168.20.0/24 |
| Chặn host cụ thể | access-list 10 deny host 192.168.10.10 | host tương đương wildcard 0.0.0.0 |
| Cho phép tất cả | access-list 10 permit any | Nên thêm cuối ACL nếu không muốn implicit deny chặn hết |
| Ghi chú dòng ACL | access-list 10 remark TEXT | Chỉ để chú thích, không lọc packet |
| Named ACL | ip access-list standard NAME | Dễ quản lý hơn khi cấu hình lớn |
| Apply ACL | ip access-group 10 in/out | Đặt trong interface config mode |
| Xem ACL | show access-lists | Xem sequence, permit/deny, hit count |
| Xem ACL trên interface | show ip interface g0/0 | Kiểm tra ACL đang áp inbound/outbound |

## 4. Quy trình lab Packet Tracer

Bước 1: Đọc yêu cầu bài lab: chặn/cho phép mạng nào, host nào, đi đến đâu.

Bước 2: Vẽ luồng packet: nguồn -> router gần nguồn -> router trung gian -> router gần đích -> đích.

Bước 3: Tính wildcard mask đúng với host hoặc subnet cần lọc.

Bước 4: Viết ACL theo thứ tự cụ thể trước, tổng quát sau.

Bước 5: Apply ACL vào đúng interface và đúng chiều in/out.

Bước 6: Test bằng ping/tracert và kiểm tra bằng show access-lists, show ip interface.

## 5. Kiến thức trọng tâm cần nhớ

ACL là danh sách permit/deny dùng để lọc packet dựa vào thông tin header.

ACL không tự hoạt động nếu chưa được apply vào interface bằng ip access-group.

ACL đọc từ trên xuống; gặp dòng match đầu tiên thì dừng.

Cuối ACL luôn có implicit deny, nên nếu chỉ viết deny mà không permit thì có thể chặn hết traffic.

Wildcard mask: 0 = phải match, 255 = bỏ qua. Ví dụ 192.168.1.0 0.0.0.255 là mạng /24.

Standard ACL chỉ lọc source IP, nên đặt gần đích nhất có thể.

## 6. Ghi chú nguồn học thêm

Nội dung chính được biên soạn từ transcript Buổi 35. Trước khi biên soạn, đã tìm các highlight liên quan trên Glasp bằng các truy vấn về ACL, wildcard mask, standard ACL và extended ACL; không tìm thấy highlight trực...

Có thể đối chiếu thêm tài liệu Cisco về IP Access Lists để kiểm tra cú pháp ACL, wildcard mask, numbered/named ACL và cách áp ACL lên interface.

Learn more on Glasp: https://glasp.co/reader?url=https://www.youtube.com/watch?v=OBv-gBj9brA

## 7. Checklist thực hành

- Đọc yêu cầu lab và xác định phần kiến thức liên quan.
- Vẽ hoặc quan sát topology trước khi cấu hình.
- Ghi lại IP/subnet/VLAN/interface cần dùng.
- Cấu hình theo từng cụm nhỏ, tránh nhập toàn bộ một lần.
- Kiểm tra trạng thái interface và bảng liên quan sau mỗi bước.
- Dùng `ping`, `traceroute` hoặc lệnh `show` phù hợp để xác minh.
- Nếu lỗi, quay lại kiểm tra từ Layer 1/2 trước rồi mới lên Layer 3.
- Lưu cấu hình và ghi chú nguyên nhân lỗi nếu có.

## 8. Bảng tham chiếu nhanh

| Nguồn video | https://www.youtube.com/watch?v=OBv-gBj9brA |
| --- | --- |
| Mục tiêu | Hiểu ACL là gì, cách router xử lý ACL, wildcard mask, standard/extended ACL và cách apply ACL lên interface. |
| Phần thực hành | Packet Tracer: bài 5.1.8 và 5.1.9, làm quen với ACL cơ bản. |
| Ghi chú Glasp | Đã tìm Glasp theo yêu cầu nhưng không thấy highlight trực tiếp phù hợp cho video này. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | ACL |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 9. Câu hỏi ôn tập

### Lý thuyết

1. ACL giải quyết vấn đề gì trong mạng?
2. Các thành phần hoặc trạng thái quan trọng nhất của chủ đề này là gì?
3. Khi nào cần dùng kiến thức này trong lab CCNA?
4. Dấu hiệu nào cho thấy cấu hình hoặc thiết kế đang sai?

### Bài tập

1. Dựng một topology nhỏ trong Packet Tracer có liên quan đến bài học.
2. Cấu hình theo yêu cầu, sau đó ghi lại lệnh kiểm tra chính.
3. Tạo một lỗi thường gặp, quan sát triệu chứng và sửa lại.
4. Viết checklist 5 bước để tự kiểm tra trước khi nộp lab.

## 10. Thuật ngữ quan trọng

| Thuật ngữ | Tiếng Việt | Giải thích |
| --- | --- | --- |
| ACL | Danh sách kiểm soát truy cập | Permit/deny traffic dựa trên điều kiện match. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 11. Ghi nhớ nhanh

🔑 ACL nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

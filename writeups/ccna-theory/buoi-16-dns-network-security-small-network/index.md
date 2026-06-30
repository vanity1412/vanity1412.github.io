---
layout: page-toc
title: "Buổi 16: DNS và Network Security"
permalink: /writeups/ccna-theory/buoi-16-dns-network-security-small-network/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# DNS và Network Security

## Mục tiêu học tập

- Nắm vai trò của DNS và Network Security trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. DNS, NSLOOKUP, NETWORK SECURITY CĂN BẢN VÀ THIẾT KẾ MẠNG NHỎ

Tài liệu học tập biên soạn từ transcript YouTube

https://www.youtube.com/watch?v=H7ZSF5yDi3c

Mục tiêu tài liệu: Biến transcript Buổi 16 thành tài liệu ôn tập dễ học, có giải thích khái niệm, bảng so sánh, ví dụ lệnh, flow thực hành và phần cần nhớ.

Trọng tâm: DNS/nslookup, bản ghi DNS, DHCP/FTP nhắc lại, network security, lỗ hổng, kiểu tấn công, phòng thủ theo chiều sâu, bảo vệ thiết bị Cisco, small network, network baseline và monitoring.

## 2. Cần nhớ, thuật ngữ, câu hỏi ôn tập, bài tập

Hiểu DNS và nslookup: biết DNS ánh xạ tên miền với IP, biết kiểm tra các bản ghi A, AAAA, NS, MX, CNAME, TXT, PTR.

Nắm lại tầng ứng dụng: liên hệ DNS, DHCP, FTP, Web, Mail với các dịch vụ thực tế trong mạng.

Nhận diện rủi ro bảo mật: phân biệt lỗ hổng công nghệ, cấu hình và chính sách.

Biết tư duy phòng thủ: phòng thủ theo chiều sâu, backup, cập nhật bản vá, phân quyền tối thiểu, ghi log.

Bảo vệ thiết bị Cisco cơ bản: mật khẩu mạnh, mã hóa mật khẩu, giới hạn đăng nhập sai, SSH, tắt dịch vụ/cổng không dùng.

Tư duy thiết kế mạng nhỏ: xác định thiết bị, chi phí/ngân sách, dự phòng, tài liệu hóa, baseline và giám sát.

## 3. DNS là gì?

Định nghĩa học thuật: DNS (Domain Name System) là hệ thống phân giải tên miền, dùng để ánh xạ tên miền dễ nhớ sang địa chỉ IP mà máy tính có thể sử dụng.

Ví dụ thực tế: Khi gõ một tên miền vào trình duyệt, máy sẽ hỏi DNS server xem tên miền đó tương ứng với địa chỉ IP nào, rồi mới kết nối tới máy chủ thật.

Cần nhớ: Nếu vào website bằng địa chỉ IP trực tiếp thì có thể không cần hỏi DNS. Nếu vào bằng tên miền thì gần như luôn cần quá trình phân giải DNS trước.

## 4. nslookup dùng để làm gì?

Định nghĩa học thuật: nslookup là công cụ dòng lệnh dùng để truy vấn DNS, kiểm tra tên miền, địa chỉ IP và các bản ghi DNS.

Ví dụ thực tế: Trong Windows CMD, gõ nslookup để vào chế độ tương tác, sau đó dùng set type=A hoặc set type=MX để kiểm tra bản ghi mong muốn.

nslookup

set type=A

example.com

set type=MX

## 5. Các bản ghi DNS quan trọng

| Bản ghi | Ý nghĩa | Khi dùng |
| --- | --- | --- |
| A | Tên miền -> IPv4 | Dùng khi muốn biết website/domain có địa chỉ IPv4 nào. |
| AAAA | Tên miền -> IPv6 | Dùng khi kiểm tra domain có hỗ trợ IPv6 hay không. |
| NS | Domain -> Name Server | Cho biết máy chủ DNS nào quản lý domain. |
| MX | Domain -> Mail Server | Cho biết máy chủ thư nhận email cho domain. |
| CNAME | Alias -> tên chuẩn | Tạo bí danh cho domain/subdomain. |
| TXT | Thông tin văn bản | Thường dùng cho xác minh domain, SPF/DKIM/DMARC, ghi chú bảo mật. |
| PTR | IP -> tên miền | Tra ngược địa chỉ IP ra tên miền tương ứng nếu có reverse DNS. |

## 6. Kiểm tra IPv4 của tên miền

nslookup

set type=A

actvn.vn

## 7. Kiểm tra name server quản lý domain

set type=NS

actvn.vn

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

| Bản ghi | Ý nghĩa | Khi dùng |
| --- | --- | --- |
| A | Tên miền -> IPv4 | Dùng khi muốn biết website/domain có địa chỉ IPv4 nào. |
| AAAA | Tên miền -> IPv6 | Dùng khi kiểm tra domain có hỗ trợ IPv6 hay không. |
| NS | Domain -> Name Server | Cho biết máy chủ DNS nào quản lý domain. |
| MX | Domain -> Mail Server | Cho biết máy chủ thư nhận email cho domain. |
| CNAME | Alias -> tên chuẩn | Tạo bí danh cho domain/subdomain. |
| TXT | Thông tin văn bản | Thường dùng cho xác minh domain, SPF/DKIM/DMARC, ghi chú bảo mật. |
| PTR | IP -> tên miền | Tra ngược địa chỉ IP ra tên miền tương ứng nếu có reverse DNS. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | DNS và Network Security |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. DNS và Network Security giải quyết vấn đề gì trong mạng?
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
| Port Security | Bảo mật cổng switch | Giới hạn MAC được phép dùng trên switchport. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 DNS và Network Security nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

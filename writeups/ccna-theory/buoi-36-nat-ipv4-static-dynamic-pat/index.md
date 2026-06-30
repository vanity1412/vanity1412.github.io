---
layout: page-toc
title: "Buổi 36: NAT IPv4"
permalink: /writeups/ccna-theory/buoi-36-nat-ipv4-static-dynamic-pat/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# NAT IPv4

## Mục tiêu học tập

- Nắm vai trò của NAT IPv4 trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Vì sao cần NAT cho IPv4?

IPv4 chỉ có không gian địa chỉ 32 bit nên số lượng địa chỉ public là hữu hạn. Khi số thiết bị kết nối Internet tăng lên, việc cấp một IP public riêng cho từng thiết bị trở nên không thực tế.

Giải pháp là chia địa chỉ thành hai nhóm: IP private dùng trong nội bộ và IP public dùng khi đi ra Internet. NAT nằm tại router biên để thực hiện chuyển đổi địa chỉ.

IP private không được định tuyến trực tiếp trên Internet. Muốn host private truy cập Internet, thường cần NAT tại router/firewall biên.

| Dải private IPv4 | CIDR | Ghi chú |
| --- | --- | --- |
| 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 | Dải lớn, hay dùng trong doanh nghiệp lớn. |
| 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 | Dải trung bình, hay dùng trong hệ thống nội bộ/VPN. |

## 2. NAT hoạt động như thế nào?

Khi host 192.168.10.10 gửi gói tin ra Internet, gói tin đi tới NAT router. Router thay địa chỉ nguồn private bằng địa chỉ public đại diện, ví dụ 209.165.200.226, rồi gửi ra ngoài.

Khi web server trả lời, NAT router tra bảng NAT translation để biết public IP/port đó đang đại diện cho host private nào, sau đó đổi ngược địa chỉ và chuyển gói tin về đúng máy bên trong.

## 3. Ba kiểu NAT

| Kiểu NAT | Cách hoạt động | Ưu điểm | Hạn chế |
| --- | --- | --- | --- |
| Static NAT | Một IP private ánh xạ cố định với một IP public. | Dễ truy cập từ ngoài vào, phù hợp server nội bộ cần publish. | Tốn public IP, không tiết kiệm địa chỉ. |
| Dynamic NAT | Private IP được mượn IP public từ một pool. | Linh hoạt hơn static NAT. | Pool hết thì host khác phải chờ; ngoài Internet không tự ping ngược vào host chưa có mapping. |
| PAT / NAT Overload | Nhiều host dùng chung một public IP, phân biệt bằng port. | Tiết kiệm public IP nhất, dùng phổ biến nhất. | Kết nối từ ngoài vào cần port forwarding/static mapping nếu muốn publish dịch vụ. |

## 4. Lab Static NAT

Static NAT dùng khi muốn ánh xạ cố định một server nội bộ ra một địa chỉ public. Trong demo, server 192.168.10.254 được ánh xạ thành 209.165.200.10.

! Cấu hình IP và đánh dấu vùng NAT interface g0/0 ip address 192.168.10.1 255.255.255.0 ip nat inside no shutdown interface g0/1 ip address 209.165.200.1 255.255.255.252 ip nat outside no shutdown ! Static NAT 1-1 ip...

## 5. Lab Dynamic NAT

Dynamic NAT dùng NAT pool. Trong demo, nhiều host private cùng muốn ra ngoài nhưng chỉ có một pool public nhỏ, ví dụ 209.165.200.9 đến 209.165.200.10. Vì pool chỉ có 2 địa chỉ nên tại một thời điểm chỉ có 2 host được...

! Định nghĩa pool địa chỉ public ip nat pool DYNAMIC_NAT 209.165.200.9 209.165.200.10 netmask 255.255.255.252 ! ACL chỉ ra mạng inside nào được NAT access-list 1 permit 192.168.10.0 0.0.0.255 ! Ghép ACL với NAT pool i...

## 6. Lab PAT / NAT Overload

PAT là cơ chế phổ biến nhất: rất nhiều IP private dùng chung một IP public. Router phân biệt từng phiên bằng số port. Trong Cisco IOS, PAT thường được cấu hình bằng từ khóa overload.

! ACL cho phép toàn bộ mạng inside được NAT access-list 1 permit 192.168.10.0 0.0.0.255 ! PAT: dùng địa chỉ của interface ngoài, phân biệt bằng port ip nat inside source list 1 interface g0/1 overload interface g0/0 i...

Nếu lệnh dùng pool thì viết: ip nat inside source list 1 pool <POOL_NAME>. Nếu dùng chung IP của interface ngoài thì viết: ip nat inside source list 1 interface g0/1 overload.

## 7. Checklist debug NAT trong Packet Tracer

| Lỗi thường gặp | Cách kiểm tra/sửa |
| --- | --- |
| Quên đánh dấu inside/outside | Vào đúng interface: ip nat inside ở LAN, ip nat outside ở phía Internet. |
| ACL không match mạng inside | show access-lists; kiểm tra wildcard 0.0.0.255 cho /24. |
| NAT pool sai địa chỉ hoặc sai netmask | Kiểm tra first IP, last IP và netmask của pool. |
| Outside PC không ping được vào dynamic/PAT | Bình thường: dynamic/PAT không cho ngoài tự khởi tạo phiên vào trong nếu không có mapping/port forwarding. |
| Bảng NAT còn mapping cũ | show ip nat translations; dùng clear ip nat translation * khi test lại. |
| Thiếu route quay về trong mô hình phức tạp | Kiểm tra default route/static route/OSPF để gói trả lời về được NAT router. |

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

| Nguồn video | https://www.youtube.com/watch?v=Qw43NpRGV3Q |
| --- | --- |
| Dạng nội dung | Transcript bài giảng + thực hành Packet Tracer |
| Trọng tâm | NAT IPv4, private/public IP, NAT translation table, Static/Dynamic/PAT |
| Mục tiêu | Hiểu NAT và tự cấu hình NAT cơ bản trên router Cisco |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | NAT IPv4 |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. NAT IPv4 giải quyết vấn đề gì trong mạng?
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
| NAT | Chuyển đổi địa chỉ | Dịch private IP sang public IP khi ra ngoài. |
| PAT | NAT overload | Nhiều host dùng chung một public IP bằng port. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 NAT IPv4 nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

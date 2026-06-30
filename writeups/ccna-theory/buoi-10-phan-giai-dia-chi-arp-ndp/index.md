---
layout: page-toc
title: "Buổi 10: ARP và NDP"
permalink: /writeups/ccna-theory/buoi-10-phan-giai-dia-chi-arp-ndp/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# ARP và NDP

## Mục tiêu học tập

- Nắm vai trò của ARP và NDP trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

PHÂN GIẢI ĐỊA CHỈ: ARP VÀ IPv6 NEIGHBOR DISCOVERY

Tài liệu học tập chuẩn giáo trình - dùng để ôn thi và thực hành

| --- | --- |
| Buổi số | 10 |
| Ngày | Không nêu trong transcript |
| Link video | https://www.youtube.com/watch?v=7IFgoV6ZSoo |

Ghi chú biên soạn

## 2. Tài liệu tham khảo

Sau buổi học này, sinh viên sẽ:

Phân biệt được vai trò của địa chỉ IP và địa chỉ MAC trong quá trình truyền dữ liệu.

Giải thích được khái niệm phân giải địa chỉ (Address Resolution) trong mạng máy tính.

Mô tả được cách ARP hoạt động trong IPv4 thông qua ARP Request, ARP Reply và ARP Cache.

Hiểu vì sao khi gửi dữ liệu ra ngoài LAN, máy tính chỉ cần biết MAC của Default Gateway chứ không biết MAC của máy đích ở xa.

Nhận diện được các điểm yếu cơ bản của ARP như ARP Spoofing/ARP Poisoning và broadcast overhead.

## 3. Ôn lại mô hình OSI/TCP/IP và vị trí của bài học

Khái niệm chính

Trong mô hình OSI, tầng Network chịu trách nhiệm định tuyến và sử dụng địa chỉ IP, còn tầng Data Link/Physical liên quan đến truyền frame trên môi trường vật lý. Trong mô hình TCP/IP, Data Link và Physical thường được...

Các mô hình mạng có thể chia tầng khác nhau, nhưng nguyên tắc chung vẫn là: dữ liệu đi từ lớp trên xuống lớp dưới để đóng gói, rồi đi qua mạng và được mở gói ở đầu nhận.

Ví dụ thực tế

Khi máy A gửi dữ liệu cho máy B, tầng Network dùng địa chỉ IP để biết đích logic, còn tầng Data Link cần địa chỉ MAC để gửi frame trong đoạn mạng hiện tại.

Cần nhớ

## 4. Địa chỉ MAC và địa chỉ IP

Khái niệm chính

Địa chỉ MAC (Media Access Control Address) là địa chỉ vật lý của card mạng, dùng để định danh giao diện mạng trong phạm vi liên kết cục bộ. Địa chỉ IP (Internet Protocol Address) là địa chỉ logic của thiết bị trong mô...

Ví dụ thực tế

Laptop của bạn ở nhà có thể nhận IP 192.168.1.107. Khi sang trường, laptop có thể nhận IP khác, nhưng MAC của card Wi-Fi vẫn là địa chỉ vật lý của chính card đó.

Cần nhớ

- MAC dùng trong cùng một mạng LAN hoặc cùng một liên kết cục bộ.

## 5. Vì sao cần phân giải địa chỉ?

Khái niệm chính

Phân giải địa chỉ (Address Resolution) là quá trình tìm địa chỉ lớp liên kết dữ liệu, thường là MAC address, tương ứng với một địa chỉ lớp mạng, thường là IPv4 hoặc IPv6.

Máy tính biết IP đích nhưng chưa biết phải đặt MAC đích trong Ethernet frame là gì. Vì vậy nó phải “hỏi” trong mạng: ai đang sở hữu IP này, hãy cho tôi biết MAC của bạn.

Ví dụ thực tế

Khi ping 192.168.1.104 trong cùng LAN, máy gửi chưa biết MAC của 192.168.1.104 nên phải dùng ARP để hỏi và sau đó lưu kết quả vào bảng ARP.

Cần nhớ

## 6. ARP trong IPv4: ARP Request, ARP Reply và ARP Cache

Khái niệm chính

ARP (Address Resolution Protocol) là giao thức dùng trong IPv4 để tìm địa chỉ MAC tương ứng với một địa chỉ IPv4 trong cùng mạng cục bộ. Kết quả thường được lưu tạm trong ARP Cache/ARP Table.

ARP hoạt động như một câu hỏi trong xóm: “Ai có IP 192.168.1.104 thì cho tôi biết MAC của bạn”. Máy có IP đó trả lời lại và máy hỏi ghi nhớ kết quả.

Ví dụ thực tế

Trên Windows, lệnh arp -a hiển thị các ánh xạ IPv4 - MAC đã học được. Sau khi ping một máy trong LAN, địa chỉ đó có thể xuất hiện trong bảng ARP với cột Internet Address và Physical Address.

Cần nhớ

## 7. Gửi dữ liệu đến mạng ở xa và vai trò của Default Gateway

Khái niệm chính

Default Gateway là thiết bị định tuyến mặc định mà host gửi gói tin tới khi địa chỉ IP đích không nằm trong cùng mạng cục bộ. Trong trường hợp này, host chỉ cần phân giải MAC của gateway, không cần biết MAC của máy đí...

Nếu muốn đi xa và không biết đường, bạn ra “cổng chính” hoặc “sân bay” trước. Máy tính cũng vậy: nếu đích nằm ngoài LAN, nó giao frame cho router/gateway xử lý tiếp.

Ví dụ thực tế

Khi ping 8.8.8.8 hoặc một địa chỉ public trên Internet, bảng ARP của máy tính không lưu MAC của 8.8.8.8. Máy chỉ lưu MAC của gateway, ví dụ 192.168.1.1.

Cần nhớ

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
| Buổi số | 10 |
| Ngày | Không nêu trong transcript |
| Link video | https://www.youtube.com/watch?v=7IFgoV6ZSoo |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | ARP và NDP |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. ARP và NDP giải quyết vấn đề gì trong mạng?
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
| ARP và NDP | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 ARP và NDP nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

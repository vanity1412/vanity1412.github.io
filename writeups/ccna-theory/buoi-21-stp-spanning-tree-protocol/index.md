---
layout: page-toc
title: "Buổi 21: STP"
permalink: /writeups/ccna-theory/buoi-21-stp-spanning-tree-protocol/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# STP

## Mục tiêu học tập

- Nắm vai trò của STP trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP CCNA

Chống loop Layer 2, Root Bridge, BPDU, PortFast, BPDU Guard và phân tích cổng bị block

| Nguồn bài giảng | Nguồn bài giảng |
| --- | --- |
| Video | https://www.youtube.com/watch?v=j5tqelbUxZw |
| Phạm vi | STP, loop Layer 2, broadcast storm, BPDU, Root Bridge, Root Port, Designated Port, Blocking Port, PortFast và BPDU Guard. |
| Ghi chú | Tìm kiếm Glasp theo yêu cầu nhưng không tìm thấy insight trực tiếp đủ phù hợp; tài liệu dưới đây được biên soạn từ transcript người học cung cấp. |

## 2. Vì sao cần STP trong mạng switch?

Một mạng tin cậy cần có khả năng dự phòng. Nếu chỉ có một đường duy nhất giữa các switch, khi đường đó lỗi thì toàn bộ luồng dữ liệu có thể bị gián đoạn. Vì vậy, trong thực tế người ta thường thiết kế nhiều đường kết...

Tuy nhiên, nhiều đường kết nối giữa các switch lại tạo ra nguy cơ loop Layer 2. Khác với IP ở Layer 3 có TTL để giới hạn thời gian sống của packet, frame Ethernet ở Layer 2 không có cơ chế TTL tương tự. Nếu bị loop, f...

| Yếu tố mạng tin cậy | Ý nghĩa | Liên quan đến STP |
| --- | --- | --- |
| Dự phòng | Có nhiều đường thay thế khi một đường lỗi | STP cho phép dự phòng nhưng tránh loop |
| Khả năng mở rộng | Mạng có thể tăng thêm switch, VLAN, người dùng | Mạng càng lớn càng cần kiểm soát loop |
| An toàn thông tin | Tránh thiết kế làm lộ hoặc làm sập mạng | Loop có thể gây gián đoạn dịch vụ nghiêm trọng |
| QoS / hiệu năng | Đảm bảo chất lượng truyền dữ liệu | Broadcast storm làm nghẽn mạng và giảm hiệu năng |

## 3. Loop Layer 2 và broadcast storm

Loop là tình huống dữ liệu đi vòng quanh mạng và không có điểm dừng rõ ràng. Trong mạng switch, khi switch chưa biết MAC đích, nó có thể flood frame ra các cổng còn lại. Nếu topology có vòng tròn, frame có thể quay lạ...

Switch flood unknown unicast hoặc broadcast ra các cổng còn lại, trừ cổng nhận vào.

Nếu có vòng kết nối giữa các switch, frame có thể quay lại điểm xuất phát.

Switch có thể học sai vị trí MAC trong CAM/MAC address table.

PC đích có thể nhận trùng một frame nhiều lần.

Mạng có thể bị tắc nghẽn vì lượng frame nhân bản tăng liên tục.

## 4. Cách STP chống loop bằng blocking port

STP không xóa đường dây vật lý. Nó chỉ đưa một số cổng vào trạng thái blocking ở mức logic. Nhờ vậy, mạng vẫn giữ được đường dự phòng. Khi đường chính gặp sự cố, STP có thể chuyển cổng dự phòng từ blocking sang forwar...

| Trạng thái logic | Ý nghĩa | Ví dụ trong bài |
| --- | --- | --- |
| Forwarding | Cổng được phép chuyển frame | Đường chính từ PC1 đến PC2 đi qua các switch đang forwarding |
| Blocking | Cổng không chuyển frame dữ liệu để tránh loop | Một link trong tam giác switch bị block |
| Dự phòng | Đường chưa dùng nhưng có thể kích hoạt khi link khác lỗi | Nếu link S1-S2 lỗi, cổng bị block có thể mở lại |

## 5. BPDU và quy trình bầu Root Bridge

Các switch trao đổi bản tin BPDU để bầu ra Root Bridge. Ban đầu, mỗi switch có thể tự xem mình là root. Sau khi trao đổi BPDU, switch nào có Bridge ID thấp nhất sẽ trở thành Root Bridge.

| Thành phần | Ý nghĩa | Ghi chú học tập |
| --- | --- | --- |
| Extended System ID | Liên quan VLAN ID | Dùng khi STP chạy theo từng VLAN. |
| MAC Address | Địa chỉ MAC đại diện của switch/VLAN | Nếu priority bằng nhau, MAC thấp hơn sẽ thắng. |
| Bridge ID | Tổng hợp các giá trị trên | Bridge ID thấp nhất trở thành Root Bridge. |

Trong bài giảng, giảng viên nhấn mạnh không nên chỉ nhìn MAC của từng cổng vật lý một cách vội vàng. Khi phân tích Root Bridge, cần xem Bridge ID/MAC đại diện trong output của STP, thường nằm trong phần thông tin VLAN...

## 6. Root Port, Designated Port và Blocking Port

Sau khi xác định Root Bridge, STP tiếp tục xác định vai trò của từng cổng. Mục tiêu là giữ lại đường tốt nhất về Root Bridge và block các đường còn lại để tránh loop.

| Khái niệm | Cách hiểu | Quy tắc nhanh |
| --- | --- | --- |
| Root Bridge | Switch trung tâm của cây STP | Bridge ID thấp nhất |
| Root Port | Cổng trên non-root switch đi về Root Bridge tốt nhất | Gần Root nhất / cost tốt nhất |
| Designated Port | Cổng đại diện cho một segment | Trên Root Bridge, các cổng thường là Designated Port |
| Blocking / Alternate Port | Cổng bị chặn để tránh loop | Đường kém ưu tiên hơn sẽ bị block |

## 7. PortFast và BPDU Guard

Trong Packet Tracer, khi cắm PC vào switch, cổng thường mất một khoảng thời gian mới chuyển sang màu xanh vì STP phải trải qua các bước kiểm tra/học. Với cổng nối trực tiếp đến PC, có thể dùng PortFast để cổng chuyển...

BPDU Guard dùng để bảo vệ cổng access. Nếu một cổng được xem là cổng nối PC nhưng lại nhận BPDU từ một switch lạ, điều đó có thể gây loop hoặc phá hoại topology. BPDU Guard giúp ngăn tình huống này.

| Tính năng | Dùng ở đâu? | Ý nghĩa |
| --- | --- | --- |
| PortFast | Cổng access nối PC, printer, server đơn lẻ | Giúp cổng lên forwarding nhanh, không phải chờ lâu |
| BPDU Guard | Cổng access không mong muốn nhận BPDU | Bảo vệ khi có switch lạ cắm vào cổng người dùng |
| Không nên dùng PortFast trên trunk giữa switch | Link switch-switch | Có thể gây loop nếu dùng sai |

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

| Nguồn bài giảng | Nguồn bài giảng |
| --- | --- |
| Video | https://www.youtube.com/watch?v=j5tqelbUxZw |
| Phạm vi | STP, loop Layer 2, broadcast storm, BPDU, Root Bridge, Root Port, Designated Port, Blocking Port, PortFast và BPDU Guard. |
| Ghi chú | Tìm kiếm Glasp theo yêu cầu nhưng không tìm thấy insight trực tiếp đủ phù hợp; tài liệu dưới đây được biên soạn từ transcript người học cung cấp. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | STP |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. STP giải quyết vấn đề gì trong mạng?
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
| STP | Spanning Tree Protocol | Ngăn loop Layer 2 bằng cách blocking một số port. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 STP nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

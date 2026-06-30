---
layout: page-toc
title: "Buổi 22: STP Tuning và EtherChannel"
permalink: /writeups/ccna-theory/buoi-22-stp-tuning-etherchannel/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# STP Tuning và EtherChannel

## Mục tiêu học tập

- Nắm vai trò của STP Tuning và EtherChannel trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP CCNA

Port priority, Root Bridge tuning, Rapid STP, EtherChannel, PAgP/LACP và Port-Channel

| Thông tin bài học | Thông tin bài học |
| --- | --- |
| Nguồn video | https://www.youtube.com/watch?v=fcs-i3QASEA |
| Chủ đề chính | Ôn STP nâng cao, tinh chỉnh Root Bridge/Port Priority, chuyển Rapid STP, cấu hình EtherChannel bằng LACP/PAgP và tạo Port-Channel trunk. |
| Kết quả cần đạt | Hiểu cách điều khiển đường đi trong STP và biết gộp nhiều link vật lý giữa switch thành một link logic để tăng băng thông, tránh bị STP block lãng phí. |

## 2. MỤC LỤC TÓM TẮT

- 1. Mục tiêu học tập

- 2. Tổng quan nhanh toàn buổi

- 4. Bảng lệnh cấu hình cần nhớ

- 5. Quy trình lab Packet Tracer

- 6. Kiến thức trọng tâm cần nhớ

- 7. Câu hỏi ôn tập và bài tập về nhà

## 3. Tổng quan nhanh toàn buổi

Buổi học mở đầu bằng việc nhắc lại phần STP của buổi trước. Sau khi bầu được Root Bridge, các switch còn lại phải chọn Root Port, tức là cổng có đường đi tốt nhất về Root Bridge. Nếu hai đường có Root Path Cost bằng n...

Port ID thường tương ứng với số cổng như Fa0/1, Fa0/2. Khi các tiêu chí trước đều bằng nhau, cổng có Port ID nhỏ hơn thường được ưu tiên forwarding; cổng còn lại bị block/alternate.

Giảng viên giới thiệu rằng STP không chỉ có một dạng duy nhất. Có nhiều biến thể như STP, PVST+, RSTP, Rapid PVST+ và MSTP. Trong đó, chữ Rapid thể hiện khả năng hội tụ nhanh hơn, giúp cổng chuyển trạng thái nhanh hơn...

| Phiên bản | Ý nghĩa ngắn gọn | Điểm cần nhớ |
| --- | --- | --- |
| STP / 802.1D | Bản STP truyền thống | Hội tụ chậm hơn, thường phải chờ port chuyển trạng thái. |
| PVST+ | Per-VLAN Spanning Tree | Mỗi VLAN có thể có một cây STP riêng. |

## 4. Bảng lệnh cấu hình cần nhớ

| Mục đích | Lệnh mẫu | Ghi chú |
| --- | --- | --- |
| Chuyển sang Rapid PVST+ | spanning-tree mode rapid-pvst | Giúp hội tụ nhanh hơn STP thường. |
| Đặt Root Bridge ưu tiên | spanning-tree vlan 1 priority 4096 | Priority thấp hơn sẽ ưu tiên làm Root Bridge. |
| Kiểm tra STP | show spanning-tree | Xem Root ID, Bridge ID, role/state của port. |
| Chọn dải cổng | interface range fa0/1 - 4 | Dùng khi cấu hình nhiều cổng cùng lúc. |
| Tạo EtherChannel LACP | channel-group 1 mode active | Mode active dùng với LACP. |
| Vào Port-Channel | interface port-channel 1 | Cổng logic đại diện nhóm link. |
| Đặt trunk cho Port-Channel | switchport mode trunk | Dùng khi nhiều VLAN đi qua link giữa switch. |
| Kiểm tra EtherChannel | show etherchannel summary | Xem Port-Channel đã lên chưa. |

## 5. Lab STP tuning

- Vẽ mô hình nhiều switch có đường dự phòng.

- Dùng show spanning-tree để xác định Root Bridge mặc định.

- Đổi priority của switch muốn làm Root Bridge.

- Quan sát port nào chuyển forwarding/blocking.

- Thay đổi priority của switch lân cận để điều khiển đường đi.

- Gửi PDU giữa hai PC để kiểm tra đường đi trong Simulation Mode.

## 6. Lab EtherChannel

- Kết nối hai switch bằng nhiều dây vật lý, ví dụ Fa0/1 đến Fa0/4.

- Đảm bảo hai đầu có cấu hình tương đồng: speed, duplex, access/trunk, VLAN.

- Dùng interface range để chọn đồng thời các cổng.

- Dùng channel-group 1 mode active để gộp bằng LACP.

- Vào interface port-channel 1 và cấu hình trunk nếu cần nhiều VLAN đi qua.

- Dùng show etherchannel summary để xác nhận Port-Channel hoạt động.

## 7. Kiến thức trọng tâm cần nhớ

| Khái niệm | Cách hiểu nhanh |
| --- | --- |
| Root Bridge | Switch trung tâm trong cây STP, có Bridge ID thấp nhất. |
| Root Port | Cổng tốt nhất từ switch non-root đi về Root Bridge. |
| Designated Port | Cổng đại diện forwarding trên một segment. |
| Blocking/Alternate Port | Cổng bị chặn logic để tránh loop. |
| Rapid STP | Phiên bản STP hội tụ nhanh hơn. |
| EtherChannel | Kỹ thuật gộp nhiều link vật lý thành một link logic. |
| Port-Channel | Interface logic đại diện cho nhóm EtherChannel. |
| LACP | Chuẩn mở dùng để thương lượng EtherChannel. |

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

| Thông tin bài học | Thông tin bài học |
| --- | --- |
| Nguồn video | https://www.youtube.com/watch?v=fcs-i3QASEA |
| Chủ đề chính | Ôn STP nâng cao, tinh chỉnh Root Bridge/Port Priority, chuyển Rapid STP, cấu hình EtherChannel bằng LACP/PAgP và tạo Port-Channel trunk. |
| Kết quả cần đạt | Hiểu cách điều khiển đường đi trong STP và biết gộp nhiều link vật lý giữa switch thành một link logic để tăng băng thông, tránh bị STP block lãng phí. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | STP Tuning và EtherChannel |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. STP Tuning và EtherChannel giải quyết vấn đề gì trong mạng?
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
| EtherChannel | Gộp đường uplink | Gộp nhiều link vật lý thành một link logic. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 STP Tuning và EtherChannel nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

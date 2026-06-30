---
layout: page-toc
title: "Buổi 24: FHRP và HSRP"
permalink: /writeups/ccna-theory/buoi-24-fhrp-hsrp-default-gateway-redundancy/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# FHRP và HSRP

## Mục tiêu học tập

- Nắm vai trò của FHRP và HSRP trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Chủ đề: dự phòng default gateway, router ảo, Active/Standby Router, Virtual IP và lab HSRP trong Cisco Packet Tracer.

Nguồn video: https://www.youtube.com/watch?v=xk-iwp_bsJA

Hiểu vì sao mạng cần dự phòng default gateway, không chỉ dự phòng đường switch bằng STP/EtherChannel.

Nắm khái niệm First Hop Redundancy Protocols (FHRP) và cơ chế router ảo.

Hiểu HSRP hoạt động theo mô hình Active/Standby Router, dùng Virtual IP làm default gateway cho client.

Biết ý nghĩa các lệnh cấu hình HSRP: standby group, priority, virtual IP và preempt.

## 2. Vấn đề: single default gateway là điểm lỗi đơn

Trong mạng LAN thông thường, mỗi PC thường chỉ có một default gateway. Gateway này là địa chỉ IP của router hoặc multilayer switch giúp PC đi ra ngoài mạng nội bộ. Nếu gateway đó bị lỗi, client vẫn còn IP nhưng không...

Một mạng có nhiều switch dự phòng nhưng chỉ có một default gateway thật vẫn có rủi ro mất kết nối ở điểm gateway. FHRP được sinh ra để xử lý bài toán này.

## 3. First Hop Redundancy Protocols và HSRP

First Hop Redundancy Protocols (FHRP) là nhóm giao thức tạo dự phòng cho “hop đầu tiên” của client, tức default gateway. Trong bài này, giao thức được học là HSRP - Hot Standby Router Protocol.

| Khái niệm | Ý nghĩa |
| --- | --- |
| FHRP | Nhóm giao thức dự phòng default gateway cho host trong LAN. |
| HSRP | Giao thức dự phòng gateway của Cisco, hoạt động theo mô hình Active/Standby. |
| Virtual Router | Router ảo đại diện cho nhiều router thật. |
| Virtual IP (VIP) | IP ảo được client dùng làm default gateway. |
| Active Router | Router thật đang giữ VIP và forward traffic. |
| Standby Router | Router dự phòng, theo dõi Active bằng hello message và tiếp quản khi Active lỗi. |

## 4. Cơ chế hoạt động của HSRP

HSRP làm cho nhiều router thật xuất hiện như một gateway duy nhất đối với client. Các router trong cùng HSRP group chia sẻ một Virtual IP. Router có priority cao hơn thường được chọn làm Active. Router còn lại ở trạng...

| Thành phần | Vai trò trong HSRP |
| --- | --- |
| Group number | Mã nhóm HSRP. Hai router cùng dự phòng cho một phân đoạn phải dùng cùng group. |
| Priority | Độ ưu tiên bầu Active Router. Giá trị cao hơn thường thắng. |
| Preempt | Cho phép router có priority cao hơn giành lại vai trò Active sau khi phục hồi. |
| Hello/Hold timer | Cơ chế router kiểm tra nhau còn sống hay không. |
| Virtual MAC | MAC ảo gắn với Virtual IP để client ARP đến gateway ổn định. |

## 5. Mẫu lab trong buổi học

Lab được xây theo ý tưởng: phía LAN có nhiều PC đi qua switch; phía gateway có hai router R0 và R1; phía trên là mạng server/ISP. PC không trỏ gateway về IP thật của R0 hoặc R1 nữa, mà trỏ về Virtual IP của HSRP.

| Phân đoạn | IP thật / IP ảo trong transcript |
| --- | --- |
| LAN client | 192.168.1.0/24 |
| R0 phía LAN | 192.168.1.100 (ví dụ trong bài) |
| R1 phía LAN | 192.168.1.200 (ví dụ trong bài) |
| Virtual IP LAN | 192.168.1.254 - dùng làm default gateway cho PC |
| Mạng server/upstream | 200.200.200.0/24 |
| Virtual IP upstream | 200.200.200.200 |

## 6. Cấu hình HSRP cơ bản

Trong bài, giảng viên dùng ba lệnh chính trên interface tham gia HSRP: đặt priority, khai báo Virtual IP và bật preempt. Router có priority 150 được ưu tiên làm Active; router còn lại dùng priority thấp hơn để làm Sta...

## 7. Cấu hình trên R0 - router ưu tiên Active

enable configure terminal hostname R0 ! interface g0/0 standby 1 priority 150 standby 1 ip 192.168.1.254 standby 1 preempt ! interface g0/1 standby 2 priority 150 standby 2 ip 200.200.200.200 standby 2 preempt end wri...

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

| Khái niệm | Ý nghĩa |
| --- | --- |
| FHRP | Nhóm giao thức dự phòng default gateway cho host trong LAN. |
| HSRP | Giao thức dự phòng gateway của Cisco, hoạt động theo mô hình Active/Standby. |
| Virtual Router | Router ảo đại diện cho nhiều router thật. |
| Virtual IP (VIP) | IP ảo được client dùng làm default gateway. |
| Active Router | Router thật đang giữ VIP và forward traffic. |
| Standby Router | Router dự phòng, theo dõi Active bằng hello message và tiếp quản khi Active lỗi. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | FHRP và HSRP |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. FHRP và HSRP giải quyết vấn đề gì trong mạng?
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
| HSRP | Dự phòng gateway | Tạo virtual gateway để tăng tính sẵn sàng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 FHRP và HSRP nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

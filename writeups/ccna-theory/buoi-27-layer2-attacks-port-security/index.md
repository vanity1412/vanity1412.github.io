---
layout: page-toc
title: "Buổi 27: Layer 2 Attacks và Port Security"
permalink: /writeups/ccna-theory/buoi-27-layer2-attacks-port-security/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Layer 2 Attacks và Port Security

## Mục tiêu học tập

- Nắm vai trò của Layer 2 Attacks và Port Security trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

LAN Security: Layer 2 Attacks và Port Security

Nguồn: Transcript YouTube - https://www.youtube.com/watch?v=WhEmG4b9BIc

## 2. Vì sao phải bảo mật Layer 2?

Trong LAN, switch hoạt động chủ yếu ở Layer 2. Nếu chỉ cắm switch, router và PC rồi cho chạy, mạng mới đạt mức “kết nối được”, nhưng chưa chắc an toàn. Nhiều tấn công khai thác chính cơ chế học MAC, trunk VLAN, DHCP b...

## 3. MAC Address Table Attack / CAM Table Overflow

| Mục | Ghi chú |
| --- | --- |
| Dấu hiệu | Switch flood bất thường, lưu lượng broadcast/unknown unicast tăng, nhiều MAC lạ xuất hiện nhanh trên cùng một cổng. |
| Rủi ro | Gây nghẽn mạng, làm lộ traffic cho máy đang sniffing, giảm hiệu năng switch. |
| Giảm thiểu | Bật Port Security, giới hạn số MAC trên access port, tắt port không dùng, giám sát bảng MAC. |

## 4. VLAN Hopping và Double Tagging

VLAN hopping là kỹ thuật làm traffic từ một VLAN có thể “nhảy” sang VLAN khác mà không đi qua thiết bị định tuyến hợp lệ. Có hai ý chính được nhắc trong buổi học: lợi dụng DTP/auto trunking và double tagging.

| Dạng | Giải thích |
| --- | --- |
| DTP spoofing | Attacker giả như một switch, lợi dụng dynamic auto/dynamic desirable để tạo trunk với switch. |
| Double tagging | Frame có hai thẻ VLAN. Thẻ ngoài trùng native VLAN bị switch đầu tiên gỡ ra, thẻ trong còn lại có thể đưa frame sang VLAN mục tiêu. |
| Phòng thủ | Tắt auto trunking trên access port, cấu hình trunk thủ công khi cần, không dùng VLAN người dùng làm native VLAN, tránh dùng VLAN 1 cho user. |

## 5. DHCP Starvation và DHCP Spoofing

DHCP dùng quy trình DORA: Discover, Offer, Request, Acknowledge. Vì client ban đầu chưa có IP nên quá trình này phụ thuộc nhiều vào broadcast, vì vậy dễ bị lợi dụng trong LAN nếu access layer không được bảo vệ.

| Tấn công | Ý nghĩa |
| --- | --- |
| DHCP Starvation | Attacker giả nhiều MAC/client để xin hết địa chỉ trong DHCP pool. Client hợp lệ sau đó không còn IP để dùng. |
| DHCP Spoofing | Attacker dựng DHCP server giả, cấp sai default gateway/DNS/IP để làm gián đoạn hoặc chuyển hướng traffic. |
| Giảm thiểu | Port Security giúp giới hạn số MAC trên cổng; trong thực tế nên kết hợp DHCP Snooping, trusted/untrusted port. |

## 6. ARP Poisoning / ARP Spoofing

ARP được dùng khi một máy biết IP đích nhưng chưa biết MAC tương ứng. Máy gửi ARP Request toàn mạng, thiết bị có IP đó trả ARP Reply. Attacker có thể gửi ARP Reply giả để nạn nhân học sai bảng ARP.

ARP poisoning không nhất thiết đánh trực tiếp vào switch; nó thường đánh lừa endpoint để endpoint gửi dữ liệu nhầm MAC. Muốn phòng thủ tốt cần kết hợp nhiều lớp: Port Security, DHCP Snooping, Dynamic ARP Inspection, k...

## 7. Port Security là gì?

Port Security là cơ chế trên switch giúp kiểm soát thiết bị nào được phép xuất hiện trên một access port. Ta có thể giới hạn số lượng MAC, chỉ định MAC được phép, hoặc để switch tự học rồi khóa lại.

| Khái niệm | Giải thích |
| --- | --- |
| Access port | Cổng nối xuống PC/printer/AP/user device. Port Security nên áp dụng ở đây. |
| Secure MAC | MAC được phép hoạt động trên cổng. |
| Maximum | Số MAC tối đa được phép học trên cổng. Mặc định thường là 1. |
| Violation | Hành động khi MAC lạ hoặc vượt quá maximum xuất hiện. |
| Sticky MAC | Switch tự học MAC rồi ghi vào running-config để quản trị viên có thể lưu lại. |

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

| Mục | Ghi chú |
| --- | --- |
| Dấu hiệu | Switch flood bất thường, lưu lượng broadcast/unknown unicast tăng, nhiều MAC lạ xuất hiện nhanh trên cùng một cổng. |
| Rủi ro | Gây nghẽn mạng, làm lộ traffic cho máy đang sniffing, giảm hiệu năng switch. |
| Giảm thiểu | Bật Port Security, giới hạn số MAC trên access port, tắt port không dùng, giám sát bảng MAC. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Layer 2 Attacks và Port Security |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Layer 2 Attacks và Port Security giải quyết vấn đề gì trong mạng?
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

🔑 Layer 2 Attacks và Port Security nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

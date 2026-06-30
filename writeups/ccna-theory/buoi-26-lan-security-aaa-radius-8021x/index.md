---
layout: page-toc
title: "Buổi 26: LAN Security, AAA và 802.1X"
permalink: /writeups/ccna-theory/buoi-26-lan-security-aaa-radius-8021x/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# LAN Security, AAA và 802.1X

## Mục tiêu học tập

- Nắm vai trò của LAN Security, AAA và 802.1X trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Endpoint Security, Network Security Device, Local Authentication, AAA, RADIUS Server và 802.1X

Nguồn video: https://www.youtube.com/watch?v=fguDBZ09i_U

## 2. Buổi học chuyển từ nhóm chủ đề tính sẵn sàng của mạng sang chủ đề bảo mật mạng LAN.

Mạng LAN ban đầu chỉ cần switch/router để hoạt động; nhưng để vận hành thực tế cần kiểm soát rủi ro, truy cập và điểm cuối.

Các mối đe dọa được nhắc đến gồm DDoS, data breach, malware/ransomware như WannaCry.

Các lớp bảo vệ gồm firewall/NGFW, VPN, NAC, endpoint protection, email security appliance.

## 3. Phần trọng tâm là AAA: Authentication, Authorization, Accounting.

Thực hành gồm hai hướng: xác thực local bằng username/password trên router và xác thực tập trung qua AAA/RADIUS Server.

Cuối buổi có thử nghiệm lab RADIUS trong Packet Tracer nhưng gặp lỗi đăng nhập, giáo viên hẹn sửa và gửi lại bài mẫu.

## 4. Vì sao phải bảo mật mạng LAN?

Một mạng LAN chỉ có switch, router và PC hoạt động được mới chỉ đạt mức kết nối cơ bản. Khi đi vào vận hành thực tế, mạng cần thêm các cơ chế kiểm soát truy cập, bảo vệ điểm cuối, kiểm toán hoạt động và ngăn truy cập...

| Mối đe dọa | Ý nghĩa | Tác động |
| --- | --- | --- |
| DDoS | Tấn công từ chối dịch vụ phân tán, làm hệ thống không phục vụ được người dùng. | Gián đoạn dịch vụ, mất uy tín, ảnh hưởng kinh doanh. |
| Data Breach | Dữ liệu nội bộ hoặc thông tin bí mật bị truy cập/đánh cắp. | Lộ thông tin, mất an toàn dữ liệu, thiệt hại pháp lý. |
| Malware/Ransomware | Mã độc lây vào endpoint, có thể mã hóa dữ liệu và đòi tiền chuộc. | Mất dữ liệu, dừng vận hành, phải khôi phục hệ thống. |

Bảo mật mạng LAN không chỉ là cài antivirus. Nó là tổng hợp của nhiều lớp: endpoint, firewall, VPN, NAC, AAA, logging và chính sách vận hành.

## 5. Các nhóm giải pháp bảo vệ mạng

| Giải pháp | Mục đích | Ví dụ trong bài |
| --- | --- | --- |
| Network Security Device | Bảo vệ biên mạng, lọc truy cập, phát hiện/ngăn tấn công. | Firewall, Next-Generation Firewall, IDS/IPS. |
| VPN | Tạo kết nối mã hóa giữa các chi nhánh hoặc người dùng từ xa. | Kết nối văn phòng Hà Nội - Đà Nẵng - Sài Gòn. |
| NAC | Kiểm soát ai/thiết bị nào được phép truy cập mạng. | Xác thực người dùng, cấp quyền, kiểm toán. |
| Endpoint Protection | Bảo vệ máy tính người dùng/server khỏi mã độc và rủi ro điểm cuối. | Anti-malware, EDR, endpoint security. |
| Email Security | Bảo vệ hệ thống email khỏi spam, phishing, malware. | Cisco Email Security Appliance. |

## 6. Access Control và xác thực local trên thiết bị mạng

Trong các bài trước, khi cấu hình SSH/Telnet hoặc line VTY, ta thường dùng username/password cục bộ trên router hoặc switch. Đây là cách xác thực local: tài khoản được lưu ngay trên thiết bị.

| Ưu điểm của local | Hạn chế của local |
| --- | --- |
| Dễ cấu hình, phù hợp lab nhỏ. | Mỗi thiết bị phải tạo user riêng, khó mở rộng. |
| Không cần server ngoài. | Khi đổi mật khẩu phải đổi trên từng router/switch. |
| Có thể dùng làm phương án dự phòng. | Khó audit tập trung ai đã đăng nhập, làm gì, lúc nào. |

## 7. AAA - Authentication, Authorization, Accounting

| Thành phần | Câu hỏi cần trả lời | Ví dụ |
| --- | --- | --- |
| Authentication | Bạn là ai? | Nhập username/password để đăng nhập router. |
| Authorization | Bạn được phép làm gì? | User chỉ được xem cấu hình hay được vào privileged mode. |
| Accounting | Bạn đã làm gì? | Ghi nhận thời gian đăng nhập, lệnh đã chạy, hành động cấu hình. |

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

| Mối đe dọa | Ý nghĩa | Tác động |
| --- | --- | --- |
| DDoS | Tấn công từ chối dịch vụ phân tán, làm hệ thống không phục vụ được người dùng. | Gián đoạn dịch vụ, mất uy tín, ảnh hưởng kinh doanh. |
| Data Breach | Dữ liệu nội bộ hoặc thông tin bí mật bị truy cập/đánh cắp. | Lộ thông tin, mất an toàn dữ liệu, thiệt hại pháp lý. |
| Malware/Ransomware | Mã độc lây vào endpoint, có thể mã hóa dữ liệu và đòi tiền chuộc. | Mất dữ liệu, dừng vận hành, phải khôi phục hệ thống. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | LAN Security, AAA và 802.1X |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. LAN Security, AAA và 802.1X giải quyết vấn đề gì trong mạng?
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

🔑 LAN Security, AAA và 802.1X nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

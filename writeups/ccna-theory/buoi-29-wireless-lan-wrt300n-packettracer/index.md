---
layout: page-toc
title: "Buổi 29: Wireless LAN"
permalink: /writeups/ccna-theory/buoi-29-wireless-lan-wrt300n-packettracer/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Wireless LAN

## Mục tiêu học tập

- Nắm vai trò của Wireless LAN trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Tài liệu học tập tóm tắt từ transcript video — có giải thích dễ hiểu, sơ đồ, lệnh và checklist thực hành.

## 2. Kịch bản 1 — WRT300N hoạt động như switch không dây / Access Point

Trong kịch bản đầu tiên, WRT300N không đóng vai trò định tuyến mà chỉ giúp các laptop kết nối không dây vào cùng mạng LAN với PC có dây. Vì vậy, toàn bộ thiết bị vẫn nằm chung một broadcast domain và thường dùng chung...

| Việc cần làm | Ý nghĩa | Lưu ý dễ sai |
| --- | --- | --- |
| Kết nối switch 2960 với WRT300N qua cổng LAN/Ethernet | Đưa WRT300N vào cùng mạng Layer 2 | Không dùng nhầm cổng Internet/WAN nếu mục tiêu là AP mode. |
| Tắt DHCP Server trên WRT300N | Tránh có hai DHCP server cùng cấp IP | Nếu laptop nhận IP sai dải, kiểm tra lại DHCP trên WRT. |
| Gắn card Wi-Fi cho laptop/PC | Thiết bị mới có khả năng kết nối wireless | Trong Packet Tracer cần tắt máy, tháo module cũ, gắn card wireless rồi bật lại. |
| Cấu hình DHCP trên server thật | Tập trung cấp phát IP cho cả PC có dây và laptop Wi-Fi | Server có thể dùng 192.168.1.10, pool 192.168.1.0/24. |
| Xin lại IP trên client | Cập nhật IP sau khi tắt DHCP sai nguồn | Dùng DHCP trong Desktop hoặc lệnh ipconfig /renew. |

## 3. Cấu hình SSID và WPA2 Personal

Ban đầu mạng Wi-Fi có thể ở trạng thái open access, tức là laptop kết nối không cần mật khẩu. Trong mạng thật, cách này rất nguy hiểm vì ai ở gần vùng phủ sóng cũng có thể thử truy cập vào mạng. Vì vậy buổi học hướng...

| Bước | Thao tác trong Packet Tracer | Kết quả mong muốn |
| --- | --- | --- |
| 1 | Click WRT300N → tab Wireless | Mở phần cấu hình mạng không dây. |
| 2 | Đặt SSID, ví dụ Cisco | Laptop sẽ thấy tên mạng Cisco trong danh sách Wi-Fi. |
| 3 | Wireless Security → WPA2 Personal | Bật cơ chế bảo mật bằng mật khẩu. |
| 4 | Nhập passphrase, ví dụ 123456789, rồi Save Settings | WRT300N áp dụng cấu hình mới. |
| 5 | Laptop → Desktop → PC Wireless → Connect SSID và nhập key | Laptop kết nối Wi-Fi thành công và có thể xin DHCP/ping. |

## 4. Kịch bản 2 — WRT300N hoạt động như wireless router/NAT

Trong kịch bản thứ hai, WRT300N không còn chỉ là switch không dây nữa mà đóng vai trò router. Đường từ switch bên ngoài sẽ cắm vào cổng Internet/WAN của WRT300N, DHCP trên WRT được bật lại để cấp IP cho mạng Wi-Fi bên...

| Tiêu chí | AP/Switch mode | Router/NAT mode |
| --- | --- | --- |
| Cổng dùng để nối ra mạng ngoài | LAN/Ethernet port | Internet/WAN port |
| DHCP trên WRT300N | Tắt để tránh xung đột | Bật để cấp IP cho mạng Wi-Fi nội bộ |
| Quan hệ giữa các thiết bị | Cùng một LAN/subnet | Tách thành hai mạng khác nhau |
| Ping từ Wi-Fi ra mạng ngoài | Được nếu cùng mạng và DHCP đúng | Thường được nhờ NAT |
| Ping từ mạng ngoài vào laptop Wi-Fi | Được nếu cùng LAN | Thường không tự vào được do NAT/ẩn địa chỉ nội bộ |

## 5. Các thao tác cấu hình/lệnh cần nhớ

| Mục tiêu | Thao tác/lệnh | Ghi chú |
| --- | --- | --- |
| Xin lại IP trên PC/laptop | ipconfig /renew | Trong Command Prompt phải có khoảng trắng trước /renew. |
| Xem IP hiện tại | ipconfig | Dùng để kiểm tra client nhận đúng dải IP chưa. |
| Gắn card Wi-Fi | Physical → tắt nguồn → tháo card cũ → gắn module wireless → bật nguồn | Nếu không có card Wi-Fi thì laptop/PC không bắt được SSID. |
| Kết nối Wi-Fi | Desktop → PC Wireless → Connect → chọn SSID → nhập passphrase | Dùng cho laptop/PC trong Packet Tracer. |
| Tắt DHCP trên WRT | WRT300N → GUI/Config → DHCP Server: Disable → Save Settings | Dùng trong AP/Switch mode. |
| Bật DHCP trên WRT | DHCP Server: Enable → cấu hình dải cấp phát → Save Settings | Dùng trong Router/NAT mode. |
| Cấu hình WPA2 | Wireless → Wireless Security → WPA2 Personal → Passphrase | Bảo vệ mạng Wi-Fi khỏi truy cập tự do. |

## 6. Checklist troubleshoot Wireless Packet Tracer

| Triệu chứng | Nguyên nhân hay gặp | Cách xử lý |
| --- | --- | --- |
| Laptop không thấy Wi-Fi | Chưa gắn card Wi-Fi hoặc chưa bật thiết bị | Vào Physical, tắt nguồn, gắn wireless module, bật lại. |
| Laptop thấy SSID nhưng không vào được | Sai WPA2 passphrase hoặc profile cũ | Xóa/kết nối lại profile, nhập đúng key. |
| Nhận IP không đúng dải | WRT300N DHCP vẫn bật khi đang dùng AP mode | Disable DHCP trên WRT rồi ipconfig /renew. |
| PC có dây ping laptop không được | Đang ở router/NAT mode, hai mạng bị tách | Phân biệt yêu cầu bài: AP mode hay Router mode. |
| Lệnh renew báo lỗi | Gõ sai cú pháp | Gõ: ipconfig /renew, không viết liền. |
| Ping fail vài gói đầu | Thiết bị đang hội tụ/kết nối lại | Chờ vài giây rồi ping lại, kiểm tra đèn/link. |

## 7. Cần nhớ sau Buổi 29

WRT300N có thể dùng theo hai vai trò rất khác nhau: AP/switch không dây hoặc wireless router có NAT.

AP/switch mode: tắt DHCP trên WRT, nối bằng LAN port, client nhận IP từ DHCP Server chính và cùng subnet.

Router/NAT mode: dùng Internet/WAN port, bật DHCP trên WRT, mạng Wi-Fi bên trong tách khỏi mạng ngoài.

SSID là tên mạng Wi-Fi; WPA2 Personal là cơ chế bảo mật bằng mật khẩu phù hợp cho lab/gia đình.

Nếu có hai DHCP Server cùng hoạt động, client có thể nhận IP sai dải và làm bài không thông.

Trong Packet Tracer, lỗi phổ biến nhất là quên gắn wireless card, quên connect SSID, sai passphrase hoặc gõ sai ipconfig /renew.

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

| Việc cần làm | Ý nghĩa | Lưu ý dễ sai |
| --- | --- | --- |
| Kết nối switch 2960 với WRT300N qua cổng LAN/Ethernet | Đưa WRT300N vào cùng mạng Layer 2 | Không dùng nhầm cổng Internet/WAN nếu mục tiêu là AP mode. |
| Tắt DHCP Server trên WRT300N | Tránh có hai DHCP server cùng cấp IP | Nếu laptop nhận IP sai dải, kiểm tra lại DHCP trên WRT. |
| Gắn card Wi-Fi cho laptop/PC | Thiết bị mới có khả năng kết nối wireless | Trong Packet Tracer cần tắt máy, tháo module cũ, gắn card wireless rồi bật lại. |
| Cấu hình DHCP trên server thật | Tập trung cấp phát IP cho cả PC có dây và laptop Wi-Fi | Server có thể dùng 192.168.1.10, pool 192.168.1.0/24. |
| Xin lại IP trên client | Cập nhật IP sau khi tắt DHCP sai nguồn | Dùng DHCP trong Desktop hoặc lệnh ipconfig /renew. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Wireless LAN |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Wireless LAN giải quyết vấn đề gì trong mạng?
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
| Packet Tracer | Trình mô phỏng mạng | Dùng để dựng topology, cấu hình và kiểm tra lab CCNA. |
| WLAN | Mạng LAN không dây | Mạng dùng Wi-Fi thay cho cáp Ethernet. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Wireless LAN nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

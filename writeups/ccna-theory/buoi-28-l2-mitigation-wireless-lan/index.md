---
layout: page-toc
title: "Buổi 28: L2 Mitigation và Wireless LAN"
permalink: /writeups/ccna-theory/buoi-28-l2-mitigation-wireless-lan/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# L2 Mitigation và Wireless LAN

## Mục tiêu học tập

- Nắm vai trò của L2 Mitigation và Wireless LAN trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. GIẢM THIỂU TẤN CÔNG LAYER 2 & NỀN TẢNG WIRELESS LAN

Nguồn video: https://www.youtube.com/watch?v=BRMBdKVW31M

## 2. Tóm tắt nhanh theo mốc thời gian

| Mốc thời gian | Nội dung chính |
| --- | --- |
| 00:02 | Ôn lại Port Security: kiểm soát cổng switch, hạn chế thiết bị lạ cắm vào LAN và giảm nguy cơ thất thoát thông tin. |
| 01:57 | Giảm thiểu VLAN Hopping: tắt DTP, cấu hình trunk thủ công, không để cổng người dùng tự thương lượng trunk. |
| 02:23 | Ôn DHCP Starvation và DHCP Spoofing; dùng Port Security để giới hạn MAC/request và DHCP Snooping để chặn DHCP Server giả. |
| 05:00 | DHCP Snooping phân biệt trusted port và untrusted port; chỉ cổng nối đến DHCP Server hợp lệ mới được cấp phát DHCP. |
| 23:17 | Giới thiệu Dynamic ARP Inspection để giảm ARP spoofing/poisoning dựa trên kiểm tra ARP và binding table. |
| 25:20 | Giảm STP Attack bằng PortFast và BPDU Guard trên access port, tránh thiết bị người dùng gửi BPDU vào hệ thống switch. |
| 46:08 | Chuyển sang Wireless LAN: lợi ích của mạng không dây, các nhóm WPAN/WLAN/WMAN/WWAN và công nghệ Bluetooth, Wi-Fi, WiMAX, cellular. |
| 50:22 | Mạng Wi-Fi hoạt động trên sóng radio, phổ biến ở băng tần 2.4 GHz và 5 GHz; liên quan chuẩn IEEE 802.11 và Wi-Fi Alliance. |

## 3. Chống VLAN Hopping

VLAN Hopping xảy ra khi thiết bị tấn công cố giả làm switch hoặc lợi dụng native VLAN/double tagging để đi sang VLAN khác mà không cần định tuyến hợp lệ. Cách giảm thiểu là không để cổng người dùng tự động trở thành t...

| Việc cần làm | Lệnh/ý tưởng | Ghi nhớ |
| --- | --- | --- |
| Cổng người dùng luôn là access port | switchport mode access | Không để dynamic auto/desirable trên port nối PC. |
| Tắt DTP trên trunk | switchport nonegotiate | Không để switch tự thương lượng trunk nếu không cần. |
| Trunk cấu hình thủ công | switchport mode trunk | Chỉ trunk trên link switch-switch hoặc router-switch. |
| Native VLAN riêng | Không dùng VLAN người dùng làm native VLAN | Giảm điều kiện double tagging hoạt động. |
| Tắt cổng không dùng | shutdown | Giảm nguy cơ người lạ cắm thiết bị vào mạng. |

## 4. DHCP Snooping để chống DHCP Server giả

DHCP Spoofing là tình huống có một DHCP Server giả trong mạng cấp sai default gateway, DNS hoặc IP cho client. DHCP Snooping giúp switch chỉ tin DHCP Offer/Ack từ cổng đã đánh dấu trusted.

! Bật DHCP Snooping toàn cục và theo VLAN ip dhcp snooping ip dhcp snooping vlan 1 ! Cổng nối đến DHCP Server thật interface fa0/3 ip dhcp snooping trust ! Cổng access nối client hoặc thiết bị không tin cậy interface...

Lưu ý Packet Tracer: một số phiên bản giả lập không mô phỏng đầy đủ DHCP Snooping binding table hoặc hành vi chặn gói DHCP. Khi lab trên thiết bị thật, nguyên tắc trusted/untrusted sẽ rõ hơn.

## 5. Dynamic ARP Inspection và BPDU Guard

ARP Poisoning đánh lừa máy tính bằng ARP Reply giả để traffic đi nhầm qua attacker. Dynamic ARP Inspection kiểm tra ARP dựa trên thông tin đáng tin cậy, thường kết hợp với DHCP Snooping binding table. Với STP, PortFas...

| Cơ chế | Dùng để giảm rủi ro | Lệnh thường gặp |
| --- | --- | --- |
| Dynamic ARP Inspection | ARP spoofing/poisoning | ip arp inspection vlan <vlan-id> |
| DHCP Snooping Binding | Nền dữ liệu kiểm tra IP-MAC-port | show ip dhcp snooping binding |
| PortFast | Access port lên forwarding nhanh | spanning-tree portfast |
| BPDU Guard | Khóa access port nếu nhận BPDU lạ | spanning-tree bpduguard enable |

## 6. Wireless LAN: khái niệm và thành phần

Mạng không dây giúp người dùng di chuyển linh hoạt hơn so với mạng có dây. Tuy nhiên, vì tín hiệu truyền qua không gian mở nên wireless cần cơ chế nhận dạng mạng, xác thực, bảo mật và tránh va chạm riêng.

| Loại mạng không dây | Phạm vi/ý nghĩa | Ví dụ |
| --- | --- | --- |
| WPAN | Mạng cá nhân không dây, phạm vi rất gần | Bluetooth, tai nghe, chia sẻ gần |
| WLAN | Mạng LAN không dây, theo chuẩn IEEE 802.11 | Wi-Fi trong nhà, văn phòng, trường học |
| WMAN | Mạng đô thị không dây, phạm vi rộng hơn WLAN | WiMAX hoặc mô hình phủ sóng đô thị |
| WWAN | Mạng diện rộng không dây | 4G/5G/cellular, vệ tinh |

## 7. Wireless Router khác Access Point như thế nào?

| Thiết bị | Đặc điểm | Cách hiểu nhanh |
| --- | --- | --- |
| Wireless Router | Thường có cổng Internet/WAN, switch tích hợp và phát Wi-Fi | Router Wi-Fi gia đình: vừa định tuyến vừa phát sóng |
| Autonomous AP | Mỗi AP cấu hình riêng, độc lập | Phù hợp mô hình nhỏ |
| Controller-based AP | AP nhẹ, quản lý tập trung qua WLC | Phù hợp doanh nghiệp, trường học, nhiều tầng/tòa nhà |

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

| Mốc thời gian | Nội dung chính |
| --- | --- |
| 00:02 | Ôn lại Port Security: kiểm soát cổng switch, hạn chế thiết bị lạ cắm vào LAN và giảm nguy cơ thất thoát thông tin. |
| 01:57 | Giảm thiểu VLAN Hopping: tắt DTP, cấu hình trunk thủ công, không để cổng người dùng tự thương lượng trunk. |
| 02:23 | Ôn DHCP Starvation và DHCP Spoofing; dùng Port Security để giới hạn MAC/request và DHCP Snooping để chặn DHCP Server giả. |
| 05:00 | DHCP Snooping phân biệt trusted port và untrusted port; chỉ cổng nối đến DHCP Server hợp lệ mới được cấp phát DHCP. |
| 23:17 | Giới thiệu Dynamic ARP Inspection để giảm ARP spoofing/poisoning dựa trên kiểm tra ARP và binding table. |
| 25:20 | Giảm STP Attack bằng PortFast và BPDU Guard trên access port, tránh thiết bị người dùng gửi BPDU vào hệ thống switch. |
| 46:08 | Chuyển sang Wireless LAN: lợi ích của mạng không dây, các nhóm WPAN/WLAN/WMAN/WWAN và công nghệ Bluetooth, Wi-Fi, WiMAX, cellular. |
| 50:22 | Mạng Wi-Fi hoạt động trên sóng radio, phổ biến ở băng tần 2.4 GHz và 5 GHz; liên quan chuẩn IEEE 802.11 và Wi-Fi Alliance. |
| 53:04 | Thành phần WLAN gồm wireless NIC, wireless router, access point; phân biệt autonomous AP và controller-based/lightweight AP. |
| 1:32:05 | Các mô hình Wi-Fi: ad-hoc, infrastructure, tethering, BSS, ESS; cơ chế CSMA/CA, association và bài thực hành WRT300N trong Packet Tracer. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | L2 Mitigation và Wireless LAN |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. L2 Mitigation và Wireless LAN giải quyết vấn đề gì trong mạng?
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
| WLAN | Mạng LAN không dây | Mạng dùng Wi-Fi thay cho cáp Ethernet. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 L2 Mitigation và Wireless LAN nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

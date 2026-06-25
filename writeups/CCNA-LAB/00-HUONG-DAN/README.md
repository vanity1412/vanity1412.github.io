# Lộ trình thực hành CCNA bằng Cisco Packet Tracer

Thư mục này đã phân loại **94 bài lab** theo kỹ năng, từ nền tảng đến bài tổng hợp. File gốc vẫn được giữ nguyên ở các thư mục ban đầu; `CCNA-LAB` chỉ chứa bản sao đã sắp xếp.

Thư mục `00-TONG-HOP-THEO-SO-DAU-BAI` gom toàn bộ file theo số gốc ở đầu tên bài: `1.x`, `2.x`, ... `9.x`, rồi `10.x` trở lên.

## Cách dùng hai loại file

- `.pka`: bài thực hành có đề bài, yêu cầu và chấm điểm. Mở bằng Packet Tracer, đọc **Objectives/Instructions**, làm bài rồi dùng **Check Results**.
- `.pkt`: topology tự do hoặc bài mẫu, thường không có hệ thống chấm điểm. Hãy kiểm tra topology, cấu hình từng thiết bị và tự xác minh bằng lệnh `show`, `ping`, `traceroute`.

## Lộ trình từ đầu đến cuối

### Giai đoạn 1 — Nền tảng và thao tác thiết bị

Học lần lượt thư mục 01 đến 05:

1. `01-Lam-quen-Packet-Tracer`: nhận biết thiết bị, liên kết và ký hiệu mạng.
2. `02-IOS-va-cau-hinh-thiet-bi-co-ban`: CLI, các mode IOS, hostname, password, interface và lưu cấu hình.
3. `03-Mo-hinh-mang-ARP-ICMP-TCP-UDP`: hiểu gói tin đi qua các lớp, MAC/IP, ARP và TCP/UDP.
4. `04-Ket-noi-vat-ly-va-connectivity`: chọn cáp/cổng và tạo kết nối đầu-cuối.
5. `05-Dia-chi-IP-Subnetting-VLSM`: IPv4, IPv6, subnet mask, chia subnet và VLSM.

Chỉ chuyển sang giai đoạn 2 khi bạn có thể tự cấu hình IP, default gateway và kiểm tra ping mà không nhìn đáp án.

### Giai đoạn 2 — Switching và mạng LAN

Học thư mục 06 đến 09:

6. `06-VLAN-Trunk-DTP`: tạo VLAN, gán access port, cấu hình trunk và kiểm tra VLAN.
7. `07-STP-va-EtherChannel`: hiểu chống loop, STP và gộp nhiều đường vật lý.
8. `08-Inter-VLAN-va-Layer-3-Switching`: router-on-a-stick, SVI và định tuyến giữa VLAN.
9. `09-FHRP-HSRP`: tạo default gateway dự phòng bằng HSRP.

Mốc đạt: tự dựng được 2–3 VLAN, trunk giữa các switch và cho các VLAN liên lạc qua router hoặc multilayer switch.

### Giai đoạn 3 — Routing và cấp phát địa chỉ

Học thư mục 10 đến 12:

10. `10-Static-va-Default-Routing`: route tĩnh IPv4/IPv6 và default route.
11. `11-OSPF`: OSPFv2 single-area, router ID, neighbor, DR/BDR và quảng bá default route.
12. `12-DHCP`: DHCPv4 server/relay và kiểm tra lease.

Mốc đạt: đọc được routing table, giải thích vì sao một route được chọn và tìm được lỗi khi router không học route.

### Giai đoạn 4 — Kiểm soát, NAT, Wi-Fi và bảo mật

Học thư mục 13 đến 16:

13. `13-ACL`: standard/extended ACL, named/numbered ACL và vị trí đặt ACL.
14. `14-NAT-va-PAT`: static NAT, dynamic NAT, PAT và kiểm tra bảng dịch.
15. `15-Wireless-WLAN`: WLAN, WLC và WPA2 Enterprise.
16. `16-Bao-mat-thiet-bi-va-Switch`: SSH, mật khẩu an toàn, port security và hardening thiết bị.

Mốc đạt: kiểm soát được luồng truy cập theo yêu cầu, cho mạng private ra ngoài bằng PAT và khóa các điểm truy cập không hợp lệ.

### Giai đoạn 5 — Vận hành và tổng hợp

Học thư mục 17 đến 20:

17. `17-Quan-tri-mang`: CDP, LLDP, NTP, backup cấu hình và nâng cấp IOS bằng TFTP.
18. `18-Kiem-tra-va-xu-ly-su-co`: ping, traceroute, lệnh `show` và quy trình tìm lỗi.
19. `19-WAN`: khái niệm và kết nối WAN.
20. `20-Bai-tong-hop`: bài mạng nhỏ, skills challenge và bài cuối kỳ; làm sau cùng, không xem cấu hình mẫu trước.

## Quy trình làm mỗi bài lab

1. Đọc mục tiêu, vẽ nhanh topology và lập bảng địa chỉ/VLAN trước khi cấu hình.
2. Cấu hình từ lớp thấp lên cao: cáp/cổng → VLAN/IP → routing → dịch vụ → ACL/NAT/bảo mật.
3. Sau mỗi khối, chạy lệnh kiểm tra phù hợp; đừng cấu hình hết rồi mới ping.
4. Nếu lỗi, đi theo thứ tự: trạng thái cổng → VLAN/trunk → IP/mask/gateway → routing → ACL/NAT → dịch vụ.
5. Lưu cấu hình bằng `copy running-config startup-config` khi bài yêu cầu.
6. Với `.pka`, chạy **Check Results**, đọc mục sai và sửa cho đến khi đạt yêu cầu.
7. Ghi lại ba thứ: lỗi gặp phải, lệnh đã dùng để phát hiện, lệnh đã dùng để sửa.

## Các lệnh nên thuộc lòng

```text
show running-config
show ip interface brief
show interfaces status
show vlan brief
show interfaces trunk
show spanning-tree
show etherchannel summary
show ip route
show ip ospf neighbor
show access-lists
show ip nat translations
show cdp neighbors detail
show lldp neighbors detail
ping
traceroute
```

## Tài liệu kiểm kê

- `DANH-SACH-BAI-LAB.csv`: từng file, thư mục nguồn, kích thước và SHA-256.
- `THONG-KE-THEO-DANG.csv`: số lượng bài trong từng dạng.

Nên học theo đúng số thứ tự thư mục. Trong mỗi thư mục, làm bài có số chương nhỏ trước, bài có chữ `Implement`, `Challenge` hoặc `Troubleshoot` sau.

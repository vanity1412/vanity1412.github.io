---
layout: page-toc
title: "Buổi 20: Inter-VLAN Routing"
permalink: /writeups/ccna-theory/buoi-20-intervlan-routing/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Inter-VLAN Routing

## Mục tiêu học tập

- Nắm vai trò của Inter-VLAN Routing trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. INTER-VLAN ROUTING

Legacy Router; Router-on-a-Stick; Switch Layer 3; SVI; Routed Port

| Chủ đề chính | Định tuyến giữa các VLAN để các mạng đã bị tách bởi VLAN có thể giao tiếp có kiểm soát. |
| --- | --- |
| Nguồn video | https://www.youtube.com/watch?v=5rfnJ5K3Tqc |
| Trọng tâm thực hành | Cấu hình legacy inter-VLAN routing, router-on-a-stick, switch layer 3 SVI và routed port trong Packet Tracer. |

## 2. Nguồn tham khảo

Hiểu vì sao các VLAN mặc định bị cách ly và cần thiết bị Layer 3 để giao tiếp với nhau.

Phân biệt được các phương án inter-VLAN routing: legacy router, router-on-a-stick, switch layer 3 với SVI và routed port.

Biết cấu hình trunk từ switch lên router, tạo router subinterface và gán encapsulation dot1q.

Biết cấu hình interface vlan trên switch layer 3 và bật ip routing.

Biết cách kiểm tra lỗi bằng show vlan brief, show interfaces trunk, show ip interface brief, ping và Simulation Mode trong Packet Tracer.

## 3. Bài toán Inter-VLAN Routing

Ở các buổi trước, VLAN được dùng để chia nhỏ một switch Layer 2 thành nhiều vùng logic độc lập. Mỗi VLAN hoạt động như một broadcast domain riêng. Điều đó giúp giảm broadcast, tăng khả năng quản lý và tăng tính cách l...

Tuy nhiên, khi các VLAN đã bị tách biệt, thiết bị ở VLAN 2 không thể tự nói chuyện với thiết bị ở VLAN 3 nếu chỉ có switch Layer 2. Muốn các VLAN giao tiếp với nhau, phải có thiết bị Layer 3 tham gia định tuyến.

## 4. Phương án 1: Legacy Inter-VLAN Routing

Đây là cách định tuyến VLAN truyền thống. Với mỗi VLAN, router cần một interface vật lý riêng kết nối vào một access port thuộc đúng VLAN đó trên switch. Interface router sẽ đóng vai trò default gateway cho VLAN tương...

Nếu có 3 VLAN thì router cần 3 interface vật lý. Cách này dễ hiểu, dễ demo nhưng rất tốn cổng và không phù hợp khi số VLAN tăng.

## 5. Logic cấu hình

Tạo VLAN 2, VLAN 3, VLAN 4 trên switch.

Gán các cổng kết nối PC/DHCP server/router vào đúng VLAN bằng access port.

Mỗi cổng router nối xuống switch được đặt IP gateway thuộc subnet của VLAN đó.

PC trong VLAN phải dùng IP gateway là địa chỉ interface router cùng VLAN.

Sau khi cấu hình, thiết bị ở VLAN khác nhau có thể ping qua router.

Lệnh gán access port trên switch

## 6. Phương án 2: Router-on-a-Stick

Router-on-a-Stick giải quyết nhược điểm tốn interface của phương án legacy. Thay vì mỗi VLAN cần một dây riêng, switch chỉ cần một đường trunk lên router. Trên router, một interface vật lý được chia thành nhiều subint...

## 7. Các bước cấu hình

Trên switch: cấu hình cổng nối router ở mode trunk.

Trên router: bật interface vật lý bằng no shutdown.

Tạo subinterface, ví dụ g0/0.2, g0/0.3, g0/0.4.

Mỗi subinterface phải có encapsulation dot1q VLAN_ID.

Đặt IP cho subinterface. IP này là default gateway cho thiết bị trong VLAN tương ứng.

Kiểm tra bằng ping, show ip interface brief và Simulation Mode nếu Packet Tracer phản hồi chậm.

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

| Chủ đề chính | Định tuyến giữa các VLAN để các mạng đã bị tách bởi VLAN có thể giao tiếp có kiểm soát. |
| --- | --- |
| Nguồn video | https://www.youtube.com/watch?v=5rfnJ5K3Tqc |
| Trọng tâm thực hành | Cấu hình legacy inter-VLAN routing, router-on-a-stick, switch layer 3 SVI và routed port trong Packet Tracer. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Inter-VLAN Routing |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Inter-VLAN Routing giải quyết vấn đề gì trong mạng?
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
| VLAN | Mạng LAN ảo | Chia switch thành nhiều broadcast domain logic. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Inter-VLAN Routing nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

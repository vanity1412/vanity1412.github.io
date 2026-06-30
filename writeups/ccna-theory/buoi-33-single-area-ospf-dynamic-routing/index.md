---
layout: page-toc
title: "Buổi 33: Single-Area OSPF"
permalink: /writeups/ccna-theory/buoi-33-single-area-ospf-dynamic-routing/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Single-Area OSPF

## Mục tiêu học tập

- Nắm vai trò của Single-Area OSPF trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Định tuyến động OSPF, Router ID, Wildcard Mask, OSPF Packets, DR/BDR và lab cấu hình Area 0

| --- | --- |
| Buổi số | Buổi 33 |
| Nguồn video | https://www.youtube.com/watch?v=d3aLG0KRC2w |
| Chủ đề trọng tâm | Dynamic Routing, Single-Area OSPF, OSPF packets, DR/BDR, Wildcard Mask, Lab OSPF Area 0 |

## 2. Nguồn và ghi chú

Nhắc lại ý nghĩa của router ảo/Virtual IP trong HSRP để thấy khác biệt với định tuyến động.

Hiểu OSPF là giao thức định tuyến động dạng link-state, hội tụ nhanh và phù hợp mạng vừa/lớn.

Phân biệt Neighbor Table, Topology Table/LSDB và Routing Table.

Nhớ 5 loại OSPF packet: Hello, DBD, LSR, LSU, LSAck.

Hiểu vai trò DR/BDR trong mạng multiaccess để giảm số lượng adjacency và LSA.

Thực hành lệnh router ospf, network wildcard area 0 và show ip route.

## 3. Vì sao cần router ảo?

Trong phần đầu buổi học, giảng viên nhắc lại khái niệm router ảo trong HSRP. Vấn đề là máy tính thường chỉ có một default gateway. Nếu gateway chính hỏng, người quản trị phải đổi gateway thủ công cho nhiều máy, gây gi...

thay vì PC nhớ địa chỉ của R1 hoặc R2, PC chỉ nhớ một địa chỉ IP ảo. Router nào đang active thì router đó “giữ” IP ảo và xử lý dữ liệu.

| Thành phần | Ý nghĩa |
| --- | --- |
| Virtual IP | Địa chỉ gateway ảo được cấu hình làm default gateway cho PC. |
| Active Router | Router đang giữ Virtual IP và chuyển tiếp traffic. |
| Standby Router | Router dự phòng, theo dõi Active Router và lên thay khi cần. |
| Preempt/Priority | Cơ chế ưu tiên router có priority cao trở lại làm Active khi nó phục hồi. |

## 4. Vì sao cần Dynamic Routing?

Static route phù hợp mạng nhỏ, nhưng khi số router và số mạng tăng lên, người quản trị phải gõ rất nhiều lệnh ip route. Dynamic routing giúp router tự trao đổi thông tin định tuyến và tự cập nhật khi topology thay đổi.

## 5. OSPF là gì?

Link-state: router không chỉ biết “đi qua ai”, mà còn xây dựng được bản đồ topology trong cùng area.

Hội tụ nhanh: khi đường link thay đổi, OSPF lan truyền LSA và tính lại route.

Có khả năng mở rộng: có thể chia thành nhiều area, nhưng buổi này tập trung vào Single-Area OSPF area 0.

Dễ cấu hình hơn static route khi mạng có nhiều router: mỗi router chỉ khai báo các mạng trực tiếp của mình.

## 6. Ba bảng quan trọng trong OSPF

| Bảng | Tên khác | Chức năng |
| --- | --- | --- |
| Neighbor Table | Adjacency Database | Lưu danh sách router hàng xóm và trạng thái quan hệ láng giềng. |
| Routing Table | IP Routing Table | Chỉ chứa các tuyến tốt nhất sau khi OSPF chạy thuật toán SPF. |

Topology Table có thể có nhiều đường đến một đích, nhưng Routing Table chỉ đưa vào đường tốt nhất để forward packet.

## 7. 5 loại OSPF packet

| Packet | Tên đầy đủ | Vai trò dễ hiểu |
| --- | --- | --- |
| Hello | Hello Packet | Chào hỏi, phát hiện neighbor, duy trì kết nối. |
| DBD | Database Description | Tóm tắt cơ sở dữ liệu link-state để hai router so sánh. |
| LSR | Link State Request | Yêu cầu thêm thông tin còn thiếu. |
| LSU | Link State Update | Gửi thông tin cập nhật hoặc trả lời yêu cầu LSR. |
| LSAck | Link State Acknowledgment | Xác nhận đã nhận thông tin OSPF. |

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
| Buổi số | Buổi 33 |
| Nguồn video | https://www.youtube.com/watch?v=d3aLG0KRC2w |
| Chủ đề trọng tâm | Dynamic Routing, Single-Area OSPF, OSPF packets, DR/BDR, Wildcard Mask, Lab OSPF Area 0 |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Single-Area OSPF |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Single-Area OSPF giải quyết vấn đề gì trong mạng?
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
| OSPF | Giao thức định tuyến động | Link-state routing protocol dùng area và cost. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Single-Area OSPF nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

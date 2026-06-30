---
layout: page-toc
title: "Buổi 5: Physical Layer"
permalink: /writeups/ccna-theory/buoi-5-physical-layer/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Physical Layer

## Mục tiêu học tập

- Nắm vai trò của Physical Layer trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. Tổng quan

Tài liệu học tập chuẩn giáo trình - dùng để ôn thi và thực hành Packet Tracer

| --- | --- |
| Buổi số | Buổi 5 |
| Ngày | Không ghi trong transcript |
| Nguồn video | https://www.youtube.com/watch?v=M6Dh82bmsLI |

## 2. Mẹo ghi nhớ nhanh

Sau buổi học này, sinh viên sẽ:

Trình bày được vai trò của Physical Layer trong mô hình OSI.

Giải thích được vì sao tầng vật lý truyền dữ liệu dưới dạng bit 0 và 1.

Nhận diện được các thành phần vật lý trong mạng: media, connector, NIC, cổng mạng và dây cáp.

Phân biệt được encoding và signaling ở mức cơ bản.

Giải thích và phân biệt được bandwidth, latency, throughput và goodput.

## 3. Ôn tập OSI/TCP/IP và giới thiệu Physical Layer

Định nghĩa học thuật: Mô hình OSI là mô hình tham chiếu gồm 7 tầng; Physical Layer là tầng thấp nhất, chịu trách nhiệm kết nối vật lý và truyền bit qua môi trường truyền dẫn.

Nếu xem mạng như một tòa nhà, Physical Layer là phần móng và đường dây điện bên dưới. Không có nó, các tầng phía trên không có nơi để truyền dữ liệu.

Ví dụ thực tế: Trong Packet Tracer, khi kéo dây từ PC đến switch, thao tác chọn loại dây và cổng thuộc phạm vi Physical Layer.

OSI có 7 tầng; Physical Layer là tầng dưới cùng. TCP/IP được nhắc lại như kiến thức nền từ các buổi trước. Buổi học này tập trung vào tầng vật lý và các kết nối thiết bị trong mạng LAN.

Physical Layer là nền móng của truyền thông mạng: dữ liệu muốn đi được thì trước hết phải có môi trường vật lý để đi.

## 4. Vai trò của Physical Layer trong truyền dữ liệu

Định nghĩa học thuật: Physical Layer định nghĩa cách các bit 0 và 1 được truyền qua môi trường vật lý như dây đồng, cáp quang hoặc sóng không dây.

Tầng này không cần biết dữ liệu là hình ảnh, tin nhắn hay website. Nó chỉ làm nhiệm vụ đưa tín hiệu đại diện cho 0 và 1 đi từ thiết bị này sang thiết bị khác.

Ví dụ thực tế: Khi gửi một file ảnh qua mạng, ảnh được xử lý ở các tầng trên. Đến tầng vật lý, dữ liệu cuối cùng được đẩy qua dây mạng hoặc Wi-Fi dưới dạng tín hiệu bit.

Physical Layer làm việc với bit, tín hiệu và môi trường truyền dẫn. Các thành phần như dây cáp, cổng mạng, đầu RJ45, card mạng đều thuộc phạm vi tầng vật lý. Tầng vật lý không xử lý ý nghĩa nội dung dữ liệu.

Mọi dữ liệu phức tạp đều trở thành chuỗi bit 0/1 khi đi qua tầng vật lý.

## 5. Thành phần vật lý: Hardware, Media, Connector và NIC

Định nghĩa học thuật: Các thành phần vật lý gồm thiết bị phần cứng, môi trường truyền dẫn, đầu nối và card giao tiếp mạng.

Muốn hai máy tính nói chuyện với nhau, cần có đường đi, đầu cắm và cổng giao tiếp. Thiếu một trong các phần này thì kết nối vật lý không hình thành.

Ví dụ thực tế: Một dây mạng LAN gồm sợi UTP, hai đầu RJ45 và được cắm vào cổng Ethernet trên PC hoặc switch.

Media là môi trường truyền dẫn: dây đồng, cáp quang, sóng Wi-Fi. Connector là đầu nối: ví dụ RJ45. NIC là card/cổng mạng giúp thiết bị tham gia mạng. Hardware device có thể là PC, switch, router hoặc card mạng.

Nhớ công thức đơn giản: thiết bị + dây/sóng + đầu nối/cổng = kết nối vật lý.

| Thành phần | Định nghĩa học thuật | Hiểu đời thường | Ví dụ thực tế |

## 6. Tiêu chuẩn tầng vật lý và mối liên hệ với Data Link Layer

Định nghĩa học thuật: Physical Layer được chuẩn hóa bởi nhiều tổ chức như ISO, EIA/TIA, IEEE, ANSI, ITU-T; tầng này có quan hệ chặt với Data Link Layer ở phía trên.

Thiết bị của nhiều hãng khác nhau muốn kết nối được thì phải dùng chuẩn chung. Tầng Data Link cần hiểu kiểu kết nối bên dưới để đóng gói và xử lý frame phù hợp.

Ví dụ thực tế: Card mạng Ethernet cần biết đang dùng kết nối có dây hay không dây để tầng Data Link xử lý dữ liệu đúng cách.

Chuẩn hóa giúp thiết bị mạng khác hãng vẫn hoạt động chung. Physical Layer nằm dưới Data Link Layer nên hai tầng liên hệ rất chặt. IEEE là tổ chức thường gặp khi học Ethernet và Wi-Fi.

## 7. Ba nhiệm vụ chính: Physical Components, Encoding, Signaling

Định nghĩa học thuật: Physical Layer bao gồm ba nhóm nhiệm vụ chính: thành phần vật lý, encoding và signaling.

Đầu tiên cần có phần cứng và dây/sóng để truyền. Sau đó bit phải được biểu diễn theo quy ước phù hợp. Cuối cùng tín hiệu được phát đi trên dây đồng, sóng radio hoặc tia sáng.

Ví dụ thực tế: Với cáp đồng, tín hiệu là xung điện. Với Wi-Fi, tín hiệu là sóng radio. Với cáp quang, tín hiệu là ánh sáng hoặc laser.

Có thể nhớ theo chuỗi: có phần cứng -> biểu diễn bit -> đánh tín hiệu đi.

| Nhiệm vụ | Nghĩa tiếng Việt | Giải thích | Ví dụ |
| --- | --- | --- | --- |

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
| Buổi số | Buổi 5 |
| Ngày | Không ghi trong transcript |
| Nguồn video | https://www.youtube.com/watch?v=M6Dh82bmsLI |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Physical Layer |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Physical Layer giải quyết vấn đề gì trong mạng?
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
| Physical Layer | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Physical Layer nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

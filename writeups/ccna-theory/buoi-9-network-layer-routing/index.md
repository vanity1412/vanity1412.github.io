---
layout: page-toc
title: "Buổi 9: Network Layer và Routing"
permalink: /writeups/ccna-theory/buoi-9-network-layer-routing/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Network Layer và Routing

## Mục tiêu học tập

- Nắm vai trò của Network Layer và Routing trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. NETWORK LAYER VÀ ĐỊNH TUYẾN CƠ BẢN

Sau buổi học này, sinh viên sẽ:

Hiểu vị trí và vai trò của Network Layer trong mô hình OSI và TCP/IP.

Nắm được bốn chức năng chính của Network Layer: addressing, encapsulation, routing và decapsulation.

Giải thích được ba đặc điểm quan trọng của IP: connectionless, best effort và media independent.

Nhận diện các trường quan trọng trong IPv4 header và IPv6 header, đặc biệt là TTL/Hop Limit.

Biết cách kiểm tra bảng định tuyến trên máy tính bằng route print hoặc netstat -r.

## 2. Ôn tập mô hình OSI/TCP-IP và vị trí của Network Layer

Định nghĩa học thuật:

Network Layer là tầng số 3 trong mô hình OSI, nằm trên Data Link Layer và dưới Transport Layer. Trong mô hình TCP/IP, Network Layer tương ứng với Internet Layer, nơi các giao thức IPv4 và IPv6 hoạt động.

Ví dụ thực tế:

Máy A trong mạng LAN ở nhà muốn truy cập website trường. Dữ liệu không chỉ đi trong mạng LAN mà phải qua router gia đình, nhà mạng, nhiều router trung gian rồi mới đến server website. Phần định danh và định tuyến đườn...

Network Layer làm việc chủ yếu với địa chỉ IP. Data Link Layer dùng địa chỉ MAC theo từng chặng; Network Layer dùng địa chỉ IP để xác định nguồn và đích trên toàn hành trình. Buổi 9 chuyển trọng tâm từ Ethernet/Data L...

Network Layer là tầng giúp dữ liệu vượt ra khỏi phạm vi LAN và đi qua nhiều mạng khác nhau.

## 3. Vai trò của Network Layer

Định nghĩa học thuật:

Network Layer cung cấp dịch vụ truyền packet giữa các thiết bị đầu cuối qua hệ thống mạng trung gian, trong đó các router sử dụng địa chỉ IP và bảng định tuyến để chuyển tiếp packet.

Tưởng tượng Network Layer là người giao hàng. Người gửi đưa gói hàng đã đóng, bên ngoài có địa chỉ người gửi và người nhận. Người giao hàng không cần biết bên trong là ảnh, video hay tin nhắn; nhiệm vụ chính là đưa gó...

Ví dụ thực tế:

Khi gửi một ảnh qua Internet, ứng dụng tạo dữ liệu, Transport Layer chia dữ liệu thành segment, Network Layer thêm IP header để tạo packet, rồi packet được đưa xuống Data Link Layer để đóng thành frame gửi qua từng đo...

Network Layer chịu trách nhiệm định danh địa chỉ IP nguồn và IP đích. Network Layer đóng gói dữ liệu tầng trên thành IP packet. Router đọc thông tin IP để quyết định chuyển packet đi đâu.

## 4. Bốn chức năng chính của Network Layer

| Chức năng | Thuật ngữ | Giải thích | Ví dụ |
| --- | --- | --- | --- |
| Định địa chỉ | Addressing | Gán và sử dụng địa chỉ IP để xác định nguồn/đích. | PC1: 192.168.1.10 gửi đến server: 42.112.213.88. |
| Đóng gói | Encapsulation | Thêm IP header vào dữ liệu tầng trên để tạo packet. | Segment TCP/UDP được gắn IP header thành IPv4 packet. |
| Định tuyến | Routing | Tìm đường đi tốt hoặc phù hợp để packet đến mạng đích. | Router chọn gửi packet sang router kế tiếp. |
| Mở gói | Decapsulation | Thiết bị đích gỡ IP header để chuyển dữ liệu lên tầng trên. | Server nhận packet và chuyển payload lên TCP/UDP. |

Addressing trả lời câu hỏi: nguồn và đích là ai? Encapsulation trả lời câu hỏi: đóng gói packet như thế nào? Routing trả lời câu hỏi: đi đường nào? Decapsulation trả lời câu hỏi: khi đến đích thì mở ra và đưa lên tầng...

## 5. Encapsulation ở Network Layer

Định nghĩa học thuật:

Encapsulation ở Network Layer là quá trình lấy dữ liệu từ tầng Transport, xem toàn bộ phần đó là payload, sau đó thêm IP header để tạo thành IP packet.

Ví dụ thực tế:

Khi truy cập web, dữ liệu HTTP đi xuống Transport Layer tạo TCP segment. Network Layer thêm IP header vào segment đó để tạo IPv4 hoặc IPv6 packet.

Mỗi tầng thêm header riêng để phục vụ nhiệm vụ của tầng đó. Ở Network Layer, header quan trọng nhất là IP header. IP header chứa thông tin giúp router chuyển tiếp packet.

Dữ liệu đi xuống thì được đóng gói thêm; dữ liệu đi lên thì được gỡ dần các lớp header.

## 6. IP là connectionless - giao thức phi kết nối

Định nghĩa học thuật:

Connectionless là đặc điểm trong đó IP không thiết lập phiên kết nối trước khi gửi packet, không yêu cầu thông tin điều khiển trước khi truyền và bản thân IP không bắt buộc bên nhận xác nhận đã nhận.

Ví dụ thực tế:

Router nhận IP packet thì xử lý và chuyển tiếp dựa trên routing table. Router không hỏi server đích: 'Bạn đã sẵn sàng nhận chưa?' trước khi chuyển packet.

IP không thiết lập kết nối trước như một cuộc gọi điện thoại. IP không tự đảm bảo packet chắc chắn đến đích. Các cơ chế đảm bảo độ tin cậy thường nằm ở tầng trên, ví dụ TCP.

IP hoạt động theo kiểu: có gói thì gửi, không hỏi trước, không chờ xác nhận ở chính tầng IP.

## 7. IP là best effort - nỗ lực tối đa

Định nghĩa học thuật:

Best effort nghĩa là IP cố gắng chuyển packet đến đích tốt nhất có thể, nhưng không cam kết packet chắc chắn đến nơi, không tự truyền lại khi mất gói và không đảm bảo thứ tự.

Ví dụ thực tế:

Khi mạng nghẽn hoặc router bị lỗi, packet có thể bị drop. Nếu ứng dụng cần tin cậy, TCP hoặc cơ chế tầng ứng dụng sẽ phát hiện mất dữ liệu và yêu cầu gửi lại.

Best effort không có nghĩa là IP làm qua loa; nghĩa là IP cố chuyển nhưng không hứa chắc chắn. IP không có cơ chế retransmission ở chính tầng Network. Độ tin cậy được bổ sung bởi tầng trên, không phải bởi IP cơ bản.

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

| Chức năng | Thuật ngữ | Giải thích | Ví dụ |
| --- | --- | --- | --- |
| Định địa chỉ | Addressing | Gán và sử dụng địa chỉ IP để xác định nguồn/đích. | PC1: 192.168.1.10 gửi đến server: 42.112.213.88. |
| Đóng gói | Encapsulation | Thêm IP header vào dữ liệu tầng trên để tạo packet. | Segment TCP/UDP được gắn IP header thành IPv4 packet. |
| Định tuyến | Routing | Tìm đường đi tốt hoặc phù hợp để packet đến mạng đích. | Router chọn gửi packet sang router kế tiếp. |
| Mở gói | Decapsulation | Thiết bị đích gỡ IP header để chuyển dữ liệu lên tầng trên. | Server nhận packet và chuyển payload lên TCP/UDP. |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Network Layer và Routing |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Network Layer và Routing giải quyết vấn đề gì trong mạng?
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
| Network Layer và Routing | Chủ đề chính | Khái niệm trọng tâm cần nắm trong bài. |
| Topology | Sơ đồ mạng | Cách các thiết bị được kết nối trong lab. |
| Verification | Kiểm tra | Bước xác nhận cấu hình hoạt động đúng. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Network Layer và Routing nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

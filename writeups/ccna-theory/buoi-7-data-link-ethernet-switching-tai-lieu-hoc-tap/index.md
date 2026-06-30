---
layout: page-toc
title: "Buổi 7: Ethernet và Switching"
permalink: /writeups/ccna-theory/buoi-7-data-link-ethernet-switching-tai-lieu-hoc-tap/
toc: true
---

[← Quay lại CCNA Theory](/writeups/ccna-theory/)

# Ethernet và Switching

## Mục tiêu học tập

- Nắm vai trò của Ethernet và Switching trong chương trình CCNA.
- Hiểu các khái niệm chính và khi nào cần dùng.
- Đọc được bảng, thông số hoặc trạng thái liên quan.
- Áp dụng được vào lab Packet Tracer cơ bản.
- Biết lệnh kiểm tra hoặc dấu hiệu lỗi thường gặp.

## 1. TÀI LIỆU HỌC TẬP MẠNG MÁY TÍNH

Biên soạn từ transcript bài giảng - dùng để ôn tập, làm bài thực hành và chuẩn bị kiểm tra

| --- | --- |
| Buổi số | 7 |
| Ngày | Không nêu trong transcript |
| Chủ đề chính | Data Link Layer, Ethernet Frame, MAC Address, ARP, MAC Address Table |
| Nguồn transcript | Buổi 7 - YouTube: https://www.youtube.com/watch?v=EYgbBHJ6HmI |

Sau buổi học này, sinh viên sẽ:

Hiểu vai trò của Data Link Layer trong mô hình OSI và mối liên hệ với Physical Layer.

## 2. Ôn lại Physical Layer và vị trí của Data Link Layer

Định nghĩa học thuật: Physical Layer là tầng thấp nhất trong mô hình OSI, chịu trách nhiệm truyền các bit 0/1 qua môi trường vật lý như cáp đồng, cáp quang hoặc sóng không dây. Data Link Layer là tầng ngay phía trên P...

Ví dụ thực tế: Khi máy tính gửi dữ liệu qua dây mạng Ethernet, tầng vật lý chỉ truyền tín hiệu điện biểu diễn 0/1. Tầng Data Link mới là nơi tạo ra Ethernet frame có MAC nguồn, MAC đích và phần kiểm tra lỗi.

- Physical Layer truyền bit, Data Link Layer đóng gói bit thành frame. - Data Link Layer là cầu nối giữa dữ liệu tầng trên và môi trường truyền dẫn tầng dưới. - Trong chương trình CCNA, Physical và Data Link thường đư...

Muốn hiểu mạng LAN, không thể chỉ biết dây cáp và tín hiệu; cần hiểu thêm frame, MAC address và cách switch xử lý frame.

## 3. Mục đích của Data Link Layer qua ví dụ driver thiết bị

Định nghĩa học thuật: Data Link Layer cung cấp cơ chế để các tầng trên truy cập được vào môi trường truyền dẫn vật lý bên dưới, đồng thời đóng gói dữ liệu theo khuôn dạng phù hợp với từng công nghệ mạng.

Ví dụ thực tế: Cùng là truyền dữ liệu nhưng Ethernet, Wi-Fi, PPP hay HDLC có cách đóng gói khác nhau. Data Link Layer phải biết liên kết bên dưới là loại gì để tạo frame đúng chuẩn.

- Data Link không chỉ “chuyển tiếp” dữ liệu mà còn phải hiểu công nghệ truyền bên dưới. - Mỗi công nghệ lớp 2 có frame format riêng. - Ví dụ driver giúp nhớ: có phần cứng chưa đủ, phải có lớp điều khiển để hệ thống sử...

Data Link Layer giúp dữ liệu từ tầng Network có thể đi xuống Physical Layer một cách đúng chuẩn.

## 4. Nhiệm vụ chính của Data Link Layer

Định nghĩa học thuật: Data Link Layer chịu trách nhiệm cho quá trình trao đổi dữ liệu giữa các thiết bị trên cùng một liên kết vật lý hoặc logic, đặc biệt là giữa các Network Interface Card (NIC). Tầng này cho phép dữ...

Ví dụ thực tế: Một IPv4 packet khi đi trong mạng LAN sẽ được đặt vào Ethernet frame. Ethernet frame có MAC nguồn, MAC đích và FCS để kiểm tra lỗi.

- Data Link làm việc với frame. - MAC address thuộc Layer 2. - Data Link có thể phát hiện frame lỗi và loại bỏ frame không hợp lệ.

Nói ngắn gọn: tầng 3 tạo packet, tầng 2 đóng packet vào frame, tầng 1 truyền frame dưới dạng bit.

## 5. Hai phân lớp LLC và MAC trong Data Link Layer

Định nghĩa học thuật: Data Link Layer thường được chia thành hai sublayer: LLC (Logical Link Control) và MAC (Media Access Control). LLC làm việc với tầng Network phía trên, còn MAC phụ trách truy cập môi trường truyề...

Có thể hình dung LLC là quầy tiếp nhận yêu cầu từ tầng trên, còn MAC là bộ phận trực tiếp quyết định dữ liệu sẽ được gói như thế nào và đi xuống đường truyền ra sao.

Ví dụ thực tế: Trong Ethernet, MAC sublayer định nghĩa MAC address, Ethernet frame, cơ chế phát hiện lỗi bằng FCS. Với Wi-Fi, phần MAC cũng tồn tại nhưng cách truy cập môi trường truyền khác Ethernet có dây.

- LLC thường gắn với chuẩn IEEE 802.2. - MAC gắn chặt với từng công nghệ như Ethernet IEEE 802.3, Wireless LAN IEEE 802.11, Bluetooth/PAN. - LLC nói chuyện với Network Layer; MAC nói chuyện với Physical Layer.

Muốn hiểu Ethernet switching, cần tập trung nhiều vào MAC sublayer vì switch lớp 2 ra quyết định dựa trên MAC address.

Bảng 1. Phân biệt LLC và MAC sublayer

## 6. Physical Topology và Logical Topology

Định nghĩa học thuật: Topology là cách mô tả cấu trúc kết nối trong mạng. Physical topology mô tả vị trí thiết bị, dây cáp, cổng kết nối và cách thiết bị được nối vật lý. Logical topology mô tả cách dữ liệu đi trong m...

Physical topology trả lời câu hỏi: thiết bị nằm ở đâu, dây cắm vào cổng nào. Logical topology trả lời câu hỏi: mạng này chia IP như thế nào, dữ liệu đi từ đâu đến đâu, các subnet/VLAN kết nối ra sao.

Ví dụ thực tế: Khi vào một công ty với vai trò quản trị mạng, kỹ thuật viên cần xem cả sơ đồ vật lý và sơ đồ logic. Sơ đồ vật lý giúp tìm switch, router, dây cáp; sơ đồ logic giúp hiểu IP, gateway, đường đi ra Interne...

- Doanh nghiệp nên có hồ sơ mạng gồm ít nhất physical topology và logical topology. - Chỉ có sơ đồ vật lý thì chưa đủ để vận hành mạng. - Chỉ có sơ đồ logic cũng khó xử lý sự cố cáp, port, vị trí thiết bị.

Quản trị mạng cần cả “bản đồ địa điểm” và “bản đồ đường đi dữ liệu”.

Bảng 2. So sánh Physical Topology và Logical Topology

## 7. Point-to-Point, Peer-to-Peer và môi trường Multiaccess

Định nghĩa học thuật: Point-to-point là dạng liên kết điểm-điểm trực tiếp giữa hai node trên một môi trường truyền chuyên biệt, thường gặp trong các kết nối serial/PPP/HDLC ở WAN. Multiaccess là môi trường cho phép nh...

Điểm dễ nhầm là thấy hai thiết bị nối trực tiếp bằng dây Ethernet thì tưởng đó là point-to-point. Theo bài giảng, nếu dùng Ethernet IEEE 802.3 thì bản chất vẫn là môi trường multiaccess, dù lúc đó chỉ có hai thiết bị...

Ví dụ thực tế: Hai router nối với nhau bằng cáp serial và dùng PPP frame là point-to-point thật sự. Nhưng hai PC hoặc hai router nối bằng cổng Gigabit Ethernet vẫn đang dùng công nghệ Ethernet multiaccess.

- Ethernet là công nghệ multiaccess. - Point-to-point thật sự thường gắn với serial/PPP/HDLC, không phải cứ nối hai thiết bị là point-to-point. - Peer-to-peer là mô hình trao đổi, không phải khái niệm thay thế cho poi...

Câu nhớ nhanh: Ethernet = multiaccess; Serial PPP = point-to-point.

Bảng 3. Khái niệm dễ nhầm: Point-to-Point, Peer-to-Peer, Multiaccess

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
| Buổi số | 7 |
| Ngày | Không nêu trong transcript |
| Chủ đề chính | Data Link Layer, Ethernet Frame, MAC Address, ARP, MAC Address Table |
| Nguồn transcript | Buổi 7 - YouTube: https://www.youtube.com/watch?v=EYgbBHJ6HmI |

| Mục | Cách kiểm tra / ghi nhớ |
| --- | --- |
| Chủ đề | Ethernet và Switching |
| Khi làm lab | Đọc yêu cầu, cấu hình từng bước, kiểm tra bằng lệnh show/ping/traceroute |
| Khi lỗi | Kiểm tra IP/subnet, interface, VLAN/routing/ACL liên quan và trạng thái thiết bị |

## 10. Câu hỏi ôn tập

### Lý thuyết

1. Ethernet và Switching giải quyết vấn đề gì trong mạng?
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
| Ethernet | Chuẩn LAN | Công nghệ Layer 2 phổ biến trong mạng có dây. |
| Switch | Bộ chuyển mạch | Thiết bị Layer 2 chuyển frame dựa vào MAC address. |
| CLI | Dòng lệnh | Giao diện nhập lệnh cấu hình và kiểm tra thiết bị. |
| Interface | Cổng mạng | Điểm kết nối logic hoặc vật lý trên thiết bị. |
| Gateway | Cổng ra mạng khác | Địa chỉ thiết bị chuyển tiếp traffic ra ngoài subnet. |

## 12. Ghi nhớ nhanh

🔑 Ethernet và Switching nên được học cùng lab Packet Tracer để thấy rõ tác dụng thực tế.

🔑 Luôn kiểm tra bằng lệnh show, ping hoặc traceroute thay vì chỉ nhìn cấu hình.

🔑 Khi troubleshooting, đi từ Layer 1/2 lên Layer 3/4 để tránh bỏ sót lỗi nền.

⚠️ Không copy cấu hình máy móc; cần hiểu địa chỉ, interface và chiều traffic.

## Tham khảo

- CCNA 200-301 Official Cert Guide
- Cisco Networking Academy - CCNA course materials

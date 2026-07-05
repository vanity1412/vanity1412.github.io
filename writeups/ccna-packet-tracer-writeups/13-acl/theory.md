---
layout: page-toc
title: "CCNA 13 - Lý thuyết tổng hợp ACL"
permalink: /writeups/ccna-packet-tracer-writeups/13-acl/theory/
toc: true
---

## Phần 1: Tổng quan về chủ đề

Chủ đề **ACL** trong CCNA giúp người học hiểu cách một mảng kiến thức mạng vận hành trong Packet Tracer và trong mạng doanh nghiệp nhỏ. Trọng tâm của track này là lọc traffic bằng standard ACL, named ACL, extended ACL, wildcard mask, implicit deny và placement inbound/outbound. Nếu chỉ làm theo từng bước của lab, bạn có thể hoàn thành bài nhưng vẫn chưa nhìn ra logic chung. Vì vậy trang này gom lại kiến thức nền, quy trình kiểm tra và các lỗi lặp lại trong toàn bộ lab của track.

Về roadmap, hãy học theo thứ tự từ quan sát đến cấu hình, rồi từ cấu hình đến troubleshooting. Lab đầu thường giúp nhận diện hiện tượng hoặc công nghệ, các lab giữa đi vào cấu hình chi tiết, còn lab cuối thường yêu cầu triển khai tổng hợp hoặc sửa lỗi. Khi đọc một lab, luôn tự hỏi: traffic đi từ đâu đến đâu, thiết bị nào quyết định đường đi, lệnh nào chứng minh trạng thái đúng, và lỗi nào có thể làm kết quả sai.

Chủ đề này cũng liên hệ với các phần CCNA khác như IP addressing, switching, routing, security, wireless, quản trị mạng và troubleshooting. Một cấu hình nhỏ sai interface, sai gateway, sai VLAN, sai route, sai policy hoặc thiếu service phụ trợ đều có thể làm toàn bộ kết nối thất bại.

## Phần 2: Các khái niệm cốt lõi

- **ACL xử lý rule từ trên xuống**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Standard ACL lọc chủ yếu theo source IP**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Extended ACL lọc source, destination, protocol và port**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Wildcard mask là mask đảo so với subnet mask**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Cuối ACL luôn có implicit deny**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **ACL phải được apply đúng interface và đúng chiều**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.

| Khái niệm | Ý nghĩa | Cách kiểm chứng |
| --- | --- | --- |
| ACL xử lý rule từ trên xuống | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Standard ACL lọc chủ yếu theo source IP | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Extended ACL lọc source, destination, protocol và port | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Wildcard mask là mask đảo so với subnet mask | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Cuối ACL luôn có implicit deny | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| ACL phải được apply đúng interface và đúng chiều | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |

> **💡 Lưu ý**: Đừng học thuộc lệnh một cách rời rạc. Với mỗi khái niệm, hãy biết nó giải quyết vấn đề gì, nằm ở lớp nào, và output đúng phải trông như thế nào.

## Phần 3: Nguyên lý hoạt động & quy trình

Quy trình chung khi làm các lab trong track này:

1. Đọc topology, xác định thiết bị, interface và vai trò từng đoạn mạng.
2. Ghi lại bảng thông số cần cấu hình: địa chỉ, VLAN, route, policy, service hoặc tham số bảo mật.
3. Cấu hình phần nền trước, ví dụ hostname, interface, IP, VLAN, gateway hoặc service bắt buộc.
4. Cấu hình tính năng chính của chủ đề.
5. Kiểm tra local bằng lệnh show hoặc GUI Packet Tracer.
6. Kiểm tra end-to-end bằng ping, traceroute, web/client test hoặc bảng trạng thái.
7. Nếu lỗi, khoanh vùng theo lớp: physical -> data link -> network -> service/policy.
8. Lưu cấu hình và ghi lại bằng chứng hoàn thành.

| Giai đoạn | Câu hỏi cần trả lời | Bằng chứng mong muốn |
| --- | --- | --- |
| Thiết kế | Thiết bị/interface nào tham gia? | Topology và bảng yêu cầu rõ ràng |
| Cấu hình | Lệnh đã nhập đúng mode và đúng interface chưa? | show running-config hoặc GUI đúng |
| Trạng thái | Link, protocol hoặc service đã hoạt động chưa? | Output show đúng kỳ vọng |
| Kiểm tra | Traffic thật có đi được không? | Ping/traceroute/client test thành công |
| Debug | Lỗi nằm ở lớp nào? | Sửa một điểm rồi kiểm tra lại |

## Phần 4: Công thức & cách tính toán

Các lab trong track này thường dùng các quy tắc kiểm tra hơn là công thức toán học thuần túy. Bảng dưới là bộ quy tắc nên áp dụng:

| Quy tắc | Cách áp dụng |
| --- | --- |
| Kiểm tra từ gần đến xa | Host -> gateway -> next-hop -> remote host/service |
| So khớp hai đầu | Trunk, EtherChannel, WAN, neighbor, WLAN hoặc NAT phải khớp logic |
| Xác định chiều traffic | Ghi rõ source, destination, ingress interface và egress interface |
| Ưu tiên trạng thái trước nội dung | Interface/service phải up trước khi debug rule chi tiết |
| Đọc bảng trạng thái | Neighbor, route, binding, translation, session hoặc association là bằng chứng vận hành |

Các lệnh/công cụ thường gặp:

~~~text
access-list permit
access-list deny
ip access-list standard
ip access-list extended
permit tcp eq
deny ip any any
ip access-group in
ip access-group out
show access-lists
show ip interface
~~~
## Phần 5: Các trường hợp thường gặp

- **Cấu hình đúng ý nhưng sai interface**: đối chiếu topology và tên port trước khi sửa.
- **Local test thành công nhưng end-to-end fail**: kiểm tra gateway, route, policy, NAT, ACL, trunk, service hoặc controller ở giữa đường đi.
- **Output không đúng kỳ vọng**: so sánh show running-config với yêu cầu lab thay vì xóa cấu hình hàng loạt.
- **Lab có thiết bị cấu hình sẵn**: đọc phần đã có trước khi ghi đè.
- **Ping fail lần đầu**: có thể do ARP/ND hoặc convergence; kiểm tra trạng thái rồi thử lại có kiểm soát.
- **Packet Tracer chưa đạt điểm**: ngoài connectivity, hãy kiểm tra tên thiết bị, mô tả interface, password, lưu cấu hình và các yêu cầu nhỏ.

## Phần 6: Lỗi thường gặp & cách debug

| Lỗi thường gặp | Cách phát hiện | Cách sửa |
| --- | --- | --- |
| Quên implicit deny làm chặn ngoài ý muốn | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Đặt deny trước permit cần thiết | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Wildcard mask sai | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Apply sai interface hoặc sai direction | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Dùng standard ACL quá xa destination | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Quên permit traffic còn lại | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |

Checklist troubleshooting:

| Bước | Việc cần làm | Công cụ/lệnh |
| ---: | --- | --- |
| 1 | Xác định source, destination và triệu chứng | Ghi test case cụ thể |
| 2 | Kiểm tra vật lý/interface | `show ip interface brief`, `show interfaces`, trạng thái port |
| 3 | Kiểm tra cấu hình local | show running-config, bảng địa chỉ, GUI config |
| 4 | Kiểm tra tính năng chính | Lệnh show chuyên biệt theo chủ đề |
| 5 | Kiểm tra traffic | `ping`, `traceroute`, web/client test |
| 6 | Sửa từng thay đổi nhỏ | Test lại sau mỗi lần sửa |

> **⚠️ Cảnh báo**: Không sửa nhiều thứ cùng lúc. Nếu sửa hàng loạt, bạn sẽ khó biết thay đổi nào thật sự giải quyết lỗi.

## Phần 7: Best practices & tips

> **✅ Best Practice**: Trước khi nhập lệnh, hãy viết bảng nhỏ gồm thiết bị, interface, thông số cần cấu hình, lệnh kiểm tra và kết quả mong muốn.

Luôn kiểm tra từ gần đến xa. Nếu host chưa ping được gateway, chưa cần xem router ở xa. Nếu trunk chưa mang VLAN, chưa cần debug default gateway. Nếu NAT chưa có translation, hãy tạo traffic đúng ACL NAT trước. Nếu OSPF chưa có neighbor, đừng vội chỉnh cost. Cách suy nghĩ này giúp bạn làm lab nhanh hơn và giống quy trình của network engineer thực tế.

Khi hoàn tất, lưu cấu hình, chụp hoặc ghi lại output quan trọng. Những bằng chứng như show, bảng route, bảng VLAN, NAT translation, DHCP binding, OSPF neighbor hoặc ping/traceroute thành công sẽ giúp bạn ôn lại rất nhanh.

## Phần 8: Liên kết với các lab

| Lab | File |
| --- | --- |
| 5.1.8 Packet Tracer - Configure Numbered Standard IPv4 ACLs | `labs/lab-01/index.md` |
| 5.1.9 Packet Tracer - Configure Named Standard IPv4 ACLs | `labs/lab-02/index.md` |
| 5.2.7 Packet Tracer - Configure and Modify Standard IPv4 ACLs | `labs/lab-03/index.md` |
| 5.4.12 Packet Tracer - Configure Extended IPv4 ACLs - Scenario 1 | `labs/lab-04/index.md` |
| 5.4.13 Packet Tracer - Configure Extended IPv4 ACLs - Scenario 2 | `labs/lab-05/index.md` |

Thứ tự học đề xuất là đi đúng thứ tự lab trong track. Lab đầu xây nền tảng, lab giữa luyện cấu hình, lab cuối thường là bài tổng hợp hoặc thử thách nâng cao.

## Phần 9: Tài liệu tham khảo

- Cisco Networking Academy Packet Tracer activities trong track này.
- Cisco IOS Command Reference và Cisco configuration guides theo chủ đề.
- Cisco Packet Tracer documentation.
- Các chuẩn/RFC phổ biến khi liên quan: IEEE 802.1Q, IEEE 802.11, RFC 2131 DHCP, RFC 2328 OSPFv2, RFC 3022 NAT, RFC 5905 NTP.

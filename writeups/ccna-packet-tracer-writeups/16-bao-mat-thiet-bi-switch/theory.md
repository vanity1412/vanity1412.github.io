---
layout: page-toc
title: "CCNA 16 - Lý thuyết tổng hợp Bảo mật thiết bị và switch"
permalink: /writeups/ccna-packet-tracer-writeups/16-bao-mat-thiet-bi-switch/theory/
toc: true
---

## Phần 1: Tổng quan về chủ đề

Chủ đề **Bảo mật thiết bị và switch** trong CCNA giúp người học hiểu cách một mảng kiến thức mạng vận hành trong Packet Tracer và trong mạng doanh nghiệp nhỏ. Trọng tâm của track này là bảo vệ management plane bằng password/SSH và bảo vệ access port bằng port security. Nếu chỉ làm theo từng bước của lab, bạn có thể hoàn thành bài nhưng vẫn chưa nhìn ra logic chung. Vì vậy trang này gom lại kiến thức nền, quy trình kiểm tra và các lỗi lặp lại trong toàn bộ lab của track.

Về roadmap, hãy học theo thứ tự từ quan sát đến cấu hình, rồi từ cấu hình đến troubleshooting. Lab đầu thường giúp nhận diện hiện tượng hoặc công nghệ, các lab giữa đi vào cấu hình chi tiết, còn lab cuối thường yêu cầu triển khai tổng hợp hoặc sửa lỗi. Khi đọc một lab, luôn tự hỏi: traffic đi từ đâu đến đâu, thiết bị nào quyết định đường đi, lệnh nào chứng minh trạng thái đúng, và lỗi nào có thể làm kết quả sai.

Chủ đề này cũng liên hệ với các phần CCNA khác như IP addressing, switching, routing, security, wireless, quản trị mạng và troubleshooting. Một cấu hình nhỏ sai interface, sai gateway, sai VLAN, sai route, sai policy hoặc thiếu service phụ trợ đều có thể làm toàn bộ kết nối thất bại.

## Phần 2: Các khái niệm cốt lõi

- **Management plane cần được bảo vệ bằng password mạnh**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **`enable secret` an toàn hơn password plain text**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **SSH an toàn hơn Telnet**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Local user, domain name và RSA key phục vụ SSH**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Port Security giới hạn MAC trên access port**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Violation mode protect, restrict, shutdown**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.
- **Tắt port không dùng để giảm bề mặt tấn công**: cần hiểu bản chất, lệnh kiểm tra và dấu hiệu đúng/sai trong lab.

| Khái niệm | Ý nghĩa | Cách kiểm chứng |
| --- | --- | --- |
| Management plane cần được bảo vệ bằng password mạnh | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| `enable secret` an toàn hơn password plain text | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| SSH an toàn hơn Telnet | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Local user, domain name và RSA key phục vụ SSH | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Port Security giới hạn MAC trên access port | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |
| Violation mode protect, restrict, shutdown | Vai trò cốt lõi của chủ đề | Kiểm tra bằng lệnh/GUI phù hợp trong Packet Tracer |

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
enable secret
service password-encryption
username secret
ip domain-name
crypto key generate rsa
ip ssh version 2
transport input ssh
login local
switchport port-security
switchport port-security mac-address sticky
show port-security
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
| Quên domain name nên không tạo RSA key | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| VTY vẫn cho Telnet | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Thiếu `login local` | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Port security cấu hình trên trunk | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| MAC violation làm port err-disabled | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |
| Không shutdown port unused | Đối chiếu topology, cấu hình và output kiểm tra | Sửa đúng điểm gây lỗi rồi test lại từ gần đến xa |

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
| 1.3.6 Packet Tracer - Configure SSH | `labs/lab-01/index.md` |
| 11.1.10 Packet Tracer - Implement Port Security | `labs/lab-02/index.md` |
| 11.6.1 Packet Tracer - Switch Security Configuration | `labs/lab-03/index.md` |
| 16.4.6 Packet Tracer - Configure Secure Passwords and SSH [ccna-lap-s2] | `labs/lab-04/index.md` |
| 16.4.6 Packet Tracer - Configure Secure Passwords and SSH [S1_ITN v7 Packet Tracer Activity Source Files] | `labs/lab-05/index.md` |
| 16.5.1 Packet Tracer - Secure Network Devices | `labs/lab-06/index.md` |

Thứ tự học đề xuất là đi đúng thứ tự lab trong track. Lab đầu xây nền tảng, lab giữa luyện cấu hình, lab cuối thường là bài tổng hợp hoặc thử thách nâng cao.

## Phần 9: Tài liệu tham khảo

- Cisco Networking Academy Packet Tracer activities trong track này.
- Cisco IOS Command Reference và Cisco configuration guides theo chủ đề.
- Cisco Packet Tracer documentation.
- Các chuẩn/RFC phổ biến khi liên quan: IEEE 802.1Q, IEEE 802.11, RFC 2131 DHCP, RFC 2328 OSPFv2, RFC 3022 NAT, RFC 5905 NTP.

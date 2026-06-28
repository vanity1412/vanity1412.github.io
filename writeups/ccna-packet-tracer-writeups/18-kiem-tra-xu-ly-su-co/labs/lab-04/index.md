---
layout: page-toc
title: "CCNA 18.04 - 17.5.9 Packet Tracer - Interpret show Command Output"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `17.5.9 Packet Tracer - Interpret show Command Output.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Quan sát output IOS, ghi ý nghĩa các lệnh `show`, trả lời reflection questions |

> **Đặc điểm bài lab:** Bài này không yêu cầu cấu hình thiết bị. Mục tiêu chính là truy cập `ISPRouter`, chạy các lệnh `show`, đọc output và hiểu mỗi lệnh dùng để kiểm tra phần nào của router.

## 1. Mục Tiêu Bài Lab

- Truy cập `ISPRouter` từ `ISP PC` bằng Terminal.
- Vào privileged EXEC mode để chạy các lệnh kiểm tra.
- Phân tích output của các lệnh `show` thường dùng trên Cisco IOS.
- Xác định lệnh nào dùng để xem IP interface, trạng thái interface, routing table, IOS version, flash, user line và thống kê traffic.
- Ghi lại câu trả lời cho phần Reflection Questions.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-04/topology.png)

## 2. Topology Và Quan Sát Ban Đầu

| Thành phần | Ghi chú |
| --- | --- |
| Thiết bị chính | `ISPRouter` |
| Thiết bị truy cập CLI | `ISP PC` dùng Terminal/console để vào router |
| Thiết bị trong LAN | `Switch0`, `ISP Server` |
| Kết nối WAN | `ISPRouter` kết nối ra `Internet` |
| Dạng bài | Quan sát / nhận diện output, không cấu hình |

> **Lưu ý:** Console từ `ISP PC` vào `ISPRouter` chỉ dùng để quản trị thiết bị, không phải đường truyền dữ liệu cần kiểm tra bằng `ping`.

## 3. Kế Hoạch Làm Bài

| Bước | Việc cần làm | Ghi chú |
| --- | --- | --- |
| 1 | Mở `ISP PC` → Desktop → Terminal | Dùng kết nối console có sẵn |
| 2 | Vào privileged EXEC mode | Lệnh `enable` |
| 3 | Chạy lần lượt các lệnh `show` trong đề | Nhấn `Space` nếu gặp `--More--` |
| 4 | Ghi lại chức năng chính của từng lệnh | Tập trung vào IP, interface, route, flash, IOS |
| 5 | Trả lời Reflection Questions | Dựa trên output quan sát được |

## 4. Part 1 - Analyze Show Command Output

### Bước 1: Truy cập ISPRouter từ ISP PC

```text
ISP PC > Desktop > Terminal

ISPRouter> enable
ISPRouter#
```

> **Lưu ý:** Trong bài này mình không cần vào global configuration mode vì không sửa cấu hình. Nếu prompt đang là `ISPRouter(config)#` thì gõ `end` để quay về `ISPRouter#`.

### Bước 2: Chạy các lệnh show được yêu cầu

```text
ISPRouter# show arp
ISPRouter# show flash:
ISPRouter# show ip route
ISPRouter# show interfaces
ISPRouter# show ip interface brief
ISPRouter# show protocols
ISPRouter# show users
ISPRouter# show version
```

> **Lưu ý:** Nếu router dừng ở dòng `--More--`, nhấn `Space` để xem tiếp toàn bộ output. Nếu nhấn `Enter` thì chỉ đi từng dòng, dễ bỏ sót thông tin cần trả lời.

![Show commands lab 04](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-04/show-commands.png)

## 5. Bảng Ghi Nhớ Lệnh Show

| Lệnh | Dùng để xem gì | Dấu hiệu cần chú ý |
| --- | --- | --- |
| `show arp` | Bảng ánh xạ IPv4 ↔ MAC trên các mạng trực tiếp | IP, MAC, interface học được ARP |
| `show flash:` | File trong flash và dung lượng flash | IOS image, bytes used/free |
| `show ip route` | Bảng định tuyến IPv4 | Route connected/static/default, gateway of last resort |
| `show interfaces` | Thông tin chi tiết từng interface | Line protocol, IP/prefix, bandwidth, duplex, speed, traffic counters |
| `show ip interface brief` | Tóm tắt interface, IP, status/protocol | Interface nào `up/up`, IP nào gán cho interface nào |
| `show protocols` | Trạng thái giao thức L3 trên interface | Interface up/down, Internet address và prefix |
| `show users` | Người dùng/line đang truy cập router | Console, vty, vị trí dòng có dấu `*` |
| `show version` | IOS version, uptime, image, memory, config register | IOS image, RAM, NVRAM, flash, configuration register |

> **Điểm dễ nhầm:** `show ip interface brief` rất nhanh để xem IP và trạng thái, nhưng không hiển thị prefix/subnet mask. Muốn biết prefix thì dùng `show interfaces` hoặc `show protocols`.

## 6. Part 2 - Reflection Questions

| Câu hỏi | Câu trả lời ngắn |
| --- | --- |
| 1. Lệnh nào xác định IP address và network prefix của interface? | `show interfaces` và `show protocols`. Có thể dùng thêm `show ip route` để suy ra prefix của mạng connected. |
| 2. Lệnh nào cung cấp IP address và interface assignment nhưng không có prefix? | `show ip interface brief`. |
| 3. Lệnh nào dùng để xác định interface có đang up không? | `show ip interface brief`, `show interfaces`, `show protocols`. |
| 4. Lệnh nào xem IOS version đang chạy? | `show version`. |
| 5. Lệnh nào cung cấp thông tin địa chỉ của router interface? | `show ip interface brief`, `show interfaces`, `show protocols`. |
| 6. Lệnh nào xem flash có đủ chứa IOS mới không? | `show flash:` và `show version`. |
| 7. Lệnh nào xem line đang được dùng để cấu hình/giám sát thiết bị? | `show users`. |
| 8. Lệnh nào xem thống kê traffic/performance của interface? | `show interfaces`. |
| 9. Lệnh nào xem các path/route có sẵn cho network traffic? | `show ip route`. |
| 10. Interface nào đang active trên ISP Router? | Xem các dòng `up/up` trong `show ip interface brief`. Trong topology này thường là interface nối xuống LAN/Switch và interface nối ra Internet. |

> **Ghi chú cho câu 10:** Không nên trả lời theo cảm tính từ hình topology. Cách đúng là lấy interface có cả `Status` và `Protocol` đều là `up` trong output `show ip interface brief`.

![Show ip interface brief lab 04](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-04/show-ip-interface-brief.png)

## 7. Mapping Nhanh Theo Nhu Cầu Troubleshooting

| Nhu cầu kiểm tra | Lệnh ưu tiên | Vì sao dùng lệnh này |
| --- | --- | --- |
| Xem router có route tới mạng đích không | `show ip route` | Cho biết route connected/static/default |
| Xem cổng có bị down không | `show ip interface brief` | Nhanh, gọn, dễ thấy `up/down` |
| Xem lỗi traffic/counter trên interface | `show interfaces` | Có packet count, error, duplex, speed |
| Xem file IOS trong flash | `show flash:` | Liệt kê file và dung lượng còn trống |
| Xem phiên bản IOS | `show version` | Có IOS image/version và thông tin phần cứng |
| Xem ai đang đăng nhập router | `show users` | Hiển thị console/vty line đang active |

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Không thấy đủ output | Dừng ở `--More--` nhưng không nhấn tiếp | Output bị ngắt giữa chừng | Nhấn `Space` đến khi về lại prompt `ISPRouter#` |
| Nhầm `show ip interface brief` có prefix | Lệnh này chỉ hiển thị IP, status, protocol | Không thấy `/24`, `/30` hoặc subnet mask | Dùng `show interfaces` hoặc `show protocols` |
| Trả lời câu active interface theo hình | Nhìn topology nhưng không đối chiếu CLI | Có thể sai nếu cổng shutdown/down | Dựa vào dòng `up/up` trong `show ip interface brief` |
| Nhầm `show arp` là bảng route | ARP chỉ ánh xạ IP-MAC trong LAN | Không có network path/default route | Dùng `show ip route` để xem đường đi |
| Nhầm `show users` với user account | `show users` xem line/session, không xem username database | Output hiện console/vty line | Dùng đúng mục đích: kiểm tra ai đang truy cập |

## 9. Kết Quả Cuối

| Nội dung kiểm tra | Kết quả mong muốn |
| --- | --- |
| Truy cập `ISPRouter` | Vào được prompt `ISPRouter#` |
| Chạy đủ 8 lệnh show | Có output đầy đủ, không bỏ sót do `--More--` |
| Xác định IP/interface/status | Dùng đúng `show ip interface brief`, `show interfaces`, `show protocols` |
| Xác định route/path | Dùng đúng `show ip route` |
| Xác định IOS/flash/user/traffic | Dùng đúng `show version`, `show flash:`, `show users`, `show interfaces` |
| Hoàn thành Reflection Questions | Trả lời đúng chức năng từng lệnh |

Checklist ảnh minh chứng nên chụp:

- [ ] `topology.png` - sơ đồ bài lab.
- [ ] `terminal-access.png` - truy cập `ISPRouter#` từ ISP PC.
- [ ] `show-ip-interface-brief.png` - output interface/IP/status.
- [ ] `show-interfaces.png` - output chi tiết interface.
- [ ] `show-ip-route.png` - bảng định tuyến.
- [ ] `show-version-flash.png` - IOS version và flash.
- [ ] `reflection-answers.png` - bảng câu trả lời cuối.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/">Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/">Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/">Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/">Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/">Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge</a></li>
    </ul>
  </details>
</div>

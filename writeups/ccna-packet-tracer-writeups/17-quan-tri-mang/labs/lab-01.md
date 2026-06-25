---
layout: page-toc
title: "CCNA 17.01 - 10.1.5 Packet Tracer - Use CDP to Map a Network"
permalink: /writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-01/
toc: true
---

[← Quay lại danh sách Quản Trị Mạng](/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/)

| Field | Value |
| --- | --- |
| Dạng lab | Quản Trị Mạng |
| File lab | `10.1.5 Packet Tracer - Use CDP to Map a Network.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `images/lab-01/` |

## 1. Mục Tiêu Bài Lab

Ghi lại yêu cầu chính của bài: cần cấu hình gì, cần kiểm tra gì, thiết bị nào liên quan và tiêu chí hoàn thành là gì.

## 2. Topology Và Quan Sát Ban Đầu

Đặt ảnh chụp cho bài này vào `images/lab-01/`. Ví dụ:

~~~md
![Topology lab 01](../images/lab-01/topology.png)
![Instructions lab 01](../images/lab-01/instructions.png)
~~~

| Thành phần | Ghi chú |
| --- | --- |
| Thiết bị chính |  |
| Kết nối quan trọng |  |
| VLAN/Subnet/Route liên quan |  |
| Điểm dễ sai |  |

## 3. Kế Hoạch Làm Bài

| Bước | Việc cần làm | Ghi chú |
| --- | --- | --- |
| 1 | Đọc yêu cầu và đánh dấu dữ kiện |  |
| 2 | Lập bảng địa chỉ/cổng/VLAN/route nếu có |  |
| 3 | Cấu hình từng thiết bị theo thứ tự |  |
| 4 | Kiểm tra từng phần trước khi làm tiếp |  |
| 5 | Chạy kiểm tra cuối cùng và ghi kết quả |  |

## 4. Cấu Hình Từng Bước

### Thiết bị 1

~~~txt
! Dán cấu hình hoặc ghi từng lệnh sau khi làm lab
~~~

### Thiết bị 2

~~~txt
! Bổ sung khi bài có nhiều router/switch/server/client
~~~

## 5. Kiểm Tra Và Bằng Chứng

Các lệnh nên dùng cho dạng này:

- `show cdp neighbors detail`
- `show lldp neighbors detail`
- `show ntp status`
- `copy running-config tftp`

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
|  |  |  |

## 6. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
|  |  |  |  |

## 7. Kết Quả Cuối

Ghi điểm Check Results, trạng thái ping/traceroute hoặc ảnh xác nhận hoàn thành.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 10.1.5 Packet Tracer - Use CDP to Map a Network (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-02/">Lab 2: 10.2.6  Packet Tracer - Use LLDP to Map a Network</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-03/">Lab 3: 10.3.4 Packet Tracer - Configure and Verify NTP</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-04/">Lab 4: 10.6.10 Packet Tracer - Back Up Configuration Files</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-05/">Lab 5: 10.7.6 Packet Tracer - Use a TFTP Server to Upgrade a Cisco IOS Image</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/lab-06/">Lab 6: 10.8.1 Packet Tracer - Configure CDP, LLDP, and NTP</a></li>
    </ul>
  </details>
</div>

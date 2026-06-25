---
layout: page-toc
title: "CCNA 03.03 - 9.2.9 Packet Tracer - Examine the ARP Table"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/
toc: true
---

# CCNA 03.03 - 9.2.9 Packet Tracer - Examine the ARP Table

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `9.2.9 Packet Tracer - Examine the ARP Table.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `images/lab-03/` |

## 1. Mục Tiêu Bài Lab

Ghi lại yêu cầu chính của bài: cần cấu hình gì, cần kiểm tra gì, thiết bị nào liên quan và tiêu chí hoàn thành là gì.

## 2. Topology Và Quan Sát Ban Đầu

Đặt ảnh chụp cho bài này vào `images/lab-03/`. Ví dụ:

~~~md
![Topology lab 03](../images/lab-03/topology.png)
![Instructions lab 03](../images/lab-03/instructions.png)
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

- `arp -a`
- `ipconfig /all`
- `ping`
- `Simulation event list`

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
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/">Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/">Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/">Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/">Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications</a></li>
    </ul>
  </details>
</div>

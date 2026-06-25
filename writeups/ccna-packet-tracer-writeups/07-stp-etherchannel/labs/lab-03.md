---
layout: page-toc
title: "CCNA 07.03 - 6.3.4 Packet Tracer - Troubleshoot EtherChannel"
permalink: /writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-03/
toc: true
---

# CCNA 07.03 - 6.3.4 Packet Tracer - Troubleshoot EtherChannel

[← Quay lại danh sách STP Và EtherChannel](/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/)

| Field | Value |
| --- | --- |
| Dạng lab | STP Và EtherChannel |
| File lab | `6.3.4 Packet Tracer - Troubleshoot EtherChannel.pka` |
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

- `show spanning-tree`
- `show etherchannel summary`
- `show interfaces trunk`

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
    <div><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 4 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-01/">Lab 1: 5.1.9 Packet Tracer - Investigate STP Loop Prevention</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-02/">Lab 2: 6.2.4 Packet Tracer - Configure EtherChannel</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 6.3.4 Packet Tracer - Troubleshoot EtherChannel (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/lab-04/">Lab 4: 6.4.1 Packet Tracer - Implement Etherchannel</a></li>
    </ul>
  </details>
</div>

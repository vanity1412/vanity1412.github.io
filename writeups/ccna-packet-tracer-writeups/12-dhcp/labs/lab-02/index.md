---
layout: page-toc
title: "CCNA 12.02 - 7.4.1 Packet Tracer - Implement DHCPv4"
permalink: /writeups/ccna-packet-tracer-writeups/12-dhcp/lab-02/
toc: true
---

[← Quay lại danh sách DHCP](/writeups/ccna-packet-tracer-writeups/12-dhcp/)

| Field | Value |
| --- | --- |
| Dạng lab | DHCP |
| File lab | `7.4.1 Packet Tracer - Implement DHCPv4.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |

## 1. Mục Tiêu Bài Lab

Ghi lại yêu cầu chính của bài: cần cấu hình gì, cần kiểm tra gì, thiết bị nào liên quan và tiêu chí hoàn thành là gì.

## 2. Topology Và Quan Sát Ban Đầu

Đặt ảnh chụp cho bài này vào `labs/lab-02/`. Ví dụ:

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/12-dhcp/labs/lab-02/topology.png)
![Instructions lab 02](/writeups/ccna-packet-tracer-writeups/12-dhcp/labs/lab-02/instructions.png)

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

- `show ip dhcp binding`
- `show ip dhcp pool`
- `ipconfig /all`

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
    <div><a href="/writeups/ccna-packet-tracer-writeups/12-dhcp/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/12-dhcp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 2 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/12-dhcp/lab-01/">Lab 1: 7.2.10 Packet Tracer - Configure DHCPv4</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 7.4.1 Packet Tracer - Implement DHCPv4 (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

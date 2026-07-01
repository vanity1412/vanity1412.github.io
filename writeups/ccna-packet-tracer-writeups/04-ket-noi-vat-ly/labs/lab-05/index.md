---
layout: page-toc
title: "CCNA 04.05 - 4.7.1 Packet Tracer - Connect the Physical Layer"
permalink: /writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/
toc: true
---

[← Quay lại danh sách Kết Nối Vật Lý](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/)

| Field | Value |
| --- | --- |
| Dạng lab | Kết Nối Vật Lý |
| File lab | `4.7.1 Packet Tracer - Connect the Physical Layer.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Xác định cổng vật lý, gắn module, nối đúng loại cáp và kiểm tra kết nối |

> **Đặc điểm chính:** Bài này không tập trung cấu hình IP từ đầu mà tập trung vào tầng vật lý: nhận diện cổng quản trị, cổng LAN/WAN, chọn đúng module mở rộng, chọn đúng loại cáp và kiểm tra trạng thái interface sau khi nối thiết bị.

## 1. Mục Tiêu Bài Lab

- Nhận diện các cổng quản trị, cổng LAN/WAN và khe mở rộng trên router/switch.
- Chọn đúng module để mở rộng cổng cho East router và Switch2.
- Nối thiết bị bằng đúng loại cáp theo yêu cầu của bài.
- Kiểm tra trạng thái interface bằng `show ip interface brief`.
- Kiểm tra kết nối web từ Laptop, TabletPC và các PC trong mô hình.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/topology.png)

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/topology1.png)

## 2. Bảng Interface Và Địa Chỉ Kiểm Tra

| Thiết bị | Interface | IP Address | Trạng thái mong muốn |
| --- | --- | --- | --- |
| East | GigabitEthernet0/0 | 172.30.1.1 | up/up |
| East | GigabitEthernet0/1 | 172.31.1.1 | up/up |
| East | Serial0/0/0 | 10.10.10.1 | up/up |
| East | Serial0/0/1 | unassigned | down/down |
| East | FastEthernet0/1/0 | unassigned | up/up |
| East | FastEthernet0/1/1 | unassigned | up/up |
| East | FastEthernet0/1/2 | unassigned | up/up |
| East | FastEthernet0/1/3 | unassigned | up/down |
| East | Vlan1 | 172.29.1.1 | up/up |

> **Lưu ý:** `Vlan1` là interface ảo trong phần mềm, không phải cổng vật lý. Khi bài hỏi số lượng physical interfaces, không tính `Vlan1`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Router trung tâm | East | Cần kiểm tra cổng quản trị, cổng LAN/WAN và gắn module `HWIC-4ESW` để nối PC1, PC2, PC3 |
| Nhánh bên trái | West, Cluster0, Cell Tower0 | East kết nối WAN sang West bằng Serial DCE |
| LAN bên trái | Switch1, PC4, PC5, PC6 | Switch1 nối về East và chia kết nối xuống các PC |
| LAN bên phải | Switch4, Switch3, Switch2, PC7, PC8, PC9 | Có kết nối đồng, kết nối chéo và kết nối quang giữa các switch |
| Wireless | Access Point, Laptop, TabletPC | Laptop/TabletPC kiểm tra web qua wireless; TabletPC đổi sang 3G/4G Cell1 ở bước sau |
| Server | DHCP Server | Dùng để cấp phát/tham gia mạng phục vụ kiểm tra kết nối |

> **Điểm dễ sai:** Bài có nhiều loại cáp khác nhau. Không nên dùng Auto-Connect nếu bài yêu cầu tự chọn cáp, vì mục tiêu là hiểu đúng loại kết nối vật lý.

## 4. Part 1 - Identify Physical Characteristics of Internetworking Devices

### Step 1 - Xác định management ports trên East router

| Câu hỏi | Trả lời |
| --- | --- |
| Which management ports are available? | `AUX` và `Console` |

![East router physical ports](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/east-physical-ports.png)

### Step 2 - Xác định LAN/WAN interfaces trên East router

| Câu hỏi | Trả lời |
| --- | --- |
| East router có LAN/WAN interfaces nào? | 2 cổng Gigabit Ethernet và 2 cổng Serial WAN |
| Số physical interfaces được liệt kê ban đầu? | 4 physical interfaces |
| Default bandwidth của `GigabitEthernet0/0` | `1000000 Kbit` |
| Default bandwidth của `Serial0/0/0` | `1544 Kbit` |

```text
East> show ip interface brief

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     172.30.1.1      YES manual up                    up
GigabitEthernet0/1     172.31.1.1      YES manual up                    up
Serial0/0/0            10.10.10.1      YES manual up                    up
Serial0/0/1            unassigned      YES unset  down                  down
Vlan1                  172.29.1.1      YES manual up                    up
```

```text
East> show interface gigabitethernet 0/0
! BW 1000000 Kbit

East> show interface serial 0/0/0
! BW 1544 Kbit
```

> **Lưu ý:** Bandwidth trên Serial interface thường được routing protocol dùng để tính toán đường đi. Nó không nhất thiết phản ánh tốc độ thực tế của đường truyền vật lý.

![East show interface](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/east-show-interface.png)

### Step 3 - Xác định expansion slots

| Thiết bị | Số khe mở rộng | Ghi chú |
| --- | --- | --- |
| East router | 1 slot | Dùng để gắn module mở rộng cổng Ethernet |
| Switch2 | 5 slots | Dùng để gắn module kết nối quang Gigabit |

## 5. Part 2 - Select Correct Modules for Connectivity

### Step 1 - Chọn module phù hợp

| Nhu cầu | Module cần chọn | Kết quả |
| --- | --- | --- |
| Kết nối PC1, PC2, PC3 trực tiếp vào East router khi không mua thêm switch | `HWIC-4ESW` | Cung cấp 4 cổng switch FastEthernet |
| Tạo kết nối Gigabit optical từ Switch2 đến Switch3 | `PT-SWITCH-NM-1FGE` | Cung cấp cổng Gigabit Ethernet quang |

> **Lưu ý:** `HWIC-4ESW` hoạt động như module switch 4 cổng trên router, phù hợp để nối nhiều host trực tiếp vào router trong lab này.

### Step 2 - Gắn module và bật nguồn thiết bị

| Thiết bị | Thao tác | Kết quả cần đạt |
| --- | --- | --- |
| East | Tắt nguồn, kéo `HWIC-4ESW` vào slot trống, bật nguồn lại | Xuất hiện các cổng `FastEthernet0/1/0` đến `FastEthernet0/1/3` |
| Switch2 | Tắt nguồn, kéo `PT-SWITCH-NM-1FGE` vào slot ngoài cùng bên phải, bật nguồn lại | Cổng mới hiển thị là `GigabitEthernet5/1` |

```text
Switch2> show ip interface brief
! Module quang được nhận ở slot: GigabitEthernet5/1
```

> **Lưu ý:** Một số thiết bị trong Packet Tracer không hỗ trợ hot-swap. Muốn thêm hoặc tháo module thì phải tắt nguồn thiết bị trước.

## 6. Part 3 - Connect Devices

| Thiết bị 1 | Interface | Loại cáp | Thiết bị 2 | Interface |
| --- | --- | --- | --- | --- |
| East | GigabitEthernet0/0 | Copper Straight-Through | Switch1 | GigabitEthernet0/1 |
| East | GigabitEthernet0/1 | Copper Straight-Through | Switch4 | GigabitEthernet0/1 |
| East | FastEthernet0/1/0 | Copper Straight-Through | PC1 | FastEthernet0 |
| East | FastEthernet0/1/1 | Copper Straight-Through | PC2 | FastEthernet0 |
| East | FastEthernet0/1/2 | Copper Straight-Through | PC3 | FastEthernet0 |
| Switch1 | FastEthernet0/1 | Copper Straight-Through | PC4 | FastEthernet0 |
| Switch1 | FastEthernet0/2 | Copper Straight-Through | PC5 | FastEthernet0 |
| Switch1 | FastEthernet0/3 | Copper Straight-Through | PC6 | FastEthernet0 |
| Switch4 | GigabitEthernet0/2 | Copper Cross-Over | Switch3 | GigabitEthernet3/1 |
| Switch3 | GigabitEthernet5/1 | Fiber | Switch2 | GigabitEthernet5/1 |
| Switch2 | FastEthernet0/1 | Copper Straight-Through | PC7 | FastEthernet0 |
| Switch2 | FastEthernet1/1 | Copper Straight-Through | PC8 | FastEthernet0 |
| Switch2 | FastEthernet2/1 | Copper Straight-Through | PC9 | FastEthernet0 |
| Switch2 | GigabitEthernet3/1 | Copper Straight-Through | Access Point | Port 0 |
| East | Serial0/0/0 | Serial DCE | West | Serial0/0/0 |

> **Lưu ý:** Với kết nối Serial DCE, chọn/cắm vào East trước theo yêu cầu đề. Trong bài này link lights bị tắt nên không dùng màu đèn để đánh giá đúng/sai, hãy dựa vào điểm số và lệnh kiểm tra.

![Cabling result](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/cabling-result.png)

## 7. Part 4 - Check Connectivity

### Step 1 - Kiểm tra interface status trên East

```text
East> show ip interface brief

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     172.30.1.1      YES manual up                    up
GigabitEthernet0/1     172.31.1.1      YES manual up                    up
Serial0/0/0            10.10.10.1      YES manual up                    up
Serial0/0/1            unassigned      YES unset  down                  down
FastEthernet0/1/0      unassigned      YES unset  up                    up
FastEthernet0/1/1      unassigned      YES unset  up                    up
FastEthernet0/1/2      unassigned      YES unset  up                    up
FastEthernet0/1/3      unassigned      YES unset  up                    down
Vlan1                  172.29.1.1      YES manual up                    up
```

> **Lưu ý:** `FastEthernet0/1/3` chưa nối host nên trạng thái thường là `up/down`. Ba cổng `FastEthernet0/1/0`, `0/1/1`, `0/1/2` phải `up/up` vì đã nối PC1, PC2, PC3.

![East show ip interface brief](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/east-show-ip-brief.png)

### Step 2 - Kiểm tra Laptop qua Wireless0

| Thiết bị | Interface | Thao tác | Kết quả mong muốn |
| --- | --- | --- | --- |
| Laptop | Wireless0 | Config → Wireless0 → Port Status: On | Có kết nối wireless |
| Laptop | Web Browser | Truy cập `www.cisco.pka` | Trang Cisco Packet Tracer hiển thị |

![Laptop wireless web](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/laptop-wireless-web.png)

![Laptop wireless web](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/laptop-wireless-web1.png)

### Step 3 - Kiểm tra TabletPC qua Wireless0

| Thiết bị | Interface | Thao tác | Kết quả mong muốn |
| --- | --- | --- | --- |
| TabletPC | Wireless0 | Config → Wireless0 → Port Status: On | Có kết nối wireless |
| TabletPC | Web Browser | Truy cập `www.cisco.pka` | Trang Cisco Packet Tracer hiển thị |


### Step 4 - Đổi TabletPC sang 3G/4G Cell1

| Thiết bị | Interface | Thao tác | Kết quả mong muốn |
| --- | --- | --- | --- |
| TabletPC | Wireless0 | Tắt Port Status | Kết nối wireless bị ngắt |
| TabletPC | 3G/4G Cell1 | Bật Port Status | Có kết nối cellular |
| TabletPC | Web Browser | Truy cập `www.cisco.pka` | Trang Cisco Packet Tracer hiển thị |

> **Lưu ý:** Không bật đồng thời `Wireless0` và `3G/4G Cell1` trên TabletPC để tránh thiết bị chọn sai đường ra mạng.

![Tablet cellular web](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/tablet-cellular-web.png)

### Step 5 - Kiểm tra các PC còn lại

| Nhóm thiết bị | Kiểm tra | Kết quả mong muốn |
| --- | --- | --- |
| PC1, PC2, PC3 | Web/Ping tới tài nguyên trong mạng | Thành công |
| PC4, PC5, PC6 | Web/Ping tới tài nguyên trong mạng | Thành công |
| PC7, PC8, PC9 | Web/Ping tới tài nguyên trong mạng | Thành công |
| Laptop, TabletPC | Truy cập `www.cisco.pka` | Hiển thị trang Cisco Packet Tracer |

```text
! Có thể kiểm tra từ từng PC bằng Command Prompt hoặc Web Browser
PC> ping 172.29.1.1
PC> ping 172.30.1.1
```


## 8. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không gắn được module | Thiết bị vẫn đang bật nguồn | Tắt power của router/switch, gắn module rồi bật lại |
| Không thấy cổng `FastEthernet0/1/x` trên East | Chưa gắn hoặc gắn sai module `HWIC-4ESW` | Kiểm tra Physical tab và gắn đúng module |
| Không có cổng quang trên Switch2 | Chưa gắn `PT-SWITCH-NM-1FGE` hoặc gắn sai slot | Gắn module vào slot ngoài cùng bên phải, kiểm tra lại bằng `show ip interface brief` |
| Kết nối Switch3 - Switch2 không đạt | Dùng nhầm Copper thay vì Fiber | Dùng đúng cáp Fiber giữa `GigabitEthernet5/1` và `GigabitEthernet5/1` |
| Kết nối Switch4 - Switch3 không đạt | Dùng nhầm Straight-Through thay vì Cross-Over | Dùng Copper Cross-Over |
| Serial East - West không đạt | Chọn sai cáp hoặc không cắm DCE vào East trước | Dùng Serial DCE và chọn East `Serial0/0/0` trước |
| Laptop/TabletPC không vào web được | Chưa bật Wireless0 hoặc chưa kết nối AP | Bật Port Status của Wireless0 và chờ kết nối xuất hiện |
| TabletPC lúc wireless lúc cellular bị lỗi | Bật cùng lúc Wireless0 và 3G/4G Cell1 | Chỉ bật một interface truy cập tại một thời điểm |

## 9. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| Nhận diện management ports | East có `AUX` và `Console` | Đạt |
| Nhận diện LAN/WAN interfaces | East có 2 Gigabit Ethernet và 2 Serial WAN | Đạt |
| Kiểm tra bandwidth | G0/0 = `1000000 Kbit`, S0/0/0 = `1544 Kbit` | Đạt |
| Gắn module East | `HWIC-4ESW` xuất hiện các cổng FastEthernet mở rộng | Đạt |
| Gắn module Switch2 | `PT-SWITCH-NM-1FGE` xuất hiện ở `GigabitEthernet5/1` | Đạt |
| Nối cáp | Tất cả kết nối đúng loại cáp theo bảng | Đạt |
| Kiểm tra East | Các interface chính đạt trạng thái đúng như đề | Đạt |
| Kiểm tra web | Laptop, TabletPC và các PC truy cập được tài nguyên | Đạt |


![Tablet cellular web](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-05/final.png)
---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/">Lab 1: 2.7.6 Packet Tracer - Implement Basic Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/">Lab 2: 2.8.1 Video Activity - Test the Interface Assignment</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/">Lab 3: 2.8.2 Video Activity - Test End-to-End Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/">Lab 4: 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 4.7.1 Packet Tracer - Connect the Physical Layer (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

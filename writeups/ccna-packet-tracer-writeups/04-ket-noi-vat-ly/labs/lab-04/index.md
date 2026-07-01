---
layout: page-toc
title: "CCNA 04.04 - 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN"
permalink: /writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-04/
toc: true
---

[← Quay lại danh sách Kết Nối Vật Lý](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/)

| Field | Value |
| --- | --- |
| Dạng lab | Kết Nối Vật Lý |
| File lab | `4.6.5 Packet Tracer - Connect a Wired and Wireless LAN.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-04/` |
| Trạng thái | Hoàn thành khi nối đúng toàn bộ cáp, ping thành công và truy cập được `http://netacad.pka` |

> **Ghi chú:** Bài này không yêu cầu cấu hình IP thủ công. Nhiệm vụ chính là đọc đúng bảng địa chỉ, chọn đúng loại cáp, nối đúng cổng và kiểm tra kết nối ở Logical Workspace và Physical Workspace.

## 1. Mục Tiêu Bài Lab

- Kết nối Cloud với Router0 bằng đúng loại cáp.
- Kết nối Cloud với Cable Modem bằng cáp coaxial.
- Kết nối Router0 với Router1, netacad.pka và Configuration Terminal.
- Kết nối Router1, Switch, Cable Modem, Wireless Router và Family PC.
- Kiểm tra kết nối bằng `ping`, Web Browser và Terminal.
- Quan sát Physical Workspace để trả lời các câu hỏi về topology vật lý.

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/topology.png)

![Topology lab 04](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/topology1.png)

## 2. Bảng Địa Chỉ IP

| Thiết bị | Interface | IP Address | Kết nối tới |
| --- | --- | --- | --- |
| Cloud | Eth6 | N/A | Router0 F0/0 |
| Cloud | Coax7 | N/A | Cable Modem Port0 |
| Cable Modem | Port0 | N/A | Cloud Coax7 |
| Cable Modem | Port1 | N/A | Wireless Router Internet |
| Router0 | Console | N/A | Configuration Terminal RS232 |
| Router0 | F0/0 | `192.168.2.1/24` | Cloud Eth6 |
| Router0 | F0/1 | `10.0.0.1/24` | netacad.pka F0 |
| Router0 | S0/0/0 | `172.31.0.1/24` | Router1 S0/0 |
| Router1 | S0/0 | `172.31.0.2/24` | Router0 S0/0/0 |
| Router1 | F1/0 | `172.16.0.1/24` | Switch F0/1 |
| Wireless Router | Internet | `192.168.2.2/24` | Cable Modem Port1 |
| Wireless Router | Eth1 | `192.168.1.1` | Family PC F0 |
| Family PC | F0 | `192.168.1.102` | Wireless Router Eth1 |
| Switch | F0/1 | `172.16.0.2` | Router1 F1/0 |
| netacad.pka | F0 | `10.0.0.254` | Router0 F0/1 |
| Configuration Terminal | RS232 | N/A | Router0 Console |

> **Lưu ý:** Các địa chỉ IP đã được cấu hình sẵn trong file lab. Nếu ping lỗi, ưu tiên kiểm tra sai cáp hoặc sai cổng trước, không vội cấu hình lại IP.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| WAN/Cloud | Cloud, Cable Modem | Cloud nối Router0 bằng Ethernet và nối Cable Modem bằng coaxial. |
| Primary Network | Router0, netacad.pka, Configuration Terminal | Router0 kết nối vừa mạng dữ liệu vừa console quản trị. |
| Secondary Network | Router1, Switch | Router1 nối Switch bằng cáp Ethernet straight-through. |
| Home Network | Cable Modem, Wireless Router, Family PC, Home PC, Home Printer | Family PC nối dây, Home PC và Home Printer kết nối không dây. |

> **Điểm dễ sai:** Không phải đường nào cũng dùng Copper Straight-Through. Router0 nối netacad.pka cần Copper Cross-Over, Cloud nối Cable Modem cần Coaxial, Router0 nối Configuration Terminal cần Console cable.

## 4. Part 1 - Connect to the Cloud

### Step 1: Connect Cloud to Router0

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Router0 | F0/0 | Cloud | Eth6 | Copper Straight-Through | Link light màu xanh |

> **Lưu ý:** Cloud trong bài hoạt động giống thiết bị switch ở cổng Ethernet, nên Router0 F0/0 nối Cloud Eth6 dùng cáp thẳng.

![Cloud to Router0](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/cloud-router0.png)

### Step 2: Connect Cloud to Cable Modem

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Cloud | Coax7 | Cable Modem | Port0 | Coaxial | Link light màu xanh |

![Cloud to Cable Modem](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/cloud-cable-modem.png)

### Kiểm tra Part 1

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Router0 F0/0 ↔ Cloud Eth6 | Đèn link xanh |
| Cloud Coax7 ↔ Cable Modem Port0 | Đèn link xanh |
| Không có dây đỏ hoặc dây sai cổng | Hoàn thành Part 1 |

## 5. Part 2 - Connect Router0

### Step 1: Connect Router0 to Router1

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Router0 | S0/0/0 | Router1 | S0/0 | Serial cable | Link light màu xanh |

> **Lưu ý:** Kết nối giữa hai router qua cổng serial phải dùng Serial cable, không dùng cáp Ethernet.

![Router0 to Router1](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/router0-router1.png)

### Step 2: Connect Router0 to netacad.pka

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Router0 | F0/1 | netacad.pka | F0 | Copper Cross-Over | Link light màu xanh |

> **Lưu ý:** Router0 và netacad.pka không có NIC tự động nhận cặp truyền/nhận trong bài này, nên phải dùng cáp chéo.

![Router0 to netacad](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/router0-netacad.png)

### Step 3: Connect Router0 to Configuration Terminal

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Router0 | Console | Configuration Terminal | RS232 | Console cable | Link light màu đen |

> **Lưu ý:** Cáp console không dùng để truyền dữ liệu mạng. Nó chỉ dùng để truy cập CLI và cấu hình Router0 qua Terminal.


### Kiểm tra Part 2

```text
Router0> enable
Router0# show ip interface brief
```

| Interface | IP mong muốn | Status mong muốn | Protocol mong muốn |
| --- | --- | --- | --- |
| FastEthernet0/0 | `192.168.2.1` | up | up |
| FastEthernet0/1 | `10.0.0.1` | up | up |
| Serial0/0/0 | `172.31.0.1` | up | up |

![Router0 show ip interface brief](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/router0-show-ip-interface-brief.png)

## 6. Part 3 - Connect Remaining Devices

### Step 1: Connect Router1 to Switch

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Router1 | F1/0 | Switch | F0/1 | Muilti mode fiber | Amber chuyển sang xanh sau vài giây |

> **Lưu ý:** Router nối Switch dùng cáp thẳng. Nếu đèn ban đầu màu cam, chờ vài giây để cổng chuyển trạng thái.

![Router1 to Switch](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/router1-switch.png)

### Step 2: Connect Cable Modem to Wireless Router

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Cable Modem | Port1 | Wireless Router | Internet | Copper Straight-Through | Link light màu xanh |

![Cable Modem to Wireless Router](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/cable-modem-wireless-router.png)

### Step 3: Connect Wireless Router to Family PC

| From | Port | To | Port | Cáp cần chọn | Trạng thái đúng |
| --- | --- | --- | --- | --- | --- |
| Wireless Router | Ethernet 1 | Family PC | F0 | Copper Straight-Through | Link light màu xanh |

![Wireless Router to Family PC](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/wireless-router-family-pc.png)

### Kiểm tra Part 3

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Router1 F1/0 ↔ Switch F0/1 | Đèn xanh |
| Cable Modem Port1 ↔ Wireless Router Internet | Đèn xanh |
| Wireless Router Eth1 ↔ Family PC F0 | Đèn xanh |
| Home PC và Home Printer | Kết nối không dây tới Wireless Router |

## 7. Part 4 - Verify Connections

### Step 1: Test Family PC to netacad.pka

```text
PC> ping 10.0.0.254

! Hoặc ping theo hostname nếu Packet Tracer phân giải được tên:
PC> ping netacad.pka
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Family PC ping `10.0.0.254` | Successful |
| Family PC ping `netacad.pka` | Successful nếu hostname được phân giải |

![Family PC ping netacad](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/family-pc-ping-netacad.png)

### Step 2: Open netacad.pka by Web Browser

| Thiết bị | Ứng dụng | Địa chỉ cần nhập | Kết quả mong muốn |
| --- | --- | --- | --- |
| Family PC | Web Browser | `http://netacad.pka` | Trang web mở thành công |

![Family PC web netacad](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/family-pc-web-netacad.png)

### Step 3: Ping Switch from Home PC

```text
PC> ping 172.16.0.2
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Home PC ping Switch `172.16.0.2` | Successful |

![Home PC ping Switch](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/home-pc-ping-switch.png)

### Step 4: Open Router0 from Configuration Terminal

```text
Router0> enable
Router0# show ip interface brief
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| Terminal mở được Router0 CLI | Thấy prompt `Router0>` hoặc `Router0#` |
| `show ip interface brief` | Các interface đã nối dây ở trạng thái `up/up` |


## 8. Part 5 - Examine the Physical Topology

### Step 1: Examine the Cloud

| Câu hỏi | Đáp án |
| --- | --- |
| How many wires are connected to the switch in the blue rack? | Có **2 dây** được kết nối vào switch trong blue rack. |


### Step 2: Examine the Primary Network

| Câu hỏi | Đáp án |
| --- | --- |
| What is located on the table to the right of the blue rack? | **Configuration Terminal** nằm trên bàn bên phải blue rack. |


### Step 3: Examine the Secondary Network

| Câu hỏi | Đáp án |
| --- | --- |
| Why are there two orange cables connected to each device? | Vì đó là cáp quang theo cặp: một dây dùng để truyền dữ liệu, một dây dùng để nhận dữ liệu. |


### Step 4: Examine the Home Network

| Câu hỏi | Đáp án |
| --- | --- |
| Why is there no rack to hold the equipment? | Vì đây là mạng gia đình, thiết bị thường đặt trực tiếp trên bàn/kệ, không cần tủ rack như mạng doanh nghiệp. |

## 9. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Router0 F0/1 nối netacad.pka không xanh | Dùng nhầm Copper Straight-Through | Xóa dây và nối lại bằng Copper Cross-Over |
| Cloud không nối được Cable Modem | Dùng nhầm cáp Ethernet | Dùng Coaxial từ Cloud Coax7 tới Cable Modem Port0 |
| Không mở được Router0 từ Configuration Terminal | Dùng nhầm cáp hoặc nhầm cổng | Dùng Console cable từ Router0 Console tới RS232 |
| Ping từ Family PC đến netacad.pka thất bại | Sai một trong các đường nối trung gian | Kiểm tra lần lượt Wireless Router, Cable Modem, Cloud, Router0 và netacad.pka |
| Home PC ping Switch thất bại | Home PC chưa kết nối wireless hoặc sai đường WAN/LAN | Kiểm tra kết nối wireless và các link từ Wireless Router về Switch |
| Đèn link Router1-Switch còn màu cam | Cổng switch đang chuyển trạng thái | Chờ vài giây, nếu không xanh thì kiểm tra lại cáp và đúng cổng |

## 10. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| Cloud Eth6 ↔ Router0 F0/0 | Link xanh | Đạt |
| Cloud Coax7 ↔ Cable Modem Port0 | Link xanh | Đạt |
| Router0 S0/0/0 ↔ Router1 S0/0 | Link xanh | Đạt |
| Router0 F0/1 ↔ netacad.pka F0 | Link xanh | Đạt |
| Router0 Console ↔ Configuration Terminal RS232 | Mở được Router0 CLI | Đạt |
| Router1 F1/0 ↔ Switch F0/1 | Link xanh | Đạt |
| Cable Modem Port1 ↔ Wireless Router Internet | Link xanh | Đạt |
| Wireless Router Eth1 ↔ Family PC F0 | Link xanh | Đạt |
| Family PC ping netacad.pka | Successful | Đạt |
| Family PC mở `http://netacad.pka` | Trang web mở được | Đạt |
| Home PC ping Switch `172.16.0.2` | Successful | Đạt |
| Physical Workspace questions | Trả lời đầy đủ | Đạt |

![final](/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/labs/lab-04/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 3</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 5 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-01/">Lab 1: 2.7.6 Packet Tracer - Implement Basic Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-02/">Lab 2: 2.8.1 Video Activity - Test the Interface Assignment</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-03/">Lab 3: 2.8.2 Video Activity - Test End-to-End Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 4: 4.6.5 Packet Tracer - Connect a Wired and Wireless LAN (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/lab-05/">Lab 5: 4.7.1 Packet Tracer - Connect the Physical Layer</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 01.01 - 1.5.7 Packet Tracer - Network Representation"
permalink: /writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/lab-01/
toc: true
---

[← Quay lại danh sách Làm Quen Packet Tracer](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/)

| Field | Value |
| --- | --- |
| Dạng lab | Làm Quen Packet Tracer |
| File lab | `1.5.7 Packet Tracer - Network Representation.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành phần quan sát, phân loại thiết bị và trả lời câu hỏi |

> **Ghi chú:** Bài lab đầu tiên trong nhóm "Làm quen Packet Tracer". Mục tiêu là quan sát topology, nhận diện thiết bị và trả lời câu hỏi. **Không yêu cầu cấu hình CLI.**

---

## 1. Mục Tiêu Bài Lab

- Phân biệt thiết bị đầu cuối, thiết bị trung gian và đường truyền mạng
- Xác định các khu vực mạng: Home Office, Central, Branch, Internet, Intranet
- Nắm vai trò cơ bản của router, switch, server, wireless router, access point, modem
- Phân biệt LAN và WAN
- Hoàn thành các câu hỏi trong phần Instructions của Packet Tracer

![Instructions lab 01](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/instructions.png)

---

## 2. Topology Và Quan Sát Ban Đầu

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/topology.png)

### Các khu vực trong topology

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Home Office | HomeDesktop, HomeLaptop, Inkjet, Tablet, WRS, Modem | Mạng gia đình, có dây và không dây |
| Central | CentralServer, R2, S3, D1, D2, S1, S2, PC1, PC2, PC3, PC4 | Mạng trung tâm, có server, router và nhiều switch |
| Branch | BranchServer, R4, S4, Wireless AP, Laser, Smart Phone, Guest, Sales, Accounting, IP Phone0, IP Phone1 | Mạng chi nhánh, có Wi-Fi và IP Phone |
| Internet | Internet cloud | WAN — đại diện mạng Internet |
| Intranet | Intranet cloud | WAN — đại diện mạng nội bộ diện rộng |

> **Điểm dễ sai:** Dễ đếm nhầm IP Phone là intermediary device; dễ nhầm cloud là thiết bị trung gian; dễ bỏ sót thiết bị kết nối wireless (đường nét đứt).

---

## 3. Trả Lời Câu Hỏi Bài Lab

### Step 1: Identify common components of a network

#### Câu 1. List the intermediary device categories.

| Intermediary Device Category | Vai trò |
| --- | --- |
| Routers | Định tuyến dữ liệu giữa các mạng |
| Switches | Kết nối thiết bị trong cùng LAN |
| Hubs | Kết nối thiết bị ở mức cơ bản, ít dùng hiện nay |
| Wireless Devices | Cung cấp kết nối không dây |
| WAN Emulation | Mô phỏng kết nối WAN |

---

#### Câu 2. How many icons represent endpoint devices? (không tính 2 cloud)

**Đáp án: 15 endpoint devices**

| Khu vực | Thiết bị | Số lượng |
| --- | --- | --- |
| Home Office | HomeDesktop, HomeLaptop, Inkjet, Tablet | 4 |
| Central | CentralServer, PC1, PC2, PC3, PC4 | 5 |
| Branch | BranchServer, Laser, Smart Phone, Guest, Sales, Accounting | 6 |
| **Tổng** | | **15** |

![Endpoint devices](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/endpoint-devices.png)

---

#### Câu 3. How many icons represent intermediary devices? (không tính 2 cloud)

**Đáp án: 11 intermediary devices**

| Khu vực | Thiết bị | Số lượng |
| --- | --- | --- |
| Home Office | WRS, Modem | 2 |
| Central | S3, R2, D1, D2, S1, S2 | 6 |
| Branch | R4, S4, Wireless AP | 3 |
| **Tổng** | | **11** |

> **Lưu ý:** IP Phone0 và IP Phone1 **không** tính vào intermediary devices — chúng là end devices phục vụ thoại IP. Nếu tính nhầm sẽ ra 13 thay vì 11.

![Intermediary devices](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/intermediary-devices.png)

---

#### Câu 4. How many end devices are not desktop computers?

**Đáp án: 8 devices**

| Thiết bị | Loại |
| --- | --- |
| HomeLaptop | Laptop |
| Guest | Laptop |
| Inkjet | Printer |
| Laser | Printer |
| Tablet | Tablet |
| Smart Phone | Smartphone |
| CentralServer | Server |
| BranchServer | Server |

---

#### Câu 5. How many different types of media connections are used?

**Đáp án: 4 loại**

| Loại kết nối | Ví dụ trong topology |
| --- | --- |
| Copper/Ethernet | PC, switch, router, server |
| Wireless | Tablet, smartphone, Guest, laptop |
| Serial WAN | Đường màu đỏ giữa router và cloud |
| Coaxial | Modem lên Internet |

![Media connection types](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/media-types.png)

---

### Step 2: Explain the purpose of the devices

#### Câu a. Explain the client-server model.

| Thành phần | Vai trò | Ví dụ trong topology |
| --- | --- | --- |
| Client | Gửi yêu cầu sử dụng dịch vụ | PC1, PC2, Sales, Accounting, HomeDesktop, HomeLaptop |
| Server | Tiếp nhận và cung cấp dịch vụ | CentralServer, BranchServer |

---

#### Câu b. List at least two functions of intermediary devices.

| Chức năng | Giải thích |
| --- | --- |
| Kết nối các thiết bị mạng | Switch kết nối PC, server, printer trong cùng LAN |
| Chuyển tiếp dữ liệu | Switch/router chuyển frame/packet đến đúng đích |
| Định tuyến giữa các mạng | Router cho phép các mạng khác nhau giao tiếp |
| Kết nối LAN ra Internet | Modem/router kết nối LAN với WAN |
| Bảo mật và quản lý traffic | Dùng ACL, NAT, firewall, filtering |

---

#### Câu c. List at least two criteria for choosing a network media type.

| Tiêu chí | Giải thích |
| --- | --- |
| Khoảng cách truyền | Cáp đồng phù hợp khoảng ngắn, cáp quang phù hợp khoảng xa |
| Tốc độ / băng thông | Chọn media hỗ trợ bandwidth phù hợp yêu cầu |
| Môi trường triển khai | Nơi nhiều nhiễu điện từ ưu tiên cáp quang |
| Chi phí | Cáp đồng rẻ hơn cáp quang |
| Tính linh hoạt | Wireless phù hợp thiết bị di động |
| Bảo mật | Có dây khó bị nghe lén hơn không dây |

---

### Step 3: Compare and contrast LANs and WANs

#### Câu a. Explain the difference between a LAN and a WAN.

| Tiêu chí | LAN | WAN |
| --- | --- | --- |
| Tên đầy đủ | Local Area Network | Wide Area Network |
| Phạm vi | Nhỏ: nhà, văn phòng, chi nhánh | Rộng: giữa nhiều chi nhánh, thành phố, quốc gia |
| Thiết bị thường gặp | Switch, access point, PC, server | Router, ISP, leased line, MPLS |
| Ví dụ | Mạng gia đình, mạng công ty | Internet, kết nối trụ sở với chi nhánh |

---

#### Câu b. How many WANs do you see?

**Đáp án: 2 WANs** — Internet và Intranet

![WAN clouds](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/wan-clouds.png)

---

#### Câu c. How many LANs do you see?

**Đáp án: 3 LANs**

| LAN | Khu vực |
| --- | --- |
| LAN 1 | Home Office |
| LAN 2 | Central |
| LAN 3 | Branch |

---

#### Câu d. Briefly describe the internet.

Internet là hệ thống "mạng của nhiều mạng" toàn cầu, gồm router lõi, hệ thống ISP, cáp quang biển, trung tâm dữ liệu và DNS. Trong Packet Tracer chỉ được mô phỏng bằng một cloud icon để đơn giản hóa.

---

#### Câu e. Common ways a home user connects to the internet?

| Phương thức | Mô tả |
| --- | --- |
| FTTH/Fiber | Cáp quang đến nhà, phổ biến hiện nay |
| Cable Internet | Qua hệ thống cáp truyền hình |
| DSL | Qua đường dây điện thoại |
| 4G/5G | Qua mạng di động |
| Satellite | Vệ tinh, dùng ở vùng xa |

---

#### Câu f. Common methods businesses use to connect to the internet?

| Phương thức | Mô tả |
| --- | --- |
| Business Fiber | Cáp quang doanh nghiệp |
| Leased Line | Đường thuê riêng, có cam kết SLA |
| Metro Ethernet | Ethernet tốc độ cao trong đô thị |
| MPLS/VPN | Kết nối nhiều chi nhánh, bảo mật cao |
| Site-to-Site VPN | Kết nối chi nhánh qua Internet bằng tunnel VPN |
| 4G/5G Backup | Dự phòng khi đường truyền chính lỗi |

---

## 4. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Đếm sai endpoint devices (không ra 15) | Nhầm cloud hoặc IP Phone vào nhóm | Không tính cloud; IP Phone là end device |
| Đếm sai intermediary devices (ra 13) | Tính IP Phone0/1 là intermediary | Bỏ IP Phone khỏi nhóm intermediary |
| Nhầm LAN và WAN | Đếm Internet/Intranet là LAN | LAN: Home Office, Central, Branch; WAN: Internet, Intranet |
| Bỏ sót thiết bị không dây | Bỏ qua đường nét đứt | Phóng to topology, kiểm tra kết nối wireless |
| Đếm thiếu loại media (không ra 4) | Chỉ đếm Ethernet | Kiểm tra cả Wireless, Serial WAN và Coaxial |

---

## 5. Kết Quả Cuối

| Nội dung | Kết quả |
| --- | --- |
| Endpoint devices | **15** |
| Intermediary devices | **11** |
| End devices không phải desktop | **8** |
| Media connection types | **4** |
| WANs | **2** |
| LANs | **3** |
| Cấu hình CLI | Không yêu cầu |


---

## 6. Challenge Question (Không Bắt Buộc)

### 6.1. Add an end device to the topology

Thêm PC mới vào LAN Central hoặc Branch. Thiết bị mới cần:

| Thông tin | Mục đích |
| --- | --- |
| IP Address | Định danh trong mạng |
| Subnet Mask | Xác định subnet |
| Default Gateway | Gửi dữ liệu ra ngoài LAN |
| DNS Server | Phân giải tên miền |
| Media Connection | Kết nối vật lý hoặc không dây vào switch |

```text
ipconfig
ping <default_gateway>
ping <IP_thiết_bị_khác>
```

![Challenge add PC](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/challenge-add-pc.png)

---

### 6.2. Add a new intermediary device

Thêm switch mới vào LAN Central hoặc Branch. Cần chú ý:

| Thành phần | Mục đích |
| --- | --- |
| Kết nối đúng port | Dữ liệu có thể đi qua thiết bị |
| Loại dây phù hợp | Ethernet copper để nối PC với switch |
| IP quản trị (nếu cần) | Cho phép quản trị switch từ xa |
| Default gateway (nếu quản trị khác mạng) | Truy cập switch từ mạng khác |

![Challenge add switch](/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/labs/lab-01/challenge-add-switch.png)

---

### 6.3. Create a new network with at least two LANs connected by a WAN

```text
LAN 1 --- Router 1 --- WAN --- Router 2 --- LAN 2
```

| Thành phần | Ghi chú |
| --- | --- |
| 2 switch | Mỗi LAN một switch |
| 2 router | Kết nối mỗi LAN ra WAN |
| 2+ PC | Mỗi LAN ít nhất một end device |
| IP addressing | Mỗi LAN dùng subnet khác nhau |
| Default gateway | PC trỏ về cổng router trong LAN |
| Static/dynamic route | Hai LAN liên lạc qua WAN |

```text
ping <IP_PC_LAN2>   ! từ PC ở LAN 1
```
---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><span></span></div>
  </div>

  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 1 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
      <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 1.5.7 Packet Tracer - Network Representation (Đang đọc)</strong></li>
    </ul>
  </details>
</div>

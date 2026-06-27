---
layout: page-toc
title: "CCNA 02.06 - 10.3.4 Packet Tracer - Connect a Router to a LAN"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `10.3.4 Packet Tracer - Connect a Router to a LAN.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-06/` |
| Trạng thái | Cấu hình IP các cổng router, kiểm tra routing table và ping end-to-end |

> **Nhận diện đề:** Đây là bài lab cấu hình router interface trong LAN/WAN nhỏ. Router đã có một số cấu hình nền, nhiệm vụ chính là kiểm tra trạng thái ban đầu, cấu hình các cổng GigabitEthernet theo bảng địa chỉ, lưu cấu hình và kiểm tra kết nối giữa các PC.

## 1. Mục Tiêu Bài Lab

- Xem thông tin interface trên router bằng các lệnh `show`.
- Kiểm tra địa chỉ IP, trạng thái cổng và routing table trên R1/R2.
- Cấu hình các cổng GigabitEthernet trên R1 và R2.
- Gán địa chỉ IP, subnet mask và default gateway cho PC1 đến PC4.
- Lưu cấu hình router vào NVRAM.
- Kiểm tra ping giữa các PC ở những mạng khác nhau.

![Topology lab 06](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/topology.png)

## 2. Bảng Địa Chỉ IPv4

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `192.168.10.1` | `255.255.255.0` | N/A |
| R1 | G0/1 | `192.168.11.1` | `255.255.255.0` | N/A |
| R1 | S0/0/0 DCE | `209.165.200.225` | `255.255.255.252` | N/A |
| R2 | G0/0 | `10.1.1.1` | `255.255.255.0` | N/A |
| R2 | G0/1 | `10.1.2.1` | `255.255.255.0` | N/A |
| R2 | S0/0/0 | `209.165.200.226` | `255.255.255.252` | N/A |
| PC1 | NIC | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC2 | NIC | `192.168.11.10` | `255.255.255.0` | `192.168.11.1` |
| PC3 | NIC | `10.1.1.10` | `255.255.255.0` | `10.1.1.1` |
| PC4 | NIC | `10.1.2.10` | `255.255.255.0` | `10.1.2.1` |

> **Lưu ý:** Mạng WAN `209.165.200.224/30` chỉ có 2 địa chỉ usable: `209.165.200.225` và `209.165.200.226`. Cổng serial phía R1 là DCE nên nếu serial chưa chạy, cần kiểm tra `clock rate` trên R1.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN trái trên | PC1 - S1 - R1 G0/0 | Mạng `192.168.10.0/24`, gateway là `192.168.10.1` |
| LAN trái dưới | PC2 - S2 - R1 G0/1 | Mạng `192.168.11.0/24`, gateway là `192.168.11.1` |
| WAN giữa | R1 S0/0/0 - R2 S0/0/0 | Mạng point-to-point `209.165.200.224/30` |
| LAN phải trên | R2 G0/0 - S3 - PC3 | Mạng `10.1.1.0/24`, gateway là `10.1.1.1` |
| LAN phải dưới | R2 G0/1 - S4 - PC4 | Mạng `10.1.2.0/24`, gateway là `10.1.2.1` |

> **Điểm dễ sai:** Switch trong bài này không cần cấu hình IP để ping end-to-end. Các PC ping qua router, không ping qua địa chỉ quản trị của switch.

## 4. Part 1 - Display Router Information

### Step 1: Xem thông tin interface trên R1

```text
R1> enable
Password: class
R1# show interfaces
R1# show interfaces serial 0/0/0
R1# show interfaces gigabitethernet 0/0
```

| Câu hỏi | Trả lời |
| --- | --- |
| Lệnh hiển thị thống kê tất cả interface trên router | `show interfaces` |
| Lệnh hiển thị riêng interface Serial 0/0/0 | `show interfaces serial 0/0/0` |
| IP trên R1 S0/0/0 | `209.165.200.225` |
| Bandwidth trên Serial 0/0/0 | `1544 Kbit` |
| IP trên R1 G0/0 trước khi cấu hình | Thường là `unassigned` nếu bài chưa cấu hình sẵn G0/0 |
| IP trên R1 G0/0 sau khi cấu hình | `192.168.10.1` |
| MAC address của G0/0 | Phụ thuộc thiết bị Packet Tracer, xem trực tiếp trong output `show interfaces g0/0` |
| Bandwidth của GigabitEthernet 0/0 | `1000000 Kbit` |

> **Lưu ý:** MAC address không nên chép cứng vào writeup vì mỗi file Packet Tracer có thể sinh giá trị khác nhau.

![show interfaces R1](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/show-interfaces-r1.png)

### Step 2: Xem tóm tắt interface trên R1 và R2

```text
R1# show ip interface brief
R2# show ip interface brief
```

| Câu hỏi | Trả lời |
| --- | --- |
| Lệnh hiển thị tóm tắt interface, IP và trạng thái | `show ip interface brief` |
| Số serial interface trên R1/R2 | Thường có `2` serial interface trên mỗi router, nhưng bài dùng chính `S0/0/0` |
| Số Ethernet interface trên R1/R2 | `2` GigabitEthernet interface trên mỗi router: `G0/0` và `G0/1` |
| Các Ethernet interface trên R1 có giống nhau không? | Có, trong bài này đều là GigabitEthernet |

> **Lưu ý:** Nếu Packet Tracer hiển thị thêm interface chưa dùng, chỉ cần giữ trạng thái mặc định. Bài này chấm chính các cổng trong bảng địa chỉ.

![show ip interface brief before](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/show-ip-int-brief-before.png)

### Step 3: Xem routing table trên R1

```text
R1# show ip route
```

| Câu hỏi | Trả lời |
| --- | --- |
| Lệnh hiển thị routing table | `show ip route` |
| Connected route ban đầu trên R1 | Thường thấy mạng WAN `209.165.200.224/30` nếu serial đã được cấu hình sẵn |
| Route hiển thị với ký hiệu `C` | `C 209.165.200.224/30 is directly connected, Serial0/0/0` |
| Gói tin đến mạng không có trong routing table | Router drop gói tin nếu không có route cụ thể hoặc default route phù hợp |

![show ip route R1 before](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/show-ip-route-r1-before.png)

## 5. Part 2 - Configure Router Interfaces

### Step 1: Cấu hình R1

```text
R1> enable
Password: class
R1# configure terminal

R1(config)# interface gigabitethernet 0/0
R1(config-if)# description LAN connection to S1
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface gigabitethernet 0/1
R1(config-if)# description LAN connection to S2
R1(config-if)# ip address 192.168.11.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit

! Serial thường đã được cấu hình sẵn trong bài.
! Nếu kiểm tra thấy serial chưa có IP hoặc đang shutdown thì cấu hình lại như dưới.
R1(config)# interface serial 0/0/0
R1(config-if)# description WAN connection to R2
R1(config-if)# ip address 209.165.200.225 255.255.255.252
R1(config-if)# clock rate 128000
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** Chỉ cổng DCE mới cần `clock rate`. Trong bảng địa chỉ, R1 S0/0/0 là DCE.

![configure R1 interfaces](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/configure-r1-interfaces.png)

### Step 2: Cấu hình R2

```text
R2> enable
Password: class
R2# configure terminal

R2(config)# interface gigabitethernet 0/0
R2(config-if)# description LAN connection to S3
R2(config-if)# ip address 10.1.1.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit

R2(config)# interface gigabitethernet 0/1
R2(config-if)# description LAN connection to S4
R2(config-if)# ip address 10.1.2.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit

! Serial thường đã được cấu hình sẵn trong bài.
! Nếu kiểm tra thấy serial chưa có IP hoặc đang shutdown thì cấu hình lại như dưới.
R2(config)# interface serial 0/0/0
R2(config-if)# description WAN connection to R1
R2(config-if)# ip address 209.165.200.226 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# exit

R2(config)# end
R2# copy running-config startup-config
```

> **Lưu ý:** Bài này tập trung vào router interface. OSPF thường đã được cấu hình nền trong file lab, mình chỉ cần đưa các interface lên `up/up` để route động xuất hiện đầy đủ.

![configure R2 interfaces](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/configure-r2-interfaces.png)

### Step 3: Cấu hình IP cho PC

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC2 | `192.168.11.10` | `255.255.255.0` | `192.168.11.1` |
| PC3 | `10.1.1.10` | `255.255.255.0` | `10.1.1.1` |
| PC4 | `10.1.2.10` | `255.255.255.0` | `10.1.2.1` |

![PC1 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/pc1-ip-config.png)
![PC2 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/pc2-ip-config.png)
![PC3 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/pc3-ip-config.png)
![PC4 IP configuration](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/pc4-ip-config.png)

### Kiểm tra cuối Part 2

```text
R1# show ip interface brief
R2# show ip interface brief

! Kiểm tra từ R1 đến PC1
R1# ping 192.168.10.10

! Kiểm tra từ R2 đến PC3
R2# ping 10.1.1.10
```

| Thiết bị | Interface cần đúng | Trạng thái mong muốn |
| --- | --- | --- |
| R1 | `G0/0`, `G0/1`, `S0/0/0` | `up/up` |
| R2 | `G0/0`, `G0/1`, `S0/0/0` | `up/up` |

![verify interfaces after config](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/verify-interfaces-after-config.png)

## 6. Part 3 - Verify the Configuration

### Step 1: Kiểm tra interface configuration

```text
R1# show ip interface brief
R2# show ip interface brief
```

| Câu hỏi | Trả lời |
| --- | --- |
| Số interface có IP và `up/up` trên R1 | `3`: `G0/0`, `G0/1`, `S0/0/0` |
| Số interface có IP và `up/up` trên R2 | `3`: `G0/0`, `G0/1`, `S0/0/0` |
| Phần không hiển thị trong `show ip interface brief` | Description của interface |
| Lệnh kiểm tra description | `show running-config`, `show interfaces description`, hoặc `show interfaces <interface>` |

```text
R1# show interfaces description
R2# show interfaces description
```

![show interface description](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/show-interface-description.png)

### Step 2: Kiểm tra routing table

```text
R1# show ip route
R2# show ip route
```

| Câu hỏi | R1 | R2 |
| --- | --- | --- |
| Connected routes ký hiệu `C` | `3` | `3` |
| OSPF routes ký hiệu `O` | `2` | `2` |
| Tổng số LAN/WAN trong topology | `5` | `5` |
| Tổng `C + O` có khớp topology không? | Có | Có |

| Network | Loại mạng | Router kết nối trực tiếp |
| --- | --- | --- |
| `192.168.10.0/24` | LAN | R1 |
| `192.168.11.0/24` | LAN | R1 |
| `209.165.200.224/30` | WAN | R1 và R2 |
| `10.1.1.0/24` | LAN | R2 |
| `10.1.2.0/24` | LAN | R2 |

> **Lưu ý:** Nếu thiếu OSPF route, thường không phải do PC sai IP mà do router interface chưa `up/up`, IP interface sai subnet hoặc cấu hình OSPF nền chưa nhận được mạng đó.

![show ip route after](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/show-ip-route-after.png)

### Step 3: Kiểm tra ping end-to-end

```text
! Từ PC1 ping PC4
PC> ping 10.1.2.10

! Từ PC1 ping PC3
PC> ping 10.1.1.10

! Từ PC2 ping PC3
PC> ping 10.1.1.10

! Từ PC2 ping PC4
PC> ping 10.1.2.10

! Từ R2 ping PC2
R2# ping 192.168.11.10
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC1 ping PC4 | Success |
| PC1 ping PC3 | Success |
| PC2 ping PC3 | Success |
| PC2 ping PC4 | Success |
| R2 ping PC2 | Success |

![ping end to end](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-06/ping-end-to-end.png)

## 7. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Interface router vẫn đỏ/down | Quên `no shutdown` | Vào đúng interface và chạy `no shutdown` |
| PC không ping được gateway | Sai IP PC, subnet mask hoặc gateway | Kiểm tra lại Desktop > IP Configuration |
| Serial giữa R1-R2 không lên | Thiếu `clock rate` ở đầu DCE hoặc interface shutdown | Kiểm tra `show controllers serial 0/0/0`, thêm `clock rate` trên R1 DCE |
| Routing table thiếu OSPF route | Interface chưa up hoặc sai IP/subnet | Kiểm tra `show ip interface brief` và `show ip route` |
| Ping lần đầu bị mất 1 gói | ARP/khởi tạo đường đi lần đầu | Ping lại lần hai, nếu sau đó success là bình thường |
| Lưu rồi nhưng mở lại bị mất cấu hình | Chưa copy running-config sang startup-config | Chạy `copy running-config startup-config` trên cả R1 và R2 |
| Cấu hình nhầm G0/0 với G0/1 | Nhìn nhầm LAN theo topology | Đối chiếu bảng địa chỉ trước khi nhập IP |

## 8. Kết Quả Cuối

| Hạng mục | Kết quả cần đạt |
| --- | --- |
| R1 G0/0 | `192.168.10.1/24`, trạng thái `up/up` |
| R1 G0/1 | `192.168.11.1/24`, trạng thái `up/up` |
| R1 S0/0/0 | `209.165.200.225/30`, trạng thái `up/up` |
| R2 G0/0 | `10.1.1.1/24`, trạng thái `up/up` |
| R2 G0/1 | `10.1.2.1/24`, trạng thái `up/up` |
| R2 S0/0/0 | `209.165.200.226/30`, trạng thái `up/up` |
| PC1 - PC4 | Đúng IP, subnet mask và default gateway |
| Routing table | Mỗi router có `3` connected routes và `2` OSPF routes |
| End-to-end connectivity | PC ở các LAN khác nhau ping được nhau |
| Save configuration | Đã lưu bằng `copy running-config startup-config` |

- [ ] Ảnh topology: `topology.png`
- [ ] Ảnh bảng IP hoặc instruction: `instructions.png`
- [ ] Ảnh `show ip interface brief`: `verify-interfaces-after-config.png`
- [ ] Ảnh `show ip route`: `show-ip-route-after.png`
- [ ] Ảnh ping PC1 đến PC4: `ping-end-to-end.png`
- [ ] Ảnh Check Results hoàn thành: `check-results.png`

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 5</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 7 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

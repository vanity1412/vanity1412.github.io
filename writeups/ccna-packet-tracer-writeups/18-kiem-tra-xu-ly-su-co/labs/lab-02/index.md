---
layout: page-toc
title: "CCNA 18.02 - 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Khôi phục kết nối IPv4 và IPv6 bằng `ping`, `tracert`, `show ip interface brief`, `show ip route`, `show ipv6 interface brief` |

> **Ghi chú:** Đây là lab troubleshoot. Thiết bị đã được cấu hình sẵn nhưng có lỗi kết nối. Trọng tâm là dùng `ipconfig`, `ipv6config`, `ping`, `tracert` và lệnh `show` để khoanh vùng lỗi trước khi sửa.

## 1. Mục Tiêu Bài Lab

- Hoàn thiện thông tin địa chỉ IPv4/IPv6 còn thiếu của các PC.
- Dùng `ping` để kiểm tra kết nối IPv4 giữa PC1 và PC3.
- Dùng `tracert` để xác định hop cuối cùng còn đi được khi IPv4 bị lỗi.
- Dùng `show ip interface brief` và `show ip route` để kiểm tra router.
- Dùng `ping` để kiểm tra kết nối IPv6 giữa PC2 và PC4.
- Dùng `tracert` và `show ipv6 interface brief` để xác định lỗi IPv6.
- Sửa cấu hình sai và xác nhận kết nối end-to-end hoạt động.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/topology.png)

## 2. Bảng Địa Chỉ

### 2.1. IPv4

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/1 | `10.10.1.97` | `255.255.255.224` | N/A |
| R1 | S0/0/1 | `10.10.1.6` | `255.255.255.252` | N/A |
| R2 | S0/0/0 | `10.10.1.5` | `255.255.255.252` | N/A |
| R2 | S0/0/1 | `10.10.1.9` | `255.255.255.252` | N/A |
| R3 | G0/1 | `10.10.1.17` | `255.255.255.240` | N/A |
| R3 | S0/0/1 | `10.10.1.10` | `255.255.255.252` | N/A |
| PC1 | NIC | `10.10.1.126` | `255.255.255.224` | `10.10.1.97` |
| PC3 | NIC | `10.10.1.30` | `255.255.255.240` | `10.10.1.17` |

> **Lưu ý:** Nếu file Packet Tracer hiển thị IP PC bằng `ipconfig /all` khác với bảng trên, ưu tiên giá trị thực tế trong file `.pka`. Nguyên tắc kiểm tra không đổi: PC1 phải nằm trong `10.10.1.96/27`, PC3 phải nằm trong `10.10.1.16/28`.

### 2.2. IPv6

| Device | Interface | IPv6 Address / Prefix | Default Gateway |
| --- | --- | --- | --- |
| R1 | G0/0 | `2001:db8:1:1::1/64` | N/A |
| R1 | S0/0/1 | `2001:db8:1:2::2/64` | N/A |
| R1 | S0/0/1 | `fe80::1` | N/A |
| R2 | S0/0/0 | `2001:db8:1:2::1/64` | N/A |
| R2 | S0/0/1 | `2001:db8:1:3::1/64` | N/A |
| R2 | S0/0/1 | `fe80::2` | N/A |
| R3 | G0/0 | `2001:db8:1:4::1/64` | N/A |
| R3 | S0/0/1 | `2001:db8:1:3::2/64` | N/A |
| R3 | S0/0/1 | `fe80::3` | N/A |
| PC2 | NIC | `2001:db8:1:1::a/64` | `2001:db8:1:1::1` |
| PC4 | NIC | `2001:db8:1:4::a/64` | `2001:db8:1:4::1` |

> **Lưu ý:** Một số file Packet Tracer có thể dùng link-local làm IPv6 default gateway. Khi đó gateway của PC2/PC4 phải trùng địa chỉ gateway thực tế trên cổng LAN của R1/R3.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| IPv4 LAN bên trái | PC1 - S1 - R1 | PC1 dùng mạng `10.10.1.96/27`, gateway là R1 `G0/1`. |
| IPv6 LAN bên trái | PC2 - S2 - R1 | PC2 dùng mạng `2001:db8:1:1::/64`, gateway là R1 `G0/0`. |
| Core router | R1 - R2 - R3 | Hai kết nối serial dùng subnet `/30` cho IPv4 và `/64` cho IPv6. |
| IPv4 LAN bên phải | R3 - S3 - PC3 | PC3 dùng mạng `10.10.1.16/28`, gateway là R3 `G0/1`. |
| IPv6 LAN bên phải | R3 - S4 - PC4 | PC4 dùng mạng `2001:db8:1:4::/64`, gateway là R3 `G0/0`. |

> **Điểm dễ sai:** Khi `ping` thất bại, không sửa ngay. Dùng `tracert` để xem gói tin dừng ở router nào, sau đó mới kiểm tra địa chỉ interface và bảng định tuyến của router đó.

## 4. Part 1 - Test and Restore IPv4 Connectivity

### 4.1. Hoàn thiện địa chỉ IPv4 trên PC1 và PC3

```text
PC1> ipconfig /all

! Ghi lại IPv4 Address, Subnet Mask, Default Gateway của PC1

PC3> ipconfig /all

! Ghi lại IPv4 Address, Subnet Mask, Default Gateway của PC3
```

| PC | Network đúng | Gateway đúng | Kết luận cần kiểm tra |
| --- | --- | --- | --- |
| PC1 | `10.10.1.96/27` | `10.10.1.97` | IP PC1 phải cùng subnet với R1 `G0/1`. |
| PC3 | `10.10.1.16/28` | `10.10.1.17` | IP PC3 phải cùng subnet với R3 `G0/1`. |

![PC IPv4 configuration](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/pc-ipv4-config.png)

### 4.2. Kiểm tra ping IPv4 ban đầu

```text
PC1> ping 10.10.1.30

PC3> ping 10.10.1.126
```

| Test | Kết quả ban đầu | Ý nghĩa |
| --- | --- | --- |
| PC1 ping PC3 | Fail | Có lỗi trên đường IPv4 end-to-end. |
| PC3 ping PC1 | Fail | Lỗi ảnh hưởng hai chiều, cần kiểm tra router trung gian. |

![IPv4 ping failed](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/ipv4-ping-failed.png)

### 4.3. Dùng traceroute để khoanh vùng lỗi IPv4

```text
PC1> tracert 10.10.1.30

! Dừng trace bằng Ctrl+C nếu chạy quá lâu

PC3> tracert 10.10.1.126

! Dừng trace bằng Ctrl+C nếu chạy quá lâu
```

| Hướng trace | Hop kỳ vọng | Ý nghĩa khi dừng |
| --- | --- | --- |
| PC1 → PC3 | PC1 → R1 → R2 → R3 → PC3 | Nếu dừng trước/ở R2, kiểm tra serial IPv4 trên R2. |
| PC3 → PC1 | PC3 → R3 → R2 → R1 → PC1 | Nếu dừng trước/ở R2, kiểm tra serial IPv4 trên R2. |

![IPv4 tracert failed](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/ipv4-tracert-failed.png)

### 4.4. Kiểm tra R1, R2, R3

```text
R1> enable
Password: class
R1# show ip interface brief
R1# show ip route

R2> enable
Password: class
R2# show ip interface brief
R2# show ip route

R3> enable
Password: class
R3# show ip interface brief
R3# show ip route
```

| Router | Interface cần đúng | Địa chỉ đúng | Connected route kỳ vọng |
| --- | --- | --- | --- |
| R1 | S0/0/1 | `10.10.1.6/30` | `10.10.1.4/30` |
| R2 | S0/0/0 | `10.10.1.5/30` | `10.10.1.4/30` |
| R2 | S0/0/1 | `10.10.1.9/30` | `10.10.1.8/30` |
| R3 | S0/0/1 | `10.10.1.10/30` | `10.10.1.8/30` |

> **Lưu ý:** R1 và R2 phải cùng subnet trên link `10.10.1.4/30`. R2 và R3 phải cùng subnet trên link `10.10.1.8/30`.

### 4.5. Documentation Table - IPv4

| Location | Problem | Solution |
| --- | --- | --- |
| R2 | IPv4 trên serial link không khớp với topology hoặc bị cấu hình sai interface | Sửa `S0/0/0` thành `10.10.1.5/30` và `S0/0/1` thành `10.10.1.9/30`. |
| PC1/PC3 | Có thể sai IPv4 address, subnet mask hoặc default gateway | Kiểm tra bằng `ipconfig /all`, sửa theo Addressing Table nếu sai. |
| R1/R3 route | Có thể thiếu route tới mạng remote | Kiểm tra `show ip route`; giữ đúng static/dynamic route có sẵn trong bài. |

### 4.6. Sửa lỗi IPv4 trên R2

```text
R2# configure terminal
R2(config)# interface s0/0/0
R2(config-if)# ip address 10.10.1.5 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# interface s0/0/1
R2(config-if)# ip address 10.10.1.9 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# end
R2# copy running-config startup-config
```

> **Lưu ý:** Nếu interface serial trong file của bạn đang đúng địa chỉ nhưng vẫn lỗi, kiểm tra tiếp `show ip route`. Không đổi loại route nếu đề yêu cầu giữ thiết kế định tuyến có sẵn.

### 4.7. Kiểm tra lại IPv4

```text
R2# show ip interface brief
R2# show ip route

PC1> ping 10.10.1.30
PC3> ping 10.10.1.126

PC1> tracert 10.10.1.30
PC3> tracert 10.10.1.126
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `show ip interface brief` trên R2 | `S0/0/0` và `S0/0/1` có IP đúng, trạng thái up/up. |
| PC1 ping PC3 | Successful. |
| PC3 ping PC1 | Successful. |
| `tracert` IPv4 | Đi qua R1, R2, R3 rồi tới PC đích. |

![IPv4 connectivity restored](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/ipv4-connectivity-restored.png)

## 5. Part 2 - Test and Restore IPv6 Connectivity

### 5.1. Hoàn thiện địa chỉ IPv6 trên PC2 và PC4

```text
PC2> ipv6config /all

! Ghi lại IPv6 Address, Prefix, Default Gateway của PC2

PC4> ipv6config /all

! Ghi lại IPv6 Address, Prefix, Default Gateway của PC4
```

| PC | Network đúng | Gateway đúng | Kết luận cần kiểm tra |
| --- | --- | --- | --- |
| PC2 | `2001:db8:1:1::/64` | R1 `G0/0` | PC2 phải đi gateway ở LAN trái. |
| PC4 | `2001:db8:1:4::/64` | R3 `G0/0` | PC4 phải đi gateway ở LAN phải. |

![PC IPv6 configuration](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/pc-ipv6-config.png)

### 5.2. Kiểm tra ping IPv6 ban đầu

```text
PC2> ping 2001:db8:1:4::a

PC4> ping 2001:db8:1:1::a
```

| Test | Kết quả ban đầu | Ý nghĩa |
| --- | --- | --- |
| PC2 ping PC4 | Fail | Có lỗi trên đường IPv6 end-to-end. |
| PC4 ping PC2 | Fail | Cần kiểm tra gateway hoặc IPv6 trên router. |

![IPv6 ping failed](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/ipv6-ping-failed.png)

### 5.3. Dùng traceroute để khoanh vùng lỗi IPv6

```text
PC2> tracert 2001:db8:1:4::a

! Dừng trace bằng Ctrl+C nếu chạy quá lâu

PC4> tracert 2001:db8:1:1::a

! Dừng trace bằng Ctrl+C nếu chạy quá lâu
```

| Hướng trace | Hop kỳ vọng | Ý nghĩa khi dừng |
| --- | --- | --- |
| PC2 → PC4 | PC2 → R1 → R2 → R3 → PC4 | Nếu dừng ở phía R3/PC4, kiểm tra IPv6 gateway LAN phải. |
| PC4 → PC2 | PC4 → R3 → R2 → R1 → PC2 | Nếu không ra khỏi LAN phải, kiểm tra PC4 gateway hoặc R3 `G0/0`. |

### 5.4. Kiểm tra IPv6 trên R3

```text
R3> enable
Password: class
R3# show ipv6 interface brief
R3# show ipv6 route
```

| Interface | IPv6 đúng | Vai trò |
| --- | --- | --- |
| R3 G0/0 | `2001:db8:1:4::1/64` | Gateway cho PC4. |
| R3 S0/0/1 | `2001:db8:1:3::2/64` | Kết nối về R2. |
| R3 S0/0/1 | `fe80::3` | Link-local serial theo bảng đề. |

### 5.5. Documentation Table - IPv6

| Location | Problem | Solution |
| --- | --- | --- |
| R3 G0/0 hoặc PC4 gateway | Gateway IPv6 của PC4 không khớp với địa chỉ IPv6 trên cổng LAN của R3 | Sửa R3 `G0/0` đúng `2001:db8:1:4::1/64` hoặc sửa gateway PC4 đúng với R3 `G0/0`. |
| R3 | Có thể thiếu `ipv6 unicast-routing` | Bật `ipv6 unicast-routing` nếu router không forward IPv6. |
| PC2/PC4 | Có thể sai IPv6 address hoặc prefix | Kiểm tra bằng `ipv6config /all`, sửa theo Addressing Table. |

### 5.6. Sửa lỗi IPv6 trên R3

```text
R3# configure terminal
R3(config)# ipv6 unicast-routing
R3(config)# interface g0/0
R3(config-if)# no ipv6 address 2001:db8:1:5::1/64
R3(config-if)# ipv6 address 2001:db8:1:4::1/64
R3(config-if)# no shutdown
R3(config-if)# end
R3# copy running-config startup-config
```

> **Lưu ý:** Dòng `no ipv6 address 2001:db8:1:5::1/64` chỉ dùng khi bạn thấy địa chỉ sai đó xuất hiện trong `show ipv6 interface brief`. Nếu địa chỉ sai khác, xóa đúng địa chỉ sai trong file của bạn.

### 5.7. Kiểm tra lại IPv6

```text
R3# show ipv6 interface brief
R3# show ipv6 route

PC2> ping 2001:db8:1:4::a
PC4> ping 2001:db8:1:1::a

PC2> tracert 2001:db8:1:4::a
PC4> tracert 2001:db8:1:1::a
```

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| `show ipv6 interface brief` trên R3 | G0/0 có `2001:db8:1:4::1/64`, trạng thái up/up. |
| PC2 ping PC4 | Successful. |
| PC4 ping PC2 | Successful. |
| `tracert` IPv6 | Đi qua R1, R2, R3 rồi tới PC đích. |

![IPv6 connectivity restored](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-02/ipv6-connectivity-restored.png)

## 6. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| PC cùng mạng ping được nhưng khác mạng ping fail | Sai default gateway hoặc router trung gian lỗi | Kiểm tra `ipconfig /all`, `tracert`, `show ip route`. |
| Traceroute dừng ở router đầu tiên | Router không có route hoặc link kế tiếp sai IP | Kiểm tra serial interface và bảng định tuyến. |
| R2 không nối được R1/R3 | Serial interface sai subnet hoặc sai địa chỉ | Sửa `S0/0/0` và `S0/0/1` đúng subnet `/30`. |
| IPv6 ping fail nhưng IPv4 đã hoạt động | IPv6 là cấu hình riêng, không tự kế thừa IPv4 | Kiểm tra `show ipv6 interface brief` và `ipv6 unicast-routing`. |
| PC4 không ra khỏi LAN bằng IPv6 | Gateway IPv6 không khớp R3 LAN interface | Sửa gateway PC4 hoặc IPv6 trên R3 `G0/0`. |
| Xóa IPv6 sai không hết | IPv6 interface có thể giữ nhiều địa chỉ | Dùng `no ipv6 address <địa-chỉ-sai>/<prefix>` trước khi thêm địa chỉ đúng. |

## 7. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| PC1 ↔ PC3 IPv4 | Ping thành công hai chiều. |
| PC2 ↔ PC4 IPv6 | Ping thành công hai chiều. |
| Traceroute IPv4 | Đường đi thể hiện qua R1 → R2 → R3. |
| Traceroute IPv6 | Đường đi thể hiện qua R1 → R2 → R3. |
| Router interfaces | Các interface cần dùng đều up/up. |
| Check Results | Đạt yêu cầu sau khi sửa lỗi. |

- [ ] Chụp `ipconfig /all` trên PC1 và PC3.
- [ ] Chụp `ipv6config /all` trên PC2 và PC4.
- [ ] Chụp `tracert` IPv4 trước khi sửa.
- [ ] Chụp `tracert` IPv6 trước khi sửa.
- [ ] Chụp `show ip interface brief` trên R2 sau khi sửa.
- [ ] Chụp `show ipv6 interface brief` trên R3 sau khi sửa.
- [ ] Chụp ping thành công PC1 ↔ PC3.
- [ ] Chụp ping thành công PC2 ↔ PC4.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/">Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/">Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/">Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/">Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/">Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge</a></li>
    </ul>
  </details>
</div>

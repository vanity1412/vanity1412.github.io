---
layout: page-toc
title: "CCNA 18.01 - 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thiện bảng địa chỉ, cô lập lỗi default gateway/IP sai và kiểm tra end-to-end connectivity |

> **Ghi chú:** Lab này không phải bài cấu hình mới hoàn toàn. Trọng tâm là đọc bảng địa chỉ, kiểm tra ping theo từng lớp gần → xa, phát hiện sai IP/default gateway và sửa từng lỗi một.

## 1. Mục Tiêu Bài Lab

- Hoàn thiện thông tin default gateway còn thiếu trong bảng địa chỉ.
- Kiểm tra kết nối nội bộ trong cùng subnet.
- Kiểm tra kết nối giữa hai mạng `192.168.10.0/24` và `192.168.11.0/24`.
- Xác định lỗi cấu hình trên PC, switch hoặc router bằng `ping`, `ipconfig`, `show`.
- Sửa lỗi từng bước và ghi lại nguyên nhân, cách phát hiện, cách xử lý.
- Xác nhận tất cả PC có thể ping qua lại sau khi sửa.

![Topology lab 01](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/topology.png)

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| R1 | G0/0 | `192.168.10.1` | `255.255.255.0` | N/A |
| R1 | G0/1 | `192.168.11.1` | `255.255.255.0` | N/A |
| S1 | VLAN 1 | `192.168.10.2` | `255.255.255.0` | `192.168.10.1` |
| S2 | VLAN 1 | `192.168.11.2` | `255.255.255.0` | `192.168.11.1` |
| PC1 | NIC | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC2 | NIC | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` |
| PC3 | NIC | `192.168.11.10` | `255.255.255.0` | `192.168.11.1` |
| PC4 | NIC | `192.168.11.11` | `255.255.255.0` | `192.168.11.1` |

> **Lưu ý:** Default gateway của host phải là IP router nằm cùng subnet với host. Ví dụ PC1 thuộc `192.168.10.0/24`, gateway đúng là `192.168.10.1`, không phải `192.168.11.1`.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 1 | PC1, PC2, S1, R1 G0/0 | Dùng mạng `192.168.10.0/24`; gateway là `192.168.10.1`. |
| LAN 2 | PC3, PC4, S2, R1 G0/1 | Dùng mạng `192.168.11.0/24`; gateway là `192.168.11.1`. |
| Router trung tâm | R1 | Định tuyến trực tiếp giữa hai mạng LAN. |
| Switch quản trị | S1, S2 | Cần `ip default-gateway` để switch VLAN 1 có thể được truy cập từ mạng khác. |

> **Điểm dễ sai:** PC cùng LAN vẫn ping nhau được dù default gateway sai. Default gateway sai thường chỉ lộ rõ khi ping sang mạng khác.

## 4. Part 1 - Verify Network Documentation and Isolate Problems

### Step 1 - Kiểm tra IP trên PC

Trên từng PC vào **Desktop > Command Prompt**.

```text
ipconfig
```

| Thiết bị | Giá trị cần khớp | Nếu sai thì sửa ở đâu |
| --- | --- | --- |
| PC1 | `192.168.10.10 /24`, GW `192.168.10.1` | Desktop > IP Configuration |
| PC2 | `192.168.10.11 /24`, GW `192.168.10.1` | Desktop > IP Configuration |
| PC3 | `192.168.11.10 /24`, GW `192.168.11.1` | Desktop > IP Configuration |
| PC4 | `192.168.11.11 /24`, GW `192.168.11.1` | Desktop > IP Configuration |

![PC IP configuration](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/pc-ip-configuration.png)

> **Lưu ý:** Đề đã gợi ý lỗi đầu tiên là IP address trên PC1. Vì vậy cần kiểm tra PC1 trước bằng `ipconfig`, rồi sửa đúng về `192.168.10.10/24`.

### Step 2 - Kiểm tra router R1

```text
R1> enable
R1# show ip interface brief
R1# show ip route
```

| Interface | IP đúng | Trạng thái cần có |
| --- | --- | --- |
| G0/0 | `192.168.10.1` | up/up |
| G0/1 | `192.168.11.1` | up/up |

Nếu router sai địa chỉ hoặc interface shutdown, sửa theo cấu hình chuẩn:

```text
R1# configure terminal
interface g0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
 exit
interface g0/1
 ip address 192.168.11.1 255.255.255.0
 no shutdown
 exit
end
copy running-config startup-config
```

![R1 show ip interface brief](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/r1-show-ip-interface-brief.png)

### Step 3 - Kiểm tra default gateway trên switch

Trên S1:

```text
S1> enable
S1# show running-config
S1# show ip interface brief
```

Cấu hình đúng cho S1:

```text
S1# configure terminal
interface vlan 1
 ip address 192.168.10.2 255.255.255.0
 no shutdown
 exit
ip default-gateway 192.168.10.1
end
copy running-config startup-config
```

Trên S2:

```text
S2> enable
S2# show running-config
S2# show ip interface brief
```

Cấu hình đúng cho S2:

```text
S2# configure terminal
interface vlan 1
 ip address 192.168.11.2 255.255.255.0
 no shutdown
 exit
ip default-gateway 192.168.11.1
end
copy running-config startup-config
```

> **Lưu ý:** `ip default-gateway` trên switch Layer 2 dùng cho quản trị từ xa. Nó không thay router định tuyến giữa hai LAN.

## 5. Part 2 - Implement, Verify, and Document Solutions

### Step 1 - Sửa IP/default gateway trên các PC

| PC | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| PC1 | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC2 | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` |
| PC3 | `192.168.11.10` | `255.255.255.0` | `192.168.11.1` |
| PC4 | `192.168.11.11` | `255.255.255.0` | `192.168.11.1` |

![PC gateway corrected](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/pc-gateway-corrected.png)

### Step 2 - Documentation Table

| Test | Successful ban đầu? | Vấn đề phát hiện | Cách sửa | Verified |
| --- | --- | --- | --- | --- |
| PC1 → PC2 | No | IP address trên PC1 không khớp bảng địa chỉ | Sửa PC1 về `192.168.10.10/24`, gateway `192.168.10.1` | Yes |
| PC1 → S1 | Có thể No nếu PC1 sai IP | PC1 không cùng subnet với S1 hoặc gateway/IP sai | Kiểm tra `ipconfig`, sửa IP PC1 | Yes |
| PC1 → R1 G0/0 | Có thể No nếu PC1 sai IP | PC1 không tới được gateway cục bộ | Sửa PC1 và kiểm tra R1 G0/0 up/up | Yes |
| PC3 → PC4 | Có thể Yes | Cùng LAN `192.168.11.0/24` | Không sửa nếu ping thành công | Yes |
| PC1 → PC4 | No nếu gateway sai | Default gateway trên PC hoặc router interface sai | Sửa gateway PC1/PC4 theo local LAN | Yes |
| S1 → S2 | No nếu switch thiếu gateway | Switch Layer 2 thiếu `ip default-gateway` | Cấu hình gateway S1/S2 đúng subnet | Yes |

> **Lưu ý:** Khi troubleshoot, sửa một lỗi rồi test lại. Không nên sửa nhiều chỗ cùng lúc vì sẽ khó biết lỗi thật nằm ở đâu.

## 6. Kiểm Tra Và Bằng Chứng

### Kiểm tra local connectivity

```text
! Trên PC1
ping 192.168.10.11
ping 192.168.10.2
ping 192.168.10.1

! Trên PC3
ping 192.168.11.11
ping 192.168.11.2
ping 192.168.11.1
```

![Local ping result](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/local-ping-result.png)

### Kiểm tra remote connectivity

```text
! Từ LAN 192.168.10.0/24 sang LAN 192.168.11.0/24
PC1> ping 192.168.11.10
PC1> ping 192.168.11.11

! Từ LAN 192.168.11.0/24 sang LAN 192.168.10.0/24
PC4> ping 192.168.10.10
PC4> ping 192.168.10.11
```

![Remote ping result](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-01/remote-ping-result.png)

### Kiểm tra đường đi bằng tracert

```text
PC1> tracert 192.168.11.11
PC4> tracert 192.168.10.10
```

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
| PC1 ping PC2 | Success | `local-ping-result.png` |
| PC3 ping PC4 | Success | `local-ping-result.png` |
| PC1 ping R1 G0/0 | Success | `local-ping-result.png` |
| PC4 ping R1 G0/1 | Success | `local-ping-result.png` |
| PC1 ping PC4 | Success | `remote-ping-result.png` |
| PC4 ping PC1 | Success | `remote-ping-result.png` |
| S1/S2 có default gateway đúng | `ip default-gateway` khớp router local | `switch-gateway.png` |

## 7. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC1 không ping được PC2 | IP PC1 sai hoặc không cùng subnet | `ipconfig` trên PC1 | Sửa PC1 thành `192.168.10.10/24` |
| PC ping được cùng LAN nhưng không ping được khác LAN | Default gateway sai hoặc thiếu | `ipconfig`, ping gateway local | Đặt gateway đúng: `192.168.10.1` hoặc `192.168.11.1` |
| Switch không ping được thiết bị khác mạng | Thiếu `ip default-gateway` | `show running-config` trên switch | Cấu hình `ip default-gateway` đúng router local |
| Router không định tuyến được hai LAN | Interface G0/0 hoặc G0/1 down/sai IP | `show ip interface brief` | Sửa IP và `no shutdown` |
| Sửa xong nhưng ping vẫn fail lần đầu | ARP chưa cập nhật hoặc ICMP timeout ban đầu | Ping lại lần 2 | Chờ vài giây hoặc ping lại |

## 8. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| Bảng default gateway | Hoàn thiện đúng cho S1, S2, PC1, PC2, PC3, PC4 |
| Local connectivity | Các thiết bị cùng LAN ping nhau thành công |
| Gateway connectivity | Từng PC ping được gateway của subnet mình |
| Remote connectivity | PC ở `192.168.10.0/24` ping được PC ở `192.168.11.0/24` |
| Troubleshooting documentation | Có bảng ghi lỗi, nguyên nhân, cách sửa, trạng thái verified |
| Check Results | Hoàn thành sau khi sửa toàn bộ lỗi cấu hình |

- [ ] `topology.png` - ảnh sơ đồ mạng.
- [ ] `pc-ip-configuration.png` - ảnh kiểm tra IP ban đầu trên PC.
- [ ] `pc-gateway-corrected.png` - ảnh PC sau khi sửa gateway/IP.
- [ ] `r1-show-ip-interface-brief.png` - ảnh kiểm tra interface R1.
- [ ] `switch-gateway.png` - ảnh cấu hình gateway trên S1/S2.
- [ ] `local-ping-result.png` - ảnh ping cùng LAN.
- [ ] `remote-ping-result.png` - ảnh ping khác LAN.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/">Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/">Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/">Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/">Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/">Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge</a></li>
    </ul>
  </details>
</div>

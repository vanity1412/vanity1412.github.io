---
layout: page-toc
title: "CCNA 18.05 - 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues"
permalink: /writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-05/
toc: true
---

[← Quay lại danh sách Kiểm Tra Và Xử Lý Sự Cố](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/)

| Field | Value |
| --- | --- |
| Dạng lab | Kiểm Tra Và Xử Lý Sự Cố |
| File lab | `17.7.7 Packet Tracer - Troubleshoot Connectivity Issues.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Hoàn thành khi toàn bộ PC truy cập được `www.cisco.pka` và ping được `209.165.201.2` |

> **Đặc điểm bài này:** đây là lab xử lý sự cố kết nối. Không cấu hình lại toàn bộ mạng từ đầu, mà cần dùng `ipconfig`, `ping`, `tracert`, kiểm tra DNS và kiểm tra route trên R1 để xác định lỗi rồi sửa đúng điểm sai.

## 1. Mục Tiêu Bài Lab

- Kiểm tra cấu hình IPv4, subnet mask, default gateway và DNS trên từng PC.
- Xác minh kết nối nội bộ trong từng LAN: `172.16.1.0/24` và `172.16.2.0/24`.
- Kiểm tra kết nối từ các PC đến Web Server `209.165.201.2`.
- Kiểm tra truy cập website bằng tên miền `www.cisco.pka` và bằng địa chỉ IP.
- Dùng SSH vào R1 để kiểm tra interface, bảng định tuyến và route ra ISP.
- Ghi lại lỗi, nguyên nhân, cách sửa và bằng chứng sau khi sửa.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/topology.png)

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| R1 | G0/0 | `172.16.1.1` | `255.255.255.0` | N/A | Gateway LAN PC-01/PC-02 |
| R1 | G0/1 | `172.16.2.1` | `255.255.255.0` | N/A | Gateway LAN PC-A/PC-B |
| R1 | S0/0/0 | `209.165.200.226` | `255.255.255.252` | N/A | Kết nối ISP |
| R2 | G0/0 | `209.165.201.1` | `255.255.255.224` | N/A | Gateway server network |
| R2 | S0/0/0 | `209.165.200.225` | `255.255.255.252` | N/A | ISP router, không truy cập được |
| PC-01 | NIC | `172.16.1.3` | `255.255.255.0` | `172.16.1.1` | DNS nên trỏ về DNS hoạt động |
| PC-02 | NIC | `172.16.1.4` | `255.255.255.0` | `172.16.1.1` | DNS nên trỏ về DNS hoạt động |
| PC-A | NIC | `172.16.2.3` | `255.255.255.0` | `172.16.2.1` | DNS nên trỏ về DNS hoạt động |
| PC-B | NIC | `172.16.2.4` | `255.255.255.0` | `172.16.2.1` | Có thể liên quan DNS2 |
| Web | NIC | `209.165.201.2` | `255.255.255.224` | `209.165.201.1` | Server `www.cisco.pka` |
| DNS1 | NIC | `209.165.201.3` | `255.255.255.224` | `209.165.201.1` | DNS chính |
| DNS2 | NIC | `209.165.201.4` | `255.255.255.224` | `209.165.201.1` | DNS mới thêm |

> **Lưu ý:** nếu ping bằng IP thành công nhưng truy cập `www.cisco.pka` thất bại, lỗi thường nằm ở DNS, không phải routing.

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| LAN 1 | PC-01, PC-02, S1, R1 G0/0 | Mạng `172.16.1.0/24`, gateway đúng là `172.16.1.1` |
| LAN 2 | PC-A, PC-B, S2, R1 G0/1 | Mạng `172.16.2.0/24`, gateway đúng là `172.16.2.1` |
| WAN | R1 S0/0/0 ↔ R2 S0/0/0 | Mạng point-to-point `209.165.200.224/30` |
| ISP Server Network | Web, DNS1, DNS2 | Mạng `209.165.201.0/27`, gateway server là `209.165.201.1` |
| Điểm hạn chế | R2, Web, DNS1, DNS2 | Không có quyền truy cập trực tiếp, nếu lỗi nằm tại DNS2/server thì cần escalated |

> **Điểm dễ sai:** các PC cùng LAN có thể ping nhau dù default gateway sai. Default gateway chỉ thể hiện rõ khi ping sang mạng khác hoặc truy cập Web Server.

## 4. Quy Trình Xử Lý Sự Cố

### Part 1 - Kiểm tra nhanh từ từng PC

```text
C:\> ipconfig
C:\> ping <default-gateway>
C:\> ping 209.165.201.2
C:\> ping <PC-cung-LAN>
C:\> ping <PC-khac-LAN>
C:\> tracert 209.165.201.2
```

| Thiết bị kiểm tra | Lệnh kiểm tra | Kết quả mong muốn |
| --- | --- | --- |
| PC-01 | `ping 172.16.1.1` | Thành công |
| PC-01 | `ping 172.16.1.4` | Thành công |
| PC-01 | `ping 172.16.2.3` | Thành công sau khi routing/gateway đúng |
| PC-01 | `ping 209.165.201.2` | Thành công nếu R1 có route ra ISP |
| PC-02 | `ping 172.16.1.1` | Thành công |
| PC-A | `ping 172.16.2.1` | Thành công |
| PC-B | `ping 172.16.2.1` | Thành công |

![PC ping tests](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/pc-ping-tests.png)

### Part 2 - Kiểm tra truy cập web bằng tên miền và địa chỉ IP

```text
! Kiểm tra bằng tên miền
http://www.cisco.pka

! Kiểm tra bằng IP Web Server
http://209.165.201.2
```

| Trường hợp | Kết luận |
| --- | --- |
| URL lỗi, IP lỗi | Có thể sai IP/gateway/route |
| URL lỗi, IP chạy | Lỗi DNS hoặc PC đang trỏ sai DNS server |
| URL chạy, IP chạy | Kết nối và DNS đã đúng |

![Web access test](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/web-access-test.png)

### Part 3 - Kiểm tra và sửa cấu hình IP trên PC

| PC | IP đúng | Mask đúng | Gateway đúng | DNS khuyến nghị |
| --- | --- | --- | --- | --- |
| PC-01 | `172.16.1.3` | `255.255.255.0` | `172.16.1.1` | `209.165.201.3` hoặc DNS đang hoạt động |
| PC-02 | `172.16.1.4` | `255.255.255.0` | `172.16.1.1` | `209.165.201.3` hoặc DNS đang hoạt động |
| PC-A | `172.16.2.3` | `255.255.255.0` | `172.16.2.1` | `209.165.201.3` hoặc DNS đang hoạt động |
| PC-B | `172.16.2.4` | `255.255.255.0` | `172.16.2.1` | Kiểm tra kỹ nếu đang dùng DNS2 `209.165.201.4` |

> **Lưu ý:** trong Packet Tracer, vào **PC > Desktop > IP Configuration** để sửa IP, subnet mask, default gateway và DNS server.

![PC IP configuration](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/pc-ip-configuration.png)

### Part 4 - SSH vào R1 và kiểm tra route ra ISP

R1 chỉ truy cập bằng SSH với tài khoản `Admin01` và mật khẩu `cisco12345`.

```text
C:\> ssh -l Admin01 172.16.1.1
Password: cisco12345

R1> enable
R1# show ip interface brief
R1# show ip route
R1# show running-config | include ip route
R1# ping 209.165.200.225
R1# ping 209.165.201.2
```

| Lệnh | Mục đích | Kết quả cần thấy |
| --- | --- | --- |
| `show ip interface brief` | Kiểm tra IP và trạng thái cổng R1 | G0/0, G0/1, S0/0/0 đều `up/up` |
| `show ip route` | Kiểm tra R1 có đường đến ISP server network không | Có route tới `209.165.201.0/27` hoặc default route |
| `ping 209.165.200.225` | Kiểm tra link R1 ↔ R2 | Thành công |
| `ping 209.165.201.2` | Kiểm tra R1 tới Web Server | Thành công |

Nếu R1 thiếu đường ra mạng ISP server, cấu hình một trong hai cách sau:

```text
R1# configure terminal
! Cách 1: default route ra ISP
R1(config)# ip route 0.0.0.0 0.0.0.0 209.165.200.225
R1(config)# end
R1# copy running-config startup-config
```

```text
R1# configure terminal
! Cách 2: static route cụ thể tới server network
R1(config)# ip route 209.165.201.0 255.255.255.224 209.165.200.225
R1(config)# end
R1# copy running-config startup-config
```

> **Lưu ý:** nếu Packet Tracer chấm theo cấu hình cụ thể, nên giữ đúng kiểu route mà lab đang yêu cầu. Với bài troubleshoot, mục tiêu là PC đi được tới `209.165.201.2`.

![R1 route check](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/r1-route-check.png)

## 5. Documentation Table

| Vị trí | Dấu hiệu | Nguyên nhân có thể | Cách sửa | Verified |
| --- | --- | --- | --- | --- |
| PC-01 | Không ping được gateway hoặc PC cùng LAN | Sai IP/mask/gateway | Đặt lại `172.16.1.3/24`, gateway `172.16.1.1` | `[ ]` |
| PC-02 | Không ping được gateway hoặc PC-01 | Sai IP/mask/gateway | Đặt lại `172.16.1.4/24`, gateway `172.16.1.1` | `[ ]` |
| PC-A | Không ping được gateway hoặc PC-B | Sai IP/mask/gateway | Đặt lại `172.16.2.3/24`, gateway `172.16.2.1` | `[ ]` |
| PC-B | Ping IP server được nhưng URL lỗi | DNS server/record sai | Dùng DNS hoạt động hoặc escalated lỗi DNS2 | `[ ]` |
| R1 | PC ping gateway được nhưng không ping Web Server | Thiếu route ra ISP | Thêm default route hoặc static route tới `209.165.201.0/27` | `[ ]` |
| DNS2 | Muốn dùng DNS2 nhưng URL vẫn lỗi | DNS2 sai bản ghi `www.cisco.pka` | Cần người có quyền trên server/DNS2 sửa bản ghi | `[ ]` |

> **Trả lời câu hỏi PC-B:** nếu DNS2 đang sai bản ghi và mình không có quyền truy cập DNS2/server, không thể vừa giữ DNS2 vừa tự sửa triệt để từ phía PC-B. Cần escalated cho nhóm quản trị DNS/server để sửa record `www.cisco.pka -> 209.165.201.2`, hoặc tạm thời đổi PC-B sang DNS1 đang hoạt động.

## 6. Kiểm Tra Sau Khi Sửa

### Kiểm tra từ PC-01

```text
C:\> ping 172.16.1.1
C:\> ping 172.16.1.4
C:\> ping 172.16.2.3
C:\> ping 172.16.2.4
C:\> ping 209.165.201.2
```

### Kiểm tra từ PC-02

```text
C:\> ping 172.16.1.1
C:\> ping 172.16.1.3
C:\> ping 172.16.2.3
C:\> ping 172.16.2.4
C:\> ping 209.165.201.2
```

### Kiểm tra từ PC-A

```text
C:\> ping 172.16.2.1
C:\> ping 172.16.2.4
C:\> ping 172.16.1.3
C:\> ping 172.16.1.4
C:\> ping 209.165.201.2
```

### Kiểm tra từ PC-B

```text
C:\> ping 172.16.2.1
C:\> ping 172.16.2.3
C:\> ping 172.16.1.3
C:\> ping 172.16.1.4
C:\> ping 209.165.201.2
```

### Kiểm tra web cuối cùng

```text
http://www.cisco.pka
http://209.165.201.2
```

![Final verification](/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/labs/lab-05/final-verification.png)

## 7. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| PC không ping được gateway | Sai IP, subnet mask hoặc default gateway | `ipconfig`, `ping <gateway>` | Sửa lại theo Addressing Table |
| PC cùng LAN ping nhau lỗi | Sai IP/mask hoặc cáp/cổng chưa up | `ipconfig`, quan sát link light | Sửa IP/mask, chờ link xanh |
| PC ping gateway được nhưng không ping Web Server | R1 thiếu route ra ISP hoặc WAN lỗi | `tracert 209.165.201.2`, `show ip route` | Thêm route trên R1 hoặc kiểm tra serial link |
| Truy cập bằng IP được nhưng URL lỗi | DNS server sai hoặc bản ghi DNS sai | Mở `http://209.165.201.2` và `http://www.cisco.pka` để so sánh | Sửa DNS trên PC hoặc escalated DNS server |
| Không SSH được R1 | Sai username/password hoặc SSH tới sai IP | `ssh -l Admin01 172.16.1.1` | Dùng đúng `Admin01/cisco12345` và IP gateway gần PC |
| Chỉnh nhiều lỗi cùng lúc khó kiểm chứng | Không xác định được lỗi nào đã được sửa | Log kết quả trước/sau | Sửa từng lỗi, test lại từng bước |

## 8. Kết Quả Cuối

| Hạng mục | Kết quả mong muốn |
| --- | --- |
| PC-01, PC-02 | IP/mask/gateway đúng theo bảng |
| PC-A, PC-B | IP/mask/gateway đúng theo bảng |
| R1 | Các interface `G0/0`, `G0/1`, `S0/0/0` hoạt động |
| Routing | R1 có đường tới `209.165.201.0/27` hoặc default route ra `209.165.200.225` |
| DNS | `www.cisco.pka` phân giải về Web Server `209.165.201.2` |
| Web access | Tất cả PC truy cập được `www.cisco.pka` |
| Check Results | Hoàn thành 100% sau khi sửa đúng lỗi |

Checklist ảnh minh chứng:

- [ ] `ipconfig` đúng trên PC-01, PC-02, PC-A, PC-B.
- [ ] Ping gateway thành công từ từng PC.
- [ ] Ping `209.165.201.2` thành công từ từng PC.
- [ ] Truy cập `http://www.cisco.pka` thành công.
- [ ] `show ip interface brief` trên R1.
- [ ] `show ip route` trên R1.
- [ ] Check Results đạt 100%.

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 6 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-01/">Lab 1: 10.3.5 Packet Tracer - Troubleshoot Default Gateway Issues</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-02/">Lab 2: 13.2.7 Packet Tracer - Use Ping and Traceroute to Test Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-03/">Lab 3: 13.3.1 Packet Tracer - Use ICMP to Test and Correct Network Connectivity</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-04/">Lab 4: 17.5.9 Packet Tracer - Interpret show Command Output</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 17.7.7 Packet Tracer - Troubleshoot Connectivity Issues (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/lab-06/">Lab 6: 17.8.3 Packet Tracer - Troubleshooting Challenge</a></li>
    </ul>
  </details>
</div>

---
layout: page-toc
title: "CCNA 06.01 - 3.1.4 Packet Tracer - Who Hears the Broadcast"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.1.4 Packet Tracer - Who Hears the Broadcast.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-01/` |
| Trạng thái | Hoàn thành quan sát broadcast/unicast theo từng VLAN và trả lời reflection questions |

> **Ghi chú:** Bài này không yêu cầu cấu hình CLI. Nhiệm vụ chính là dùng **Simulation mode**, tạo broadcast ICMP bằng **Add Complex PDU**, quan sát switch flood frame trong từng VLAN và xác định đúng collision domain / broadcast domain.

---

## 1. Mục Tiêu Bài Lab

- Kiểm tra kết nối ban đầu giữa các PC trong cùng VLAN bằng `ping`
- Tạo broadcast packet đến địa chỉ `255.255.255.255` bằng **Add Complex PDU**
- Quan sát cách switch xử lý broadcast traffic trong từng VLAN
- Phân biệt broadcast domain, collision domain và phạm vi truyền frame theo VLAN
- Trả lời các câu hỏi reflection dựa trên kết quả quan sát trong Simulation mode

![Topology Who Hears the Broadcast](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/topology.png)

![Instructions Who Hears the Broadcast](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/instructions.png)

---

## 2. Bảng VLAN Và Phạm Vi Thiết Bị

| VLAN | Dải IP trong topology | Thiết bị | Cổng switch tương ứng | Vai trò khi có broadcast |
| --- | --- | --- | --- | --- |
| VLAN 30 | 192.168.1.1 - 192.168.1.8/27 | PC0 - PC7 | Fa0/1 - Fa0/8 | Chỉ các PC trong VLAN 30 nhận broadcast của VLAN 30 |
| VLAN 10 | 192.168.1.33 - 192.168.1.40/27 | PC8 - PC15 | Fa0/9 - Fa0/16 | Chỉ các PC trong VLAN 10 nhận broadcast của VLAN 10 |
| VLAN 20 | 192.168.1.17 - 192.168.1.24/27 | PC16 - PC23 | Fa0/17 - Fa0/24 | Chỉ các PC trong VLAN 20 nhận broadcast của VLAN 20 |

> **Lưu ý:** Broadcast domain trong bài này được quyết định bởi **VLAN**, không chỉ dựa vào địa chỉ IP. Một broadcast từ VLAN này sẽ không đi sang VLAN khác nếu không có thiết bị Layer 3 định tuyến giữa các VLAN.

---

## 3. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Nhóm dưới | PC0 - PC7 | Thuộc VLAN 30, dùng để kiểm tra broadcast trong VLAN 30 |
| Nhóm bên phải | PC8 - PC15 | Thuộc VLAN 10, dùng để kiểm tra broadcast trong VLAN 10 |
| Nhóm bên trái | PC16 - PC23 | Thuộc VLAN 20, dùng để kiểm tra broadcast trong VLAN 20 |
| Switch trung tâm | Catalyst 2960 24-port | Tất cả port đều được sử dụng, mỗi port là một collision domain riêng |

> **Điểm dễ sai:** Khi thấy tất cả PC cùng cắm vào một switch, không được kết luận tất cả cùng một broadcast domain. Switch có VLAN sẽ tách broadcast domain theo từng VLAN.

---

## 4. Part 1: Observe Broadcast Traffic in a VLAN Implementation

### Step 1: Kiểm tra ping trong cùng VLAN

Trên **PC0 → Desktop → Command Prompt**:

```text
ping 192.168.1.8
```

| Kiểm tra | Kết quả mong muốn | Giải thích ngắn |
| --- | --- | --- |
| PC0 ping 192.168.1.8 | Succeed | PC0 và PC7 cùng VLAN 30 |

![Ping PC0 to PC7](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/ping-pc0-pc7.png)

> **Lưu ý:** Ping trong cùng VLAN thành công vì frame chỉ cần được switch chuyển tiếp trong cùng broadcast domain, không cần router.

---

## 5. Part 2: Generate and Examine Broadcast Traffic

### Step 1: Chuyển sang Simulation mode và lọc ICMP

| Thao tác | Giá trị cần chọn |
| --- | --- |
| Mode | Simulation |
| Edit Filters | Bỏ chọn `Show All/None` |
| Protocol cần quan sát | ICMP |

![Simulation ICMP Filter](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/simulation-icmp-filter.png)

---

### Step 2: Tạo Complex PDU từ PC0

| Trường trong Create Complex PDU | Giá trị |
| --- | --- |
| Source | PC0 |
| Destination IP Address | 255.255.255.255 |
| Sequence Number | 1 |
| One Shot Time | 0 |
| Select Application | PING |

![Create Complex PDU PC0](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/create-pdu-pc0.png)

**Câu hỏi:** What are at least 3 other applications available for use?

| Ứng dụng có thể chọn | Ghi chú |
| --- | --- |
| DNS | Kiểm tra phân giải tên miền |
| FTP | Kiểm tra truyền file |
| HTTP | Kiểm tra web traffic |
| HTTPS | Kiểm tra web traffic bảo mật |
| SSH | Kiểm tra truy cập quản trị bảo mật |
| TELNET | Kiểm tra truy cập dòng lệnh không mã hóa |
| TFTP | Kiểm tra truyền file đơn giản |

> Chỉ cần nêu tối thiểu 3 ứng dụng. Ví dụ trả lời ngắn: **DNS, FTP, HTTP**.

---

### Step 3: Quan sát khi bấm Capture/Forward

| Lần quan sát | Kết quả |
| --- | --- |
| Capture/Forward lần 1 | Packet đi từ PC0 vào switch |
| Capture/Forward lần 2 | Switch flood packet ra các port cùng VLAN 30, không gửi sang VLAN 10 hoặc VLAN 20 |

![Broadcast From PC0 VLAN 30](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/broadcast-pc0-vlan30.png)

**Câu hỏi:** What happened to the packet?

| Source | VLAN nguồn | Thiết bị nhận broadcast | Kết luận |
| --- | --- | --- | --- |
| PC0 | VLAN 30 | PC1 - PC7 | Packet được gửi đến switch, sau đó switch chỉ flood trong VLAN 30 |

> **Lưu ý:** Switch không gửi lại frame ra chính cổng nhận vào, nên PC0 là nguồn gửi và các PC còn lại trong VLAN 30 là bên nhận.

---

### Step 4: Lặp lại với PC8 và PC16

| Source | VLAN nguồn | Thiết bị nhận broadcast | Kết luận |
| --- | --- | --- | --- |
| PC8 | VLAN 10 | PC9 - PC15 | Broadcast chỉ nằm trong VLAN 10 |
| PC16 | VLAN 20 | PC17 - PC23 | Broadcast chỉ nằm trong VLAN 20 |

![Broadcast From PC8 VLAN 10](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/broadcast-pc8-vlan10.png)

![Broadcast From PC16 VLAN 20](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/broadcast-pc16-vlan20.png)

---

## 6. Đáp Án Reflection Questions

### Câu 1: If a PC in VLAN 10 sends a broadcast message, which devices receive it?

| VLAN gửi | Thiết bị nhận |
| --- | --- |
| VLAN 10 | Các thiết bị trong VLAN 10: PC8 - PC15 |

> Nếu một PC trong VLAN 10 là nguồn gửi, các PC còn lại trong VLAN 10 sẽ nhận broadcast. VLAN 20 và VLAN 30 không nhận.

---

### Câu 2: If a PC in VLAN 20 sends a broadcast message, which devices receive it?

| VLAN gửi | Thiết bị nhận |
| --- | --- |
| VLAN 20 | Các thiết bị trong VLAN 20: PC16 - PC23 |

> Nếu một PC trong VLAN 20 là nguồn gửi, các PC còn lại trong VLAN 20 sẽ nhận broadcast. VLAN 10 và VLAN 30 không nhận.

---

### Câu 3: If a PC in VLAN 30 sends a broadcast message, which devices receive it?

| VLAN gửi | Thiết bị nhận |
| --- | --- |
| VLAN 30 | Các thiết bị trong VLAN 30: PC0 - PC7 |

> Nếu một PC trong VLAN 30 là nguồn gửi, các PC còn lại trong VLAN 30 sẽ nhận broadcast. VLAN 10 và VLAN 20 không nhận.

---

### Câu 4: What happens to a frame sent from a PC in VLAN 10 to a PC in VLAN 30?

| Tình huống | Kết quả |
| --- | --- |
| PC trong VLAN 10 gửi frame đến PC trong VLAN 30 | Frame bị drop, switch không forward trực tiếp sang VLAN khác |

> Muốn VLAN 10 giao tiếp với VLAN 30 cần có **inter-VLAN routing** bằng router hoặc Layer 3 switch. Trong bài này không có thiết bị Layer 3 xử lý giữa các VLAN.

---

### Câu 5: Which ports on the switch light up if a PC connected to port 11 sends a unicast message to a PC connected to port 13?

| Cổng nguồn | Cổng đích | VLAN | Cổng sáng |
| --- | --- | --- | --- |
| Port 11 | Port 13 | VLAN 10 | Port 11 và Port 13 |

> Đây là unicast trong cùng VLAN, nên switch chỉ chuyển frame giữa cổng nguồn và cổng đích.

---

### Câu 6: Which ports on the switch light if a PC connected to port 2 sends a unicast message to a PC connected to port 23?

| Cổng nguồn | VLAN nguồn | Cổng đích | VLAN đích | Kết quả |
| --- | --- | --- | --- | --- |
| Port 2 | VLAN 30 | Port 23 | VLAN 20 | Frame bị drop, không forward sang port 23 |

> Port 2 và port 23 thuộc hai VLAN khác nhau. Switch Layer 2 không chuyển unicast trực tiếp giữa hai VLAN.

---

### Câu 7: In terms of ports, what are the collision domains on the switch?

| Thiết bị | Collision domain |
| --- | --- |
| Catalyst 2960 24-port switch | Mỗi port là một collision domain riêng |

**Kết luận:** Có **24 collision domains**, tương ứng với **Fa0/1 đến Fa0/24**.

---

### Câu 8: In terms of ports, what are the broadcast domains on the switch?

| Broadcast domain | Port thuộc broadcast domain |
| --- | --- |
| VLAN 30 | Fa0/1 - Fa0/8 |
| VLAN 10 | Fa0/9 - Fa0/16 |
| VLAN 20 | Fa0/17 - Fa0/24 |

**Kết luận:** Có **3 broadcast domains**, tương ứng với **3 VLAN: VLAN 10, VLAN 20, VLAN 30**.

---

## 7. Kiểm Tra Và Bằng Chứng

### Kiểm tra VLAN trên switch

```text
show vlan brief
```

Kết quả mong muốn:

```text
VLAN    Name       Status    Ports
----    --------   ------    -------------------------------
10      VLAN0010   active    Fa0/9, Fa0/10, Fa0/11, Fa0/12
                              Fa0/13, Fa0/14, Fa0/15, Fa0/16
20      VLAN0020   active    Fa0/17, Fa0/18, Fa0/19, Fa0/20
                              Fa0/21, Fa0/22, Fa0/23, Fa0/24
30      VLAN0030   active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                              Fa0/5, Fa0/6, Fa0/7, Fa0/8
```

![Show VLAN Brief](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/show-vlan-brief.png)

### Kiểm tra ping trong cùng VLAN

```text
ping 192.168.1.8      ! PC0 → PC7, cùng VLAN 30
ping 192.168.1.40     ! PC8 → PC15, cùng VLAN 10
ping 192.168.1.24     ! PC16 → PC23, cùng VLAN 20
```

![Ping Same VLAN](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/ping-same-vlan.png)

### Kiểm tra traffic khác VLAN

```text
ping 192.168.1.17     ! PC0 → PC16, khác VLAN
ping 192.168.1.33     ! PC0 → PC8, khác VLAN
```

| Kiểm tra | Kết quả mong muốn | Lý do |
| --- | --- | --- |
| PC0 → PC16 | Fail | VLAN 30 không giao tiếp trực tiếp với VLAN 20 |
| PC0 → PC8 | Fail | VLAN 30 không giao tiếp trực tiếp với VLAN 10 |

![Ping Different VLAN Failed](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/ping-different-vlan-failed.png)

---

## 8. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Nghĩ rằng tất cả PC đều nhận broadcast | Nhầm switch vật lý với broadcast domain chung | Simulation mode chỉ hiện packet tới PC cùng VLAN | Ghi nhớ mỗi VLAN là một broadcast domain riêng |
| Trả lời PC0 broadcast thuộc VLAN 10 | Nhìn nhầm nhóm PC hoặc tham khảo đáp án không khớp topology | PC0 nằm trong nhóm 192.168.1.1 - 192.168.1.8/27 VLAN 30 | Đối chiếu lại nhãn VLAN trên topology |
| Ping khác VLAN bị fail nhưng tưởng lỗi IP | Chưa có inter-VLAN routing | Ping cùng VLAN thành công, khác VLAN thất bại | Đây là hành vi đúng của bài lab |
| Nhầm collision domain với broadcast domain | Chưa phân biệt phạm vi collision và broadcast | Collision domain theo port, broadcast domain theo VLAN | Đếm 24 collision domains và 3 broadcast domains |
| Quan sát quá nhiều protocol trong Simulation mode | Chưa lọc ICMP | Event List hiện nhiều gói không liên quan | Edit Filters → chỉ chọn ICMP |
| Thấy ARP/broadcast trước unicast rồi kết luận sai | Ping lần đầu có thể phát sinh ARP | Nhiều port cùng VLAN sáng trước khi unicast xảy ra | Phân biệt ARP broadcast và ICMP unicast |

---

## 9. Kết Quả Cuối

| Nội dung kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC0 ping 192.168.1.8 | Thành công vì cùng VLAN 30 |
| Broadcast từ PC0 | Chỉ lan trong VLAN 30: PC1 - PC7 |
| Broadcast từ PC8 | Chỉ lan trong VLAN 10: PC9 - PC15 |
| Broadcast từ PC16 | Chỉ lan trong VLAN 20: PC17 - PC23 |
| Frame VLAN 10 → VLAN 30 | Bị drop nếu không có inter-VLAN routing |
| Unicast port 11 → port 13 | Port 11 và port 13 sáng |
| Unicast port 2 → port 23 | Bị drop vì khác VLAN |
| Collision domain | 24 collision domains, mỗi switch port là một collision domain |
| Broadcast domain | 3 broadcast domains: VLAN 10, VLAN 20, VLAN 30 |

Checklist ảnh minh chứng cần chèn:

- [ ] `topology.png` — topology tổng thể
- [ ] `instructions.png` — yêu cầu bài lab
- [ ] `ping-pc0-pc7.png` — ping PC0 đến PC7 thành công
- [ ] `simulation-icmp-filter.png` — bộ lọc ICMP trong Simulation mode
- [ ] `create-pdu-pc0.png` — cấu hình Complex PDU từ PC0
- [ ] `broadcast-pc0-vlan30.png` — broadcast từ PC0 chỉ đi trong VLAN 30
- [ ] `broadcast-pc8-vlan10.png` — broadcast từ PC8 chỉ đi trong VLAN 10
- [ ] `broadcast-pc16-vlan20.png` — broadcast từ PC16 chỉ đi trong VLAN 20
- [ ] `show-vlan-brief.png` — bảng VLAN trên switch
- [ ] `final.png` — kết quả hoàn thành cuối bài

![Final Result](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-01/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><span></span></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 2 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
      <li style="margin: 0.5rem 0;"><strong>→ Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast (Đang đọc)</strong></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/">Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/">Lab 3: 3.3.12 Packet Tracer - VLAN Configuration</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/">Lab 4: 3.4.5 Packet Tracer - Configure Trunks</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/">Lab 5: 3.5.5 Packet Tracer - Configure DTP</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/">Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking</a></li>
    </ul>
  </details>
</div>

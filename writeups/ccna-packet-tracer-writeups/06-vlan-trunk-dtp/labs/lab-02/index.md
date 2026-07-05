---
layout: page-toc
title: "CCNA 06.02 - 3.2.8 Packet Tracer - Investigate a VLAN Implementation"
permalink: /writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-02/
toc: true
---

[← Quay lại danh sách VLAN, Trunk Và DTP](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/)

| Field | Value |
| --- | --- |
| Dạng lab | VLAN, Trunk Và DTP |
| File lab | `3.2.8 Packet Tracer - Investigate a VLAN Implementation.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Hoàn thành quan sát broadcast traffic khi có VLAN và khi xóa VLAN |

> **Ghi chú:** Bài này không yêu cầu cấu hình VLAN mới. Mục tiêu chính là quan sát cách ARP broadcast đi qua switch khi VLAN đã được cấu hình sẵn, sau đó xóa cấu hình switch để so sánh với mạng không chia VLAN.

---

## 1. Mục Tiêu Bài Lab

- Quan sát ARP broadcast khi các switch đã chia VLAN
- Kiểm tra vì sao PC khác VLAN không nhận được broadcast
- Kiểm tra vì sao PC cùng VLAN nhưng khác switch vẫn nhận được broadcast
- Xóa startup configuration và VLAN database trên S1, S2, S3
- So sánh broadcast traffic trước và sau khi không còn VLAN
- Trả lời các câu hỏi reflection về collision domain và broadcast domain

![Topology Investigate VLAN Implementation](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/topology.png)

![Instructions Investigate VLAN Implementation](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/instructions.png)

---

## 2. Bảng Địa Chỉ IP

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- | --- |
| S1 | VLAN 99 | 172.17.99.31 | 255.255.255.0 | N/A |
| S2 | VLAN 99 | 172.17.99.32 | 255.255.255.0 | N/A |
| S3 | VLAN 99 | 172.17.99.33 | 255.255.255.0 | N/A |
| PC1 | NIC | 172.17.10.21 | 255.255.255.0 | 172.17.10.1 |
| PC2 | NIC | 172.17.20.22 | 255.255.255.0 | 172.17.20.1 |
| PC3 | NIC | 172.17.30.23 | 255.255.255.0 | 172.17.30.1 |
| PC4 | NIC | 172.17.10.24 | 255.255.255.0 | 172.17.10.1 |
| PC5 | NIC | 172.17.20.25 | 255.255.255.0 | 172.17.20.1 |
| PC6 | NIC | 172.17.30.26 | 255.255.255.0 | 172.17.30.1 |
| PC7 | NIC | 172.17.10.27 | 255.255.255.0 | 172.17.10.1 |
| PC8 | NIC | 172.17.20.28 | 255.255.255.0 | 172.17.20.1 |
| PC9 | NIC | 172.17.30.29 | 255.255.255.0 | 172.17.30.1 |

> **Lưu ý:** Default gateway của các PC đã được điền theo từng subnet, nhưng bài lab này không có router hoặc multilayer switch để định tuyến giữa các VLAN. Vì vậy PC khác VLAN không thể giao tiếp trực tiếp với nhau.

---

## 3. Topology Overview

| Nhóm | Thiết bị | VLAN/Subnet | Nhận xét |
| --- | --- | --- | --- |
| Management | S1, S2, S3 | VLAN 99 / 172.17.99.0/24 | Dùng làm VLAN quản trị switch |
| Faculty/Staff | PC1, PC4, PC7 | VLAN 10 / 172.17.10.0/24 | Broadcast trong VLAN 10 chỉ đi đến các PC thuộc VLAN 10 |
| Students | PC2, PC5, PC8 | VLAN 20 / 172.17.20.0/24 | Broadcast trong VLAN 20 không đi sang VLAN 10 hoặc VLAN 30 |
| Guest | PC3, PC6, PC9 | VLAN 30 / 172.17.30.0/24 | Broadcast trong VLAN 30 chỉ đi trong nhóm VLAN 30 |
| Trunk links | Kết nối giữa S1, S2, S3 | VLAN 10, 20, 30, 99 | Cho phép VLAN đi qua nhiều switch |

> **Điểm dễ sai:** VLAN là broadcast domain logic. Hai PC có thể cắm ở hai switch khác nhau nhưng nếu cùng VLAN thì vẫn nhận broadcast của nhau thông qua trunk link.

---

## 4. Part 1: Observe Broadcast Traffic in a VLAN Implementation

### Step 1: Ping từ PC1 đến PC6

| Thao tác | Giá trị |
| --- | --- |
| Mode | Simulation |
| Công cụ | Add Simple PDU |
| Source | PC1 |
| Destination | PC6 |
| Gói cần quan sát | ARP, ICMP |

![PC1 to PC6 Simple PDU](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/pc1-to-pc6-pdu.png)

| Câu hỏi | Trả lời |
| --- | --- |
| Were the pings successful? Explain. | Không thành công. PC1 thuộc VLAN 10, PC6 thuộc VLAN 30. Broadcast/ARP của PC1 bị giới hạn trong VLAN 10 nên PC6 không nhận được ARP request. Không có ARP reply nên ping thất bại. |
| Look at the Simulation Panel, where did S3 send the packet after receiving it? | S3 chỉ gửi ARP request ra cổng nối đến PC4, thường là `F0/11`, vì PC4 cùng VLAN 10 với PC1. |

![Simulation PC1 to PC6 Event List](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/simulation-pc1-to-pc6.png)

> **Lưu ý:** Switch không flood broadcast sang tất cả VLAN. Switch chỉ flood broadcast ra các port thuộc cùng VLAN với frame nhận vào.

---

### Step 2: Ping từ PC1 đến PC4

| Thao tác | Giá trị |
| --- | --- |
| Scenario | New scenario |
| Mode | Simulation |
| Công cụ | Add Simple PDU |
| Source | PC1 |
| Destination | PC4 |
| Gói cần quan sát | ARP, ICMP |

![PC1 to PC4 Simple PDU](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/pc1-to-pc4-pdu.png)

| Câu hỏi | Trả lời |
| --- | --- |
| Were the pings successful? Explain. | Thành công. PC1 và PC4 đều thuộc VLAN 10, cùng subnet 172.17.10.0/24. ARP request của PC1 được flood trong VLAN 10, PC4 nhận được và gửi ARP reply lại cho PC1. |
| When the packet reached S1, why does it also forward the packet to PC7? | Vì PC7 cũng thuộc VLAN 10. Khi S1 nhận ARP broadcast trong VLAN 10, S1 flood frame ra các port khác thuộc VLAN 10, bao gồm port nối đến PC7. |

![Simulation PC1 to PC4 Event List](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/simulation-pc1-to-pc4.png)

---

## 5. Part 2: Observe Broadcast Traffic without VLANs

### Step 1: Xóa startup configuration và VLAN database trên S1, S2, S3

Thực hiện trên từng switch: **S1**, **S2**, **S3**.

```text
enable
erase startup-config

delete vlan.dat

reload
```

Khi switch hỏi xác nhận, nhấn `Enter` hoặc nhập `y` tùy thông báo trong Packet Tracer.

| Câu hỏi | Trả lời |
| --- | --- |
| What command is used to delete the startup configuration of the switches? | `erase startup-config` |
| Where is the VLAN file stored in the switches? | VLAN database được lưu trong flash, file thường là `vlan.dat`. |
| What command deletes the VLAN file stored in the switches? | `delete vlan.dat` hoặc `delete flash:vlan.dat` |

![Clear Switch Configuration](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/clear-switch-config.png)

> **Lưu ý:** Nếu chỉ dùng `erase startup-config` mà không xóa `vlan.dat`, các VLAN cũ vẫn có thể còn trong switch sau khi reload.

---

### Step 2: Reload switch và kiểm tra VLAN mặc định

Sau khi reload, đợi tất cả link chuyển sang màu xanh. Có thể nhấn **Fast Forward Time** để rút ngắn thời gian chờ.

```text
show vlan brief
```

Kết quả mong muốn sau khi xóa VLAN database:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

![Show VLAN Brief After Reload](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/show-vlan-after-reload.png)

---

### Step 3: Quan sát ARP broadcast khi không còn VLAN

| Thao tác | Giá trị |
| --- | --- |
| Mode | Simulation |
| Scenario | Scenario 0 |
| Nút dùng | Capture/Forward |
| Gói cần quan sát | ARP, ICMP |

![Broadcast Without VLANs](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/broadcast-without-vlans.png)

| Trạng thái | Nhận xét |
| --- | --- |
| Trước khi xóa VLAN | ARP broadcast chỉ đi trong VLAN của source |
| Sau khi xóa VLAN | Tất cả port trở về VLAN 1, switch flood ARP broadcast ra mọi port khác port nhận vào |
| Hiệu quả mạng | Broadcast lan rộng hơn, dễ gây nhiều traffic không cần thiết |
| Ý nghĩa của VLAN | Giảm broadcast domain, chia nhỏ mạng logic, tăng hiệu quả và bảo mật lớp 2 |

> **Lưu ý:** Không còn VLAN không đồng nghĩa là mọi PC khác subnet sẽ ping được nhau. Muốn các subnet khác nhau giao tiếp cần thiết bị định tuyến Layer 3.

---

## 6. Reflection Questions

### Câu 1: If a PC in VLAN 10 sends a broadcast message, which devices receive it?

| VLAN | Thiết bị nhận broadcast |
| --- | --- |
| VLAN 10 | Các thiết bị còn lại trong VLAN 10: PC1, PC4, PC7 |

> Nếu PC1 là thiết bị gửi, thiết bị nhận thực tế là PC4 và PC7. Khi xét theo thành viên broadcast domain, VLAN 10 gồm PC1, PC4, PC7.

---

### Câu 2: If a PC in VLAN 20 sends a broadcast message, which devices receive it?

| VLAN | Thiết bị nhận broadcast |
| --- | --- |
| VLAN 20 | Các thiết bị thuộc VLAN 20: PC2, PC5, PC8 |

---

### Câu 3: If a PC in VLAN 30 sends a broadcast message, which devices receive it?

| VLAN | Thiết bị nhận broadcast |
| --- | --- |
| VLAN 30 | Các thiết bị thuộc VLAN 30: PC3, PC6, PC9 |

---

### Câu 4: What happens to a frame sent from a PC in VLAN 10 to a PC in VLAN 30?

Frame không được chuyển trực tiếp từ VLAN 10 sang VLAN 30 ở Layer 2. Nếu không có router hoặc multilayer switch làm inter-VLAN routing, quá trình giao tiếp sẽ thất bại.

---

### Câu 5: In terms of ports, what are the collision domains on the switch?

Mỗi port của switch là một collision domain riêng.

| Thành phần | Collision domain |
| --- | --- |
| Port nối PC | Mỗi port nối PC là một collision domain riêng |
| Port trunk giữa switch | Mỗi trunk link cũng là một collision domain riêng |
| Toàn bộ switch | Không dùng chung một collision domain như hub |

---

### Câu 6: In terms of ports, what are the broadcast domains on the switch?

| Trạng thái | Broadcast domain |
| --- | --- |
| Khi có VLAN | Mỗi VLAN là một broadcast domain riêng: VLAN 10, VLAN 20, VLAN 30, VLAN 99 |
| Khi không có VLAN sau reload | Tất cả port mặc định thuộc VLAN 1, gần như chỉ còn một broadcast domain Layer 2 |

---

## 7. Lỗi Thường Gặp

| Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
| --- | --- | --- | --- |
| Nghĩ PC1 ping PC6 phải thành công vì cùng switch network | PC1 ở VLAN 10, PC6 ở VLAN 30 | Simulation thấy ARP không đi đến PC6 | Nhớ rằng VLAN chặn broadcast domain |
| Không thấy gói ARP trong Simulation | Chưa chọn đúng filter | Event List không hiện ARP/ICMP | Edit Filters, bật ARP và ICMP |
| Sau khi `erase startup-config`, VLAN vẫn còn | Chưa xóa `vlan.dat` trong flash | `show vlan brief` vẫn thấy VLAN 10, 20, 30, 99 | Dùng `delete vlan.dat`, sau đó `reload` |
| Ping khác subnet vẫn không thành công sau khi xóa VLAN | Không có router/default gateway thật để định tuyến | ARP gateway không có reply | Cần inter-VLAN routing nếu muốn ping khác subnet |
| Nhầm broadcast domain với collision domain | Broadcast domain theo VLAN, collision domain theo switch port | Trả lời reflection bị sai | Ghi nhớ: VLAN = broadcast domain, port switch = collision domain |
| PC cùng VLAN nhưng khác switch vẫn nhận broadcast | Quên vai trò trunk link | Simulation thấy broadcast đi qua S1/S2/S3 | Trunk link mang VLAN giữa nhiều switch |

---

## 8. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn |
| --- | --- |
| PC1 → PC6 khi có VLAN | Ping thất bại vì khác VLAN |
| S3 nhận ARP từ PC1 | S3 chỉ gửi tiếp đến PC4 trong VLAN 10 |
| PC1 → PC4 khi có VLAN | Ping thành công vì cùng VLAN 10 |
| S1 nhận ARP VLAN 10 | S1 flood đến PC7 vì PC7 cùng VLAN 10 |
| Xóa startup-config | Hoàn thành trên S1, S2, S3 |
| Xóa VLAN database | Hoàn thành bằng `delete vlan.dat` |
| Sau reload | Các port trở về VLAN 1 |
| Broadcast sau khi không còn VLAN | ARP flood ra toàn mạng Layer 2 |

Ảnh minh chứng cần chèn:

- [ ] `topology.png`
- [ ] `instructions.png`
- [ ] `pc1-to-pc6-pdu.png`
- [ ] `simulation-pc1-to-pc6.png`
- [ ] `pc1-to-pc4-pdu.png`
- [ ] `simulation-pc1-to-pc4.png`
- [ ] `clear-switch-config.png`
- [ ] `show-vlan-after-reload.png`
- [ ] `broadcast-without-vlans.png`
- [ ] `final.png`

![Final Result](/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/labs/lab-02/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 6 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-01/">Lab 1: 3.1.4 Packet Tracer - Who Hears the Broadcast</a></li>
      <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 3.2.8 Packet Tracer - Investigate a VLAN Implementation (Đang đọc)</strong></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-03/">Lab 3: 3.3.12 Packet Tracer - VLAN Configuration</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-04/">Lab 4: 3.4.5 Packet Tracer - Configure Trunks</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-05/">Lab 5: 3.5.5 Packet Tracer - Configure DTP</a></li>
      <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/lab-06/">Lab 6: 3.6.1 Packet Tracer - Implement VLANs and Trunking</a></li>
    </ul>
  </details>
</div>

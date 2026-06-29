---
layout: page-toc
title: "CCNA 03.02 - 9.1.3 Packet Tracer - Identify MAC and IP Addresses"
permalink: /writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-02/
toc: true
---

[← Quay lại danh sách ARP, ICMP, TCP Và UDP](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/)

| Field | Value |
| --- | --- |
| Dạng lab | ARP, ICMP, TCP Và UDP |
| File lab | `9.1.3 Packet Tracer - Identify MAC and IP Addresses.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Quan sát PDU trong Simulation Mode, nhận diện MAC/IP khi ping nội bộ LAN và ping sang mạng khác |

> **Ghi chú:** Bài này không yêu cầu cấu hình thiết bị. Trọng tâm là dùng Simulation Mode để theo dõi PDU, so sánh địa chỉ MAC ở từng chặng và xác định lúc nào địa chỉ MAC thay đổi khi gói tin đi qua router.

## 1. Mục Tiêu Bài Lab

- Dùng Simulation Mode để quan sát PDU khi ping trong cùng mạng LAN.
- Ghi lại địa chỉ MAC nguồn, MAC đích, IPv4 nguồn và IPv4 đích ở từng thiết bị trung gian.
- So sánh cách xử lý PDU của switch, hub, access point và router.
- Quan sát sự thay đổi địa chỉ MAC khi gói tin đi từ mạng `172.16.31.0` sang mạng `10.10.10.0`.
- Trả lời các câu hỏi reflection dựa trên dữ liệu bắt được trong Packet Tracer.

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-02/topology.png)

![Topology lab 02](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-02/topology1.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Mạng `172.16.31.0` | Các PC `172.16.31.2`, `172.16.31.3`, `172.16.31.4`, `172.16.31.5`, Switch1, Hub | Dùng để kiểm tra ping nội bộ LAN và quan sát hub/switch xử lý PDU |
| Mạng `10.10.10.0` | Laptop `10.10.10.2`, Laptop `10.10.10.3`, Access Point, Switch0 | Dùng để kiểm tra truyền thông từ mạng 172 sang mạng 10 qua router |
| Thiết bị định tuyến | Router | Là điểm thay đổi địa chỉ MAC khi gói tin đi sang mạng khác |
| Thiết bị Layer 1/2 | Hub, Switch, Access Point | Không thay đổi địa chỉ IP nguồn/đích của gói tin |

> **Lưu ý:** IP nguồn và IP đích giữ nguyên trong suốt chiều đi của gói ICMP request. MAC nguồn và MAC đích chỉ có ý nghĩa trên từng đoạn mạng cục bộ nên sẽ thay đổi khi đi qua router.

## 3. Bảng Thiết Bị Quan Sát

| Thiết bị | Vai trò | Mạng liên quan |
| --- | --- | --- |
| `172.16.31.5` | PC gửi ping trong các bài kiểm tra chính | `172.16.31.0/24` |
| `172.16.31.2` | PC nhận ping nội bộ LAN | `172.16.31.0/24` |
| `172.16.31.3` | PC gửi ping bổ sung | `172.16.31.0/24` |
| `172.16.31.4` | PC nhận ping bổ sung | `172.16.31.0/24` |
| `10.10.10.2` | Thiết bị nhận ping ở mạng khác | `10.10.10.0/24` |
| Router | Default gateway giữa hai mạng | `172.16.31.0/24` và `10.10.10.0/24` |
| Hub | Thiết bị lặp tín hiệu trong LAN | `172.16.31.0/24` |
| Access Point | Thiết bị chuyển tiếp sang môi trường wireless | `10.10.10.0/24` |

## 4. Part 1 - Gather PDU Information for Local Network Communication

### Step 1 - Ping từ `172.16.31.5` đến `172.16.31.2`

```text
PC> ping 172.16.31.2
```

![Ping local 172.16.31.5 to 172.16.31.2](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-02/ping-local-172-16-31-5-to-172-16-31-2.png)

| At Device | Dest. MAC | Src MAC | Src IPv4 | Dest IPv4 |
| --- | --- | --- | --- | --- |
| `172.16.31.5` | `000C:85CC:1DA7` | `00D0:D311:C788` | `172.16.31.5` | `172.16.31.2` |
| `Switch1` | `000C:85CC:1DA7` | `00D0:D311:C788` | `N/A` | `N/A` |
| `Hub` | `N/A` | `N/A` | `N/A` | `N/A` |
| `172.16.31.2` | `00D0:D311:C788` | `000C:85CC:1DA7` | `172.16.31.2` | `172.16.31.5` |

> **Lưu ý:** Khi ping trong cùng LAN, MAC đích là MAC của chính thiết bị nhận. Gói tin không cần đi qua router.


### Step 2 - Ping bổ sung trong cùng LAN

```text
PC> ping 172.16.31.2
! Thực hiện từ PC 172.16.31.3

PC> ping 172.16.31.4
! Thực hiện từ PC 172.16.31.5
```

| Bài kiểm tra | MAC đích mong đợi | IP nguồn/đích | Nhận xét |
| --- | --- | --- | --- |
| `172.16.31.3` ping `172.16.31.2` | MAC của `172.16.31.2` | `172.16.31.3` → `172.16.31.2` | Giao tiếp nội bộ LAN |
| `172.16.31.5` ping `172.16.31.4` | MAC của `172.16.31.4` | `172.16.31.5` → `172.16.31.4` | Không đổi IP khi đi qua switch/hub |


## 5. Part 2 - Gather PDU Information for Remote Network Communication

### Step 1 - Ping từ `172.16.31.5` đến `10.10.10.2`

```text
PC> ping 10.10.10.2
```

| At Device | Dest. MAC | Src MAC | Src IPv4 | Dest IPv4 |
| --- | --- | --- | --- | --- |
| `172.16.31.5` | `00D0:BA8E:741A` | `00D0:D311:C788` | `172.16.31.5` | `10.10.10.2` |
| `Switch1` | `00D0:BA8E:741A` | `00D0:D311:C788` | `N/A` | `N/A` |
| `Router` | `0060:2F84:4AB6` | `00D0:588C:2401` | `172.16.31.5` | `10.10.10.2` |
| `Switch0` | `0060:2F84:4AB6` | `00D0:588C:2401` | `N/A` | `N/A` |
| `Access Point` | `N/A` | `N/A` | `N/A` | `N/A` |
| `10.10.10.2` | `00D0:588C:2401` | `0060:2F84:4AB6` | `10.10.10.2` | `172.16.31.5` |

> **Lưu ý:** Ở bước đầu, MAC đích `00D0:BA8E:741A` là MAC của router ở phía mạng `172.16.31.0`. Vì `10.10.10.2` nằm khác mạng, PC gửi frame đến default gateway thay vì gửi trực tiếp đến MAC của `10.10.10.2`.

![PDU remote details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-02/pdu-remote-details.png)

![PDU remote details](/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/labs/lab-02/pdu-remote-details1.png)


### Câu hỏi trong Part 2

| Câu hỏi | Trả lời |
| --- | --- |
| MAC đích `00D0:BA8E:741A` thuộc thiết bị nào? | Router, cụ thể là interface của router nối với mạng `172.16.31.0/24`. |
| Khi gói tin đi qua router, địa chỉ MAC có thay đổi không? | Có. Router tháo frame cũ và đóng gói lại frame mới cho mạng kế tiếp. |
| IP nguồn/đích có đổi khi đi từ `172.16.31.5` sang `10.10.10.2` không? | Không. Trong chiều ICMP request, IP nguồn vẫn là `172.16.31.5`, IP đích vẫn là `10.10.10.2`. |

## 6. Reflection Questions

| # | Câu hỏi | Trả lời ngắn |
| --- | --- | --- |
| 1 | Có nhiều loại cable/media khác nhau không? | Có. Topology có kết nối wired và wireless. |
| 2 | Cable có làm thay đổi cách xử lý PDU không? | Không làm đổi thông tin Layer 3; thiết bị trung gian mới quyết định cách xử lý frame. |
| 3 | Hub có làm mất thông tin nhận được không? | Không. Hub lặp lại tín hiệu, không đọc MAC/IP. |
| 4 | Hub làm gì với MAC và IP? | Không xử lý MAC/IP; chỉ hoạt động như thiết bị lặp tín hiệu. |
| 5 | Access Point có thay đổi thông tin được đưa tới nó không? | Không thay đổi IP; chủ yếu chuyển tiếp qua môi trường wireless. |
| 6 | Có MAC hoặc IP nào bị mất khi truyền wireless không? | Không. PDU vẫn giữ thông tin cần thiết để đến đích. |
| 7 | Layer OSI cao nhất mà Hub và Access Point dùng là gì? | Trong quan sát bài này, Hub/AP chủ yếu thể hiện ở Layer 1 khi chuyển tiếp tín hiệu. |
| 8 | Hub hoặc Access Point có nhân bản PDU bị từ chối bằng dấu X đỏ không? | Có thể thấy PDU bị nhân bản ra thiết bị không phải đích và bị loại bỏ. |
| 9 | Trong PDU Details, MAC nào xuất hiện trước? | Destination MAC xuất hiện trước Source MAC. |
| 10 | Vì sao MAC xuất hiện theo thứ tự đó? | Frame Ethernet đặt địa chỉ đích trước để thiết bị nhận nhanh chóng xác định frame có dành cho mình không. |
| 11 | Có pattern gì ở MAC address không? | Trong cùng LAN, MAC nguồn/đích là của hai host; qua router, MAC đổi theo từng đoạn mạng. |
| 12 | Switch có nhân bản PDU bị từ chối bằng dấu X đỏ không? | Có trong trường hợp broadcast/unknown traffic; với unicast đã học MAC thì switch chỉ chuyển đúng cổng. |
| 13 | MAC address đột ngột thay đổi ở đâu? | Tại router, khi gói tin đi giữa mạng `172.16.31.0` và `10.10.10.0`. |
| 14 | Thiết bị nào dùng MAC bắt đầu bằng `00D0:BA`? | Interface router ở phía mạng `172.16.31.0/24`. |
| 15 | Các MAC khác thuộc thiết bị nào? | `00D0:D311:C788`: PC `172.16.31.5`; `000C:85CC:1DA7`: PC `172.16.31.2`; `00D0:588C:2401`: router phía mạng `10.10.10.0`; `0060:2F84:4AB6`: thiết bị `10.10.10.2`. |
| 16 | IPv4 nguồn/đích có thay đổi trong PDU không? | Không trong cùng chiều truyền. Router chỉ thay đổi frame Layer 2, không đổi IP nguồn/đích của ICMP request. |
| 17 | Khi xem ICMP reply/pong, IPv4 nguồn và đích có đảo chiều không? | Có. Reply sẽ đổi chiều: nguồn là thiết bị trả lời, đích là thiết bị ban đầu gửi ping. |
| 18 | Pattern IPv4 trong mô phỏng là gì? | Có hai mạng chính: `172.16.31.0/24` và `10.10.10.0/24`, được nối với nhau qua router. |
| 19 | Vì sao các cổng router phải thuộc các IP network khác nhau? | Mỗi cổng router đại diện cho một mạng Layer 3 riêng; router cần các mạng khác nhau để định tuyến giữa chúng. |
| 20 | Nếu dùng IPv6 thay IPv4 thì khác gì? | Không dùng ARP; IPv6 dùng Neighbor Discovery/ICMPv6. MAC vẫn là địa chỉ Layer 2 theo từng link, còn IPv6 nguồn/đích vẫn đi end-to-end. |

## 7. Kiểm Tra Và Bằng Chứng

| Kiểm tra | Kết quả mong muốn | Ảnh/log bằng chứng |
| --- | --- | --- |
| Ping `172.16.31.5` → `172.16.31.2` | Thành công trong cùng LAN | `ping-local-172-16-31-5-to-172-16-31-2.png` |
| PDU tại PC nguồn | MAC đích là MAC của PC đích nếu cùng LAN | `pdu-local-details.png` |
| Ping `172.16.31.5` → `10.10.10.2` | Thành công qua router | `ping-remote-172-to-10.png` |
| PDU tại PC nguồn khi ping remote | MAC đích là MAC của default gateway | `pdu-remote-source.png` |
| PDU tại router | MAC nguồn/đích được thay đổi theo mạng kế tiếp | `pdu-at-router.png` |
| ICMP reply | IPv4 nguồn/đích đảo chiều | `icmp-reply-details.png` |

## 8. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không thấy PDU xuất hiện | Đang ở Realtime Mode hoặc chưa chạy lệnh ping sau khi chuyển Simulation Mode | Chuyển sang Simulation Mode rồi ping lại |
| Event list có quá nhiều gói | Chưa lọc đúng loại event | Dùng Event List Filters, chỉ chọn ICMP/ARP nếu cần |
| Không đọc được MAC/IP ở Hub hoặc Access Point | Hub/AP không xử lý đầy đủ Layer 2/3 như router hoặc host trong cửa sổ PDU | Ghi `N/A` nếu Packet Tracer không hiển thị thông tin |
| Nhầm MAC của host đích với MAC của gateway | Chưa phân biệt local network và remote network | Cùng LAN dùng MAC host đích; khác mạng dùng MAC default gateway |
| Nghĩ IP đổi khi qua router | Nhầm giữa Layer 2 và Layer 3 | Router đổi địa chỉ MAC theo từng link, IP nguồn/đích giữ nguyên trong cùng chiều truyền |

## 9. Kết Quả Cuối

| Nội dung | Kết quả |
| --- | --- |
| Quan sát ping nội bộ LAN | Hoàn thành |
| Quan sát ping sang mạng khác | Hoàn thành |
| Xác định điểm thay đổi MAC | Router |
| Xác định IP nguồn/đích | Giữ nguyên trong chiều request, đảo chiều trong reply |
| Trả lời reflection questions | Hoàn thành |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 5 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-01/">Lab 1: 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 9.1.3 Packet Tracer - Identify MAC and IP Addresses (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-03/">Lab 3: 9.2.9 Packet Tracer - Examine the ARP Table</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-04/">Lab 4: 9.3.4 Packet Tracer - IPv6 Neighbor Discovery</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/lab-05/">Lab 5: 14.8.1 Packet Tracer - TCP and UDP Communications</a></li>
    </ul>
  </details>
</div>

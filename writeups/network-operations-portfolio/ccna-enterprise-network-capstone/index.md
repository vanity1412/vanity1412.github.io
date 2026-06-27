---
layout: page-toc
title: "CCNA Enterprise Network Capstone Lab"
permalink: /writeups/network-operations-portfolio/ccna-enterprise-network-capstone/
toc: true
---

## 1. Overview

Lab này mô phỏng một hệ thống mạng doanh nghiệp nhỏ/trung bình với nhiều VLAN, định tuyến nội bộ, kết nối edge ra Internet giả lập, chính sách truy cập cơ bản và dự phòng gateway. Mục tiêu là biến kiến thức CCNA thành một project có thể trình bày như một mini network operation project.

## 2. Lab Objectives

- Thiết kế topology theo hướng access, distribution/core và edge.
- Cấu hình VLAN, trunk, inter-VLAN routing, STP và EtherChannel.
- Cấu hình DHCP, OSPF, NAT/PAT, ACL và HSRP.
- Kiểm chứng bằng lệnh `show`, `ping`, `traceroute`.
- Ghi lại lỗi, cách troubleshoot và bài học vận hành.

## 3. Network Topology

Chèn topology sau khi hoàn thành lab.

```text
Place topology image here:
/writeups/network-operations-portfolio/ccna-enterprise-network-capstone/topology.png
```

## 4. IP Addressing & VLAN Plan

| VLAN | Name | Subnet | Gateway | Purpose |
| --- | --- | --- | --- | --- |
| 10 | USERS | 192.168.10.0/24 | 192.168.10.1 | User devices |
| 20 | SERVERS | 192.168.20.0/24 | 192.168.20.1 | Internal services |
| 30 | MGMT | 192.168.30.0/24 | 192.168.30.1 | Network management |
| 99 | NATIVE | N/A | N/A | Native/unused VLAN |

## 5. Switching Design

| Item | Design Decision | Verification |
| --- | --- | --- |
| VLAN | Separate users, servers and management | `show vlan brief` |
| Trunk | Allow required VLANs only | `show interfaces trunk` |
| STP | Define root primary/secondary | `show spanning-tree root` |
| EtherChannel | Bundle uplinks between switches | `show etherchannel summary` |

## 6. Routing Design

| Item | Design Decision | Verification |
| --- | --- | --- |
| Inter-VLAN | Layer 3 switch or router-on-a-stick | `show ip interface brief` |
| OSPF | Single-area OSPF for internal routing | `show ip ospf neighbor` |
| Default route | Edge router points to ISP/Internet cloud | `show ip route` |

## 7. NAT, ACL & Edge Policy

| Policy | Goal | Verification |
| --- | --- | --- |
| NAT/PAT | Internal VLANs reach outside network | `show ip nat translations` |
| ACL | Limit traffic between user/server/management zones | `show access-lists` |
| Edge route | LAN can reach simulated Internet | `traceroute` |

## 8. High Availability with HSRP

| Item | Goal | Verification |
| --- | --- | --- |
| Virtual gateway | Clients use stable default gateway | `show standby brief` |
| Active/standby | Gateway failover between L3 devices | failover ping test |

## 9. Verification Checklist

| Test | Expected Result | Evidence |
| --- | --- | --- |
| PC in VLAN 10 gets DHCP | Receives IP/gateway/DNS | Screenshot or CLI output |
| VLAN 10 to VLAN 20 | Allowed/denied based on ACL policy | `ping`, `traceroute` |
| OSPF adjacency | FULL state | `show ip ospf neighbor` |
| NAT translation | Inside local translated to outside interface | `show ip nat translations` |
| HSRP failover | Connectivity recovers after active gateway failure | continuous ping |

## 10. Operations Mindset

Trong mạng thật, cấu hình chỉ là một phần. Phần quan trọng hơn là biết kiểm chứng thay đổi, ghi bằng chứng trước/sau, hiểu phạm vi ảnh hưởng và có phương án rollback nếu thay đổi làm gián đoạn dịch vụ.

## 11. Lessons Learned

### Technical Lessons

- Ghi lại các lỗi cấu hình thật đã gặp trong lúc làm lab.
- Gắn mỗi lỗi với command phát hiện và command xác minh sau khi sửa.

### Operations / SLA Impact

- Lỗi routing có thể gây blackhole hoặc asymmetric path.
- Lỗi VLAN/trunk có thể làm người dùng mất kết nối theo từng segment.
- Lỗi NAT/ACL ở edge có thể làm toàn bộ LAN không truy cập được dịch vụ bên ngoài.

## 12. Future Improvements

- Thêm syslog, NTP và SNMP để mô phỏng monitoring.
- Thêm automation backup config bằng Python/Netmiko.
- Thêm config diff để phát hiện thay đổi ngoài kế hoạch.
- Viết 3 case study troubleshooting dựa trên chính lab này.

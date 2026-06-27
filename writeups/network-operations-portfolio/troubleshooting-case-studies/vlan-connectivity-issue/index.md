---
layout: page-toc
title: "Troubleshooting VLAN Connectivity Issue"
permalink: /writeups/network-operations-portfolio/troubleshooting-case-studies/vlan-connectivity-issue/
toc: true
---

## 1. Problem Description

PC thuộc `VLAN 20` không ping được default gateway và không truy cập được server nội bộ. Các VLAN khác vẫn hoạt động bình thường.

## 2. Expected Behavior

- PC trong VLAN 20 nhận IP đúng subnet.
- PC ping được SVI/default gateway của VLAN 20.
- VLAN 20 đi qua trunk giữa access switch và distribution switch.

## 3. Symptoms

```txt
PC-VLAN20> ping 192.168.20.1
Request timed out.

SW1# show interfaces trunk
Vlans allowed on trunk
10,30,99
```

Triệu chứng chính:

- Chỉ VLAN 20 bị ảnh hưởng.
- Access port của PC đúng VLAN.
- Trunk uplink không allow VLAN 20.

## 4. Initial Hypothesis

| Hypothesis | Reason |
| --- | --- |
| Access port sai VLAN | PC có thể bị đặt nhầm VLAN. |
| Trunk không allow VLAN | VLAN không đi qua uplink. |
| SVI down | Gateway VLAN không hoạt động. |
| STP blocking | Port có thể bị block ở topology có loop. |
| Default gateway sai | PC gửi traffic sai gateway. |

## 5. Troubleshooting Flow

| Step | Command / Check | Observation | Decision |
| --- | --- | --- | --- |
| 1 | `show vlan brief` | PC port thuộc VLAN 20 | Access VLAN đúng |
| 2 | `show ip interface brief` | SVI VLAN 20 up/up | Gateway đang hoạt động |
| 3 | `show interfaces trunk` | VLAN 20 không nằm trong allowed list | Tập trung sửa trunk |
| 4 | `show spanning-tree vlan 20` | Không thấy VLAN 20 qua trunk | Xác nhận VLAN bị chặn ở trunk |

## 6. Root Cause

Root cause: trunk uplink giữa `SW1` và distribution switch chỉ allow VLAN `10,30,99`, thiếu VLAN `20`.

Ví dụ lỗi:

```txt
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,30,99
```

## 7. Fix Implementation

Thêm VLAN 20 vào allowed VLAN list trên trunk.

```txt
conf t
interface GigabitEthernet0/1
 switchport trunk allowed vlan add 20
end
```

## 8. Verification

```txt
SW1# show interfaces trunk
Vlans allowed on trunk
10,20,30,99

PC-VLAN20> ping 192.168.20.1
Success rate is 100 percent
```

| Test | Expected | Result |
| --- | --- | --- |
| `show interfaces trunk` | VLAN 20 allowed | Pass |
| Ping gateway | Success | Pass |
| Ping internal server | Depends on ACL policy | Pass |

## 9. Technical Lesson Learned

Khi một VLAN riêng lẻ mất kết nối, không nên kiểm tra routing đầu tiên. Nên đi từ access port, VLAN database, trunk allowed list, STP state, SVI state rồi mới lên Layer 3. Lỗi trunk allowed VLAN là lỗi phổ biến trong campus switching.

## 10. Real Operations / SLA Impact

Trong vận hành thực tế, lỗi trunk thiếu VLAN thường gây sự cố theo phạm vi phòng ban hoặc dịch vụ cụ thể. Người dùng trong VLAN bị ảnh hưởng có thể mất DHCP, mất gateway, mất truy cập server. Nếu VLAN đó phục vụ hệ thống quan trọng như management hoặc server farm, lỗi nhỏ ở trunk có thể làm gián đoạn monitoring, backup hoặc vận hành từ xa.

## 11. Prevention

- Dùng change checklist khi thêm VLAN mới: VLAN database, access port, trunk allowed list, SVI, DHCP scope, ACL.
- Ghi lại output trước/sau của `show interfaces trunk`.
- Tránh cấu hình allowed VLAN thủ công không có tài liệu IP/VLAN plan.
- Monitoring nên cảnh báo khi SVI down hoặc số lượng MAC trong VLAN giảm bất thường.

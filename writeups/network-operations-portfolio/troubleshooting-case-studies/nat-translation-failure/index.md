---
layout: page-toc
title: "Troubleshooting NAT Translation Failure"
permalink: /writeups/network-operations-portfolio/troubleshooting-case-studies/nat-translation-failure/
toc: true
---

## 1. Problem Description

Client trong LAN ping được default gateway nhưng không truy cập được mạng outside/Internet giả lập. Trên edge router không xuất hiện NAT translation.

## 2. Expected Traffic Flow

```text
Client VLAN -> Core/Distribution -> Edge Router NAT inside -> NAT outside -> ISP/Internet cloud
```

Kỳ vọng:

- Inside local address được translate sang outside interface.
- Router có default route ra ngoài.
- ACL NAT match đúng subnet nội bộ.

## 3. Symptoms

```txt
EDGE# show ip nat translations
<empty>

EDGE# show ip nat statistics
Total active translations: 0
```

Triệu chứng chính:

- Client ping gateway thành công.
- Client không ra được outside network.
- Không có NAT translation.
- Default route tồn tại.

## 4. Initial Hypothesis

| Hypothesis | Reason |
| --- | --- |
| Thiếu `ip nat inside/outside` | Router không biết hướng translate. |
| ACL NAT sai subnet | Traffic không match NAT rule. |
| Thiếu `overload` | PAT không hoạt động cho nhiều client. |
| Default route sai | Traffic không đi ra outside interface. |
| ACL security chặn traffic | Packet bị deny trước/sau NAT. |

## 5. Troubleshooting Steps

| Step | Command / Check | Observation | Decision |
| --- | --- | --- | --- |
| 1 | `show ip route` | Default route có tồn tại | Loại trừ thiếu default route |
| 2 | `show running-config | include ip nat` | NAT rule có cấu hình | Kiểm tra interface role và ACL |
| 3 | `show access-lists` | ACL NAT match sai subnet | Xác định root cause |
| 4 | `show ip nat statistics` | Hits không tăng | Traffic không match NAT rule |

## 6. Root Cause

Root cause: ACL dùng cho NAT chỉ match `192.168.10.0/24`, trong khi client lỗi nằm ở `192.168.20.0/24`.

Ví dụ lỗi:

```txt
access-list 1 permit 192.168.10.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

## 7. Solution

Thêm đúng subnet LAN cần NAT vào ACL hoặc dùng ACL chuẩn hóa cho toàn bộ dải nội bộ.

```txt
conf t
access-list 1 permit 192.168.20.0 0.0.0.255
end

clear ip nat translation *
```

Nếu cần gom nhiều VLAN nội bộ:

```txt
conf t
ip access-list standard NAT_INSIDE
 permit 192.168.10.0 0.0.0.255
 permit 192.168.20.0 0.0.0.255
 permit 192.168.30.0 0.0.0.255
exit
ip nat inside source list NAT_INSIDE interface GigabitEthernet0/1 overload
end
```

## 8. Verification

```txt
EDGE# show ip nat translations
Pro  Inside global       Inside local        Outside local       Outside global
icmp 203.0.113.2:1       192.168.20.10:1     198.51.100.10:1     198.51.100.10:1
```

| Test | Expected | Result |
| --- | --- | --- |
| `show access-lists` | NAT ACL hit count increases | Pass |
| `show ip nat translations` | Translation appears | Pass |
| Client ping outside | Success | Pass |

## 9. Technical Lesson Learned

NAT troubleshooting nên kiểm tra theo luồng: inside interface, outside interface, NAT ACL, NAT rule, route ra ngoài, ACL security và translation table. Nếu translation table rỗng, thường traffic chưa match NAT rule hoặc interface role bị thiếu.

## 10. Real Operations / SLA Impact

Trong mạng thật, lỗi NAT ở edge có thể làm cả một nhóm người dùng hoặc chi nhánh mất truy cập Internet/SaaS. Nếu NAT ACL bị sửa sai trong change window, sự cố có thể ảnh hưởng đến dịch vụ email, VPN, monitoring agent hoặc ứng dụng cloud. Với môi trường có SLA, cần phát hiện nhanh qua NAT hit count, syslog, synthetic ping và rollback policy.

## 11. Prevention

- Chuẩn hóa ACL NAT theo IP plan.
- Luôn lưu pre-change output: `show run | include ip nat`, `show access-lists`, `show ip route`.
- Sau change, kiểm tra hit count và NAT translation thật từ một client đại diện.
- Kết hợp automation backup/diff config để phát hiện thay đổi NAT ngoài kế hoạch.

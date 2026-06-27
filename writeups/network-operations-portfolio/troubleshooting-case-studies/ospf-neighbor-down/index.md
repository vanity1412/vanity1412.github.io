---
layout: page-toc
title: "Troubleshooting OSPF Neighbor Down"
permalink: /writeups/network-operations-portfolio/troubleshooting-case-studies/ospf-neighbor-down/
toc: true
---

## 1. Problem Description

Trong capstone lab, OSPF neighbor giữa `R1` và `R2` không lên trạng thái `FULL`. Hai router vẫn up interface vật lý, nhưng không học route OSPF từ nhau.

## 2. Expected Behavior

- `R1` và `R2` hình thành OSPF adjacency ở trạng thái `FULL`.
- Mỗi router học được route OSPF của phía còn lại.
- Traffic giữa các subnet nội bộ đi đúng next-hop.

## 3. Symptoms

```txt
R1# show ip ospf neighbor
<no neighbor>

R1# show ip route ospf
<no OSPF route>
```

Triệu chứng chính:

- Không có neighbor trong `show ip ospf neighbor`.
- Không có route OSPF trong routing table.
- Ping giữa các subnet remote thất bại.

## 4. Initial Hypothesis

| Hypothesis | Reason |
| --- | --- |
| Sai OSPF area | Neighbor phải cùng area trên cùng link. |
| Sai subnet mask/IP | Hai đầu link không cùng subnet nên không trao đổi hello. |
| Passive interface | Router không gửi OSPF hello trên interface đó. |
| Hello/dead timer mismatch | Neighbor không hình thành nếu timer lệch. |

## 5. Troubleshooting Steps

| Step | Command / Check | Observation | Decision |
| --- | --- | --- | --- |
| 1 | `show ip interface brief` | Interface up/up | Loại trừ lỗi vật lý/L1-L2 cơ bản |
| 2 | `show ip ospf interface brief` | Interface đã chạy OSPF nhưng area không khớp | Tập trung kiểm tra cấu hình OSPF |
| 3 | `show running-config | section router ospf` | R1 dùng area 0, R2 dùng area 1 trên cùng link | Xác định root cause |
| 4 | `show ip protocols` | Network statement match interface nhưng area sai | Cần sửa area cho thống nhất |

## 6. Root Cause

Root cause: hai đầu link chạy OSPF khác area.

Ví dụ lỗi:

```txt
! R1
router ospf 1
 network 10.0.12.0 0.0.0.3 area 0

! R2
router ospf 1
 network 10.0.12.0 0.0.0.3 area 1
```

## 7. Solution

Sửa area OSPF trên cùng link về thống nhất.

```txt
! R2
conf t
router ospf 1
 no network 10.0.12.0 0.0.0.3 area 1
 network 10.0.12.0 0.0.0.3 area 0
end
```

## 8. Verification

```txt
R1# show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:33    10.0.12.2       GigabitEthernet0/0

R1# show ip route ospf
O    192.168.20.0/24 [110/2] via 10.0.12.2, 00:00:12, GigabitEthernet0/0
```

| Test | Expected | Result |
| --- | --- | --- |
| `show ip ospf neighbor` | Neighbor `FULL` | Pass |
| `show ip route ospf` | Remote route appears | Pass |
| Ping remote subnet | Success | Pass |

## 9. Technical Lesson Learned

OSPF adjacency phụ thuộc vào nhiều điều kiện: cùng subnet, cùng area, timer tương thích, authentication/MTU phù hợp và interface không bị passive. Khi neighbor không lên, nên kiểm tra theo flow: physical/interface -> IP/subnet -> OSPF interface -> OSPF process -> routing table.

## 10. Real Operations / SLA Impact

Trong mạng thật, OSPF adjacency down có thể làm traffic reroute sang đường dự phòng, tăng latency hoặc mất route hoàn toàn nếu không có alternate path. Nếu route biến mất nhưng thiết bị edge vẫn nhận traffic, có thể sinh blackhole và ảnh hưởng SLA của dịch vụ khách hàng.

## 11. Prevention

- Chuẩn hóa OSPF area plan trước khi triển khai.
- Lưu pre-check và post-check cho các lệnh `show ip ospf neighbor`, `show ip route`, `ping`, `traceroute`.
- Cấu hình syslog/SNMP/telemetry để cảnh báo khi adjacency chuyển trạng thái.
- Với production, cần rollback plan nếu route không hội tụ sau change.

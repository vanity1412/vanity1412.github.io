---
layout: page-toc
title: "Network Operations Research Notes"
permalink: /writeups/network-operations-portfolio/research-notes/
toc: true
---

## Overview

Các bài research ngắn phục vụ hướng **Core IP / Transmission / Network Automation**. Mục tiêu là cho thấy mình không chỉ làm lab cấu hình, mà còn hiểu bối cảnh công nghệ vận hành mạng backbone hiện đại.

## Blog Post

- [Xu hướng Research: Core IP, Transmission & Network Automation](/posts/xu-huong-research-network-operations/) - post tổng hợp để hiển thị trên blog/homepage và dẫn về các research note chi tiết.
- [SOC vs NOC](/writeups/network-operations-portfolio/research-notes/soc-vs-noc/) - bài nền giúp phân biệt vai trò vận hành ổn định của NOC và vai trò phòng thủ/phản ứng sự cố của SOC.

## Notes

- [DWDM for IP Network Engineers](/writeups/network-operations-portfolio/research-notes/dwdm-for-ip-network-engineers/) - giải thích DWDM từ góc nhìn IP/Core Network Engineer, tập trung vào optical link, OTN, protection và troubleshooting cross-layer.
- [SNMP vs Streaming Telemetry](/writeups/network-operations-portfolio/research-notes/snmp-vs-streaming-telemetry/) - so sánh mô hình giám sát pull/push, SNMP, YANG, gNMI, telemetry pipeline và liên hệ AI/Ops.
- [Segment Routing (SR-MPLS / SRv6)](/writeups/network-operations-portfolio/research-notes/segment-routing-sr-mpls-srv6/) - phân tích SR-MPLS, SRv6, SID stack, SR Policy, TI-LFA và hướng thay thế LDP/RSVP-TE trong core transport.
- [MPLS L3VPN: VRF, RD, RT](/writeups/network-operations-portfolio/research-notes/mpls-l3vpn-vrf-rd-rt/) - giải thích kiến trúc L3VPN, VRF, Route Distinguisher, Route Target, MP-BGP VPNv4 và troubleshooting dịch vụ VPN lớp 3.

## Portfolio Value

| Note | Mentor thấy gì |
| --- | --- |
| SOC vs NOC | Hiểu bối cảnh operations: NOC giữ dịch vụ ổn định, SOC bảo vệ hệ thống, hai bên phối hợp khi sự cố vừa ảnh hưởng uptime vừa có yếu tố an ninh. |
| DWDM for IP Network Engineers | Có awareness về truyền dẫn/quang, biết phân tầng sự cố giữa IP và optical. |
| SNMP vs Streaming Telemetry | Có định hướng automation, monitoring data, AI/Big Data đúng với yêu cầu JD. |
| Segment Routing (SR-MPLS / SRv6) | Hiểu xu hướng core transport hiện đại, giảm state trong mạng lõi và thiết kế traffic engineering bằng SR Policy. |
| MPLS L3VPN: VRF, RD, RT | Nắm nền tảng dịch vụ VPN ISP, multi-tenant routing, MP-BGP và cách tách biệt khách hàng bằng VRF/RD/RT. |

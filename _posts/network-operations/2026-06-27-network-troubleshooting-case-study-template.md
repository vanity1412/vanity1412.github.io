---
title: "Network Troubleshooting"
date: 2026-06-27 00:10:00 +0700
categories: [Network Operations, Troubleshooting]
tags: [network-operations, troubleshooting, case-study, ccna, noc, sla, template]
description: "Template viết case study troubleshooting mạng theo hướng vận hành: triệu chứng, giả thuyết, root cause, solution, verification và ảnh hưởng SLA."
image:
  path: /assets/img/posts/network-operations/troubleshooting-template.png
  alt: Network Troubleshooting
pin: false
---

## Giới thiệu

Khi làm các lab troubleshooting, mình nhận ra nếu chỉ viết "lỗi gì và sửa thế nào" thì khá là thiếu. Ngoài thực tế người ta còn cần biết: impact ra sao, root cause thật sự là gì, verify thế nào, và làm sao tránh lặp lại. Nên mình tạo template này để viết case study theo hướng vận hành: có triệu chứng, có giả thuyết, có bằng chứng, có solution, có verification, và cả phần SLA impact nếu lỗi này xảy ra trong môi trường production.

## Link template

- [Network Troubleshooting Case Study Template](/writeups/network-operations-portfolio/case-study-template/)

## Áp dụng cho case nào?

Mình dùng template này cho các case thường gặp khi học CCNA:

- OSPF neighbor không lên.
- VLAN không thông qua trunk.
- NAT không dịch địa chỉ.
- Interface flap hoặc CRC tăng.
- DHCP relay sai.
- ACL chặn nhầm traffic.

## Cấu trúc template

Mỗi section có mục đích riêng, giúp case study đầy đủ như một incident report thật:

| Section | Mục tiêu |
| --- | --- |
| Problem Description | Mô tả ticket/sự cố như môi trường NOC thật. |
| Expected Behavior | Trạng thái đúng của hệ thống nếu không lỗi. |
| Symptoms | Dấu hiệu quan sát được từ ping, traceroute, log, show command. |
| Initial Hypothesis | Các giả thuyết nguyên nhân theo xác suất (không phải đoán mò, mà dựa trên symptom). |
| Troubleshooting Steps | Quy trình kiểm tra có bằng chứng - mỗi bước loại trừ một giả thuyết. |
| Root Cause | Nguyên nhân gốc đã được chứng minh bằng output cụ thể. |
| Solution | Cấu hình hoặc thao tác sửa lỗi. |
| Verification | Kết quả sau khi fix - chứng minh hệ thống đã hoạt động đúng. |
| Technical Lesson Learned | Bài học kỹ thuật từ case này (ví dụ: nhớ check MTU, nhớ verify area ID). |
| Real Operations / SLA Impact | Ảnh hưởng nếu lỗi này xảy ra trong mạng production (downtime, số user ảnh hưởng, SLA breach). |
| Prevention | Checklist, monitoring, rollback hoặc automation để tránh lặp lại. |

## Case studies đã viết

Hiện tại mình đã áp dụng template này cho:

- [OSPF Neighbor Down](/writeups/network-operations-portfolio/troubleshooting-case-studies/ospf-neighbor-down/)
- [VLAN Connectivity Issue](/writeups/network-operations-portfolio/troubleshooting-case-studies/vlan-connectivity-issue/)
- [NAT Translation Failure](/writeups/network-operations-portfolio/troubleshooting-case-studies/nat-translation-failure/)


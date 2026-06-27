---
layout: page-toc
title: "Network Troubleshooting Case Study Template"
permalink: /writeups/network-operations-portfolio/case-study-template/
toc: true
---

## 1. Problem Description

Mo ta loi theo cach mot NOC/network engineer tiep nhan ticket: thiet bi nao bi anh huong, dich vu nao bi anh huong, thoi diem xay ra va trieu chung ban dau.

## 2. Expected Behavior

Mo ta trang thai dung cua he thong neu khong co loi.

## 3. Symptoms

- Ket qua ping/traceroute.
- Trang thai interface/routing/VLAN/NAT.
- Log hoac output bat thuong.

## 4. Initial Hypothesis

Liet ke 2-4 gia thuyet ban dau, sap xep theo kha nang cao den thap.

## 5. Troubleshooting Steps

| Step | Command / Check | Observation | Decision |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## 6. Root Cause

Ket luan nguyen nhan goc, kem bang chung tu command output.

## 7. Solution

Ghi cau hinh da sua va giai thich vi sao cach sua nay dung.

```txt
! Paste fixed config snippet here
```

## 8. Verification

| Test | Expected | Result |
| --- | --- | --- |
|  |  |  |

## 9. Technical Lesson Learned

Neu quy tac ky thuat rut ra tu case nay. Vi du: OSPF neighbor phu thuoc area, hello/dead timer, subnet, MTU va passive-interface.

## 10. Real Operations / SLA Impact

Lien he van hanh thuc te: loi nay neu xay ra tren production se lam mat ket noi, route blackhole, tang latency, failover khong mong muon hoac vi pham SLA nhu the nao.

## 11. Prevention

- Checklist truoc khi change.
- Command verify sau khi change.
- Monitoring/alert nen co.
- Rollback plan neu change that bai.

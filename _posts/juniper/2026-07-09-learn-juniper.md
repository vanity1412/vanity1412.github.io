---
title: "Learn Juniper"
date: 2026-07-09 08:00:00 +0700
categories: [Juniper, Learning]
tags: [juniper, junos, jncia, is-is, noc, troubleshooting, networking, routing]
description: "Trang điều hướng học Juniper: nền tảng JNCIA/Junos, IS-IS trên Junos và checklist vận hành NOC/Service Operation."
pin: false
---

## Overview

Post này là điểm bắt đầu cho hướng **Learn Juniper**. Mình chia thành 3 nhánh học chính: nền tảng Junos/JNCIA để quen hệ điều hành, CLI và mô hình cấu hình; **IS-IS trên Junos** để đi sâu vào core routing; và checklist **NOC/Service Operation** để dùng trong vận hành, kiểm tra nhanh và troubleshooting.

<div class="juniper-paths" markdown="1">

<a class="juniper-path-card" href="/writeups/learn-juniper/jncia-junos/">
  <span class="juniper-path-card__kicker">Path 01</span>
  <strong>JNCIA Junos - Lý thuyết trọng tâm</strong>
  <span>Nền tảng Junos OS, CLI, mô hình cấu hình, interface, routing cơ bản, policy, firewall filter, CoS và checklist ôn tập.</span>
  <em>Đọc hướng JNCIA/Junos →</em>
</a>

<a class="juniper-path-card" href="/writeups/learn-juniper/isis-user-guide/">
  <span class="juniper-path-card__kicker">Path 02</span>
  <strong>IS-IS User Guide Juniper/Junos</strong>
  <span>Lý thuyết IS-IS theo từng mục: adjacency, LSP/LSDB, level, metric, route leaking, BFD, traffic engineering, IPv6, Segment Routing và troubleshooting.</span>
  <em>Đọc hướng IS-IS →</em>
</a>

<a class="juniper-path-card" href="/writeups/learn-juniper/noc-service-operation-troubleshooting/">
  <span class="juniper-path-card__kicker">Path 03</span>
  <strong>Juniper Junos cho NOC / Service Operation</strong>
  <span>Checklist lệnh cấu hình, kiểm tra thiết bị, interface, routing, log, service và các bước troubleshooting thường dùng trong môi trường NOC.</span>
  <em>Đọc hướng NOC/Operation →</em>
</a>

</div>

## Gợi ý thứ tự học

1. Đọc **JNCIA Junos - Lý thuyết trọng tâm** trước để quen cách Junos tổ chức control plane, forwarding plane, cấu hình candidate/commit và các lệnh kiểm tra cơ bản.
2. Sau đó chuyển sang **IS-IS User Guide Juniper/Junos** để học routing ở mức core network, đặc biệt khi cần hiểu MPLS, SR-MPLS/SRv6 hoặc vận hành mạng nhà mạng.
3. Đọc tiếp **Juniper Junos cho NOC / Service Operation** để gom các lệnh kiểm tra nhanh, log, interface, routing và quy trình xử lý sự cố vào một checklist vận hành.
4. Khi đọc xong mỗi phần, tự tạo checklist lệnh `show`, `monitor`, `traceoptions` tương ứng để biến lý thuyết thành thói quen troubleshooting.

<style>
.juniper-paths {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin: 1.25rem 0 1.75rem;
}

.juniper-path-card {
  display: flex;
  min-width: 0;
  min-height: 13rem;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1rem;
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
  color: var(--text-color);
  text-decoration: none;
}

.juniper-path-card:hover {
  border-color: #0f766e;
  text-decoration: none;
}

.juniper-path-card__kicker {
  color: #0f766e;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.juniper-path-card strong {
  color: var(--heading-color);
  font-size: 1.1rem;
  line-height: 1.35;
}

.juniper-path-card span:not(.juniper-path-card__kicker) {
  color: var(--text-muted-color);
  line-height: 1.58;
}

.juniper-path-card em {
  margin-top: auto;
  color: #0f766e;
  font-style: normal;
  font-weight: 600;
}

@media (max-width: 768px) {
  .juniper-paths {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 769px) and (max-width: 1100px) {
  .juniper-paths {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>

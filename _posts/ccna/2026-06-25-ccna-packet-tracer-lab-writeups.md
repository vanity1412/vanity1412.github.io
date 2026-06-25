---
title: "CCNA Packet Tracer Lab Writeups"
date: 2026-06-25 10:00:00 +0700
categories: [CCNA, Packet Tracer]
tags: [ccna, packet-tracer, networking, routing, switching, lab, writeup]
description: "Bộ writeup các bài lab CCNA Packet Tracer: cấu hình thiết bị, subnetting, VLAN, routing, OSPF, ACL, NAT, WLAN và troubleshooting."
image:
  path: /assets/img/posts/ccna/ccna.png
  alt: CCNA Packet Tracer Lab Writeups
pin: true
---

## Overview

Đây là trang tổng hợp các bài **CCNA Packet Tracer Lab Writeups**. Mỗi card bên dưới là một dạng lab riêng. Nút **Read writeup** mở mục lục của từng dạng; trong đó mỗi bài lab có trang riêng và mở ở tab mới. Nút **Download labs** mở trang tải file .pka/.pkt để tự làm trước.

Hiện có **94 lab** được chia thành **20 dạng**, kèm thêm track **Full Lab Từ Đầu Đến Cuối** từ folder 00-TONG-HOP-THEO-SO-DAU-BAI cho người muốn học một mạch theo thứ tự tổng hợp.

## Cách Đọc

1. Chọn dạng lab muốn học.
2. Nếu muốn tự làm trước, bấm **Download labs**.
3. Khi cần đối chiếu, bấm **Read writeup**, rồi chọn **Đọc bài** để mở trang riêng của từng lab.
4. Mỗi trang writeup có sẵn chỗ cho ảnh topology, cấu hình, kiểm tra và lỗi gặp phải.

## Lab Tracks

<style>
.ccna-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1.25rem 0 2rem;
}

.ccna-card {
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
}

.ccna-card__body {
  display: flex;
  min-height: 100%;
  flex-direction: column;
  padding: 0.95rem;
}

.ccna-card__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
  font-size: 0.78rem;
  color: var(--text-muted-color);
}

.ccna-card__title {
  margin: 0 0 0.45rem;
  font-size: 1.04rem;
  line-height: 1.3;
}

.ccna-card__summary {
  flex: 1;
  min-height: 4.4rem;
  margin: 0 0 0.85rem;
  color: var(--text-muted-color);
  font-size: 0.9rem;
  line-height: 1.45;
}

.ccna-card__actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}

.ccna-card__actions a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.15rem;
  padding: 0.35rem 0.55rem;
  border: 1px solid var(--main-border-color);
  border-radius: 6px;
  font-size: 0.84rem;
  font-weight: 600;
  text-align: center;
}

.ccna-card__actions a:first-child {
  background: #0f766e;
  border-color: #0f766e;
  color: #fff;
}

.ccna-card__actions a:last-child {
  background: transparent;
}
</style>

<div class="ccna-grid">
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#01</span><span>1 labs</span></div>
      <h3 class="ccna-card__title">Làm Quen Packet Tracer</h3>
      <p class="ccna-card__summary">Nhận diện thiết bị, đường kết nối, topology và cách đọc bài lab Packet Tracer.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/01-lam-quen-packet-tracer/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#02</span><span>8 labs</span></div>
      <h3 class="ccna-card__title">IOS Và Cấu Hình Cơ Bản</h3>
      <p class="ccna-card__summary">Thao tác CLI, cấu hình switch/router ban đầu, interface, password và lưu cấu hình.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#03</span><span>5 labs</span></div>
      <h3 class="ccna-card__title">ARP, ICMP, TCP Và UDP</h3>
      <p class="ccna-card__summary">Quan sát cách host giao tiếp qua MAC/IP, ARP, ICMP, TCP và UDP.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/03-arp-icmp-tcp-udp/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#04</span><span>5 labs</span></div>
      <h3 class="ccna-card__title">Kết Nối Vật Lý</h3>
      <p class="ccna-card__summary">Chọn cáp, chọn cổng, kiểm tra interface và xác minh end-to-end connectivity.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/04-ket-noi-vat-ly/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#05</span><span>7 labs</span></div>
      <h3 class="ccna-card__title">IP Addressing, Subnetting, VLSM</h3>
      <p class="ccna-card__summary">Thiết kế IPv4/IPv6, chia subnet, VLSM và gán địa chỉ đúng yêu cầu.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/05-ip-subnetting-vlsm/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#06</span><span>6 labs</span></div>
      <h3 class="ccna-card__title">VLAN, Trunk Và DTP</h3>
      <p class="ccna-card__summary">Tạo VLAN, gán access port, cấu hình trunk và kiểm tra DTP.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/06-vlan-trunk-dtp/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#07</span><span>4 labs</span></div>
      <h3 class="ccna-card__title">STP Và EtherChannel</h3>
      <p class="ccna-card__summary">Phân tích STP, root bridge, port role và triển khai EtherChannel.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/07-stp-etherchannel/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#08</span><span>4 labs</span></div>
      <h3 class="ccna-card__title">Inter-VLAN Và Layer 3 Switching</h3>
      <p class="ccna-card__summary">Cấu hình router-on-a-stick, SVI, Layer 3 switching và xử lý lỗi liên VLAN.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/08-inter-vlan-layer-3-switching/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#09</span><span>1 labs</span></div>
      <h3 class="ccna-card__title">FHRP Và HSRP</h3>
      <p class="ccna-card__summary">Cấu hình gateway dự phòng với HSRP và kiểm tra active/standby.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/09-fhrp-hsrp/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/09-fhrp-hsrp/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#10</span><span>3 labs</span></div>
      <h3 class="ccna-card__title">Static Và Default Routing</h3>
      <p class="ccna-card__summary">Cấu hình static route, default route IPv4/IPv6 và troubleshoot routing table.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/10-static-default-routing/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#11</span><span>7 labs</span></div>
      <h3 class="ccna-card__title">OSPF</h3>
      <p class="ccna-card__summary">Triển khai single-area OSPFv2, router ID, neighbor, DR/BDR và default route.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/11-ospf/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/11-ospf/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#12</span><span>2 labs</span></div>
      <h3 class="ccna-card__title">DHCP</h3>
      <p class="ccna-card__summary">Cấu hình DHCPv4 pool, excluded address, gateway, DNS và kiểm tra lease.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/12-dhcp/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/12-dhcp/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#13</span><span>5 labs</span></div>
      <h3 class="ccna-card__title">ACL</h3>
      <p class="ccna-card__summary">Cấu hình standard, extended, named ACL và đặt đúng interface/direction.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/13-acl/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/13-acl/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#14</span><span>8 labs</span></div>
      <h3 class="ccna-card__title">NAT Và PAT</h3>
      <p class="ccna-card__summary">Thực hành static NAT, dynamic NAT, PAT và kiểm tra translation.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/14-nat-pat/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/14-nat-pat/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#15</span><span>5 labs</span></div>
      <h3 class="ccna-card__title">Wireless Và WLAN</h3>
      <p class="ccna-card__summary">Cấu hình WLAN, WLC, WPA2 Enterprise và troubleshoot kết nối không dây.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/15-wireless-wlan/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/15-wireless-wlan/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#16</span><span>6 labs</span></div>
      <h3 class="ccna-card__title">Bảo Mật Thiết Bị Và Switch</h3>
      <p class="ccna-card__summary">Cấu hình SSH, password an toàn, port security và hardening cơ bản.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/16-bao-mat-thiet-bi-switch/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/16-bao-mat-thiet-bi-switch/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#17</span><span>6 labs</span></div>
      <h3 class="ccna-card__title">Quản Trị Mạng</h3>
      <p class="ccna-card__summary">Dùng CDP, LLDP, NTP, TFTP, backup config và nâng cấp IOS.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/17-quan-tri-mang/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#18</span><span>6 labs</span></div>
      <h3 class="ccna-card__title">Kiểm Tra Và Xử Lý Sự Cố</h3>
      <p class="ccna-card__summary">Dùng ping, traceroute và show commands để tìm lỗi theo từng lớp.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/18-kiem-tra-xu-ly-su-co/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#19</span><span>1 labs</span></div>
      <h3 class="ccna-card__title">WAN</h3>
      <p class="ccna-card__summary">Ghi chú khái niệm WAN và cách đọc kết nối giữa các mạng ở phạm vi rộng.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/19-wan/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/19-wan/downloads/">Download labs</a>
      </div>
    </div>
  </article>
  <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#20</span><span>3 labs</span></div>
      <h3 class="ccna-card__title">Bài Tổng Hợp</h3>
      <p class="ccna-card__summary">Tổng hợp IP, VLAN, routing, dịch vụ mạng, bảo mật và troubleshooting.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/20-bai-tong-hop/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/20-bai-tong-hop/downloads/">Download labs</a>
      </div>
    </div>
  </article>
    <article class="ccna-card">
    <div class="ccna-card__body">
      <div class="ccna-card__meta"><span>#21</span><span>94 labs</span></div>
      <h3 class="ccna-card__title">Full Lab Từ Đầu Đến Cuối</h3>
      <p class="ccna-card__summary">Lộ trình tổng hợp toàn bộ lab, phù hợp khi muốn làm tuần tự từ bài đầu đến bài cuối.</p>
      <div class="ccna-card__actions">
        <a href="/writeups/ccna-packet-tracer-writeups/00-full-lab-tu-dau-den-cuoi/">Read writeup</a>
        <a href="/writeups/ccna-packet-tracer-writeups/00-full-lab-tu-dau-den-cuoi/downloads/">Download labs</a>
      </div>
    </div>
  </article>
</div>

---

## Writeup Structure

Mỗi dạng lab có cấu trúc thống nhất:

- **Tổng quan**: dạng lab này cần nắm gì.
- **Danh sách bài lab**: mỗi file .pka/.pkt là một dòng riêng, có nút mở trang lab.
- **Trang lab riêng**: mỗi bài có permalink riêng, mở được ở tab mới.
- **Lab chi tiết**: mục tiêu, topology, kế hoạch, cấu hình, kiểm tra, lỗi gặp phải và kết quả cuối.

Phần tải file được tách ra thành trang riêng để trang đọc lời giải không bị lẫn với trang download.

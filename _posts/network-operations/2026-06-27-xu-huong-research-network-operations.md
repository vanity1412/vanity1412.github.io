---
title: "Research: Core IP, Transmission & Network Automation"
date: 2026-06-27 00:20:00 +0700
categories: [Network Operations, Research]
tags: [network-operations, core-ip, dwdm, snmp, telemetry, automation, aiops, research]
description: "Research index cho hướng Core IP, truyền dẫn quang, telemetry và automation trong vận hành mạng."
image:
  path: /assets/img/posts/network-operations/research-trends.png
  alt: Network Operations Research Trends
pin: false
---

<div class="research-trends-post" markdown="1">

## Giới thiệu

Sau khi làm xong mấy lab CCNA, mình bắt đầu tự hỏi: OK vậy ngoài thực tế người ta làm việc thế nào? Rồi mình mới nhận ra có cả một lớp kiến thức mà CCNA chưa chạm tới - từ lớp truyền dẫn quang bên dưới IP, đến telemetry/monitoring, rồi automation. Post này mình tổng hợp lại các research note đang học dần về **Network Operations / Core IP / Transmission / Automation**.

<style>
.research-hero {
  display: grid;
  gap: 1rem;
  margin: 1.25rem 0 1.75rem;
  padding: 1.1rem;
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
}

.research-hero__kicker {
  margin: 0;
  color: var(--text-muted-color);
  font-size: 0.86rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.research-hero__title {
  margin: 0;
  font-size: 1.35rem;
  line-height: 1.35;
}

.research-hero__text {
  margin: 0;
  color: var(--text-muted-color);
  line-height: 1.62;
}

.research-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin: 1.25rem 0 2rem;
}

.research-card {
  display: flex;
  min-width: 0;
  flex-direction: column;
  gap: 0.85rem;
  padding: 1rem;
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
}

.research-card__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.research-chip {
  display: inline-flex;
  align-items: center;
  min-height: 1.65rem;
  padding: 0.15rem 0.52rem;
  border: 1px solid var(--main-border-color);
  border-radius: 999px;
  color: var(--text-muted-color);
  font-size: 0.76rem;
  font-weight: 700;
}

.research-card h3 {
  margin: 0;
  font-size: 1.08rem;
  line-height: 1.35;
}

.research-card p {
  margin: 0;
  color: var(--text-muted-color);
  line-height: 1.58;
}

.research-card a {
  width: fit-content;
  margin-top: auto;
  padding: 0.42rem 0.72rem;
  border: 1px solid #0f766e;
  border-radius: 6px;
  background: #0f766e;
  color: #fff;
  font-size: 0.84rem;
  font-weight: 700;
}

.research-flow {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.75rem;
  margin: 1rem 0 1.75rem;
}

.research-flow div {
  min-width: 0;
  padding: 0.85rem;
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
}

.research-flow strong {
  display: block;
  margin-bottom: 0.35rem;
}

.research-flow span {
  color: var(--text-muted-color);
  font-size: 0.88rem;
  line-height: 1.45;
}

@media (max-width: 760px) {
  .research-grid,
  .research-flow {
    grid-template-columns: 1fr;
  }
}
</style>

<section class="research-hero">
  <p class="research-hero__kicker">Research direction</p>
  <h2 class="research-hero__title">Từ CCNA lab sang tư duy vận hành Core IP</h2>
  <p class="research-hero__text">Học xong routing/switching cơ bản thì mình phát hiện còn thiếu nhiều mảnh ghép lắm. Ví dụ link core flap thì đổ lỗi cho bên nào? Làm sao biết được là lỗi IP layer hay optical layer? Rồi làm sao giám sát mạng theo kiểu real-time chứ không phải cứ 5 phút poll SNMP một lần? Đây là lý do mình bắt đầu đào sâu vào truyền dẫn quang, telemetry và automation.</p>
</section>

## Research Notes

<div class="research-grid">
  <article class="research-card">
    <div class="research-card__meta">
      <span class="research-chip">Transmission</span>
      <span class="research-chip">Core IP</span>
      <span class="research-chip">SLA</span>
    </div>
    <h3>DWDM for IP Network Engineers</h3>
    <p>Lúc đầu mình nghĩ DWDM là chuyện của transmission team chứ IP engineer không cần quan tâm. Nhưng khi link core bị issue, không hiểu optical layer thì khó mà tách được lỗi IP hay lỗi phía dưới. Note này mình tổng hợp những khái niệm wavelength, transponder, OTN, coherent optics theo góc nhìn của người làm Core IP.</p>
    <a href="/writeups/network-operations-portfolio/research-notes/dwdm-for-ip-network-engineers/">Read research note</a>
  </article>

  <article class="research-card">
    <div class="research-card__meta">
      <span class="research-chip">Monitoring</span>
      <span class="research-chip">Telemetry</span>
      <span class="research-chip">AI-Ops</span>
    </div>
    <h3>SNMP vs Streaming Telemetry</h3>
    <p>SNMP poll cứ 5 phút thì làm sao bắt kịp event xảy ra trong 10 giây? Streaming telemetry push data real-time về, dùng gRPC/gNMI và YANG model. Mình đang tìm hiểu xem workflow này hoạt động thế nào và liên hệ gì với AI-Ops về sau.</p>
    <a href="/writeups/network-operations-portfolio/research-notes/snmp-vs-streaming-telemetry/">Read research note</a>
  </article>

  <article class="research-card">
    <div class="research-card__meta">
      <span class="research-chip">NOC</span>
      <span class="research-chip">SOC</span>
      <span class="research-chip">Operations</span>
    </div>
    <h3>SOC vs NOC</h3>
    <p>Có lần mình bị hỏi "em muốn vào SOC hay NOC?" mà không biết khác nhau chỗ nào. Sau khi research thì mình mới hiểu NOC tập trung giữ dịch vụ ổn định (availability, performance), còn SOC tập trung phát hiện và xử lý threat. Hai bên cần phối hợp khi có sự cố nhưng workflow và mindset khác nhau.</p>
    <a href="/writeups/network-operations-portfolio/research-notes/soc-vs-noc/">Read research note</a>
  </article>
</div>

## Tại sao chọn mấy topic này?

<div class="research-flow">
  <div>
    <strong>Core IP</strong>
    <span>Biết routing/switching thì mới hiểu traffic đi đường nào, failover ra sao, và route mất ở đâu khi có sự cố.</span>
  </div>
  <div>
    <strong>Transmission</strong>
    <span>Hiểu DWDM thì mới biết phân tầng lỗi đúng. Link flap có thể do optical layer, không phải lúc nào cũng là lỗi config IP.</span>
  </div>
  <div>
    <strong>Telemetry</strong>
    <span>Dữ liệu real-time giúp phát hiện anomaly nhanh hơn SNMP polling kiểu cũ, và cũng cần thiết cho AI-Ops về sau.</span>
  </div>
  <div>
    <strong>Automation</strong>
    <span>Backup config tự động, diff config trước/sau thay đổi giúp có bằng chứng cho change management, giảm được manual error.</span>
  </div>
</div>

## Liên hệ với Portfolio

Các research note này mình dùng để bổ sung cho các lab thực hành trong portfolio:

| Portfolio piece | Vai trò |
| --- | --- |
| CCNA Enterprise Capstone | Chứng minh nền tảng routing/switching và thiết kế lab. |
| Troubleshooting case studies | Chứng minh quy trình debug có hệ thống: từ symptom → hypothesis → root cause → fix → verify. |
| Netmiko config backup + diff | Chứng minh tư duy automation cho change management. |
| DWDM / Telemetry research | Chứng minh định hướng Core IP, transmission và data-driven operations. |
| SOC vs NOC | Chứng minh hiểu bối cảnh operations: vận hành dịch vụ khác với security operations nhưng hai bên phải phối hợp. |

## Góp ý

Portfolio mình đang xây dựng theo hướng **Network Operations / Core IP / Automation**. Nếu bạn thấy phần research hay cách liên hệ với vận hành thực tế có chỗ nào còn vụng về hoặc chưa rõ, mình rất mong được góp ý!

</div>

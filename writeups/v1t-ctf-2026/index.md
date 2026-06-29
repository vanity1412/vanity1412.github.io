---
layout: page
title: "V1T CTF 2026 Writeups"
description: "Writeups for V1T CTF 2026 by ComTamHoangDieu2."
permalink: /writeups/v1t-ctf-2026/
---

<style>
.v1t-hero {
  display: grid;
  grid-template-columns: minmax(96px, 140px) 1fr;
  gap: 1.25rem;
  align-items: center;
  margin: 0.5rem 0 1.5rem;
}

.v1t-hero img {
  width: 100%;
  max-width: 140px;
  border-radius: 8px;
}

.v1t-hero h2 {
  margin: 0 0 0.35rem;
}

.v1t-hero p {
  margin: 0;
  color: var(--text-muted-color);
}

.v1t-scoreboard {
  margin: 1rem 0 1.75rem;
  border-radius: 8px;
}

.v1t-writeups {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}

.v1t-writeup {
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  padding: 1rem;
  background: var(--card-bg);
}

.v1t-writeup h3 {
  margin: 0 0 0.45rem;
  font-size: 1.05rem;
}

.v1t-writeup p {
  min-height: 3.25rem;
  margin: 0 0 0.85rem;
  color: var(--text-muted-color);
  font-size: 0.92rem;
}

.v1t-writeup a {
  font-weight: 600;
}

@media (max-width: 576px) {
  .v1t-hero {
    grid-template-columns: 88px 1fr;
    gap: 1rem;
  }
}
</style>

<section class="v1t-hero">
  <img src="/assets/portfolio-assets/img/v1t-ctf-2026/avatar.png" alt="V1T CTF 2026 avatar">
  <div>
    <h2>ComTamHoangDieu2 - V1T CTF 2026</h2>
    <p>Team result: 11th place with 7294 points. This page collects the solved challenge writeups and supporting notes.</p>
  </div>
</section>

![ComTamHoangDieu2 top 11 scoreboard](/assets/portfolio-assets/img/v1t-ctf-2026/top-11.png){: .v1t-scoreboard }

## Writeups

<div class="v1t-writeups">
  <article class="v1t-writeup">
    <h3>78CT</h3>
    <p>OSINT and mixed-case text steganography through a public Google Maps review.</p>
    <a href="/writeups/v1t-ctf-2026/78ct-osint-stego/">Open writeup</a>
  </article>

  <article class="v1t-writeup">
    <h3>BasicQnA</h3>
    <p>Network forensics with PCAPNG analysis, HTTP traffic reconstruction, command injection artifacts, and final QnA flag recovery.</p>
    <a href="/writeups/v1t-ctf-2026/basicqna-forensics/">Open writeup</a>
  </article>

  <article class="v1t-writeup">
    <h3>Hardware & BLE Forensics</h3>
    <p>ESP32 firmware reverse engineering, AES-XTS flash decryption, and BLE/GATT multi-stage decoding.</p>
    <a href="/writeups/v1t-ctf-2026/hardware-ble-forensics/">Open writeup</a>
  </article>

  <article class="v1t-writeup">
    <h3>Pwn VBAFI</h3>
    <p>Pwn notes for taleMate, StaleMate - Revenge, and Acroform with exploit flow and scripts.</p>
    <a href="/writeups/v1t-ctf-2026/pwn-vbafi/">Open writeup</a>
  </article>
</div>


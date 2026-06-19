---
title: "HackTheBox Sherlocks - Blue Team Writeups"
date: 2026-06-18 10:00:00 +0700
categories: [HackTheBox, Sherlocks]
tags: [hackthebox, sherlocks, dfir, blue-team, writeup]
description: "Blue Team writeup collection for HackTheBox Sherlocks challenges."
image:
  path: /assets/portfolio-assets/img/htb/avt.png
  alt: HackTheBox Sherlocks Overview
pin: true
---

## Overview

A collection of HackTheBox Sherlocks Blue Team writeups. Click on each writeup to view the detailed investigation report.

## Writeup Index

<style>
.sherlock-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.15rem;
  margin: 1.25rem 0 2rem;
}

.sherlock-card {
  overflow: hidden;
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
}

.sherlock-card__cover {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  object-position: top center;
  border-bottom: 1px solid var(--main-border-color);
}

.sherlock-card__body {
  padding: 0.9rem;
}

.sherlock-card__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
  font-size: 0.78rem;
  color: var(--text-muted-color);
}

.sherlock-card__title {
  margin: 0 0 0.45rem;
  font-size: 1.05rem;
  line-height: 1.25;
}

.sherlock-card__summary {
  min-height: 4.5rem;
  margin: 0 0 0.8rem;
  color: var(--text-muted-color);
  font-size: 0.9rem;
  line-height: 1.45;
}

.sherlock-card__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
}

.sherlock-card__actions a {
  display: inline-flex;
  align-items: center;
  min-height: 2.1rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid var(--main-border-color);
  border-radius: 6px;
  font-size: 0.86rem;
  font-weight: 600;
}

.sherlock-card__actions a:first-child {
  background: #9fef00;
  border-color: #9fef00;
  color: #111;
}
</style>

<div class="sherlock-grid">
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-01-bling-bling.png" alt="Bling Bling PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#01</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Bling Bling</h3>
      <p class="sherlock-card__summary">Investigate a Diwali sale web incident around a StoreD-backed shopping site and identify suspicious activity.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-01-bling-bling/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-02-compromised.png" alt="Compromised PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#02</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Compromised</h3>
      <p class="sherlock-card__summary">Analyze suspicious network activity, find the root cause, and recommend remediation steps for the SOC.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-02-compromised/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-03-constellation.png" alt="Constellation PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#03</span><span>Medium</span></div>
      <h3 class="sherlock-card__title">Constellation</h3>
      <p class="sherlock-card__summary">Follow memory-carved URLs to assess insider-threat leads, exfiltration evidence, and threat intelligence clues.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-03-constellation/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-04-cookie-consumption.png" alt="Cookie Consumption PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#04</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Cookie Consumption</h3>
      <p class="sherlock-card__summary">Trace a Kubernetes breach against Santa's Cookie Consumption Scheduler and identify attacker actions.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-04-cookie-consumption/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-05-detroit-become-human.png" alt="Detroit Become Human PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#05</span><span>Hard</span></div>
      <h3 class="sherlock-card__title">Detroit Become Human</h3>
      <p class="sherlock-card__summary">Investigate a suspicious AI-tool download from social media and uncover the true source of the endpoint incident.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-05-detroit-become-human/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-06-einladen.png" alt="Einladen PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#06</span><span>Medium</span></div>
      <h3 class="sherlock-card__title">Einladen</h3>
      <p class="sherlock-card__summary">Analyze a suspected embassy-invite phishing email using binaries, packet capture, DLLs, and HTA artifacts.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-06-einladen/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-07-hyperfiletable.png" alt="HyperFileTable PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#07</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">HyperFileTable</h3>
      <p class="sherlock-card__summary">Review a phishing case involving a malicious onboarding attachment delivered to a new Forela employee.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-07-hyperfiletable/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-08-jingle-bell.png" alt="Jingle Bell PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#08</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Jingle Bell</h3>
      <p class="sherlock-card__summary">Investigate an insider-threat suspicion, unauthorized software, and the conversation behind a possible data leak.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-08-jingle-bell/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-09-knock-knock.png" alt="Knock Knock PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#09</span><span>Medium</span></div>
      <h3 class="sherlock-card__title">Knock Knock</h3>
      <p class="sherlock-card__summary">Use packet capture evidence to reconstruct how an internet-exposed development server was hit by ransomware.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-09-knock-knock/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-10-kuber.png" alt="Kuber PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#10</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Kuber</h3>
      <p class="sherlock-card__summary">Analyze Kubernetes namespace data from an exposed proxy test environment and determine whether it was compromised.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-10-kuber/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-11-litter.png" alt="Litter PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#11</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Litter</h3>
      <p class="sherlock-card__summary">Investigate traffic from a shared testing host to determine how it was compromised and what data was stolen.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-11-litter/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-12-lockpick-2-0.png" alt="LockPick 2.0 PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#12</span><span>Hard</span></div>
      <h3 class="sherlock-card__title">LockPick 2.0</h3>
      <p class="sherlock-card__summary">Handle a ransomware recovery case, safely analyze dangerous artifacts, and recover encrypted files without negotiation.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-12-lockpick-2-0/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-13-loggy.png" alt="Loggy PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#13</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Loggy</h3>
      <p class="sherlock-card__summary">Reverse and investigate a suspicious screenshot tool tied to repeated credential exposure on the dark web.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-13-loggy/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-14-neural-noel.png" alt="Neural Noel PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#14</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Neural Noel</h3>
      <p class="sherlock-card__summary">Investigate suspicious files, unusual HTTP traffic, and strange chatbot prompts in Santa's AI support system.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-14-neural-noel/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-15-noted.png" alt="Noted PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#15</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Noted</h3>
      <p class="sherlock-card__summary">Work a data-extortion case from a developer workstation and identify how sensitive files were collected.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-15-noted/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-16-nubilum-2.png" alt="Nubilum 2 PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#16</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Nubilum 2</h3>
      <p class="sherlock-card__summary">Investigate AWS S3 public-access exposure, object changes, and the identity behind disrupted file access.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-16-nubilum-2/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-17-origins.png" alt="Origins PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#17</span><span>Very Easy</span></div>
      <h3 class="sherlock-card__title">Origins</h3>
      <p class="sherlock-card__summary">Use PCAP evidence to prove FTP compromise, brute force activity, and data exfiltration after an S3 breach.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-17-origins/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-18-percy-pay.png" alt="Percy Pay PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#18</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Percy Pay</h3>
      <p class="sherlock-card__summary">Validate dark-web claims about exposed payment-provider customer data and measure the AWS/S3 impact.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-18-percy-pay/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-19-psittaciformes.png" alt="Psittaciformes PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#19</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Psittaciformes</h3>
      <p class="sherlock-card__summary">Analyze retrospective host collection to verify how an internal pentest team's credential store was compromised.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-19-psittaciformes/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-20-super-star.png" alt="Super Star PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#20</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Super Star</h3>
      <p class="sherlock-card__summary">Investigate fake discount-coupon phishing, suspicious processes, malicious binaries, and related network traffic.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-20-super-star/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-21-team-work.png" alt="Team Work PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#21</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Team Work</h3>
      <p class="sherlock-card__summary">Assess mailbox evidence after discovery-command alerts on a developer workstation during a supply-chain concern.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-21-team-work/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-22-ticktock.png" alt="TickTock PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#22</span><span>Medium</span></div>
      <h3 class="sherlock-card__title">TickTock</h3>
      <p class="sherlock-card__summary">Investigate a spear-phishing/social-engineering case where fake IT staff try to obtain remote PC access.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-22-ticktock/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-23-training-day.png" alt="Training Day PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#23</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Training Day</h3>
      <p class="sherlock-card__summary">Practice reverse engineering across three binaries and document each artifact's behavior.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-23-training-day/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-24-trent.png" alt="Trent PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#24</span><span>Medium</span></div>
      <h3 class="sherlock-card__title">Trent</h3>
      <p class="sherlock-card__summary">Use packet capture evidence to investigate lateral movement and exploitation against a SOHO router.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-24-trent/report/">Read report</a></div>
    </div>
  </article>
  <article class="sherlock-card">
    <img class="sherlock-card__cover" src="/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-25-ultimatum.png" alt="Ultimatum PDF cover">
    <div class="sherlock-card__body">
      <div class="sherlock-card__meta"><span>#25</span><span>Easy</span></div>
      <h3 class="sherlock-card__title">Ultimatum</h3>
      <p class="sherlock-card__summary">Investigate a compromised WordPress blog, identify the vulnerable plugin path, and restore the service.</p>
      <div class="sherlock-card__actions"><a href="/writeups/htb-sherlocks-blue-team-writeups/sherlock-25-ultimatum/report/">Read report</a></div>
    </div>
  </article>
</div>

---

## About These Writeups

Each writeup includes:
- **Scenario Summary**: Context and background
- **Investigation Process**: Step-by-step analysis with questions and answers
- **Key Findings**: Summary of discoveries
- **IOCs**: Indicators of Compromise
- **Timeline**: Event chronology
- **Tools Used**: Analysis toolkit

Click on any **?? Read** button above to view the full writeup.


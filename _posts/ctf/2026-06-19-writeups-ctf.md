---
title: "Writeups CTF"
date: 2026-06-19 09:15:00 +0700
categories: [CTF, Writeups]
tags: [ctf, capture-the-flag, web, crypto, reversing, forensics, pwn, writeup]
description: "CTF competition writeups, solve notes, screenshots, payloads, and scripts."
pin: false
---

## Overview

CTF writeup collection for competition solves. Each event page will be updated later with challenge notes, screenshots, payloads, scripts, and final solve paths.

## CTF Index

<style>
.ctf-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin: 1.25rem 0 2rem;
}

.ctf-card {
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  background: var(--card-bg);
  padding: 1rem;
}

.ctf-card__meta {
  display: flex;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.65rem;
  color: var(--text-muted-color);
  font-size: 0.82rem;
}

.ctf-card h3 {
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
}

.ctf-card p {
  min-height: 3.75rem;
  margin: 0 0 0.85rem;
  color: var(--text-muted-color);
  font-size: 0.92rem;
  line-height: 1.45;
}

.ctf-card a {
  display: inline-flex;
  align-items: center;
  min-height: 2.1rem;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  background: #9fef00;
  color: #111;
  font-weight: 600;
}
</style>

<div class="ctf-grid">
  <article class="ctf-card">
    <div class="ctf-card__meta"><span>2026</span><span>Draft</span></div>
    <h3>Google Capture The Flag 2026</h3>
    <p>Google CTF challenge writeups for web, crypto, reversing, pwn, forensics, scripts, and solve notes.</p>
    <a href="/writeups/google-capture-the-flag-2026/">Open event</a>
  </article>

  <article class="ctf-card">
    <div class="ctf-card__meta"><span>7.0</span><span>Draft</span></div>
    <h3>BCACTF 7.0</h3>
    <p>BCACTF challenge writeups for analysis notes, screenshots, payloads, scripts, and final solve paths.</p>
    <a href="/writeups/bcactf-7-0/">Open event</a>
  </article>
</div>

## Writeup Format

Use this structure when adding each challenge:

1. Challenge Summary
2. Files Provided
3. Initial Observations
4. Solve Path
5. Exploit Or Script
6. Flag
7. Lessons Learned

---
title: "picoCTF - Scan Surprise"
date: 2026-06-18 10:00:00 +0700
categories: [CTF, Writeup]
tags: [picoctf, forensics, qr-code, writeup]
description: "A short CTF writeup for a QR-code based forensics challenge."
image:
  path: /assets/portfolio-assets/img/CTF2025.png
  alt: CTF writeup
---

## Challenge

| Field | Value |
| --- | --- |
| Platform | picoCTF |
| Category | Forensics |
| Name | Scan Surprise |
| Difficulty | Easy |

The challenge provides an archive containing an image. The title hints that the answer is hidden in something that should be scanned.

## Files

After downloading the challenge archive, I first checked the extracted files:

```bash
unzip challenge.zip
ls -la
file *
```

The interesting file was an image containing a QR code.

## Approach

Because the artifact is a QR code, the fastest path is to decode it locally instead of manually scanning it with a phone. On Linux, `zbarimg` is useful for this:

```bash
zbarimg flag.png
```

If `zbarimg` is not installed:

```bash
sudo apt install zbar-tools
```

## Result

The QR decoder returned the flag text directly.

```text
QR-Code:picoCTF{...}
```

## Takeaway

For simple forensics challenges, I usually start with file identification before trying complex analysis. Small hints in the challenge title can be enough to choose the right tool quickly.


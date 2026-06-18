---
title: "Ransomware Response Challenge: a mini SOC lab journal"
date: 2025-11-01 09:00:00 +0700
categories: [Blue Team, Incident Response]
tags: [soc, incident-response, ransomware, threat-hunting]
description: "A reusable ransomware response lab structure covering triage, timeline building, containment, and lessons learned."
image:
  path: /assets/portfolio-assets/img/blue/Lab_SOC/setup1.png
  alt: SOC lab
---

## Context

This lab simulates a workstation with abnormal behavior: renamed files, suspicious processes running from a user directory, and increased network traffic. The goal is to document the SOC/IR triage process rather than only recording the final answer.

## Questions to answer

- Where did the first alert come from?
- Which host and user were involved?
- Is there evidence of encryption, lateral movement, or exfiltration?
- Which IOCs can be used for additional hunting?

## Data to collect

- Windows Event Logs: Security, Sysmon, PowerShell Operational.
- Processes, scheduled tasks, services, and startup items.
- File timeline around the alert window.
- Network connections, DNS queries, proxy logs, or firewall logs when available.

## Analysis timeline

1. Identify the first alert timestamp.
2. Filter processes created around the suspicious window.
3. Find unusual parent processes and command lines that may download payloads.
4. Correlate mass file writes/renames with authentication events.
5. Review outbound connections to evaluate possible exfiltration.

## IOC

| Type | Value | Note |
| --- | --- | --- |
| Host | `LAB-WIN-01` | Affected workstation |
| Path | `%AppData%\\*.exe` | Location to inspect |
| Event | `4688`, Sysmon `1`, Sysmon `11` | Process/file activity |

## Conclusion

For a real writeup, this section should briefly answer root cause, scope, strongest evidence, and containment steps. This sample keeps the structure ready for future lab evidence.

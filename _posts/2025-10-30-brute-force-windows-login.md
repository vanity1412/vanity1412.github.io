---
title: "Brute-force Windows Login: triaging RDP with Event Logs"
date: 2025-10-30 09:00:00 +0700
categories: [Blue Team, Incident Response]
tags: [windows-security, rdp, event-log, incident-response]
description: "A Windows Event Log triage template for repeated failed logons and possible successful RDP access."
image:
  path: /assets/portfolio-assets/img/Blueteam.png
  alt: Blue Team
---

## Context

An alert reports many failed logon attempts against a Windows host. The goal is to determine whether this is noise, password spraying, brute-force activity, or a successful login after repeated failures.

## Event IDs to check

| Event ID | Meaning |
| --- | --- |
| `4625` | Failed logon |
| `4624` | Successful logon |
| `4648` | Logon with explicit credentials |
| `4776` | NTLM authentication |
| `1149` | RDP authentication |

## Triage flow

1. Filter `4625` by account, source IP, and `LogonType`.
2. Check whether `4624` appears for the same account/source after the failed attempts.
3. Review `LogonType 10` for RDP or `LogonType 3` for network logons.
4. Check whether the account is privileged, locked, or recently changed.
5. Look for post-logon activity: new processes, services, scheduled tasks, or outbound connections.

## Sample conclusion

If there are only failed attempts and no post-authentication activity, the case can be recorded as a brute-force attempt. If there is a successful logon, the case should move into incident response: scope the host, collect artifacts, reset credentials, and hunt for lateral movement.

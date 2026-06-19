---
layout: page
title: "Sherlock: ultimatum - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-25-ultimatum/report/
---

![ultimatum cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-25-ultimatum.png)

# ultimatum

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `ultimatum.pdf` |
| Pages | 9 |
| Difficulty | Easy |
| Prepared by | n4ch0 |
| Author | (s): CyberJunkie |

## Scenario Summary

One of the Forelas WordPress servers was a target of notorious Threat Actors TA. The
website was running a blog dedicated to the Forela Social Club, where Forela employees
can chat and discuss random topics. Unfortunately, it became a target of a threat group.
The SOC team believe this was due to the blog running a vulnerable plugin. The IT admin
already followed the acquisition playbook and triaged the server for the security team.
Ultimately (no pun intended) it is your responsibility to investigate the incident. Step in and
confirm the culprits behind the attack and restore this important service within the Forela
environment.
Ultimatum 1

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Ultimatum.zip 3FD4E122BBD899F43FA7101918FE335D
Skills Learnt
Linux Forensics
Incident Response
Web forensics
Correlation between artifacts

## Tools Used

| Tool | Purpose |
| --- | --- |
| PowerShell | Used or likely relevant based on the source writeup |
| Docker | Used or likely relevant based on the source writeup |
| VirusTotal | Used or likely relevant based on the source writeup |

## Investigation Process

No structured question-and-answer text was detected. Review the source PDF and complete this section manually.

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Primary finding | To be completed after review |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Initial Access | Phishing: Spearphishing Attachment/Link | Observed in extracted case notes; validate with report evidence. |
| Execution | Command and Scripting Interpreter | Observed in extracted case notes; validate with report evidence. |
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
| Discovery | System / Network Discovery | Observed in extracted case notes; validate with report evidence. |
| Lateral Movement | Remote Services | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Linux
DFIR

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

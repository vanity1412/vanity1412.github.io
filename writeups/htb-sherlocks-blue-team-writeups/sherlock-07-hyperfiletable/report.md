---
layout: page
title: "Sherlock: HyperFileTable - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-07-hyperfiletable/report/
---

![HyperFileTable cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-07-hyperfiletable.png)

# HyperFileTable

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `hyperfiletable.pdf` |
| Pages | 5 |
| Difficulty | Easy |
| Prepared by | Blitztide |
| Author | (s): Blitztide |

## Scenario Summary

There has been a new joininer in Forela, they have downloaded their onboarding
documentation, however someone has managed to phish the user with a malicious
attachment.
Artefacts Provided
HyperFileTable.zip - 9070aa868d6f0592c838be2f52cc185320b1a90b

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `hyperfiletable.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |
| PowerShell | Used or likely relevant based on the source writeup |

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
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Add lessons learned after completing the investigation.

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

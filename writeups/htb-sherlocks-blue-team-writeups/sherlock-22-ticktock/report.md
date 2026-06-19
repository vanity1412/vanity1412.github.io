---
layout: page
title: "Sherlock: TickTock - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-22-ticktock/report/
---

![TickTock cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-22-ticktock.png)

# TickTock

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `ticktock.pdf` |
| Pages | 14 |
| Difficulty | Medium |
| Prepared by | sebh24 |
| Author | (s): Blitztide |

## Scenario Summary

Gladys is a new joiner in the company, she has recieved an email
informing her that the IT department is due to do some work on her PC,
she is guided to call the IT team where they will inform her on how to
allow them remote access. The IT team however are actually a group of
hackers that are attempting to attack Forela.
Description
In this Sherlock, you find yourself investigating a potential spear-
phishing attack against Forela. Gladys, a new employee, has received an
email supposedly from the IT department, asking her to provide them with
remote access to her PC for maintenance. Unbeknownst to Gladys, the 'IT
team' is in reality a group of hackers posing as internal staff to
infiltrate Forela's systems. Your mission is to assess the nature and
extent of this attempted attack, identify any potential breaches in
security that may have occurred, and establish defensive measures to
prevent such occurrences in the future. This challenge will test your
ability to analyze communication trails, spot phishing tactics, and
effectively investigate a complex attack.
Artefacts Provided
Enter the artefacts provided along with their file hash here.
ticktock.zip -
1cb5d3267271978ed0bd1eb0d667932e59a45aa8daa8a330e4fd62d6e80c6f4a
Containing a KAPE output

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `ticktock.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |
| PowerShell | Used or likely relevant based on the source writeup |
| Windows Event Logs | Used or likely relevant based on the source writeup |
| Sysmon | Used or likely relevant based on the source writeup |
| Splunk | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |

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
| Exfiltration | Exfiltration Over Web Service | Observed in extracted case notes; validate with report evidence. |
| Impact | Data Encrypted for Impact | Observed in extracted case notes; validate with report evidence. |

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

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.






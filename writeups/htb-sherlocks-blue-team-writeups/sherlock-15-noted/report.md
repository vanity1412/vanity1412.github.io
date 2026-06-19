---
layout: page
title: "Sherlock: Noted - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-15-noted/report/
---

# Noted

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Noted.pdf` |
| Pages | 8 |
| Difficulty | Easy |
| Prepared by | Cyberjunkie & Sebh24 |
| Author | (s): Cyberjunkie |

## Scenario Summary

Simon, a developer working at forela notified the CERT team about a note appearing on
his desktop which claims that his system was compromised and they collected all
sensitive data from simon's workstation. They performed data extortion on his
workstation and are now threatening to release the data on dark web unless their
demands are met. Simon had multiple sensitive files like planned software works,
internal development plans and code base of applications.The threat intelligence team
beleives that the threat actor made some mistakes and the TI team cannot find any way
to contact threat actors. The company stakeholders really need this incident to be
handled and all the sensitive data back. They are demanding that no matter what, the
data should not be leaked.
Since you are our junior security analyst , you are assigned only a specific type of
dfir investigation regarding this case. The CERT lead triaged the workstation and
provided you only with notepad++ artifacts, since he suspected that attacker created
extortion note and other extortion activities with hands-on keyboard access. Now its
your duty to find out how the attack happened and find a way to get in contact with
threat actors as they accidently locked out their information on how to contact them.
Artefacts provided
1- Noted.zip md5 : 528F1181FCE7B59E311F1FAA0D88E316
Skills Learnt
Windows Forensics
Data Extortion
OSINT
IOC Gathering
Ransom

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `Noted.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
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

Windows Forensics
Notepad ++
Incident Response

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

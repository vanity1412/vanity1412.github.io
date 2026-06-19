---
layout: page
title: "Sherlock: einladen - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-06-einladen/report/
---

![einladen cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-06-einladen.png)

# einladen

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `einladen.pdf` |
| Pages | 12 |
| Difficulty | Medium |
| Prepared by | Sebh24 |
| Author | (s): thewhitefriday |

## Scenario Summary

Our staff recently received an invite to the German embassy to bid farewell to
the Germany Ambassador. We believe this invite was a phishing email due to alerts
that fired on our organisation's SIEM tooling following the receipt of such mail.
We have provided a wide variety of artifacts inclusive of numerous binaries, a
network capture, DLLs from the host system and also a .hta file. Please analyse
and complete the questions detailed below!
Analysis
As usual, we download the relevant zip file, unzip and then confirm the contents:
(sebh24maroc)-[~/Desktop/einladen]
$ ls -alh
total 19M
drwxr-xr-x 2 sebh24 sebh24 4.0K Apr 4 16:56 .
drwxr-xr-x 8 sebh24 sebh24 4.0K Apr 4 16:56 ..
-rw-r--r-- 1 sebh24 sebh24 2.5K Jul 28 2023 AppVIsvSubsystems64.dll
-rw-r--r-- 1 sebh24 sebh24 294K Aug 12 2023 downloader.html
-rw-r--r-- 1 sebh24 sebh24 62K Aug 30 2023 EmpireClient.exe
-rw-r--r-- 1 sebh24 sebh24 295K Jul 28 2023 Invitation_Farewell_DE_EMB.hta
-rw-r--r-- 1 sebh24 sebh24 82K Aug 30 2023 Invitation_Farewell_DE_EMB.zip
-rw-r--r-- 1 sebh24 sebh24 25K Jul 28 2023 Invitation.pdf
-rw-r--r-- 1 sebh24 sebh24 15M Aug 16 2023 Logfile.PML
-rw-r--r-- 1 sebh24 sebh24 33K Jul 28 2023 mso.dll
-rw-r--r-- 1 sebh24 sebh24 59K Jul 28 2023 msoev.exe
-rw-r--r-- 1 sebh24 sebh24 53K Aug 16 2023 msoev.pcapng
-rw-r--r-- 1 sebh24 sebh24 2.7M Aug 9 2023 sheet.hta
-rw-r--r-- 1 sebh24 sebh24 174K Aug 30 2023 unc.js
We are provided with a brief of the incident which highlights an invite to the German embassy.
Taking this into account we initially open the HTML file using the web browser of our choice. This
will ask

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `einladen.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| Zeek | Used or likely relevant based on the source writeup |
| CyberChef | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |
| strings | Used or likely relevant based on the source writeup |
| VirusTotal | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

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
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
| Defense Evasion | Obfuscated Files or Information | Observed in extracted case notes; validate with report evidence. |

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

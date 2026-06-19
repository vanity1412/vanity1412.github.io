---
layout: page
title: "Sherlock: Jingle Bell - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-08-jingle-bell/report/
---

# Jingle Bell

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `jinglebell.pdf` |
| Pages | 8 |
| Difficulty | Easy |
| Prepared by | VivisGhost |
| Author | CyberJunkie |

## Scenario Summary

Torrin is suspected to be an insider threat in Forela. He is believed to
have leaked some data and removed certain applications from their
workstation. They managed to bypass some controls and installed
unauthorised software. Despite the forensic team's efforts, no evidence
of data leakage was found. As a senior incident responder, you have been
tasked with investigating the incident to determine the conversation
between the two parties involved.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

jinglebell.zip -
4d857dd670e8f91479e201cd564dacc6480384c323735309f4ad8c0ab2a97ad9
Skills Learnt
Extracting forensic evidence from Windows Notifications
Analyzing SQLite databases
Investigating insider threats

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: Which software/application did Torrin use to leak Forela's secrets?
- Analysis note: Launch slack:channel and invitation to join Slack are good indications of the
application.
- Answer: `Slack`
### Question 2: What's the name of the rival company to which Torrin leaked the data?
- Answer: `PrimeTech Innovations`
### Question 3: What is the username of the person from the competitor organization whom Torrin shared
information with?
- Analysis note: Answer found in same Notification as question #2.
- Answer: `Cyberjunkie-PrimeTechDev`
### Question 4: What's the channel name in which they conversed with each other?
- Answer: `forela-secrets-leak`
### Question 5: What was the password for the archive server?
- Analysis note: Answer found in same Notification as question #4.
- Answer: `Tobdaf8Qip$re@1`
### Question 6: What was the URL provided to Torrin to upload stolen data to?
- Answer: `https://drive.google.com/drive/folders/1vW97VBmxDZUIEuEUG64g5DLZvFP-`
### Question 7: When was the above link shared with Torrin?
- Analysis note: Going to https://www.epochconverter.com/ we can convert the time to UTC.
- Answer: `2023-04-20 10:34:49`
### Question 8: For how much money did Torrin leak Forela's secrets?
- Answer: `10000`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Which software/application did Torrin use to leak Forela's secrets? | Slack |
| What's the name of the rival company to which Torrin leaked the data? | PrimeTech Innovations |
| What is the username of the person from the competitor organization whom Torrin shared
information with? | Cyberjunkie-PrimeTechDev |
| What's the channel name in which they conversed with each other? | forela-secrets-leak |
| What was the password for the archive server? | Tobdaf8Qip$re@1 |
| What was the URL provided to Torrin to upload stolen data to? | https://drive.google.com/drive/folders/1vW97VBmxDZUIEuEUG64g5DLZvFP- |
| When was the above link shared with Torrin? | 2023-04-20 10:34:49 |
| For how much money did Torrin leak Forela's secrets? | 10000 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Initial Access | Phishing: Spearphishing Attachment/Link | Observed in extracted case notes; validate with report evidence. |
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
| Exfiltration | Exfiltration Over Web Service | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Windows Forensics
Incident Response

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

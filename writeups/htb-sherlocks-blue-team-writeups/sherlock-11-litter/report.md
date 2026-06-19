---
layout: page
title: "Sherlock: litter - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-11-litter/report/
---

# litter

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `litter.pdf` |
| Pages | 12 |
| Difficulty | Easy |
| Prepared by | sebh24 |
| Author | (s): Broomey28 |

## Scenario Summary

Khalid has just logged onto a host that he and his team use as a testing host for many different
purposes, its off their corporate network but has access to lots of resources in network. The host
is used as a dumping ground for a lot of people at the company but its very useful, so no one has
raised any issues.
Little does Khalid know; the machine has been compromised and company information that
should not have been on there has now been stolen its up to you to figure out what has
happened and what data has been taken.
Artefacts Provided
suspicious_traffic.pcap - 98c26da32ebc0518f327636f5bad777d
Tools Used:
Brim
Brim is an open-source desktop application designed to provide an intuitive interface for
exploring data in various formats, including network captures (pcaps) and logs. It utilizes the
powerful Zed system for analytics and storage, offering efficient search and data
transformation capabilities. Brim comes with integrated visualizations, making it easier to
analyze network traffic patterns and dig into detailed packet information. It's an excellent tool
for security professionals and network administrators who need to navigate large datasets
with a combination of structured and unstructured data.
Wireshark
Wireshark is the most widely known and used network protocol analyzer. It allows you to
capture and interactively browse the traffic running on a computer network. It has a rich
feature set that includes deep inspection of hundreds of protocols, live capture and offline
analysis, and VoIP analysis. Wireshark's powerful filtering and search capabilities make it an

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `litter.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| Zeek | Used or likely relevant based on the source writeup |
| CyberChef | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: At a glance, what protocol seems to be suspect in this attack?
- Answer: `DNS`
### Question 2: There seems to be a lot of traffic between our host and another, what is the IP address of the
suspect host?
- Answer: `192.168.157.145`
### Question 3: What is the first command the attacker sends to the client?
- Answer: `whoami`
### Question 4: What is the version of the DNS tunneling tool the attacker is using?
- Answer: `0.07`
### Question 5: The attackers attempts to rename the tool they accidentally left on the clients host. What do
they name it to?
- Answer: `win_installer.exe`
### Question 6: The attacker attempts to enumerate the users cloud storage. How many files do they locate
in their cloud storage directory?
- Answer: `No`
### Question 7: What is the full location of the PII file that was stolen?
- Analysis note: (Format: C:\path\to\file\file.ext)
- Answer: `C:\users\test\documents\client data optimisation\ user details.csv`
### Question 8: Exactly how many customer PII records were stolen?
- Analysis note: (format: integer e.g 65)
- Answer: `721`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| At a glance, what protocol seems to be suspect in this attack? | DNS |
| There seems to be a lot of traffic between our host and another, what is the IP address of the
suspect host? | 192.168.157.145 |
| What is the first command the attacker sends to the client? | whoami |
| What is the version of the DNS tunneling tool the attacker is using? | 0.07 |
| The attackers attempts to rename the tool they accidentally left on the clients host. What do
they name it to? | win_installer.exe |
| The attacker attempts to enumerate the users cloud storage. How many files do they locate
in their cloud storage directory? | No |
| What is the full location of the PII file that was stolen? | C:\users\test\documents\client data optimisation\ user details.csv |
| Exactly how many customer PII records were stolen? | 721 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Initial Access | Phishing: Spearphishing Attachment/Link | Observed in extracted case notes; validate with report evidence. |
| Execution | Command and Scripting Interpreter | Observed in extracted case notes; validate with report evidence. |
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

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

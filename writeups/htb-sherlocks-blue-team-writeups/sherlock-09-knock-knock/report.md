---
layout: page
title: "Sherlock: Knock Knock - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-09-knock-knock/report/
---

# Knock Knock

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `knockknock.pdf` |
| Pages | 18 |
| Difficulty | Medium |
| Prepared by | sebh24 |
| Author | (s): CyberJunkie |

## Scenario Summary

A critical Forela Dev server got targeted by a ransomware. The Dev server was
accidently left open to internet which it was not supposed to be. The senior dev
Abdullah told the IT team that the server was fully hardened and it's still
difficult to comprehend how did the attack took place and how the attacker got
access in the first place. Forela recently started its business expansion in
Pakistan and Abdullah was the one IN charge of all infrastructure deployment and
management. The Security Team need to contain and remediate the threat as soon as
possible as any more damage can be devastating for the company especially at the
crucial stage of expanding in other region.
Thankfully a packet capture tool was running in the subnet which was setup few
months ago. A packet capture is provided to you of around the time of incident
(1-2) days margin because we dont know exactly when attacker got access. As our
forensics analyst, you have been provided the packet capture to analyze how
attacker got access.
Artefacts provided
Capture.pcap 85D7DCBC8764A8422AE1F1C3E069FF87
Skills Learnt
Network Forensics
PCAP Analysis
Wireshark filters
Data recovery
Network telemetry correlation with incidents

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `knockknock.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| Zeek | Used or likely relevant based on the source writeup |
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

Network Forensics
OSINT (Open Source Intelligence)
PCAP Analysis
Incident Response
Analysis
Whenever we receive an artefact as part of an incident response investigation our standard we
verify that the hash is identical to the hash provided by the tool or team who initially collected.
md5sum Capture.pcap
Rather than immediately opening the PCAP in Wireshark, or attempting to parse within tcpdump
we instead open up the network capture in a tool called Network Miner. Network Miner is a
popular network forensic analysis tool that helps in capturing and analyzing network traffic. It
works by parsing packet capture (PCAP) files and extracts useful information like hostnames, open
ports, operating systems, services running on the network, etc. It then presents this information in
a user-friendly graphical interface, making it easier for incident responders to quickly identify
potential security threats and malicious activities in the network.
Network Miner is useful for incident response for several reasons. Firstly, it allows incident
responders to quickly identify which hosts on the network are communicating with each other and
what type of traffic is being exchanged. This information can be used to identify potential security
threats, such as unauthorised access attempts or data exfiltration.
When we navigate to the "Files" tab in order to get a view of any "low hanging fruit". In data
analysis, low hanging fruit might refer to quick and easy data visualisations or summary statistics
that can provide initial insights into a data set. This might include simple methods of gainin

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

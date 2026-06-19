---
layout: page
title: "Sherlock: Compromised - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-02-compromised/report/
---

![Compromised cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-02-compromised.png)

# Compromised

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Compromised.pdf` |
| Pages | 9 |
| Difficulty | Easy |
| Prepared by | VivisGhost |
| Author | Abdelrhman |

## Scenario Summary

Our Security Operations Center (SOC) has detected unusual and potentially
malicious network activity. As a security analyst, your task is to
investigate the suspicious traffic, identify the root cause, and
recommend appropriate remediation steps.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

compromized.zip -
f6d51e9d768a0940aa8c484a3e38b8a19de300cae30d2a04822a960cd09c2ca3
Skills Learnt
Network traffic analysis
Utilizing threat intelligence deeds to validate findings

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| VirusTotal | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What is the IP address used for initial access?
- Analysis note: We found this answer in our intial analysis when checking out the 6ctf5JL file.
- Answer: `162.252.172.54`
### Question 2: What is the SHA256 hash of the malware?
- Answer: `9b8ffdc8ba2b2caa485cca56a82b2dcbd251f65fb30bc88f0ac3da6704e4d3c6`
### Question 3: What is the Family label of the malware?
- Analysis note: We found this information on VirusTotal during the initial analysis.
- Answer: `Pikabot`
### Question 4: When was the malware was first seen in the wild (UTC)?
- Analysis note: This detail was retrieved from VirusTotal.
- Answer: `2023-05-19 14:01:21`
### Question 2: Cross-reference threat-hunting feeds to confirm associated IOCs.
- Analysis note: When examining the PCAP we looked for instances where the issuer and subject
were identical, indicating a self-signed certificate.
Compare that to this Digicert signed certificate for Twitter.
Now having an idea of what we are looking for in the PCAP we can compare these findings
to threat intelligence.
Taking a look from this GitHub repositiory we can see some similar IPs.
https://github.com/pr0xylife/Qakbot/blob/ma
- Answer: `2078, 2222, 32999`
### Question 6: What is the id-at-localityName of the self-signed certificate associated with the first
malicious IP?
- Analysis note: Similar to the previous question, we checked the packets in the PCAP file and validated
this information with threat intelligence sources.
- Answer: `Pyopneumopericardium`
### Question 7: What is the notBefore time(UTC) for this self-signed certificate?
- Analysis note: This was answered in the previous question.
- Answer: `2023-05-14 08:36:52 UTC`
### Question 8: What was the domain used for tunneling?
- Analysis note: We located the domain in both the PCAP file and Unit42's threat hunting GitHub. A final
review of the threat intelligence information confirmed the domain has been observed in
similar incidents.
https://github.com/PaloAltoNetworks/Unit42-timely-threat-
intel/blob/main/2023-05-17-IOCs-for-Pikabot-with-Cobalt-Strike.txt
- Answer: `steasteel.net`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What is the IP address used for initial access? | 162.252.172.54 |
| What is the SHA256 hash of the malware? | 9b8ffdc8ba2b2caa485cca56a82b2dcbd251f65fb30bc88f0ac3da6704e4d3c6 |
| What is the Family label of the malware? | Pikabot |
| When was the malware was first seen in the wild (UTC)? | 2023-05-19 14:01:21 |
| Cross-reference threat-hunting feeds to confirm associated IOCs. | 2078, 2222, 32999 |
| What is the id-at-localityName of the self-signed certificate associated with the first
malicious IP? | Pyopneumopericardium |
| What is the notBefore time(UTC) for this self-signed certificate? | 2023-05-14 08:36:52 UTC |
| What was the domain used for tunneling? | steasteel.net |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
| Discovery | System / Network Discovery | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Incident response
Network forensics

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

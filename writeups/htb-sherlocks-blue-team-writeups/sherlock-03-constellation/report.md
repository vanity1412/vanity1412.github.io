---
layout: page
title: "Sherlock: Constellation - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-03-constellation/report/
---

![Constellation cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-03-constellation.png)

# Constellation

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `constellation.pdf` |
| Pages | 18 |
| Difficulty | Medium |
| Prepared by | CyberJunkie |
| Author | (s): CyberJunkie |

## Scenario Summary

SOC team was recently made aware of a possible insider threat
existence. The suspect employee's workstation was contained and
triaged.During memory analysis, Senior DFIR Analyst was able to carve
out some interesting urls from the memory. You are provided this
evidence to further analyse these and try to find any evidence like
evidence of data exfiltration, evidence of contact with malicious
entities and so on.
You will be working closely with threat intel team if you find any
information regarding the attacking group or individuals invovled .
You will also be in touch with Forensics team, helping them in
timeline creation
Artefacts provided
1- IOCs.txt (txt file), sha1 : D94F86578DED38A794E16D2BACEC124669B2FF99
Skills Learnt
URL Analysis
Timeline creation
Metadata analysis
OSINT (tracking opsec mistakes)
Contextual Analysis
Chaining of multiple Artefacts

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `constellation.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
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
| Initial Access | Phishing: Spearphishing Attachment/Link | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
| Exfiltration | Exfiltration Over Web Service | Observed in extracted case notes; validate with report evidence. |
| Defense Evasion | Obfuscated Files or Information | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

DFIR
Incident Response
Initial Analysis :
We will start by extracting the provided zip file. We see it contains a single txt file named
IOCs.
Lets open it to see what IOCs are provided.
It looks like we are provided with 2 URLs. The first url looks like a discord attachment link
which upon visiting downloads a pdf file named NDA_Instructions.pdf.
Lets open this pdf.
It looks like some kind of instructions. Upon reading this we find that this pdf was delivered
to karen riley whos forela employee. And she is about to perform sabotage and sell
sensitive information to a Threat actor group possibly by name of "AntiCorp Gr04p". They
are being given instructions on how to collect and exfill data via s3 buckets.
Now lets take a look at second URL. Its a google search url and going to the urls gives us
this result
So far we dont know what to make of these urls. Just from context we know that the
discord attachment and this google search url are connected because we saw some
archive instructions using tar in the pdf file, and it looks like karen had some problems
doing that so she used google for help.
Before diving into the questions answers, if we take a quick look at questions they demand
answers like timestamps and other information which all look overwhelming because we
only have 2 urls as artifacts and nothing more. Well here comes the learning curve for this
sherlock. We will utilise a tool called unfurl which gives forensically important information
and parses out so much information just from a single URL!!!!!!!.
Questions and Answers :
Q1 When did the suspect first started

## Conclusion

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.







---
layout: page
title: "Sherlock: LockPick 2.0 - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-12-lockpick-2-0/report/
---

# LockPick 2.0

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `lockpick2.pdf` |
| Pages | 10 |
| Difficulty | Hard |
| Prepared by | blitztide |
| Author | (s): sebh24 |

## Scenario Summary

We've been hit by Ransomware again, but this time the threat actor seems to have
upped their skillset. Once again a they've managed to encrypt a large set of our
files. It is our policy NOT to negotiate with criminals. Please recover the files
they have encrypted - we have no other option! Unfortunately our CEO is on a no-
tech retreat so can't be reached. Warning This is a warning that this Sherlock
includes software that is going to interact with your computer and files. This
software has been intentionally included for educational purposes and is NOT
intended to be executed or used otherwise. Always handle such files in isolated,
controlled, and secure environments. One the Sherlock zip has been unzipped, you
will find a DANGER.txt file. Please read this to proceed.
Warning
This is a warning that this Sherlock includes software that is going to interact with your computer
and files. This software has been intentionally included for educational purposes and is NOT
intended to be executed or used otherwise. Always handle such files in isolated, controlled, and
secure environments.
One the Sherlock zip has been unzipped, you will find a DANGER.txt file. Please read this to
proceed.
The analysis in this Sherlock has been performed in an isolated (from work/personal devices)
network with a live internet connection.
Artefacts Provided
lockpick2.zip - 4a9765cfc4c7faec1f64bd07daa76a08e6c8742d3fcec1cb976b4e42a04357d8

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `lockpick2.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| CyberChef | Used or likely relevant based on the source writeup |
| strings | Used or likely relevant based on the source writeup |
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
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
| Discovery | System / Network Discovery | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
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

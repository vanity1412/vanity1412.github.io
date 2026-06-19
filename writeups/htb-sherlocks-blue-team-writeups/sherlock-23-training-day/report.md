---
layout: page
title: "Sherlock: Training Day - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-23-training-day/report/
---

![Training Day cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-23-training-day.png)

# Training Day

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `TrainingDay.pdf` |
| Pages | 12 |
| Difficulty | Easy |
| Prepared by | iamroot |
| Author | (s): Megachar0x01 |

## Scenario Summary

A fresh new day, a well-rested cybersecurity professionalready to
learn something new after a chaotic week. Scrolling through
challenges, they stumble upon TrainingDay, download the artifacts, and
boomthree different binaries, each doing its own thing. Do they
panic? Nope. This is exactly what they signed up forsome good old-
fashioned reversing fun. If this sounds like you, what are you waiting
for? Grab your debugger and dive in!

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Enter the artifacts provided along with their file hash here.
argument_baby_1.exe - 71AA9BFA63B6F5262305030012CDD366
argument_baby_2.exe - 0E607DABF9F4AD503A0CECFE985DE6C2
argument_baby_3.exe - 75199A70DC118D0157C3380187C7ACEC
Skills Learnt
Basics of reversing.
Players will learn different calling conventions.
basics of reversing.

## Tools Used

| Tool | Purpose |
| --- | --- |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What is sha256sum hash of argument_baby_1.exe ?
- Answer: `dc6267608ddfcc5c80571ccd46475a03fb667baf8620d0e91c93ccacacf97ef6`
### Question 2: Can you find development enviroment of malware author (e.g:ide) ?
- Answer: `visual studio`
### Question 3: What CPU architecture was argument_baby_1.exe compiled for ?
- Answer: `32 bit`
### Question 4: Is argument_baby_1.exe a symbol-stripped binary?
- Answer: `false`
### Question 5: Retrieve the full PDB file path from the debug information of
- Analysis note: argument_baby_1.exe
- Answer: `C:\Users\HTB\Desktop\argument\Release\argument.pdb`
### Question 6: The malware author was using a Windows OS. What was the associated
username?
- Answer: `HTB`
### Question 7: What calling convention is used in argument_baby_1.exe ?
- Answer: `cdecl`
### Question 8: How is the 1st argument passed to the function in argument_baby_1.exe?
- Answer: `esp`
### Question 9: How is the 2nd argument passed to the function in argument_baby_1.exe?
- Answer: `esp+4`
### Question 10: How is the 3rd argument passed to the function in argument_baby_1.exe?
- Answer: `esp+8`
### Question 11: How is the 4th argument passed to the function in argument_baby_1.exe?
- Answer: `esp+c`
### Question 12: How is the 5th argument passed to the function in argument_baby_1.exe?
- Answer: `esp+10`
### Question 13: Which CPU register holds the function's return value in argument_baby_1.exe?
- Answer: `eax`
### Question 14: What calling convention is used in argument_baby_2.exe ?
- Answer: `fastcall`
### Question 15: How is the 1st argument passed to the function in argument_baby_2.exe?
- Answer: `ecx`
### Question 16: How is the 2nd argument passed to the function in argument_baby_2.exe?
- Answer: `edx`
### Question 17: How is the 3rd argument passed to the function in argument_baby_2.exe?
- Answer: `esp`
### Question 18: How is the 4th argument passed to the function in argument_baby_2.exe?
- Answer: `esp+4`
### Question 19: How is the 5th argument passed to the function in argument_baby_2.exe?
- Answer: `esp+8`
### Question 20: What CPU architecture was argument_baby_3.exe compiled for ?
- Answer: `64 bit`
### Question 21: How is the 1st argument passed to the function in argument_baby_3.exe?
- Answer: `rcx`
### Question 22: How is the 2nd argument passed to the function in argument_baby_3.exe?
- Answer: `rdx`
### Question 23: How is the 3rd argument passed to the function in argument_baby_3.exe?
- Answer: `r8`
### Question 24: How is the 4th argument passed to the function in argument_baby_3.exe?
- Answer: `r9`
### Question 25: How is the 5th argument passed to the function in argument_baby_3.exe?
- Answer: `rsp+20`
### Question 26: In the case of argument_baby_3.exe, which CPU register stores the function's
return value?
- Answer: `rax`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What is sha256sum hash of argument_baby_1.exe ? | dc6267608ddfcc5c80571ccd46475a03fb667baf8620d0e91c93ccacacf97ef6 |
| Can you find development enviroment of malware author (e.g:ide) ? | visual studio |
| What CPU architecture was argument_baby_1.exe compiled for ? | 32 bit |
| Is argument_baby_1.exe a symbol-stripped binary? | false |
| Retrieve the full PDB file path from the debug information of | C:\Users\HTB\Desktop\argument\Release\argument.pdb |
| The malware author was using a Windows OS. What was the associated
username? | HTB |
| What calling convention is used in argument_baby_1.exe ? | cdecl |
| How is the 1st argument passed to the function in argument_baby_1.exe? | esp |
| How is the 2nd argument passed to the function in argument_baby_1.exe? | esp+4 |
| How is the 3rd argument passed to the function in argument_baby_1.exe? | esp+8 |
| How is the 4th argument passed to the function in argument_baby_1.exe? | esp+c |
| How is the 5th argument passed to the function in argument_baby_1.exe? | esp+10 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Execution | Command and Scripting Interpreter | Observed in extracted case notes; validate with report evidence. |
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
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

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.






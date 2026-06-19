---
layout: page
title: "Sherlock: Loggy - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-13-loggy/report/
---

![Loggy cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-13-loggy.png)

# Loggy

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Loggy.pdf` |
| Pages | 12 |
| Difficulty | Easy |
| Prepared by | WibblyWobbly + VivisGhost |
| Author | Unknown |

## Scenario Summary

Janice from accounting is beside herself! She was contacted by the SOC to
tell her that her work credentials were found on the dark web by the
threat intel team. They investigated and scanned her machine but couldnt
find any malicious activity. She changed her password anyway as a
precaution, but she was contacted by the SOC that her credentials were
shared on the dark web again! This time, during the investigation, it was
discovered that she was using a screenshot tool she found on a sketchy
site. The forensic team managed to recover the suspicious executable and
some files and gave it to their malware reverse engineer to analyze.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Loggy.zip - 4226e5f90a5dc89807d001986ae78f00e2549dbb7c57d6165e93c9478de8b3e6
Loggy.exe -
6acd8a362def62034cbd011e6632ba5120196e2011c83dc6045fcb28b590457c
keylog.txt -
7dfb5222834c48e00ad25e66a521ca13c8dd4ee4bd2aeee06ff9c20ea40b238d
screenshot_1718068575.png -
54c190d80e6c2c8f41ada58c293f0cd6a509710a8d6de22e77c0b20055ceef2f
screenshot_1718068581.png -
f0fbd9cf8bb1b068067419d1fd8c454b45d9d11ac574e731c00c95366b45a86d
screenshot_1718068593.png -
8f531c1511572e5e6af70a1c822e4d0659f8cf8c5e6e84e63066559eb57c3102
screenshot_1718068600.png -
7e29f8d7c4495e91559108d2bf004f8ba20046b47015ec0d2a98a73d408cd8a1
Skills Learnt
Malware Analysis

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| strings | Used or likely relevant based on the source writeup |
| Ghidra | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What is the SHA-256 hash of this malware binary?
- Analysis note: We can use the following command to get the hash.
sha256sum Loggy.exe
- Answer: `6acd8a362def62034cbd011e6632ba5120196e2011c83dc6045fcb28b590457c`
### Question 2: What programming language (and version) is this malware written in?
- Analysis note: In the initial analysis we were able to see it was a Go binary. We can use go version -m
to get its version and dependencies.
We can see the version, dependencies and build; exe, Windows OS and amd64
architecture.
- Answer: `Golang 1.22.3`
### Question 3: There are multiple GitHub repos referenced in the static strings. Which GitHub repo
would be most likely suggest the ability of this malware to exfiltrate data?
- Analysis note: Building upon the initial analysis, with static strings I typically CTRL+F with common top-
level domains (.com, .net, .ru, .cn), the github string, and common internet protocols
(http, https, ftp, sftp). This produces fruitful results:
This can also be found in the version command from question #2.
- Answer: `github.com/jlaffaye/ftp`
### Question 4: What dependency, expressed as a GitHub repo, supports Janices assertion that she
thought she downloaded something that can just take screenshots?
- Analysis note: Also, I see a reason to believe that Janice thought she was downloading a program
designed to take screenshots:
This can also be found in the version command from question #2.
- Answer: `github.com/kbinani/screenshot`
### Question 5: Which function call suggests that the malware produces a file after execution?
- Analysis note: To get an idea of the malwares functionality, I check the imports. Interesting to note is
WriteFile, which suggests that this malware writes something to disk:
- Answer: `WriteFile`
### Question 6: You observe that the malware is exfiltrating data over FTP. What is the domain it is
exfiltrating data to?
- Analysis note: For dynamic analysis, I will finally detonate the malware. After detonation I immediately
check Wireshark in my REMnux VM.
I see an interesting DNS query:
We can also find this with static analysis.
With Go binaries, the main functionality of the program is often in main.main . Opening
the executable in Ghidra and navigating to main.main a couple functions stick out.
logKeystokes - line 71
captureScreenshots - line 7
- Answer: `gotthem.htb`
### Question 7: What are the threat actors credentials?
- Analysis note: Continuing with the dynamic analysis and considering the hints at FTP functionality in the
static strings, I look for FTP requests within Wireshark, and I find:
We have threat actor credentials!
This could also be found with static analysis in the same function as shown in the previous
question. Here we can see the password on line 108 and the username on line 110.
- Answer: `NottaHacker:Cle@rtextP@ssword`
### Question 8: What file keeps getting written to disk?
- Analysis note: When I look at Process Monitor, I see that a single file keeps getting written to disk:
- Answer: `keylog.txt`
### Question 9: When Janice changed her password, this was captured in a file. What is Janice's
username and password?
- Analysis note: When I open up the keylog.txt file, I can see that Janice entered her username and
password. The first highlight shows that her username was entered with all lowercase
characters. The second highlight shows that Janice entered her password with an
uppercase "P" due to the use of the SHIFT key right before entering it:
- Answer: `janice:Password123`
### Question 10: What app did Janice have open the last time she ran the "screenshot app"?
- Analysis note: When I open up the screenshots, I can see what Janice is working on while on the job:
- Answer: `Solitaire`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What is the SHA-256 hash of this malware binary? | 6acd8a362def62034cbd011e6632ba5120196e2011c83dc6045fcb28b590457c |
| What programming language (and version) is this malware written in? | Golang 1.22.3 |
| There are multiple GitHub repos referenced in the static strings. Which GitHub repo
would be most likely suggest the ability of this malware to exfiltrate data? | github.com/jlaffaye/ftp |
| What dependency, expressed as a GitHub repo, supports Janices assertion that she
thought she downloaded something that can just take screenshots? | github.com/kbinani/screenshot |
| Which function call suggests that the malware produces a file after execution? | WriteFile |
| You observe that the malware is exfiltrating data over FTP. What is the domain it is
exfiltrating data to? | gotthem.htb |
| What are the threat actors credentials? | NottaHacker:Cle@rtextP@ssword |
| What file keeps getting written to disk? | keylog.txt |
| When Janice changed her password, this was captured in a file. What is Janice's
username and password? | janice:Password123 |
| What app did Janice have open the last time she ran the "screenshot app"? | Solitaire |

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

Malware Analysis
Golang

## Conclusion

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.






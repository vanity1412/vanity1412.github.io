---
layout: page
title: "Sherlock: Psittaciformes - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-19-psittaciformes/report/
---

![Psittaciformes cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-19-psittaciformes.png)

# Psittaciformes

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Psittaciformes.pdf` |
| Pages | 16 |
| Difficulty | Easy |
| Prepared by | VivisGhost |
| Author | sebh24 |

## Scenario Summary

Forela carry out penetration testing of their internal networks utilising
an internal team within their security department. The security team have
notes from tests in addition to company critical credentials. It seems
their host may have been compromised. Please verify how this occurred
using the retrospective collection provided.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Psittaciformes.zip -
4aa1724d1bcbf6cff55b4953d85ca29f01105b5a5ee367422ff4c81f33854de7
Skills Learnt
Shell Script Code Review
GitHub Commit Review

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |
| VirusTotal | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 3: Unzip file.
- Analysis note: The output file defined on line 4 resembles what we found in full-timeline.csv
We can try using the same methods in the script to download the ZIP file ourselves.
Unzipping the file with the password from line 8 and running sha1sum we get the same
hash found in the initial analysis.
From here we can conclude that the autoenum repository was responsible for delivering
the malicious blob .
- Answer: `autoenum`
### Question 2: What is the name of the malicious function within the script ran by the Pen Tester?
- Analysis note: Can see this on line 1 in the second screenshot from the first question.
- Answer: `do_wget_and_run`
### Question 3: What is the password of the zip file downloaded within the malicious function?
- Analysis note: From the original screenshot line 6-8 define the password. We can replicate it locally with
the following.
- Answer: `superhacker`
### Question 4: What is the full URL of the file downloaded by the attacker?
- Analysis note: This can be found on lines 2 and 3 in the second screenshot from the first question .
- Answer: `https://www.dropbox.com/scl/fi/uw8oxug0jydibnorjvyl2/blob.zip?`
### Question 5: When did the attacker finally take out the real comments for the malicious function?
- Analysis note: To investigate previous versions of the file we used git clone , to clone the repository to
our local machine.
To view the differences between file versions, we used the git log command withe the
-p and --pretty=fuller options.
-p : Displays the patch introduced in each comment, showing line-by-line changes.
--pretty=fuller : Provides detailed metadata for each commit.
Continuing to review the log, we identified a sp
- Answer: `2024-12-23 22:27:58`
### Question 6: The attacker changed the URL to download the file, what was it before the change?
- Answer: `https://www.dropbox.com/scl/fi/wu0lhwixtk2ap4nnbvv4a/blob.zip?`
### Question 7: What is the MITRE technique ID utilized by the attacker to persist?
- Analysis note: Continuing on in the enum.sh code on line 58 we can see the crontab entry(seen in
initial analysis).
Looking up the corresponding MITRE
https://attack.mitre.org/techniques/T1053/003/
- Answer: `T1053.003`
### Question 8: What is the name of the technique relevant to the binary the attacker runs?
- Analysis note: Mentioned in the initial analysis, running the blob binary hash on VirusTotal we found it was
a crypto miner.
Additionally, the dropbox ZIP file which delivered the malicious blob also contained a
config.json Looking into the file below we see more evidence of a crypto miner.
"pools" typically specify the network the malware will connect to, "coin":"XMR"
signifies the coin is Monero and the "url" again suggests Moner
- Answer: `T1496`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Unzip file. | autoenum |
| What is the name of the malicious function within the script ran by the Pen Tester? | do_wget_and_run |
| What is the password of the zip file downloaded within the malicious function? | superhacker |
| What is the full URL of the file downloaded by the attacker? | https://www.dropbox.com/scl/fi/uw8oxug0jydibnorjvyl2/blob.zip? |
| When did the attacker finally take out the real comments for the malicious function? | 2024-12-23 22:27:58 |
| The attacker changed the URL to download the file, what was it before the change? | https://www.dropbox.com/scl/fi/wu0lhwixtk2ap4nnbvv4a/blob.zip? |
| What is the MITRE technique ID utilized by the attacker to persist? | T1053.003 |
| What is the name of the technique relevant to the binary the attacker runs? | T1496 |

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

GitHub Analysis
Cryptojacking

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

---
layout: page
title: "Sherlock: Team Work - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-21-team-work/report/
---

![Team Work cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-21-team-work.png)

# Team Work

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `TeamWork.pdf` |
| Pages | 16 |
| Difficulty | Easy |
| Prepared by | achille |
| Author | (s): achille |

## Scenario Summary

It is Friday afternoon and the SOC at Edny Consulting Ltd has received alerts from the
workstation of Jason Longfield, a software engineer on the development team, regarding the
execution of some discovery commands. Jason has just gone on holiday and is not available
by phone.The workstation appears to have been switched off, so the only evidence we have at
the moment is an export of his mailbox containing today's messages. As the company was
recently the victim of a supply chain attack, this case is being taken seriously and the
Cyber Threat Intelligence team is being called in to determine the severity of the threat.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

mailbox.zip - d48793ce17f4ffe349d66b3941c995d82a03dfddb4cd5bd4764898aa9704941d
Skills Learnt
Mapping Threats to MITRE ATT&CK Framework
Basic Threat Intelligence Pivoting
Threat Research

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |
| VirusTotal | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: Identify the sender of the suspicious email.
- Analysis note: We start by analyzing the email from the ProtonMail account with the subject line "Update on JavaScript
Authentication Module"
There seems to be nothing suspicious about this message, so we move on to the other one with the subject line
"Opportunity to Invest in NFT Game Project".
This is clearly an unusual message, here are some of the red flags that make the email suspicious:
Request for cooperation from an outside
- Answer: `theodore.todtenhaupt@developingdreams.site`
### Question 2: The suspicious email came from a custom domain, identify its creation date.
- Analysis note: Hint: If the domain is expired or the WHOIS is somehow unavailable, you can find a WHOIS Lookup
saved here:
https://web.archive.org/web/20250219112815/https://www.whois.com/whois/developingdreams.site
To retrieve the creation date for a given domain we can perform a WHOIS lookup using the whois command:
or use one of the many tools available online:
- Answer: `2025-01-31`
### Question 3: The domain was registered shortly before the suspicious email was received, which likely corresponds to
the time when the threat actor was planning this campaign. Which MITRE ATT&CK sub-technique of the
Resource Development tactic corresponds to this activity?
- Analysis note: The threat actor has registered a domain to use for their illicit purposes; this activity falls under the Resource
Development tactic, specifically the Acquire Infrastructure: Domains sub-technique, identified by T1583.001
- Answer: `T1583.001`
### Question 4: The previously identified domain appears to belong to a company, what is the full URL of the company's
page on X (formerly Twitter)?
- Analysis note: Hint: The original website may be unavailable or may have been seized. Try https://web.archive.org/.
To get more information about that company we try to browse to the previously identified domain, but their
website is no longer available. If a resource is no longer available on the web, one of the most useful tools for
finding a copy of that resource is the Wayback Machine.
So, after searching for the domain "develo
- Answer: `https://x.com/Develop_Dreams`
### Question 5: Reading the suspicious email carefully, it appears that the threat actor first contacted the victim using the
previously identified social media profile. Which MITRE ATT&CK sub-technique of the Resource
Development tactic corresponds to this activity?
- Analysis note: The email message indicates that the victim was previously contacted on platform X . This suggests that the
threat actor created one or more social media accounts and then developed a believable persona to lure victims.
This falls under the Resource Development tactic, specifically the Establish Accounts: Social Media
Accounts sub-technique, identified by T1585.001
- Answer: `T1585.001`
### Question 6: What is the name of the game the threat actor would like us to collaborate on?
- Analysis note: This information is also available on the website, if we have a look at the Our products section, we can see that
there are already two games in development, one of which is in Beta, as the e-mail said: DeTankWar .
- Answer: `DeTankWar`
### Question 7: What is the SHA-256 hash of the executable shared by the threat actor?
- Analysis note: Clicking on the Beta button we can download the beta_release_v.1.32.zip archive and extract its contents
using the password provided in the email: DTWBETA2025 .
Inside the archive there is only one file named beta_release_v.1.32.exe , so we calculate its SHA-256 hash by
using the sha256sum utility: 56554117d96d12bd3504ebef2a8f28e790dd1fe583c33ad58ccbf614313ead8c .
- Answer: `56554117d96d12bd3504ebef2a8f28e790dd1fe583c33ad58ccbf614313ead8c`
### Question 8: As part of the preparation of the tools for the attack, the threat actor hosted this file, presumably
malware, on its infrastructure. Which MITRE ATT&CK sub-technique of the Resource Development tactic
corresponds to this activity?
- Analysis note: Threat actors may upload malware to third-party infrastructure or to infrastructure previously compromised to
make it accessible during the attack. In this case, the malware seems to be hosted on infrastructure previously
purchased/rented by the adversary (see Q3).
This falls under the Resource Development tactic, specifically the Stage Capabilities: Upload Malware sub-
technique, identified by T1608.001 .
- Answer: `T1608.001`
### Question 9: Based on the information you have gathered so far, do some research to identify the name of the threat
- Analysis note: actor who may have carried out this attack.
We can now search the Web for some of the indicators we have gathered so far, such as the malware hash.
VirusTotal, for example, provides us with some helpful information:
a confirmation about the name, that seems related to the one we saw on the website: DeTankWar ;
a reference to a Microsoft security blog post: https://www.microsoft.com/en-us/security/blog/2024/05/28/m
oo
- Answer: `Moonstone Sleet`
### Question 10: What nation is the threat actor believed to be associated with?
- Analysis note: This information is available both in the report itself and on the threat actor page of the MITRE ATT&CK
website.
- Answer: `North Korea`
### Question 11: Another campaign from this threat actor used a trojanized version of a well-known software to infect
victims. What is the name of this tool?
- Analysis note: In the Microsoft report, the first documented attack by this group (around August 2023), consists of the delivery
of a trojanized version of putty , the well-known SSH client, via social media such as Linkedin and Telegram.
- Answer: `putty`
### Question 12: Which MITRE ATT&CK technique corresponds to the activity of deploying trojanized/manipulated
software?
- Analysis note: Attackers can compromise software before it reaches end users by modifying source code, tampering with
distribution systems, or replacing legitimate releases with malicious versions. In this case, the original putty
has been replaced with another that is fully functional, but contains code that decrypts, decompresses, and then
executes other malware.
This falls under the Initial Access tactic, specifically the Supply
- Answer: `T1195.002`
### Question 13: Our company wants to protect itself from other supply chain attacks, so in documenting more about this
threat actor, the CTI team found that other security researchers were also tracking a group whose
techniques closely match Moonstone Sleet, and discovered a new supply chain campaign around the end
of July 2024. What technology is this campaign targeting?
- Analysis note: A web search for Moonstone Sleet and supply-chain should easily direct our attention to the right article, but
if we want to filter the results further, we can use the after and before operators.
Let's analyze the blog post published by Datadog researchers in July 2024 about a DPKR-linked threat actor.
This post analyzes another campaign by a threat actor that appears to be very similar to Moonstone Sleet ,
which Dat
- Answer: `npm`
### Question 14: We now need some indicators to be able to rule out that other systems have been compromised. What is
the name and version of the lastest malicious package published?
- Analysis note: (Format: package-name vX.X.X)
From the previous screenshot we can see that the npm packages involved in the supply-chain attack are two:
harthat-hash and harthat-api . Scrolling down to the "The Initial Lead" section, we can see more details
about these packages, including release timestamps and versions:
So, the latest package to be published is harthat-hash and its version is v1.3.3 .
- Answer: `harthat-hash v1.3.3`
### Question 15: The malicious packages downloaded an additional payload from a C2 server, what is its IP address?
- Analysis note: The report analyzes all phases of the attack, and we can see from both the attack flowchart and the package
analysis that the additional payload is downloaded using curl from the IP address 142.111.77.196 .
- Answer: `142.111.77.196`
### Question 16: The payload, after being renamed, is finally executed by a legitimate Windows binary to evade defenses.
Which MITRE ATT&CK technique corresponds to this activity?
- Analysis note: The last part of the package analysis shows that the malicious payload is renamed from Temp.b to package.db
and then is executed by rundll32 to evade system defenses, as it is a Windows trusted binary.
This activity falls under the Defense Evasion tactic, specifically the System Binary Proxy Execution: Rundll32
sub-technique, identified by T1218.011 .
- Answer: `T1218.011`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Identify the sender of the suspicious email. | theodore.todtenhaupt@developingdreams.site |
| The suspicious email came from a custom domain, identify its creation date. | 2025-01-31 |
| The domain was registered shortly before the suspicious email was received, which likely corresponds to
the time when the threat actor was planning this campaign. Which MITRE ATT&CK sub-technique of the
Resource Development tactic corresponds to this activity? | T1583.001 |
| The previously identified domain appears to belong to a company, what is the full URL of the company's
page on X (formerly Twitter)? | https://x.com/Develop_Dreams |
| Reading the suspicious email carefully, it appears that the threat actor first contacted the victim using the
previously identified social media profile. Which MITRE ATT&CK sub-technique of the Resource
Development tactic corresponds to this activity? | T1585.001 |
| What is the name of the game the threat actor would like us to collaborate on? | DeTankWar |
| What is the SHA-256 hash of the executable shared by the threat actor? | 56554117d96d12bd3504ebef2a8f28e790dd1fe583c33ad58ccbf614313ead8c |
| As part of the preparation of the tools for the attack, the threat actor hosted this file, presumably
malware, on its infrastructure. Which MITRE ATT&CK sub-technique of the Resource Development tactic
corresponds to this activity? | T1608.001 |
| Based on the information you have gathered so far, do some research to identify the name of the threat | Moonstone Sleet |
| What nation is the threat actor believed to be associated with? | North Korea |
| Another campaign from this threat actor used a trojanized version of a well-known software to infect
victims. What is the name of this tool? | putty |
| Which MITRE ATT&CK technique corresponds to the activity of deploying trojanized/manipulated
software? | T1195.002 |

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

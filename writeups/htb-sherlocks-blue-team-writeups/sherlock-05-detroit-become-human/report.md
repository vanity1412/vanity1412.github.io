---
layout: page
title: "Sherlock: Detroit Become Human - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-05-detroit-become-human/report/
---

![Detroit Become Human cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-05-detroit-become-human.png)

# Detroit Become Human

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `detroitbecomehuman.pdf` |
| Pages | 18 |
| Difficulty | Hard |
| Prepared by | achille |
| Author | (s): CyberJunkie |

## Scenario Summary

Alonzo Spire is fascinated by AI after noticing the recent uptick in
usage of AI tools to help aid in daily tasks. He came across a
sponsored post on social media about an AI tool by Google. The post
had a massive reach, and the Page which posted had 200k + followers.
Without any second thought, he downloaded the tool provided via the
Post. But after installing it he could not find the tool on his system
which raised his suspicions. A DFIR analyst was notified of a possible
incident on Forela's sysadmin machine. You are tasked to help the
analyst in analysis to find the true source of this odd incident.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Enter the artifacts provided along with their file hash here.
detroitbecomehuman.zip -
aaf034c530c88a8c743364401fb8c518654f5d2c1660b8117302b70795e9101d
Skills Learnt
NTFS Forensics
Timeline creation
File Recovery
Disk Forensics
Contextual Analysis
Event Log Analysis
Threat intelligence
Browser forensics

## Tools Used

| Tool | Purpose |
| --- | --- |
| Zeek | Used or likely relevant based on the source writeup |
| PowerShell | Used or likely relevant based on the source writeup |
| Windows Event Logs | Used or likely relevant based on the source writeup |
| strings | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 2: Can you confirm the timestamp in UTC when alonzo visited this post?
- Analysis note: We can get the timestamp by looking at the last_visit_time column:
13355296200136503 . This is a timestamp in Chrome/WebKit format, so we need to
convert it to a UTC timestamp, and then we get 2024-03-19 04:30:00 .
- Answer: `2024-03-19 04:30:00`
### Question 3: Alonzo downloaded a file on the system thinking it was an AI Assistant tool. What
is name of the archive file downloaded?
- Analysis note: This information is also available in the browser history file, if we switch to the
downloads table we can see 5 entries, the last one refers to the suspicious archive:
AI.Gemini Ultra For PC V1.0.1.rar .
- Answer: `AI.Gemini Ultra For PC V1.0.1.rar`
### Question 4: What was the full direct url from where the file was downloaded?
- Analysis note: To answer this question, we need to note the download ID from the previous table ( 5 )
and then go to the download_url_chains table, where we can find a chronological list
of web addresses involved in a file download, revealing the full chain of redirects and
the final destination where the file was actually downloaded.
In our case, we have four entries for ID 5 , meaning that after clicking the link, there
were thre
- Answer: `https://drive.usercontent.google.com/download?id=1z-`
### Question 5: Alonzo then proceeded to install the newly download app, thinking that it is a legit
AI tool. What is the true product version which was installed?
- Analysis note: Since we know that Alonzo downloaded an archive related to Gemini AI, we will first try
to search for the keyword Gemini in the Windows logs.
We use chainsaw , a very powerful tool to search and hunt on Windows logs:
chainsaw --no-banner search -e Gemini *
There are two events, one of which is shown above:
Both events come from the MsiInstaller provider.
The two events, one with ID 1040 (Installer Started) and the ot
- Answer: `3.32.3`
### Question 6: When was the malicious product/package successfully installed on the system?
- Analysis note: To answer this question we will print the event with ID 11707 instead:
chainsaw --no-banner search --timestamp
'Event.System.TimeCreated_attributes.SystemTime' -t
'Event.System.EventID: =11707' --from '2024-03-19T04:31:02'
Application.evtx
- Answer: `2024-03-19 04:31:33`
### Question 7: The malware used a legitimate location to stage its file on the endpoint. Can you
find out the Directory path of this location?
- Analysis note: To answer this question, we will focus our attention on the $MFT artifact. After
converting it to a CSV file, we open it with Timeline Explorer.
Then we apply a time filter to select only events with FileName creation timestamp
( Created0x30 ) newer than the first installation event of the MSI file.
After sorting the entries in ascending order, we can see right away that there are a
bunch of files that are located un
- Answer: `C:\Program Files (x86)\Google`
### Question 8: The malware executed a command from a file. What is name of this file?
- Analysis note: From the previous analysis we saw that there are some suspicious files in the identified
folder, such as ru.ps1 , install.cmd , background.js and content.js .
Since this question asks from which file a command was executed, the most likely is
install.cmd .
- Answer: `install.cmd`
### Question 9: What are the contents of the file from question 8?
- Analysis note: Remove whitespace to avoid
format issues.
We can confirm our previous assumption by looking at the contents of install.cmd
using MFTECmd.
From the Timeline Explorer we noted the Entry Number (51471) and the Sequence
Number (4) for install.cmd , then we execute:
.\MFTCmd.exe -f '..\$MFT' --de 51471-4
**
- Answer: `** <span style="color: #9FEF00;">`@echooffpowershell-`
### Question 10: What was the command executed from this file according to the logs?
- Analysis note: Because this is a PowerShell command, we expect to see the execution of this
command in the Windows PowerShell event logs.
Again, we use chainsaw to find this entry in the EVTX file:
chainsaw --no-banner search -e 'ru.ps1' logs/Windows\
PowerShell.evtx | tail -n 30
We need to remove the escape character ( \ ) from the path and then we get:
powershell -ExecutionPolicy Bypass -File C:\Program Files
(x86)\Google\Install
- Answer: `powershell -ExecutionPolicy Bypass -File C:\Program Files`
### Question 11: Under malware staging Directory, a js file resides which is very small in size. What
is the hex offset for this file on the filesystem?
- Analysis note: We have already identified two JS files: background.js and content.js , which are
17208 and 258 bytes respectively.
So again, from the Timeline Explorer, we note the Entry and Sequence numbers for
content.js and then pass them to MFTCmd:
.\MFTCmd.exe -f '..\$MFT' --de 64067-4
The output will provide us with the Offset ( 3E90C00 ) and also the content of the file.
- Answer: `3E90C00`
### Question 13: Upon seeing no AI Assistant app being run, alonzo tried searching it from file
explorer. What keywords did he use to search?
- Analysis note: This is not a common DFIR technique, but there is a great article that explains how to
retrieve information about searched strings in Windows.
So we fire up Registry Explorer and feed it with Alonzo's NTUSER.DAT .
Then browsing to
\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery we can
see the keyword that Alonzo searched: Google Ai Gemini .
- Answer: `Google Ai Gemini tool`
### Question 14: When did alonzo searched it?
- Analysis note: The Last Write Timestamp column in the previous screenshot gives us the answer:
2024-03-19 04:32:11 .
- Answer: `2024-03-19 04:32:11`
### Question 15: After alonzo could not find any AI tool on the system, he became suspicious,
contacted the security team and deleted the downloaded file. When was the file
deleted by alonzo?
- Analysis note: We switch back to our Timeline Explorer and, since Alonzo downloaded a RAR
archive, this time we apply a filter to select only files with a .rar extension.
Then we sort the timestamps in ascending order and the only one older than the
download time is: 2024-03-19 04:34:16 .
- Answer: `2024-03-19 04:34:16`
### Question 16: Looking back at the starting point of this infection, please find the MD5 hash of
- Analysis note: the malicious installer.
To answer this last question, we try to search for the MSI file name on the web. The first
result is a page from AnyRun (a well-known online sandbox) that analyzes this installer,
so we can get the MS5 hash of the file from here:
BF17D7F8DAC7DF58B37582CEC39E609D .
- Answer: `BF17D7F8DAC7DF58B37582CEC39E609D`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Can you confirm the timestamp in UTC when alonzo visited this post? | 2024-03-19 04:30:00 |
| Alonzo downloaded a file on the system thinking it was an AI Assistant tool. What
is name of the archive file downloaded? | AI.Gemini Ultra For PC V1.0.1.rar |
| What was the full direct url from where the file was downloaded? | https://drive.usercontent.google.com/download?id=1z- |
| Alonzo then proceeded to install the newly download app, thinking that it is a legit
AI tool. What is the true product version which was installed? | 3.32.3 |
| When was the malicious product/package successfully installed on the system? | 2024-03-19 04:31:33 |
| The malware used a legitimate location to stage its file on the endpoint. Can you
find out the Directory path of this location? | C:\Program Files (x86)\Google |
| The malware executed a command from a file. What is name of this file? | install.cmd |
| What are the contents of the file from question 8? | ** <span style="color: #9FEF00;">`@echooffpowershell- |
| What was the command executed from this file according to the logs? | powershell -ExecutionPolicy Bypass -File C:\Program Files |
| Under malware staging Directory, a js file resides which is very small in size. What
is the hex offset for this file on the filesystem? | 3E90C00 |
| Upon seeing no AI Assistant app being run, alonzo tried searching it from file
explorer. What keywords did he use to search? | Google Ai Gemini tool |
| When did alonzo searched it? | 2024-03-19 04:32:11 |

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

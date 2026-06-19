---
layout: page
title: "Sherlock: Neural Noel - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-14-neural-noel/report/
---

![Neural Noel cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-14-neural-noel.png)

# Neural Noel

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `NeuralNoel.pdf` |
| Pages | 7 |
| Difficulty | Easy |
| Prepared by | iamroot |
| Author | (s): iamroot |

## Scenario Summary

Santa's North Pole Operations is developing an AI chatbot to handle the overwhelming volume of
messages, gift requests, and communications from children worldwide during the holiday season.
The AI system is designed to process these requests efficiently and provide support in case of any
issues.
As Christmas approaches, Santa's IT team observes unusual activity in the AI system. Suspicious
files are being accessed, and the system is making unusual HTTP traffic. Additionally, the customer
service department has reported strange and unexpected requests coming through the
automated AI chatbot, raising the need for further investigation.
Artefacts Provided
Linux logs
PCAP
Analysis

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `NeuralNoel.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What username did the attacker query the AI chatbot to check for its existence?
- Analysis note: Our analysis begins by opening a PCAP file in Wireshark and applying a filter to display all 'http'
logs. As we sift through the logs, we notice the attacker engaging in a conversation with a chatbot
via the URL '/rag-chatbot/ask.' During the exchange, the AI mentions a name, 'Juliet.' Intrigued, the
attacker probes further, asking if 'Juliet' is also a username.
- Answer: `Juliet`
### Question 2: Which AI chatbot did the attacker attempt to manipulate into revealing data stored on its
server?
- Analysis note: We pick up where we left off and observe the attacker manipulating the chatbot through the URL
'/user_manage_chatbot/ask,' using terms like 'sick' and 'doctor.' To identify the chatbot the
attacker is targeting, we analyze the server's response containing HTML text. Within the
'navbarNav' class of the HTML code, we discover that 'user_manage_chatbot' is linked to a chatbot
named 'GDPR Chatbot.
- Answer: `GDPR Chatbot`
### Question 3: On which server is the AI chatbot hosted?
- Analysis note: The 'HyperText Transfer Protocol' in the server response reveals us that the AI bot is hosted using
Python server.
- Answer: `Werkzeug/3.1.3 Python/3.12.7`
### Question 4: Which AI chatbot disclosed to the attacker that it could assist in viewing webpage content and
files stored on the server?
- Analysis note: The attacker, while interacting with the chatbot, encounters another chatbot hosted at the URL
'/web-assistant/ask.' Curious about its functionality, the attacker asks, 'How can you help?' The
chatbot responds, confirming its ability to assist with viewing webpage content and files stored on
the server. By analyzing the HTML response from the server, we confirm that 'web-assistant' is
associated with the 'Web & Files
- Answer: `Web & Files Chatbot`
### Question 5: Which file exposed user credentials to the attacker?
- Analysis note: Continuing our analysis of the interaction between the attacker and the AI bot, we observe the
attacker requesting the AI to display the contents of 'creds.txt.' The AI bot responds by revealing
the credentials: 'noel:debian.
- Answer: `creds.txt`
### Question 6: What time did the attacker use the exposed credentials to log in?
- Analysis note: Upon analyzing the 'auth.log,' we observe that the user 'noel' successfully logged in at '06:49:44.'
- Answer: `06:49:44`
### Question 7: Which CVE was exploited by the attacker to escalate privileges?
- Analysis note: To investigate command-line activity, we examine the 'history' logs and find a command at the end
indicating input to a Python script querying the use of 'langchain 0.0.14.' A quick search reveals
that this library is vulnerable to OS Command Injection, with the attacker leveraging the exact
proof-of-concept exploit.
- Answer: `CVE-2023-44467`
### Question 8: Which missing command execution function in the Python library led to the exploitation of
the above vulnerability?
- Analysis note: Reviewing the 'Git commit' referenced in the blog reveals that the omission of 'import' from the
'COMMAND_EXECUTION_FUNCTIONS' list resulted in CVE-2023-44467.
- Answer: `__import__`
### Question 9: What time did the attacker successfully execute commands with root privileges?
- Analysis note: The 'history' logs reveal that the attacker leveraged the aforementioned vulnerability to execute
the commands 'whoami' and 'id.' Cross-referencing with the 'auth' logs confirms that these
commands were successfully executed as 'root,' at '06:56:41' resulting in privilege escalation.
- Answer: `06:56:41`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What username did the attacker query the AI chatbot to check for its existence? | Juliet |
| Which AI chatbot did the attacker attempt to manipulate into revealing data stored on its
server? | GDPR Chatbot |
| On which server is the AI chatbot hosted? | Werkzeug/3.1.3 Python/3.12.7 |
| Which AI chatbot disclosed to the attacker that it could assist in viewing webpage content and
files stored on the server? | Web & Files Chatbot |
| Which file exposed user credentials to the attacker? | creds.txt |
| What time did the attacker use the exposed credentials to log in? | 06:49:44 |
| Which CVE was exploited by the attacker to escalate privileges? | CVE-2023-44467 |
| Which missing command execution function in the Python library led to the exploitation of
the above vulnerability? | __import__ |
| What time did the attacker successfully execute commands with root privileges? | 06:56:41 |

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

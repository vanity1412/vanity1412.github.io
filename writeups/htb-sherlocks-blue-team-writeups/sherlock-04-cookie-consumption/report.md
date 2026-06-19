---
layout: page
title: "Sherlock: Cookie Consumption - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-04-cookie-consumption/report/
---

![Cookie Consumption cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-04-cookie-consumption.png)

# Cookie Consumption

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `CookieConsumption.pdf` |
| Pages | 15 |
| Difficulty | Easy |
| Prepared by | VivisGhost |
| Author | (s): felamos |

## Scenario Summary

Santas North Pole Operations have implemented the Cookie Consumption
Scheduler (CCS), a crucial service running on a Kubernetes cluster. This
service ensures Santas cookie and milk intake is balanced during his
worldwide deliveries, optimizing his energy levels and health.
Description
In this scenario, players investigate a Kubernetes breach by analyzing
artifacts to track the attackers actions, focusing on tasks such as
investigating compromised namespaces and detecting malicious behavior.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Cookie_Consumption.zip -
87728bbc7ede12b5511855c96f2d37d70f18f928fe536bfca02fae5593ef362d

## Tools Used

| Tool | Purpose |
| --- | --- |
| kubectl | Used or likely relevant based on the source writeup |
| Docker | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: How many replicas are configured for the flask-app deployment?
- Analysis note: The deployments.log file contains the configurations and statues of the Deployments in
the Kubernetes cluster. A Deployment ensures the desired number of pod replicas are
running and automatically handles updates to the application.
This information can also be found in the pods.log file, which will be discussed more
later.
- Answer: `3`
### Question 2: What is the NodePort through which the flask-app is exposed?
- Analysis note: The services.log file describes Services configured in the cluster, which define how
pods are exposed to other services or external users. Services provide stable networking
endpoints for pods and can expose applications via NodePort.
- Answer: `30000/TCP`
### Question 3: What time (UTC) did the attacker first initiate fuzzing on the /system/ endpoint?
- Analysis note: When analyzing the flask-app.log in the context of web fuzzing, the HTTP status codes
can reveal critical information about an attack. A 404 status code indicates the requested
page does not exist. A series of 404 response errors is an indicator of fuzzing.
- Answer: `2024-11-08 22:02:48`
### Question 4: Which endpoint did the attacker discover through fuzzing and subsequently exploit?
- Analysis note: A 200 status code indicates a successful request. How we know this endpoint was being
exploited will be discussed in the next question.
- Answer: `/system/execute`
### Question 5: Which program did the attacker attempt to install to access their HTTP pages?
- Analysis note: Continuing to look in the flask logs we can see a couple interesting entries. The red box
suggests the threat actor has RCE and ran the id command. The next command in the
orange box suggests they tried to run Netcat to establish a reverse shell, but the system
doesn't have it. Finally, the yellow box suggests they attempted to use the curl
command, but as seen below the box, the system didn't have that either.
Movin
- Answer: `curl`
### Question 6: What is the IP address of the attacker?
- Analysis note: In the host-process.log during the initial analysis we saw a sketchy command of
someone downloading something with curl then piping it to bash to run it. Given the
presence of Netcat in the previous question we were able to surmise that threat actor was
establishing a reverse shell and connecting back to their IP.
- Answer: `10.129.231.112`
### Question 7: What is the name of the pod that was compromised and used by the attacker as the
initial foothold?
- Analysis note: In default/process we can find the process dump. Using grep to filter for commands
(line after process id) we see the curl command again.
- Answer: `flask-app-77fbdcfcff-2tqgw`
### Question 8: What is the name of the malicious pod created by the attacker?
- Analysis note: The pods.log file provides details about the Pods running in the cluster, including their
names, statuses and associated configurations.
An important aspect to notice
The container has /mnt mounted. (Red Box)
The host directory being mounted is the root directory ( //// ). (Orange Box)
Since the container can access /mnt (which maps to / on the host filesystem) with
read-write permissions, it has the ability to:
Acce
- Answer: `evil`
### Question 9: What is the absolute path of the backdoor file left behind by the attacker?
- Analysis note: This was found looking into cron.txt during the initial analysis. To gain a better idea of
timing we can examine systemd-journal.log . This log shows the location of the file and
when the CRON first runs.
- Answer: `/opt/backdoor.sh`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| How many replicas are configured for the flask-app deployment? | 3 |
| What is the NodePort through which the flask-app is exposed? | 30000/TCP |
| What time (UTC) did the attacker first initiate fuzzing on the /system/ endpoint? | 2024-11-08 22:02:48 |
| Which endpoint did the attacker discover through fuzzing and subsequently exploit? | /system/execute |
| Which program did the attacker attempt to install to access their HTTP pages? | curl |
| What is the IP address of the attacker? | 10.129.231.112 |
| What is the name of the pod that was compromised and used by the attacker as the
initial foothold? | flask-app-77fbdcfcff-2tqgw |
| What is the name of the malicious pod created by the attacker? | evil |
| What is the absolute path of the backdoor file left behind by the attacker? | /opt/backdoor.sh |

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

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Log Analysis
Kubernetes Configuration

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

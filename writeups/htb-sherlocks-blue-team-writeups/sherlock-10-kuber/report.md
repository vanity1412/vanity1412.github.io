---
layout: page
title: "Sherlock: Kuber - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-10-kuber/report/
---

![Kuber cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-10-kuber.png)

# Kuber

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `Kuber.pdf` |
| Pages | 12 |
| Difficulty | Easy |
| Prepared by | felamos |
| Author | (s): felamos |

## Scenario Summary

As a digital forensics investigator, you received an urgent request
from a client managing multiple proxy Kubernetes clusters. The client
reports unusual behavior in one of their development environments,
where they were testing a proxy via SSH. This environment was exposed
to the internet, raising concerns about a potential security breach.
You have been provided with a dump of the `kube-system` namespace, as
most of the testing activity occurred there. Your task is to
thoroughly analyze the data and determine if the system has been
compromised.
Description
Kuber is an easy Sherlock designed to help you understand the
structure of Kubernetes resources. You will learn to analyse resource
dumps from a Kubernetes cluster, enabling you to identify malicious
activities and assess potential attack vectors. Through this process,
you will gain insights into how an attacker can compromise the cluster
and escalate privileges to gain full access to the host system.
Artefacts provided
Kuber.zip - a632a03355131c8c0d8a67bddda24e98
Skills Learnt
Kubernetes resource configuration Analysis

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

Source PDF: `Kuber.pdf`. Add downloaded challenge artifacts and hashes here when available.

## Tools Used

| Tool | Purpose |
| --- | --- |
| kubectl | Used or likely relevant based on the source writeup |
| Docker | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: At which NodePort is the sssssssshhhh----ddddeeeeppppllllooooyyyymmmmeeeennnntttt Kubernetes service exposed for
external access?
- Analysis note: Question wants to know which NodePort is being used for explosing the service.
Looking at the services yaml file we can see that one of the service is exposing the said
deployment
- Answer: `31337`
### Question 2: What is the ClusterIP of the kubernetes cluster?
- Analysis note: NodePort builds on top of the ClusterIP so the IP can be found inside services yaml
- Answer: `10.43.191.212`
### Question 3: What is the value of the FLAG data inside ssh-config configmap?
- Analysis note: Configmap is an API object used to store non-confidential data in key-value pairs, if we
look at the ssh-config configmap we can see flag key-value pair.
- Answer: `HTB{1d2d2b861c5f8631f841b57f327f46f8}`
### Question 4: What is the value of password (in plaintext) which is found inside ssh-deployment
via secret?
- Analysis note: There is a chain to this, deployment refers secret which in our case is ssh-secret , we
can simply read USER_PASSWORD value and decode the base64 which will reveal our
password.
- Answer: `SuperCrazyPassword123!`
### Question 5: What is the name of the malicious pod?
- Analysis note: Malicious actor camouflages the name of the pod which a real service which is
metrics-server in our case.
- Answer: `metrics-server-557ff575fx-4q62x`
### Question 6: What is the image attacker is using to create malicious pod?
- Analysis note: Inpecting the malicious pod reveals which image is the pod using.
- Answer: `alpine`
### Question 7: IP Address of the malicious actor
- Analysis note: If we look at the cmdline and argument of the pod, it will reveal a reverse shell
connection to attack IP.
- Answer: `10.10.14.11`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| At which NodePort is the sssssssshhhh----ddddeeeeppppllllooooyyyymmmmeeeennnntttt Kubernetes service exposed for
external access? | 31337 |
| What is the ClusterIP of the kubernetes cluster? | 10.43.191.212 |
| What is the value of the FLAG data inside ssh-config configmap? | HTB{1d2d2b861c5f8631f841b57f327f46f8} |
| What is the value of password (in plaintext) which is found inside ssh-deployment
via secret? | SuperCrazyPassword123! |
| What is the name of the malicious pod? | metrics-server-557ff575fx-4q62x |
| What is the image attacker is using to create malicious pod? | alpine |
| IP Address of the malicious actor | 10.10.14.11 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Execution | Command and Scripting Interpreter | Observed in extracted case notes; validate with report evidence. |
| Credential Access | Credential Dumping / Unsecured Credentials | Observed in extracted case notes; validate with report evidence. |
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

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.






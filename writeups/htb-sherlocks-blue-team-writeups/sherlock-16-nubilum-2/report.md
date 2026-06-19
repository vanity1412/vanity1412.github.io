---
layout: page
title: "Sherlock: Nubilum 2 - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-16-nubilum-2/report/
---

![Nubilum 2 cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-16-nubilum-2.png)

# Nubilum 2

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `nubilum_2.pdf` |
| Pages | 15 |
| Difficulty | Easy |
| Prepared by | n4cho |
| Author | (s): n4cho |

## Scenario Summary

Leading telecoms provider Forela uses AWS S3 as an essential part of their infrastructure. They
can deploy applications quickly and do effective analytics on their sizable dataset thanks to it
acting as both an application storage and a data lake storage.
Recently, a user reported an urgent issue to the helpdesk: an inability to access files within a
designated S3 directory. This disruption has not only impeded critical operations but has also
raised immediate security concerns.
The urgency of this situation demands a security-focused approach. Reports of a misconfigured S3
Bucket policy for the forela-fileshare bucket, resulting in unintended public access, highlight a
potential security vulnerability that calls for immediate corrective measures. Consequently, a
thorough investigation is paramount.
In order to rectify this situation, you are tasked to diligently identify who initiated the actions, how
these actions were executed, and what specifically transpired with the S3 objects, leading to their
inaccessibility. This comprehensive understanding is essential for a targeted and effective
resolution.
Initiating with a comprehensive analysis of the AWS CloudTrail logs will provide a detailed record
of all interactions with the affected S3 bucket. This step is pivotal in comprehending the entire
extent of the incident and ensuring the necessary actions are taken to address it from a security
perspective.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

CloudTrail Logs
Skills Learnt
CloudTrail Analysis
AWS Services Familiarity
Threat Actor Identification
Privilege Escalation Awareness
Log Querying and Analysis using Splunk

## Tools Used

| Tool | Purpose |
| --- | --- |
| Splunk | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |
| strings | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: What was the originating IP address the Threat Actor (TA) used to infiltrate the Forelas AWS
account?
- Analysis note: To pinpoint the infiltrator, we can utilize Splunk's filtering capabilities to scrutinize all source IP
addresses that interacted with the affected S3 bucket. One particular IP address stands out,
displaying a notably higher frequency of interactions compared to others. It's advisable to
investigate the specific requests made by this address within the bucket.
By thoroughly reviewing the requested events, it becomes 
- Answer: `54.242.59.197`
### Question 2: What was the time, filename, and Account ID of the first recorded s3 object accessed by the
TA?
- Analysis note: Upon closer inspection of the events tied to the malicious IP address, it becomes apparent that
several requests were executed, including the retrieval of files from the affected S3 bucket.
Hence, we can identify the initial object that the threat actor either viewed or downloaded along,
with other important details.
- Answer: `2023-11-02T14:52:03Z,prod-EC2-readonly_accessKeys.csv,anonymous`
### Question 3: How many Access Keys were compromised, at a minimum?
- Analysis note: Looking at the events that the TA requested initially, we are able to see files that are ansible
playbooks and filenames that has suffixed _accessKeys.csv which is the default names of AWS
Keys as well. There is a possibility that there are also access keys stored in the ansible playbook
but we are unsure since there is no event data showing that there is hard coded creds inside
those files.
Upon reviewing the events
- Answer: `7`
### Question 4: The TA executed a command to filter EC2 instances. What were the name and value used for
filtering?
- Analysis note: This information can be obtained by querying the DescribeInstances events as requested by the
TA and by examining the items in the filterSet, we can uncover the name and value used for
filtering.
The describe-instances command can be utilized by Threat Actors to discover and gather
information about running instances within an AWS environment. In this case, the filter indicates
that the Threat Actor was interested in
- Answer: `instance-state-name:running`
### Question 5: Can you provide the count of unsuccessful discovery and privilege escalation attempts made
by the TA before gaining elevated access with the compromised keys?
- Analysis note: To efficiently identify failed discovery and privilege escalation attempts made by the TA, we can
enhance our query by adding a filter of errorCode="AccessDenied". By implementing this filter, we
can streamline the process of detecting and analyzing unauthorized access attempts.
- Answer: `42`
### Question 6: Which IAM user successfully gained elevated privileges in this incident?
- Analysis note: Scanning the events further, we noticed that when the TA utilized the dev-policy-specialist IAM
user account, it did not encounter any error codes while attempting to List events that had failed
using the previous IAM accounts. This implies that the requests made by the TA were successful.
Furthermore, it was able to execute the PutUserPolicy action. https://docs.aws.amazon.com/IAM/l
atest/APIReference/API_PutUserPol
- Answer: `dev-policy-specialist`
### Question 7: Which event name permitted the threat actor to generate an admin-level policy?
- Answer: `PutUserPolicy`
### Question 8: What is the name and statement of the policy that was created that gave a standard user
account elevated privileges?
- Answer: `Sbhyy79zky,[{"Effect": "Allow","Action": "","Resource": ""}]`
### Question 9: What was the ARN (Amazon Resource Name) used to encrypt the files?
- Analysis note: Upon closer inspection of the events, it becomes apparent that there are instances where TA
requested a large number of GetObject operations, indicating that it may have downloaded all of
the files in the affected S3 bucket.
Following the GetObject events, we can see that there are also CopyObject events.
In essence, GetObject is an activity that allows you to obtain (view or download) an item from the
S3 bucket. Cop
- Answer: `arn:aws:kms:us-east-1:263954014653:key/mrk-85e24f85d964469cba9e4589335dd0f4`
### Question 10: What was the name of the file that the TA uploaded to the S3 bucket?
- Analysis note: To promptly spot uploaded objects in an S3 bucket, we can use the filter eventName=PutObject.
Judging by the filename, it appears that the TA left a ransomware note intended for Forela
employees. Ransomware occurrences in AWS setups are not infrequent and warrant serious
attention from organizations. Even with AWS's robust security measures in place, policy
misconfigurations, weak credentials, and vulnerabilities rem
- Answer: `README2DECRYPT.txt`
### Question 11: Which IAM user account did the TA modify in order to gain additional persistent access?
- Analysis note: It appears the Threat Actor isn't done yet. Continuing with the remaining events left by the TA,
another significant discovery was made. This involved a request for a ListUsers action, followed by
a CreateAccessKey event indicating an attempt at persistence. The TA successfully manipulated
the forela-admin account by generating an additional access key, potentially as a backup in case
the Forela Security Team manages
- Answer: `forela-admin`
### Question 12: What action was the user not authorized to perform to view or download the file in the S3
bucket?
- Analysis note: Finally, lets turn our attention to the files that were tried to be opened. By employing the query
eventName=GetObject errorCode=AccessDenied we can isolate events where accesses was
attempted but failed.
Analyzing the event, it is evident that user John made an unsuccessful attempt to access
Executive_Summary_Q1_2023.docx within the reports directory due to insufficient permissions for
kms:decrypt.
- Answer: `kms:Decrypt`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| What was the originating IP address the Threat Actor (TA) used to infiltrate the Forelas AWS
account? | 54.242.59.197 |
| What was the time, filename, and Account ID of the first recorded s3 object accessed by the
TA? | 2023-11-02T14:52:03Z,prod-EC2-readonly_accessKeys.csv,anonymous |
| How many Access Keys were compromised, at a minimum? | 7 |
| The TA executed a command to filter EC2 instances. What were the name and value used for
filtering? | instance-state-name:running |
| Can you provide the count of unsuccessful discovery and privilege escalation attempts made
by the TA before gaining elevated access with the compromised keys? | 42 |
| Which IAM user successfully gained elevated privileges in this incident? | dev-policy-specialist |
| Which event name permitted the threat actor to generate an admin-level policy? | PutUserPolicy |
| What is the name and statement of the policy that was created that gave a standard user
account elevated privileges? | Sbhyy79zky,[{"Effect": "Allow","Action": "","Resource": ""}] |
| What was the ARN (Amazon Resource Name) used to encrypt the files? | arn:aws:kms:us-east-1:263954014653:key/mrk-85e24f85d964469cba9e4589335dd0f4 |
| What was the name of the file that the TA uploaded to the S3 bucket? | README2DECRYPT.txt |
| Which IAM user account did the TA modify in order to gain additional persistent access? | forela-admin |
| What action was the user not authorized to perform to view or download the file in the S3
bucket? | kms:Decrypt |

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

Add lessons learned after completing the investigation.

## Conclusion

This report was generated from the source PDF and should be reviewed while solving the Sherlock manually. Replace draft notes with your own investigation evidence before publishing.

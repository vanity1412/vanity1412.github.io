---
layout: page
title: "Sherlock: Percy Pay - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-18-percy-pay/report/
---

# Percy Pay

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `PercyPay.pdf` |
| Pages | 37 |
| Difficulty | Easy |
| Prepared by | b3ngriffiths & VivisGhost |
| Author | b3ngriffiths |

## Scenario Summary

You are working for an innovative new payment provider, PercyPay, who
are revolutionising the financial technology landscape with their
cutting-edge solutions and customer-centric approach.
There's a new Cyber Threat Intelligence Analyst as part of your team,
and they're still finding their feet, understanding the business and
our SecOps processes. They're just come across what appears to be some
valuable information, but asking the wider team for support to help
understand how real it is. And if real, what's the next steps and
impact seen.
On AlphaBay (a dark web marketplace), PercyPay customer data has been
listed for sale. There is no further information about quantities, or
what type of data, but a single sample file has been made available as
proof. The filename is `CustomerB-2024-12-09-f97a1bcc-7.json`.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

PercyPay.zip -
dbb1dc102b8609ba651516553ba0ebf22294b3191dd535570a8a34bd36372ad8
CloudTrail.zip -
60979c3a4bf2fc51a6ca243ea91f0c8cb22add91dbec755f02c7ca3950860266
percypay-website-host.zip -
5f5716b2437b6fa29cd7003b7bd882b5fa295ed0761728e53ebe84c3db13390c
Skills Learnt
AWS Cloud Security
Log Analysis

## Tools Used

| Tool | Purpose |
| --- | --- |
| Splunk | Used or likely relevant based on the source writeup |
| AWS CLI / CloudTrail | Used or likely relevant based on the source writeup |
| jq | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: Which S3 bucket was the affected file stored in?
- Analysis note: We have been given the name of the affected file in the scenario. We can create a table
with the time, bucket name and search for the file.
Using Chronicle.
- Answer: `percypay-payment-data`
### Question 2: Which AWS IAM user interacted with the file?
- Analysis note: Now we think we have a suspicious user we can take a peek at some of the actions.
We can filter looking for unique eventNames
Using Chronicle.
- Answer: `arn:aws:iam::857609373938:user/percypay-webapp-user`
### Question 3: What AWS Access Key should be revoked, as part of response action?
- Analysis note: Answer can be seen in first screenshot from Question 2.
Using Chronicle.
- Answer: `AKIA4PLMARDZ[REDACTED]` (AWS Access Key - redacted for security)
### Question 4: What was the Threat Actor's (TA) IP address?
- Analysis note: Answer can be seen in first screenshot from Question 2.
Using Chronicle.
- Answer: `149.102.244.70`
### Question 5: What was the blast radius, how many files were impacted?
- Analysis note: The Threat Actor (TA) is offering multiple files for sale, to understand the extent lets
pivot on that compromised IAM user to see any other activity of interest. It appears the
user has conducted several actions, looking at the events there are more GetObject.
Reviewing these events specifically can see they all occurred around similar time, from
the same IP address.
Using Chronicle.
- Answer: `164`
### Question 6: Which Customer's data has been impacted?
- Analysis note: Legal have been made aware of the investigation, and they're preparing customer
communications. At this point, it's key they get more details of the blast radius by
understanding the number of customers impacted. Pivoting on the GetObject events,
and the target/resource ARN, it's possible to review the directory and filenames of
impacted files.
Using Chronicle.
- Answer: `CustomerB`
### Question 7: What date was the payment data from?
- Analysis note: Based on logs already reviewed, and the naming conventions for directories and
filename in the S3 bucket, it's possible to identify when the payment data was from.
Further, ordering by object ARN in ascending order makes this easy to quickly review.
Using Chronicle.
- Answer: `2024-12-09`
### Question 8: What was the time for initial event from this user?
- Analysis note: Now the blast radius has been established Legal can begin to confirm customer
notification requirements. It's now crucial to understand how this all happened. Going
back to look at all the actions the user performed, lets start from beginning.
Using Chronicle.
- Answer: `2024-12-15 20:42:16`
### Question 9: How many IP addresses did the TA use for this user?
- Analysis note: Conducting an investigation around a single IP address can be dangerous, it's one of
the easiest things for a TA to change and therefore we shouldn't get tunnel visioned.
Using Chronicle.
- Answer: `3`
### Question 3: ARN (Amazon Resource Name): The ARN associated with the calling entity.
- Analysis note: This event is particularly useful for verifying the identity of the caller.
Using Chronicle.
- Answer: `GetCallerIdentity`
### Question 11: What was the first IAM Policy the TA reviewed?
- Analysis note: The Threat Actor listed the IAM Policies associated with the IAM user, and followed this
by GetPolicyVersion requests to review the permissions within those policies.
Using Chronicle.
- Answer: `lambda-export-data`
### Question 12: What operation did the TA perform to alter IAM Policy permissions available to the
user?
- Analysis note: The TA likely saw a previous IAM Policy version had additional and/or more attractive
permissions. This operation sets the specified version of a policy as the default
(operative) version, which is in effect for all users which the policy is attached. When
IAM Policies are modified, a copy of the previous Policy is still available, and if
iam:SetDefaultPolicyVersion and/or iam:* actions are available, the IAM entity

- Answer: `SetDefaultPolicyVersion`
### Question 13: Which IAM Policy was next utilized by the TA?
- Analysis note: The chosen IAM policy to be set as default can be seen in the request parameters.
Using Chronicle.
- Answer: `lambda-export-invoke`
### Question 14: What was the ARN of the next resource the TA created?
- Analysis note: Once new permissions have been obtained via altering the associated IAM Policy, the
next activity is CreateFunction20150331 .
Using Chronicle.
- Answer: `arn:aws:lambda:eu-west-1:857609373938:function:web-processor-`
### Question 15: Which user created the resource?
- Analysis note: The userIdentity for this action can be found in the same log.
Using Chronicle.
- Answer: `percypay-webapp-user`
### Question 16: The role given to the resource is different to that of the creating user, which IAM
action has likely been used?
- Analysis note: Again, within the same log it's possible to see the role requested to be assigned to the
Lambda Function. When creating a Lambda function and assigning it a role, the
iam:PassRole permission is essential. This permission allows the entity (user, group,
or role) to pass an IAM role to the Lambda function. However, we must infer this
permission is used as it will not be explicitly seen in the logs. In order to see this
- Answer: `iam:PassRole`
### Question 17: What action did the TA created Lambda Function perform?
- Analysis note: The Lambda function web-processor-function assumed role lambda-commander to
AttachUserPolicy to IAM user percypay-webapp-user
Using Chronicle.
- Answer: `AttachUserPolicy`
### Question 18: What Policy was assigned?
- Analysis note: From the previous log, it's possible to identify the IAM Policy applied and to the user,
within the requestParameters.
Using Chronicle.
- Answer: `arn:aws:iam::aws:policy/AdministratorAccess`
### Question 19: What AWS service did the user conduct discovery activity against next?
- Analysis note: The compromised user, under a new IP address, performs ListDetectors which lists all
the detector IDs of GuardDuty detector resources in the AWS account.
Looking back to the unique events ran by the user, we see ListDetectors from
GuardDuty.
Using Chronicle.
- Answer: `GuardDuty`
### Question 20: What was the ID of the detector the TA deleted?
- Analysis note: The next action by the TA, was to DeleteDetector, and in the log it's possible to view the
requestParameters which shows the detectorId.
Using Chronicle.
- Answer: `00c9d931bcc21531a8a27c046903bc2f`
### Question 21: Which AWS service did the user target next for discovery activities?
- Analysis note: The compromised user performs DescribeLogGroups which lists all the log groups
(unless filter specified) for the CloudWatch service in the AWS account.
In the Splunk screenshot from Question 19, after GuardDuty we see evidence of logs.
Using Chronicle.
- Answer: `CloudWatch`
### Question 22: What is the ARN of the response to the aforementioned request by the TA?
- Analysis note: From the aforementioned log, it's also possible to identify the response returned to the
Threat Actor. This is for the CloudTrail log group.
Using Chronicle.
- Answer: `arn:aws:logs:eu-west-1:857609373938:log-group:aws-cloudtrail-logs-`
### Question 23: What was the TA first action with S3?
- Analysis note: The TA's first action was to discover what S3 buckets were available, this was
performed using ListBuckets action.
Again looking at the Splunk screenshot from Question 19, after the logs we see actions
in S3, the first being List buckets.
Using Chronicle.
- Answer: `ListBuckets`
### Question 24: Immediately before exfiltration, what was the TA final request?
- Analysis note: The TA requested all the Objects in the S3 bucket percypay-payment-data, using the
prefix CustomerB/2024-12-09/ to only get results for that directory. As we establishing
earlier in this scenario, the TA was specifically exfiltrating data associated with that
Customer and that day.
Using Chronicle.
- Answer: `ListObject`
### Question 25: After the exfiltration, what Role did the TA create?
- Analysis note: The TA continues their attack, by creating another role.
Using Chronicle.
- Answer: `arn:aws:iam::857609373938:role/replicator-role`
### Question 26: What was the name of the Policy applied to that role?
- Analysis note: The TA continues by using PutRolePolicy to apply a Policy directly to that role.
Using Chronicle.
- Answer: `replicator-policy`
### Question 27: The Policy allows ssss3333::::RRRReeeepppplllliiiiccccaaaatttteeeeOOOObbbbjjjjeeeecccctttt action for what resource?
- Analysis note: The Policy applied allows replicating objects for the resource apt-we-love-transactions
S3 bucket.
Using Chronicle.
- Answer: `arn:aws:s3:::apt-we-love-transactions/*`
### Question 28: The TA attempts PPPPuuuuttttBBBBuuuucccckkkkeeeettttRRRReeeepppplllliiiiccccaaaattttiiiioooonnnn action, what was the error message?
- Analysis note: Applying bucket replication would allow the TA continued access to the data, via their
S3 bucket, until the replication was removed. It failed to be applied - InvalidRequest
error code can be seen in the log, with further details in the error message.
Using Chronicle.
- Answer: `Destination bucket must exist.`
### Question 29: What IAM User did the TA create?
- Analysis note: The TA has now moved to exploring further persistence options, and created a new
user.
Using Chronicle.
- Answer: `tfe-user`
### Question 30: When was the AdministratorAccess policy attached to the newly created user?
- Analysis note: The TA continues to use percypay-webapp-user to apply a permissive policy to the new
user.
Using Chronicle.
- Answer: `2024-12-15 20:53:26`
### Question 31: What was the Access Key ID for the new user?
- Analysis note: The TA creates an Access Key, giving them ability to perform actions as this new user.
Not to be confused with the access key of the requesting user.
Using Chronicle.
- Answer: `AKIA4PLMARDZ[REDACTED]` (AWS Access Key - redacted for security)
### Question 32: What time was the new user first used?
- Analysis note: Using the aforementioned Access Key ID, we can pivot to explore activity completed
with this user.
Using Chronicle.
- Answer: `2024-12-15 20:54:42`
### Question 33: For this user, what IP address was the TA using?
- Analysis note: The TA has switched IP address again.
Using Chronicle.
- Answer: `89.187.177.75`
### Question 34: What Service did the TA stop?
- Analysis note: Once the TA has described the Trails, to identify what's in use, they
move onto stopping logging. Thus disabling CloudTrail.
Using Chronicle.
- Answer: `CloudTrail`
### Question 35: What anomaly user event occurred before the original User was compromised?
- Analysis note: Looking back to Question 8, the compromised user was first used 2024-12-15T20:42:16Z
Exploring activity in the days before this timestamp, there's a bunch of typical event activity
performed by usual users. Amongst it though is an anomaly, being developer-dan user.
Filtering on this specific user, there's a single PutObject event.
Using Chronicle.
- Answer: `PutObject`
### Question 36: What was the ARN for resource uploaded to ppppeeeerrrrccccyyyyppppaaaayyyy----wwwweeeebbbbssssiiiitttteeee----hhhhoooosssstttt ?
- Analysis note: The event was putting an object into the percypay-website-host bucket.
Using Chronicle.
- Answer: `arn:aws:s3:::percypay-website-host/backend-access-key.html`
### Question 37: What was the Access Key Secret for the original compromised user?
- Analysis note: Inspecting the uploaded file, it's possible to see the source code unfortunately leaked the
AWS credentials, and this is believe to be the root cause of the user compromise.
- Answer: `[REDACTED]` (AWS Secret Access Key - redacted for security)

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Which S3 bucket was the affected file stored in? | percypay-payment-data |
| Which AWS IAM user interacted with the file? | arn:aws:iam::857609373938:user/percypay-webapp-user |
| What AWS Access Key should be revoked, as part of response action? | AKIA4PLMARDZ[REDACTED] |
| What was the Threat Actor's (TA) IP address? | 149.102.244.70 |
| What was the blast radius, how many files were impacted? | 164 |
| Which Customer's data has been impacted? | CustomerB |
| What date was the payment data from? | 2024-12-09 |
| What was the time for initial event from this user? | 2024-12-15 20:42:16 |
| How many IP addresses did the TA use for this user? | 3 |
| ARN (Amazon Resource Name): The ARN associated with the calling entity. | GetCallerIdentity |
| What was the first IAM Policy the TA reviewed? | lambda-export-data |
| What operation did the TA perform to alter IAM Policy permissions available to the
user? | SetDefaultPolicyVersion |

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

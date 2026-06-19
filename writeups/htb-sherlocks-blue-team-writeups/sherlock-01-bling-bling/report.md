---
layout: page
title: "Sherlock: Bling Bling - Report"
permalink: /writeups/htb-sherlocks-blue-team-writeups/sherlock-01-bling-bling/report/
---

![Bling Bling cover](/assets/portfolio-assets/writeups/hackthebox-sherlocks/thumbs/sherlock-01-bling-bling.png)

# Bling Bling

## Overview

| Field | Value |
| --- | --- |
| Source PDF | `BlingBling.pdf` |
| Pages | 9 |
| Difficulty | Easy |
| Prepared by | felamos |
| Author | felamos |

## Scenario Summary

It's the festive season of Diwali, and a newly launched website, Bling-Bling Crackers (a fictional
site, inspired by platforms like Amazon and Flipkart), is offering huge discounts and free gifts
for new users. To celebrate the festival of lights, Deepam Mart has launched a "Diwali
Dhamaka" sale, offering 1 products, 50% off discounts, and free gifts like Diwali decorations
and sweets for first-time users. The company Bling-Bling Crackers uses StoreD.

## Investigation Objective

Identify the activity described in the scenario, analyze the provided artifacts, answer the investigation questions, and document evidence in a repeatable Blue Team report format.

## Evidence Provided

bf470e205234a1312c94e6ee3f6d648c artifacts/opsk-5.zip

## Tools Used

| Tool | Purpose |
| --- | --- |
| Neo4j | Used or likely relevant based on the source writeup |

## Investigation Process

### Question 1: Total number of Nodes in the database?
- Analysis note: The database information panel displays the total number of nodes and relationships.
However, you can also retrieve this information using the following query:
MATCH (n) RETURN count(n);
- Answer: `2802`
### Question 2: How many Account nodes does the database have?
- Analysis note: The relationship data reveals that Account nodes are connected to Credit Card nodes,
which will be useful for later queries.
To find the total number of Account nodes, you can check the database information or use
this query:
MATCH (n:Account) RETURN count(n);
- Answer: `1406`
### Question 3: How many accounts are registered from the IP address 88.236.1.190?
- Analysis note: Each Account node has several properties, including register_ip_address, which records
the IP address used during account registration. Use the following query to find the count
of accounts registered with a specific IP address:
match (n:Account) where n.register_ip_address = "88.236.1.190" return
count(n)
The 22 accounts registered with this IP might suggest a single owner or could indicate
shared usage through NAT 
- Answer: `22`
### Question 4: How many Users have created multiple accounts with same IP address?
- Analysis note: To identify other accounts created from the same IP address (not just the specific IP
given), use this query to detect potential fraudulent activities:
MATCH (n:Account)
WITH n.register_ip_address AS prop1, COLLECT(n) AS nodes
WHERE SIZE(nodes) > 1
RETURN prop1, SIZE(nodes) AS duplicate_count
22 + 16 = 38
- Answer: `38`
### Question 5: What physical address has been used multiple times?
- Analysis note: We can also investigate shared physical addresses, which are more challenging to change
than IP addresses due to delivery requirements. Use the following query:
MATCH (n:Account)
WITH n.address AS prop1, COLLECT(n) AS nodes
WHERE SIZE(nodes) > 1
RETURN prop1, SIZE(nodes) AS duplicate_count
"19/63, Krishnan Ganj, Danapur 441303"
- Answer: `19/63, Krishnan Ganj, Danapur 441303`
### Question 6: Which Credit Card number is attached to multiple accounts?
- Analysis note: Additionally, to detect potential credit card fraud (e.g., a single credit card number being
associated with multiple accounts), use the query below:
MATCH (c:CreditCard)-[r:HAS_CREDITCARD]-()
WITH c, COUNT(r) AS relationship_count
WHERE relationship_count > 1
RETURN c, relationship_count
- Answer: `371593995427734`
### Question 7: When was the account with username obhandari created?
- Analysis note: To determine when a specific account was created, use this query to see if the creation
date aligns with any suspicious activity:
match (m:Account) where m.username = "obhandari" return m.created_at
- Answer: `2024-11-08 07:42:20.228775`
### Question 8: How many accounts using the credit card number from question 6 use the same
registered IP address?
- Analysis note: Finally, if you need to check the number of accounts using the same credit card and
registered from the same IP address, the following query provides the count:
MATCH (c:CreditCard)-[r:HAS_CREDITCARD]-()
WITH c, COUNT(r) AS relationship_count
WHERE relationship_count > 1
RETURN relationship_count
- Answer: `11`

## Key Findings

| Finding / Question | Answer / Evidence |
| --- | --- |
| Total number of Nodes in the database? | 2802 |
| How many Account nodes does the database have? | 1406 |
| How many accounts are registered from the IP address 88.236.1.190? | 22 |
| How many Users have created multiple accounts with same IP address? | 38 |
| What physical address has been used multiple times? | 19/63, Krishnan Ganj, Danapur 441303 |
| Which Credit Card number is attached to multiple accounts? | 371593995427734 |
| When was the account with username obhandari created? | 2024-11-08 07:42:20.228775 |
| How many accounts using the credit card number from question 6 use the same
registered IP address? | 11 |

## Attack Timeline

See `timeline.md` for extracted timestamps and timeline notes.

## Indicators of Compromise

See `iocs.md` for extracted indicators and context.

## MITRE ATT&CK Mapping

| Tactic | Technique | Evidence |
| --- | --- | --- |
| Discovery | System / Network Discovery | Observed in extracted case notes; validate with report evidence. |
| Collection | Data from Local System / Cloud Storage | Observed in extracted case notes; validate with report evidence. |
| Exfiltration | Exfiltration Over Web Service | Observed in extracted case notes; validate with report evidence. |

## Impact Assessment

Assess affected users, hosts, accounts, data exposure, and operational risk after validating the evidence.

## Recommendations

- Preserve original artifacts and document hashes.
- Validate suspicious accounts, hosts, IP addresses, domains, and files.
- Add detections for the confirmed behaviors.
- Review access control and logging gaps found during the investigation.

## Lessons Learned

Data Analysis
Query Construction

## Conclusion

This writeup documents the investigation flow, key evidence, answers, and lessons learned from the Sherlock challenge.






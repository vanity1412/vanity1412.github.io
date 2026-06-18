---
title: "Beacon Detection Challenge: following C2-like traffic rhythm"
date: 2025-10-31 09:00:00 +0700
categories: [Blue Team, Threat Hunting]
tags: [soc, threat-hunting, c2-detection, network-security]
description: "A lightweight hunting note for repeated outbound traffic, C2 beacon hypotheses, and network log validation."
image:
  path: /assets/portfolio-assets/img/Blueteam.png
  alt: Blue Team
---

## Context

A lab host creates outbound connections at a repeated interval. This pattern may come from legitimate software, an administration agent, or C2 beaconing. The goal is to validate the hypothesis with evidence instead of jumping to a conclusion.

## Approach

1. Group connections by `src_ip`, `dst_ip`, `dst_port`, and timestamp.
2. Measure the interval between requests and check for a stable rhythm.
3. Review the domain, user-agent, JA3/JA4, or TLS metadata if available.
4. Correlate the network activity with endpoint process data.
5. Hunt for other hosts with similar behavior.

## Notable signals

- Repeated connections with low jitter.
- Similar payload or response size.
- Newly registered domains, unusual DNS behavior, or low-reputation IPs.
- A process creating network connections that does not match the host role.

## Hunting note

```sql
-- Query idea, adjust it to the actual SIEM schema.
SELECT src_ip, dst_ip, dst_port, COUNT(*) AS hits
FROM network_events
WHERE timestamp > NOW() - INTERVAL '24 hours'
GROUP BY src_ip, dst_ip, dst_port
HAVING hits > 20;
```

## Conclusion

A good writeup should separate observation, hypothesis, and confirmed evidence. If the evidence is incomplete, write the finding as suspicious beaconing and list what additional data is needed.

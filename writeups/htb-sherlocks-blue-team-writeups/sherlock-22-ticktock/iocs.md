# IOCs - TickTock

| Type | Value | Context |
| --- | --- | --- |
| IPv4 | 52.56.142.81 | We perform a search in Splunk to locate any top talking IPs within the event logs. The IP 52.56.142.81 is found communicating within the sysmon logs out of the network 357 times. T |
| IPv4 | 10.10.0.79 | -000000000700",RuleName: Usermode,SourceHostname: DESKTOP- R30EAMH.forela.local,SourceIp: 10.10.0.79,DestinationHostname: ec2- 52-56-142-81.eu-west-2.compute.amazonaws.com,Destinat |
| Hash | 1cb5d3267271978ed0bd1eb0d667932e59a45aa8daa8a330e4fd62d6e80c6f4a | cts Provided Enter the artefacts provided along with their file hash here. ticktock.zip - 1cb5d3267271978ed0bd1eb0d667932e59a45aa8daa8a330e4fd62d6e80c6f4a Containing a KAPE output |
| Hash | ac688f1ba6d4b23899750b86521331d7f7ccfb69 | swered within initial analysis. 9. What is the SHA1 and SHA2 sum of the malicious binary? ac688f1ba6d4b23899750b86521331d7f7ccfb69:42ec59f760d8b6a50bbc7187829f62c3b 6b8e1b841164e71 |
| Domain | R30EAMH.forela.local | sGUID: 5080714d-89ce-6453- c202-000000000700",RuleName: Usermode,SourceHostname: DESKTOP- R30EAMH.forela.local,SourceIp: 10.10.0.79,DestinationHostname: ec2- 52-56-142-81.eu-west-2 |
| Domain | 52-56-142-81.eu-west-2.compute.amazonaws.com | rceHostname: DESKTOP- R30EAMH.forela.local,SourceIp: 10.10.0.79,DestinationHostname: ec2- 52-56-142-81.eu-west-2.compute.amazonaws.com,DestinationIp: 52.56.142.81,,False,C:\Users\s |
| Domain | west-2.compute.amazonaws.com | "":""52.56.142.81""}, {""@Name"":""DestinationHostname"",""#text"":""ec2-52-56-142-81.eu- west-2.compute.amazonaws.com""}, {""@Name"":""DestinationPort"",""#text"":""80""}, {""@Nam |
| Domain | ec2-52-56-142-81.eu-west-2.compute.amazonaws.com | process ID, destination IP & hostname: Destination IP: 52.56.142.81 Destination hostname: ec2-52-56-142-81.eu-west-2.compute.amazonaws.com Process ID: 5768 Merlin Location on FS: C |

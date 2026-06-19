# IOCs - Knock Knock

| Type | Value | Context |
| --- | --- | --- |
| IPv4 | 3.13.65.234 | ated with via TCP with the syn flag set. fetch.sh #!/bin/bash # Define variables DB_HOST="3.13.65.234" DB_PORT="3306" DB_USER="tony.shephard" DB_PASSWORD="GameOfthronesRocks7865!" |
| IPv4 | 13.233.179.35 | is we can also extract the IP addresses the unusual files above were transferred to/from: 13.233.179.35 -> Forela host (Ransomware2_Server.zip) - 2023-03-21 11:42:34 UTC, HTTP Fore |
| IPv4 | 3.109.209.43 | 35 -> Forela host (Ransomware2_Server.zip) - 2023-03-21 11:42:34 UTC, HTTP Forela host -> 3.109.209.43 (backup) - 2023-03-21 10:52:03 UTC, FTP Forela host -> 3.109.209.43 (fetch.sh |
| IPv4 | 1.1.1.1 | o -o UserKnownHostsFile=/dev/null {{ ssh_user }}@{{ inventory_hostname }} 'id;whoami;ping 1.1.1.1' - name: Clean up /tmp directory every 5 hours become_user: root become_method: su |
| Hash | 85D7DCBC8764A8422AE1F1C3E069FF87 | ed the packet capture to analyze how attacker got access. Artefacts provided Capture.pcap 85D7DCBC8764A8422AE1F1C3E069FF87 Skills Learnt Network Forensics PCAP Analysis Wireshark f |
| Hash | ccc387e5a6fc0a7c727162a433d6c82144d6c6eb | onfiguration to make the yaml "more secure". sebh24@rabat:/tmp/forela-dev$ git log commit ccc387e5a6fc0a7c727162a433d6c82144d6c6eb (HEAD -> main, origin/main, origin/HEAD) Author: |
| Hash | ab04702b3269f016def0521a734380fb12596994 | .noreply.github.com> Date: Tue Mar 21 16:13:57 2023 +0500 Update internal-dev.yaml commit ab04702b3269f016def0521a734380fb12596994 Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | ffee1d9c3150b182c4d029d272745e308a8537a6 | -dev.yaml Updated the script to be more secure. Earlier configuration was insecure commit ffee1d9c3150b182c4d029d272745e308a8537a6 Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | c6337958b97d8db407ffcfe027e864abcde4dddc | .noreply.github.com> Date: Mon Mar 20 16:03:40 2023 +0500 Update internal-dev.yaml commit c6337958b97d8db407ffcfe027e864abcde4dddc Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | 182da42155d49211abc628c01afe8bda5ab8fcae | ie@users.noreply.github.com> Date: Mon Mar 20 16:02:15 2023 +0500 Update README.md commit 182da42155d49211abc628c01afe8bda5ab8fcae Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | a851be6fabbaa7e3719d048100b9dd6b91a72353 | Mon Mar 20 15:59:12 2023 +0500 Create internal-dev.yaml Ansible script for testing commit a851be6fabbaa7e3719d048100b9dd6b91a72353 Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | 002aaca44db0a65841a9ff0f0a60f51417cb994f | Junnkie@users.noreply.github.com> Date: Mon Mar 20 15:39:02 2023 +0500 Delete test commit 002aaca44db0a65841a9ff0f0a60f51417cb994f Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | 9963a8570720d8873ab64e3b11291f5bcd00ac78 | Junnkie@users.noreply.github.com> Date: Mon Mar 20 15:28:57 2023 +0500 Update test commit 9963a8570720d8873ab64e3b11291f5bcd00ac78 Author: CyberJunnkie <76212264+CyberJunnkie@users |
| Hash | 033aaef91cb0d51839708632bb32695fd5637992 | Junnkie@users.noreply.github.com> Date: Mon Mar 20 15:27:52 2023 +0500 Create test commit 033aaef91cb0d51839708632bb32695fd5637992 Author: brown249 <85936721+brown249@users.noreply |
| URL | http://13.233.1 | cture: We can see under the directory structure that the file was downloaded from the uri http://13.233.1 79.35/PKCampaign/Targets/Forela/Ransomware2_server.zip Whilst we are perfo |
| URL | http://dev.forela.co.uk/internal/secrets/cyberjunkie- | .dev gather_facts: no become: yes tasks: - name: Download SSH key from URL get_url: url: "http://dev.forela.co.uk/internal/secrets/cyberjunkie- internal.pem" dest: "/tmp/cyberjunki |
| URL | https://github.com/forela-finance/forela-dev | thin the yaml. We move forward and git clone the repository. sebh24@rabat:/tmp$ git clone https://github.com/forela-finance/forela-dev Cloning into 'forela-dev'... remote: Enumerat |
| URL | http://13.233.179.35/PKCampaign/Targets/Forela/Ransomware2_Server.zip | ho "Logged in via SSH"' Q19 Whats the full url from where attacker downloaded ransomware? http://13.233.179.35/PKCampaign/Targets/Forela/Ransomware2_Server.zip Q20 Whats the tool/u |
| Email | 76212264+CyberJunnkie@users.noreply.github.com | 7c727162a433d6c82144d6c6eb (HEAD -> main, origin/main, origin/HEAD) Author: CyberJunnkie <76212264+CyberJunnkie@users.noreply.github.com> Date: Tue Mar 21 16:13:57 2023 +0500 Updat |
| Email | 85936721+brown249@users.noreply.github.com | 2023 +0500 Create test commit 033aaef91cb0d51839708632bb32695fd5637992 Author: brown249 <85936721+brown249@users.noreply.github.com> Date: Mon Mar 20 10:24:40 2023 +0000 Initial co |
| Domain | forela-internal.dev | ev.yaml as detailed bekow, containing the URL for the relevant SSH key file. --- - hosts: forela-internal.dev gather_facts: no become: yes tasks: - name: Download SSH key from URL |
| Domain | github.com | yaml. We move forward and git clone the repository. sebh24@rabat:/tmp$ git clone https://github.com/forela-finance/forela-dev Cloning into 'forela-dev'... remote: Enumerating objec |
| Domain | users.noreply.github.com | c6eb (HEAD -> main, origin/main, origin/HEAD) Author: CyberJunnkie <76212264+CyberJunnkie@users.noreply.github.com> Date: Tue Mar 21 16:13:57 2023 +0500 Update internal-dev.yaml co |

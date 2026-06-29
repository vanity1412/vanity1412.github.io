---
layout: page-toc
title: "V1T CTF 2026 - BasicQnA Forensics"
description: "Network forensics writeup for V1T CTF 2026 BasicQnA."
permalink: /writeups/v1t-ctf-2026/basicqna-forensics/
toc: true
render_with_liquid: false
---

# Write-up CTF: Forensics Basic QnA

## Thông tin challenge

- **Tên challenge:** BasicQnA / Forensics Basic QnA
- **Category:** Forensics / Network Analysis / Web Attack Investigation
- **File phân tích:** `challenge.pcapng`
- **Mục tiêu:** Phân tích lưu lượng mạng trong file PCAPNG để trả lời 9 câu hỏi điều tra, từ đó lấy flag cuối cùng.
- **Flag cuối cùng:** `v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}`

---

# 1. Tóm tắt bài challenge

File được cung cấp là một file **PCAPNG** chứa lưu lượng mạng giữa một máy nghi là attacker và một web server nạn nhân. Dựa vào các gói tin trong capture, cần xác định:

1. IP attacker và victim.
2. Dịch vụ SSH đang chạy trên victim.
3. Công cụ reconnaissance attacker sử dụng.
4. TCP stream thể hiện attacker tạo thành công tài khoản admin tạm thời.
5. Tài khoản admin tạm thời được tạo.
6. CVE liên quan đến kỹ thuật bị abuse.
7. Tham số bị abuse để đạt RCE.
8. Hai file attacker đọc sau khi có command execution.
9. Github ID tìm được.

Dấu hiệu ban đầu cho thấy bài này đi theo hướng **network forensics** vì dữ liệu nằm trong file capture, có nhiều HTTP request/response, SSH banner, User-Agent, cookie session và payload có dấu hiệu command injection.

---

# 2. Công cụ sử dụng

| Công cụ | Mục đích sử dụng | Ý nghĩa |
|---|---|---|
| `file` | Kiểm tra loại file ban đầu | Xác nhận file là PCAPNG |
| `Wireshark` | Phân tích trực quan packet, follow TCP stream | Xem rõ request/response HTTP và stream ID |
| `tshark` | Trích xuất dữ liệu PCAP bằng dòng lệnh | Tìm IP, HTTP request, User-Agent, TCP stream |
| `strings` | Tìm chuỗi ASCII trong PCAP | Nhanh chóng phát hiện banner, payload, account, flag |
| `grep` | Lọc chuỗi quan trọng | Tìm các keyword như `Nmap`, `OpenSSH`, `backup_name`, `.env` |
| `CyberChef` | Decode URL encoding khi cần | Đọc rõ payload có `%3B`, `%2F`, `%24` |
| Browser / Web challenge page | Submit từng đáp án | Xác minh đáp án đúng/sai |

---

# 3. Quy trình phân tích từng bước

## Bước 1: Kiểm tra file ban đầu

### Mục tiêu

Xác định file được cung cấp thuộc loại gì và có thể phân tích bằng công cụ nào.

### Lệnh

```bash
file challenge.pcapng
```

### Kết quả kỳ vọng

```text
challenge.pcapng: pcapng capture file - version 1.0
```

### Ý nghĩa

Kết quả cho thấy đây là file packet capture dạng PCAPNG, phù hợp để phân tích bằng Wireshark hoặc tshark.

---

## Bước 2: Xác định IP attacker và victim

### Mục tiêu

Tìm hai IP chính xuất hiện trong quá trình tấn công: máy gửi nhiều request bất thường là attacker, máy nhận request là victim.

### Lệnh gợi ý với tshark

```bash
tshark -r challenge.pcapng -q -z conv,ip
```

Hoặc lọc các request HTTP:

```bash
tshark -r challenge.pcapng -Y "http.request" -T fields -e ip.src -e ip.dst -e http.request.method -e http.request.uri
```

### Phân tích

Trong capture, IP `172.29.9.159` gửi nhiều request/scan đến IP `13.212.67.96`. Các request bao gồm truy cập web, kiểm tra endpoint, scan service và request có User-Agent của Nmap.

### Kết luận

- **Attacker IP:** `172.29.9.159`
- **Victim IP:** `13.212.67.96`

**Q1 answer:**

```text
172.29.9.159,13.212.67.96
```

---

## Bước 3: Xác định SSH service/version trên victim

### Mục tiêu

Tìm banner SSH trả về từ victim. Banner SSH thường có dạng:

```text
SSH-2.0-OpenSSH_x.x distro
```

### Lệnh gợi ý

```bash
strings -a challenge.pcapng | grep -i "OpenSSH"
```

Hoặc với tshark:

```bash
tshark -r challenge.pcapng -Y "tcp.port == 22" -T fields -e data.text
```

### Bằng chứng

Trong PCAP có banner:

```text
SSH-2.0-OpenSSH_10.2p1 Ubuntu-2ubuntu3.2
```

Theo format câu hỏi `service_version distro_version`, cần bỏ phần `SSH-2.0-`.

### Kết luận

**Q2 answer:**

```text
OpenSSH_10.2p1 Ubuntu-2ubuntu3.2
```

---

## Bước 4: Xác định tool reconnaissance attacker sử dụng

### Mục tiêu

Tìm dấu hiệu scan/reconnaissance trong traffic, đặc biệt là User-Agent hoặc probe đặc trưng của tool.

### Lệnh

```bash
strings -a challenge.pcapng | grep -i "Nmap"
```

### Bằng chứng

Trong PCAP xuất hiện User-Agent:

```text
User-Agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
```

Ngoài ra còn có SSH probe liên quan đến Nmap:

```text
SSH-2.0-Nmap-SSH2-Hostkey
SSH-1.5-NmapNSE_1.0
```

### Kết luận

Tool reconnaissance là **Nmap**.

**Q3 answer:**

```text
Nmap
```

---

## Bước 5: Tìm TCP stream tạo temporary admin account

### Mục tiêu

Tìm request/response chứng minh attacker tạo thành công tài khoản admin tạm thời.

### Cách làm trên Wireshark

1. Mở `challenge.pcapng` bằng Wireshark.
2. Dùng filter:

```text
http contains "Temporary support access created"
```

3. Chọn packet match.
4. Right click → **Follow** → **TCP Stream**.
5. Xem stream ID tương ứng.

### Lệnh gợi ý với tshark

```bash
tshark -r challenge.pcapng -Y 'http contains "Temporary support access created"' -T fields -e frame.number -e tcp.stream -e ip.src -e ip.dst
```

Hoặc tìm action AJAX:

```bash
tshark -r challenge.pcapng -Y 'http contains "wpgmp_temp_access_ajax"' -T fields -e frame.number -e tcp.stream -e http.request.method -e http.request.uri
```

### Bằng chứng kỹ thuật

Response trả về:

```json
{"message":"Temporary support access created.","role":"admin","success":true,"support_url":"http://13.212.67.96/magic-login/GsheBj53E0_rg1qnYAnIQYgNBJcGMzbL","user":"support_c30cde@corpvault.local"}
```

Luồng TCP chứa bằng chứng tạo account thành công là:

```text
tcp.stream eq 4491
```

### Kết luận

**Q4 answer:**

```text
tcp.stream eq 4491
```

---

## Bước 6: Xác định temporary admin account

### Mục tiêu

Từ response tạo account, lấy email tài khoản admin tạm thời attacker đã tạo.

### Lệnh

```bash
strings -a challenge.pcapng | grep -i "Temporary support access created" -A 2
```

Hoặc:

```bash
strings -a challenge.pcapng | grep -i "support_"
```

### Bằng chứng

Trong JSON response:

```json
"user":"support_c30cde@corpvault.local"
```

Trong audit log cũng thể hiện:

```html
support_c30cde@corpvault.local - Temporary admin account created by public AJAX support handler
```

### Kết luận

**Q5 answer:**

```text
support_c30cde@corpvault.local
```

---

## Bước 7: Xác định CVE của kỹ thuật bị abuse

### Mục tiêu

Liên kết action bị abuse với lỗ hổng/CVE tương ứng.

### Dấu hiệu chính

Trong PCAP có action:

```text
wpgmp_temp_access_ajax
```

Đây là public AJAX support handler cho phép tạo temporary admin account. Hành vi này tương ứng với kỹ thuật **Unauthenticated Privilege Escalation via Administrator Account Creation** trong plugin WP Maps Pro.

### Kết luận

CVE liên quan là:

```text
CVE-2026-8732
```

**Q6 answer:**

```text
CVE-2026-8732
```

---

## Bước 8: Phân tích RCE qua backup feature

### Mục tiêu

Sau khi có tài khoản admin tạm thời, attacker truy cập chức năng maintenance/backup và lạm dụng input người dùng để thực thi lệnh hệ thống.

### Dấu hiệu bất thường

Form backup có input:

```html
<input name="backup_name" value="daily-contracts" placeholder="daily-contracts">
```

Attacker thay giá trị bình thường bằng payload có dấu `;` để nối lệnh shell:

```text
backup_name=daily-contracts%3B+echo+HOME%3D%24HOME%3B+pwd%3B+ls+-la+~
```

Decode URL encoding:

```text
backup_name=daily-contracts; echo HOME=$HOME; pwd; ls -la ~
```

### Giải thích kỹ thuật

- `%3B` là ký tự `;` sau khi decode.
- Trong shell, `;` dùng để kết thúc lệnh hiện tại và chạy lệnh mới.
- Nếu backend ghép trực tiếp `backup_name` vào command mà không sanitize/escape, attacker có thể command injection.

Ví dụ command preview trong response:

```html
<pre class="terminal">echo Building backup package: daily-contracts; whoami; ls /</pre>
```

### Kết luận

Tham số user-controlled bị abuse để đạt RCE là:

```text
backup_name
```

**Q7 answer:**

```text
backup_name
```

---

## Bước 9: Xác định hai file attacker đọc sau RCE

### Mục tiêu

Tìm các lệnh đọc file nhạy cảm sau khi attacker có command execution.

### Lệnh

```bash
strings -a challenge.pcapng | grep -i "cat" -C 3
```

Hoặc lọc request POST có `backup_name`:

```bash
tshark -r challenge.pcapng -Y 'http.request.method == "POST" && http contains "backup_name"' -T fields -e tcp.stream -e http.file_data
```

### Bằng chứng

Attacker đọc file thứ nhất:

```text
backup_name=daily-contracts%3B+cat+%2Fapp%2Fstatic%2F.env
```

Decode:

```text
backup_name=daily-contracts; cat /app/static/.env
```

Response trả về:

```text
Building backup package: daily-contracts
Ich1ck3nPlus:<REDACTED_GITHUB_PAT>
```

Attacker đọc file thứ hai:

```text
backup_name=daily-contracts%3B+cat+%2Fapp%2Ftemplates%2F.env
```

Decode:

```text
backup_name=daily-contracts; cat /app/templates/.env
```

Response trả về:

```text
Building backup package: daily-contracts
Ich1ck3nPlus/final
```

### Kết luận

Hai file attacker đọc là:

```text
/app/static/.env,/app/templates/.env
```

**Q8 answer:**

```text
/app/static/.env,/app/templates/.env
```

---

## Bước 10: Tìm Github ID

### Mục tiêu

Từ nội dung hai file `.env`, xác định Github ID được nhắc tới.

### Bằng chứng

File `/app/static/.env` lộ thông tin dạng:

```text
Ich1ck3nPlus:<REDACTED_GITHUB_PAT>
```

File `/app/templates/.env` lộ magic string:

```text
Ich1ck3nPlus/final
```

Câu hỏi yêu cầu **Github ID**, không yêu cầu repo path. Vì vậy chỉ lấy username/ID:

```text
Ich1ck3nPlus
```

### Kết luận

**Q9 answer:**

```text
Ich1ck3nPlus
```

---

# 4. Bảng tổng hợp đáp án 9 câu

| Câu | Nội dung | Đáp án |
|---|---|---|
| Q1 | Attacker IP và victim IP | `172.29.9.159,13.212.67.96` |
| Q2 | SSH service/version | `OpenSSH_10.2p1 Ubuntu-2ubuntu3.2` |
| Q3 | Reconnaissance tool | `Nmap` |
| Q4 | TCP stream tạo temporary admin | `tcp.stream eq 4491` |
| Q5 | Temporary admin account | `support_c30cde@corpvault.local` |
| Q6 | CVE bị abuse | `CVE-2026-8732` |
| Q7 | Parameter bị abuse để RCE | `backup_name` |
| Q8 | Hai file attacker đọc | `/app/static/.env,/app/templates/.env` |
| Q9 | Github ID | `Ich1ck3nPlus` |

---

# 5. Phân tích kỹ thuật chi tiết

## 5.1. Reconnaissance

Attacker bắt đầu bằng việc quét dịch vụ và thu thập thông tin. Dấu hiệu rõ nhất là User-Agent của Nmap Scripting Engine:

```text
User-Agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
```

Ngoài HTTP, attacker còn probe SSH và nhận banner:

```text
SSH-2.0-OpenSSH_10.2p1 Ubuntu-2ubuntu3.2
```

Điều này cho thấy attacker đang fingerprint dịch vụ trên victim.

## 5.2. Initial access / Privilege escalation

Sau bước recon, attacker abuse endpoint AJAX:

```text
wpgmp_temp_access_ajax
```

Response trả về cho biết tài khoản temporary support được tạo với quyền admin:

```json
{"message":"Temporary support access created.","role":"admin","success":true,"user":"support_c30cde@corpvault.local"}
```

Đây là hành vi privilege escalation vì attacker từ trạng thái chưa có quyền admin đã tạo được tài khoản admin tạm thời.

## 5.3. Abuse magic login

Response còn chứa `support_url`:

```text
http://13.212.67.96/magic-login/GsheBj53E0_rg1qnYAnIQYgNBJcGMzbL
```

Magic link này cho phép attacker đăng nhập bằng tài khoản temporary admin mà không cần biết mật khẩu.

Audit log trong web app ghi nhận:

```text
support_c30cde@corpvault.local - Logged in using temporary support magic link
```

## 5.4. Command injection qua backup feature

Sau khi đăng nhập admin, attacker truy cập chức năng Maintenance Backup. Input `backup_name` được ghép vào shell command.

Giá trị bình thường:

```text
daily-contracts
```

Giá trị attacker gửi:

```text
daily-contracts; whoami; ls /
```

Dấu `;` làm command ban đầu bị nối thêm command mới. Đây là dấu hiệu điển hình của command injection.

## 5.5. Đọc file nhạy cảm

Attacker tiếp tục dùng RCE để đọc file `.env`:

```bash
cat /app/static/.env
cat /app/templates/.env
```

Kết quả trả về làm lộ GitHub ID, token GitHub và magic string.

## 5.6. IOC và artifact

| Loại | Giá trị | Ý nghĩa |
|---|---|---|
| Attacker IP trong PCAP | `172.29.9.159` | Máy tạo traffic tấn công trong capture |
| Victim IP | `13.212.67.96` | Web server/SSH server bị tấn công |
| Public IP trong audit log | `171.250.164.212` | IP được ứng dụng ghi nhận trong audit log |
| Recon tool | `Nmap` | Công cụ scan/fingerprint |
| SSH banner | `OpenSSH_10.2p1 Ubuntu-2ubuntu3.2` | Phiên bản SSH của victim |
| Exploited action | `wpgmp_temp_access_ajax` | Public AJAX handler bị abuse |
| Temporary admin | `support_c30cde@corpvault.local` | Account admin attacker tạo |
| RCE parameter | `backup_name` | Input bị command injection |
| Sensitive files | `/app/static/.env`, `/app/templates/.env` | File bị đọc sau RCE |
| GitHub ID | `Ich1ck3nPlus` | ID tìm được từ `.env` |

---

# 6. Script Python hỗ trợ trích xuất artifact

Script dưới đây không thay thế Wireshark/tshark, nhưng có thể dùng để quét nhanh các chuỗi quan trọng trong PCAPNG.

```python
#!/usr/bin/env python3
import re
from pathlib import Path

pcap_path = Path("challenge.pcapng")

data = pcap_path.read_bytes()

# Extract printable ASCII strings with length >= 4
strings = re.findall(rb"[\x20-\x7e]{4,}", data)
strings = [s.decode("utf-8", errors="ignore") for s in strings]

keywords = [
    "OpenSSH",
    "Nmap",
    "wpgmp_temp_access_ajax",
    "Temporary support access created",
    "support_",
    "backup_name",
    "/app/static/.env",
    "/app/templates/.env",
    "github_pat",
    "Ich1ck3nPlus",
    "v1t{",
]

for keyword in keywords:
    print(f"\n===== Keyword: {keyword} =====")
    for line in strings:
        if keyword.lower() in line.lower():
            print(line)
```

### Cách chạy

```bash
python3 extract_artifacts.py
```

### Ý nghĩa

Script đọc file PCAPNG ở dạng binary, trích các chuỗi ASCII có thể đọc được, sau đó lọc các keyword liên quan đến quá trình tấn công. Cách này hữu ích khi cần rà nhanh artifact trước khi phân tích sâu bằng Wireshark.

---

# 7. Flag cuối cùng

Sau khi submit đúng 9 câu hỏi, hệ thống trả về flag:

```text
v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}
```

**FLAG tìm được:** `v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}`

Mức độ chắc chắn: **cao**, vì flag được trả về sau khi các đáp án trên được xác minh đúng trên trang challenge.

---

# 8. Nội dung viết portfolio

## Phiên bản tiếng Việt

### Project/CTF Challenge: BasicQnA - Forensics Basic QnA

**Category:** Forensics / Network Analysis / Web Attack Investigation

**Objective:**  
Phân tích file PCAPNG để tái dựng lại chuỗi tấn công của một attacker, bao gồm reconnaissance, tạo tài khoản admin tạm thời, khai thác RCE qua command injection và thu thập thông tin nhạy cảm từ file `.env`.

**Tools Used:**  
Wireshark, tshark, strings, grep, CyberChef, Linux command line.

**Methodology:**

1. Kiểm tra loại file và xác nhận đây là PCAPNG network capture.
2. Phân tích conversation để xác định attacker IP và victim IP.
3. Tìm SSH banner và User-Agent để xác định phiên bản dịch vụ và công cụ reconnaissance.
4. Follow TCP stream chứa response tạo temporary admin account thành công.
5. Phân tích các HTTP POST request đến chức năng backup để phát hiện command injection qua tham số `backup_name`.
6. Trích xuất nội dung file `.env` bị đọc để tìm Github ID và hoàn thành challenge.

**Key Findings:**

- Attacker IP: `172.29.9.159`
- Victim IP: `13.212.67.96`
- Recon tool: `Nmap`
- Temporary admin account: `support_c30cde@corpvault.local`
- Abused CVE: `CVE-2026-8732`
- RCE parameter: `backup_name`
- Sensitive files read: `/app/static/.env`, `/app/templates/.env`
- Github ID: `Ich1ck3nPlus`

**Result:**  
Recovered final flag: `v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}`

**Skills Demonstrated:**

- Network forensics with PCAPNG.
- HTTP request/response analysis.
- TCP stream investigation in Wireshark.
- SSH banner grabbing analysis.
- Reconnaissance detection through User-Agent.
- Web attack chain reconstruction.
- Command injection/RCE artifact analysis.
- Sensitive file exposure investigation.

**Lessons Learned:**

Qua challenge này, tôi hiểu rõ hơn cách tái dựng một chuỗi tấn công từ file PCAP: bắt đầu từ reconnaissance, leo quyền qua temporary admin account, đăng nhập bằng magic link, khai thác command injection và đọc file nhạy cảm. Bài cũng giúp rèn luyện kỹ năng đọc HTTP traffic, xác định IOC/artifact và trình bày kết quả theo hướng SOC/forensics report.

---

## Short English Version

### Project/CTF Challenge: BasicQnA - Forensics Basic QnA

**Category:** Forensics / Network Analysis / Web Attack Investigation

**Objective:**  
Analyze a PCAPNG capture to reconstruct an attack chain involving reconnaissance, temporary admin account creation, command injection, and sensitive file disclosure.

**Tools Used:**  
Wireshark, tshark, strings, grep, CyberChef, Linux CLI.

**Methodology:**

1. Identified the file as a PCAPNG network capture.
2. Reviewed IP conversations to determine the attacker and victim IP addresses.
3. Extracted SSH banners and User-Agent strings to identify service versions and reconnaissance tools.
4. Followed the TCP stream showing successful temporary admin account creation.
5. Investigated HTTP POST requests to the backup feature and found command injection through `backup_name`.
6. Extracted leaked `.env` file contents to identify the GitHub ID and complete the challenge.

**Key Findings:**

- Attacker IP: `172.29.9.159`
- Victim IP: `13.212.67.96`
- Recon tool: `Nmap`
- Temporary admin account: `support_c30cde@corpvault.local`
- Abused CVE: `CVE-2026-8732`
- RCE parameter: `backup_name`
- Files read: `/app/static/.env`, `/app/templates/.env`
- GitHub ID: `Ich1ck3nPlus`

**Result:**  
Recovered flag: `v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}`

**Skills Demonstrated:**  
Network forensics, Wireshark TCP stream analysis, HTTP traffic investigation, reconnaissance detection, command injection analysis, and incident reconstruction.

**Lessons Learned:**  
This challenge improved my ability to reconstruct a realistic web attack chain from network traffic and document key findings in a SOC/forensics-style report.

---

# 9. Báo cáo ngắn để nộp

## Mục tiêu

Mục tiêu của bài là phân tích file `challenge.pcapng` để xác định chuỗi hành vi của attacker, trả lời các câu hỏi điều tra và tìm flag cuối cùng.

## Môi trường phân tích

- Hệ điều hành: Linux/Kali/Ubuntu hoặc Windows có Wireshark.
- File đầu vào: `challenge.pcapng`.
- Công cụ chính: Wireshark, tshark, strings, grep.

## Công cụ sử dụng

- **Wireshark:** Mở file PCAPNG, xem packet và follow TCP stream.
- **tshark:** Trích xuất thông tin bằng command line.
- **strings + grep:** Tìm nhanh các chuỗi như `OpenSSH`, `Nmap`, `backup_name`, `.env`, `Ich1ck3nPlus`.
- **CyberChef:** Decode URL encoding để đọc rõ payload command injection.

## Các bước thực hiện

1. Kiểm tra file và xác định đây là file PCAPNG.
2. Phân tích IP conversation để xác định attacker `172.29.9.159` và victim `13.212.67.96`.
3. Tìm SSH banner `OpenSSH_10.2p1 Ubuntu-2ubuntu3.2` trên victim.
4. Phát hiện User-Agent của `Nmap`, xác định công cụ reconnaissance.
5. Follow TCP stream `tcp.stream eq 4491` để tìm response tạo temporary admin account thành công.
6. Xác định temporary admin account là `support_c30cde@corpvault.local`.
7. Liên kết action `wpgmp_temp_access_ajax` với `CVE-2026-8732`.
8. Phân tích chức năng backup và phát hiện command injection qua tham số `backup_name`.
9. Tìm hai file bị đọc sau RCE: `/app/static/.env` và `/app/templates/.env`.
10. Trích xuất Github ID `Ich1ck3nPlus` và submit hoàn thành challenge.

## Kết quả

Các đáp án chính xác giúp hoàn thành challenge:

```text
172.29.9.159,13.212.67.96
OpenSSH_10.2p1 Ubuntu-2ubuntu3.2
Nmap
tcp.stream eq 4491
support_c30cde@corpvault.local
CVE-2026-8732
backup_name
/app/static/.env,/app/templates/.env
Ich1ck3nPlus
```

Flag cuối cùng:

```text
v1t{llm_c0uld_s0lv3_th1s_ez_chall3ng3!!!}
```

## Kết luận

Challenge mô phỏng một tình huống điều tra network forensics khá thực tế: attacker quét dịch vụ bằng Nmap, abuse lỗ hổng tạo temporary admin account, đăng nhập bằng magic link, sau đó khai thác command injection trong backup feature để đọc file nhạy cảm. Qua quá trình phân tích PCAP, có thể tái dựng đầy đủ attack chain và xác minh flag cuối cùng.

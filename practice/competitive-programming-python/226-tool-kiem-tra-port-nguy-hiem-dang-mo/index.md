---
layout: page
title: '226. Tool kiểm tra port nguy hiểm đang mở'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra port nguy hiểm đang mở.

## Input mẫu — `input.txt`

```text
192.0.2.10,22,OPEN
192.0.2.10,23,OPEN
192.0.2.11,445,OPEN
192.0.2.12,3389,OPEN
192.0.2.13,80,OPEN
```

## Kết quả mong đợi

```text
ALERT 192.0.2.10:23 Telnet
ALERT 192.0.2.11:445 SMB
ALERT 192.0.2.12:3389 RDP
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.txt`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 226
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

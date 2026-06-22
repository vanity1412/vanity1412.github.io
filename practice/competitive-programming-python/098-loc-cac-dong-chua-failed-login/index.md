---
layout: page
title: '098. Lọc các dòng chứa "failed login"'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Lọc các dòng chứa "failed login".

## Input mẫu — `input.log`

```text
Login successful user admin
Failed login user guest from 10.0.0.2
FAILED LOGIN user root from 10.0.0.3
Interface up
```

## Kết quả mong đợi

```text
Failed login user guest from 10.0.0.2
FAILED LOGIN user root from 10.0.0.3
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.log`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 098
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

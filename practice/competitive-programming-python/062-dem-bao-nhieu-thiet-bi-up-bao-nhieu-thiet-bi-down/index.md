---
layout: page
title: '062. Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN.

## Input mẫu — `input.txt`

```text
router01,192.168.1.1,UP
switch01,192.168.1.2,DOWN
firewall01,192.168.1.254,UP
switch02,192.168.1.3,DOWN
```

## Kết quả mong đợi

```text
UP: 2
DOWN: 2
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
python .\check_answer.py 062
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

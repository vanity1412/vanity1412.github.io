---
layout: page
title: '167. Đếm số lần đăng nhập thất bại theo username'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Đếm số lần đăng nhập thất bại theo username.

## Input mẫu — `input.txt`

```text
login failed user admin from 10.0.0.2
login failed user guest from 10.0.0.3
login failed user admin from 10.0.0.4
login successful user admin from 10.0.0.2
```

## Kết quả mong đợi

```text
admin: 2
guest: 1
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
python .\check_answer.py 167
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

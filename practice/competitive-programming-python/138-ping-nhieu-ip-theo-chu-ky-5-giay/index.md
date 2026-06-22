---
layout: page
title: '138. Ping nhiều IP theo chu kỳ 5 giây'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP theo chu kỳ 5 giây.

> Demo mô phỏng ba chu kỳ, không chờ thật 5 giây.

## Input mẫu — `input.txt`

```text
192.0.2.10,UP
192.0.2.11,DOWN
```

## Kết quả mong đợi

```text
t=0s | 192.0.2.10: UP
t=0s | 192.0.2.11: DOWN
t=5s | 192.0.2.10: UP
t=5s | 192.0.2.11: DOWN
t=10s | 192.0.2.10: UP
t=10s | 192.0.2.11: DOWN
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
python .\check_answer.py 138
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

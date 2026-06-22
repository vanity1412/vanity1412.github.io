---
layout: page
title: '165. Tìm login failed trong log'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tìm login failed trong log.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00 auth INFO login successful user admin from 10.0.0.2
2026-06-22 09:01:00 auth ERROR login failed user guest from 10.0.0.3
2026-06-22 09:02:00 auth ERROR LOGIN FAILED user root from 10.0.0.4
```

## Kết quả mong đợi

```text
2026-06-22 09:01:00 auth ERROR login failed user guest from 10.0.0.3
2026-06-22 09:02:00 auth ERROR LOGIN FAILED user root from 10.0.0.4
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
python .\check_answer.py 165
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '159. Lọc log theo ngày'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log theo ngày.

## Input mẫu — `input.log`

```text
2026-06-21 10:00:00 router01 INFO ready
2026-06-22 09:00:00 router01 ERROR interface down
2026-06-22 09:05:00 switch01 WARNING high CPU
2026-06-23 08:00:00 router01 INFO ready
2026-06-22
```

## Kết quả mong đợi

```text
2026-06-22 09:00:00 router01 ERROR interface down
2026-06-22 09:05:00 switch01 WARNING high CPU
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
python .\check_answer.py 159
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '170. Tạo alert khi có nhiều dòng "failed" trong log'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tạo alert khi có nhiều dòng "failed" trong log.

## Input mẫu — `input.log`

```text
5
INFO ready
ERROR failed login admin
ERROR failed login guest
WARNING failed authentication
ERROR failed login root
ERROR failed login test
INFO complete
```

## Kết quả mong đợi

```text
ALERT: 5 dòng failed
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
python .\check_answer.py 170
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

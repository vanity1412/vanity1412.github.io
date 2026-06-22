---
layout: page
title: '218. Tool lọc log lỗi từ syslog'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool lọc log lỗi từ syslog.

## Input mẫu — `input.log`

```text
INFO system ready
ERROR interface Gi0/1 down
WARNING high CPU
error login failed
INFO backup complete
```

## Kết quả mong đợi

```text
ERROR interface Gi0/1 down
error login failed
Tổng lỗi: 2
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
python .\check_answer.py 218
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

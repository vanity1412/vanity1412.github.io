---
layout: page
title: '123. Chia mạng /24 thành 4 subnet bằng nhau'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Chia mạng /24 thành 4 subnet bằng nhau.

## Input mẫu — `input.txt`

```text
10.10.10.0/24
```

## Kết quả mong đợi

```text
Subnet 1: 10.10.10.0/26
Subnet 2: 10.10.10.64/26
Subnet 3: 10.10.10.128/26
Subnet 4: 10.10.10.192/26
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
python .\check_answer.py 123
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

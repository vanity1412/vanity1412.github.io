---
layout: page
title: '125. Kiểm tra danh sách IP nào nằm ngoài subnet cho phép'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Kiểm tra danh sách IP nào nằm ngoài subnet cho phép.

## Input mẫu — `input.txt`

```text
192.168.1.0/24
192.168.1.10
192.168.2.5
10.0.0.1
192.168.1.200
```

## Kết quả mong đợi

```text
192.168.2.5
10.0.0.1
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
python .\check_answer.py 125
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

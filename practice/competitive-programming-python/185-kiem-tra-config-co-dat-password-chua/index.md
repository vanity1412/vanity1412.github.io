---
layout: page
title: '185. Kiểm tra config có đặt password chưa'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra config có đặt password chưa.

## Input mẫu — `config.txt`

```text
enable secret StrongSecret
username admin secret AdminSecret
line console 0
 password ConsoleSecret
 login
```

## Kết quả mong đợi

```text
enable secret: YES
username secret: YES
line password: YES
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `config.txt`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 185
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

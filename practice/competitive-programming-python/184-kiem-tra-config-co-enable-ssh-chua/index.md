---
layout: page
title: '184. Kiểm tra config có enable SSH chưa'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra config có enable SSH chưa.

## Input mẫu — `config.txt`

```text
hostname R1
ip domain-name company.local
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 transport input ssh
```

## Kết quả mong đợi

```text
Đã bật SSH
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
python .\check_answer.py 184
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

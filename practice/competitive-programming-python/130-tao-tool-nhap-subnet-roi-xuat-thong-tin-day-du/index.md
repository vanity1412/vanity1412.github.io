---
layout: page
title: '130. Tạo tool nhập subnet rồi xuất thông tin đầy đủ'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo tool nhập subnet rồi xuất thông tin đầy đủ.

## Input mẫu — `input.txt`

```text
192.168.50.0/27
```

## Kết quả mong đợi

```text
Network: 192.168.50.0
Netmask: 255.255.255.224
Broadcast: 192.168.50.31
Prefix: /27
Usable hosts: 30
First host: 192.168.50.1
Last host: 192.168.50.30
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
python .\check_answer.py 130
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

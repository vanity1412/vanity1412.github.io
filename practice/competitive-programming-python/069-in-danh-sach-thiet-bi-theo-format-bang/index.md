---
layout: page
title: '069. In danh sách thiết bị theo format bảng'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

In danh sách thiết bị theo format bảng.

## Input mẫu — `input.txt`

```text
router01,192.168.1.1,UP
switch01,192.168.1.2,DOWN
firewall01,192.168.1.254,UP
```

## Kết quả mong đợi

```text
HOSTNAME     IP              STATUS
---------------------------------------
router01     192.168.1.1     UP
switch01     192.168.1.2     DOWN
firewall01   192.168.1.254   UP
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
python .\check_answer.py 069
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

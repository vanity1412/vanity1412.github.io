---
layout: page
title: '211. Tool kiểm tra danh sách thiết bị UP/DOWN'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra danh sách thiết bị UP/DOWN.

## Input mẫu — `input.txt`

```text
router01,192.0.2.10,UP
switch01,192.0.2.11,DOWN
firewall01,192.0.2.12,UP
```

## Kết quả mong đợi

```text
router01 (192.0.2.10): UP
switch01 (192.0.2.11): DOWN
firewall01 (192.0.2.12): UP
Tổng: UP=2, DOWN=1
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
python .\check_answer.py 211
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

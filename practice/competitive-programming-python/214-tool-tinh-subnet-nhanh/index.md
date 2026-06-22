---
layout: page
title: '214. Tool tính subnet nhanh'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tính subnet nhanh.

## Input mẫu — `input.txt`

```text
10.20.30.0/27
```

## Kết quả mong đợi

```text
Network: 10.20.30.0
Mask: 255.255.255.224
Broadcast: 10.20.30.31
Usable: 30
Range: 10.20.30.1 - 10.20.30.30
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
python .\check_answer.py 214
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

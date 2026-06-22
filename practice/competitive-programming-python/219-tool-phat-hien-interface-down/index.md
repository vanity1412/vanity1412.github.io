---
layout: page
title: '219. Tool phát hiện interface down'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool phát hiện interface down.

## Input mẫu — `input.txt`

```text
Jun 22 router01 Interface Gi0/1 changed state to down
Jun 22 router01 Interface Gi0/2 changed state to up
Jun 22 switch01 Interface Gi0/24 changed state to DOWN
```

## Kết quả mong đợi

```text
ALERT router01 Gi0/1 DOWN
ALERT switch01 Gi0/24 DOWN
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
python .\check_answer.py 219
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

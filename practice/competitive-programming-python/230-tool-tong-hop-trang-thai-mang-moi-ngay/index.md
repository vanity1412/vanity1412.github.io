---
layout: page
title: '230. Tool tổng hợp trạng thái mạng mỗi ngày'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tổng hợp trạng thái mạng mỗi ngày.

## Input mẫu — `input.txt`

```text
2026-06-22
router01,UP,12,35,0
switch01,DOWN,0,0,12
firewall01,UP,45,62,0
switch02,UP,25,48,2
```

## Kết quả mong đợi

```text
DAILY NETWORK REPORT - 2026-06-22
Devices: 4 (UP 3 / DOWN 1)
Average CPU (UP): 27.3%
Average memory (UP): 48.3%
Interfaces down: 14
Down devices: switch01
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
python .\check_answer.py 230
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

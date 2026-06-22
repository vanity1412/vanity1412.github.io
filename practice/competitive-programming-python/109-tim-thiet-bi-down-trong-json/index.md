---
layout: page
title: '109. Tìm thiết bị DOWN trong JSON'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Tìm thiết bị DOWN trong JSON.

## Input mẫu — `input.json`

```json
[
  {"hostname": "router01", "ip": "192.168.1.1", "status": "UP"},
  {"hostname": "switch01", "ip": "192.168.1.2", "status": "DOWN"},
  {"hostname": "firewall01", "ip": "192.168.1.254", "status": "DOWN"}
]
```

## Kết quả mong đợi

```text
switch01 - 192.168.1.2
firewall01 - 192.168.1.254
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.json`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 109
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.json](./input.json)

[← Quay lại danh sách 230 bài](/luyen-code/)

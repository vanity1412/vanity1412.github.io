---
layout: page
title: '193. SSH vào nhiều thiết bị từ file CSV'
---

**Nhóm:** I. Automation với SSH


## Đề bài

SSH vào nhiều thiết bị từ file CSV.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.csv`

```csv
hostname,ip,device_type,status
router01,192.0.2.10,cisco_ios,OK
switch01,192.0.2.11,cisco_ios,OK
router02,192.0.2.12,cisco_ios,FAIL
```

## Kết quả mong đợi

```text
router01 (192.0.2.10): SSH OK
switch01 (192.0.2.11): SSH OK
router02 (192.0.2.12): SSH FAIL
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.csv`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 193
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.csv](./input.csv)

[← Quay lại danh sách 230 bài](/luyen-code/)

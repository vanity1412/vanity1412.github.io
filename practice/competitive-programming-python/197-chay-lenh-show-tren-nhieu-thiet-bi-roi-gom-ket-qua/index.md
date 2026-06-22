---
layout: page
title: '197. Chạy lệnh show trên nhiều thiết bị rồi gom kết quả'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Chạy lệnh show trên nhiều thiết bị rồi gom kết quả.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01|show clock|09:00:00 UTC Sun Jun 22 2026
router01|show ip route summary|5 routes
switch01|show vlan brief|3 active VLANs
```

## Kết quả mong đợi

```text
[router01] show clock
09:00:00 UTC Sun Jun 22 2026
[router01] show ip route summary
5 routes
[switch01] show vlan brief
3 active VLANs
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
python .\check_answer.py 197
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

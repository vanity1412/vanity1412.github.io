---
layout: page
title: '199. Ghi log lỗi khi SSH thất bại'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Ghi log lỗi khi SSH thất bại.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00,switch01,192.0.2.11,Authentication failed
2026-06-22 09:00:03,router02,192.0.2.12,Connection timeout
2026-06-22 09:00:05,router01,192.0.2.10,OK
```

## Kết quả mong đợi

```text
2026-06-22 09:00:00,switch01,192.0.2.11,Authentication failed
2026-06-22 09:00:03,router02,192.0.2.12,Connection timeout
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.log`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 199
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

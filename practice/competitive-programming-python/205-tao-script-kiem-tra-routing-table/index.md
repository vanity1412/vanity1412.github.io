---
layout: page
title: '205. Tạo script kiểm tra routing table'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra routing table.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,C,192.168.1.0/24,GigabitEthernet0/1
router01,O,10.0.0.0/8,10.1.1.2
router01,S*,0.0.0.0/0,203.0.113.1
```

## Kết quả mong đợi

```text
router01: C 192.168.1.0/24 via GigabitEthernet0/1
router01: O 10.0.0.0/8 via 10.1.1.2
router01: S* 0.0.0.0/0 via 203.0.113.1
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
python .\check_answer.py 205
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

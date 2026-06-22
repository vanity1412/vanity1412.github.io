---
layout: page
title: '201. Tạo script kiểm tra version IOS'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra version IOS.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,Cisco IOS XE Software Version 17.09.03
switch01,Cisco IOS Software Version 15.2(7)E9
router02,Cisco IOS XE Software Version 16.12.05
```

## Kết quả mong đợi

```text
router01: Cisco IOS XE Software Version 17.09.03
switch01: Cisco IOS Software Version 15.2(7)E9
router02: Cisco IOS XE Software Version 16.12.05
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
python .\check_answer.py 201
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

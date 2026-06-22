---
layout: page
title: '146. Kiểm tra danh sách IP và port từ CSV'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Kiểm tra danh sách IP và port từ CSV.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.csv`

```csv
mode,host,port,status
demo,192.0.2.10,22,OPEN
demo,192.0.2.11,80,CLOSED
demo,192.0.2.12,443,OPEN
```

## Kết quả mong đợi

```text
192.0.2.10:22 - OPEN
192.0.2.11:80 - CLOSED
192.0.2.12:443 - OPEN
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
python .\check_answer.py 146
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.csv](./input.csv)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '134. Ping nhiều IP và ghi kết quả ra CSV'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP và ghi kết quả ra CSV.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.csv`

```csv
mode,host,status
demo,192.0.2.10,UP
demo,192.0.2.11,DOWN
demo,192.0.2.12,UP
```

## Kết quả mong đợi

```text
host,result
192.0.2.10,UP
192.0.2.11,DOWN
192.0.2.12,UP
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
python .\check_answer.py 134
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.csv](./input.csv)

[← Quay lại danh sách 230 bài](/luyen-code/)

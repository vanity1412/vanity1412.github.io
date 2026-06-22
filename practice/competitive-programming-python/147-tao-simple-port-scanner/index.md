---
layout: page
title: '147. Tạo simple port scanner'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Tạo simple port scanner.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10
20,21,22,23,80,443
OPEN:22,80,443
```

## Kết quả mong đợi

```text
192.0.2.10:20 - CLOSED
192.0.2.10:21 - CLOSED
192.0.2.10:22 - OPEN
192.0.2.10:23 - CLOSED
192.0.2.10:80 - OPEN
192.0.2.10:443 - OPEN
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
python .\check_answer.py 147
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

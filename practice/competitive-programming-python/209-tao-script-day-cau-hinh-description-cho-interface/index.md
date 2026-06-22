---
layout: page
title: '209. Tạo script đẩy cấu hình description cho interface'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script đẩy cấu hình description cho interface.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `config.txt`

```text
GigabitEthernet0/1,Uplink to Core
GigabitEthernet0/2,User Floor 1
GigabitEthernet0/3,Printer Room
```

## Kết quả mong đợi

```text
interface GigabitEthernet0/1
 description Uplink to Core
interface GigabitEthernet0/2
 description User Floor 1
interface GigabitEthernet0/3
 description Printer Room
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `config.txt`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 209
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

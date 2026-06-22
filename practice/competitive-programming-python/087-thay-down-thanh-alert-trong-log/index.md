---
layout: page
title: '087. Thay "DOWN" thành "ALERT" trong log'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Thay "DOWN" thành "ALERT" trong log.

## Input mẫu — `input.log`

```text
Interface Gi0/1 is DOWN; Gi0/2 is UP
```

## Kết quả mong đợi

```text
Interface Gi0/1 is ALERT; Gi0/2 is UP
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
python .\check_answer.py 087
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

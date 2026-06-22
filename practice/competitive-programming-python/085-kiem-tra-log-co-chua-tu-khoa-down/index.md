---
layout: page
title: '085. Kiểm tra log có chứa từ khóa "down"'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Kiểm tra log có chứa từ khóa "down".

## Input mẫu — `input.log`

```text
Interface GigabitEthernet0/1 changed state to down
```

## Kết quả mong đợi

```text
Có từ khóa down
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
python .\check_answer.py 085
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

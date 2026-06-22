---
layout: page
title: '155. Tìm interface bị down nhiều nhất'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tìm interface bị down nhiều nhất.

## Input mẫu — `input.txt`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:02:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to down
Jun 22 09:05:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
```

## Kết quả mong đợi

```text
GigabitEthernet0/1: 2 lần
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
python .\check_answer.py 155
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

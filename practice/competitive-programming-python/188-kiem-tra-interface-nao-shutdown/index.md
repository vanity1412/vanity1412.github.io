---
layout: page
title: '188. Kiểm tra interface nào shutdown'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra interface nào shutdown.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/1
 description USERS
 no shutdown
interface GigabitEthernet0/2
 description UNUSED
 shutdown
interface GigabitEthernet0/3
 shutdown
```

## Kết quả mong đợi

```text
GigabitEthernet0/2
GigabitEthernet0/3
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
python .\check_answer.py 188
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

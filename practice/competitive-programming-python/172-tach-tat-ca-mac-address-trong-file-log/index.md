---
layout: page
title: '172. Tách tất cả MAC address trong file log'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách tất cả MAC address trong file log.

## Input mẫu — `input.log`

```text
Learned 0011.2233.4455 and aa:bb:cc:dd:ee:ff, old 00-1A-2B-3C-4D-5E
```

## Kết quả mong đợi

```text
0011.2233.4455
aa:bb:cc:dd:ee:ff
00-1A-2B-3C-4D-5E
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
python .\check_answer.py 172
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

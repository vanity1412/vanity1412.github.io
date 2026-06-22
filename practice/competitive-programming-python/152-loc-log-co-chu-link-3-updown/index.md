---
layout: page
title: '152. Lọc log có chữ "LINK-3-UPDOWN"'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log có chữ "LINK-3-UPDOWN".

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol down
Jun 22 09:01:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
```

## Kết quả mong đợi

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:01:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
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
python .\check_answer.py 152
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

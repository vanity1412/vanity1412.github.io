---
layout: page
title: '153. Lọc log có chữ "LINEPROTO"'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log có chữ "LINEPROTO".

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface Gi0/1 down
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1 down
Jun 22 09:01:02 switch01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/2 up
```

## Kết quả mong đợi

```text
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1 down
Jun 22 09:01:02 switch01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/2 up
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
python .\check_answer.py 153
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '182. Tách ACL number'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách ACL number.

## Input mẫu — `input.txt`

```text
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 101 deny tcp any any eq 23
ip access-list extended WEB_ONLY
```

## Kết quả mong đợi

```text
10
101
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
python .\check_answer.py 182
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

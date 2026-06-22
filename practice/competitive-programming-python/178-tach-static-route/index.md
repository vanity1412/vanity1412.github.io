---
layout: page
title: '178. Tách static route'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách static route.

## Input mẫu — `input.txt`

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.1
ip route 10.10.0.0 255.255.0.0 192.168.1.2
router ospf 1
```

## Kết quả mong đợi

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.1
ip route 10.10.0.0 255.255.0.0 192.168.1.2
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
python .\check_answer.py 178
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

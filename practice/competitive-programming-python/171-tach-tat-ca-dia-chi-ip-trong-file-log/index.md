---
layout: page
title: '171. Tách tất cả địa chỉ IP trong file log'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách tất cả địa chỉ IP trong file log.

## Input mẫu — `input.log`

```text
Router 192.168.1.1 sent packet to 10.0.0.5 via 172.16.0.1
```

## Kết quả mong đợi

```text
192.168.1.1
10.0.0.5
172.16.0.1
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
python .\check_answer.py 171
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.log](./input.log)

[← Quay lại danh sách 230 bài](/luyen-code/)

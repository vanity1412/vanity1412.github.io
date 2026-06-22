---
layout: page
title: '126. Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest.

## Input mẫu — `input.txt`

```text
192.168.10.0/24
IT,50
HR,20
Sales,40
Guest,80
```

## Kết quả mong đợi

```text
Guest: 192.168.10.0/25
IT: 192.168.10.128/26
Sales: 192.168.10.192/26
HR: 192.168.11.0/27
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
python .\check_answer.py 126
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

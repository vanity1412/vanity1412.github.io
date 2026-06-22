---
layout: page
title: '128. Tạo bảng VLAN ID, subnet, gateway'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo bảng VLAN ID, subnet, gateway.

## Input mẫu — `input.txt`

```text
10,192.168.10.0/24
20,192.168.20.0/24
30,192.168.30.0/24
```

## Kết quả mong đợi

```text
VLAN  SUBNET             GATEWAY
10    192.168.10.0/24    192.168.10.1
20    192.168.20.0/24    192.168.20.1
30    192.168.30.0/24    192.168.30.1
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
python .\check_answer.py 128
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

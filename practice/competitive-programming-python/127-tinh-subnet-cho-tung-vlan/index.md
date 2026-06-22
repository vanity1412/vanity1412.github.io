---
layout: page
title: '127. Tính subnet cho từng VLAN'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tính subnet cho từng VLAN.

## Input mẫu — `input.txt`

```text
10,192.168.10.0/24
20,192.168.20.0/25
30,192.168.30.0/26
```

## Kết quả mong đợi

```text
VLAN 10: 192.168.10.0/24 - 254 hosts
VLAN 20: 192.168.20.0/25 - 126 hosts
VLAN 30: 192.168.30.0/26 - 62 hosts
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
python .\check_answer.py 127
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

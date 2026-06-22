---
layout: page
title: '176. Tách IP address trên interface'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách IP address trên interface.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/0
 ip address 203.0.113.2 255.255.255.252
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
interface GigabitEthernet0/2
 no ip address
```

## Kết quả mong đợi

```text
GigabitEthernet0/0: 203.0.113.2 255.255.255.252
GigabitEthernet0/1: 192.168.1.1 255.255.255.0
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
python .\check_answer.py 176
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

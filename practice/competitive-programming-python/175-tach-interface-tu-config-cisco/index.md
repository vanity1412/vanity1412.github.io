---
layout: page
title: '175. Tách interface từ config Cisco'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách interface từ config Cisco.

## Input mẫu — `config.txt`

```text
hostname R1
interface GigabitEthernet0/0
 description WAN
interface GigabitEthernet0/1
 description LAN
interface Loopback0
```

## Kết quả mong đợi

```text
GigabitEthernet0/0
GigabitEthernet0/1
Loopback0
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `config.txt`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 175
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

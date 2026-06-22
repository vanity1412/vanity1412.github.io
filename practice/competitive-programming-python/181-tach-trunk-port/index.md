---
layout: page
title: '181. Tách trunk port'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách trunk port.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/1
 switchport mode access
interface GigabitEthernet0/24
 switchport trunk allowed vlan 10,20,99
 switchport mode trunk
interface Port-channel1
 switchport mode trunk
```

## Kết quả mong đợi

```text
GigabitEthernet0/24
Port-channel1
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
python .\check_answer.py 181
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

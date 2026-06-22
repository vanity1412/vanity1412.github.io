---
layout: page
title: '192. SSH vào switch và chạy show vlan brief'
---

**Nhóm:** I. Automation với SSH


## Đề bài

SSH vào switch và chạy show vlan brief.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
switch01
VLAN Name                             Status    Ports
1    default                          active    Gi0/1
10   USERS                            active    Gi0/2, Gi0/3
20   SERVERS                          active    Gi0/4
```

## Kết quả mong đợi

```text
switch01 - show vlan brief
VLAN Name                             Status    Ports
1    default                          active    Gi0/1
10   USERS                            active    Gi0/2, Gi0/3
20   SERVERS                          active    Gi0/4
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
python .\check_answer.py 192
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

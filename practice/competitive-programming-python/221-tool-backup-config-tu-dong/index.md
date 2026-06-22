---
layout: page
title: '221. Tool backup config tự động'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool backup config tự động.

## Input mẫu — `config.txt`

```text
2026-06-22
### router01
hostname router01
interface Gi0/0
 no shutdown
### switch01
hostname switch01
vlan 10
```

## Kết quả mong đợi

```text
Backup OK: router01-2026-06-22.cfg
Backup OK: switch01-2026-06-22.cfg
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
python .\check_answer.py 221
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

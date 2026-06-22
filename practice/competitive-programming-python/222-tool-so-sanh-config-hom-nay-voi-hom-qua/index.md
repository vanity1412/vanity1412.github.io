---
layout: page
title: '222. Tool so sánh config hôm nay với hôm qua'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool so sánh config hôm nay với hôm qua.

## Input mẫu — `config.txt`

```text
### YESTERDAY
hostname R1
interface Gi0/1
 description OLD
 no shutdown
### TODAY
hostname R1
interface Gi0/1
 description UPLINK-CORE
 no shutdown
interface Gi0/2
 shutdown
```

## Kết quả mong đợi

```text
ADDED:
 description UPLINK-CORE
 shutdown
interface Gi0/2
REMOVED:
 description OLD
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
python .\check_answer.py 222
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

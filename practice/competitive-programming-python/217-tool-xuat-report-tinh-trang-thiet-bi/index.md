---
layout: page
title: '217. Tool xuất report tình trạng thiết bị'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool xuất report tình trạng thiết bị.

## Input mẫu — `input.txt`

```text
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,DOWN
firewall01,192.168.1.254,firewall,UP
```

## Kết quả mong đợi

```text
NETWORK STATUS REPORT
Total: 3
UP: 2
DOWN: 1
Types: firewall=1, router=1, switch=1
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
python .\check_answer.py 217
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

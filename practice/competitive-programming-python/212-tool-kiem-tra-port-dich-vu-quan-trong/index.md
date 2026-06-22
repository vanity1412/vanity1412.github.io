---
layout: page
title: '212. Tool kiểm tra port dịch vụ quan trọng'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra port dịch vụ quan trọng.

## Input mẫu — `input.txt`

```text
router01,192.0.2.10,22,OPEN
web01,192.0.2.20,80,OPEN
web01,192.0.2.20,443,CLOSED
dns01,192.0.2.53,53,OPEN
```

## Kết quả mong đợi

```text
router01 SSH (192.0.2.10:22): OPEN
web01 HTTP (192.0.2.20:80): OPEN
web01 HTTPS (192.0.2.20:443): CLOSED
dns01 DNS (192.0.2.53:53): OPEN
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
python .\check_answer.py 212
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '204. Tạo script kiểm tra OSPF neighbor'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra OSPF neighbor.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,1,10.0.0.2,FULL
router01,1,10.0.0.3,FULL
router02,1,10.0.0.1,INIT
```

## Kết quả mong đợi

```text
router01 area 1 neighbor 10.0.0.2: FULL
router01 area 1 neighbor 10.0.0.3: FULL
router02 area 1 neighbor 10.0.0.1: INIT
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
python .\check_answer.py 204
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

---
layout: page
title: '228. Tool tạo báo cáo incident dạng CSV'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng CSV.

## Input mẫu — `input.csv`

```csv
id,date,title,severity,status
INC-001,2026-06-22,Interface down,High,Resolved
INC-002,2026-06-22,Failed login,Medium,Investigating
```

## Kết quả mong đợi

```text
id,date,title,severity,status
INC-001,2026-06-22,Interface down,High,Resolved
INC-002,2026-06-22,Failed login,Medium,Investigating
```

## Các file

- `main.py`: khung trống để bạn viết lời giải.
- `input.csv`: dữ liệu mẫu được `main.py` và `solve.py` đọc tự động.
- `solve.py`: lời giải tham khảo; nên tự làm trước khi mở.
- `expected_output.txt`: kết quả chuẩn dùng để đối chiếu.

## Cách chạy

```powershell
python .\main.py
python .\solve.py
```

Sau khi làm xong, đứng ở thư mục gốc và kiểm tra bài này bằng:

```powershell
python .\check_answer.py 228
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.csv](./input.csv)

[← Quay lại danh sách 230 bài](/luyen-code/)

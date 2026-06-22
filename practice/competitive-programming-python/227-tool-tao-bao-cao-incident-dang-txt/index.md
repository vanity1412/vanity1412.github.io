---
layout: page
title: '227. Tool tạo báo cáo incident dạng TXT'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng TXT.

## Input mẫu — `input.txt`

```text
INC-2026-001
2026-06-22 09:15
Network outage Floor 2
High
Switch access-02 lost power
Power restored and interfaces verified
```

## Kết quả mong đợi

```text
INCIDENT: INC-2026-001
Time: 2026-06-22 09:15
Title: Network outage Floor 2
Severity: High
Cause: Switch access-02 lost power
Resolution: Power restored and interfaces verified
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
python .\check_answer.py 227
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

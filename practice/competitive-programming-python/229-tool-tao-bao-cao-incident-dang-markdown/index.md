---
layout: page
title: '229. Tool tạo báo cáo incident dạng Markdown'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng Markdown.

## Input mẫu — `input.txt`

```text
INC-2026-003
2026-06-22 10:30
Core link flapping
Critical
Investigating optic module
NOC Team
```

## Kết quả mong đợi

```text
# Incident INC-2026-003

- **Time:** 2026-06-22 10:30
- **Title:** Core link flapping
- **Severity:** Critical
- **Status:** Investigating optic module
- **Owner:** NOC Team
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
python .\check_answer.py 229
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [expected_output.txt](./expected_output.txt)
- [input.txt](./input.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

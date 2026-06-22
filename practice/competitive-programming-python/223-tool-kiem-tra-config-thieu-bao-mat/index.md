---
layout: page
title: '223. Tool kiểm tra config thiếu bảo mật'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra config thiếu bảo mật.

## Input mẫu — `config.txt`

```text
hostname R1
enable password cisco
line vty 0 4
 transport input telnet
interface Gi0/0
 no shutdown
```

## Kết quả mong đợi

```text
FAIL: enable secret
FAIL: SSH v2
FAIL: password encryption
FAIL: banner
FAIL: no telnet
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
python .\check_answer.py 223
```

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [solve.py](./solve.py)
- [config.txt](./config.txt)
- [expected_output.txt](./expected_output.txt)

[← Quay lại danh sách 230 bài](/luyen-code/)

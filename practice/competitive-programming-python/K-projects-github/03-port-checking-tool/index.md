---
layout: page
title: 'Port Checking Tool'
---

Kiểm tra nhiều port trên nhiều IP và cảnh báo dịch vụ nhạy cảm.

## Chức năng

- Đọc target/port từ CSV
- Kiểm tra OPEN/CLOSED
- Cảnh báo FTP, Telnet, RDP, SMB, MySQL
- Xuất CSV

## Cấu trúc

- `main.py`
- `targets.csv`
- `result.csv`
- `screenshots/`

## Chạy project

```powershell
python .\main.py          # demo
python .\main.py --live   # socket thật
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Cho phép nhập target từ CLI
- [ ] Quét song song
- [ ] Xuất HTML dashboard

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [result.csv](./result.csv)
- [targets.csv](./targets.csv)

[← Quay lại danh sách luyện code](/luyen-code/)

---
layout: page
title: 'Python Ping Monitoring Tool'
---

Theo dõi trạng thái UP/DOWN của danh sách thiết bị.

## Chức năng

- Đọc thiết bị từ TXT
- Ping tuần tự
- Hiển thị thời gian kiểm tra
- Xuất CSV

## Cấu trúc

- `main.py`
- `devices.txt`
- `result.csv`
- `screenshots/`

## Chạy project

```powershell
python .\main.py          # demo
python .\main.py --live   # ping thật
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Ping song song bằng concurrent.futures
- [ ] Gửi cảnh báo Telegram/email
- [ ] Lập lịch chạy định kỳ

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [devices.txt](./devices.txt)
- [result.csv](./result.csv)

[← Quay lại danh sách luyện code](/luyen-code/)

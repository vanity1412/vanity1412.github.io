---
layout: page
title: 'Daily Network Health Report'
---

Tổng hợp ping, SSH, CPU, RAM và interface thành báo cáo hằng ngày.

## Chức năng

- Tổng hợp UP/DOWN
- Kiểm tra trạng thái SSH
- CPU/RAM giả lập từ CSV
- Xuất Markdown

## Cấu trúc

- `main.py`
- `devices.csv`
- `daily-report.md`
- `screenshots/`

## Chạy project

```powershell
python .\main.py
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Thu thập dữ liệu thật bằng SSH
- [ ] Gửi report qua email/Teams
- [ ] Vẽ biểu đồ xu hướng 7 ngày

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [daily-report.md](./daily-report.md)
- [devices.csv](./devices.csv)

[← Quay lại danh sách luyện code](/luyen-code/)

---
layout: page
title: 'Syslog Analyzer'
---

Phân tích log vận hành mạng và tạo báo cáo Markdown.

## Chức năng

- Lọc interface down
- Lọc login failed
- Đếm lỗi theo hostname/severity
- Xuất Markdown

## Cấu trúc

- `main.py`
- `syslog.log`
- `report.md`
- `screenshots/`

## Chạy project

```powershell
python .\main.py
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Nhận syslog realtime qua UDP
- [ ] Vẽ biểu đồ severity
- [ ] Phát hiện brute force

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [report.md](./report.md)
- [syslog.log](./syslog.log)

[← Quay lại danh sách luyện code](/luyen-code/)

---
layout: page
title: 'Cisco Config Audit Tool'
---

Audit nhanh running-config theo checklist bảo mật và vận hành.

## Chức năng

- Kiểm tra hostname/SSH/Telnet
- Password encryption/enable secret
- Interface shutdown
- Interface thiếu description

## Cấu trúc

- `main.py`
- `running-config.txt`
- `audit-report.md`
- `screenshots/`

## Chạy project

```powershell
python .\main.py
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Audit nhiều config cùng lúc
- [ ] Xuất JSON/CSV
- [ ] Ánh xạ tiêu chuẩn CIS Benchmark

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [audit-report.md](./audit-report.md)
- [running-config.txt](./running-config.txt)

[← Quay lại danh sách luyện code](/luyen-code/)

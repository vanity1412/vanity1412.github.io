---
layout: page
title: 'Network Backup Automation'
---

Tự động thu thập và lưu running-config theo hostname/ngày.

## Chức năng

- Đọc thiết bị CSV
- SSH bằng Netmiko ở live mode
- Lưu config theo ngày
- Log thành công/thất bại

## Cấu trúc

- `main.py`
- `devices.csv`
- `demo-configs/`
- `backups/`
- `backup.log`
- `screenshots/`

## Chạy project

```powershell
python .\main.py          # demo
pip install -r requirements.txt
python .\main.py --live
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Mã hóa credential bằng biến môi trường
- [ ] So sánh config giữa hai ngày
- [ ] Upload backup lên Git/S3

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [backup.log](./backup.log)
- [devices.csv](./devices.csv)
- [requirements.txt](./requirements.txt)

[← Quay lại danh sách luyện code](/luyen-code/)

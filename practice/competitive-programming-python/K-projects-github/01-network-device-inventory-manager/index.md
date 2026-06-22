---
layout: page
title: 'Network Device Inventory Manager'
---

CLI quản lý danh sách router, switch và firewall.

## Chức năng

- Đọc/ghi inventory CSV
- Thêm, xóa và tìm thiết bị
- Cập nhật UP/DOWN
- Xuất JSON

## Cấu trúc

- `main.py`
- `inventory.csv`
- `inventory.json`
- `screenshots/`

## Chạy project

```powershell
python .\main.py list
python .\main.py find 192.168.1.2
python .\main.py export
```

Project chạy ở chế độ demo với dữ liệu mẫu. Chỉ dùng chế độ live trên hệ thống bạn sở hữu hoặc được phép kiểm tra.

## Gợi ý nâng cấp

- [ ] Validate IPv4 bằng `ipaddress`
- [ ] Thêm unit test
- [ ] Tạo giao diện web Flask/FastAPI

## Screenshot

Thêm ảnh terminal hoặc report vào thư mục `screenshots/` trước khi đưa project lên GitHub.

## Mã nguồn và dữ liệu

- [main.py](./main.py)
- [inventory.csv](./inventory.csv)
- [inventory.json](./inventory.json)

[← Quay lại danh sách luyện code](/luyen-code/)

---
layout: page-toc
title: "Cisco Config Backup Tool with Python & Netmiko"
permalink: /projects/cisco-config-backup-netmiko/
toc: true
---

# Cisco Config Backup Tool with Python & Netmiko

Tool nhỏ phục vụ hướng Network Operations: SSH vào thiết bị Cisco, lấy `show running-config`, lưu backup theo timestamp, so sánh với bản backup trước đó và xuất report để phát hiện thay đổi cấu hình.

## Why This Matters

Trong vận hành mạng, backup config chỉ là bước đầu. Phần có giá trị hơn là biết config đã thay đổi gì so với baseline trước đó. Chức năng diff giúp hỗ trợ change management, phát hiện thay đổi ngoài kế hoạch và chuẩn bị rollback khi cần.

## Features

- Đọc danh sách thiết bị từ `devices.yaml`.
- Hỗ trợ credential bằng biến môi trường hoặc `.env`.
- Backup `show running-config` qua Netmiko.
- Lưu file theo cấu trúc `backups/<device>/<timestamp>_<device>_running-config.txt`.
- Tự so sánh backup mới nhất với bản trước đó.
- Bỏ qua các dòng cấu hình dễ thay đổi như timestamp để diff sạch hơn.
- Xuất unified diff vào `reports/`.
- Xuất CSV report cho từng lần chạy.
- Ghi log vào `logs/backup.log`.

## Project Files

```text
projects/cisco-config-backup-netmiko/
├── backup_config.py
├── devices.example.yaml
├── .env.example
├── requirements.txt
├── backups/
├── logs/
├── reports/
└── tests/
```

## Quick Start

```powershell
cd projects/cisco-config-backup-netmiko
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item devices.example.yaml devices.yaml
Copy-Item .env.example .env
```

Sửa `devices.yaml` và `.env`, sau đó chạy:

```powershell
python backup_config.py --inventory devices.yaml
```

## Example Inventory

```yaml
devices:
  - name: R1
    host: 192.0.2.10
    device_type: cisco_ios
    username: ${NETMIKO_USERNAME}
    password: ${NETMIKO_PASSWORD}
    secret: ${NETMIKO_SECRET}
    command: show running-config
```

## Example Output

```text
R1: backup OK, diff status: CHANGED
Report: reports/20260627-221530_backup_report.csv
```

Diff file example:

```diff
--- backups/R1/previous_R1_running-config.txt
+++ backups/R1/current_R1_running-config.txt
@@ -24,6 +24,7 @@
 interface GigabitEthernet0/1
  description LAN
+ ip access-group USERS_OUT in
```

## Operations Notes

- `UNCHANGED`: config giống bản backup trước đó sau khi normalize.
- `CHANGED`: có thay đổi cấu hình, cần review diff.
- `NO_BASELINE`: lần backup đầu tiên của thiết bị.
- `BACKUP_FAILED`: không lấy được config, cần kiểm tra SSH, credential, reachability hoặc enable secret.

## Future Improvements

- Gửi report qua email/Slack.
- Tích hợp Git để version control backup.
- Thêm scheduler bằng Windows Task Scheduler hoặc cron.
- Hỗ trợ Juniper/Arista theo inventory.
- Thêm policy check để cảnh báo các dòng cấu hình nhạy cảm.

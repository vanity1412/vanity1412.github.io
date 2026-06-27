# Cisco Config Backup Tool with Python & Netmiko

Network automation starter project for backing up Cisco running-configs, comparing the latest backup with the previous one, and producing a CSV report for operational review.

## Features

- Load devices from `devices.yaml`.
- Read credentials from environment variables or `.env`.
- Connect to Cisco IOS devices with Netmiko.
- Save timestamped running-config backups.
- Compare the new config with the previous backup.
- Save unified diff files for changed devices.
- Write a CSV report and operation log.

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item devices.example.yaml devices.yaml
Copy-Item .env.example .env
python backup_config.py --inventory devices.yaml
```

## Inventory Example

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

Use lab IP addresses from Packet Tracer/EVE-NG/CML. Do not commit real credentials.

## Why Diff Config Matters

Backup answers: "Can I restore the device?"

Config diff answers: "What changed since the last known backup?"

That second question is closer to real network operations and change management. It helps detect unplanned changes, review maintenance windows, and prepare rollback evidence.

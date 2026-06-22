"""Backup config demo; --live yêu cầu Netmiko và lab được phép."""

import argparse
import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BACKUP_DIR = BASE_DIR / "backups"

# TODO mở rộng: dùng biến môi trường cho credential và đẩy backup lên Git/S3.


def live_backup(device: dict[str, str]) -> str:
    from netmiko import ConnectHandler
    params = {k: device[k] for k in ("host", "device_type", "username", "password")}
    with ConnectHandler(**params) as connection:
        return connection.send_command("show running-config")


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--live", action="store_true")
    args = parser.parse_args(); BACKUP_DIR.mkdir(exist_ok=True); logs = []
    with (BASE_DIR / "devices.csv").open(encoding="utf-8", newline="") as file:
        devices = list(csv.DictReader(file))
    date = datetime.now().strftime("%Y-%m-%d")
    for device in devices:
        try:
            if args.live:
                live = dict(device); live["host"] = device["ip"]; config = live_backup(live)
            else:
                if device["demo_status"] != "OK": raise ConnectionError("demo connection failed")
                config = (BASE_DIR / device["demo_config"]).read_text(encoding="utf-8")
            filename = f"{device['hostname']}-{date}.cfg"
            (BACKUP_DIR / filename).write_text(config.rstrip() + "\n", encoding="utf-8")
            logs.append(f"SUCCESS {device['hostname']} -> {filename}")
        except Exception as error:
            logs.append(f"FAILED {device['hostname']} -> {error}")
    text = "\n".join(logs); (BASE_DIR / "backup.log").write_text(text + "\n", encoding="utf-8"); print(text)


if __name__ == "__main__": main()

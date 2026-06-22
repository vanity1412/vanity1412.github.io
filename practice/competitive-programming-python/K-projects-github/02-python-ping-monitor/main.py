"""Ping monitor: mặc định demo, thêm --live để ping thật."""

import argparse
import csv
import platform
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# TODO mở rộng: ping song song, lập lịch và gửi cảnh báo.


def load_devices() -> list[tuple[str, str, str]]:
    rows = []
    for line in (BASE_DIR / "devices.txt").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            rows.append(tuple(part.strip() for part in line.split(",")))
    return rows


def ping(host: str) -> bool:
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(["ping", flag, "1", host], capture_output=True, timeout=4)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--live", action="store_true")
    args = parser.parse_args(); checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
    results = []
    for hostname, ip, demo_status in load_devices():
        status = ("UP" if ping(ip) else "DOWN") if args.live else demo_status
        results.append({"hostname": hostname, "ip": ip, "status": status, "checked_at": checked_at})
        print(f"{hostname:<12} {ip:<15} {status}")
    with (BASE_DIR / "result.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys()); writer.writeheader(); writer.writerows(results)


if __name__ == "__main__":
    main()

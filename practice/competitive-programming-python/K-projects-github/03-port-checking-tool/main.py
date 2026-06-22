"""Kiểm tra port với chế độ demo hoặc socket thật."""

import argparse
import csv
import socket
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DANGEROUS = {21: "FTP", 23: "Telnet", 3389: "RDP", 445: "SMB", 3306: "MySQL"}

# TODO mở rộng: quét song song và xuất dashboard HTML.


def is_open(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=1): return True
    except OSError: return False


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--live", action="store_true")
    args = parser.parse_args(); results = []
    with (BASE_DIR / "targets.csv").open(encoding="utf-8", newline="") as file:
        targets = list(csv.DictReader(file))
    for target in targets:
        demo_open = {int(x) for x in target["demo_open"].split("|") if x}
        for port in map(int, target["ports"].split("|")):
            opened = is_open(target["host"], port) if args.live else port in demo_open
            warning = DANGEROUS.get(port, "") if opened else ""
            status = "OPEN" if opened else "CLOSED"
            print(f"{target['host']}:{port} {status}" + (f"  ALERT {warning}" if warning else ""))
            results.append({"host": target["host"], "port": port, "status": status, "warning": warning, "checked_at": datetime.now().isoformat(timespec="seconds")})
    with (BASE_DIR / "result.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys()); writer.writeheader(); writer.writerows(results)


if __name__ == "__main__": main()

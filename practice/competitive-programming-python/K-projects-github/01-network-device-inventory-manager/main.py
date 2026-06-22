"""CLI quản lý inventory thiết bị mạng bằng CSV."""

from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "inventory.csv"
FIELDS = ["hostname", "ip", "type", "status"]

# TODO mở rộng: validate IPv4, thêm unit test và giao diện web.


def load_devices() -> list[dict[str, str]]:
    with CSV_FILE.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def save_devices(devices: list[dict[str, str]]) -> None:
    with CSV_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(devices)


def print_devices(devices: list[dict[str, str]]) -> None:
    print(f"{'HOSTNAME':<14} {'IP':<16} {'TYPE':<10} STATUS")
    print("-" * 50)
    for item in devices:
        print(f"{item['hostname']:<14} {item['ip']:<16} {item['type']:<10} {item['status']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Network Device Inventory Manager")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("list")
    add = sub.add_parser("add")
    add.add_argument("hostname"); add.add_argument("ip"); add.add_argument("type")
    add.add_argument("--status", choices=["UP", "DOWN"], default="DOWN")
    delete = sub.add_parser("delete"); delete.add_argument("hostname")
    find = sub.add_parser("find"); find.add_argument("keyword")
    update = sub.add_parser("update"); update.add_argument("hostname")
    update.add_argument("status", choices=["UP", "DOWN"])
    export = sub.add_parser("export"); export.add_argument("--output", default="inventory.json")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    devices = load_devices()
    if args.command in {None, "list"}:
        print_devices(devices)
    elif args.command == "add":
        if any(d["hostname"] == args.hostname or d["ip"] == args.ip for d in devices):
            raise SystemExit("Hostname hoặc IP đã tồn tại")
        devices.append({"hostname": args.hostname, "ip": args.ip, "type": args.type, "status": args.status})
        save_devices(devices); print("Đã thêm thiết bị")
    elif args.command == "delete":
        updated = [d for d in devices if d["hostname"] != args.hostname]
        save_devices(updated); print(f"Đã xóa {len(devices) - len(updated)} thiết bị")
    elif args.command == "find":
        print_devices([d for d in devices if args.keyword in {d["hostname"], d["ip"]}])
    elif args.command == "update":
        found = False
        for device in devices:
            if device["hostname"] == args.hostname:
                device["status"] = args.status; found = True
        save_devices(devices); print("Đã cập nhật" if found else "Không tìm thấy")
    elif args.command == "export":
        output = BASE_DIR / args.output
        output.write_text(json.dumps(devices, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Đã xuất {output.name}")


if __name__ == "__main__":
    main()

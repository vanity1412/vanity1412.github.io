from __future__ import annotations

import argparse
import csv
import difflib
import logging
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional convenience dependency
    load_dotenv = None


ENV_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")
SAFE_NAME_PATTERN = re.compile(r"[^A-Za-z0-9_.-]+")

VOLATILE_LINE_PATTERNS = [
    re.compile(r"^Building configuration", re.IGNORECASE),
    re.compile(r"^Current configuration", re.IGNORECASE),
    re.compile(r"^! Last configuration change", re.IGNORECASE),
    re.compile(r"^! NVRAM config last updated", re.IGNORECASE),
    re.compile(r"^ntp clock-period\s+", re.IGNORECASE),
    re.compile(r"^crypto pki certificate chain", re.IGNORECASE),
]


@dataclass(frozen=True)
class Device:
    name: str
    host: str
    device_type: str
    username: str
    password: str
    secret: str | None
    port: int
    command: str
    read_timeout: int


def safe_name(value: str) -> str:
    cleaned = SAFE_NAME_PATTERN.sub("_", value.strip())
    return cleaned.strip("._") or "device"


def expand_env(value: Any) -> Any:
    if isinstance(value, str):
        return ENV_PATTERN.sub(lambda match: os.getenv(match.group(1), match.group(0)), value)
    if isinstance(value, list):
        return [expand_env(item) for item in value]
    if isinstance(value, dict):
        return {key: expand_env(item) for key, item in value.items()}
    return value


def normalize_config(config_text: str) -> str:
    normalized_lines: list[str] = []

    for raw_line in config_text.splitlines():
        line = raw_line.rstrip()

        if not line:
            continue

        if any(pattern.search(line) for pattern in VOLATILE_LINE_PATTERNS):
            continue

        normalized_lines.append(line)

    return "\n".join(normalized_lines) + "\n"


def build_config_diff(
    previous_config: str,
    current_config: str,
    previous_label: str,
    current_label: str,
) -> str:
    previous_lines = normalize_config(previous_config).splitlines()
    current_lines = normalize_config(current_config).splitlines()

    diff_lines = list(
        difflib.unified_diff(
            previous_lines,
            current_lines,
            fromfile=previous_label,
            tofile=current_label,
            lineterm="",
        )
    )

    return "\n".join(diff_lines) + ("\n" if diff_lines else "")


def load_inventory(path: Path) -> list[Device]:
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PyYAML is required. Install dependencies with: pip install -r requirements.txt") from exc

    if not path.exists():
        raise FileNotFoundError(f"Inventory file not found: {path}")

    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data = expand_env(data)
    raw_devices = data.get("devices", [])

    if not isinstance(raw_devices, list) or not raw_devices:
        raise ValueError("Inventory must contain a non-empty 'devices' list.")

    devices: list[Device] = []

    for item in raw_devices:
        if not isinstance(item, dict):
            raise ValueError("Each device entry must be a mapping.")

        name = str(item.get("name") or item.get("host") or "").strip()
        host = str(item.get("host") or "").strip()
        device_type = str(item.get("device_type") or "cisco_ios").strip()
        username = str(item.get("username") or os.getenv("NETMIKO_USERNAME") or "").strip()
        password = str(item.get("password") or os.getenv("NETMIKO_PASSWORD") or "")
        secret = item.get("secret") or os.getenv("NETMIKO_SECRET")
        command = str(item.get("command") or "show running-config").strip()
        port = int(item.get("port") or 22)
        read_timeout = int(item.get("read_timeout") or 60)

        if not name or not host or not username or not password:
            raise ValueError(f"Device '{name or host or '<unknown>'}' is missing name, host, username or password.")

        unresolved = [value for value in (username, password, secret) if isinstance(value, str) and "${" in value]
        if unresolved:
            raise ValueError(f"Device '{name}' has unresolved environment variable placeholders.")

        devices.append(
            Device(
                name=name,
                host=host,
                device_type=device_type,
                username=username,
                password=password,
                secret=str(secret) if secret else None,
                port=port,
                command=command,
                read_timeout=read_timeout,
            )
        )

    return devices


def setup_logging(log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def collect_running_config(device: Device) -> str:
    try:
        from netmiko import ConnectHandler
    except ImportError as exc:
        raise RuntimeError("Netmiko is required. Install dependencies with: pip install -r requirements.txt") from exc

    connection_params = {
        "device_type": device.device_type,
        "host": device.host,
        "username": device.username,
        "password": device.password,
        "port": device.port,
    }

    if device.secret:
        connection_params["secret"] = device.secret

    connection = ConnectHandler(**connection_params)

    try:
        if device.secret:
            connection.enable()

        return connection.send_command(device.command, read_timeout=device.read_timeout)
    finally:
        connection.disconnect()


def find_previous_backup(device_backup_dir: Path, current_backup: Path) -> Path | None:
    candidates = sorted(
        path
        for path in device_backup_dir.glob("*_running-config.txt")
        if path.is_file() and path != current_backup
    )
    return candidates[-1] if candidates else None


def write_csv_report(report_path: Path, rows: list[dict[str, str]]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "run_id",
        "device",
        "host",
        "status",
        "backup_file",
        "previous_file",
        "diff_status",
        "diff_file",
        "message",
    ]

    with report_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def backup_one_device(
    device: Device,
    run_id: str,
    backup_root: Path,
    report_root: Path,
    skip_diff: bool,
) -> dict[str, str]:
    device_slug = safe_name(device.name)
    device_backup_dir = backup_root / device_slug
    device_backup_dir.mkdir(parents=True, exist_ok=True)

    row = {
        "run_id": run_id,
        "device": device.name,
        "host": device.host,
        "status": "FAILED",
        "backup_file": "",
        "previous_file": "",
        "diff_status": "NOT_RUN",
        "diff_file": "",
        "message": "",
    }

    try:
        logging.info("Connecting to %s (%s)", device.name, device.host)
        config = collect_running_config(device)

        backup_file = device_backup_dir / f"{run_id}_{device_slug}_running-config.txt"
        backup_file.write_text(config.rstrip() + "\n", encoding="utf-8")

        row["status"] = "OK"
        row["backup_file"] = str(backup_file)

        previous_backup = find_previous_backup(device_backup_dir, backup_file)
        if previous_backup:
            row["previous_file"] = str(previous_backup)

        if skip_diff:
            row["diff_status"] = "SKIPPED"
        elif previous_backup is None:
            row["diff_status"] = "NO_BASELINE"
        else:
            previous_config = previous_backup.read_text(encoding="utf-8", errors="replace")
            diff_text = build_config_diff(
                previous_config=previous_config,
                current_config=config,
                previous_label=str(previous_backup),
                current_label=str(backup_file),
            )

            if diff_text:
                diff_file = report_root / f"{run_id}_{device_slug}_config.diff"
                diff_file.write_text(diff_text, encoding="utf-8")
                row["diff_status"] = "CHANGED"
                row["diff_file"] = str(diff_file)
            else:
                row["diff_status"] = "UNCHANGED"

        row["message"] = "Backup completed."
        logging.info("%s: backup OK, diff status: %s", device.name, row["diff_status"])

    except Exception as exc:  # noqa: BLE001 - report per-device failures without stopping all backups
        row["status"] = "FAILED"
        row["diff_status"] = "BACKUP_FAILED"
        row["message"] = str(exc)
        logging.exception("%s: backup failed", device.name)

    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Back up Cisco running-configs and compare each backup with the previous one."
    )
    parser.add_argument("--inventory", default="devices.yaml", help="Path to devices inventory YAML.")
    parser.add_argument("--backup-dir", default="backups", help="Directory for config backups.")
    parser.add_argument("--report-dir", default="reports", help="Directory for CSV and diff reports.")
    parser.add_argument("--log-file", default="logs/backup.log", help="Log file path.")
    parser.add_argument("--skip-diff", action="store_true", help="Only back up configs; do not compare diffs.")
    return parser.parse_args()


def main() -> int:
    if load_dotenv:
        load_dotenv()

    args = parse_args()
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")

    backup_root = Path(args.backup_dir)
    report_root = Path(args.report_dir)
    setup_logging(Path(args.log_file))

    try:
        devices = load_inventory(Path(args.inventory))
    except Exception as exc:  # noqa: BLE001 - CLI entry point should print clean failure
        logging.error("Unable to load inventory: %s", exc)
        return 2

    rows = [
        backup_one_device(
            device=device,
            run_id=run_id,
            backup_root=backup_root,
            report_root=report_root,
            skip_diff=args.skip_diff,
        )
        for device in devices
    ]

    report_path = report_root / f"{run_id}_backup_report.csv"
    write_csv_report(report_path, rows)
    logging.info("Report: %s", report_path)

    failed = [row for row in rows if row["status"] != "OK"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

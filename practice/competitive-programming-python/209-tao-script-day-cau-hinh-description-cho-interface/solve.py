"""Lời giải tham khảo bài 209: Tạo script đẩy cấu hình description cho interface."""

from pathlib import Path
import collections
import csv
import io
import ipaddress
import json
import math
import platform
import re
import socket
import subprocess
import unicodedata

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "config.txt"

def run_live_command(device: dict, command: str) -> str:
    """Dùng hàm này khi có lab thật và đã cài: pip install netmiko."""
    from netmiko import ConnectHandler

    with ConnectHandler(**device) as connection:
        return connection.send_command(command)

def solve(data: str) -> str:
    rows=[line.split(',',1) for line in data.splitlines()]; return '\n'.join(f"interface {iface}\n description {desc}" for iface,desc in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

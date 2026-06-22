"""Lời giải tham khảo bài 208: Tạo script kiểm tra số interface down."""

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
INPUT_FILE = BASE_DIR / "input.txt"

def run_live_command(device: dict, command: str) -> str:
    """Dùng hàm này khi có lab thật và đã cài: pip install netmiko."""
    from netmiko import ConnectHandler

    with ConnectHandler(**device) as connection:
        return connection.send_command(command)

def solve(data: str) -> str:
    rows=[line.split(',') for line in data.splitlines()]; counts=collections.Counter(h for h,iface,status in rows if status=='down'); return '\n'.join(f"{h}: {counts.get(h,0)} interface down" for h in dict.fromkeys(r[0] for r in rows))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

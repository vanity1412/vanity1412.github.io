"""Lời giải tham khảo bài 207: Tạo script kiểm tra memory usage."""

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
    rows=[line.split(',') for line in data.splitlines()]; return '\n'.join(f"{h}: {int(used)/int(total)*100:.1f}% used{' ALERT' if int(used)/int(total)>=0.8 else ''}" for h,total,used in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

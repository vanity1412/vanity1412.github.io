"""Lời giải tham khảo bài 220: Tool phát hiện login failed nhiều lần."""

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
INPUT_FILE = BASE_DIR / "input.log"

def solve(data: str) -> str:
    ips=re.findall(r'from ((?:\d{1,3}\.){3}\d{1,3})',data); counts=collections.Counter(ips); alerts=[f"ALERT {ip}: {n} failed logins" for ip,n in counts.items() if n>5]; return '\n'.join(alerts) or 'Không có cảnh báo'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

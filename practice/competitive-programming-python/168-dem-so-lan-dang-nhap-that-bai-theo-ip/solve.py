"""Lời giải tham khảo bài 168: Đếm số lần đăng nhập thất bại theo IP."""

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

def solve(data: str) -> str:
    ips=re.findall(r'login failed.*?from ((?:\d{1,3}\.){3}\d{1,3})',data,flags=re.I); counts=collections.Counter(ips); return '\n'.join(f"{ip}: {c}" for ip,c in sorted(counts.items()))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 093: Đọc danh sách IP từ file TXT."""

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
    ips=[line.strip() for line in data.splitlines() if line.strip()]
    return '\n'.join(f"IP {i+1}: {ip}" for i,ip in enumerate(ips))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

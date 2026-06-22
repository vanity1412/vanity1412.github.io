"""Lời giải tham khảo bài 061: Lưu danh sách thiết bị mạng gồm hostname, IP, status."""

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
    rows=[line.split(',') for line in data.splitlines() if line]
    return '\n'.join(f"{h}: {ip} ({status})" for h,ip,status in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

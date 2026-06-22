"""Lời giải tham khảo bài 100: Đọc file CSV danh sách thiết bị mạng."""

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
INPUT_FILE = BASE_DIR / "input.csv"

def solve(data: str) -> str:
    rows=list(csv.DictReader(io.StringIO(data)))
    return '\n'.join(f"{r['hostname']}: {r['ip']} - {r['type']} - {r['status']}" for r in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 174: Tách hostname từ config Cisco."""

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

def solve(data: str) -> str:
    m=re.search(r'^hostname\s+(\S+)',data,flags=re.M|re.I); return m.group(1) if m else 'Không tìm thấy'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

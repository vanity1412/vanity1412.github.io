"""Lời giải tham khảo bài 219: Tool phát hiện interface down."""

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
    rows=[]
    for line in data.splitlines():
        if 'down' in line.casefold():
            m=re.search(r'Interface (\S+)',line,re.I); host=line.split()[2]; rows.append(f"ALERT {host} {m.group(1)} DOWN")
    return '\n'.join(rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 156: Tách hostname từ dòng syslog."""

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
    hosts=[]
    for line in data.splitlines():
        m=re.match(r'\w+\s+\d+\s+\S+\s+(\S+)',line)
        if m: hosts.append(m.group(1))
    return '\n'.join(hosts)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

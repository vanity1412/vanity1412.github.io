"""Lời giải tham khảo bài 094: Ghi danh sách IP UP/DOWN ra file TXT."""

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
    content='\n'.join(f"{ip}: {status}" for ip,status in rows)
    (BASE_DIR/'ip_status.txt').write_text(content+'\n',encoding='utf-8')
    return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 103: Tìm thiết bị theo IP trong file CSV."""

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
    rows=list(csv.DictReader(io.StringIO(data))); query=next(r['ip'] for r in rows if r['hostname']=='QUERY'); found=next((r for r in rows if r['ip']==query and r['hostname']!='QUERY'),None)
    return f"{found['hostname']} - {found['type']} - {found['status']}" if found else 'Không tìm thấy'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

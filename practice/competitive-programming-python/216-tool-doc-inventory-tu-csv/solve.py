"""Lời giải tham khảo bài 216: Tool đọc inventory từ CSV."""

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
    rows=list(csv.DictReader(io.StringIO(data))); return '\n'.join(f"{r['hostname']:<10} {r['ip']:<15} {r['type']:<8} {r['status']}" for r in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

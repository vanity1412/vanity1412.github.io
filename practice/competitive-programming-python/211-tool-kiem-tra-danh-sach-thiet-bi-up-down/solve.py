"""Lời giải tham khảo bài 211: Tool kiểm tra danh sách thiết bị UP/DOWN."""

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
    rows=[line.split(',') for line in data.splitlines()]; up=sum(r[2]=='UP' for r in rows); return '\n'.join(f"{h} ({ip}): {st}" for h,ip,st in rows)+f"\nTổng: UP={up}, DOWN={len(rows)-up}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

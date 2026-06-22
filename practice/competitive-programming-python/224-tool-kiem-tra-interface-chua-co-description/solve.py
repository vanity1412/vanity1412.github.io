"""Lời giải tham khảo bài 224: Tool kiểm tra interface chưa có description."""

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
    blocks=re.split(r'(?=^interface )',data,flags=re.M); missing=[]
    for b in blocks:
        m=re.search(r'^interface (\S+)',b,re.M)
        if m and not re.search(r'^\s*description ',b,re.M): missing.append(m.group(1))
    return '\n'.join(missing)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

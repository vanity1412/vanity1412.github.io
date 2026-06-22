"""Lời giải tham khảo bài 181: Tách trunk port."""

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
    blocks=re.split(r'(?=^interface )',data,flags=re.M); return '\n'.join(re.search(r'^interface\s+(\S+)',b,re.M).group(1) for b in blocks if 'switchport mode trunk' in b)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

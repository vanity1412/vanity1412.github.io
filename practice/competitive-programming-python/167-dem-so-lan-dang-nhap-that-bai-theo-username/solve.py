"""Lời giải tham khảo bài 167: Đếm số lần đăng nhập thất bại theo username."""

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
    users=re.findall(r'login failed user (\S+)',data,flags=re.I); counts=collections.Counter(users); return '\n'.join(f"{u}: {c}" for u,c in sorted(counts.items()))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 079: Kiểm tra chuỗi có phải địa chỉ IP đơn giản không."""

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
    parts=data.strip().split('.')
    ok=len(parts)==4 and all(p.isdigit() and 0<=int(p)<=255 for p in parts)
    return 'IPv4 hợp lệ' if ok else 'IPv4 không hợp lệ'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

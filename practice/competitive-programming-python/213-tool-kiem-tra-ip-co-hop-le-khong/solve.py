"""Lời giải tham khảo bài 213: Tool kiểm tra IP có hợp lệ không."""

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
    out=[]
    for value in data.splitlines():
        try: ipaddress.ip_address(value); status='VALID'
        except ValueError: status='INVALID'
        out.append(f"{value}: {status}")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

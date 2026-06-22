"""Lời giải tham khảo bài 069: In danh sách thiết bị theo format bảng."""

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
    rows=[line.split(',') for line in data.splitlines()]
    out=['HOSTNAME     IP              STATUS','-'*39]
    out += [f"{h:<12} {ip:<15} {st}" for h,ip,st in rows]
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

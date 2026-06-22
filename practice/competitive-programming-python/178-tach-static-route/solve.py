"""Lời giải tham khảo bài 178: Tách static route."""

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
    return '\n'.join(line for line in data.splitlines() if re.match(r'^ip route\s+',line))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

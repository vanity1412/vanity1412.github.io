"""Lời giải tham khảo bài 184: Kiểm tra config có enable SSH chưa."""

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
INPUT_FILE = BASE_DIR / "config.txt"

def solve(data: str) -> str:
    ok=bool(re.search(r'^ip ssh version\s+2',data,re.M) and re.search(r'transport input.*\bssh\b',data))
    return 'Đã bật SSH' if ok else 'Chưa bật SSH đầy đủ'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

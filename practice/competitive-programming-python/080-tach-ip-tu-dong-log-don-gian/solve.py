"""Lời giải tham khảo bài 080: Tách IP từ dòng log đơn giản."""

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
INPUT_FILE = BASE_DIR / "input.log"

def solve(data: str) -> str:
    m=re.search(r'(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)',data)
    return m.group() if m else 'Không tìm thấy'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

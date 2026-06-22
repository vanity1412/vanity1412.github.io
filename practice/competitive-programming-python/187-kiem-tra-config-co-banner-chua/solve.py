"""Lời giải tham khảo bài 187: Kiểm tra config có banner chưa."""

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
    return 'Đã cấu hình banner' if re.search(r'^banner\s+\S+',data,re.M) else 'Chưa cấu hình banner'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

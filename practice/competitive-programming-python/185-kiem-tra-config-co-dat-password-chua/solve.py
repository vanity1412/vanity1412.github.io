"""Lời giải tham khảo bài 185: Kiểm tra config có đặt password chưa."""

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
    checks={'enable secret':r'^enable secret\s+\S+','username secret':r'^username\s+\S+\s+secret\s+\S+','line password':r'^\s*password\s+\S+'}; return '\n'.join(f"{name}: {'YES' if re.search(p,data,re.M) else 'NO'}" for name,p in checks.items())


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

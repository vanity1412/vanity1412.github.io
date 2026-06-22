"""Lời giải tham khảo bài 223: Tool kiểm tra config thiếu bảo mật."""

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
    checks=[('enable secret',bool(re.search(r'^enable secret',data,re.M))),('SSH v2',bool(re.search(r'^ip ssh version 2',data,re.M))),('password encryption',bool(re.search(r'^service password-encryption$',data,re.M))),('banner',bool(re.search(r'^banner ',data,re.M))),('no telnet',not bool(re.search(r'transport input.*telnet',data)))]
    return '\n'.join(f"{'PASS' if ok else 'FAIL'}: {name}" for name,ok in checks)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

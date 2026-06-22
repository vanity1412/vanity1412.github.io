"""Lời giải tham khảo bài 190: Tạo checklist audit config Cisco bằng Python."""

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
    checks=[('Enable secret',bool(re.search(r'^enable secret',data,re.M))),('SSH v2',bool(re.search(r'^ip ssh version 2',data,re.M))),('Password encryption',bool(re.search(r'^service password-encryption$',data,re.M))),('Banner',bool(re.search(r'^banner ',data,re.M))),('Không dùng Telnet',not bool(re.search(r'transport input.*telnet',data)))]
    return '\n'.join(f"[{'PASS' if ok else 'FAIL'}] {name}" for name,ok in checks)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

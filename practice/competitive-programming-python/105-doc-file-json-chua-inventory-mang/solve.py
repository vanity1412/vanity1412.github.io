"""Lời giải tham khảo bài 105: Đọc file JSON chứa inventory mạng."""

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
INPUT_FILE = BASE_DIR / "input.json"

def solve(data: str) -> str:
    devices=json.loads(data)
    return '\n'.join(f"{d['hostname']}: {d['ip']} ({d['status']})" for d in devices)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

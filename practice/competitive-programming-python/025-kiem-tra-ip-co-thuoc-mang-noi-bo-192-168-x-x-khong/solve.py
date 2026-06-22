"""Lời giải tham khảo bài 025: Kiểm tra IP có thuộc mạng nội bộ 192.168.x.x không."""

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
    parts = data.strip().split('.')
    ok = len(parts) == 4 and parts[:2] == ['192','168']
    return 'Thuộc mạng nội bộ' if ok else 'Không thuộc mạng nội bộ'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

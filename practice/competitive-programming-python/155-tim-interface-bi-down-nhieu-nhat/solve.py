"""Lời giải tham khảo bài 155: Tìm interface bị down nhiều nhất."""

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
    interfaces=re.findall(r'Interface ([\w/.-]+).*?down',data,flags=re.I); counts=collections.Counter(interfaces); name,count=counts.most_common(1)[0]
    return f"{name}: {count} lần"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

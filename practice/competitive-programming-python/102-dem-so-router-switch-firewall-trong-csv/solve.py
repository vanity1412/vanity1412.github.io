"""Lời giải tham khảo bài 102: Đếm số router/switch/firewall trong CSV."""

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
INPUT_FILE = BASE_DIR / "input.csv"

def solve(data: str) -> str:
    rows=list(csv.DictReader(io.StringIO(data))); counts=collections.Counter(r['type'] for r in rows)
    return '\n'.join(f"{kind}: {counts.get(kind,0)}" for kind in ['router','switch','firewall'])


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

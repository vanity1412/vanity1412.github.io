"""Lời giải tham khảo bài 217: Tool xuất report tình trạng thiết bị."""

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
    rows=list(csv.DictReader(io.StringIO(data))); up=sum(r['status']=='UP' for r in rows); types=collections.Counter(r['type'] for r in rows); return '\n'.join(['NETWORK STATUS REPORT',f"Total: {len(rows)}",f"UP: {up}",f"DOWN: {len(rows)-up}",'Types: '+', '.join(f"{k}={v}" for k,v in sorted(types.items()))])


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

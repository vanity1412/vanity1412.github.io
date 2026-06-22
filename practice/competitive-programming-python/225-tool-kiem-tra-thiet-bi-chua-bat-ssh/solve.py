"""Lời giải tham khảo bài 225: Tool kiểm tra thiết bị chưa bật SSH."""

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
    blocks=re.split(r'^### ',data,flags=re.M)[1:]; missing=[]
    for b in blocks:
        rows=b.splitlines(); host=rows[0]; config='\n'.join(rows[1:]); ok='ip ssh version 2' in config and re.search(r'transport input.*ssh',config);
        if not ok: missing.append(host)
    return '\n'.join(missing)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

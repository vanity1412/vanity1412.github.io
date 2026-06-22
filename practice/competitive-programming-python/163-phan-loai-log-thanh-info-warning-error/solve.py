"""Lời giải tham khảo bài 163: Phân loại log thành INFO, WARNING, ERROR."""

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
INPUT_FILE = BASE_DIR / "input.log"

def solve(data: str) -> str:
    groups={'INFO':[],'WARNING':[],'ERROR':[]}
    for line in data.splitlines():
        level=next((x for x in groups if f' {x} ' in line),'INFO'); groups[level].append(line)
    return '\n'.join(f"{level}: {len(lines)}" for level,lines in groups.items())


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

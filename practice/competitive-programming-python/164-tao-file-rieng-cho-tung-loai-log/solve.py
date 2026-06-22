"""Lời giải tham khảo bài 164: Tạo file riêng cho từng loại log."""

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
    for level,lines in groups.items(): (BASE_DIR/f'{level.lower()}.log').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return '\n'.join(f"{level.lower()}.log: {len(lines)} dòng" for level,lines in groups.items())


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

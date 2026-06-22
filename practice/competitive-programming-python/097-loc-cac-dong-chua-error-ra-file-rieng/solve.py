"""Lời giải tham khảo bài 097: Lọc các dòng chứa "error" ra file riêng."""

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
    lines=[line for line in data.splitlines() if 'error' in line.casefold()]
    content='\n'.join(lines)
    (BASE_DIR/'errors.log').write_text(content+'\n',encoding='utf-8')
    return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

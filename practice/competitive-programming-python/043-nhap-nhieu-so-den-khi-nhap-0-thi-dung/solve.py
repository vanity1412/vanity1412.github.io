"""Lời giải tham khảo bài 043: Nhập nhiều số đến khi nhập 0 thì dừng."""

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
    numbers = [int(x) for x in data.split()]
    values = numbers[:numbers.index(0)] if 0 in numbers else numbers
    return f"Đã nhập: {' '.join(map(str,values))}\nTổng: {sum(values)}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

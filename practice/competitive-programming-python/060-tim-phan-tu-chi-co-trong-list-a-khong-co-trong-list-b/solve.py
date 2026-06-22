"""Lời giải tham khảo bài 060: Tìm phần tử chỉ có trong list A, không có trong list B."""

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
    a,b=(set(map(int,line.split())) for line in data.splitlines())
    return ' '.join(map(str,sorted(a-b)))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

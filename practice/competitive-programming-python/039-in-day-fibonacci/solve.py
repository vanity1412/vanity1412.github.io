"""Lời giải tham khảo bài 039: In dãy Fibonacci."""

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
    n = int(data)
    a, b, out = 0, 1, []
    for _ in range(n):
        out.append(a); a, b = b, a+b
    return ' '.join(map(str,out))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 056: Đếm số lần xuất hiện của một số."""

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
    lines=data.splitlines(); target=int(lines[0]); values=list(map(int,lines[1].split()))
    return str(values.count(target))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 113: Kiểm tra IP thuộc class A/B/C."""

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
    first=int(data.split('.')[0]); cls='A' if 1<=first<=126 else 'B' if 128<=first<=191 else 'C' if 192<=first<=223 else 'Không thuộc A/B/C'
    return f"Class {cls}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

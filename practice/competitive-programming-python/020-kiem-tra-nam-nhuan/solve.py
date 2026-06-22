"""Lời giải tham khảo bài 020: Kiểm tra năm nhuận."""

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
    year = int(data)
    leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    return 'Năm nhuận' if leap else 'Không phải năm nhuận'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

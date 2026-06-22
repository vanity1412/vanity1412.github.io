"""Lời giải tham khảo bài 222: Tool so sánh config hôm nay với hôm qua."""

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
INPUT_FILE = BASE_DIR / "config.txt"

def solve(data: str) -> str:
    parts=re.split(r'^### (?:YESTERDAY|TODAY)\n',data,flags=re.M)[1:]; old=set(parts[0].splitlines()); new=set(parts[1].splitlines()); out=['ADDED:']+sorted(new-old)+['REMOVED:']+sorted(old-new); return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

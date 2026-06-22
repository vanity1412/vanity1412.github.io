"""Lời giải tham khảo bài 152: Lọc log có chữ "LINK-3-UPDOWN"."""

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
    return '\n'.join(line for line in data.splitlines() if 'LINK-3-UPDOWN' in line)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

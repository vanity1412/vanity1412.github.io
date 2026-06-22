"""Lời giải tham khảo bài 062: Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN."""

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
    statuses=[line.split(',')[2].upper() for line in data.splitlines() if line]
    return f"UP: {statuses.count('UP')}\nDOWN: {statuses.count('DOWN')}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

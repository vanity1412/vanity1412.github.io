"""Lời giải tham khảo bài 068: Xóa thiết bị khỏi inventory."""

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
    lines=data.splitlines(); inventory=dict(line.split(',') for line in lines[:-1]); inventory.pop(lines[-1],None)
    return '\n'.join(f"{h}: {ip}" for h,ip in inventory.items())


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

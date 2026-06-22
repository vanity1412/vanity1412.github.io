"""Lời giải tham khảo bài 112: Kiểm tra IP có thuộc private IP không."""

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
    ip=ipaddress.ip_address(data.strip())
    return 'Private IP' if ip.is_private else 'Public IP'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

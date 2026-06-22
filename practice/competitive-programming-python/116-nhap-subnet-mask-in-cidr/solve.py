"""Lời giải tham khảo bài 116: Nhập subnet mask, in CIDR."""

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
    network=ipaddress.IPv4Network(f'0.0.0.0/{data.strip()}'); return f"/{network.prefixlen}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

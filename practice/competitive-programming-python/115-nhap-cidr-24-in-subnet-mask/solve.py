"""Lời giải tham khảo bài 115: Nhập CIDR /24, in subnet mask."""

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
    prefix=int(data.strip().lstrip('/')); return str(ipaddress.IPv4Network(f'0.0.0.0/{prefix}').netmask)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

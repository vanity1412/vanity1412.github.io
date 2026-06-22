"""Lời giải tham khảo bài 125: Kiểm tra danh sách IP nào nằm ngoài subnet cho phép."""

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
    lines=data.splitlines(); net=ipaddress.ip_network(lines[0]); outside=[ip for ip in lines[1:] if ipaddress.ip_address(ip) not in net]
    return '\n'.join(outside)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

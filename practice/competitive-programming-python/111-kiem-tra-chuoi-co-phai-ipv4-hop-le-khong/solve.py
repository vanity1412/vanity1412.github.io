"""Lời giải tham khảo bài 111: Kiểm tra chuỗi có phải IPv4 hợp lệ không."""

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
    try:
        ip=ipaddress.IPv4Address(data.strip()); result='IPv4 hợp lệ'
    except ipaddress.AddressValueError: result='IPv4 không hợp lệ'
    return result


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

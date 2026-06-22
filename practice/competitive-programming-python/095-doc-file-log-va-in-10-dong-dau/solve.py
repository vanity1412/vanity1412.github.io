"""Lời giải tham khảo bài 095: Đọc file log và in 10 dòng đầu."""

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
    return '\n'.join(data.splitlines()[:10])


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

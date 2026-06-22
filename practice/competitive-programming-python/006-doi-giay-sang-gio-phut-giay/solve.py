"""Lời giải tham khảo bài 006: Đổi giây sang giờ, phút, giây."""

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
    total = int(data)
    h, rem = divmod(total, 3600)
    m, sec = divmod(rem, 60)
    return f"{h} giờ {m} phút {sec} giây"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 027: Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không."""

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
    total, used = map(float, data.split())
    remain = (total-used)/total*100
    status = 'CẢNH BÁO' if remain < 20 else 'Bình thường'
    return f"Còn lại: {remain:.1f}% - {status}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

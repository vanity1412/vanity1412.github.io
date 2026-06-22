"""Lời giải tham khảo bài 170: Tạo alert khi có nhiều dòng "failed" trong log."""

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
    lines=data.splitlines(); threshold=int(lines[0]); count=sum('failed' in line.casefold() for line in lines[1:]); return f"ALERT: {count} dòng failed" if count>=threshold else f"Bình thường: {count} dòng failed"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 010: Tính tiền điện theo số kWh nhập vào."""

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
    kwh = float(data)
    fee = min(kwh, 50)*1800 + min(max(kwh-50, 0), 50)*1900 + max(kwh-100, 0)*2200
    return f"{fee:.0f} VND"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

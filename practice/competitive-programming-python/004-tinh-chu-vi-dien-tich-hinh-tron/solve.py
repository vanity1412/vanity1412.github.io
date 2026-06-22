"""Lời giải tham khảo bài 004: Tính chu vi, diện tích hình tròn."""

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
    r = float(data)
    return f"Chu vi: {2*math.pi*r:.2f}\nDiện tích: {math.pi*r*r:.2f}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

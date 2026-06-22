"""Lời giải tham khảo bài 002: Tính tổng, hiệu, tích, thương của 2 số."""

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
    a, b = map(float, data.split())
    return f"Tổng: {a+b:g}\nHiệu: {a-b:g}\nTích: {a*b:g}\nThương: {a/b:g}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

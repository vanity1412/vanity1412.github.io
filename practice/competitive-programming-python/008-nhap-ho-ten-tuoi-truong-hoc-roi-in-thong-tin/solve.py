"""Lời giải tham khảo bài 008: Nhập họ tên, tuổi, trường học rồi in thông tin."""

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
    name, age, school = data.splitlines()
    return f"Họ tên: {name}\nTuổi: {age}\nTrường: {school}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

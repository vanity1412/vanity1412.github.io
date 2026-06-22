"""Lời giải tham khảo bài 057: Tách số chẵn và số lẻ thành 2 list."""

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
    v=list(map(int,data.split()))
    return f"Chẵn: {' '.join(map(str,[n for n in v if n%2==0]))}\nLẻ: {' '.join(map(str,[n for n in v if n%2]))}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

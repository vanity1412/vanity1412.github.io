"""Lời giải tham khảo bài 162: Đếm số log warning/error."""

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
    levels=[line.split()[3] for line in data.splitlines()]; return f"WARNING: {levels.count('WARNING')}\nERROR: {levels.count('ERROR')}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

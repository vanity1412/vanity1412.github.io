"""Lời giải tham khảo bài 160: Lọc log theo hostname."""

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
    lines=data.splitlines(); target=lines[-1]; return '\n'.join(line for line in lines[:-1] if f' {target} ' in line)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 015: Tính tổng dung lượng 3 file MB và đổi sang GB."""

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
    mb = sum(map(float, data.split()))
    return f"{mb:g} MB\n{mb/1024:.3f} GB"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

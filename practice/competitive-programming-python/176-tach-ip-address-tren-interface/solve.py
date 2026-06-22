"""Lời giải tham khảo bài 176: Tách IP address trên interface."""

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
    blocks=re.split(r'(?=^interface )',data,flags=re.M); out=[]
    for block in blocks:
        im=re.search(r'^interface\s+(\S+)',block,re.M); ipm=re.search(r'^\s*ip address\s+(\S+)\s+(\S+)',block,re.M)
        if im and ipm: out.append(f"{im.group(1)}: {ipm.group(1)} {ipm.group(2)}")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

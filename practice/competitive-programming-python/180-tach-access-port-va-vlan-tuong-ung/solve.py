"""Lời giải tham khảo bài 180: Tách access port và VLAN tương ứng."""

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
        im=re.search(r'^interface\s+(\S+)',block,re.M); vm=re.search(r'switchport access vlan\s+(\d+)',block)
        if im and vm: out.append(f"{im.group(1)} -> VLAN {vm.group(1)}")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

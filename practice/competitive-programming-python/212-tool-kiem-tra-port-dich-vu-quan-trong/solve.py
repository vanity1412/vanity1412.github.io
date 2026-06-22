"""Lời giải tham khảo bài 212: Tool kiểm tra port dịch vụ quan trọng."""

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
    services={22:'SSH',80:'HTTP',443:'HTTPS',53:'DNS'}; rows=[line.split(',') for line in data.splitlines()]; return '\n'.join(f"{h} {services.get(int(p),'UNKNOWN')} ({ip}:{p}): {st}" for h,ip,p,st in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

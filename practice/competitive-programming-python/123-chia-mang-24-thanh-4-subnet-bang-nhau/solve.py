"""Lời giải tham khảo bài 123: Chia mạng /24 thành 4 subnet bằng nhau."""

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
    net=ipaddress.ip_network(data.strip()); subs=list(net.subnets(prefixlen_diff=2)); return '\n'.join(f"Subnet {i+1}: {sub}" for i,sub in enumerate(subs))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

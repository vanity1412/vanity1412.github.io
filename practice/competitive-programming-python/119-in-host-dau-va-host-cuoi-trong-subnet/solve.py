"""Lời giải tham khảo bài 119: In host đầu và host cuối trong subnet."""

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
    net=ipaddress.ip_network(data.strip()); hosts=list(net.hosts()); return f"Host đầu: {hosts[0]}\nHost cuối: {hosts[-1]}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

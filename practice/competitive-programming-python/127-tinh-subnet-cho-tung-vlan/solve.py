"""Lời giải tham khảo bài 127: Tính subnet cho từng VLAN."""

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
    rows=[line.split(',') for line in data.splitlines()]; return '\n'.join(f"VLAN {vlan}: {ipaddress.ip_network(cidr)} - {ipaddress.ip_network(cidr).num_addresses-2} hosts" for vlan,cidr in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 128: Tạo bảng VLAN ID, subnet, gateway."""

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
    rows=[line.split(',') for line in data.splitlines()]; out=['VLAN  SUBNET             GATEWAY']
    for vlan,cidr in rows:
        net=ipaddress.ip_network(cidr); out.append(f"{vlan:<5} {str(net):<18} {next(net.hosts())}")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

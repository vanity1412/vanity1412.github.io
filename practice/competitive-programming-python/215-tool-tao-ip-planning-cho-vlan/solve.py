"""Lời giải tham khảo bài 215: Tool tạo IP planning cho VLAN."""

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
    rows=[line.split(',') for line in data.splitlines()]; out=['VLAN | SUBNET | GATEWAY | USABLE']
    for vlan,cidr in rows:
        net=ipaddress.ip_network(cidr); out.append(f"{vlan} | {net} | {next(net.hosts())} | {net.num_addresses-2}")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

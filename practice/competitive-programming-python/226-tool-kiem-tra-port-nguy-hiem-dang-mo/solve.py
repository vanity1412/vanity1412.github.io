"""Lời giải tham khảo bài 226: Tool kiểm tra port nguy hiểm đang mở."""

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
    danger={23:'Telnet',445:'SMB',3389:'RDP'}; rows=[line.split(',') for line in data.splitlines()]; return '\n'.join(f"ALERT {ip}:{port} {danger[int(port)]}" for ip,port,status in rows if status=='OPEN' and int(port) in danger)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

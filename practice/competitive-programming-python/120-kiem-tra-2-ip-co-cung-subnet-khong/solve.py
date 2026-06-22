"""Lời giải tham khảo bài 120: Kiểm tra 2 IP có cùng subnet không."""

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
    ip1,ip2,prefix=data.split(); n1=ipaddress.ip_network(f'{ip1}/{prefix}',strict=False); n2=ipaddress.ip_network(f'{ip2}/{prefix}',strict=False)
    return 'Cùng subnet' if n1==n2 else 'Khác subnet'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 126: Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest."""

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
    lines=data.splitlines(); base=ipaddress.ip_network(lines[0]); requests=[(name,int(count)) for name,count in (line.split(',') for line in lines[1:])]; requests.sort(key=lambda x:x[1],reverse=True)
    start=int(base.network_address); allocated=[]
    for name,hosts in requests:
        prefix=32-math.ceil(math.log2(hosts+2)); size=2**(32-prefix); start=(start+size-1)//size*size; net=ipaddress.ip_network((start,prefix)); allocated.append((name,net)); start+=size
    return '\n'.join(f"{name}: {net}" for name,net in allocated)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

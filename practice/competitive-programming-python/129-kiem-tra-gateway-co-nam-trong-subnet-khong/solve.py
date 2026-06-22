"""Lời giải tham khảo bài 129: Kiểm tra gateway có nằm trong subnet không."""

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
    cidr,gateway=data.split(); net=ipaddress.ip_network(cidr); ip=ipaddress.ip_address(gateway)
    return 'Gateway hợp lệ' if ip in net and ip not in {net.network_address,net.broadcast_address} else 'Gateway không hợp lệ'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

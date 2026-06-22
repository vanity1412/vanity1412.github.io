"""Lời giải tham khảo bài 026: Kiểm tra port nhập vào có phải port phổ biến không."""

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
    port = int(data)
    services = {22:'SSH', 53:'DNS', 80:'HTTP', 443:'HTTPS', 3389:'RDP'}
    return services.get(port, 'Port không phổ biến')


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

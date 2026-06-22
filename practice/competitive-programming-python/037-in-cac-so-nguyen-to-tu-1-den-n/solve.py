"""Lời giải tham khảo bài 037: In các số nguyên tố từ 1 đến N."""

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
    n = int(data)
    primes = [v for v in range(2,n+1) if all(v%i for i in range(2,int(v**0.5)+1))]
    return ' '.join(map(str, primes))


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 036: Kiểm tra số nguyên tố."""

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
    is_prime = n >= 2 and all(n % i for i in range(2, int(n**0.5)+1))
    return 'Số nguyên tố' if is_prime else 'Không phải số nguyên tố'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

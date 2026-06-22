"""Lời giải tham khảo bài 024: Kiểm tra username và password đăng nhập."""

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
    username, password = data.split()
    return 'Đăng nhập thành công' if (username, password) == ('admin','123456') else 'Đăng nhập thất bại'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 090: Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b"."""

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
    text=data.strip().replace('Đ','D').replace('đ','d')
    text=unicodedata.normalize('NFD',text)
    text=''.join(c for c in text if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

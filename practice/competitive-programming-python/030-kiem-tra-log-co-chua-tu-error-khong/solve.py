"""Lời giải tham khảo bài 030: Kiểm tra log có chứa từ “error” không."""

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
INPUT_FILE = BASE_DIR / "input.log"

def solve(data: str) -> str:
    return 'Có lỗi' if 'error' in data.casefold() else 'Không có lỗi'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

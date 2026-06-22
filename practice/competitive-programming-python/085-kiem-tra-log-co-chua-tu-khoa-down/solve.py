"""Lời giải tham khảo bài 085: Kiểm tra log có chứa từ khóa "down"."""

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
    return 'Có từ khóa down' if 'down' in data.casefold() else 'Không có từ khóa down'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

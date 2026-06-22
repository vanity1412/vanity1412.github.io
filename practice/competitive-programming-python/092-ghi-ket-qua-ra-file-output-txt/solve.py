"""Lời giải tham khảo bài 092: Ghi kết quả ra file output.txt."""

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
    content=data.strip().upper()
    (BASE_DIR/'output.txt').write_text(content+'\n',encoding='utf-8')
    return f"Đã ghi output.txt:\n{content}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

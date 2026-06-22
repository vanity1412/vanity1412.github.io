"""Lời giải tham khảo bài 021: Xếp loại học lực theo điểm."""

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
    score = float(data)
    rank = 'Giỏi' if score >= 8 else 'Khá' if score >= 6.5 else 'Trung bình' if score >= 5 else 'Yếu'
    return rank


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

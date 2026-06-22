"""Lời giải tham khảo bài 013: Tính BMI."""

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
    weight, height = map(float, data.split())
    bmi = weight/(height**2)
    level = 'Thiếu cân' if bmi < 18.5 else 'Bình thường' if bmi < 25 else 'Thừa cân' if bmi < 30 else 'Béo phì'
    return f"BMI: {bmi:.2f} - {level}"


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

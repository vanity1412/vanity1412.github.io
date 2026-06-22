"""Lời giải tham khảo bài 107: Thêm thiết bị mới vào JSON."""

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
INPUT_FILE = BASE_DIR / "input.json"

def solve(data: str) -> str:
    obj=json.loads(data); obj['devices'].append(obj['new_device'])
    return json.dumps(obj['devices'],ensure_ascii=False,indent=2)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

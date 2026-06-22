"""Lời giải tham khảo bài 106: Ghi inventory mạng ra JSON."""

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
    devices=json.loads(data); content=json.dumps(devices,ensure_ascii=False,indent=2)
    (BASE_DIR/'inventory_output.json').write_text(content+'\n',encoding='utf-8')
    return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

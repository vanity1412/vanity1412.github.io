"""Lời giải tham khảo bài 221: Tool backup config tự động."""

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
INPUT_FILE = BASE_DIR / "config.txt"

def solve(data: str) -> str:
    lines=data.splitlines(); date=lines[0]; blocks=re.split(r'^### ', '\n'.join(lines[1:]),flags=re.M)[1:]; names=[]
    for block in blocks:
        rows=block.splitlines(); host=rows[0]; name=f'{host}-{date}.cfg'; (BASE_DIR/name).write_text('\n'.join(rows[1:])+'\n',encoding='utf-8'); names.append(name)
    return '\n'.join(f"Backup OK: {name}" for name in names)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 196: Lưu backup theo tên hostname và ngày tháng."""

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

def run_live_command(device: dict, command: str) -> str:
    """Dùng hàm này khi có lab thật và đã cài: pip install netmiko."""
    from netmiko import ConnectHandler

    with ConnectHandler(**device) as connection:
        return connection.send_command(command)

def solve(data: str) -> str:
    lines=data.splitlines(); date=lines[0]; blocks=re.split(r'^### ', '\n'.join(lines[1:]),flags=re.M)[1:]; out=[]
    for block in blocks:
        rows=block.splitlines(); host=rows[0]; name=f'{host}-{date}.cfg'; (BASE_DIR/name).write_text('\n'.join(rows[1:])+'\n',encoding='utf-8'); out.append(name)
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

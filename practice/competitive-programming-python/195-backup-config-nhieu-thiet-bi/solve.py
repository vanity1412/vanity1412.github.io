"""Lời giải tham khảo bài 195: Backup config nhiều thiết bị."""

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

def run_live_command(device: dict, command: str) -> str:
    """Dùng hàm này khi có lab thật và đã cài: pip install netmiko."""
    from netmiko import ConnectHandler

    with ConnectHandler(**device) as connection:
        return connection.send_command(command)

def solve(data: str) -> str:
    blocks=re.split(r'^### ',data,flags=re.M)[1:]; out=[]
    for block in blocks:
        lines=block.splitlines(); host=lines[0]; content='\n'.join(lines[1:]); (BASE_DIR/f'{host}-running.cfg').write_text(content+'\n',encoding='utf-8'); out.append(f"{host}: OK")
    return '\n'.join(out)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

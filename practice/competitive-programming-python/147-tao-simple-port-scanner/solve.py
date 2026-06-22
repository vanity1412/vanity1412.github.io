"""Lời giải tham khảo bài 147: Tạo simple port scanner."""

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

def live_ping(host: str) -> bool:
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=3,
    )
    return result.returncode == 0


def live_port(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except OSError:
        return False

def solve(data: str) -> str:
    lines=data.splitlines(); host=lines[1]; ports=map(int,lines[2].split(',')); opened=set(map(int,lines[3].split(':')[1].split(',')))
    return '\n'.join(f"{host}:{p} - {'OPEN' if p in opened else 'CLOSED'}" for p in ports)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

"""Lời giải tham khảo bài 148: Tạo tool kiểm tra service: SSH, HTTP, HTTPS, RDP, DNS."""

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
    services={22:'SSH',80:'HTTP',443:'HTTPS',3389:'RDP',53:'DNS'}; lines=data.splitlines(); host=lines[1]; rows=[line.split(',') for line in lines[2:]]
    return '\n'.join(f"{services[int(p)]}: {host}:{p} - {st}" for p,st in rows)


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

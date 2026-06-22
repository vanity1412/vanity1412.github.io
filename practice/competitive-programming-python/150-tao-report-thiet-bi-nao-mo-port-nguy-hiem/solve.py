"""Lời giải tham khảo bài 150: Tạo report thiết bị nào mở port nguy hiểm."""

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
    dangerous={23:'Telnet',445:'SMB',3389:'RDP'}; rows=[line.split(',') for line in data.splitlines()]; alerts=[f"ALERT {h}:{p} ({dangerous[int(p)]})" for h,p,st in rows if int(p) in dangerous and st=='OPEN']
    return '\n'.join(alerts) if alerts else 'Không phát hiện port nguy hiểm'


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

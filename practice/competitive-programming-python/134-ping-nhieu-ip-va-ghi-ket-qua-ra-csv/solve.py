"""Lời giải tham khảo bài 134: Ping nhiều IP và ghi kết quả ra CSV."""

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
INPUT_FILE = BASE_DIR / "input.csv"

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
    rows=list(csv.DictReader(io.StringIO(data))); out=io.StringIO(); w=csv.writer(out,lineterminator='\n'); w.writerow(['host','result'])
    for r in rows: w.writerow([r['host'],r['status'] if r['mode']=='demo' else ('UP' if live_ping(r['host']) else 'DOWN')])
    content=out.getvalue().rstrip(); (BASE_DIR/'ping_results.csv').write_text(content+'\n',encoding='utf-8'); return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

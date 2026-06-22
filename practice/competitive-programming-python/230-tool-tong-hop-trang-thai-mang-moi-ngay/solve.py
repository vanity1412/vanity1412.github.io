"""Lời giải tham khảo bài 230: Tool tổng hợp trạng thái mạng mỗi ngày."""

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
    lines=data.splitlines(); date=lines[0]; rows=[line.split(',') for line in lines[1:]]; up=sum(r[1]=='UP' for r in rows); avg_cpu=sum(int(r[2]) for r in rows if r[1]=='UP')/up; avg_mem=sum(int(r[3]) for r in rows if r[1]=='UP')/up; down_if=sum(int(r[4]) for r in rows)
    return '\n'.join([f"DAILY NETWORK REPORT - {date}",f"Devices: {len(rows)} (UP {up} / DOWN {len(rows)-up})",f"Average CPU (UP): {avg_cpu:.1f}%",f"Average memory (UP): {avg_mem:.1f}%",f"Interfaces down: {down_if}",'Down devices: '+(', '.join(r[0] for r in rows if r[1]=='DOWN') or 'None')])


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

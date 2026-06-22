"""Lời giải tham khảo bài 110: Xuất report TXT từ dữ liệu JSON."""

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
    devices=json.loads(data); up=sum(d['status']=='UP' for d in devices); down=len(devices)-up
    lines=['NETWORK INVENTORY REPORT',f"Total: {len(devices)}",f"UP: {up}",f"DOWN: {down}",'']+[f"{d['hostname']} | {d['ip']} | {d['type']} | {d['status']}" for d in devices]
    content='\n'.join(lines); (BASE_DIR/'report.txt').write_text(content+'\n',encoding='utf-8'); return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

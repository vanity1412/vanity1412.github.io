"""Lời giải tham khảo bài 104: Cập nhật trạng thái thiết bị trong file CSV."""

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

def solve(data: str) -> str:
    rows=list(csv.DictReader(io.StringIO(data))); update=next(r for r in rows if r['hostname']=='UPDATE'); devices=[r for r in rows if r['hostname']!='UPDATE']
    for r in devices:
        if r['hostname']==update['ip']: r['status']=update['status']
    out=io.StringIO(); w=csv.DictWriter(out,fieldnames=['hostname','ip','type','status'],lineterminator='\n'); w.writeheader(); w.writerows(devices)
    content=out.getvalue().rstrip(); (BASE_DIR/'updated_inventory.csv').write_text(content+'\n',encoding='utf-8'); return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

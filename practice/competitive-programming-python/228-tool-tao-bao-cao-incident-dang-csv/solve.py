"""Lời giải tham khảo bài 228: Tool tạo báo cáo incident dạng CSV."""

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
    rows=list(csv.DictReader(io.StringIO(data))); out=io.StringIO(); w=csv.DictWriter(out,fieldnames=['id','date','title','severity','status'],lineterminator='\n'); w.writeheader(); w.writerows(rows); content=out.getvalue().rstrip(); (BASE_DIR/'incident_report.csv').write_text(content+'\n',encoding='utf-8'); return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

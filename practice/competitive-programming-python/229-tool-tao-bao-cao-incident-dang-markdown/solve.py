"""Lời giải tham khảo bài 229: Tool tạo báo cáo incident dạng Markdown."""

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
    incident,date,title,severity,status,owner=data.splitlines(); content='\n'.join([f"# Incident {incident}",'',f"- **Time:** {date}",f"- **Title:** {title}",f"- **Severity:** {severity}",f"- **Status:** {status}",f"- **Owner:** {owner}"]); (BASE_DIR/'incident_report.md').write_text(content+'\n',encoding='utf-8'); return content


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

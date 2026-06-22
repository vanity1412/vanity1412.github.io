"""Lời giải tham khảo bài 130: Tạo tool nhập subnet rồi xuất thông tin đầy đủ."""

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
    net=ipaddress.ip_network(data.strip(),strict=False); hosts=list(net.hosts())
    return '\n'.join([f"Network: {net.network_address}",f"Netmask: {net.netmask}",f"Broadcast: {net.broadcast_address}",f"Prefix: /{net.prefixlen}",f"Usable hosts: {len(hosts)}",f"First host: {hosts[0]}",f"Last host: {hosts[-1]}"] )


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

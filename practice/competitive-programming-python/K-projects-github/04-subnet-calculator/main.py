"""Subnet calculator dùng thư viện chuẩn ipaddress."""

import ipaddress
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# TODO mở rộng: hỗ trợ IPv6 và chia subnet VLSM.


def main() -> None:
    lines = [x.strip() for x in (BASE_DIR / "input.txt").read_text().splitlines() if x.strip()]
    network = ipaddress.ip_network(lines[0], strict=False); hosts = list(network.hosts())
    output = [
        f"Network: {network.network_address}", f"Broadcast: {network.broadcast_address}",
        f"Subnet mask: {network.netmask}", f"Prefix: /{network.prefixlen}",
        f"Usable hosts: {len(hosts)}", f"First host: {hosts[0] if hosts else 'N/A'}",
        f"Last host: {hosts[-1] if hosts else 'N/A'}", "", "IP membership:",
    ]
    for value in lines[1:]:
        ip = ipaddress.ip_address(value); output.append(f"{ip}: {'YES' if ip in network else 'NO'}")
    text = "\n".join(output); print(text)
    (BASE_DIR / "output.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__": main()

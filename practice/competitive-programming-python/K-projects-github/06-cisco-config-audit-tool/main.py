"""Audit các cấu hình bảo mật và interface Cisco cơ bản."""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# TODO mở rộng: audit nhiều config và ánh xạ CIS Benchmark.


def interface_blocks(config: str) -> list[tuple[str, str]]:
    result = []
    for block in re.split(r"(?=^interface )", config, flags=re.M):
        match = re.search(r"^interface\s+(\S+)", block, flags=re.M)
        if match: result.append((match.group(1), block))
    return result


def main() -> None:
    config = (BASE_DIR / "running-config.txt").read_text(encoding="utf-8")
    hostname = re.search(r"^hostname\s+(\S+)", config, flags=re.M)
    checks = [
        ("Hostname configured", hostname is not None),
        ("SSH v2 enabled", bool(re.search(r"^ip ssh version 2$", config, flags=re.M))),
        ("Telnet disabled", not bool(re.search(r"transport input.*telnet", config))),
        ("Password encryption", "service password-encryption" in config),
        ("Enable secret", bool(re.search(r"^enable secret\s+", config, flags=re.M))),
    ]
    blocks = interface_blocks(config)
    shutdown = [name for name, block in blocks if re.search(r"^\s*shutdown$", block, flags=re.M)]
    no_description = [name for name, block in blocks if not re.search(r"^\s*description\s+", block, flags=re.M)]
    report = ["# Cisco Config Audit", "", f"Hostname: `{hostname.group(1) if hostname else 'MISSING'}`", "", "## Checklist"]
    report += [f"- [{'x' if passed else ' '}] {'PASS' if passed else 'FAIL'} — {name}" for name, passed in checks]
    report += ["", "## Shutdown interfaces"] + [f"- {name}" for name in shutdown]
    report += ["", "## Interfaces missing description"] + [f"- {name}" for name in no_description]
    text = "\n".join(report) + "\n"; (BASE_DIR / "audit-report.md").write_text(text, encoding="utf-8"); print(text)


if __name__ == "__main__": main()

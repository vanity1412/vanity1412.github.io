"""Phân tích Cisco syslog và xuất report Markdown."""

import collections
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# TODO mở rộng: nhận syslog realtime và phát hiện brute force.


def main() -> None:
    lines = (BASE_DIR / "syslog.log").read_text(encoding="utf-8").splitlines()
    interface_down = [x for x in lines if "interface" in x.casefold() and "down" in x.casefold()]
    login_failed = [x for x in lines if "login_failed" in x.casefold() or "login failed" in x.casefold()]
    host_counts = collections.Counter((x.split()[3] if len(x.split()) > 3 else "UNKNOWN") for x in interface_down + login_failed)
    severities = collections.Counter(re.search(r"%[A-Z_]+-(\d)-", x).group(1) for x in lines if re.search(r"%[A-Z_]+-(\d)-", x))
    report = ["# Syslog Analysis Report", "", f"- Total logs: {len(lines)}", f"- Interface down: {len(interface_down)}", f"- Login failed: {len(login_failed)}", "", "## Errors by hostname"]
    report += [f"- {host}: {count}" for host, count in sorted(host_counts.items())]
    report += ["", "## Logs by severity"] + [f"- Severity {level}: {count}" for level, count in sorted(severities.items())]
    report += ["", "## Interface down"] + [f"- `{line}`" for line in interface_down]
    report += ["", "## Login failed"] + [f"- `{line}`" for line in login_failed]
    text = "\n".join(report) + "\n"; (BASE_DIR / "report.md").write_text(text, encoding="utf-8"); print(text)


if __name__ == "__main__": main()

"""Tổng hợp health check demo thành báo cáo Markdown."""

import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# TODO mở rộng: thu thập live qua SSH và gửi report qua email/Teams.


def main() -> None:
    with (BASE_DIR / "devices.csv").open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    up = [r for r in rows if r["ping_status"] == "UP"]; down = [r for r in rows if r["ping_status"] == "DOWN"]
    ssh_open = sum(r["ssh_status"] == "OPEN" for r in rows)
    avg_cpu = sum(int(r["cpu"]) for r in up) / len(up) if up else 0
    avg_ram = sum(int(r["ram"]) for r in up) / len(up) if up else 0
    report = [
        f"# Daily Network Health Report — {datetime.now().date()}", "",
        "## Summary", "", f"- Devices: {len(rows)}", f"- UP: {len(up)}", f"- DOWN: {len(down)}",
        f"- SSH open: {ssh_open}/{len(rows)}", f"- Average CPU (UP): {avg_cpu:.1f}%",
        f"- Average RAM (UP): {avg_ram:.1f}%", f"- Interfaces down: {sum(int(r['interfaces_down']) for r in rows)}",
        "", "## Device details", "", "| Hostname | IP | Ping | SSH | CPU | RAM | Interfaces down |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    report += [f"| {r['hostname']} | {r['ip']} | {r['ping_status']} | {r['ssh_status']} | {r['cpu']}% | {r['ram']}% | {r['interfaces_down']} |" for r in rows]
    if down: report += ["", "## Alerts", ""] + [f"- **DOWN:** {r['hostname']} ({r['ip']})" for r in down]
    text = "\n".join(report) + "\n"; (BASE_DIR / "daily-report.md").write_text(text, encoding="utf-8"); print(text)


if __name__ == "__main__": main()

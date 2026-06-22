"""Chạy main.py và so sánh với expected_output.txt."""

from pathlib import Path
import os
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def main() -> int:
    if len(sys.argv) != 2:
        print("Cách dùng: python check_answer.py 001")
        return 2

    prefix = sys.argv[1].strip().zfill(3) + "-"
    matches = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(prefix)]
    if len(matches) != 1:
        print(f"Không tìm thấy duy nhất một bài với mã {sys.argv[1]}")
        return 2

    folder = matches[0]
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    run = subprocess.run(
        [sys.executable, "main.py"],
        cwd=folder,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=15,
    )
    if run.returncode != 0:
        print("RUNTIME ERROR")
        print(run.stderr.rstrip())
        return 1

    actual = run.stdout.rstrip()
    expected = (folder / "expected_output.txt").read_text(encoding="utf-8").rstrip()
    if actual == expected:
        print(f"PASS: {folder.name}")
        return 0

    print(f"FAIL: {folder.name}")
    print("--- Kết quả của bạn ---")
    print(actual or "<không có output>")
    print("--- Kết quả mong đợi ---")
    print(expected)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

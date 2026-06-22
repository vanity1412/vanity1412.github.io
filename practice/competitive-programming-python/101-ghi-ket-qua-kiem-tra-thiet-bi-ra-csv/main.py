"""Bài 101: Ghi kết quả kiểm tra thiết bị ra CSV."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.csv"


def solve(data: str) -> str:
    # TODO: Phân tích `data`, viết thuật toán và trả về kết quả dạng chuỗi.
    return ""


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

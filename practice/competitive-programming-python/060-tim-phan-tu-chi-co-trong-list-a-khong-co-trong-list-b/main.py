"""Bài 060: Tìm phần tử chỉ có trong list A, không có trong list B."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"


def solve(data: str) -> str:
    # TODO: Phân tích `data`, viết thuật toán và trả về kết quả dạng chuỗi.
    return ""


if __name__ == "__main__":
    result = solve(INPUT_FILE.read_text(encoding="utf-8"))
    if result is not None:
        print(result)

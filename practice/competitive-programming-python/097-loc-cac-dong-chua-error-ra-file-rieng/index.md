---
layout: page
title: '097. Lọc các dòng chứa "error" ra file riêng'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Lọc các dòng chứa "error" ra file riêng.

## Input mẫu — `input.txt`

```text
INFO system started
ERROR interface down
WARNING high CPU
error failed login
INFO ready
```

## Kết quả mong đợi

```text
ERROR interface down
error failed login
```

## Tự luyện

<textarea class="code-practice-area" spellcheck="false" placeholder="Viết code của bạn ở đây..." style="width: 100%; min-height: 320px; padding: 1rem; border: 1px solid var(--main-border-color); border-radius: 6px; background: var(--highlight-bg-color); color: var(--text-color); font-family: var(--code-font-family); font-size: 0.95rem; line-height: 1.55; resize: vertical;"></textarea>

## Lời giải tham khảo

```python
{% capture solution_code %}
{% include_relative solve.py %}
{% endcapture %}
{{ solution_code | split: 'if __name__ == "__main__":' | first | split: 'def solve' | last | prepend: 'def solve' | strip }}
```

## Bài tiếp theo

- [← Quay lại danh sách 230 bài](/luyen-code/)
- [098. Lọc các dòng chứa "failed login"](/practice/competitive-programming-python/098-loc-cac-dong-chua-failed-login/)
- [099. Lọc các dòng chứa "interface down"](/practice/competitive-programming-python/099-loc-cac-dong-chua-interface-down/)
- [100. Đọc file CSV danh sách thiết bị mạng](/practice/competitive-programming-python/100-doc-file-csv-danh-sach-thiet-bi-mang/)

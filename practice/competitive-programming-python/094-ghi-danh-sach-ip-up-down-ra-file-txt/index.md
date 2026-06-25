---
layout: page
title: '094. Ghi danh sách IP UP/DOWN ra file TXT'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Ghi danh sách IP UP/DOWN ra file TXT.

## Input mẫu — `input.txt`

```text
192.168.1.1,UP
192.168.1.2,DOWN
10.0.0.1,UP
```

## Kết quả mong đợi

```text
192.168.1.1: UP
192.168.1.2: DOWN
10.0.0.1: UP
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
- [095. Đọc file log và in 10 dòng đầu](/practice/competitive-programming-python/095-doc-file-log-va-in-10-dong-dau/)
- [096. Đếm số dòng trong file log](/practice/competitive-programming-python/096-dem-so-dong-trong-file-log/)
- [097. Lọc các dòng chứa "error" ra file riêng](/practice/competitive-programming-python/097-loc-cac-dong-chua-error-ra-file-rieng/)

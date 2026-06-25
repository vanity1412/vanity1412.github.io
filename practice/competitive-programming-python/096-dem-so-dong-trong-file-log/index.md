---
layout: page
title: '096. Đếm số dòng trong file log'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đếm số dòng trong file log.

## Input mẫu — `input.log`

```text
line one
line two
line three
line four
```

## Kết quả mong đợi

```text
4
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
- [097. Lọc các dòng chứa "error" ra file riêng](/practice/competitive-programming-python/097-loc-cac-dong-chua-error-ra-file-rieng/)
- [098. Lọc các dòng chứa "failed login"](/practice/competitive-programming-python/098-loc-cac-dong-chua-failed-login/)
- [099. Lọc các dòng chứa "interface down"](/practice/competitive-programming-python/099-loc-cac-dong-chua-interface-down/)

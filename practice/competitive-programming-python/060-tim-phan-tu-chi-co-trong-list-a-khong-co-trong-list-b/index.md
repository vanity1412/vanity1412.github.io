---
layout: page
title: '060. Tìm phần tử chỉ có trong list A, không có trong list B'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tìm phần tử chỉ có trong list A, không có trong list B.

## Input mẫu — `input.txt`

```text
1 2 3 4 5
4 5 6 7
```

## Kết quả mong đợi

```text
1 2 3
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
- [061. Lưu danh sách thiết bị mạng gồm hostname, IP, status](/practice/competitive-programming-python/061-luu-danh-sach-thiet-bi-mang-gom-hostname-ip-status/)
- [062. Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN](/practice/competitive-programming-python/062-dem-bao-nhieu-thiet-bi-up-bao-nhieu-thiet-bi-down/)
- [063. Tạo dictionary lưu username và password](/practice/competitive-programming-python/063-tao-dictionary-luu-username-va-password/)

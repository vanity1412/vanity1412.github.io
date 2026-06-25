---
layout: page
title: '072. Đếm số từ trong câu'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Đếm số từ trong câu.

## Input mẫu — `input.txt`

```text
Python giúp tự động hóa công việc mạng.
```

## Kết quả mong đợi

```text
8
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
- [073. Viết hoa toàn bộ chuỗi](/practice/competitive-programming-python/073-viet-hoa-toan-bo-chuoi/)
- [074. Viết thường toàn bộ chuỗi](/practice/competitive-programming-python/074-viet-thuong-toan-bo-chuoi/)
- [075. Chuẩn hóa họ tên](/practice/competitive-programming-python/075-chuan-hoa-ho-ten/)

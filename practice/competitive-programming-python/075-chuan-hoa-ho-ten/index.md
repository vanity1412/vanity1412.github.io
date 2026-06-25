---
layout: page
title: '075. Chuẩn hóa họ tên'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Chuẩn hóa họ tên.

## Input mẫu — `input.txt`

```text
nGUYỄN   vĂN   aN
```

## Kết quả mong đợi

```text
Nguyễn Văn An
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
- [076. Tách username từ email](/practice/competitive-programming-python/076-tach-username-tu-email/)
- [077. Tách domain từ email](/practice/competitive-programming-python/077-tach-domain-tu-email/)
- [078. Kiểm tra email có chứa “@” không](/practice/competitive-programming-python/078-kiem-tra-email-co-chua-khong/)

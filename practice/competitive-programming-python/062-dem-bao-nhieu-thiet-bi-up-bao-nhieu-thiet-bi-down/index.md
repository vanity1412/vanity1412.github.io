---
layout: page
title: '062. Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN.

## Input mẫu — `input.txt`

```text
router01,192.168.1.1,UP
switch01,192.168.1.2,DOWN
firewall01,192.168.1.254,UP
switch02,192.168.1.3,DOWN
```

## Kết quả mong đợi

```text
UP: 2
DOWN: 2
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
- [063. Tạo dictionary lưu username và password](/practice/competitive-programming-python/063-tao-dictionary-luu-username-va-password/)
- [064. Tạo dictionary lưu hostname và IP](/practice/competitive-programming-python/064-tao-dictionary-luu-hostname-va-ip/)
- [065. Tìm IP theo hostname](/practice/competitive-programming-python/065-tim-ip-theo-hostname/)

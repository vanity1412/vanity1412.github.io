---
layout: page
title: '063. Tạo dictionary lưu username và password'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tạo dictionary lưu username và password.

## Input mẫu — `input.txt`

```text
admin:secret123
operator:noc2026
guest:guest
```

## Kết quả mong đợi

```text
{
  "admin": "secret123",
  "operator": "noc2026",
  "guest": "guest"
}
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
- [064. Tạo dictionary lưu hostname và IP](/practice/competitive-programming-python/064-tao-dictionary-luu-hostname-va-ip/)
- [065. Tìm IP theo hostname](/practice/competitive-programming-python/065-tim-ip-theo-hostname/)
- [066. Tìm hostname theo IP](/practice/competitive-programming-python/066-tim-hostname-theo-ip/)

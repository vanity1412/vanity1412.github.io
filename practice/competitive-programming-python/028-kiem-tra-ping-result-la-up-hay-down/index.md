---
layout: page
title: '028. Kiểm tra ping result là UP hay DOWN'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra ping result là UP hay DOWN.

## Input mẫu — `input.txt`

```text
Reply from 192.168.1.1: bytes=32 time=1ms
```

## Kết quả mong đợi

```text
UP
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
- [029. Kiểm tra trạng thái interface là up/down](/practice/competitive-programming-python/029-kiem-tra-trang-thai-interface-la-up-down/)
- [030. Kiểm tra log có chứa từ “error” không](/practice/competitive-programming-python/030-kiem-tra-log-co-chua-tu-error-khong/)
- [031. In các số từ 1 đến N](/practice/competitive-programming-python/031-in-cac-so-tu-1-den-n/)

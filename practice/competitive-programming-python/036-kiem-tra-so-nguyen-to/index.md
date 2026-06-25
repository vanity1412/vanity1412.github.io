---
layout: page
title: '036. Kiểm tra số nguyên tố'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

Kiểm tra số nguyên tố.

## Input mẫu — `input.txt`

```text
29
```

## Kết quả mong đợi

```text
Số nguyên tố
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
- [037. In các số nguyên tố từ 1 đến N](/practice/competitive-programming-python/037-in-cac-so-nguyen-to-tu-1-den-n/)
- [038. Tính giai thừa N](/practice/competitive-programming-python/038-tinh-giai-thua-n/)
- [039. In dãy Fibonacci](/practice/competitive-programming-python/039-in-day-fibonacci/)

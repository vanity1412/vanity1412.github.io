---
layout: page
title: '031. In các số từ 1 đến N'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

In các số từ 1 đến N.

## Input mẫu — `input.txt`

```text
10
```

## Kết quả mong đợi

```text
1 2 3 4 5 6 7 8 9 10
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
- [032. Tính tổng từ 1 đến N](/practice/competitive-programming-python/032-tinh-tong-tu-1-den-n/)
- [033. Tính tổng các số chẵn từ 1 đến N](/practice/competitive-programming-python/033-tinh-tong-cac-so-chan-tu-1-den-n/)
- [034. Tính tổng các số lẻ từ 1 đến N](/practice/competitive-programming-python/034-tinh-tong-cac-so-le-tu-1-den-n/)

---
layout: page
title: '039. In dãy Fibonacci'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

In dãy Fibonacci.

## Input mẫu — `input.txt`

```text
10
```

## Kết quả mong đợi

```text
0 1 1 2 3 5 8 13 21 34
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
- [040. Đếm số chữ số của một số](/practice/competitive-programming-python/040-dem-so-chu-so-cua-mot-so/)
- [041. Đảo ngược một số](/practice/competitive-programming-python/041-dao-nguoc-mot-so/)
- [042. Tính tổng các chữ số của một số](/practice/competitive-programming-python/042-tinh-tong-cac-chu-so-cua-mot-so/)

---
layout: page
title: '035. In bảng cửu chương'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

In bảng cửu chương.

## Input mẫu — `input.txt`

```text
7
```

## Kết quả mong đợi

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
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
- [036. Kiểm tra số nguyên tố](/practice/competitive-programming-python/036-kiem-tra-so-nguyen-to/)
- [037. In các số nguyên tố từ 1 đến N](/practice/competitive-programming-python/037-in-cac-so-nguyen-to-tu-1-den-n/)
- [038. Tính giai thừa N](/practice/competitive-programming-python/038-tinh-giai-thua-n/)

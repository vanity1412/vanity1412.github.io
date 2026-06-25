---
layout: page
title: '001. A cộng B'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

A cộng B.

## Input mẫu — `input.txt`

```text
7 5
```

## Kết quả mong đợi

```text
12
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
- [002. Tính tổng, hiệu, tích, thương của 2 số](/practice/competitive-programming-python/002-tinh-tong-hieu-tich-thuong-cua-2-so/)
- [003. Tính chu vi, diện tích hình chữ nhật](/practice/competitive-programming-python/003-tinh-chu-vi-dien-tich-hinh-chu-nhat/)
- [004. Tính chu vi, diện tích hình tròn](/practice/competitive-programming-python/004-tinh-chu-vi-dien-tich-hinh-tron/)

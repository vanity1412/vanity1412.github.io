---
layout: page
title: '004. Tính chu vi, diện tích hình tròn'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

Tính chu vi, diện tích hình tròn.

## Input mẫu — `input.txt`

```text
3
```

## Kết quả mong đợi

```text
Chu vi: 18.85
Diện tích: 28.27
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
- [005. Đổi độ C sang độ F](/practice/competitive-programming-python/005-doi-do-c-sang-do-f/)
- [006. Đổi giây sang giờ, phút, giây](/practice/competitive-programming-python/006-doi-giay-sang-gio-phut-giay/)
- [007. Nhập tên người dùng và in lời chào](/practice/competitive-programming-python/007-nhap-ten-nguoi-dung-va-in-loi-chao/)

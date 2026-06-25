---
layout: page
title: '005. Đổi độ C sang độ F'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

Đổi độ C sang độ F.

## Input mẫu — `input.txt`

```text
25
```

## Kết quả mong đợi

```text
77.00
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
- [006. Đổi giây sang giờ, phút, giây](/practice/competitive-programming-python/006-doi-giay-sang-gio-phut-giay/)
- [007. Nhập tên người dùng và in lời chào](/practice/competitive-programming-python/007-nhap-ten-nguoi-dung-va-in-loi-chao/)
- [008. Nhập họ tên, tuổi, trường học rồi in thông tin](/practice/competitive-programming-python/008-nhap-ho-ten-tuoi-truong-hoc-roi-in-thong-tin/)

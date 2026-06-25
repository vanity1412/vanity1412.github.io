---
layout: page
title: '014. Đổi VNĐ sang USD theo tỷ giá nhập vào'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

Đổi VNĐ sang USD theo tỷ giá nhập vào.

## Input mẫu — `input.txt`

```text
2300000 23000
```

## Kết quả mong đợi

```text
100.00 USD
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
- [015. Tính tổng dung lượng 3 file MB và đổi sang GB](/practice/competitive-programming-python/015-tinh-tong-dung-luong-3-file-mb-va-doi-sang-gb/)
- [016. Kiểm tra số chẵn/lẻ](/practice/competitive-programming-python/016-kiem-tra-so-chan-le/)
- [017. Kiểm tra số dương, âm, bằng 0](/practice/competitive-programming-python/017-kiem-tra-so-duong-am-bang-0/)

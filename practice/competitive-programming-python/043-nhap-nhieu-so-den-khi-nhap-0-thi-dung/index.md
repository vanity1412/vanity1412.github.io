---
layout: page
title: '043. Nhập nhiều số đến khi nhập 0 thì dừng'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

Nhập nhiều số đến khi nhập 0 thì dừng.

## Input mẫu — `input.txt`

```text
3
5
7
0
```

## Kết quả mong đợi

```text
Đã nhập: 3 5 7
Tổng: 15
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
- [044. Tìm số lớn nhất trong danh sách nhập từ bàn phím](/practice/competitive-programming-python/044-tim-so-lon-nhat-trong-danh-sach-nhap-tu-ban-phim/)
- [045. Tính trung bình danh sách số nhập vào](/practice/competitive-programming-python/045-tinh-trung-binh-danh-sach-so-nhap-vao/)
- [046. Nhập danh sách IP rồi in từng IP](/practice/competitive-programming-python/046-nhap-danh-sach-ip-roi-in-tung-ip/)

---
layout: page
title: '009. Tính điểm trung bình 3 môn'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

Tính điểm trung bình 3 môn.

## Input mẫu — `input.txt`

```text
8 7.5 9
```

## Kết quả mong đợi

```text
8.17
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
- [010. Tính tiền điện theo số kWh nhập vào](/practice/competitive-programming-python/010-tinh-tien-dien-theo-so-kwh-nhap-vao/)
- [011. Tính tiền mạng theo số tháng sử dụng](/practice/competitive-programming-python/011-tinh-tien-mang-theo-so-thang-su-dung/)
- [012. Tính lương nhân viên theo giờ làm và lương/giờ](/practice/competitive-programming-python/012-tinh-luong-nhan-vien-theo-gio-lam-va-luong-gio/)

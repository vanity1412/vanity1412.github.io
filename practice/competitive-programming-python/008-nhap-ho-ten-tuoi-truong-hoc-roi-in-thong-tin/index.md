---
layout: page
title: '008. Nhập họ tên, tuổi, trường học rồi in thông tin'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Nhập xuất, biến, toán tử

## Đề bài

Nhập họ tên, tuổi, trường học rồi in thông tin.

## Input mẫu — `input.txt`

```text
Nguyễn Văn An
20
Đại học Bách Khoa
```

## Kết quả mong đợi

```text
Họ tên: Nguyễn Văn An
Tuổi: 20
Trường: Đại học Bách Khoa
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
- [009. Tính điểm trung bình 3 môn](/practice/competitive-programming-python/009-tinh-diem-trung-binh-3-mon/)
- [010. Tính tiền điện theo số kWh nhập vào](/practice/competitive-programming-python/010-tinh-tien-dien-theo-so-kwh-nhap-vao/)
- [011. Tính tiền mạng theo số tháng sử dụng](/practice/competitive-programming-python/011-tinh-tien-mang-theo-so-thang-su-dung/)

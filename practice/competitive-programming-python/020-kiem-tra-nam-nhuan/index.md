---
layout: page
title: '020. Kiểm tra năm nhuận'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra năm nhuận.

## Input mẫu — `input.txt`

```text
2024
```

## Kết quả mong đợi

```text
Năm nhuận
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
- [021. Xếp loại học lực theo điểm](/practice/competitive-programming-python/021-xep-loai-hoc-luc-theo-diem/)
- [022. Kiểm tra tuổi có đủ điều kiện đi làm part-time không](/practice/competitive-programming-python/022-kiem-tra-tuoi-co-du-dieu-kien-di-lam-part-time-khong/)
- [023. Kiểm tra mật khẩu có đúng không](/practice/competitive-programming-python/023-kiem-tra-mat-khau-co-dung-khong/)

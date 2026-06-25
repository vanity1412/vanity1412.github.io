---
layout: page
title: '016. Kiểm tra số chẵn/lẻ'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra số chẵn/lẻ.

## Input mẫu — `input.txt`

```text
42
```

## Kết quả mong đợi

```text
Số chẵn
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
- [017. Kiểm tra số dương, âm, bằng 0](/practice/competitive-programming-python/017-kiem-tra-so-duong-am-bang-0/)
- [018. Tìm số lớn nhất trong 2 số](/practice/competitive-programming-python/018-tim-so-lon-nhat-trong-2-so/)
- [019. Tìm số lớn nhất trong 3 số](/practice/competitive-programming-python/019-tim-so-lon-nhat-trong-3-so/)

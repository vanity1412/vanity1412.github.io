---
layout: page
title: '027. Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không.

## Input mẫu — `input.txt`

```text
100 85
```

## Kết quả mong đợi

```text
Còn lại: 15.0% - CẢNH BÁO
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
- [028. Kiểm tra ping result là UP hay DOWN](/practice/competitive-programming-python/028-kiem-tra-ping-result-la-up-hay-down/)
- [029. Kiểm tra trạng thái interface là up/down](/practice/competitive-programming-python/029-kiem-tra-trang-thai-interface-la-up-down/)
- [030. Kiểm tra log có chứa từ “error” không](/practice/competitive-programming-python/030-kiem-tra-log-co-chua-tu-error-khong/)

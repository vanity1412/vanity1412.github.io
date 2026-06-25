---
layout: page
title: '051. Tạo danh sách 10 số và tính tổng'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tạo danh sách 10 số và tính tổng.

## Input mẫu — `input.txt`

```text
1 2 3 4 5 6 7 8 9 10
```

## Kết quả mong đợi

```text
55
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
- [052. Tìm max/min trong list](/practice/competitive-programming-python/052-tim-max-min-trong-list/)
- [053. Sắp xếp list tăng dần](/practice/competitive-programming-python/053-sap-xep-list-tang-dan/)
- [054. Sắp xếp list giảm dần](/practice/competitive-programming-python/054-sap-xep-list-giam-dan/)

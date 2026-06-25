---
layout: page
title: '054. Sắp xếp list giảm dần'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Sắp xếp list giảm dần.

## Input mẫu — `input.txt`

```text
8 3 15 -2 7 10
```

## Kết quả mong đợi

```text
15 10 8 7 3 -2
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
- [055. Xóa phần tử trùng trong list](/practice/competitive-programming-python/055-xoa-phan-tu-trung-trong-list/)
- [056. Đếm số lần xuất hiện của một số](/practice/competitive-programming-python/056-dem-so-lan-xuat-hien-cua-mot-so/)
- [057. Tách số chẵn và số lẻ thành 2 list](/practice/competitive-programming-python/057-tach-so-chan-va-so-le-thanh-2-list/)

---
layout: page
title: '057. Tách số chẵn và số lẻ thành 2 list'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tách số chẵn và số lẻ thành 2 list.

## Input mẫu — `input.txt`

```text
1 2 3 4 5 6 7 8
```

## Kết quả mong đợi

```text
Chẵn: 2 4 6 8
Lẻ: 1 3 5 7
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
- [058. Gộp 2 list thành 1 list](/practice/competitive-programming-python/058-gop-2-list-thanh-1-list/)
- [059. Tìm phần tử chung giữa 2 list](/practice/competitive-programming-python/059-tim-phan-tu-chung-giua-2-list/)
- [060. Tìm phần tử chỉ có trong list A, không có trong list B](/practice/competitive-programming-python/060-tim-phan-tu-chi-co-trong-list-a-khong-co-trong-list-b/)

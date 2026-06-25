---
layout: page
title: '067. Cập nhật trạng thái thiết bị trong dictionary'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Cập nhật trạng thái thiết bị trong dictionary.

## Input mẫu — `input.txt`

```text
router01,UP
switch01,DOWN
firewall01,UP
switch01,UP
```

## Kết quả mong đợi

```text
router01: UP
switch01: UP
firewall01: UP
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
- [068. Xóa thiết bị khỏi inventory](/practice/competitive-programming-python/068-xoa-thiet-bi-khoi-inventory/)
- [069. In danh sách thiết bị theo format bảng](/practice/competitive-programming-python/069-in-danh-sach-thiet-bi-theo-format-bang/)
- [070. Tạo inventory mạng gồm router, switch, firewall](/practice/competitive-programming-python/070-tao-inventory-mang-gom-router-switch-firewall/)

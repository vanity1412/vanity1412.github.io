---
layout: page
title: '070. Tạo inventory mạng gồm router, switch, firewall'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tạo inventory mạng gồm router, switch, firewall.

## Input mẫu — `input.txt`

```text
router,router01,192.168.1.1,UP
switch,switch01,192.168.1.2,UP
firewall,firewall01,192.168.1.254,DOWN
```

## Kết quả mong đợi

```text
ROUTER: router01 - 192.168.1.1 - UP
SWITCH: switch01 - 192.168.1.2 - UP
FIREWALL: firewall01 - 192.168.1.254 - DOWN
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
- [071. Đếm số ký tự trong chuỗi](/practice/competitive-programming-python/071-dem-so-ky-tu-trong-chuoi/)
- [072. Đếm số từ trong câu](/practice/competitive-programming-python/072-dem-so-tu-trong-cau/)
- [073. Viết hoa toàn bộ chuỗi](/practice/competitive-programming-python/073-viet-hoa-toan-bo-chuoi/)

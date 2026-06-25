---
layout: page
title: '069. In danh sách thiết bị theo format bảng'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

In danh sách thiết bị theo format bảng.

## Input mẫu — `input.txt`

```text
router01,192.168.1.1,UP
switch01,192.168.1.2,DOWN
firewall01,192.168.1.254,UP
```

## Kết quả mong đợi

```text
HOSTNAME     IP              STATUS
---------------------------------------
router01     192.168.1.1     UP
switch01     192.168.1.2     DOWN
firewall01   192.168.1.254   UP
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
- [070. Tạo inventory mạng gồm router, switch, firewall](/practice/competitive-programming-python/070-tao-inventory-mang-gom-router-switch-firewall/)
- [071. Đếm số ký tự trong chuỗi](/practice/competitive-programming-python/071-dem-so-ky-tu-trong-chuoi/)
- [072. Đếm số từ trong câu](/practice/competitive-programming-python/072-dem-so-tu-trong-cau/)

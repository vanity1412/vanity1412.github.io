---
layout: page
title: '083. Tách VLAN ID từ chuỗi "VLAN10"'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Tách VLAN ID từ chuỗi "VLAN10".

## Input mẫu — `input.txt`

```text
VLAN10
```

## Kết quả mong đợi

```text
10
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
- [084. Tách interface từ "GigabitEthernet0/1 is up"](/practice/competitive-programming-python/084-tach-interface-tu-gigabitethernet0-1-is-up/)
- [085. Kiểm tra log có chứa từ khóa "down"](/practice/competitive-programming-python/085-kiem-tra-log-co-chua-tu-khoa-down/)
- [086. Đếm số lần xuất hiện của "failed" trong log](/practice/competitive-programming-python/086-dem-so-lan-xuat-hien-cua-failed-trong-log/)

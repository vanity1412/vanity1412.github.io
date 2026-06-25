---
layout: page
title: '085. Kiểm tra log có chứa từ khóa "down"'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Kiểm tra log có chứa từ khóa "down".

## Input mẫu — `input.log`

```text
Interface GigabitEthernet0/1 changed state to down
```

## Kết quả mong đợi

```text
Có từ khóa down
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
- [086. Đếm số lần xuất hiện của "failed" trong log](/practice/competitive-programming-python/086-dem-so-lan-xuat-hien-cua-failed-trong-log/)
- [087. Thay "DOWN" thành "ALERT" trong log](/practice/competitive-programming-python/087-thay-down-thanh-alert-trong-log/)
- [088. Chuẩn hóa danh sách IP bị dư khoảng trắng](/practice/competitive-programming-python/088-chuan-hoa-danh-sach-ip-bi-du-khoang-trang/)

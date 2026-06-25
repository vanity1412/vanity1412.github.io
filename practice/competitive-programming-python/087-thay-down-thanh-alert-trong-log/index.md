---
layout: page
title: '087. Thay "DOWN" thành "ALERT" trong log'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Thay "DOWN" thành "ALERT" trong log.

## Input mẫu — `input.log`

```text
Interface Gi0/1 is DOWN; Gi0/2 is UP
```

## Kết quả mong đợi

```text
Interface Gi0/1 is ALERT; Gi0/2 is UP
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
- [088. Chuẩn hóa danh sách IP bị dư khoảng trắng](/practice/competitive-programming-python/088-chuan-hoa-danh-sach-ip-bi-du-khoang-trang/)
- [089. Tách nhiều IP từ một chuỗi](/practice/competitive-programming-python/089-tach-nhieu-ip-tu-mot-chuoi/)
- [090. Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b"](/practice/competitive-programming-python/090-tao-slug-folder-tu-ten-bai-vi-du-a-cong-b-thanh-a-cong-b/)

---
layout: page
title: '105. Đọc file JSON chứa inventory mạng'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đọc file JSON chứa inventory mạng.

## Input mẫu — `input.json`

```json
[
  {"hostname": "router01", "ip": "192.168.1.1", "status": "UP"},
  {"hostname": "switch01", "ip": "192.168.1.2", "status": "DOWN"}
]
```

## Kết quả mong đợi

```text
router01: 192.168.1.1 (UP)
switch01: 192.168.1.2 (DOWN)
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
- [106. Ghi inventory mạng ra JSON](/practice/competitive-programming-python/106-ghi-inventory-mang-ra-json/)
- [107. Thêm thiết bị mới vào JSON](/practice/competitive-programming-python/107-them-thiet-bi-moi-vao-json/)
- [108. Xóa thiết bị khỏi JSON](/practice/competitive-programming-python/108-xoa-thiet-bi-khoi-json/)

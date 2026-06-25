---
layout: page
title: '106. Ghi inventory mạng ra JSON'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Ghi inventory mạng ra JSON.

## Input mẫu — `input.json`

```json
[
  {"hostname": "router01", "ip": "192.168.1.1", "status": "UP"},
  {"hostname": "switch01", "ip": "192.168.1.2", "status": "DOWN"}
]
```

## Kết quả mong đợi

```text
[
  {
    "hostname": "router01",
    "ip": "192.168.1.1",
    "status": "UP"
  },
  {
    "hostname": "switch01",
    "ip": "192.168.1.2",
    "status": "DOWN"
  }
]
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
- [107. Thêm thiết bị mới vào JSON](/practice/competitive-programming-python/107-them-thiet-bi-moi-vao-json/)
- [108. Xóa thiết bị khỏi JSON](/practice/competitive-programming-python/108-xoa-thiet-bi-khoi-json/)
- [109. Tìm thiết bị DOWN trong JSON](/practice/competitive-programming-python/109-tim-thiet-bi-down-trong-json/)

---
layout: page
title: '109. Tìm thiết bị DOWN trong JSON'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Tìm thiết bị DOWN trong JSON.

## Input mẫu — `input.json`

```json
[
  {"hostname": "router01", "ip": "192.168.1.1", "status": "UP"},
  {"hostname": "switch01", "ip": "192.168.1.2", "status": "DOWN"},
  {"hostname": "firewall01", "ip": "192.168.1.254", "status": "DOWN"}
]
```

## Kết quả mong đợi

```text
switch01 - 192.168.1.2
firewall01 - 192.168.1.254
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
- [110. Xuất report TXT từ dữ liệu JSON](/practice/competitive-programming-python/110-xuat-report-txt-tu-du-lieu-json/)
- [111. Kiểm tra chuỗi có phải IPv4 hợp lệ không](/practice/competitive-programming-python/111-kiem-tra-chuoi-co-phai-ipv4-hop-le-khong/)
- [112. Kiểm tra IP có thuộc private IP không](/practice/competitive-programming-python/112-kiem-tra-ip-co-thuoc-private-ip-khong/)

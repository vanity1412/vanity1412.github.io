---
layout: page
title: '110. Xuất report TXT từ dữ liệu JSON'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Xuất report TXT từ dữ liệu JSON.

## Input mẫu — `input.json`

```json
[
  {"hostname": "router01", "ip": "192.168.1.1", "type": "router", "status": "UP"},
  {"hostname": "switch01", "ip": "192.168.1.2", "type": "switch", "status": "DOWN"},
  {"hostname": "firewall01", "ip": "192.168.1.254", "type": "firewall", "status": "UP"}
]
```

## Kết quả mong đợi

```text
NETWORK INVENTORY REPORT
Total: 3
UP: 2
DOWN: 1

router01 | 192.168.1.1 | router | UP
switch01 | 192.168.1.2 | switch | DOWN
firewall01 | 192.168.1.254 | firewall | UP
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
- [111. Kiểm tra chuỗi có phải IPv4 hợp lệ không](/practice/competitive-programming-python/111-kiem-tra-chuoi-co-phai-ipv4-hop-le-khong/)
- [112. Kiểm tra IP có thuộc private IP không](/practice/competitive-programming-python/112-kiem-tra-ip-co-thuoc-private-ip-khong/)
- [113. Kiểm tra IP thuộc class A/B/C](/practice/competitive-programming-python/113-kiem-tra-ip-thuoc-class-a-b-c/)

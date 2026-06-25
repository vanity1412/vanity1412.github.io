---
layout: page
title: '065. Tìm IP theo hostname'
---

**Nhóm:** B. List, tuple, dict


## Đề bài

Tìm IP theo hostname.

## Input mẫu — `input.txt`

```text
router01,192.168.1.1
switch01,192.168.1.2
firewall01,192.168.1.254
switch01
```

## Kết quả mong đợi

```text
192.168.1.2
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
- [066. Tìm hostname theo IP](/practice/competitive-programming-python/066-tim-hostname-theo-ip/)
- [067. Cập nhật trạng thái thiết bị trong dictionary](/practice/competitive-programming-python/067-cap-nhat-trang-thai-thiet-bi-trong-dictionary/)
- [068. Xóa thiết bị khỏi inventory](/practice/competitive-programming-python/068-xoa-thiet-bi-khoi-inventory/)

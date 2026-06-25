---
layout: page
title: '102. Đếm số router/switch/firewall trong CSV'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đếm số router/switch/firewall trong CSV.

## Input mẫu — `input.csv`

```csv
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,UP
switch02,192.168.1.3,switch,DOWN
firewall01,192.168.1.254,firewall,UP
```

## Kết quả mong đợi

```text
router: 1
switch: 2
firewall: 1
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
- [103. Tìm thiết bị theo IP trong file CSV](/practice/competitive-programming-python/103-tim-thiet-bi-theo-ip-trong-file-csv/)
- [104. Cập nhật trạng thái thiết bị trong file CSV](/practice/competitive-programming-python/104-cap-nhat-trang-thai-thiet-bi-trong-file-csv/)
- [105. Đọc file JSON chứa inventory mạng](/practice/competitive-programming-python/105-doc-file-json-chua-inventory-mang/)

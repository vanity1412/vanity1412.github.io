---
layout: page
title: '100. Đọc file CSV danh sách thiết bị mạng'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đọc file CSV danh sách thiết bị mạng.

## Input mẫu — `input.csv`

```csv
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,DOWN
firewall01,192.168.1.254,firewall,UP
```

## Kết quả mong đợi

```text
router01: 192.168.1.1 - router - UP
switch01: 192.168.1.2 - switch - DOWN
firewall01: 192.168.1.254 - firewall - UP
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
- [101. Ghi kết quả kiểm tra thiết bị ra CSV](/practice/competitive-programming-python/101-ghi-ket-qua-kiem-tra-thiet-bi-ra-csv/)
- [102. Đếm số router/switch/firewall trong CSV](/practice/competitive-programming-python/102-dem-so-router-switch-firewall-trong-csv/)
- [103. Tìm thiết bị theo IP trong file CSV](/practice/competitive-programming-python/103-tim-thiet-bi-theo-ip-trong-file-csv/)

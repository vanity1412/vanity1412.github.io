---
layout: page
title: '104. Cập nhật trạng thái thiết bị trong file CSV'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Cập nhật trạng thái thiết bị trong file CSV.

## Input mẫu — `input.csv`

```csv
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,DOWN
firewall01,192.168.1.254,firewall,UP
UPDATE,switch01,,UP
```

## Kết quả mong đợi

```text
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,UP
firewall01,192.168.1.254,firewall,UP
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
- [105. Đọc file JSON chứa inventory mạng](/practice/competitive-programming-python/105-doc-file-json-chua-inventory-mang/)
- [106. Ghi inventory mạng ra JSON](/practice/competitive-programming-python/106-ghi-inventory-mang-ra-json/)
- [107. Thêm thiết bị mới vào JSON](/practice/competitive-programming-python/107-them-thiet-bi-moi-vao-json/)

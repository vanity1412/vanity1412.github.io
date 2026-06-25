---
layout: page
title: '215. Tool tạo IP planning cho VLAN'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo IP planning cho VLAN.

## Input mẫu — `input.txt`

```text
10,192.168.10.0/24
20,192.168.20.0/24
30,192.168.30.0/25
99,192.168.99.0/28
```

## Kết quả mong đợi

```text
VLAN | SUBNET | GATEWAY | USABLE
10 | 192.168.10.0/24 | 192.168.10.1 | 254
20 | 192.168.20.0/24 | 192.168.20.1 | 254
30 | 192.168.30.0/25 | 192.168.30.1 | 126
99 | 192.168.99.0/28 | 192.168.99.1 | 14
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
- [216. Tool đọc inventory từ CSV](/practice/competitive-programming-python/216-tool-doc-inventory-tu-csv/)
- [217. Tool xuất report tình trạng thiết bị](/practice/competitive-programming-python/217-tool-xuat-report-tinh-trang-thiet-bi/)
- [218. Tool lọc log lỗi từ syslog](/practice/competitive-programming-python/218-tool-loc-log-loi-tu-syslog/)

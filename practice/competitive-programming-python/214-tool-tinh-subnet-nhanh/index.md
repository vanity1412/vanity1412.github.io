---
layout: page
title: '214. Tool tính subnet nhanh'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tính subnet nhanh.

## Input mẫu — `input.txt`

```text
10.20.30.0/27
```

## Kết quả mong đợi

```text
Network: 10.20.30.0
Mask: 255.255.255.224
Broadcast: 10.20.30.31
Usable: 30
Range: 10.20.30.1 - 10.20.30.30
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
- [215. Tool tạo IP planning cho VLAN](/practice/competitive-programming-python/215-tool-tao-ip-planning-cho-vlan/)
- [216. Tool đọc inventory từ CSV](/practice/competitive-programming-python/216-tool-doc-inventory-tu-csv/)
- [217. Tool xuất report tình trạng thiết bị](/practice/competitive-programming-python/217-tool-xuat-report-tinh-trang-thiet-bi/)

---
layout: page
title: '213. Tool kiểm tra IP có hợp lệ không'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra IP có hợp lệ không.

## Input mẫu — `input.txt`

```text
192.168.1.1
256.1.1.1
10.0.0.5
abc.def.1.2
```

## Kết quả mong đợi

```text
192.168.1.1: VALID
256.1.1.1: INVALID
10.0.0.5: VALID
abc.def.1.2: INVALID
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
- [214. Tool tính subnet nhanh](/practice/competitive-programming-python/214-tool-tinh-subnet-nhanh/)
- [215. Tool tạo IP planning cho VLAN](/practice/competitive-programming-python/215-tool-tao-ip-planning-cho-vlan/)
- [216. Tool đọc inventory từ CSV](/practice/competitive-programming-python/216-tool-doc-inventory-tu-csv/)

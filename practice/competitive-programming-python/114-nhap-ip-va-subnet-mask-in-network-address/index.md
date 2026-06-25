---
layout: page
title: '114. Nhập IP và subnet mask, in network address'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Nhập IP và subnet mask, in network address.

## Input mẫu — `input.txt`

```text
192.168.10.25 255.255.255.0
```

## Kết quả mong đợi

```text
192.168.10.0
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
- [115. Nhập CIDR /24, in subnet mask](/practice/competitive-programming-python/115-nhap-cidr-24-in-subnet-mask/)
- [116. Nhập subnet mask, in CIDR](/practice/competitive-programming-python/116-nhap-subnet-mask-in-cidr/)
- [117. Tính broadcast address](/practice/competitive-programming-python/117-tinh-broadcast-address/)

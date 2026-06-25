---
layout: page
title: '115. Nhập CIDR /24, in subnet mask'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Nhập CIDR /24, in subnet mask.

## Input mẫu — `input.txt`

```text
24
```

## Kết quả mong đợi

```text
255.255.255.0
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
- [116. Nhập subnet mask, in CIDR](/practice/competitive-programming-python/116-nhap-subnet-mask-in-cidr/)
- [117. Tính broadcast address](/practice/competitive-programming-python/117-tinh-broadcast-address/)
- [118. Tính số host usable trong subnet](/practice/competitive-programming-python/118-tinh-so-host-usable-trong-subnet/)

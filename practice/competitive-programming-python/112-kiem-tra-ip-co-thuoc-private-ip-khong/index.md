---
layout: page
title: '112. Kiểm tra IP có thuộc private IP không'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Kiểm tra IP có thuộc private IP không.

## Input mẫu — `input.txt`

```text
10.20.30.40
```

## Kết quả mong đợi

```text
Private IP
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
- [113. Kiểm tra IP thuộc class A/B/C](/practice/competitive-programming-python/113-kiem-tra-ip-thuoc-class-a-b-c/)
- [114. Nhập IP và subnet mask, in network address](/practice/competitive-programming-python/114-nhap-ip-va-subnet-mask-in-network-address/)
- [115. Nhập CIDR /24, in subnet mask](/practice/competitive-programming-python/115-nhap-cidr-24-in-subnet-mask/)

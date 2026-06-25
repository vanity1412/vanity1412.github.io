---
layout: page
title: '120. Kiểm tra 2 IP có cùng subnet không'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Kiểm tra 2 IP có cùng subnet không.

## Input mẫu — `input.txt`

```text
192.168.1.10 192.168.1.200 24
```

## Kết quả mong đợi

```text
Cùng subnet
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
- [121. Kiểm tra IP có nằm trong subnet 192.168.1.0/24 không](/practice/competitive-programming-python/121-kiem-tra-ip-co-nam-trong-subnet-192-168-1-0-24-khong/)
- [122. Chia mạng /24 thành các subnet /26](/practice/competitive-programming-python/122-chia-mang-24-thanh-cac-subnet-26/)
- [123. Chia mạng /24 thành 4 subnet bằng nhau](/practice/competitive-programming-python/123-chia-mang-24-thanh-4-subnet-bang-nhau/)

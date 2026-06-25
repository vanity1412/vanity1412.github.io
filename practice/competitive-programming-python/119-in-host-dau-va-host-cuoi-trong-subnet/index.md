---
layout: page
title: '119. In host đầu và host cuối trong subnet'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

In host đầu và host cuối trong subnet.

## Input mẫu — `input.txt`

```text
192.168.1.0/26
```

## Kết quả mong đợi

```text
Host đầu: 192.168.1.1
Host cuối: 192.168.1.62
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
- [120. Kiểm tra 2 IP có cùng subnet không](/practice/competitive-programming-python/120-kiem-tra-2-ip-co-cung-subnet-khong/)
- [121. Kiểm tra IP có nằm trong subnet 192.168.1.0/24 không](/practice/competitive-programming-python/121-kiem-tra-ip-co-nam-trong-subnet-192-168-1-0-24-khong/)
- [122. Chia mạng /24 thành các subnet /26](/practice/competitive-programming-python/122-chia-mang-24-thanh-cac-subnet-26/)

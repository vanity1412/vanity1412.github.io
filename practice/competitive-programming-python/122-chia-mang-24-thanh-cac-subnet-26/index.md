---
layout: page
title: '122. Chia mạng /24 thành các subnet /26'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Chia mạng /24 thành các subnet /26.

## Input mẫu — `input.txt`

```text
192.168.1.0/24
```

## Kết quả mong đợi

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
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
- [123. Chia mạng /24 thành 4 subnet bằng nhau](/practice/competitive-programming-python/123-chia-mang-24-thanh-4-subnet-bang-nhau/)
- [124. Tạo danh sách toàn bộ IP usable trong subnet](/practice/competitive-programming-python/124-tao-danh-sach-toan-bo-ip-usable-trong-subnet/)
- [125. Kiểm tra danh sách IP nào nằm ngoài subnet cho phép](/practice/competitive-programming-python/125-kiem-tra-danh-sach-ip-nao-nam-ngoai-subnet-cho-phep/)

---
layout: page
title: '123. Chia mạng /24 thành 4 subnet bằng nhau'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Chia mạng /24 thành 4 subnet bằng nhau.

## Input mẫu — `input.txt`

```text
10.10.10.0/24
```

## Kết quả mong đợi

```text
Subnet 1: 10.10.10.0/26
Subnet 2: 10.10.10.64/26
Subnet 3: 10.10.10.128/26
Subnet 4: 10.10.10.192/26
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
- [124. Tạo danh sách toàn bộ IP usable trong subnet](/practice/competitive-programming-python/124-tao-danh-sach-toan-bo-ip-usable-trong-subnet/)
- [125. Kiểm tra danh sách IP nào nằm ngoài subnet cho phép](/practice/competitive-programming-python/125-kiem-tra-danh-sach-ip-nao-nam-ngoai-subnet-cho-phep/)
- [126. Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest](/practice/competitive-programming-python/126-tao-ip-planning-cho-4-phong-ban-it-hr-sales-guest/)

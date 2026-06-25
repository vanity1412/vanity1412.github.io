---
layout: page
title: '126. Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest.

## Input mẫu — `input.txt`

```text
192.168.10.0/24
IT,50
HR,20
Sales,40
Guest,80
```

## Kết quả mong đợi

```text
Guest: 192.168.10.0/25
IT: 192.168.10.128/26
Sales: 192.168.10.192/26
HR: 192.168.11.0/27
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
- [127. Tính subnet cho từng VLAN](/practice/competitive-programming-python/127-tinh-subnet-cho-tung-vlan/)
- [128. Tạo bảng VLAN ID, subnet, gateway](/practice/competitive-programming-python/128-tao-bang-vlan-id-subnet-gateway/)
- [129. Kiểm tra gateway có nằm trong subnet không](/practice/competitive-programming-python/129-kiem-tra-gateway-co-nam-trong-subnet-khong/)

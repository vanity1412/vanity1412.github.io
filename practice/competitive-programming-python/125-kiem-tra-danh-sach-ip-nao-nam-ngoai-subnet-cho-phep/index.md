---
layout: page
title: '125. Kiểm tra danh sách IP nào nằm ngoài subnet cho phép'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Kiểm tra danh sách IP nào nằm ngoài subnet cho phép.

## Input mẫu — `input.txt`

```text
192.168.1.0/24
192.168.1.10
192.168.2.5
10.0.0.1
192.168.1.200
```

## Kết quả mong đợi

```text
192.168.2.5
10.0.0.1
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
- [126. Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest](/practice/competitive-programming-python/126-tao-ip-planning-cho-4-phong-ban-it-hr-sales-guest/)
- [127. Tính subnet cho từng VLAN](/practice/competitive-programming-python/127-tinh-subnet-cho-tung-vlan/)
- [128. Tạo bảng VLAN ID, subnet, gateway](/practice/competitive-programming-python/128-tao-bang-vlan-id-subnet-gateway/)

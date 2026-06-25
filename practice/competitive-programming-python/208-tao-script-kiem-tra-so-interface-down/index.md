---
layout: page
title: '208. Tạo script kiểm tra số interface down'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra số interface down.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,GigabitEthernet0/0,up
router01,GigabitEthernet0/1,down
switch01,GigabitEthernet0/1,up
switch01,GigabitEthernet0/2,down
switch01,GigabitEthernet0/3,down
```

## Kết quả mong đợi

```text
router01: 1 interface down
switch01: 2 interface down
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
- [209. Tạo script đẩy cấu hình description cho interface](/practice/competitive-programming-python/209-tao-script-day-cau-hinh-description-cho-interface/)
- [210. Tạo script cấu hình VLAN hàng loạt](/practice/competitive-programming-python/210-tao-script-cau-hinh-vlan-hang-loat/)
- [211. Tool kiểm tra danh sách thiết bị UP/DOWN](/practice/competitive-programming-python/211-tool-kiem-tra-danh-sach-thiet-bi-up-down/)

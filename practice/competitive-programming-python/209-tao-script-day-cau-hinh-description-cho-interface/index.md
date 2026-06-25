---
layout: page
title: '209. Tạo script đẩy cấu hình description cho interface'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script đẩy cấu hình description cho interface.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `config.txt`

```text
GigabitEthernet0/1,Uplink to Core
GigabitEthernet0/2,User Floor 1
GigabitEthernet0/3,Printer Room
```

## Kết quả mong đợi

```text
interface GigabitEthernet0/1
 description Uplink to Core
interface GigabitEthernet0/2
 description User Floor 1
interface GigabitEthernet0/3
 description Printer Room
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
- [210. Tạo script cấu hình VLAN hàng loạt](/practice/competitive-programming-python/210-tao-script-cau-hinh-vlan-hang-loat/)
- [211. Tool kiểm tra danh sách thiết bị UP/DOWN](/practice/competitive-programming-python/211-tool-kiem-tra-danh-sach-thiet-bi-up-down/)
- [212. Tool kiểm tra port dịch vụ quan trọng](/practice/competitive-programming-python/212-tool-kiem-tra-port-dich-vu-quan-trong/)

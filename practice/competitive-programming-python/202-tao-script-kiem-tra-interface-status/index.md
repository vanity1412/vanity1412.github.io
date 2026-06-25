---
layout: page
title: '202. Tạo script kiểm tra interface status'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra interface status.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,GigabitEthernet0/0,up,up
router01,GigabitEthernet0/1,down,down
switch01,GigabitEthernet0/1,up,up
switch01,GigabitEthernet0/2,up,down
```

## Kết quả mong đợi

```text
router01 GigabitEthernet0/0: up/up
router01 GigabitEthernet0/1: down/down
switch01 GigabitEthernet0/1: up/up
switch01 GigabitEthernet0/2: up/down
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
- [203. Tạo script kiểm tra VLAN trên nhiều switch](/practice/competitive-programming-python/203-tao-script-kiem-tra-vlan-tren-nhieu-switch/)
- [204. Tạo script kiểm tra OSPF neighbor](/practice/competitive-programming-python/204-tao-script-kiem-tra-ospf-neighbor/)
- [205. Tạo script kiểm tra routing table](/practice/competitive-programming-python/205-tao-script-kiem-tra-routing-table/)

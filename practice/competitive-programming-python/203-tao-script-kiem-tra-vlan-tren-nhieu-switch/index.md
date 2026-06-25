---
layout: page
title: '203. Tạo script kiểm tra VLAN trên nhiều switch'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra VLAN trên nhiều switch.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
switch01,1,default,active
switch01,10,USERS,active
switch01,20,SERVERS,active
switch02,1,default,active
switch02,10,USERS,active
```

## Kết quả mong đợi

```text
switch01: VLAN 1 default (active), VLAN 10 USERS (active), VLAN 20 SERVERS (active)
switch02: VLAN 1 default (active), VLAN 10 USERS (active)
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
- [204. Tạo script kiểm tra OSPF neighbor](/practice/competitive-programming-python/204-tao-script-kiem-tra-ospf-neighbor/)
- [205. Tạo script kiểm tra routing table](/practice/competitive-programming-python/205-tao-script-kiem-tra-routing-table/)
- [206. Tạo script kiểm tra CPU usage](/practice/competitive-programming-python/206-tao-script-kiem-tra-cpu-usage/)

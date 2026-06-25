---
layout: page
title: '201. Tạo script kiểm tra version IOS'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra version IOS.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,Cisco IOS XE Software Version 17.09.03
switch01,Cisco IOS Software Version 15.2(7)E9
router02,Cisco IOS XE Software Version 16.12.05
```

## Kết quả mong đợi

```text
router01: Cisco IOS XE Software Version 17.09.03
switch01: Cisco IOS Software Version 15.2(7)E9
router02: Cisco IOS XE Software Version 16.12.05
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
- [202. Tạo script kiểm tra interface status](/practice/competitive-programming-python/202-tao-script-kiem-tra-interface-status/)
- [203. Tạo script kiểm tra VLAN trên nhiều switch](/practice/competitive-programming-python/203-tao-script-kiem-tra-vlan-tren-nhieu-switch/)
- [204. Tạo script kiểm tra OSPF neighbor](/practice/competitive-programming-python/204-tao-script-kiem-tra-ospf-neighbor/)

---
layout: page
title: '210. Tạo script cấu hình VLAN hàng loạt'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script cấu hình VLAN hàng loạt.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `config.txt`

```text
10,USERS
20,SERVERS
30,VOICE
99,MANAGEMENT
```

## Kết quả mong đợi

```text
vlan 10
 name USERS
vlan 20
 name SERVERS
vlan 30
 name VOICE
vlan 99
 name MANAGEMENT
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
- [211. Tool kiểm tra danh sách thiết bị UP/DOWN](/practice/competitive-programming-python/211-tool-kiem-tra-danh-sach-thiet-bi-up-down/)
- [212. Tool kiểm tra port dịch vụ quan trọng](/practice/competitive-programming-python/212-tool-kiem-tra-port-dich-vu-quan-trong/)
- [213. Tool kiểm tra IP có hợp lệ không](/practice/competitive-programming-python/213-tool-kiem-tra-ip-co-hop-le-khong/)

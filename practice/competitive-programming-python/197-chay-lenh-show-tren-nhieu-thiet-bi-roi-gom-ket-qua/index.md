---
layout: page
title: '197. Chạy lệnh show trên nhiều thiết bị rồi gom kết quả'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Chạy lệnh show trên nhiều thiết bị rồi gom kết quả.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01|show clock|09:00:00 UTC Sun Jun 22 2026
router01|show ip route summary|5 routes
switch01|show vlan brief|3 active VLANs
```

## Kết quả mong đợi

```text
[router01] show clock
09:00:00 UTC Sun Jun 22 2026
[router01] show ip route summary
5 routes
[switch01] show vlan brief
3 active VLANs
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
- [198. Kiểm tra thiết bị nào SSH không được](/practice/competitive-programming-python/198-kiem-tra-thiet-bi-nao-ssh-khong-duoc/)
- [199. Ghi log lỗi khi SSH thất bại](/practice/competitive-programming-python/199-ghi-log-loi-khi-ssh-that-bai/)
- [200. Tạo script kiểm tra uptime thiết bị](/practice/competitive-programming-python/200-tao-script-kiem-tra-uptime-thiet-bi/)

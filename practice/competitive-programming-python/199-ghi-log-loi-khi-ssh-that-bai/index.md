---
layout: page
title: '199. Ghi log lỗi khi SSH thất bại'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Ghi log lỗi khi SSH thất bại.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00,switch01,192.0.2.11,Authentication failed
2026-06-22 09:00:03,router02,192.0.2.12,Connection timeout
2026-06-22 09:00:05,router01,192.0.2.10,OK
```

## Kết quả mong đợi

```text
2026-06-22 09:00:00,switch01,192.0.2.11,Authentication failed
2026-06-22 09:00:03,router02,192.0.2.12,Connection timeout
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
- [200. Tạo script kiểm tra uptime thiết bị](/practice/competitive-programming-python/200-tao-script-kiem-tra-uptime-thiet-bi/)
- [201. Tạo script kiểm tra version IOS](/practice/competitive-programming-python/201-tao-script-kiem-tra-version-ios/)
- [202. Tạo script kiểm tra interface status](/practice/competitive-programming-python/202-tao-script-kiem-tra-interface-status/)

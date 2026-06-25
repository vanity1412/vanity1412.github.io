---
layout: page
title: '198. Kiểm tra thiết bị nào SSH không được'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Kiểm tra thiết bị nào SSH không được.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,192.0.2.10,OK
switch01,192.0.2.11,FAIL
router02,192.0.2.12,FAIL
firewall01,192.0.2.13,OK
```

## Kết quả mong đợi

```text
switch01 (192.0.2.11)
router02 (192.0.2.12)
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
- [199. Ghi log lỗi khi SSH thất bại](/practice/competitive-programming-python/199-ghi-log-loi-khi-ssh-that-bai/)
- [200. Tạo script kiểm tra uptime thiết bị](/practice/competitive-programming-python/200-tao-script-kiem-tra-uptime-thiet-bi/)
- [201. Tạo script kiểm tra version IOS](/practice/competitive-programming-python/201-tao-script-kiem-tra-version-ios/)

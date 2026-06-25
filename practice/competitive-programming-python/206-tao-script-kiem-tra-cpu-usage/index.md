---
layout: page
title: '206. Tạo script kiểm tra CPU usage'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra CPU usage.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,12
switch01,67
firewall01,35
```

## Kết quả mong đợi

```text
router01: CPU 12%
switch01: CPU 67%
firewall01: CPU 35%
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
- [207. Tạo script kiểm tra memory usage](/practice/competitive-programming-python/207-tao-script-kiem-tra-memory-usage/)
- [208. Tạo script kiểm tra số interface down](/practice/competitive-programming-python/208-tao-script-kiem-tra-so-interface-down/)
- [209. Tạo script đẩy cấu hình description cho interface](/practice/competitive-programming-python/209-tao-script-day-cau-hinh-description-cho-interface/)

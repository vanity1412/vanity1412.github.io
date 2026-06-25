---
layout: page
title: '205. Tạo script kiểm tra routing table'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra routing table.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,C,192.168.1.0/24,GigabitEthernet0/1
router01,O,10.0.0.0/8,10.1.1.2
router01,S*,0.0.0.0/0,203.0.113.1
```

## Kết quả mong đợi

```text
router01: C 192.168.1.0/24 via GigabitEthernet0/1
router01: O 10.0.0.0/8 via 10.1.1.2
router01: S* 0.0.0.0/0 via 203.0.113.1
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
- [206. Tạo script kiểm tra CPU usage](/practice/competitive-programming-python/206-tao-script-kiem-tra-cpu-usage/)
- [207. Tạo script kiểm tra memory usage](/practice/competitive-programming-python/207-tao-script-kiem-tra-memory-usage/)
- [208. Tạo script kiểm tra số interface down](/practice/competitive-programming-python/208-tao-script-kiem-tra-so-interface-down/)

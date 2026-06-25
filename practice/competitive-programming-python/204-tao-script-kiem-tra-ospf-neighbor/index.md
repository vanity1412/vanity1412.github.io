---
layout: page
title: '204. Tạo script kiểm tra OSPF neighbor'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Tạo script kiểm tra OSPF neighbor.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01,1,10.0.0.2,FULL
router01,1,10.0.0.3,FULL
router02,1,10.0.0.1,INIT
```

## Kết quả mong đợi

```text
router01 area 1 neighbor 10.0.0.2: FULL
router01 area 1 neighbor 10.0.0.3: FULL
router02 area 1 neighbor 10.0.0.1: INIT
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
- [205. Tạo script kiểm tra routing table](/practice/competitive-programming-python/205-tao-script-kiem-tra-routing-table/)
- [206. Tạo script kiểm tra CPU usage](/practice/competitive-programming-python/206-tao-script-kiem-tra-cpu-usage/)
- [207. Tạo script kiểm tra memory usage](/practice/competitive-programming-python/207-tao-script-kiem-tra-memory-usage/)

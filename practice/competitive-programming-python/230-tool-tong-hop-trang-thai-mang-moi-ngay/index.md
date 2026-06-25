---
layout: page
title: '230. Tool tổng hợp trạng thái mạng mỗi ngày'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tổng hợp trạng thái mạng mỗi ngày.

## Input mẫu — `input.txt`

```text
2026-06-22
router01,UP,12,35,0
switch01,DOWN,0,0,12
firewall01,UP,45,62,0
switch02,UP,25,48,2
```

## Kết quả mong đợi

```text
DAILY NETWORK REPORT - 2026-06-22
Devices: 4 (UP 3 / DOWN 1)
Average CPU (UP): 27.3%
Average memory (UP): 48.3%
Interfaces down: 14
Down devices: switch01
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

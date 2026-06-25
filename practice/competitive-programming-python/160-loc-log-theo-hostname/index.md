---
layout: page
title: '160. Lọc log theo hostname'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log theo hostname.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00 router01 ERROR interface down
2026-06-22 09:05:00 switch01 WARNING high CPU
2026-06-22 09:10:00 router01 INFO recovered
router01
```

## Kết quả mong đợi

```text
2026-06-22 09:00:00 router01 ERROR interface down
2026-06-22 09:10:00 router01 INFO recovered
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
- [161. Lọc log theo severity](/practice/competitive-programming-python/161-loc-log-theo-severity/)
- [162. Đếm số log warning/error](/practice/competitive-programming-python/162-dem-so-log-warning-error/)
- [163. Phân loại log thành INFO, WARNING, ERROR](/practice/competitive-programming-python/163-phan-loai-log-thanh-info-warning-error/)

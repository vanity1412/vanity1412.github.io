---
layout: page
title: '158. Tách interface từ dòng log'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tách interface từ dòng log.

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:01:02 switch01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan10, changed state to up
```

## Kết quả mong đợi

```text
GigabitEthernet0/1
Vlan10
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
- [159. Lọc log theo ngày](/practice/competitive-programming-python/159-loc-log-theo-ngay/)
- [160. Lọc log theo hostname](/practice/competitive-programming-python/160-loc-log-theo-hostname/)
- [161. Lọc log theo severity](/practice/competitive-programming-python/161-loc-log-theo-severity/)

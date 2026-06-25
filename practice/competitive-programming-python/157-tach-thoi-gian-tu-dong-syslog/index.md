---
layout: page
title: '157. Tách thời gian từ dòng syslog'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tách thời gian từ dòng syslog.

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface Gi0/1 down
Jun 22 09:01:02 switch01 %SYS-5-CONFIG_I: Configured by admin
```

## Kết quả mong đợi

```text
Jun 22 09:00:01
Jun 22 09:01:02
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
- [158. Tách interface từ dòng log](/practice/competitive-programming-python/158-tach-interface-tu-dong-log/)
- [159. Lọc log theo ngày](/practice/competitive-programming-python/159-loc-log-theo-ngay/)
- [160. Lọc log theo hostname](/practice/competitive-programming-python/160-loc-log-theo-hostname/)

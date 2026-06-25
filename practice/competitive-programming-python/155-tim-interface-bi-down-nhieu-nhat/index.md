---
layout: page
title: '155. Tìm interface bị down nhiều nhất'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tìm interface bị down nhiều nhất.

## Input mẫu — `input.txt`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:02:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to down
Jun 22 09:05:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
```

## Kết quả mong đợi

```text
GigabitEthernet0/1: 2 lần
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
- [156. Tách hostname từ dòng syslog](/practice/competitive-programming-python/156-tach-hostname-tu-dong-syslog/)
- [157. Tách thời gian từ dòng syslog](/practice/competitive-programming-python/157-tach-thoi-gian-tu-dong-syslog/)
- [158. Tách interface từ dòng log](/practice/competitive-programming-python/158-tach-interface-tu-dong-log/)

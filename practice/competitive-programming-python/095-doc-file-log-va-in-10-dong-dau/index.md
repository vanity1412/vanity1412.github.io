---
layout: page
title: '095. Đọc file log và in 10 dòng đầu'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đọc file log và in 10 dòng đầu.

## Input mẫu — `input.log`

```text
log line 01
log line 02
log line 03
log line 04
log line 05
log line 06
log line 07
log line 08
log line 09
log line 10
log line 11
log line 12
```

## Kết quả mong đợi

```text
log line 01
log line 02
log line 03
log line 04
log line 05
log line 06
log line 07
log line 08
log line 09
log line 10
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
- [096. Đếm số dòng trong file log](/practice/competitive-programming-python/096-dem-so-dong-trong-file-log/)
- [097. Lọc các dòng chứa "error" ra file riêng](/practice/competitive-programming-python/097-loc-cac-dong-chua-error-ra-file-rieng/)
- [098. Lọc các dòng chứa "failed login"](/practice/competitive-programming-python/098-loc-cac-dong-chua-failed-login/)

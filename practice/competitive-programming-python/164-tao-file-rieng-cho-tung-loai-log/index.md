---
layout: page
title: '164. Tạo file riêng cho từng loại log'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tạo file riêng cho từng loại log.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00 router01 INFO ready
2026-06-22 09:05:00 router01 WARNING high CPU
2026-06-22 09:10:00 router01 ERROR interface down
2026-06-22 09:12:00 switch01 ERROR failed login
```

## Kết quả mong đợi

```text
info.log: 1 dòng
warning.log: 1 dòng
error.log: 2 dòng
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
- [165. Tìm login failed trong log](/practice/competitive-programming-python/165-tim-login-failed-trong-log/)
- [166. Tìm login successful trong log](/practice/competitive-programming-python/166-tim-login-successful-trong-log/)
- [167. Đếm số lần đăng nhập thất bại theo username](/practice/competitive-programming-python/167-dem-so-lan-dang-nhap-that-bai-theo-username/)

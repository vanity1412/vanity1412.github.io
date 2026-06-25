---
layout: page
title: '165. Tìm login failed trong log'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Tìm login failed trong log.

## Input mẫu — `input.log`

```text
2026-06-22 09:00:00 auth INFO login successful user admin from 10.0.0.2
2026-06-22 09:01:00 auth ERROR login failed user guest from 10.0.0.3
2026-06-22 09:02:00 auth ERROR LOGIN FAILED user root from 10.0.0.4
```

## Kết quả mong đợi

```text
2026-06-22 09:01:00 auth ERROR login failed user guest from 10.0.0.3
2026-06-22 09:02:00 auth ERROR LOGIN FAILED user root from 10.0.0.4
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
- [166. Tìm login successful trong log](/practice/competitive-programming-python/166-tim-login-successful-trong-log/)
- [167. Đếm số lần đăng nhập thất bại theo username](/practice/competitive-programming-python/167-dem-so-lan-dang-nhap-that-bai-theo-username/)
- [168. Đếm số lần đăng nhập thất bại theo IP](/practice/competitive-programming-python/168-dem-so-lan-dang-nhap-that-bai-theo-ip/)

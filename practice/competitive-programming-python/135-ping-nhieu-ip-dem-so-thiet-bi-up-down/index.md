---
layout: page
title: '135. Ping nhiều IP, đếm số thiết bị UP/DOWN'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP, đếm số thiết bị UP/DOWN.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10,UP
192.0.2.11,DOWN
192.0.2.12,UP
192.0.2.13,DOWN
```

## Kết quả mong đợi

```text
UP: 2
DOWN: 2
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
- [136. Ping nhiều IP, chỉ in thiết bị DOWN](/practice/competitive-programming-python/136-ping-nhieu-ip-chi-in-thiet-bi-down/)
- [137. Ping nhiều IP, thêm thời gian kiểm tra](/practice/competitive-programming-python/137-ping-nhieu-ip-them-thoi-gian-kiem-tra/)
- [138. Ping nhiều IP theo chu kỳ 5 giây](/practice/competitive-programming-python/138-ping-nhieu-ip-theo-chu-ky-5-giay/)

---
layout: page
title: '137. Ping nhiều IP, thêm thời gian kiểm tra'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP, thêm thời gian kiểm tra.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
2026-06-22 09:00:00
192.0.2.10,UP
192.0.2.11,DOWN
```

## Kết quả mong đợi

```text
2026-06-22 09:00:00 | 192.0.2.10 | UP
2026-06-22 09:00:00 | 192.0.2.11 | DOWN
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
- [138. Ping nhiều IP theo chu kỳ 5 giây](/practice/competitive-programming-python/138-ping-nhieu-ip-theo-chu-ky-5-giay/)
- [139. Ping gateway trước, nếu fail thì báo lỗi mạng nội bộ](/practice/competitive-programming-python/139-ping-gateway-truoc-neu-fail-thi-bao-loi-mang-noi-bo/)
- [140. Ping DNS 8.8.8.8 để kiểm tra internet](/practice/competitive-programming-python/140-ping-dns-8-8-8-8-de-kiem-tra-internet/)

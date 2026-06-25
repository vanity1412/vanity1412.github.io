---
layout: page
title: '138. Ping nhiều IP theo chu kỳ 5 giây'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP theo chu kỳ 5 giây.

> Demo mô phỏng ba chu kỳ, không chờ thật 5 giây.

## Input mẫu — `input.txt`

```text
192.0.2.10,UP
192.0.2.11,DOWN
```

## Kết quả mong đợi

```text
t=0s | 192.0.2.10: UP
t=0s | 192.0.2.11: DOWN
t=5s | 192.0.2.10: UP
t=5s | 192.0.2.11: DOWN
t=10s | 192.0.2.10: UP
t=10s | 192.0.2.11: DOWN
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
- [139. Ping gateway trước, nếu fail thì báo lỗi mạng nội bộ](/practice/competitive-programming-python/139-ping-gateway-truoc-neu-fail-thi-bao-loi-mang-noi-bo/)
- [140. Ping DNS 8.8.8.8 để kiểm tra internet](/practice/competitive-programming-python/140-ping-dns-8-8-8-8-de-kiem-tra-internet/)
- [141. Kiểm tra port 22 SSH có mở không](/practice/competitive-programming-python/141-kiem-tra-port-22-ssh-co-mo-khong/)

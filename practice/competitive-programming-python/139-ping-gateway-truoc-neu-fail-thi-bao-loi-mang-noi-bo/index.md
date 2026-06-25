---
layout: page
title: '139. Ping gateway trước, nếu fail thì báo lỗi mạng nội bộ'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping gateway trước, nếu fail thì báo lỗi mạng nội bộ.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
gateway,192.168.1.1,DOWN
device,192.168.1.10,UP
```

## Kết quả mong đợi

```text
Lỗi mạng nội bộ: gateway DOWN
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
- [140. Ping DNS 8.8.8.8 để kiểm tra internet](/practice/competitive-programming-python/140-ping-dns-8-8-8-8-de-kiem-tra-internet/)
- [141. Kiểm tra port 22 SSH có mở không](/practice/competitive-programming-python/141-kiem-tra-port-22-ssh-co-mo-khong/)
- [142. Kiểm tra port 80 HTTP có mở không](/practice/competitive-programming-python/142-kiem-tra-port-80-http-co-mo-khong/)

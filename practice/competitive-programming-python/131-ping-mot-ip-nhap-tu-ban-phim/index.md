---
layout: page
title: '131. Ping một IP nhập từ bàn phím'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping một IP nhập từ bàn phím.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10,UP
```

## Kết quả mong đợi

```text
192.0.2.10: UP
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
- [132. Ping nhiều IP từ file TXT](/practice/competitive-programming-python/132-ping-nhieu-ip-tu-file-txt/)
- [133. Ping nhiều IP và in UP/DOWN](/practice/competitive-programming-python/133-ping-nhieu-ip-va-in-up-down/)
- [134. Ping nhiều IP và ghi kết quả ra CSV](/practice/competitive-programming-python/134-ping-nhieu-ip-va-ghi-ket-qua-ra-csv/)

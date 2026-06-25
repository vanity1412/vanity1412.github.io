---
layout: page
title: '144. Kiểm tra nhiều port trên một IP'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Kiểm tra nhiều port trên một IP.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10,22,OPEN
192.0.2.10,80,OPEN
192.0.2.10,443,CLOSED
```

## Kết quả mong đợi

```text
192.0.2.10:22 - OPEN
192.0.2.10:80 - OPEN
192.0.2.10:443 - CLOSED
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
- [145. Kiểm tra một port trên nhiều IP](/practice/competitive-programming-python/145-kiem-tra-mot-port-tren-nhieu-ip/)
- [146. Kiểm tra danh sách IP và port từ CSV](/practice/competitive-programming-python/146-kiem-tra-danh-sach-ip-va-port-tu-csv/)
- [147. Tạo simple port scanner](/practice/competitive-programming-python/147-tao-simple-port-scanner/)

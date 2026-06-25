---
layout: page
title: '146. Kiểm tra danh sách IP và port từ CSV'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Kiểm tra danh sách IP và port từ CSV.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.csv`

```csv
mode,host,port,status
demo,192.0.2.10,22,OPEN
demo,192.0.2.11,80,CLOSED
demo,192.0.2.12,443,OPEN
```

## Kết quả mong đợi

```text
192.0.2.10:22 - OPEN
192.0.2.11:80 - CLOSED
192.0.2.12:443 - OPEN
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
- [147. Tạo simple port scanner](/practice/competitive-programming-python/147-tao-simple-port-scanner/)
- [148. Tạo tool kiểm tra service: SSH, HTTP, HTTPS, RDP, DNS](/practice/competitive-programming-python/148-tao-tool-kiem-tra-service-ssh-http-https-rdp-dns/)
- [149. Ghi kết quả port check ra CSV](/practice/competitive-programming-python/149-ghi-ket-qua-port-check-ra-csv/)

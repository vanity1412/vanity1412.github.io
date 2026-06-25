---
layout: page
title: '148. Tạo tool kiểm tra service: SSH, HTTP, HTTPS, RDP, DNS'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Tạo tool kiểm tra service: SSH, HTTP, HTTPS, RDP, DNS.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10
22,OPEN
80,OPEN
443,CLOSED
3389,CLOSED
53,OPEN
```

## Kết quả mong đợi

```text
SSH: 192.0.2.10:22 - OPEN
HTTP: 192.0.2.10:80 - OPEN
HTTPS: 192.0.2.10:443 - CLOSED
RDP: 192.0.2.10:3389 - CLOSED
DNS: 192.0.2.10:53 - OPEN
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
- [149. Ghi kết quả port check ra CSV](/practice/competitive-programming-python/149-ghi-ket-qua-port-check-ra-csv/)
- [150. Tạo report thiết bị nào mở port nguy hiểm](/practice/competitive-programming-python/150-tao-report-thiet-bi-nao-mo-port-nguy-hiem/)
- [151. Đọc file syslog Cisco](/practice/competitive-programming-python/151-doc-file-syslog-cisco/)

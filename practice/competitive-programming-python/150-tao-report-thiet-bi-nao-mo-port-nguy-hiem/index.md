---
layout: page
title: '150. Tạo report thiết bị nào mở port nguy hiểm'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Tạo report thiết bị nào mở port nguy hiểm.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
192.0.2.10,22,OPEN
192.0.2.10,23,OPEN
192.0.2.11,445,OPEN
192.0.2.12,80,OPEN
192.0.2.13,3389,CLOSED
```

## Kết quả mong đợi

```text
ALERT 192.0.2.10:23 (Telnet)
ALERT 192.0.2.11:445 (SMB)
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
- [151. Đọc file syslog Cisco](/practice/competitive-programming-python/151-doc-file-syslog-cisco/)
- [152. Lọc log có chữ "LINK-3-UPDOWN"](/practice/competitive-programming-python/152-loc-log-co-chu-link-3-updown/)
- [153. Lọc log có chữ "LINEPROTO"](/practice/competitive-programming-python/153-loc-log-co-chu-lineproto/)

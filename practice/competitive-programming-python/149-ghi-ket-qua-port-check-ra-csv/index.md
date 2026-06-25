---
layout: page
title: '149. Ghi kết quả port check ra CSV'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ghi kết quả port check ra CSV.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.csv`

```csv
mode,host,port,status
demo,192.0.2.10,22,OPEN
demo,192.0.2.10,80,OPEN
demo,192.0.2.11,443,CLOSED
```

## Kết quả mong đợi

```text
host,port,status
192.0.2.10,22,OPEN
192.0.2.10,80,OPEN
192.0.2.11,443,CLOSED
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
- [150. Tạo report thiết bị nào mở port nguy hiểm](/practice/competitive-programming-python/150-tao-report-thiet-bi-nao-mo-port-nguy-hiem/)
- [151. Đọc file syslog Cisco](/practice/competitive-programming-python/151-doc-file-syslog-cisco/)
- [152. Lọc log có chữ "LINK-3-UPDOWN"](/practice/competitive-programming-python/152-loc-log-co-chu-link-3-updown/)

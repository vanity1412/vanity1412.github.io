---
layout: page
title: '134. Ping nhiều IP và ghi kết quả ra CSV'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Ping nhiều IP và ghi kết quả ra CSV.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.csv`

```csv
mode,host,status
demo,192.0.2.10,UP
demo,192.0.2.11,DOWN
demo,192.0.2.12,UP
```

## Kết quả mong đợi

```text
host,result
192.0.2.10,UP
192.0.2.11,DOWN
192.0.2.12,UP
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
- [135. Ping nhiều IP, đếm số thiết bị UP/DOWN](/practice/competitive-programming-python/135-ping-nhieu-ip-dem-so-thiet-bi-up-down/)
- [136. Ping nhiều IP, chỉ in thiết bị DOWN](/practice/competitive-programming-python/136-ping-nhieu-ip-chi-in-thiet-bi-down/)
- [137. Ping nhiều IP, thêm thời gian kiểm tra](/practice/competitive-programming-python/137-ping-nhieu-ip-them-thoi-gian-kiem-tra/)

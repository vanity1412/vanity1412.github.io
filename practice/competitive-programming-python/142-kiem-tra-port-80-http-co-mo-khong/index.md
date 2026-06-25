---
layout: page
title: '142. Kiểm tra port 80 HTTP có mở không'
---

**Nhóm:** F. Ping, port, socket


## Đề bài

Kiểm tra port 80 HTTP có mở không.

> Input mẫu chạy ở chế độ demo để kết quả ổn định. Đổi dòng đầu thành `live` và bỏ cột trạng thái nếu muốn kiểm tra hệ thống được phép truy cập.

## Input mẫu — `input.txt`

```text
demo
192.0.2.10,80,OPEN
```

## Kết quả mong đợi

```text
192.0.2.10:80 HTTP - OPEN
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
- [143. Kiểm tra port 443 HTTPS có mở không](/practice/competitive-programming-python/143-kiem-tra-port-443-https-co-mo-khong/)
- [144. Kiểm tra nhiều port trên một IP](/practice/competitive-programming-python/144-kiem-tra-nhieu-port-tren-mot-ip/)
- [145. Kiểm tra một port trên nhiều IP](/practice/competitive-programming-python/145-kiem-tra-mot-port-tren-nhieu-ip/)

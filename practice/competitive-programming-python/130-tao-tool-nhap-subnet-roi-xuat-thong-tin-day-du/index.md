---
layout: page
title: '130. Tạo tool nhập subnet rồi xuất thông tin đầy đủ'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo tool nhập subnet rồi xuất thông tin đầy đủ.

## Input mẫu — `input.txt`

```text
192.168.50.0/27
```

## Kết quả mong đợi

```text
Network: 192.168.50.0
Netmask: 255.255.255.224
Broadcast: 192.168.50.31
Prefix: /27
Usable hosts: 30
First host: 192.168.50.1
Last host: 192.168.50.30
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
- [131. Ping một IP nhập từ bàn phím](/practice/competitive-programming-python/131-ping-mot-ip-nhap-tu-ban-phim/)
- [132. Ping nhiều IP từ file TXT](/practice/competitive-programming-python/132-ping-nhieu-ip-tu-file-txt/)
- [133. Ping nhiều IP và in UP/DOWN](/practice/competitive-programming-python/133-ping-nhieu-ip-va-in-up-down/)

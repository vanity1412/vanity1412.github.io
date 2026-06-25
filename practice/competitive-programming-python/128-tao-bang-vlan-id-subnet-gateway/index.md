---
layout: page
title: '128. Tạo bảng VLAN ID, subnet, gateway'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Tạo bảng VLAN ID, subnet, gateway.

## Input mẫu — `input.txt`

```text
10,192.168.10.0/24
20,192.168.20.0/24
30,192.168.30.0/24
```

## Kết quả mong đợi

```text
VLAN  SUBNET             GATEWAY
10    192.168.10.0/24    192.168.10.1
20    192.168.20.0/24    192.168.20.1
30    192.168.30.0/24    192.168.30.1
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
- [129. Kiểm tra gateway có nằm trong subnet không](/practice/competitive-programming-python/129-kiem-tra-gateway-co-nam-trong-subnet-khong/)
- [130. Tạo tool nhập subnet rồi xuất thông tin đầy đủ](/practice/competitive-programming-python/130-tao-tool-nhap-subnet-roi-xuat-thong-tin-day-du/)
- [131. Ping một IP nhập từ bàn phím](/practice/competitive-programming-python/131-ping-mot-ip-nhap-tu-ban-phim/)

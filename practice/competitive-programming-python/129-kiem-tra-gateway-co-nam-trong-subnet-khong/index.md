---
layout: page
title: '129. Kiểm tra gateway có nằm trong subnet không'
---

**Nhóm:** E. Python cho IP/Subnet


## Đề bài

Kiểm tra gateway có nằm trong subnet không.

## Input mẫu — `input.txt`

```text
192.168.1.0/24 192.168.1.1
```

## Kết quả mong đợi

```text
Gateway hợp lệ
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
- [130. Tạo tool nhập subnet rồi xuất thông tin đầy đủ](/practice/competitive-programming-python/130-tao-tool-nhap-subnet-roi-xuat-thong-tin-day-du/)
- [131. Ping một IP nhập từ bàn phím](/practice/competitive-programming-python/131-ping-mot-ip-nhap-tu-ban-phim/)
- [132. Ping nhiều IP từ file TXT](/practice/competitive-programming-python/132-ping-nhieu-ip-tu-file-txt/)

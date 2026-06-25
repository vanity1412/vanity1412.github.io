---
layout: page
title: '088. Chuẩn hóa danh sách IP bị dư khoảng trắng'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Chuẩn hóa danh sách IP bị dư khoảng trắng.

## Input mẫu — `input.txt`

```text
  192.168.1.1  
10.0.0.1   
   172.16.0.1
```

## Kết quả mong đợi

```text
192.168.1.1
10.0.0.1
172.16.0.1
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
- [089. Tách nhiều IP từ một chuỗi](/practice/competitive-programming-python/089-tach-nhieu-ip-tu-mot-chuoi/)
- [090. Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b"](/practice/competitive-programming-python/090-tao-slug-folder-tu-ten-bai-vi-du-a-cong-b-thanh-a-cong-b/)
- [091. Đọc file input.txt và in nội dung](/practice/competitive-programming-python/091-doc-file-input-txt-va-in-noi-dung/)

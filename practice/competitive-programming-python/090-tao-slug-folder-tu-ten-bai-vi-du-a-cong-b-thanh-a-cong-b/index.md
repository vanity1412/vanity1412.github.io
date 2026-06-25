---
layout: page
title: '090. Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b"'
---

**Nhóm:** C. Xử lý chuỗi


## Đề bài

Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b".

## Input mẫu — `input.txt`

```text
A cộng B
```

## Kết quả mong đợi

```text
a-cong-b
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
- [091. Đọc file input.txt và in nội dung](/practice/competitive-programming-python/091-doc-file-input-txt-va-in-noi-dung/)
- [092. Ghi kết quả ra file output.txt](/practice/competitive-programming-python/092-ghi-ket-qua-ra-file-output-txt/)
- [093. Đọc danh sách IP từ file TXT](/practice/competitive-programming-python/093-doc-danh-sach-ip-tu-file-txt/)

---
layout: page
title: '091. Đọc file input.txt và in nội dung'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Đọc file input.txt và in nội dung.

## Input mẫu — `input.txt`

```text
Xin chào từ input.txt!
Dòng thứ hai.
```

## Kết quả mong đợi

```text
Xin chào từ input.txt!
Dòng thứ hai.
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
- [092. Ghi kết quả ra file output.txt](/practice/competitive-programming-python/092-ghi-ket-qua-ra-file-output-txt/)
- [093. Đọc danh sách IP từ file TXT](/practice/competitive-programming-python/093-doc-danh-sach-ip-tu-file-txt/)
- [094. Ghi danh sách IP UP/DOWN ra file TXT](/practice/competitive-programming-python/094-ghi-danh-sach-ip-up-down-ra-file-txt/)

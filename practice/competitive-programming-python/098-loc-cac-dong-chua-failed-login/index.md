---
layout: page
title: '098. Lọc các dòng chứa "failed login"'
---

**Nhóm:** D. File TXT, CSV, JSON


## Đề bài

Lọc các dòng chứa "failed login".

## Input mẫu — `input.log`

```text
Login successful user admin
Failed login user guest from 10.0.0.2
FAILED LOGIN user root from 10.0.0.3
Interface up
```

## Kết quả mong đợi

```text
Failed login user guest from 10.0.0.2
FAILED LOGIN user root from 10.0.0.3
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
- [099. Lọc các dòng chứa "interface down"](/practice/competitive-programming-python/099-loc-cac-dong-chua-interface-down/)
- [100. Đọc file CSV danh sách thiết bị mạng](/practice/competitive-programming-python/100-doc-file-csv-danh-sach-thiet-bi-mang/)
- [101. Ghi kết quả kiểm tra thiết bị ra CSV](/practice/competitive-programming-python/101-ghi-ket-qua-kiem-tra-thiet-bi-ra-csv/)

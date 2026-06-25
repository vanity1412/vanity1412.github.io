---
layout: page
title: '048. Nhập N port, in port nào là 22, 80, 443'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

Nhập N port, in port nào là 22, 80, 443.

## Input mẫu — `input.txt`

```text
22 21 80 8080 443 53
```

## Kết quả mong đợi

```text
22 80 443
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
- [049. Nhập nhiều dòng log, đếm dòng có chữ “failed”](/practice/competitive-programming-python/049-nhap-nhieu-dong-log-dem-dong-co-chu-failed/)
- [050. Nhập nhiều hostname, in ra hostname viết hoa](/practice/competitive-programming-python/050-nhap-nhieu-hostname-in-ra-hostname-viet-hoa/)
- [051. Tạo danh sách 10 số và tính tổng](/practice/competitive-programming-python/051-tao-danh-sach-10-so-va-tinh-tong/)

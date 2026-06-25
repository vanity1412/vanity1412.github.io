---
layout: page
title: '045. Tính trung bình danh sách số nhập vào'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

Tính trung bình danh sách số nhập vào.

## Input mẫu — `input.txt`

```text
4 6 8 10
```

## Kết quả mong đợi

```text
7.00
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
- [046. Nhập danh sách IP rồi in từng IP](/practice/competitive-programming-python/046-nhap-danh-sach-ip-roi-in-tung-ip/)
- [047. Nhập N địa chỉ IP, kiểm tra IP nào có dạng 192.168.x.x](/practice/competitive-programming-python/047-nhap-n-dia-chi-ip-kiem-tra-ip-nao-co-dang-192-168-x-x/)
- [048. Nhập N port, in port nào là 22, 80, 443](/practice/competitive-programming-python/048-nhap-n-port-in-port-nao-la-22-80-443/)

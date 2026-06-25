---
layout: page
title: '040. Đếm số chữ số của một số'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Vòng lặp

## Đề bài

Đếm số chữ số của một số.

## Input mẫu — `input.txt`

```text
-12345
```

## Kết quả mong đợi

```text
5
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
- [041. Đảo ngược một số](/practice/competitive-programming-python/041-dao-nguoc-mot-so/)
- [042. Tính tổng các chữ số của một số](/practice/competitive-programming-python/042-tinh-tong-cac-chu-so-cua-mot-so/)
- [043. Nhập nhiều số đến khi nhập 0 thì dừng](/practice/competitive-programming-python/043-nhap-nhieu-so-den-khi-nhap-0-thi-dung/)

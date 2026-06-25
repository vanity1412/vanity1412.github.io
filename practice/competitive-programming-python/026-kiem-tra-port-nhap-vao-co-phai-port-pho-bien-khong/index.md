---
layout: page
title: '026. Kiểm tra port nhập vào có phải port phổ biến không'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra port nhập vào có phải port phổ biến không.

## Input mẫu — `input.txt`

```text
443
```

## Kết quả mong đợi

```text
HTTPS
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
- [027. Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không](/practice/competitive-programming-python/027-kiem-tra-dung-luong-o-dia-con-lai-co-duoi-20-khong/)
- [028. Kiểm tra ping result là UP hay DOWN](/practice/competitive-programming-python/028-kiem-tra-ping-result-la-up-hay-down/)
- [029. Kiểm tra trạng thái interface là up/down](/practice/competitive-programming-python/029-kiem-tra-trang-thai-interface-la-up-down/)

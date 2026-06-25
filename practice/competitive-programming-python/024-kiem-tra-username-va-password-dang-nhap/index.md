---
layout: page
title: '024. Kiểm tra username và password đăng nhập'
---

**Nhóm:** A. Python cơ bản để làm nền

**Phần:** Điều kiện if else

## Đề bài

Kiểm tra username và password đăng nhập.

## Input mẫu — `input.txt`

```text
admin 123456
```

## Kết quả mong đợi

```text
Đăng nhập thành công
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
- [025. Kiểm tra IP có thuộc mạng nội bộ 192.168.x.x không](/practice/competitive-programming-python/025-kiem-tra-ip-co-thuoc-mang-noi-bo-192-168-x-x-khong/)
- [026. Kiểm tra port nhập vào có phải port phổ biến không](/practice/competitive-programming-python/026-kiem-tra-port-nhap-vao-co-phai-port-pho-bien-khong/)
- [027. Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không](/practice/competitive-programming-python/027-kiem-tra-dung-luong-o-dia-con-lai-co-duoi-20-khong/)

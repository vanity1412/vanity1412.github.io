---
layout: page
title: '169. Phát hiện IP đăng nhập sai quá 5 lần'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Phát hiện IP đăng nhập sai quá 5 lần.

## Input mẫu — `input.txt`

```text
login failed user admin from 10.0.0.9
login failed user root from 10.0.0.9
login failed user guest from 10.0.0.9
login failed user admin from 10.0.0.9
login failed user root from 10.0.0.9
login failed user guest from 10.0.0.9
login failed user admin from 10.0.0.2
```

## Kết quả mong đợi

```text
ALERT 10.0.0.9: 6 lần
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
- [170. Tạo alert khi có nhiều dòng "failed" trong log](/practice/competitive-programming-python/170-tao-alert-khi-co-nhieu-dong-failed-trong-log/)
- [171. Tách tất cả địa chỉ IP trong file log](/practice/competitive-programming-python/171-tach-tat-ca-dia-chi-ip-trong-file-log/)
- [172. Tách tất cả MAC address trong file log](/practice/competitive-programming-python/172-tach-tat-ca-mac-address-trong-file-log/)

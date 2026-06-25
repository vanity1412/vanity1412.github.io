---
layout: page
title: '185. Kiểm tra config có đặt password chưa'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra config có đặt password chưa.

## Input mẫu — `config.txt`

```text
enable secret StrongSecret
username admin secret AdminSecret
line console 0
 password ConsoleSecret
 login
```

## Kết quả mong đợi

```text
enable secret: YES
username secret: YES
line password: YES
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
- [186. Kiểm tra config có service password-encryption chưa](/practice/competitive-programming-python/186-kiem-tra-config-co-service-password-encryption-chua/)
- [187. Kiểm tra config có banner chưa](/practice/competitive-programming-python/187-kiem-tra-config-co-banner-chua/)
- [188. Kiểm tra interface nào shutdown](/practice/competitive-programming-python/188-kiem-tra-interface-nao-shutdown/)

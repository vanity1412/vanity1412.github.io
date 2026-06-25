---
layout: page
title: '183. Tách dòng permit/deny trong ACL'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách dòng permit/deny trong ACL.

## Input mẫu — `input.txt`

```text
access-list 101 permit tcp any host 192.168.1.10 eq 443
access-list 101 deny ip any any log
access-list 10 permit 10.0.0.0 0.255.255.255
```

## Kết quả mong đợi

```text
access-list 101 permit tcp any host 192.168.1.10 eq 443
access-list 101 deny ip any any log
access-list 10 permit 10.0.0.0 0.255.255.255
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
- [184. Kiểm tra config có enable SSH chưa](/practice/competitive-programming-python/184-kiem-tra-config-co-enable-ssh-chua/)
- [185. Kiểm tra config có đặt password chưa](/practice/competitive-programming-python/185-kiem-tra-config-co-dat-password-chua/)
- [186. Kiểm tra config có service password-encryption chưa](/practice/competitive-programming-python/186-kiem-tra-config-co-service-password-encryption-chua/)

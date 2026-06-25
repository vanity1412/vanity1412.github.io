---
layout: page
title: '172. Tách tất cả MAC address trong file log'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách tất cả MAC address trong file log.

## Input mẫu — `input.log`

```text
Learned 0011.2233.4455 and aa:bb:cc:dd:ee:ff, old 00-1A-2B-3C-4D-5E
```

## Kết quả mong đợi

```text
0011.2233.4455
aa:bb:cc:dd:ee:ff
00-1A-2B-3C-4D-5E
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
- [173. Tách tất cả port number trong log](/practice/competitive-programming-python/173-tach-tat-ca-port-number-trong-log/)
- [174. Tách hostname từ config Cisco](/practice/competitive-programming-python/174-tach-hostname-tu-config-cisco/)
- [175. Tách interface từ config Cisco](/practice/competitive-programming-python/175-tach-interface-tu-config-cisco/)

---
layout: page
title: '173. Tách tất cả port number trong log'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách tất cả port number trong log.

## Input mẫu — `input.log`

```text
Connection src port 51515 dst port 443; fallback port 80
```

## Kết quả mong đợi

```text
51515
443
80
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
- [174. Tách hostname từ config Cisco](/practice/competitive-programming-python/174-tach-hostname-tu-config-cisco/)
- [175. Tách interface từ config Cisco](/practice/competitive-programming-python/175-tach-interface-tu-config-cisco/)
- [176. Tách IP address trên interface](/practice/competitive-programming-python/176-tach-ip-address-tren-interface/)

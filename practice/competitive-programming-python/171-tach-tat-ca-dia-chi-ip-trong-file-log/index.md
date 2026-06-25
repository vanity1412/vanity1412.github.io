---
layout: page
title: '171. Tách tất cả địa chỉ IP trong file log'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách tất cả địa chỉ IP trong file log.

## Input mẫu — `input.log`

```text
Router 192.168.1.1 sent packet to 10.0.0.5 via 172.16.0.1
```

## Kết quả mong đợi

```text
192.168.1.1
10.0.0.5
172.16.0.1
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
- [172. Tách tất cả MAC address trong file log](/practice/competitive-programming-python/172-tach-tat-ca-mac-address-trong-file-log/)
- [173. Tách tất cả port number trong log](/practice/competitive-programming-python/173-tach-tat-ca-port-number-trong-log/)
- [174. Tách hostname từ config Cisco](/practice/competitive-programming-python/174-tach-hostname-tu-config-cisco/)

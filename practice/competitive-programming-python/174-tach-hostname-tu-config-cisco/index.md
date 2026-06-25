---
layout: page
title: '174. Tách hostname từ config Cisco'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách hostname từ config Cisco.

## Input mẫu — `config.txt`

```text
version 15.2
hostname R1-HCM
interface GigabitEthernet0/0
```

## Kết quả mong đợi

```text
R1-HCM
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
- [175. Tách interface từ config Cisco](/practice/competitive-programming-python/175-tach-interface-tu-config-cisco/)
- [176. Tách IP address trên interface](/practice/competitive-programming-python/176-tach-ip-address-tren-interface/)
- [177. Tách default gateway](/practice/competitive-programming-python/177-tach-default-gateway/)

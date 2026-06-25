---
layout: page
title: '176. Tách IP address trên interface'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách IP address trên interface.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/0
 ip address 203.0.113.2 255.255.255.252
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
interface GigabitEthernet0/2
 no ip address
```

## Kết quả mong đợi

```text
GigabitEthernet0/0: 203.0.113.2 255.255.255.252
GigabitEthernet0/1: 192.168.1.1 255.255.255.0
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
- [177. Tách default gateway](/practice/competitive-programming-python/177-tach-default-gateway/)
- [178. Tách static route](/practice/competitive-programming-python/178-tach-static-route/)
- [179. Tách VLAN ID trong config switch](/practice/competitive-programming-python/179-tach-vlan-id-trong-config-switch/)

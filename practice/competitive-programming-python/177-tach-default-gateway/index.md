---
layout: page
title: '177. Tách default gateway'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách default gateway.

## Input mẫu — `input.txt`

```text
hostname R1
ip default-gateway 192.168.1.1
end
```

## Kết quả mong đợi

```text
192.168.1.1
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
- [178. Tách static route](/practice/competitive-programming-python/178-tach-static-route/)
- [179. Tách VLAN ID trong config switch](/practice/competitive-programming-python/179-tach-vlan-id-trong-config-switch/)
- [180. Tách access port và VLAN tương ứng](/practice/competitive-programming-python/180-tach-access-port-va-vlan-tuong-ung/)

---
layout: page
title: '180. Tách access port và VLAN tương ứng'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách access port và VLAN tương ứng.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
interface GigabitEthernet0/2
 switchport mode access
 switchport access vlan 20
interface GigabitEthernet0/24
 switchport mode trunk
```

## Kết quả mong đợi

```text
GigabitEthernet0/1 -> VLAN 10
GigabitEthernet0/2 -> VLAN 20
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
- [181. Tách trunk port](/practice/competitive-programming-python/181-tach-trunk-port/)
- [182. Tách ACL number](/practice/competitive-programming-python/182-tach-acl-number/)
- [183. Tách dòng permit/deny trong ACL](/practice/competitive-programming-python/183-tach-dong-permit-deny-trong-acl/)

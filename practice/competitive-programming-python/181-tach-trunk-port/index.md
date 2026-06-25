---
layout: page
title: '181. Tách trunk port'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tách trunk port.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/1
 switchport mode access
interface GigabitEthernet0/24
 switchport trunk allowed vlan 10,20,99
 switchport mode trunk
interface Port-channel1
 switchport mode trunk
```

## Kết quả mong đợi

```text
GigabitEthernet0/24
Port-channel1
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
- [182. Tách ACL number](/practice/competitive-programming-python/182-tach-acl-number/)
- [183. Tách dòng permit/deny trong ACL](/practice/competitive-programming-python/183-tach-dong-permit-deny-trong-acl/)
- [184. Kiểm tra config có enable SSH chưa](/practice/competitive-programming-python/184-kiem-tra-config-co-enable-ssh-chua/)

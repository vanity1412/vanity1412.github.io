---
layout: page
title: '189. Kiểm tra interface nào chưa có description'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra interface nào chưa có description.

## Input mẫu — `input.txt`

```text
interface GigabitEthernet0/1
 description Uplink to Core
 no shutdown
interface GigabitEthernet0/2
 no shutdown
interface GigabitEthernet0/3
 shutdown
```

## Kết quả mong đợi

```text
GigabitEthernet0/2
GigabitEthernet0/3
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
- [190. Tạo checklist audit config Cisco bằng Python](/practice/competitive-programming-python/190-tao-checklist-audit-config-cisco-bang-python/)
- [191. SSH vào một router và chạy lệnh show ip interface brief](/practice/competitive-programming-python/191-ssh-vao-mot-router-va-chay-lenh-show-ip-interface-brief/)
- [192. SSH vào switch và chạy show vlan brief](/practice/competitive-programming-python/192-ssh-vao-switch-va-chay-show-vlan-brief/)

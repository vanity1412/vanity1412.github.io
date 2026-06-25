---
layout: page
title: '190. Tạo checklist audit config Cisco bằng Python'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Tạo checklist audit config Cisco bằng Python.

## Input mẫu — `config.txt`

```text
hostname R1
enable password cisco
line vty 0 4
 transport input telnet
interface GigabitEthernet0/0
 no shutdown
interface GigabitEthernet0/1
 description LAN
 no shutdown
```

## Kết quả mong đợi

```text
[FAIL] Enable secret
[FAIL] SSH v2
[FAIL] Password encryption
[FAIL] Banner
[FAIL] Không dùng Telnet
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
- [191. SSH vào một router và chạy lệnh show ip interface brief](/practice/competitive-programming-python/191-ssh-vao-mot-router-va-chay-lenh-show-ip-interface-brief/)
- [192. SSH vào switch và chạy show vlan brief](/practice/competitive-programming-python/192-ssh-vao-switch-va-chay-show-vlan-brief/)
- [193. SSH vào nhiều thiết bị từ file CSV](/practice/competitive-programming-python/193-ssh-vao-nhieu-thiet-bi-tu-file-csv/)

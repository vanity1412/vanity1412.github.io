---
layout: page
title: '191. SSH vào một router và chạy lệnh show ip interface brief'
---

**Nhóm:** I. Automation với SSH


## Đề bài

SSH vào một router và chạy lệnh show ip interface brief.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
router01
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     203.0.113.2     YES manual up                    up
GigabitEthernet0/1     192.168.1.1     YES manual up                    up
```

## Kết quả mong đợi

```text
router01 - show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     203.0.113.2     YES manual up                    up
GigabitEthernet0/1     192.168.1.1     YES manual up                    up
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
- [192. SSH vào switch và chạy show vlan brief](/practice/competitive-programming-python/192-ssh-vao-switch-va-chay-show-vlan-brief/)
- [193. SSH vào nhiều thiết bị từ file CSV](/practice/competitive-programming-python/193-ssh-vao-nhieu-thiet-bi-tu-file-csv/)
- [194. Backup running-config của một thiết bị](/practice/competitive-programming-python/194-backup-running-config-cua-mot-thiet-bi/)

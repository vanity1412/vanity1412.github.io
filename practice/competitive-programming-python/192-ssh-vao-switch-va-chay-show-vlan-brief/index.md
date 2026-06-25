---
layout: page
title: '192. SSH vào switch và chạy show vlan brief'
---

**Nhóm:** I. Automation với SSH


## Đề bài

SSH vào switch và chạy show vlan brief.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
switch01
VLAN Name                             Status    Ports
1    default                          active    Gi0/1
10   USERS                            active    Gi0/2, Gi0/3
20   SERVERS                          active    Gi0/4
```

## Kết quả mong đợi

```text
switch01 - show vlan brief
VLAN Name                             Status    Ports
1    default                          active    Gi0/1
10   USERS                            active    Gi0/2, Gi0/3
20   SERVERS                          active    Gi0/4
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
- [193. SSH vào nhiều thiết bị từ file CSV](/practice/competitive-programming-python/193-ssh-vao-nhieu-thiet-bi-tu-file-csv/)
- [194. Backup running-config của một thiết bị](/practice/competitive-programming-python/194-backup-running-config-cua-mot-thiet-bi/)
- [195. Backup config nhiều thiết bị](/practice/competitive-programming-python/195-backup-config-nhieu-thiet-bi/)

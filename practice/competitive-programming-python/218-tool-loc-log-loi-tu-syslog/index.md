---
layout: page
title: '218. Tool lọc log lỗi từ syslog'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool lọc log lỗi từ syslog.

## Input mẫu — `input.log`

```text
INFO system ready
ERROR interface Gi0/1 down
WARNING high CPU
error login failed
INFO backup complete
```

## Kết quả mong đợi

```text
ERROR interface Gi0/1 down
error login failed
Tổng lỗi: 2
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
- [219. Tool phát hiện interface down](/practice/competitive-programming-python/219-tool-phat-hien-interface-down/)
- [220. Tool phát hiện login failed nhiều lần](/practice/competitive-programming-python/220-tool-phat-hien-login-failed-nhieu-lan/)
- [221. Tool backup config tự động](/practice/competitive-programming-python/221-tool-backup-config-tu-dong/)

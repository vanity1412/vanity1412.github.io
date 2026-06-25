---
layout: page
title: '161. Lọc log theo severity'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log theo severity.

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface Gi0/1 down
Jun 22 09:01:02 switch01 %SYS-5-CONFIG_I: Configured by admin
Jun 22 09:02:03 firewall01 %ASA-4-106023: Deny tcp
3
```

## Kết quả mong đợi

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface Gi0/1 down
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
- [162. Đếm số log warning/error](/practice/competitive-programming-python/162-dem-so-log-warning-error/)
- [163. Phân loại log thành INFO, WARNING, ERROR](/practice/competitive-programming-python/163-phan-loai-log-thanh-info-warning-error/)
- [164. Tạo file riêng cho từng loại log](/practice/competitive-programming-python/164-tao-file-rieng-cho-tung-loai-log/)

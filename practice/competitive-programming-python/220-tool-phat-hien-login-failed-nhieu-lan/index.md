---
layout: page
title: '220. Tool phát hiện login failed nhiều lần'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool phát hiện login failed nhiều lần.

## Input mẫu — `input.log`

```text
login failed user admin from 10.0.0.9
login failed user root from 10.0.0.9
login failed user guest from 10.0.0.9
login failed user admin from 10.0.0.9
login failed user root from 10.0.0.9
login failed user guest from 10.0.0.9
login failed user admin from 10.0.0.2
```

## Kết quả mong đợi

```text
ALERT 10.0.0.9: 6 failed logins
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
- [221. Tool backup config tự động](/practice/competitive-programming-python/221-tool-backup-config-tu-dong/)
- [222. Tool so sánh config hôm nay với hôm qua](/practice/competitive-programming-python/222-tool-so-sanh-config-hom-nay-voi-hom-qua/)
- [223. Tool kiểm tra config thiếu bảo mật](/practice/competitive-programming-python/223-tool-kiem-tra-config-thieu-bao-mat/)

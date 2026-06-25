---
layout: page
title: '219. Tool phát hiện interface down'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool phát hiện interface down.

## Input mẫu — `input.txt`

```text
Jun 22 router01 Interface Gi0/1 changed state to down
Jun 22 router01 Interface Gi0/2 changed state to up
Jun 22 switch01 Interface Gi0/24 changed state to DOWN
```

## Kết quả mong đợi

```text
ALERT router01 Gi0/1 DOWN
ALERT switch01 Gi0/24 DOWN
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
- [220. Tool phát hiện login failed nhiều lần](/practice/competitive-programming-python/220-tool-phat-hien-login-failed-nhieu-lan/)
- [221. Tool backup config tự động](/practice/competitive-programming-python/221-tool-backup-config-tu-dong/)
- [222. Tool so sánh config hôm nay với hôm qua](/practice/competitive-programming-python/222-tool-so-sanh-config-hom-nay-voi-hom-qua/)

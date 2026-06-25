---
layout: page
title: '187. Kiểm tra config có banner chưa'
---

**Nhóm:** H. Regex cho log và config


## Đề bài

Kiểm tra config có banner chưa.

## Input mẫu — `config.txt`

```text
hostname R1
banner motd #Authorized users only#
line console 0
```

## Kết quả mong đợi

```text
Đã cấu hình banner
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
- [188. Kiểm tra interface nào shutdown](/practice/competitive-programming-python/188-kiem-tra-interface-nao-shutdown/)
- [189. Kiểm tra interface nào chưa có description](/practice/competitive-programming-python/189-kiem-tra-interface-nao-chua-co-description/)
- [190. Tạo checklist audit config Cisco bằng Python](/practice/competitive-programming-python/190-tao-checklist-audit-config-cisco-bang-python/)

---
layout: page
title: '229. Tool tạo báo cáo incident dạng Markdown'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng Markdown.

## Input mẫu — `input.txt`

```text
INC-2026-003
2026-06-22 10:30
Core link flapping
Critical
Investigating optic module
NOC Team
```

## Kết quả mong đợi

```text
# Incident INC-2026-003

- **Time:** 2026-06-22 10:30
- **Title:** Core link flapping
- **Severity:** Critical
- **Status:** Investigating optic module
- **Owner:** NOC Team
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
- [230. Tool tổng hợp trạng thái mạng mỗi ngày](/practice/competitive-programming-python/230-tool-tong-hop-trang-thai-mang-moi-ngay/)

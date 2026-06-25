---
layout: page
title: '228. Tool tạo báo cáo incident dạng CSV'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng CSV.

## Input mẫu — `input.csv`

```csv
id,date,title,severity,status
INC-001,2026-06-22,Interface down,High,Resolved
INC-002,2026-06-22,Failed login,Medium,Investigating
```

## Kết quả mong đợi

```text
id,date,title,severity,status
INC-001,2026-06-22,Interface down,High,Resolved
INC-002,2026-06-22,Failed login,Medium,Investigating
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
- [229. Tool tạo báo cáo incident dạng Markdown](/practice/competitive-programming-python/229-tool-tao-bao-cao-incident-dang-markdown/)
- [230. Tool tổng hợp trạng thái mạng mỗi ngày](/practice/competitive-programming-python/230-tool-tong-hop-trang-thai-mang-moi-ngay/)

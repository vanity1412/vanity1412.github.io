---
layout: page
title: '227. Tool tạo báo cáo incident dạng TXT'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool tạo báo cáo incident dạng TXT.

## Input mẫu — `input.txt`

```text
INC-2026-001
2026-06-22 09:15
Network outage Floor 2
High
Switch access-02 lost power
Power restored and interfaces verified
```

## Kết quả mong đợi

```text
INCIDENT: INC-2026-001
Time: 2026-06-22 09:15
Title: Network outage Floor 2
Severity: High
Cause: Switch access-02 lost power
Resolution: Power restored and interfaces verified
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
- [228. Tool tạo báo cáo incident dạng CSV](/practice/competitive-programming-python/228-tool-tao-bao-cao-incident-dang-csv/)
- [229. Tool tạo báo cáo incident dạng Markdown](/practice/competitive-programming-python/229-tool-tao-bao-cao-incident-dang-markdown/)
- [230. Tool tổng hợp trạng thái mạng mỗi ngày](/practice/competitive-programming-python/230-tool-tong-hop-trang-thai-mang-moi-ngay/)

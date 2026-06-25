---
layout: page
title: '226. Tool kiểm tra port nguy hiểm đang mở'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra port nguy hiểm đang mở.

## Input mẫu — `input.txt`

```text
192.0.2.10,22,OPEN
192.0.2.10,23,OPEN
192.0.2.11,445,OPEN
192.0.2.12,3389,OPEN
192.0.2.13,80,OPEN
```

## Kết quả mong đợi

```text
ALERT 192.0.2.10:23 Telnet
ALERT 192.0.2.11:445 SMB
ALERT 192.0.2.12:3389 RDP
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
- [227. Tool tạo báo cáo incident dạng TXT](/practice/competitive-programming-python/227-tool-tao-bao-cao-incident-dang-txt/)
- [228. Tool tạo báo cáo incident dạng CSV](/practice/competitive-programming-python/228-tool-tao-bao-cao-incident-dang-csv/)
- [229. Tool tạo báo cáo incident dạng Markdown](/practice/competitive-programming-python/229-tool-tao-bao-cao-incident-dang-markdown/)

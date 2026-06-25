---
layout: page
title: '153. Lọc log có chữ "LINEPROTO"'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log có chữ "LINEPROTO".

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface Gi0/1 down
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1 down
Jun 22 09:01:02 switch01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/2 up
```

## Kết quả mong đợi

```text
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1 down
Jun 22 09:01:02 switch01 %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/2 up
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
- [154. Đếm số lần interface bị down](/practice/competitive-programming-python/154-dem-so-lan-interface-bi-down/)
- [155. Tìm interface bị down nhiều nhất](/practice/competitive-programming-python/155-tim-interface-bi-down-nhieu-nhat/)
- [156. Tách hostname từ dòng syslog](/practice/competitive-programming-python/156-tach-hostname-tu-dong-syslog/)

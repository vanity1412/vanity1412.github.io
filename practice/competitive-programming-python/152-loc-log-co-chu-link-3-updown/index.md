---
layout: page
title: '152. Lọc log có chữ "LINK-3-UPDOWN"'
---

**Nhóm:** G. Log analysis cho Network Operations


## Đề bài

Lọc log có chữ "LINK-3-UPDOWN".

## Input mẫu — `input.log`

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:00:04 router01 %LINEPROTO-5-UPDOWN: Line protocol down
Jun 22 09:01:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
```

## Kết quả mong đợi

```text
Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
Jun 22 09:01:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
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
- [153. Lọc log có chữ "LINEPROTO"](/practice/competitive-programming-python/153-loc-log-co-chu-lineproto/)
- [154. Đếm số lần interface bị down](/practice/competitive-programming-python/154-dem-so-lan-interface-bi-down/)
- [155. Tìm interface bị down nhiều nhất](/practice/competitive-programming-python/155-tim-interface-bi-down-nhieu-nhat/)

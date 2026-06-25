---
layout: page
title: '211. Tool kiểm tra danh sách thiết bị UP/DOWN'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra danh sách thiết bị UP/DOWN.

## Input mẫu — `input.txt`

```text
router01,192.0.2.10,UP
switch01,192.0.2.11,DOWN
firewall01,192.0.2.12,UP
```

## Kết quả mong đợi

```text
router01 (192.0.2.10): UP
switch01 (192.0.2.11): DOWN
firewall01 (192.0.2.12): UP
Tổng: UP=2, DOWN=1
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
- [212. Tool kiểm tra port dịch vụ quan trọng](/practice/competitive-programming-python/212-tool-kiem-tra-port-dich-vu-quan-trong/)
- [213. Tool kiểm tra IP có hợp lệ không](/practice/competitive-programming-python/213-tool-kiem-tra-ip-co-hop-le-khong/)
- [214. Tool tính subnet nhanh](/practice/competitive-programming-python/214-tool-tinh-subnet-nhanh/)

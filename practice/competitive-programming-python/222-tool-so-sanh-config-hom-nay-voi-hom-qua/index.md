---
layout: page
title: '222. Tool so sánh config hôm nay với hôm qua'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool so sánh config hôm nay với hôm qua.

## Input mẫu — `config.txt`

```text
### YESTERDAY
hostname R1
interface Gi0/1
 description OLD
 no shutdown
### TODAY
hostname R1
interface Gi0/1
 description UPLINK-CORE
 no shutdown
interface Gi0/2
 shutdown
```

## Kết quả mong đợi

```text
ADDED:
 description UPLINK-CORE
 shutdown
interface Gi0/2
REMOVED:
 description OLD
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
- [223. Tool kiểm tra config thiếu bảo mật](/practice/competitive-programming-python/223-tool-kiem-tra-config-thieu-bao-mat/)
- [224. Tool kiểm tra interface chưa có description](/practice/competitive-programming-python/224-tool-kiem-tra-interface-chua-co-description/)
- [225. Tool kiểm tra thiết bị chưa bật SSH](/practice/competitive-programming-python/225-tool-kiem-tra-thiet-bi-chua-bat-ssh/)

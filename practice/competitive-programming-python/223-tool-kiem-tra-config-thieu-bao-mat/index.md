---
layout: page
title: '223. Tool kiểm tra config thiếu bảo mật'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra config thiếu bảo mật.

## Input mẫu — `config.txt`

```text
hostname R1
enable password cisco
line vty 0 4
 transport input telnet
interface Gi0/0
 no shutdown
```

## Kết quả mong đợi

```text
FAIL: enable secret
FAIL: SSH v2
FAIL: password encryption
FAIL: banner
FAIL: no telnet
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
- [224. Tool kiểm tra interface chưa có description](/practice/competitive-programming-python/224-tool-kiem-tra-interface-chua-co-description/)
- [225. Tool kiểm tra thiết bị chưa bật SSH](/practice/competitive-programming-python/225-tool-kiem-tra-thiet-bi-chua-bat-ssh/)
- [226. Tool kiểm tra port nguy hiểm đang mở](/practice/competitive-programming-python/226-tool-kiem-tra-port-nguy-hiem-dang-mo/)

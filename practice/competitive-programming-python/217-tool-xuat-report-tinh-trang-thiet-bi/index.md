---
layout: page
title: '217. Tool xuất report tình trạng thiết bị'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool xuất report tình trạng thiết bị.

## Input mẫu — `input.txt`

```text
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,DOWN
firewall01,192.168.1.254,firewall,UP
```

## Kết quả mong đợi

```text
NETWORK STATUS REPORT
Total: 3
UP: 2
DOWN: 1
Types: firewall=1, router=1, switch=1
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
- [218. Tool lọc log lỗi từ syslog](/practice/competitive-programming-python/218-tool-loc-log-loi-tu-syslog/)
- [219. Tool phát hiện interface down](/practice/competitive-programming-python/219-tool-phat-hien-interface-down/)
- [220. Tool phát hiện login failed nhiều lần](/practice/competitive-programming-python/220-tool-phat-hien-login-failed-nhieu-lan/)

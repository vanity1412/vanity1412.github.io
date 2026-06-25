---
layout: page
title: '216. Tool đọc inventory từ CSV'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool đọc inventory từ CSV.

## Input mẫu — `input.csv`

```csv
hostname,ip,type,status
router01,192.168.1.1,router,UP
switch01,192.168.1.2,switch,DOWN
firewall01,192.168.1.254,firewall,UP
```

## Kết quả mong đợi

```text
router01   192.168.1.1     router   UP
switch01   192.168.1.2     switch   DOWN
firewall01 192.168.1.254   firewall UP
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
- [217. Tool xuất report tình trạng thiết bị](/practice/competitive-programming-python/217-tool-xuat-report-tinh-trang-thiet-bi/)
- [218. Tool lọc log lỗi từ syslog](/practice/competitive-programming-python/218-tool-loc-log-loi-tu-syslog/)
- [219. Tool phát hiện interface down](/practice/competitive-programming-python/219-tool-phat-hien-interface-down/)

---
layout: page
title: '194. Backup running-config của một thiết bị'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Backup running-config của một thiết bị.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `config.txt`

```text
router01
hostname router01
interface GigabitEthernet0/0
 ip address 203.0.113.2 255.255.255.252
 no shutdown
```

## Kết quả mong đợi

```text
Đã backup: router01-running.cfg (4 dòng)
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
- [195. Backup config nhiều thiết bị](/practice/competitive-programming-python/195-backup-config-nhieu-thiet-bi/)
- [196. Lưu backup theo tên hostname và ngày tháng](/practice/competitive-programming-python/196-luu-backup-theo-ten-hostname-va-ngay-thang/)
- [197. Chạy lệnh show trên nhiều thiết bị rồi gom kết quả](/practice/competitive-programming-python/197-chay-lenh-show-tren-nhieu-thiet-bi-roi-gom-ket-qua/)

---
layout: page
title: '193. SSH vào nhiều thiết bị từ file CSV'
---

**Nhóm:** I. Automation với SSH


## Đề bài

SSH vào nhiều thiết bị từ file CSV.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.csv`

```csv
hostname,ip,device_type,status
router01,192.0.2.10,cisco_ios,OK
switch01,192.0.2.11,cisco_ios,OK
router02,192.0.2.12,cisco_ios,FAIL
```

## Kết quả mong đợi

```text
router01 (192.0.2.10): SSH OK
switch01 (192.0.2.11): SSH OK
router02 (192.0.2.12): SSH FAIL
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
- [194. Backup running-config của một thiết bị](/practice/competitive-programming-python/194-backup-running-config-cua-mot-thiet-bi/)
- [195. Backup config nhiều thiết bị](/practice/competitive-programming-python/195-backup-config-nhieu-thiet-bi/)
- [196. Lưu backup theo tên hostname và ngày tháng](/practice/competitive-programming-python/196-luu-backup-theo-ten-hostname-va-ngay-thang/)

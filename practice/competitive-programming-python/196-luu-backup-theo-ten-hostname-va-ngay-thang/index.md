---
layout: page
title: '196. Lưu backup theo tên hostname và ngày tháng'
---

**Nhóm:** I. Automation với SSH


## Đề bài

Lưu backup theo tên hostname và ngày tháng.

> Bài mẫu dùng output SSH giả lập để chạy offline. `solve.py` có hàm `run_live_command()` tham khảo cho lab thật; chỉ kết nối thiết bị được phép quản trị.

## Input mẫu — `input.txt`

```text
2026-06-22
### router01
hostname router01
interface Gi0/0
 no shutdown
### switch01
hostname switch01
vlan 10
```

## Kết quả mong đợi

```text
router01-2026-06-22.cfg
switch01-2026-06-22.cfg
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
- [197. Chạy lệnh show trên nhiều thiết bị rồi gom kết quả](/practice/competitive-programming-python/197-chay-lenh-show-tren-nhieu-thiet-bi-roi-gom-ket-qua/)
- [198. Kiểm tra thiết bị nào SSH không được](/practice/competitive-programming-python/198-kiem-tra-thiet-bi-nao-ssh-khong-duoc/)
- [199. Ghi log lỗi khi SSH thất bại](/practice/competitive-programming-python/199-ghi-log-loi-khi-ssh-that-bai/)

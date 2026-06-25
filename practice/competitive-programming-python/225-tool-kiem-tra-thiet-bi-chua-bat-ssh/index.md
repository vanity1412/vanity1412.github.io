---
layout: page
title: '225. Tool kiểm tra thiết bị chưa bật SSH'
---

**Nhóm:** J. Mini tool cho NOC / Network Operations


## Đề bài

Tool kiểm tra thiết bị chưa bật SSH.

## Input mẫu — `input.txt`

```text
### router01
hostname router01
ip ssh version 2
line vty 0 4
 transport input ssh
### switch01
hostname switch01
line vty 0 4
 transport input telnet
```

## Kết quả mong đợi

```text
switch01
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
- [226. Tool kiểm tra port nguy hiểm đang mở](/practice/competitive-programming-python/226-tool-kiem-tra-port-nguy-hiem-dang-mo/)
- [227. Tool tạo báo cáo incident dạng TXT](/practice/competitive-programming-python/227-tool-tao-bao-cao-incident-dang-txt/)
- [228. Tool tạo báo cáo incident dạng CSV](/practice/competitive-programming-python/228-tool-tao-bao-cao-incident-dang-csv/)

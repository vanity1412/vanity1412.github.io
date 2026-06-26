---
layout: page-toc
title: "CCNA 02.02 - 2.3.7 Packet Tracer - Navigate the IOS"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `2.3.7 Packet Tracer - Navigate the IOS.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-02/` |
| Trạng thái | Hoàn thành kết nối console, truy cập CLI, kiểm tra IOS Help, chuyển EXEC mode và cấu hình clock |

> **Ghi chú:** Bài lab này không cấu hình IP. Trọng tâm là thao tác với Cisco IOS CLI trên switch S1 thông qua kết nối console từ PC1.

## 1. Mục Tiêu Bài Lab

- Kết nối PC1 với S1 bằng cáp Console.
- Mở Terminal trên PC1 và truy cập CLI của switch S1.
- Kiểm tra IOS Help bằng `?`, `t?`, `te?`.
- Chuyển đổi giữa User EXEC, Privileged EXEC và Global Configuration mode.
- Sử dụng Tab completion để hoàn thành lệnh.
- Cấu hình thời gian trên switch bằng lệnh `clock set`.
- Ghi nhận các thông báo lỗi thường gặp khi nhập lệnh sai hoặc thiếu tham số.

  Yêu cầu bài lab :
![Instructions part 1 lab 02](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/1.png)
![Instructions part 2 lab 02](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/2.png)
![Instructions part 3 lab 02](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/3.png)
  Ảnh topology:
![Topology Configure Router Interfaces](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/topology.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| End Device | PC1 | Dùng để mở Terminal và truy cập switch qua cổng RS-232 |
| Intermediary Device | S1 | Switch được truy cập qua cổng Console |
| Kết nối quản trị | PC1 RS-232 → S1 Console | Dùng cáp Console màu xanh nhạt |
| Cấu hình IP | Không có | Bài này chỉ thao tác CLI, không cần địa chỉ IP |

> **Lưu ý:** Cáp Console không dùng để ping hay truyền dữ liệu mạng như cáp Ethernet. Nó dùng để truy cập CLI quản trị thiết bị.

![Console connection lab 02](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/console-connection.png)

## 3. Part 1: Establish Basic Connections, Access the CLI, and Explore Help

### Step 1: Connect PC1 to S1 using a console cable

| Thao tác | Giá trị cần chọn |
| --- | --- |
| Loại cáp | Console cable màu xanh nhạt |
| Đầu cáp trên PC1 | RS-232 |
| Đầu cáp trên S1 | Console |

![Select console cable](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/select-console-cable.png)
![PC1 RS-232 to S1 Console](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/pc1-rs232-s1-console.png)

### Step 2: Establish a terminal session with S1

| Câu hỏi | Trả lời |
| --- | --- |
| What is the setting for bits per second? | `9600` |
| What is the prompt displayed on the screen? | `S1>` |

![Terminal default settings](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/terminal-default-settings.png)

Click OK

![S1 user exec prompt](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/s1-user-exec-prompt.png)

> **Lưu ý:** `S1>` là User EXEC mode. Ở mode này chỉ dùng được một số lệnh kiểm tra cơ bản, chưa vào được các lệnh cấu hình.

### Step 3: Explore the IOS Help

```text
S1> ?
```

| Câu hỏi | Trả lời |
| --- | --- |
| Which command begins with the letter `C`? | `connect` |

```text
S1> t?
telnet  terminal  traceroute
```

| Câu hỏi | Trả lời |
| --- | --- |
| Which commands are displayed? | `telnet`, `terminal`, `traceroute` |

```text
S1> te?
telnet  terminal
```

| Câu hỏi | Trả lời |
| --- | --- |
| Which commands are displayed? | `telnet`, `terminal` |

> **Lưu ý:** Khi dùng `?` ngay sau ký tự, IOS lọc các lệnh bắt đầu bằng chuỗi đã nhập. Ví dụ `te?` chỉ hiển thị các lệnh bắt đầu bằng `te`.

![IOS help user exec](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/ios-help-user-exec.png)

## 4. Part 2: Explore EXEC Modes

### Step 1: Enter privileged EXEC mode

```text
S1> ?
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information is displayed for the `enable` command? | `enable    Turn on privileged commands` |

```text
S1> en<Tab>
S1> enable
```

| Câu hỏi | Trả lời |
| --- | --- |
| What displays after pressing the Tab key? | `enable` |
| What would happen if you typed `te<Tab>` at the prompt? | Lệnh không được tự động hoàn thành vì `te` chưa đủ duy nhất, có thể là `telnet` hoặc `terminal` |

```text
S1> enable
S1#
```

| Câu hỏi | Trả lời |
| --- | --- |
| How does the prompt change? | Từ `S1>` chuyển thành `S1#` |

```text
S1# c?
clear  clock  configure connect copy
```

| Câu hỏi | Trả lời |
| --- | --- |
| How many commands are displayed now that privileged EXEC mode is active? | `5` command |

> **Lưu ý:** Dấu `#` cho biết thiết bị đang ở Privileged EXEC mode. Ở mode này có thể dùng nhiều lệnh kiểm tra và quản trị hơn so với User EXEC mode.

![Privileged EXEC mode](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/privileged-exec-mode.png)

### Step 2: Enter Global Configuration mode

```text
S1# configure
Configuring from terminal, memory, or network [terminal]?
```

| Câu hỏi | Trả lời |
| --- | --- |
| What is the message that is displayed? | `Configuring from terminal, memory, or network [terminal]?` |

```text
S1# configure
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#
```

| Câu hỏi | Trả lời |
| --- | --- |
| How does the prompt change? | Từ `S1#` chuyển thành `S1(config)#` |

```text
S1(config)# exit
S1#
```

> **Lưu ý:** `S1(config)#` là Global Configuration mode. Muốn quay lại Privileged EXEC mode có thể dùng `exit`, `end` hoặc `Ctrl-Z`.


## 5. Part 3: Set the Clock

### Step 1: Use the clock command

```text
S1# show clock
*12:38:54.299 UTC Mon Mar 1 1993
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information is displayed? | Thời gian, múi giờ, thứ, tháng, ngày và năm hiện tại trên switch |
| What is the year that is displayed? | `1993` |

> **Lưu ý:** Thời gian ban đầu trong Packet Tracer có thể lệch so với thời gian thật. Bài này yêu cầu dùng `clock set` để luyện cú pháp lệnh.

```text
S1# clock
% Incomplete command.
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information is displayed? | `% Incomplete command.` |

```text
S1# clock ?
  set  Set the time and date
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information is displayed? | `set  Set the time and date` |

```text
S1# clock set ?
  hh:mm:ss  Current Time
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information is being requested? | Thời gian hiện tại theo định dạng `hh:mm:ss` |
| What would have been displayed if only the `clock set` command had been entered? | `% Incomplete command.` |

```text
S1# clock set 15:00:00 ?
  <1-31>  Day of the month
  MONTH   Month of the year
```

| Thành phần | Giá trị nhập |
| --- | --- |
| Time | `15:00:00` |
| Day | `31` |
| Month | `Jan` |
| Year | `2035` |

```text
S1# clock set 15:00:00 31 Jan 2035
S1# show clock
*15:0:4.869 UTC Tue Jan 31 2035
```

> **Lưu ý:** Số giây trong output `show clock` có thể khác nhau tùy thời điểm chạy lệnh. Phần cần đúng là ngày `Tue Jan 31 2035` và thời gian bắt đầu từ `15:00`.

![Set clock successfully](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/set-clock-successfully.png)

### Step 2: Explore additional command messages

```text
S1# cl<Tab>
% Ambiguous command: "cl"
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information was returned? | `% Ambiguous command: "cl"` |

```text
S1# clock
% Incomplete command.
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information was returned? | `% Incomplete command.` |

```text
S1# clock set 25:00:00
              ^
% Invalid input detected at '^' marker.
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information was returned? | `% Invalid input detected at '^' marker.` |

```text
S1# clock set 15:00:00 32
                       ^
% Invalid input detected at '^' marker.
```

| Câu hỏi | Trả lời |
| --- | --- |
| What information was returned? | `% Invalid input detected at '^' marker.` |

> **Lưu ý:** Dấu `^` chỉ vị trí IOS phát hiện lỗi. Với `25:00:00`, lỗi nằm ở giờ không hợp lệ. Với `32`, lỗi nằm ở ngày không hợp lệ vì ngày chỉ trong khoảng `1-31`.

![Clock command errors](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-02/clock-command-errors.png)

## 6. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không vào được CLI của S1 | Chọn sai loại cáp hoặc sai cổng | Dùng Console cable, nối PC1 `RS-232` với S1 `Console` |
| Terminal không hiện prompt | Chưa nhấn `Enter` sau thông báo `Press RETURN to get started!` | Nhấn `Enter` để hiển thị `S1>` |
| `te<Tab>` không tự hoàn thành | Có nhiều lệnh bắt đầu bằng `te` | Dùng `te?` để xem danh sách, sau đó nhập rõ hơn |
| Không vào được Global Configuration mode | Chưa nhấn `Enter` ở dòng `[terminal]?` | Nhấn `Enter` để chấp nhận giá trị mặc định `terminal` |
| `% Incomplete command.` | Lệnh còn thiếu tham số | Gõ thêm dấu cách và `?` để xem tham số tiếp theo |
| `% Invalid input detected at '^' marker.` | Nhập sai cú pháp hoặc giá trị không hợp lệ | Nhìn vị trí dấu `^`, sửa đúng phần bị lỗi |
| Clock không ra đúng ngày | Nhập sai thứ tự ngày, tháng, năm | Dùng cú pháp `clock set 15:00:00 31 Jan 2035` |

## 7. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| Kết nối console | PC1 RS-232 nối với S1 Console | Hoàn thành |
| Terminal setting | Bits per second là `9600` | Hoàn thành |
| User EXEC mode | Prompt hiển thị `S1>` | Hoàn thành |
| Privileged EXEC mode | Prompt hiển thị `S1#` | Hoàn thành |
| Global Configuration mode | Prompt hiển thị `S1(config)#` | Hoàn thành |
| IOS Help | Xác định được `connect`, `telnet`, `terminal`, `traceroute` | Hoàn thành |
| Clock configuration | `show clock` hiển thị `Tue Jan 31 2035` | Hoàn thành |
| Error messages | Ghi nhận được incomplete, ambiguous và invalid input | Hoàn thành |

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 1</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 3 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 2: 2.3.7 Packet Tracer - Navigate the IOS (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

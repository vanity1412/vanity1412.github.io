---
layout: page-toc
title: "CCNA 02.05 - 10.1.4 Packet Tracer - Configure Initial Router Settings"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `10.1.4 Packet Tracer - Configure Initial Router Settings.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-05/` |
| Trạng thái | Hoàn tất cấu hình ban đầu cho router R1, kiểm tra bảo mật đăng nhập và lưu cấu hình vào NVRAM |

> Bài lab tập trung vào cấu hình khởi tạo router: đặt hostname, cấu hình banner MOTD, đặt mật khẩu console, cấu hình `enable password`, `enable secret`, mã hóa mật khẩu dạng clear text và lưu cấu hình.

## 1. Mục Tiêu Bài Lab

- Kết nối console từ PCA vào R1.
- Kiểm tra cấu hình mặc định của router.
- Cấu hình hostname cho router là `R1`.
- Cấu hình mật khẩu console, `enable password` và `enable secret`.
- Mã hóa các mật khẩu dạng clear text trong running-config.
- Cấu hình MOTD banner cảnh báo truy cập trái phép.
- Kiểm tra lại cấu hình sau khi đăng xuất/đăng nhập lại.
- Lưu running-config vào NVRAM.
- Tùy chọn: sao lưu startup-config vào flash.

![Topology lab 05](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/topology.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| End device | `PCA` | Dùng Terminal để truy cập CLI của router thông qua cổng console |
| Network device | `R1` | Router cần cấu hình ban đầu và bảo vệ truy cập CLI |
| Kết nối quản trị | Console cable | Nối từ `PCA RS-232` sang `R1 Console` |
| Cấu hình IP | Không yêu cầu | Bài này không cấu hình IP cho interface router hoặc PCA |

> **Lưu ý:** Đây là kết nối console để cấu hình thiết bị, không phải kết nối Ethernet để truyền dữ liệu mạng.

## 3. Part 1 - Verify the Default Router Configuration

### Step 1 - Truy cập router qua console

| Thao tác | Giá trị cần chọn |
| --- | --- |
| Cable | Console cable |
| PCA port | `RS-232` |
| R1 port | `Console` |
| Ứng dụng trên PCA | Desktop → Terminal |
| Terminal setting | Giữ mặc định, chọn OK |

![Console connection](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/console-connection.png)

### Step 2 - Kiểm tra cấu hình mặc định

```text
Router> enable
Router# show running-config
Router# show startup-config
```

| Câu hỏi | Đáp án |
| --- | --- |
| Hostname mặc định của router là gì? | `Router` |
| Router có bao nhiêu Fast Ethernet interface? | `0` |
| Router có bao nhiêu Gigabit Ethernet interface? | `2` |
| Router có bao nhiêu Serial interface? | `2` |
| Range của vty lines là gì? | `line vty 0 4` |
| Lệnh hiển thị nội dung NVRAM là gì? | `show startup-config` |
| Vì sao báo `startup-config is not present`? | Vì router chưa được lưu cấu hình vào NVRAM bằng lệnh `copy running-config startup-config` |

> **Lưu ý:** Số lượng interface có thể khác nếu Packet Tracer dùng model router khác. Trong bài này, kiểm tra trực tiếp bằng `show running-config` hoặc `show ip interface brief`.

![Show running config default](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/show-run-default.png)

## 4. Part 2 - Configure and Verify the Initial Router Configuration

### Step 1 - Cấu hình ban đầu cho R1

```text
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# banner motd "Unauthorized access is strictly prohibited."
R1(config)# service password-encryption
R1(config)# enable password cisco
R1(config)# enable secret itsasecret
R1(config)# line console 0
R1(config-line)# password letmein
R1(config-line)# login
R1(config-line)# exit
R1(config)# end
```

> **Lưu ý:** `enable secret` có độ ưu tiên cao hơn `enable password`. Khi cả hai cùng tồn tại, IOS sẽ yêu cầu mật khẩu `enable secret` để vào privileged EXEC mode.

![Configure R1 initial settings](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/configure-r1-initial-settings.png)

### Step 2 - Kiểm tra cấu hình trên R1

```text
R1# show running-config
```

| Nội dung cần thấy | Giá trị mong muốn |
| --- | --- |
| Hostname | `hostname R1` |
| MOTD banner | `Unauthorized access is strictly prohibited.` |
| Password encryption | `service password-encryption` |
| Enable password | Hiển thị dạng mã hóa type 7 |
| Enable secret | Hiển thị dạng hash, thường là type 5 |
| Console line | Có `password` và `login` dưới `line con 0` |

```text
hostname R1
!
service password-encryption
!
enable secret 5 <encrypted-secret>
enable password 7 <encrypted-password>
!
banner motd ^CUnauthorized access is strictly prohibited.^C
!
line con 0
 password 7 <encrypted-password>
 login
```

![Show running config after initial setup](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/show-run-after-config.png)

### Step 3 - Kiểm tra banner và mật khẩu console

```text
R1# exit

R1 con0 is now available

Press RETURN to get started.

Unauthorized access is strictly prohibited.

User Access Verification

Password:
```

| Câu hỏi | Đáp án |
| --- | --- |
| Lệnh nào dùng để xem cấu hình hiện tại của R1? | `show running-config` hoặc viết tắt `show run` |
| Vì sao router nên có MOTD banner? | Để hiển thị cảnh báo truy cập, nhắc người dùng rằng chỉ truy cập được ủy quyền mới được phép |
| Nếu không bị hỏi password trước khi vào user EXEC, đã quên lệnh nào? | Quên lệnh `login` trong `line console 0` |
| Vì sao `enable secret` dùng được còn `enable password` không còn hiệu lực? | Vì `enable secret` bảo mật hơn và được IOS ưu tiên hơn `enable password` |
| Mật khẩu cấu hình thêm sau `service password-encryption` sẽ hiển thị thế nào? | Không hiển thị plain text; các mật khẩu dạng clear text sẽ được mã hóa type 7 trong file cấu hình |

> **Lưu ý:** `service password-encryption` giúp tránh lộ mật khẩu trực tiếp khi xem cấu hình, nhưng mã hóa type 7 không phải cơ chế bảo mật mạnh. Với privileged EXEC nên ưu tiên `enable secret`.

![Console password verification](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/console-password-verification.png)

## 5. Part 3 - Save the Running Configuration File

### Step 1 - Lưu cấu hình vào NVRAM

```text
R1> enable
Password:
R1# copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
```

| Câu hỏi | Đáp án |
| --- | --- |
| Lệnh lưu cấu hình vào NVRAM là gì? | `copy running-config startup-config` |
| Phiên bản viết tắt thường dùng là gì? | `copy run start` |
| Lệnh kiểm tra startup-config là gì? | `show startup-config` |
| Các thay đổi đã nhập có được ghi lại không? | Có, nếu đã copy running-config sang startup-config thành công |

```text
R1# show startup-config
```

![Save running config to NVRAM](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/save-running-config.png)

### Step 2 - Tùy chọn: sao lưu startup-config vào flash

```text
R1# show flash:
R1# copy startup-config flash:
Destination filename [startup-config]? 
R1# show flash:
```

| Câu hỏi | Đáp án |
| --- | --- |
| Có bao nhiêu file trong flash? | Phụ thuộc vào router trong Packet Tracer; kiểm tra bằng `show flash:` |
| File nào có khả năng là IOS image? | File có đuôi `.bin` |
| Vì sao xác định đó là IOS image? | Vì IOS image thường là file `.bin`, tên có dạng platform + IOS version và dung lượng lớn hơn file cấu hình |
| Sau khi copy, cần thấy file nào trong flash? | `startup-config` |

> **Lưu ý:** Router vẫn boot cấu hình từ NVRAM. Bản `startup-config` trong flash chỉ là bản sao lưu bổ sung để phục hồi khi cần.

![Startup config backup in flash](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-05/startup-config-flash-backup.png)

## 6. Cấu Hình Hoàn Chỉnh Trên R1

```text
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# banner motd "Unauthorized access is strictly prohibited."
R1(config)# service password-encryption
R1(config)# enable password cisco
R1(config)# enable secret itsasecret
R1(config)# line console 0
R1(config-line)# password letmein
R1(config-line)# login
R1(config-line)# exit
R1(config)# end
R1# copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
```

## 7. Lỗi Thường Gặp Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Không thấy thông báo hỏi password khi vào console | Đã đặt `password letmein` nhưng quên `login` | Vào `line console 0`, nhập lại `login` |
| Không vào được privileged EXEC bằng `cisco` | Đã cấu hình `enable secret itsasecret`, IOS ưu tiên secret | Dùng `itsasecret` khi gõ `enable` |
| Mật khẩu vẫn hiện plain text trong `show run` | Chưa bật `service password-encryption` | Vào global config và nhập `service password-encryption` |
| Sau khi reload bị mất cấu hình | Chưa lưu running-config vào startup-config | Chạy `copy running-config startup-config` |
| Banner không đúng yêu cầu | Sai nội dung hoặc sai delimiter | Cấu hình lại `banner motd "Unauthorized access is strictly prohibited."` |
| Gõ `show startup-config` báo không có file | Chưa có cấu hình trong NVRAM | Lưu cấu hình bằng `copy run start` |

## 8. Kết Quả Cuối

| Hạng mục kiểm tra | Kết quả mong muốn |
| --- | --- |
| Console từ PCA vào R1 | Truy cập được Terminal của R1 |
| Hostname | Prompt chuyển thành `R1#` |
| MOTD banner | Hiển thị `Unauthorized access is strictly prohibited.` trước khi đăng nhập |
| Console password | Khi nhấn Enter vào console sẽ yêu cầu password |
| Enable secret | Dùng `itsasecret` để vào privileged EXEC mode |
| Password encryption | `enable password` và `line console password` không còn hiện plain text |
| Startup-config | `show startup-config` hiển thị cấu hình đã lưu |
| Backup flash tùy chọn | `show flash:` có thêm file `startup-config` sau khi copy |

Checklist ảnh minh chứng nên chèn vào writeup:

- [ ] Ảnh topology ban đầu.
- [ ] Ảnh kết nối console PCA → R1.
- [ ] Ảnh `show running-config` mặc định.
- [ ] Ảnh cấu hình hostname, banner, password.
- [ ] Ảnh kiểm tra banner và console password sau khi đăng xuất.
- [ ] Ảnh `show running-config` sau khi mã hóa mật khẩu.
- [ ] Ảnh `copy running-config startup-config` báo `[OK]`.
- [ ] Ảnh `show startup-config`.
- [ ] Ảnh `show flash:` nếu làm phần optional.
---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 4</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 6 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/">Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

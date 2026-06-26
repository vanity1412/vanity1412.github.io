---
layout: page-toc
title: "CCNA 02.03 - 2.5.5 Packet Tracer - Configure Initial Switch Settings"
permalink: /writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-03/
toc: true
---

[← Quay lại danh sách IOS Và Cấu Hình Cơ Bản](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/)

| Field | Value |
| --- | --- |
| Dạng lab | IOS Và Cấu Hình Cơ Bản |
| File lab | `2.5.5 Packet Tracer - Configure Initial Switch Settings.pka` |
| Loại file | `PKA` |
| Thư mục ảnh | `labs/lab-03/` |
| Trạng thái | Hoàn tất cấu hình cơ bản S1, S2, console password, enable password, enable secret, MOTD banner, mã hóa password và lưu cấu hình |

> Bài này tập trung vào cấu hình ban đầu cho switch Cisco 2960: kiểm tra cấu hình mặc định, đặt hostname, bảo vệ cổng console, bảo vệ privileged EXEC mode, cấu hình banner cảnh báo và lưu cấu hình vào NVRAM.

## 1. Mục Tiêu Bài Lab

- Kiểm tra cấu hình mặc định của switch bằng `show running-config`.
- Xác định số lượng cổng FastEthernet, GigabitEthernet và dải `vty line` trên switch.
- Đặt hostname cho S1 và S2.
- Cấu hình mật khẩu console bằng `line console 0`.
- Cấu hình `enable password` và `enable secret` để bảo vệ privileged EXEC mode.
- Mã hóa các mật khẩu đang hiển thị dạng plain text.
- Cấu hình MOTD banner cảnh báo truy cập trái phép.
- Lưu cấu hình từ running-config sang startup-config.

![lab 03](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/exam.png)

![Topology lab 03](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/topology.png)

## 2. Topology Overview

| Khu vực | Thiết bị | Nhận xét |
| --- | --- | --- |
| Bên trái | PC1, S1 | PC1 dùng để truy cập CLI của S1 trong quá trình cấu hình |
| Bên phải | PC2, S2 | PC2 dùng để truy cập CLI của S2 trong phần cấu hình cuối |
| Liên kết switch | S1 ↔ S2 | Có kết nối giữa 2 switch, nhưng bài này chưa yêu cầu cấu hình VLAN/IP |
| Liên kết PC-switch | PC1 ↔ S1, PC2 ↔ S2 | Dùng để mô phỏng kết nối thiết bị đầu cuối với switch |

> **Lưu ý:** Bài này không yêu cầu cấu hình địa chỉ IP cho PC hoặc switch. Trọng tâm là bảo mật truy cập CLI và lưu cấu hình thiết bị.

## 3. Part 1 - Verify the Default Switch Configuration

### Step 1 - Vào privileged EXEC mode trên S1

```text
Switch> enable
Switch#
```

![S1 enable mode](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-enable-mode.png)

### Step 2 - Kiểm tra running-config mặc định

```text
Switch# show running-config
```

| Câu hỏi | Đáp án |
| --- | --- |
| How many Fast Ethernet interfaces does the switch have? | 24 cổng FastEthernet, từ `FastEthernet0/1` đến `FastEthernet0/24` |
| How many Gigabit Ethernet interfaces does the switch have? | 2 cổng GigabitEthernet, gồm `GigabitEthernet0/1` và `GigabitEthernet0/2` |
| What is the range of values shown for the vty lines? | `line vty 0 4` và `line vty 5 15`, tổng dải là `0 - 15` |
| Which command will display the current contents of NVRAM? | `show startup-config` |
| Why does the switch respond with “startup-config is not present?” | Vì cấu hình chưa được lưu vào NVRAM bằng lệnh `copy running-config startup-config` |

![S1 default running config](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-default-running-config.png)

> **Lưu ý:** `running-config` là cấu hình đang chạy trong RAM. `startup-config` là cấu hình lưu trong NVRAM và được dùng lại sau khi thiết bị khởi động lại.

## 4. Part 2 - Create a Basic Switch Configuration

### Step 1 - Đặt hostname cho S1

```text
Switch# configure terminal
Switch(config)# hostname S1
S1(config)# exit
S1#
```

![S1 hostname](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-hostname.png)

### Step 2 - Cấu hình mật khẩu console cho S1

```text
S1# configure terminal
S1(config)# line console 0
S1(config-line)# password letmein
S1(config-line)# login
S1(config-line)# exit
S1(config)# exit
S1#
```

| Câu hỏi | Đáp án |
| --- | --- |
| Why is the login command required? | Vì `login` yêu cầu switch thực sự kiểm tra mật khẩu khi người dùng truy cập console. Nếu chỉ đặt `password letmein` mà không có `login`, switch sẽ không bắt nhập mật khẩu console. |

> **Lưu ý:** `password` chỉ tạo mật khẩu cho line console, còn `login` mới bật cơ chế yêu cầu nhập mật khẩu.

### Step 3 - Kiểm tra console password

```text
S1# exit

Switch con0 is now available

Press RETURN to get started.

User Access Verification
Password:
S1>
```

![S1 console password verification](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-console-password-verification.png)

### Step 4 - Cấu hình enable password cho S1

```text
S1> enable
S1# configure terminal
S1(config)# enable password c1$c0
S1(config)# exit
S1#
```

> **Lưu ý:** Ký tự `0` trong `c1$c0` là số không, không phải chữ O viết hoa.

### Step 5 - Kiểm tra enable password

```text
S1# exit

Switch con0 is now available

Press RETURN to get started.

User Access Verification
Password: letmein
S1> enable
Password: c1$c0
S1# show running-config
```

![S1 enable password verification](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-enable-password-verification.png)

> **Lưu ý:** Ở bước này, `enable password` và `line console password` vẫn có thể xuất hiện dạng plain text trong `show running-config`.

### Step 6 - Cấu hình enable secret cho S1

```text
S1# configure terminal
S1(config)# enable secret itsasecret
S1(config)# exit
S1#
```

> **Lưu ý:** Nếu vừa có `enable password` vừa có `enable secret`, switch sẽ ưu tiên dùng `enable secret` khi vào privileged EXEC mode.

### Step 7 - Kiểm tra enable secret trong running-config

```text
S1# show running-config
```

| Câu hỏi | Đáp án |
| --- | --- |
| What is displayed for the enable secret password? | Mật khẩu `itsasecret` không hiện trực tiếp, mà hiển thị ở dạng mã hóa/hash, ví dụ `enable secret 5 $1$...` |
| Why is the enable secret password displayed differently from what we configured? | Vì `enable secret` được IOS lưu ở dạng mã hóa/hash để không lộ mật khẩu thật trong file cấu hình. |

### Step 8 - Mã hóa enable password và console password

```text
S1# configure terminal
S1(config)# service password-encryption
S1(config)# exit
S1# show running-config
```

| Câu hỏi | Đáp án |
| --- | --- |
| If you configure any more passwords on the switch, will they be displayed in the configuration file as plain text or in encrypted form? Explain. | Các mật khẩu dạng plain text được cấu hình sau đó sẽ hiển thị ở dạng encrypted trong file cấu hình. Tuy nhiên đây là mã hóa Cisco type 7, chỉ giúp tránh nhìn thấy trực tiếp mật khẩu, không phải cơ chế bảo mật mạnh như `enable secret`. |

![S1 service password encryption](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-service-password-encryption.png)

## 5. Part 3 - Configure a MOTD Banner

### Step 1 - Cấu hình banner cảnh báo trên S1

```text
S1# configure terminal
S1(config)# banner motd "This is a secure system. Authorized Access Only!"
S1(config)# exit
S1#
```

| Câu hỏi | Đáp án |
| --- | --- |
| When will this banner be displayed? | Banner hiển thị khi người dùng truy cập vào switch qua console, Telnet hoặc SSH, thường xuất hiện trước bước đăng nhập. |
| Why should every switch have a MOTD banner? | Để cảnh báo người dùng không được phép truy cập trái phép và thông báo hệ thống chỉ dành cho người được ủy quyền. |

![S1 motd banner](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-motd-banner.png)

## 6. Part 4 - Save and Verify Configuration Files to NVRAM

### Step 1 - Lưu cấu hình S1

```text
S1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

| Câu hỏi | Đáp án |
| --- | --- |
| What is the shortest, abbreviated version of the copy running-config startup-config command? | `copy run start` |
| Which command will display the contents of NVRAM? | `show startup-config` |
| Are all the changes that were entered recorded in the file? | Có. Sau khi lưu, hostname, console password, enable password, enable secret, MOTD banner và `service password-encryption` đều được ghi vào startup-config. |

```text
S1# show startup-config
```

![S1 startup config](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/s1-startup-config.png)

## 7. Part 5 - Configure S2

### Cấu hình hoàn chỉnh trên S2

```text
Switch> enable
Switch# configure terminal

! Đặt hostname
Switch(config)# hostname S2

! Bảo vệ console
S2(config)# line console 0
S2(config-line)# password letmein
S2(config-line)# login
S2(config-line)# exit

! Bảo vệ privileged EXEC mode
S2(config)# enable password c1$c0
S2(config)# enable secret itsasecret

! Cấu hình banner cảnh báo
S2(config)# banner motd "This is a secure system. Authorized Access Only!"

! Mã hóa các mật khẩu plain text
S2(config)# service password-encryption
S2(config)# end

! Kiểm tra cấu hình đang chạy
S2# show running-config

! Lưu cấu hình vào NVRAM
S2# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

### Kiểm tra nhanh trên S2

```text
S2# show running-config
S2# show startup-config
```

| Hạng mục | Kết quả cần thấy |
| --- | --- |
| Hostname | `hostname S2` |
| Console password | `line con 0`, có `password 7 ...` và `login` |
| Enable password | `enable password 7 ...` |
| Enable secret | `enable secret 5 ...` |
| Banner | `banner motd ...` |
| Password encryption | `service password-encryption` |
| Startup-config | Có đầy đủ cấu hình sau khi lưu |

## 8. Cấu Hình Tổng Hợp

### S1

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname S1
S1(config)# line console 0
S1(config-line)# password letmein
S1(config-line)# login
S1(config-line)# exit
S1(config)# enable password c1$c0
S1(config)# enable secret itsasecret
S1(config)# banner motd "This is a secure system. Authorized Access Only!"
S1(config)# service password-encryption
S1(config)# end
S1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

### S2

```text
Switch> enable
Switch# configure terminal
Switch(config)# hostname S2
S2(config)# line console 0
S2(config-line)# password letmein
S2(config-line)# login
S2(config-line)# exit
S2(config)# enable password c1$c0
S2(config)# enable secret itsasecret
S2(config)# banner motd "This is a secure system. Authorized Access Only!"
S2(config)# service password-encryption
S2(config)# end
S2# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

## 9. Lỗi Gặp Phải Và Cách Sửa

| Lỗi | Nguyên nhân | Cách sửa |
| --- | --- | --- |
| Thoát ra vào lại console nhưng switch không hỏi password | Thiếu lệnh `login` trong `line console 0` | Vào `line console 0`, nhập lại `password letmein` và `login` |
| Không vào được privileged EXEC mode bằng `c1$c0` | Đã cấu hình `enable secret itsasecret`, nên `enable secret` ghi đè `enable password` | Dùng mật khẩu `itsasecret` khi nhập lệnh `enable` |
| `enable password` hoặc console password vẫn hiện plain text | Chưa bật `service password-encryption` | Chạy `service password-encryption` trong global configuration mode |
| Thiết bị mất cấu hình sau khi reload | Chưa lưu running-config vào startup-config | Chạy `copy running-config startup-config` |
| MOTD banner bị lỗi hoặc không nhận đủ nội dung | Dùng sai dấu phân cách hoặc thiếu dấu đóng chuỗi | Dùng dấu nháy kép hoặc delimiter rõ ràng: `banner motd "This is a secure system. Authorized Access Only!"` |
| Packet Tracer không chấm đúng mật khẩu `c1$c0` | Gõ nhầm số `0` thành chữ `O` | Nhập đúng `c1$c0`, ký tự cuối là số không |

## 10. Kết Quả Cuối

| Kiểm tra | Kết quả mong muốn | Trạng thái |
| --- | --- | --- |
| S1 hostname | Prompt hiển thị `S1#` | Hoàn tất |
| S2 hostname | Prompt hiển thị `S2#` | Hoàn tất |
| Console password | Khi truy cập console, switch yêu cầu nhập `letmein` | Hoàn tất |
| Enable password | Có cấu hình `enable password`, sau đó được mã hóa | Hoàn tất |
| Enable secret | Khi vào privileged EXEC mode, dùng `itsasecret` | Hoàn tất |
| Password encryption | Plain text password được mã hóa trong running-config | Hoàn tất |
| MOTD banner | Banner hiển thị khi truy cập CLI | Hoàn tất |
| Save configuration | `show startup-config` hiển thị cấu hình đã lưu | Hoàn tất |

![check result](/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/labs/lab-03/final.png)

---

## Các Lab Khác Trong Dạng Này

<div style="margin: 2rem 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/" style="padding: 0.5rem 1rem; background: #e2e8f0; color: #1e293b; border-radius: 6px; text-decoration: none; display: inline-block;">← Lab 2</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/" style="padding: 0.5rem 1rem; border: 1px solid #cbd5e1; border-radius: 6px; text-decoration: none; display: inline-block;">📋 Xem tất cả</a></div>
    <div><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/" style="padding: 0.5rem 1rem; background: #0f766e; color: white; border-radius: 6px; text-decoration: none; display: inline-block;">Lab 4 →</a></div>
  </div>
  
  <details open>
    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 1rem;">Danh sách 8 lab trong dạng này:</summary>
    <ul style="list-style: none; padding-left: 0;">
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-01/">Lab 1: 1.4.7 Packet Tracer - Configure Router Interfaces</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-02/">Lab 2: 2.3.7 Packet Tracer - Navigate the IOS</a></li>
  <li style="margin: 0.5rem 0;"><strong>→ Lab 3: 2.5.5 Packet Tracer - Configure Initial Switch Settings (Đang đọc)</strong></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-04/">Lab 4: 2.9.1 Packet Tracer - Basic Switch and End Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-05/">Lab 5: 10.1.4 Packet Tracer - Configure Initial Router Settings</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-06/">Lab 6: 10.3.4 Packet Tracer - Connect a Router to a LAN</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-07/">Lab 7: 10.4.3 Packet Tracer - Basic Device Configuration</a></li>
  <li style="margin: 0.5rem 0;"><a href="/writeups/ccna-packet-tracer-writeups/02-ios-va-cau-hinh-co-ban/lab-08/">Lab 8: 14.3.5 Packet Tracer - Basic Router Configuration Review</a></li>
    </ul>
  </details>
</div>

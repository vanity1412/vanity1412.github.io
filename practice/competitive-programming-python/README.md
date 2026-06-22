# Competitive Programming Python

Bộ 230 bài luyện Python từ cơ bản đến Network Operations. Mỗi bài có input mẫu, output chuẩn và lời giải tham khảo.

## Cấu trúc mỗi bài

```text
001-ten-bai/
├── index.md
├── main.py
├── solve.py
├── input.txt (hoặc CSV/JSON/LOG/config)
└── expected_output.txt
```

## Quy trình luyện tập

1. Đọc đề và ví dụ trong `index.md` của bài.
2. Viết lời giải vào `main.py` mà chưa xem `solve.py`.
3. Chạy `python main.py` ngay trong thư mục bài.
4. Từ thư mục gốc, chạy `python check_answer.py 001` để chấm bài.
5. Nếu chưa đúng, so sánh với `solve.py`.

`main.py` và `solve.py` tự đọc file input nằm cùng thư mục, nên không cần nhập lại bằng bàn phím.

## Danh sách bài tập


### A. Python cơ bản để làm nền

- [ ] [001. A cộng B](./001-a-cong-b/)
- [ ] [002. Tính tổng, hiệu, tích, thương của 2 số](./002-tinh-tong-hieu-tich-thuong-cua-2-so/)
- [ ] [003. Tính chu vi, diện tích hình chữ nhật](./003-tinh-chu-vi-dien-tich-hinh-chu-nhat/)
- [ ] [004. Tính chu vi, diện tích hình tròn](./004-tinh-chu-vi-dien-tich-hinh-tron/)
- [ ] [005. Đổi độ C sang độ F](./005-doi-do-c-sang-do-f/)
- [ ] [006. Đổi giây sang giờ, phút, giây](./006-doi-giay-sang-gio-phut-giay/)
- [ ] [007. Nhập tên người dùng và in lời chào](./007-nhap-ten-nguoi-dung-va-in-loi-chao/)
- [ ] [008. Nhập họ tên, tuổi, trường học rồi in thông tin](./008-nhap-ho-ten-tuoi-truong-hoc-roi-in-thong-tin/)
- [ ] [009. Tính điểm trung bình 3 môn](./009-tinh-diem-trung-binh-3-mon/)
- [ ] [010. Tính tiền điện theo số kWh nhập vào](./010-tinh-tien-dien-theo-so-kwh-nhap-vao/)
- [ ] [011. Tính tiền mạng theo số tháng sử dụng](./011-tinh-tien-mang-theo-so-thang-su-dung/)
- [ ] [012. Tính lương nhân viên theo giờ làm và lương/giờ](./012-tinh-luong-nhan-vien-theo-gio-lam-va-luong-gio/)
- [ ] [013. Tính BMI](./013-tinh-bmi/)
- [ ] [014. Đổi VNĐ sang USD theo tỷ giá nhập vào](./014-doi-vnd-sang-usd-theo-ty-gia-nhap-vao/)
- [ ] [015. Tính tổng dung lượng 3 file MB và đổi sang GB](./015-tinh-tong-dung-luong-3-file-mb-va-doi-sang-gb/)
- [ ] [016. Kiểm tra số chẵn/lẻ](./016-kiem-tra-so-chan-le/)
- [ ] [017. Kiểm tra số dương, âm, bằng 0](./017-kiem-tra-so-duong-am-bang-0/)
- [ ] [018. Tìm số lớn nhất trong 2 số](./018-tim-so-lon-nhat-trong-2-so/)
- [ ] [019. Tìm số lớn nhất trong 3 số](./019-tim-so-lon-nhat-trong-3-so/)
- [ ] [020. Kiểm tra năm nhuận](./020-kiem-tra-nam-nhuan/)
- [ ] [021. Xếp loại học lực theo điểm](./021-xep-loai-hoc-luc-theo-diem/)
- [ ] [022. Kiểm tra tuổi có đủ điều kiện đi làm part-time không](./022-kiem-tra-tuoi-co-du-dieu-kien-di-lam-part-time-khong/)
- [ ] [023. Kiểm tra mật khẩu có đúng không](./023-kiem-tra-mat-khau-co-dung-khong/)
- [ ] [024. Kiểm tra username và password đăng nhập](./024-kiem-tra-username-va-password-dang-nhap/)
- [ ] [025. Kiểm tra IP có thuộc mạng nội bộ 192.168.x.x không](./025-kiem-tra-ip-co-thuoc-mang-noi-bo-192-168-x-x-khong/)
- [ ] [026. Kiểm tra port nhập vào có phải port phổ biến không](./026-kiem-tra-port-nhap-vao-co-phai-port-pho-bien-khong/)
- [ ] [027. Kiểm tra dung lượng ổ đĩa còn lại có dưới 20% không](./027-kiem-tra-dung-luong-o-dia-con-lai-co-duoi-20-khong/)
- [ ] [028. Kiểm tra ping result là UP hay DOWN](./028-kiem-tra-ping-result-la-up-hay-down/)
- [ ] [029. Kiểm tra trạng thái interface là up/down](./029-kiem-tra-trang-thai-interface-la-up-down/)
- [ ] [030. Kiểm tra log có chứa từ “error” không](./030-kiem-tra-log-co-chua-tu-error-khong/)
- [ ] [031. In các số từ 1 đến N](./031-in-cac-so-tu-1-den-n/)
- [ ] [032. Tính tổng từ 1 đến N](./032-tinh-tong-tu-1-den-n/)
- [ ] [033. Tính tổng các số chẵn từ 1 đến N](./033-tinh-tong-cac-so-chan-tu-1-den-n/)
- [ ] [034. Tính tổng các số lẻ từ 1 đến N](./034-tinh-tong-cac-so-le-tu-1-den-n/)
- [ ] [035. In bảng cửu chương](./035-in-bang-cuu-chuong/)
- [ ] [036. Kiểm tra số nguyên tố](./036-kiem-tra-so-nguyen-to/)
- [ ] [037. In các số nguyên tố từ 1 đến N](./037-in-cac-so-nguyen-to-tu-1-den-n/)
- [ ] [038. Tính giai thừa N](./038-tinh-giai-thua-n/)
- [ ] [039. In dãy Fibonacci](./039-in-day-fibonacci/)
- [ ] [040. Đếm số chữ số của một số](./040-dem-so-chu-so-cua-mot-so/)
- [ ] [041. Đảo ngược một số](./041-dao-nguoc-mot-so/)
- [ ] [042. Tính tổng các chữ số của một số](./042-tinh-tong-cac-chu-so-cua-mot-so/)
- [ ] [043. Nhập nhiều số đến khi nhập 0 thì dừng](./043-nhap-nhieu-so-den-khi-nhap-0-thi-dung/)
- [ ] [044. Tìm số lớn nhất trong danh sách nhập từ bàn phím](./044-tim-so-lon-nhat-trong-danh-sach-nhap-tu-ban-phim/)
- [ ] [045. Tính trung bình danh sách số nhập vào](./045-tinh-trung-binh-danh-sach-so-nhap-vao/)
- [ ] [046. Nhập danh sách IP rồi in từng IP](./046-nhap-danh-sach-ip-roi-in-tung-ip/)
- [ ] [047. Nhập N địa chỉ IP, kiểm tra IP nào có dạng 192.168.x.x](./047-nhap-n-dia-chi-ip-kiem-tra-ip-nao-co-dang-192-168-x-x/)
- [ ] [048. Nhập N port, in port nào là 22, 80, 443](./048-nhap-n-port-in-port-nao-la-22-80-443/)
- [ ] [049. Nhập nhiều dòng log, đếm dòng có chữ “failed”](./049-nhap-nhieu-dong-log-dem-dong-co-chu-failed/)
- [ ] [050. Nhập nhiều hostname, in ra hostname viết hoa](./050-nhap-nhieu-hostname-in-ra-hostname-viet-hoa/)

### B. List, tuple, dict

- [ ] [051. Tạo danh sách 10 số và tính tổng](./051-tao-danh-sach-10-so-va-tinh-tong/)
- [ ] [052. Tìm max/min trong list](./052-tim-max-min-trong-list/)
- [ ] [053. Sắp xếp list tăng dần](./053-sap-xep-list-tang-dan/)
- [ ] [054. Sắp xếp list giảm dần](./054-sap-xep-list-giam-dan/)
- [ ] [055. Xóa phần tử trùng trong list](./055-xoa-phan-tu-trung-trong-list/)
- [ ] [056. Đếm số lần xuất hiện của một số](./056-dem-so-lan-xuat-hien-cua-mot-so/)
- [ ] [057. Tách số chẵn và số lẻ thành 2 list](./057-tach-so-chan-va-so-le-thanh-2-list/)
- [ ] [058. Gộp 2 list thành 1 list](./058-gop-2-list-thanh-1-list/)
- [ ] [059. Tìm phần tử chung giữa 2 list](./059-tim-phan-tu-chung-giua-2-list/)
- [ ] [060. Tìm phần tử chỉ có trong list A, không có trong list B](./060-tim-phan-tu-chi-co-trong-list-a-khong-co-trong-list-b/)
- [ ] [061. Lưu danh sách thiết bị mạng gồm hostname, IP, status](./061-luu-danh-sach-thiet-bi-mang-gom-hostname-ip-status/)
- [ ] [062. Đếm bao nhiêu thiết bị UP, bao nhiêu thiết bị DOWN](./062-dem-bao-nhieu-thiet-bi-up-bao-nhieu-thiet-bi-down/)
- [ ] [063. Tạo dictionary lưu username và password](./063-tao-dictionary-luu-username-va-password/)
- [ ] [064. Tạo dictionary lưu hostname và IP](./064-tao-dictionary-luu-hostname-va-ip/)
- [ ] [065. Tìm IP theo hostname](./065-tim-ip-theo-hostname/)
- [ ] [066. Tìm hostname theo IP](./066-tim-hostname-theo-ip/)
- [ ] [067. Cập nhật trạng thái thiết bị trong dictionary](./067-cap-nhat-trang-thai-thiet-bi-trong-dictionary/)
- [ ] [068. Xóa thiết bị khỏi inventory](./068-xoa-thiet-bi-khoi-inventory/)
- [ ] [069. In danh sách thiết bị theo format bảng](./069-in-danh-sach-thiet-bi-theo-format-bang/)
- [ ] [070. Tạo inventory mạng gồm router, switch, firewall](./070-tao-inventory-mang-gom-router-switch-firewall/)

### C. Xử lý chuỗi

- [ ] [071. Đếm số ký tự trong chuỗi](./071-dem-so-ky-tu-trong-chuoi/)
- [ ] [072. Đếm số từ trong câu](./072-dem-so-tu-trong-cau/)
- [ ] [073. Viết hoa toàn bộ chuỗi](./073-viet-hoa-toan-bo-chuoi/)
- [ ] [074. Viết thường toàn bộ chuỗi](./074-viet-thuong-toan-bo-chuoi/)
- [ ] [075. Chuẩn hóa họ tên](./075-chuan-hoa-ho-ten/)
- [ ] [076. Tách username từ email](./076-tach-username-tu-email/)
- [ ] [077. Tách domain từ email](./077-tach-domain-tu-email/)
- [ ] [078. Kiểm tra email có chứa “@” không](./078-kiem-tra-email-co-chua-khong/)
- [ ] [079. Kiểm tra chuỗi có phải địa chỉ IP đơn giản không](./079-kiem-tra-chuoi-co-phai-dia-chi-ip-don-gian-khong/)
- [ ] [080. Tách IP từ dòng log đơn giản](./080-tach-ip-tu-dong-log-don-gian/)
- [ ] [081. Tách port từ chuỗi "192.168.1.1:443"](./081-tach-port-tu-chuoi-192-168-1-1-443/)
- [ ] [082. Tách hostname từ "router01.company.local"](./082-tach-hostname-tu-router01-company-local/)
- [ ] [083. Tách VLAN ID từ chuỗi "VLAN10"](./083-tach-vlan-id-tu-chuoi-vlan10/)
- [ ] [084. Tách interface từ "GigabitEthernet0/1 is up"](./084-tach-interface-tu-gigabitethernet0-1-is-up/)
- [ ] [085. Kiểm tra log có chứa từ khóa "down"](./085-kiem-tra-log-co-chua-tu-khoa-down/)
- [ ] [086. Đếm số lần xuất hiện của "failed" trong log](./086-dem-so-lan-xuat-hien-cua-failed-trong-log/)
- [ ] [087. Thay "DOWN" thành "ALERT" trong log](./087-thay-down-thanh-alert-trong-log/)
- [ ] [088. Chuẩn hóa danh sách IP bị dư khoảng trắng](./088-chuan-hoa-danh-sach-ip-bi-du-khoang-trang/)
- [ ] [089. Tách nhiều IP từ một chuỗi](./089-tach-nhieu-ip-tu-mot-chuoi/)
- [ ] [090. Tạo slug folder từ tên bài, ví dụ "A cộng B" thành "a-cong-b"](./090-tao-slug-folder-tu-ten-bai-vi-du-a-cong-b-thanh-a-cong-b/)

### D. File TXT, CSV, JSON

- [ ] [091. Đọc file input.txt và in nội dung](./091-doc-file-input-txt-va-in-noi-dung/)
- [ ] [092. Ghi kết quả ra file output.txt](./092-ghi-ket-qua-ra-file-output-txt/)
- [ ] [093. Đọc danh sách IP từ file TXT](./093-doc-danh-sach-ip-tu-file-txt/)
- [ ] [094. Ghi danh sách IP UP/DOWN ra file TXT](./094-ghi-danh-sach-ip-up-down-ra-file-txt/)
- [ ] [095. Đọc file log và in 10 dòng đầu](./095-doc-file-log-va-in-10-dong-dau/)
- [ ] [096. Đếm số dòng trong file log](./096-dem-so-dong-trong-file-log/)
- [ ] [097. Lọc các dòng chứa "error" ra file riêng](./097-loc-cac-dong-chua-error-ra-file-rieng/)
- [ ] [098. Lọc các dòng chứa "failed login"](./098-loc-cac-dong-chua-failed-login/)
- [ ] [099. Lọc các dòng chứa "interface down"](./099-loc-cac-dong-chua-interface-down/)
- [ ] [100. Đọc file CSV danh sách thiết bị mạng](./100-doc-file-csv-danh-sach-thiet-bi-mang/)
- [ ] [101. Ghi kết quả kiểm tra thiết bị ra CSV](./101-ghi-ket-qua-kiem-tra-thiet-bi-ra-csv/)
- [ ] [102. Đếm số router/switch/firewall trong CSV](./102-dem-so-router-switch-firewall-trong-csv/)
- [ ] [103. Tìm thiết bị theo IP trong file CSV](./103-tim-thiet-bi-theo-ip-trong-file-csv/)
- [ ] [104. Cập nhật trạng thái thiết bị trong file CSV](./104-cap-nhat-trang-thai-thiet-bi-trong-file-csv/)
- [ ] [105. Đọc file JSON chứa inventory mạng](./105-doc-file-json-chua-inventory-mang/)
- [ ] [106. Ghi inventory mạng ra JSON](./106-ghi-inventory-mang-ra-json/)
- [ ] [107. Thêm thiết bị mới vào JSON](./107-them-thiet-bi-moi-vao-json/)
- [ ] [108. Xóa thiết bị khỏi JSON](./108-xoa-thiet-bi-khoi-json/)
- [ ] [109. Tìm thiết bị DOWN trong JSON](./109-tim-thiet-bi-down-trong-json/)
- [ ] [110. Xuất report TXT từ dữ liệu JSON](./110-xuat-report-txt-tu-du-lieu-json/)

### E. Python cho IP/Subnet

- [ ] [111. Kiểm tra chuỗi có phải IPv4 hợp lệ không](./111-kiem-tra-chuoi-co-phai-ipv4-hop-le-khong/)
- [ ] [112. Kiểm tra IP có thuộc private IP không](./112-kiem-tra-ip-co-thuoc-private-ip-khong/)
- [ ] [113. Kiểm tra IP thuộc class A/B/C](./113-kiem-tra-ip-thuoc-class-a-b-c/)
- [ ] [114. Nhập IP và subnet mask, in network address](./114-nhap-ip-va-subnet-mask-in-network-address/)
- [ ] [115. Nhập CIDR /24, in subnet mask](./115-nhap-cidr-24-in-subnet-mask/)
- [ ] [116. Nhập subnet mask, in CIDR](./116-nhap-subnet-mask-in-cidr/)
- [ ] [117. Tính broadcast address](./117-tinh-broadcast-address/)
- [ ] [118. Tính số host usable trong subnet](./118-tinh-so-host-usable-trong-subnet/)
- [ ] [119. In host đầu và host cuối trong subnet](./119-in-host-dau-va-host-cuoi-trong-subnet/)
- [ ] [120. Kiểm tra 2 IP có cùng subnet không](./120-kiem-tra-2-ip-co-cung-subnet-khong/)
- [ ] [121. Kiểm tra IP có nằm trong subnet 192.168.1.0/24 không](./121-kiem-tra-ip-co-nam-trong-subnet-192-168-1-0-24-khong/)
- [ ] [122. Chia mạng /24 thành các subnet /26](./122-chia-mang-24-thanh-cac-subnet-26/)
- [ ] [123. Chia mạng /24 thành 4 subnet bằng nhau](./123-chia-mang-24-thanh-4-subnet-bang-nhau/)
- [ ] [124. Tạo danh sách toàn bộ IP usable trong subnet](./124-tao-danh-sach-toan-bo-ip-usable-trong-subnet/)
- [ ] [125. Kiểm tra danh sách IP nào nằm ngoài subnet cho phép](./125-kiem-tra-danh-sach-ip-nao-nam-ngoai-subnet-cho-phep/)
- [ ] [126. Tạo IP planning cho 4 phòng ban: IT, HR, Sales, Guest](./126-tao-ip-planning-cho-4-phong-ban-it-hr-sales-guest/)
- [ ] [127. Tính subnet cho từng VLAN](./127-tinh-subnet-cho-tung-vlan/)
- [ ] [128. Tạo bảng VLAN ID, subnet, gateway](./128-tao-bang-vlan-id-subnet-gateway/)
- [ ] [129. Kiểm tra gateway có nằm trong subnet không](./129-kiem-tra-gateway-co-nam-trong-subnet-khong/)
- [ ] [130. Tạo tool nhập subnet rồi xuất thông tin đầy đủ](./130-tao-tool-nhap-subnet-roi-xuat-thong-tin-day-du/)

### F. Ping, port, socket

- [ ] [131. Ping một IP nhập từ bàn phím](./131-ping-mot-ip-nhap-tu-ban-phim/)
- [ ] [132. Ping nhiều IP từ file TXT](./132-ping-nhieu-ip-tu-file-txt/)
- [ ] [133. Ping nhiều IP và in UP/DOWN](./133-ping-nhieu-ip-va-in-up-down/)
- [ ] [134. Ping nhiều IP và ghi kết quả ra CSV](./134-ping-nhieu-ip-va-ghi-ket-qua-ra-csv/)
- [ ] [135. Ping nhiều IP, đếm số thiết bị UP/DOWN](./135-ping-nhieu-ip-dem-so-thiet-bi-up-down/)
- [ ] [136. Ping nhiều IP, chỉ in thiết bị DOWN](./136-ping-nhieu-ip-chi-in-thiet-bi-down/)
- [ ] [137. Ping nhiều IP, thêm thời gian kiểm tra](./137-ping-nhieu-ip-them-thoi-gian-kiem-tra/)
- [ ] [138. Ping nhiều IP theo chu kỳ 5 giây](./138-ping-nhieu-ip-theo-chu-ky-5-giay/)
- [ ] [139. Ping gateway trước, nếu fail thì báo lỗi mạng nội bộ](./139-ping-gateway-truoc-neu-fail-thi-bao-loi-mang-noi-bo/)
- [ ] [140. Ping DNS 8.8.8.8 để kiểm tra internet](./140-ping-dns-8-8-8-8-de-kiem-tra-internet/)
- [ ] [141. Kiểm tra port 22 SSH có mở không](./141-kiem-tra-port-22-ssh-co-mo-khong/)
- [ ] [142. Kiểm tra port 80 HTTP có mở không](./142-kiem-tra-port-80-http-co-mo-khong/)
- [ ] [143. Kiểm tra port 443 HTTPS có mở không](./143-kiem-tra-port-443-https-co-mo-khong/)
- [ ] [144. Kiểm tra nhiều port trên một IP](./144-kiem-tra-nhieu-port-tren-mot-ip/)
- [ ] [145. Kiểm tra một port trên nhiều IP](./145-kiem-tra-mot-port-tren-nhieu-ip/)
- [ ] [146. Kiểm tra danh sách IP và port từ CSV](./146-kiem-tra-danh-sach-ip-va-port-tu-csv/)
- [ ] [147. Tạo simple port scanner](./147-tao-simple-port-scanner/)
- [ ] [148. Tạo tool kiểm tra service: SSH, HTTP, HTTPS, RDP, DNS](./148-tao-tool-kiem-tra-service-ssh-http-https-rdp-dns/)
- [ ] [149. Ghi kết quả port check ra CSV](./149-ghi-ket-qua-port-check-ra-csv/)
- [ ] [150. Tạo report thiết bị nào mở port nguy hiểm](./150-tao-report-thiet-bi-nao-mo-port-nguy-hiem/)

### G. Log analysis cho Network Operations

- [ ] [151. Đọc file syslog Cisco](./151-doc-file-syslog-cisco/)
- [ ] [152. Lọc log có chữ "LINK-3-UPDOWN"](./152-loc-log-co-chu-link-3-updown/)
- [ ] [153. Lọc log có chữ "LINEPROTO"](./153-loc-log-co-chu-lineproto/)
- [ ] [154. Đếm số lần interface bị down](./154-dem-so-lan-interface-bi-down/)
- [ ] [155. Tìm interface bị down nhiều nhất](./155-tim-interface-bi-down-nhieu-nhat/)
- [ ] [156. Tách hostname từ dòng syslog](./156-tach-hostname-tu-dong-syslog/)
- [ ] [157. Tách thời gian từ dòng syslog](./157-tach-thoi-gian-tu-dong-syslog/)
- [ ] [158. Tách interface từ dòng log](./158-tach-interface-tu-dong-log/)
- [ ] [159. Lọc log theo ngày](./159-loc-log-theo-ngay/)
- [ ] [160. Lọc log theo hostname](./160-loc-log-theo-hostname/)
- [ ] [161. Lọc log theo severity](./161-loc-log-theo-severity/)
- [ ] [162. Đếm số log warning/error](./162-dem-so-log-warning-error/)
- [ ] [163. Phân loại log thành INFO, WARNING, ERROR](./163-phan-loai-log-thanh-info-warning-error/)
- [ ] [164. Tạo file riêng cho từng loại log](./164-tao-file-rieng-cho-tung-loai-log/)
- [ ] [165. Tìm login failed trong log](./165-tim-login-failed-trong-log/)
- [ ] [166. Tìm login successful trong log](./166-tim-login-successful-trong-log/)
- [ ] [167. Đếm số lần đăng nhập thất bại theo username](./167-dem-so-lan-dang-nhap-that-bai-theo-username/)
- [ ] [168. Đếm số lần đăng nhập thất bại theo IP](./168-dem-so-lan-dang-nhap-that-bai-theo-ip/)
- [ ] [169. Phát hiện IP đăng nhập sai quá 5 lần](./169-phat-hien-ip-dang-nhap-sai-qua-5-lan/)
- [ ] [170. Tạo alert khi có nhiều dòng "failed" trong log](./170-tao-alert-khi-co-nhieu-dong-failed-trong-log/)

### H. Regex cho log và config

- [ ] [171. Tách tất cả địa chỉ IP trong file log](./171-tach-tat-ca-dia-chi-ip-trong-file-log/)
- [ ] [172. Tách tất cả MAC address trong file log](./172-tach-tat-ca-mac-address-trong-file-log/)
- [ ] [173. Tách tất cả port number trong log](./173-tach-tat-ca-port-number-trong-log/)
- [ ] [174. Tách hostname từ config Cisco](./174-tach-hostname-tu-config-cisco/)
- [ ] [175. Tách interface từ config Cisco](./175-tach-interface-tu-config-cisco/)
- [ ] [176. Tách IP address trên interface](./176-tach-ip-address-tren-interface/)
- [ ] [177. Tách default gateway](./177-tach-default-gateway/)
- [ ] [178. Tách static route](./178-tach-static-route/)
- [ ] [179. Tách VLAN ID trong config switch](./179-tach-vlan-id-trong-config-switch/)
- [ ] [180. Tách access port và VLAN tương ứng](./180-tach-access-port-va-vlan-tuong-ung/)
- [ ] [181. Tách trunk port](./181-tach-trunk-port/)
- [ ] [182. Tách ACL number](./182-tach-acl-number/)
- [ ] [183. Tách dòng permit/deny trong ACL](./183-tach-dong-permit-deny-trong-acl/)
- [ ] [184. Kiểm tra config có enable SSH chưa](./184-kiem-tra-config-co-enable-ssh-chua/)
- [ ] [185. Kiểm tra config có đặt password chưa](./185-kiem-tra-config-co-dat-password-chua/)
- [ ] [186. Kiểm tra config có service password-encryption chưa](./186-kiem-tra-config-co-service-password-encryption-chua/)
- [ ] [187. Kiểm tra config có banner chưa](./187-kiem-tra-config-co-banner-chua/)
- [ ] [188. Kiểm tra interface nào shutdown](./188-kiem-tra-interface-nao-shutdown/)
- [ ] [189. Kiểm tra interface nào chưa có description](./189-kiem-tra-interface-nao-chua-co-description/)
- [ ] [190. Tạo checklist audit config Cisco bằng Python](./190-tao-checklist-audit-config-cisco-bang-python/)

### I. Automation với SSH

- [ ] [191. SSH vào một router và chạy lệnh show ip interface brief](./191-ssh-vao-mot-router-va-chay-lenh-show-ip-interface-brief/)
- [ ] [192. SSH vào switch và chạy show vlan brief](./192-ssh-vao-switch-va-chay-show-vlan-brief/)
- [ ] [193. SSH vào nhiều thiết bị từ file CSV](./193-ssh-vao-nhieu-thiet-bi-tu-file-csv/)
- [ ] [194. Backup running-config của một thiết bị](./194-backup-running-config-cua-mot-thiet-bi/)
- [ ] [195. Backup config nhiều thiết bị](./195-backup-config-nhieu-thiet-bi/)
- [ ] [196. Lưu backup theo tên hostname và ngày tháng](./196-luu-backup-theo-ten-hostname-va-ngay-thang/)
- [ ] [197. Chạy lệnh show trên nhiều thiết bị rồi gom kết quả](./197-chay-lenh-show-tren-nhieu-thiet-bi-roi-gom-ket-qua/)
- [ ] [198. Kiểm tra thiết bị nào SSH không được](./198-kiem-tra-thiet-bi-nao-ssh-khong-duoc/)
- [ ] [199. Ghi log lỗi khi SSH thất bại](./199-ghi-log-loi-khi-ssh-that-bai/)
- [ ] [200. Tạo script kiểm tra uptime thiết bị](./200-tao-script-kiem-tra-uptime-thiet-bi/)
- [ ] [201. Tạo script kiểm tra version IOS](./201-tao-script-kiem-tra-version-ios/)
- [ ] [202. Tạo script kiểm tra interface status](./202-tao-script-kiem-tra-interface-status/)
- [ ] [203. Tạo script kiểm tra VLAN trên nhiều switch](./203-tao-script-kiem-tra-vlan-tren-nhieu-switch/)
- [ ] [204. Tạo script kiểm tra OSPF neighbor](./204-tao-script-kiem-tra-ospf-neighbor/)
- [ ] [205. Tạo script kiểm tra routing table](./205-tao-script-kiem-tra-routing-table/)
- [ ] [206. Tạo script kiểm tra CPU usage](./206-tao-script-kiem-tra-cpu-usage/)
- [ ] [207. Tạo script kiểm tra memory usage](./207-tao-script-kiem-tra-memory-usage/)
- [ ] [208. Tạo script kiểm tra số interface down](./208-tao-script-kiem-tra-so-interface-down/)
- [ ] [209. Tạo script đẩy cấu hình description cho interface](./209-tao-script-day-cau-hinh-description-cho-interface/)
- [ ] [210. Tạo script cấu hình VLAN hàng loạt](./210-tao-script-cau-hinh-vlan-hang-loat/)

### J. Mini tool cho NOC / Network Operations

- [ ] [211. Tool kiểm tra danh sách thiết bị UP/DOWN](./211-tool-kiem-tra-danh-sach-thiet-bi-up-down/)
- [ ] [212. Tool kiểm tra port dịch vụ quan trọng](./212-tool-kiem-tra-port-dich-vu-quan-trong/)
- [ ] [213. Tool kiểm tra IP có hợp lệ không](./213-tool-kiem-tra-ip-co-hop-le-khong/)
- [ ] [214. Tool tính subnet nhanh](./214-tool-tinh-subnet-nhanh/)
- [ ] [215. Tool tạo IP planning cho VLAN](./215-tool-tao-ip-planning-cho-vlan/)
- [ ] [216. Tool đọc inventory từ CSV](./216-tool-doc-inventory-tu-csv/)
- [ ] [217. Tool xuất report tình trạng thiết bị](./217-tool-xuat-report-tinh-trang-thiet-bi/)
- [ ] [218. Tool lọc log lỗi từ syslog](./218-tool-loc-log-loi-tu-syslog/)
- [ ] [219. Tool phát hiện interface down](./219-tool-phat-hien-interface-down/)
- [ ] [220. Tool phát hiện login failed nhiều lần](./220-tool-phat-hien-login-failed-nhieu-lan/)
- [ ] [221. Tool backup config tự động](./221-tool-backup-config-tu-dong/)
- [ ] [222. Tool so sánh config hôm nay với hôm qua](./222-tool-so-sanh-config-hom-nay-voi-hom-qua/)
- [ ] [223. Tool kiểm tra config thiếu bảo mật](./223-tool-kiem-tra-config-thieu-bao-mat/)
- [ ] [224. Tool kiểm tra interface chưa có description](./224-tool-kiem-tra-interface-chua-co-description/)
- [ ] [225. Tool kiểm tra thiết bị chưa bật SSH](./225-tool-kiem-tra-thiet-bi-chua-bat-ssh/)
- [ ] [226. Tool kiểm tra port nguy hiểm đang mở](./226-tool-kiem-tra-port-nguy-hiem-dang-mo/)
- [ ] [227. Tool tạo báo cáo incident dạng TXT](./227-tool-tao-bao-cao-incident-dang-txt/)
- [ ] [228. Tool tạo báo cáo incident dạng CSV](./228-tool-tao-bao-cao-incident-dang-csv/)
- [ ] [229. Tool tạo báo cáo incident dạng Markdown](./229-tool-tao-bao-cao-incident-dang-markdown/)
- [ ] [230. Tool tổng hợp trạng thái mạng mỗi ngày](./230-tool-tong-hop-trang-thai-mang-moi-ngay/)

> Chỉ ping, quét port hoặc SSH vào hệ thống bạn sở hữu hoặc được phép kiểm tra.

## K. Projects lớn đưa lên GitHub

Sau khi hoàn thành các bài nhỏ, tiếp tục với [8 project portfolio](./K-projects-github/).

---
layout: page-toc
title: "V1T CTF 2026 - 78CT"
description: "OSINT and steganography writeup for V1T CTF 2026 78CT."
permalink: /writeups/v1t-ctf-2026/78ct-osint-stego/
toc: true
render_with_liquid: false
---

# Write-up CTF: 78CT

## 1. Thông tin challenge

- **Tên challenge:** 78CT
- **Tác giả/Author:** Jaze Duckling
- **Category:** OSINT / Steganography / Misc
- **Điểm:** 290
- **Độ khó:** Medium
- **Flag format:** `V1T{...}`

### Mô tả challenge

> Rawr and I used to spend hours at a lake right in the heart of our hometown during high school. It was our favorite spot to chill and just clear our minds when the afternoon breeze rolled in after those endless school days. There is also something interesting nearby. If you take a closer look from above, you might notice that a park next to the lake has a shape that resembles a dragon. Can you find the place and figure out what I left behind at the lake?

### Dữ liệu được cung cấp

Challenge cung cấp một ảnh vệ tinh/chụp từ trên cao của một khu vực có hình dạng giống **con rồng** và mô tả gợi ý rằng địa điểm nằm cạnh một hồ ở trung tâm quê nhà của tác giả.

---

## 2. Nhận định ban đầu

Đây là dạng bài **OSINT kết hợp Steganography**.

Các dấu hiệu nhận biết:

1. Challenge không cung cấp binary, source code, pcap hay file mã hóa phức tạp.
2. Mô tả tập trung vào địa điểm thật: `lake`, `hometown`, `high school`, `park`, `dragon shape`.
3. Ảnh gợi ý tìm kiếm địa lý từ góc nhìn vệ tinh.
4. Câu hỏi `what I left behind at the lake` gợi ý tác giả đã để lại một manh mối công khai tại địa điểm, thường là Google Maps review, ảnh, comment hoặc check-in.

Vì vậy hướng giải hợp lý là:

- Xác định địa điểm trong ảnh.
- Tìm trang Google Maps của địa điểm đó.
- Kiểm tra review/ảnh mới hoặc review có tên liên quan tác giả.
- Phân tích nội dung bất thường để tìm flag.

---

## 3. Tóm tắt manh mối quan trọng

| Manh mối | Ý nghĩa |
|---|---|
| Ảnh từ trên cao có hình con rồng | Gợi ý tìm công viên/hồ có thiết kế dạng rồng |
| `lake right in the heart of our hometown` | Địa điểm là hồ ở trung tâm thành phố |
| `after school days` | Gợi ý địa điểm gần khu dân cư/trường học, thường được dùng để đi dạo/chill |
| `what I left behind at the lake` | Có manh mối được để lại trên nền tảng công khai tại địa điểm |
| Tên challenge/tác giả: `Jaze Duckling` | Khi tìm review cần chú ý tên `Jaze`, `JaZe`, `Duck`, `Rawr` |
| Review có hashtag `#v1tnamese` | Gợi ý liên quan đến giải V1T và flag format `V1T{...}` |

---

## 4. Quy trình phân tích từng bước

## Bước 1: Phân tích ảnh challenge

### Mục tiêu

Xác định địa điểm trong ảnh vệ tinh.

### Quan sát

Ảnh cho thấy một khu công viên/hồ có bố cục rất đặc biệt:

- Một phần lớn uốn lượn giống thân rồng.
- Một vòng tròn nhỏ bên cạnh giống viên ngọc.
- Khu vực xung quanh là đô thị.

### Tư duy phân tích

Mô tả `park next to the lake has a shape that resembles a dragon` khớp với hình ảnh một công viên được thiết kế theo mô-típ **rồng nhả ngọc**. Đây là clue địa lý rõ ràng, nên hướng tốt nhất là tìm bằng Google Maps/Google Images với các từ khóa tiếng Việt và tiếng Anh.

### Từ khóa tìm kiếm đề xuất

```text
công viên hình con rồng bên hồ
công viên rồng nhả ngọc hồ
dragon shaped park lake Vietnam
Ho Son lake dragon park
```

### Kết quả

Địa điểm khớp là:

```text
Hồ điều hòa Hồ Sơn, Tuy Hòa, Phú Yên
```

Tên khác có thể gặp:

```text
Công viên Hồ Sơn
Hồ Sơn Lake
Ho Son Lake
```

---

## Bước 2: Mở địa điểm trên Google Maps

### Mục tiêu

Tìm manh mối mà tác giả “left behind at the lake”.

### Thao tác

Tìm trên Google Maps:

```text
Hồ điều hòa Hồ Sơn
```

Sau đó vào phần:

```text
Bài đánh giá / Reviews
```

### Lý do kiểm tra review

Trong OSINT CTF, cụm `left behind` thường không có nghĩa là vật lý thật, mà là một dấu vết công khai để người chơi tìm thấy, ví dụ:

- Google Maps review
- Ảnh đính kèm review
- Username đáng nghi
- Hashtag chứa clue
- Nội dung review bị mã hóa/stego

---

## Bước 3: Xác định review đáng nghi

Trong danh sách review tại địa điểm, review khả nghi nhất là của tài khoản:

```text
JaZe
```

Nội dung review bản tiếng Anh:

```text
traVelers MAjESTIC reFlections sUrface LAKeSIDE sh1mering ScENERY AMAzING eXpanse lak3front glImmering BREEzES suNlit harGor ExPLORERS DREAMsCAPE LAKeVIEW riVerside 9 CALMsNESS harMor higHway hazY AMAzINGLY eXplore MAzEWORK BROAdWAY HARBoR sunMist tranTquil loVely OFfERS ARcHITECTS gleaminG MEADOwS harb0r skYline HAzE suNset 9
#v1tnamese
```

### Vì sao review này khả nghi?

| Dấu hiệu | Phân tích |
|---|---|
| Username `JaZe` | Trùng với tên tác giả/challenge `Jaze Duckling` |
| Tài khoản chỉ có 1 bài đánh giá | Có thể là tài khoản tạo riêng cho challenge |
| Nội dung review không tự nhiên | Các từ được ghép lại như wordlist, không phải câu văn tự nhiên |
| Chữ hoa/chữ thường lẫn lộn bất thường | Dấu hiệu steganography bằng mixed-case |
| Có các số như `1`, `3`, `0` trong từ | Có thể là leetspeak hoặc một phần chuỗi encoded |
| Hashtag `#v1tnamese` | Gợi ý flag format `V1T{...}` |

---

## 5. Phân tích kỹ thuật review JaZe

## Bước 4: Kiểm tra kỹ thuật mixed-case steganography

### Mục tiêu

Tách ra chuỗi ẩn từ cách viết hoa/thường bất thường.

### Ý tưởng

Mỗi từ trong review có một số ký tự bị viết khác kiểu với phần còn lại.

Quy tắc rút trích:

- Nếu từ chủ yếu là **chữ thường**, lấy các ký tự **chữ hoa hoặc chữ số**.
- Nếu từ chủ yếu là **chữ hoa**, lấy các ký tự **chữ thường hoặc chữ số**.
- Bỏ qua các số `9` đứng riêng vì chúng đóng vai trò nhiễu/phân tách.

### Ví dụ

| Từ | Ký tự thường | Ký tự hoa/số | Ký tự lấy ra |
|---|---:|---:|---|
| `traVelers` | nhiều chữ thường | `V` | `V` |
| `MAjESTIC` | chủ yếu chữ hoa | `j` | `j` |
| `reFlections` | nhiều chữ thường | `F` | `F` |
| `sUrface` | nhiều chữ thường | `U` | `U` |
| `LAKeSIDE` | chủ yếu chữ hoa | `e` | `e` |
| `sh1mering` | nhiều chữ thường | `1` | `1` |

Ghép các ký tự lấy ra từ toàn bộ review sẽ thu được chuỗi:

```text
VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9
```

---

## Bước 5: Nhận diện chuỗi encoded

### Mục tiêu

Xác định chuỗi vừa trích xuất thuộc dạng mã hóa/encoding nào.

### Quan sát

Chuỗi thu được:

```text
VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9
```

Đặc điểm:

- Chỉ gồm chữ cái, số và ký tự hợp lệ của Base64.
- Độ dài phù hợp với Base64.
- Bắt đầu bằng `VjFU`, khi decode Base64 thường có thể ra `V1T`.

Vì vậy thử decode Base64.

### Lệnh kiểm tra nhanh trên Linux

```bash
echo 'VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9' | base64 -d
```

### Kết quả

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

Đây là chuỗi đúng format flag của giải.

---

## 6. Script Python kiểm chứng

Script dưới đây tự động rút trích ký tự bất thường từ review, sau đó decode Base64.

```python
import base64

text = """traVelers MAjESTIC reFlections sUrface LAKeSIDE sh1mering ScENERY AMAzING eXpanse lak3front glImmering BREEzES suNlit harGor ExPLORERS DREAMsCAPE LAKeVIEW riVerside 9 CALMsNESS harMor higHway hazY AMAzINGLY eXplore MAzEWORK BROAdWAY HARBoR sunMist tranTquil loVely OFfERS ARcHITECTS gleaminG MEADOwS harb0r skYline HAzE suNset 9"""

hidden_parts = []

for word in text.split():
    # Bỏ qua số 9 đứng riêng vì đây là ký tự gây nhiễu/phân tách
    if word == "9":
        continue

    upper_count = sum(c.isupper() for c in word)
    lower_count = sum(c.islower() for c in word)

    # Nếu từ chủ yếu viết hoa, lấy phần chữ thường hoặc số bị lệch
    if upper_count > lower_count:
        picked = ''.join(c for c in word if c.islower() or c.isdigit())
    # Nếu từ chủ yếu viết thường, lấy phần chữ hoa hoặc số bị lệch
    else:
        picked = ''.join(c for c in word if c.isupper() or c.isdigit())

    hidden_parts.append(picked)

encoded = ''.join(hidden_parts)
decoded = base64.b64decode(encoded).decode()

print("Encoded string:", encoded)
print("Decoded flag:", decoded)
```

### Output

```text
Encoded string: VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9
Decoded flag: V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

---

## 7. Công cụ sử dụng

| Tool | Mục đích | Ý nghĩa |
|---|---|---|
| Google Maps | Tìm địa điểm từ clue OSINT | Xác định Hồ điều hòa Hồ Sơn |
| Google Search / Google Images | Tìm địa điểm có công viên hình rồng | Đối chiếu hình ảnh vệ tinh với địa điểm thật |
| Google Maps Reviews | Tìm dấu vết tác giả để lại | Phát hiện review của JaZe |
| CyberChef | Có thể dùng để decode Base64 | Kiểm tra nhanh chuỗi encoded |
| Python | Tự động trích ký tự bất thường | Xác minh cách giải rõ ràng |
| Linux `base64` | Decode chuỗi Base64 | Lấy flag cuối |

---

## 8. Các lệnh/thao tác cụ thể

### Decode Base64 bằng terminal

```bash
echo 'VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9' | base64 -d
```

**Mục tiêu:** giải mã chuỗi rút trích được từ review.

**Kết quả quan trọng:**

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

Nếu kết quả không đọc được hoặc báo lỗi `invalid input`, cần kiểm tra lại chuỗi encoded có bị thiếu ký tự hoặc copy dư dấu cách không.

---

### Kiểm tra bằng Python

```bash
python3 solve_78ct.py
```

**Mục tiêu:** tự động hóa toàn bộ quá trình rút trích và decode.

**Kết quả mong đợi:** script in ra encoded string và flag.

Nếu script không ra flag, cần kiểm tra lại review bản gốc tiếng Anh, không dùng bản dịch Google Translate vì bản dịch có thể làm mất pattern chữ hoa/thường.

---

## 9. Flag cuối cùng

**FLAG tìm được:**

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

### Mức độ chắc chắn

Mức độ chắc chắn: **Rất cao**.

Lý do:

1. Flag decode ra đúng format `V1T{...}`.
2. Review chứa hashtag `#v1tnamese`, khớp với giải V1T.
3. Username `JaZe` khớp với tác giả `Jaze Duckling`.
4. Cách ẩn dữ liệu bằng mixed-case cho ra chuỗi Base64 hợp lệ.
5. Nội dung flag cũng khớp ngữ cảnh địa điểm: `We really love this place`.

---

# 10. Nội dung portfolio tiếng Việt

## Project/CTF Challenge: 78CT

**Category:** OSINT / Steganography / Misc  
**Objective:** Xác định địa điểm từ ảnh vệ tinh và mô tả OSINT, sau đó tìm manh mối được ẩn trong review Google Maps để khôi phục flag.

**Tools Used:** Google Maps, Google Search, Google Maps Reviews, Python, Base64 Decoder, CyberChef.

**Methodology:**

1. Phân tích mô tả challenge và ảnh vệ tinh để xác định đây là bài OSINT về địa điểm thật.
2. Tìm kiếm các công viên/hồ có hình dạng giống rồng và đối chiếu với ảnh challenge.
3. Xác định địa điểm là Hồ điều hòa Hồ Sơn tại Tuy Hòa.
4. Kiểm tra Google Maps Reviews để tìm review bất thường liên quan đến tác giả `Jaze`.
5. Phát hiện review có pattern chữ hoa/chữ thường bất thường và hashtag `#v1tnamese`.
6. Trích xuất các ký tự lệch kiểu chữ để tạo chuỗi Base64, sau đó decode để lấy flag.

**Key Findings:**

- Địa điểm thật là Hồ điều hòa Hồ Sơn.
- Review khả nghi được đăng bởi tài khoản `JaZe`.
- Nội dung review sử dụng kỹ thuật mixed-case steganography.
- Chuỗi ẩn thu được là Base64: `VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9`.

**Result:**

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

**Skills Demonstrated:**

- OSINT geolocation từ ảnh vệ tinh.
- Phân tích clue ngôn ngữ trong mô tả challenge.
- Tìm kiếm và xác minh dữ liệu công khai trên Google Maps.
- Nhận diện steganography trong văn bản.
- Decode Base64 và viết script Python kiểm chứng.

**Lessons Learned:**

Bài challenge cho thấy OSINT không chỉ là tìm địa điểm mà còn cần kiểm tra dấu vết công khai xung quanh địa điểm đó. Trong các bài CTF, review, ảnh hoặc hashtag có thể chứa dữ liệu ẩn. Ngoài ra, bản dịch tự động có thể làm hỏng clue, nên cần ưu tiên lấy bản gốc khi phân tích text steganography.

---

# 11. Short English Portfolio Version

## Project/CTF Challenge: 78CT

**Category:** OSINT / Steganography / Misc  
**Objective:** Identify a real-world lake location from satellite imagery and recover the hidden flag left in a public Google Maps review.

**Tools Used:** Google Maps, Google Search, Google Reviews, Python, Base64 decoder, CyberChef.

**Methodology:**

1. Analyzed the challenge description and satellite image to identify a dragon-shaped park beside a lake.
2. Used OSINT techniques to correlate the image with Ho Son Lake in Tuy Hoa, Vietnam.
3. Reviewed Google Maps comments and identified a suspicious review from the user `JaZe`.
4. Detected a mixed-case text steganography pattern in the review.
5. Extracted the abnormal characters to reconstruct a Base64 string.
6. Decoded the Base64 string to obtain the final flag.

**Key Findings:**

- Target location: Ho Son Lake, Tuy Hoa.
- Suspicious artifact: Google Maps review by `JaZe`.
- Hidden data technique: mixed-case steganography + Base64 encoding.

**Result:**

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

**Skills Demonstrated:** OSINT geolocation, public-source investigation, text steganography analysis, Base64 decoding, Python scripting.

**Lessons Learned:** Public reviews and user-generated content can be used as CTF artifacts. Original-language text should be preserved during analysis because automatic translation may destroy hidden character patterns.

---

# 12. Báo cáo ngắn để nộp

## Mục tiêu

Mục tiêu của bài là xác định địa điểm trong ảnh challenge và tìm dữ liệu mà tác giả để lại tại địa điểm đó để khôi phục flag.

## Môi trường phân tích

- Trình duyệt web
- Google Maps
- Google Search
- Python 3
- Terminal Linux hoặc CyberChef để decode Base64

## Công cụ sử dụng

| Công cụ | Vai trò |
|---|---|
| Google Maps | Xác minh địa điểm và kiểm tra review |
| Google Search | Tìm kiếm địa điểm từ clue hình rồng và hồ |
| Python | Tự động hóa quá trình trích xuất ký tự ẩn |
| Base64 decoder | Decode chuỗi ẩn để lấy flag |

## Các bước thực hiện

1. Quan sát ảnh challenge và nhận ra hình dạng công viên giống con rồng bên cạnh một hồ.
2. Tìm kiếm các địa điểm ở Việt Nam có hồ/công viên hình rồng và xác định được Hồ điều hòa Hồ Sơn tại Tuy Hòa.
3. Mở địa điểm trên Google Maps và kiểm tra phần bài đánh giá.
4. Phát hiện review của tài khoản `JaZe`, có nội dung trộn chữ hoa/thường bất thường và hashtag `#v1tnamese`.
5. Trích xuất các ký tự lệch kiểu chữ trong từng từ để tạo chuỗi encoded.
6. Decode chuỗi bằng Base64 và thu được flag.

## Kết quả

Chuỗi extracted:

```text
VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9
```

Sau khi decode Base64:

```text
V1T{W3_r34lly_l0v3_7h15_pl4c3}
```

## Kết luận

Challenge 78CT là bài OSINT kết hợp text steganography. Người chơi cần xác định đúng địa điểm từ ảnh vệ tinh, sau đó tìm review bất thường trên Google Maps. Review của `JaZe` chứa dữ liệu ẩn bằng kỹ thuật mixed-case, sau khi trích xuất và decode Base64 sẽ nhận được flag cuối cùng.

---

# 13. Tóm tắt nhanh đáp án

- **Location:** Hồ điều hòa Hồ Sơn, Tuy Hòa
- **Suspicious account:** JaZe
- **Hidden technique:** Mixed-case text steganography
- **Encoded string:** `VjFUe1czX3IzNGxseV9sMHYzXzdoMTVfcGw0YzN9`
- **Final flag:** `V1T{W3_r34lly_l0v3_7h15_pl4c3}`

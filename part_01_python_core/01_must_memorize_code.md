# GIẢI THÍCH CODE BẮT BUỘC NHỚ - PYTHON NỀN TẢNG

## 1. Mục tiêu file code

File `01_must_memorize_code.py` dùng để luyện các cú pháp Python bắt buộc khi ôn thi AI. Trọng tâm không phải viết chương trình lớn, mà là đọc hiểu được đoạn code ngắn, dự đoán output và tự viết được các thao tác dữ liệu nhỏ như đếm nhãn, chuẩn hóa min-max, chia train/test.

## 2. Danh sách block code cần nhớ

- `print`, variables, data types.
- `input` and type casting.
- `if/elif/else`.
- `for` và `range`.
- `while`.
- `list`.
- `dictionary`.
- `set`.
- `string`.
- `function`.
- Min-max normalization.
- Train/test split.
- `try/except`.
- Dataset label counting.

## 3. Giải thích từng block

### 3.1 `print`, biến và kiểu dữ liệu

Mục đích: biết cách tạo biến và kiểm tra kiểu dữ liệu.

```python
name = "An"
age = 20
height = 1.70
is_student = True
print(type(age))
```

Cú pháp cần nhớ: Python không cần khai báo kiểu trước. Kiểu được suy ra từ giá trị gán.

Lỗi hay gặp: nhầm `"20"` là số; thực tế đó là chuỗi.

### 3.2 `input` và ép kiểu

Mục đích: hiểu dữ liệu nhập từ bàn phím luôn là string.

```python
# raw_age = input("Nhap tuoi: ")
# age_number = int(raw_age)
```

Cú pháp cần nhớ: dùng `int()`, `float()` khi cần tính toán số.

Lỗi hay gặp: lấy `input()` cộng số trực tiếp gây lỗi kiểu dữ liệu.

### 3.3 `if/elif/else`

Mục đích: phân nhánh logic theo điều kiện.

```python
if score >= 8.0:
    level = "Gioi"
elif score >= 6.5:
    level = "Kha"
else:
    level = "Can co gang"
```

Cú pháp cần nhớ: sau điều kiện có dấu `:`, block bên trong phải thụt dòng.

Lỗi hay gặp: dùng `=` thay vì `==` khi so sánh bằng.

### 3.4 `for` và `range`

Mục đích: lặp số lần xác định.

```python
total = 0
for i in range(1, 11):
    total += i
```

Cú pháp cần nhớ: `range(1, 11)` sinh các số từ 1 đến 10, không gồm 11.

Lỗi hay gặp: hiểu sai điểm kết thúc của `range`.

### 3.5 `while`

Mục đích: lặp khi điều kiện còn đúng.

```python
while current <= n:
    factorial *= current
    current += 1
```

Cú pháp cần nhớ: luôn có bước cập nhật biến điều kiện.

Lỗi hay gặp: quên `current += 1` làm vòng lặp vô hạn.

### 3.6 List

Mục đích: lưu nhiều giá trị có thứ tự.

```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers[0])
```

Cú pháp cần nhớ: index bắt đầu từ 0.

Lỗi hay gặp: truy cập index vượt quá độ dài list.

### 3.7 Dictionary

Mục đích: lưu dữ liệu dạng key-value.

```python
student = {"name": "An", "score": 8.5}
print(student["score"])
```

Cú pháp cần nhớ: dùng key để lấy value.

Lỗi hay gặp: lấy key không tồn tại gây `KeyError`; có thể dùng `get()`.

### 3.8 Đếm tần suất bằng dict

Mục đích: đếm số lần xuất hiện của nhãn hoặc token.

```python
counts[label] = counts.get(label, 0) + 1
```

Cú pháp cần nhớ: `get(label, 0)` trả 0 nếu key chưa tồn tại.

Lỗi hay gặp: tăng biến đếm khi key chưa được khởi tạo.

### 3.9 Set

Mục đích: loại phần tử trùng.

```python
unique_values = set([1, 2, 2, 3])
```

Cú pháp cần nhớ: set không giữ thứ tự ổn định như list.

Lỗi hay gặp: kỳ vọng output set có thứ tự giống input.

### 3.10 String

Mục đích: làm sạch và tách chuỗi.

```python
text = "  AI,Python  "
tokens = text.strip().lower().split(",")
```

Cú pháp cần nhớ: có thể nối nhiều method nếu mỗi method trả về string phù hợp.

Lỗi hay gặp: nhầm `split()` trả string; thực tế trả list.

### 3.11 Function

Mục đích: đóng gói logic để dùng lại.

```python
def is_even(x):
    return x % 2 == 0
```

Cú pháp cần nhớ: `return` trả kết quả cho nơi gọi hàm.

Lỗi hay gặp: dùng `print` trong hàm nhưng quên `return`.

### 3.12 Min-max normalization

Mục đích: đưa dữ liệu số về khoảng 0 đến 1.

```python
(x - min_value) / (max_value - min_value)
```

Cú pháp cần nhớ: phải xử lý trường hợp `max_value == min_value` để tránh chia cho 0.

Lỗi hay gặp: normalize từng phần tử nhưng tính min/max sai phạm vi.

### 3.13 Train/test split

Mục đích: chia dữ liệu để train và kiểm tra model.

```python
split_index = int(len(data) * 0.8)
train_data = data[:split_index]
test_data = data[split_index:]
```

Cú pháp cần nhớ: slicing `[:split_index]` lấy phần đầu, `[split_index:]` lấy phần sau.

Lỗi hay gặp: chia dữ liệu đã được sắp theo nhãn mà không shuffle, làm test set lệch.

### 3.14 `try/except`

Mục đích: xử lý lỗi có thể dự đoán.

```python
try:
    number = int(raw_value)
except ValueError:
    print("Khong the ep kieu")
```

Cú pháp cần nhớ: chỉ bắt lỗi cụ thể khi có thể.

Lỗi hay gặp: bắt mọi lỗi bằng `except:` làm che mất bug thật.

### 3.15 Dataset label counting

Mục đích: thao tác dữ liệu dạng `list[dict]`, rất hay gặp trong AI.

```python
for row in dataset:
    label = row["label"]
    counts[label] = counts.get(label, 0) + 1
```

Cú pháp cần nhớ: mỗi `row` là một dict, lấy nhãn bằng `row["label"]`.

Lỗi hay gặp: tên key không thống nhất, ví dụ lúc dùng `"label"`, lúc dùng `"labels"`.

## 4. Câu hỏi ôn nhanh

1. `input()` trả về kiểu dữ liệu gì?
2. `range(1, 5)` sinh ra các số nào?
3. Vì sao index đầu tiên của list là 0?
4. Khi nào dùng dict thay vì list?
5. `set` có nhược điểm gì khi cần giữ thứ tự?
6. `split()` trả về kiểu dữ liệu gì?
7. `join()` dùng để làm gì?
8. `return` khác `print` như thế nào?
9. Vì sao cần xử lý `max == min` khi normalize?
10. Train/test split dùng để làm gì?
11. `counts.get(label, 0)` có ý nghĩa gì?
12. `KeyError` thường xảy ra khi nào?
13. `IndexError` thường xảy ra khi nào?
14. Vì sao không nên dùng vòng `while` thiếu điều kiện dừng?
15. Khi nào nên dùng `try/except`?

## 5. Bài tập tự gõ lại

- [ ] Gõ lại block biến và kiểu dữ liệu.
- [ ] Gõ lại block phân loại điểm bằng `if/elif/else`.
- [ ] Gõ lại block tính tổng bằng `for`.
- [ ] Gõ lại block tính giai thừa bằng `while`.
- [ ] Gõ lại block thao tác list.
- [ ] Gõ lại block đếm tần suất bằng dict.
- [ ] Gõ lại block xử lý string.
- [ ] Gõ lại function `is_prime`.
- [ ] Gõ lại function `min_max_normalize`.
- [ ] Gõ lại function `train_test_split_simple`.
- [ ] Gõ lại block label counting với dataset dạng `list[dict]`.

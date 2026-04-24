# Ôn nhanh Python Core

## Bảng cú pháp

| Cú pháp | Ý nghĩa | Ví dụ |
|---|---|---|
| `x = 10` | Gán biến | `score = 8.5` |
| `if condition:` | Rẽ nhánh | `if score >= 5:` |
| `for x in values:` | Duyệt từng phần tử | `for score in scores:` |
| `for i in range(n):` | Lặp theo chỉ số | `for i in range(10):` |
| `while condition:` | Lặp khi điều kiện đúng | `while n > 0:` |
| `def f(x):` | Định nghĩa hàm | `def mean(values):` |
| `return value` | Trả kết quả từ hàm | `return total / count` |

## Built-in functions

| Hàm | Ý nghĩa |
|---|---|
| `print()` | In ra màn hình |
| `type()` | Xem kiểu dữ liệu |
| `int()` | Ép sang số nguyên |
| `float()` | Ép sang số thực |
| `str()` | Ép sang chuỗi |
| `len()` | Lấy độ dài |
| `sum()` | Tính tổng |
| `min()` | Lấy giá trị nhỏ nhất |
| `max()` | Lấy giá trị lớn nhất |
| `range()` | Tạo dãy số cho vòng lặp |

## List methods

| Method | Ý nghĩa |
|---|---|
| `append(x)` | Thêm một phần tử |
| `extend(xs)` | Nối nhiều phần tử |
| `remove(x)` | Xóa phần tử theo giá trị |
| `pop()` | Lấy và xóa phần tử cuối |
| `sort()` | Sắp xếp tại chỗ |
| `count(x)` | Đếm số lần xuất hiện |

## String methods

| Method | Ý nghĩa |
|---|---|
| `strip()` | Bỏ khoảng trắng hai đầu |
| `lower()` | Chuyển thành chữ thường |
| `upper()` | Chuyển thành chữ hoa |
| `split()` | Tách chuỗi thành list |
| `join()` | Ghép list string thành chuỗi |
| `replace(a, b)` | Thay chuỗi con |

## Dict methods

| Method | Ý nghĩa |
|---|---|
| `get(key, default)` | Lấy value an toàn |
| `keys()` | Lấy danh sách key |
| `values()` | Lấy danh sách value |
| `items()` | Lấy cặp key-value |
| `update()` | Cập nhật dict |

## 20 câu hỏi ôn nhanh

1. Python dùng indentation để làm gì?
2. `=` và `==` khác nhau như thế nào?
3. `list` và `tuple` khác nhau ở điểm nào?
4. Khi nào nên dùng `dict`?
5. `set` có tác dụng gì khi xử lý dữ liệu?
6. `input()` trả về kiểu dữ liệu gì?
7. Vì sao cần `return` trong function?
8. `append` khác `extend` như thế nào?
9. `split()` trả về kiểu gì?
10. `join()` dùng trên kiểu dữ liệu nào?
11. Cách tính mean của list số là gì?
12. Làm sao tránh lỗi chia cho 0 khi normalize?
13. `try/except` dùng để làm gì?
14. `KeyError` thường xảy ra khi nào?
15. `IndexError` thường xảy ra khi nào?
16. Train/test split dùng để làm gì?
17. Label counting là gì?
18. Min-max normalization đưa dữ liệu về khoảng nào?
19. Vì sao code AI thường dùng list of dict?
20. Khi nào vòng `while` có thể bị vô hạn?

## 10 câu hỏi dự đoán output

1. Code:

```python
print(3 // 2)
```

Đáp án: __________

2. Code:

```python
print(3 % 2)
```

Đáp án: __________

3. Code:

```python
values = [1, 2, 3]
print(values[1])
```

Đáp án: __________

4. Code:

```python
text = " AI ".strip().lower()
print(text)
```

Đáp án: __________

5. Code:

```python
print(len(["a", "b", "c"]))
```

Đáp án: __________

6. Code:

```python
print([x * 2 for x in [1, 2, 3]])
```

Đáp án: __________

7. Code:

```python
counts = {}
counts["a"] = counts.get("a", 0) + 1
print(counts)
```

Đáp án: __________

8. Code:

```python
print("a,b,c".split(","))
```

Đáp án: __________

9. Code:

```python
def f(x):
    return x + 1
print(f(4))
```

Đáp án: __________

10. Code:

```python
print(set([1, 1, 2, 3]))
```

Đáp án: __________

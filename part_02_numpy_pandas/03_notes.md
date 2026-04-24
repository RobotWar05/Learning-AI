# Ghi chú NumPy và Pandas

## Ghi chú cá nhân

- Khái niệm chưa chắc: ...
- Cú pháp hay quên: ...
- Lỗi đã gặp khi chạy code: ...
- Câu hỏi cần hỏi lại: ...

## Lỗi thường gặp

### Nhầm list Python với NumPy array

```python
values = [1, 2, 3]
# values + 1  # lỗi

arr = np.array([1, 2, 3])
print(arr + 1)
```

### Nhầm shape hàng/cột

`shape = (2, 3)` nghĩa là 2 hàng và 3 cột.

### Quên `axis`

```python
data.mean()
data.mean(axis=0)
data.mean(axis=1)
```

Ba dòng trên cho kết quả khác nhau.

### Nhầm `loc` và `iloc`

- `loc`: chọn theo label.
- `iloc`: chọn theo vị trí số nguyên.

### Không xử lý missing values

Nhiều thuật toán ML không nhận dữ liệu có `NaN`. Cần kiểm tra bằng:

```python
df.isnull().sum()
```

### Chained assignment

Tránh sửa DataFrame con theo kiểu mơ hồ. Nếu cần sửa một lát cắt, nên dùng `.copy()` hoặc `.loc`.

```python
filtered = df[df["score"] >= 7].copy()
filtered["passed"] = True
```

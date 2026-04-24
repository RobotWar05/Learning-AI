# Giải thích code bắt buộc nhớ - NumPy và Pandas

## 1. Mục tiêu file code

File `01_must_memorize_code.py` giúp bạn luyện các thao tác xử lý dữ liệu thường gặp trong bài thi AI: tạo mảng, kiểm tra shape, lọc dữ liệu, tính thống kê, tạo DataFrame, xử lý missing values và merge bảng.

## 2. Các block code chính

- Import `numpy` và `pandas`.
- Tạo NumPy array.
- Kiểm tra `shape`, `ndim`, `dtype`.
- Indexing và slicing.
- Boolean mask.
- Vectorized operations.
- Broadcasting.
- Aggregation với `axis`.
- Reshape.
- Tạo DataFrame.
- Đọc CSV.
- Chọn cột, lọc dòng.
- `loc` và `iloc`.
- Thêm cột.
- `groupby`.
- `sort_values`.
- Missing values.
- Merge hai DataFrame.

## 3. Giải thích cú pháp quan trọng

### NumPy array

```python
arr = np.array([10, 20, 30])
```

NumPy array giống list ở bề mặt nhưng tối ưu cho tính toán số. Khi cộng `arr + 5`, NumPy cộng 5 cho từng phần tử; list Python không làm như vậy.

### Shape, ndim, dtype

```python
matrix.shape
matrix.ndim
matrix.dtype
```

- `shape`: kích thước từng chiều.
- `ndim`: số chiều.
- `dtype`: kiểu dữ liệu bên trong array.

Lỗi hay gặp: nhầm `(2, 3)` là 3 hàng 2 cột. Thực tế là 2 hàng, 3 cột.

### Indexing và slicing

```python
matrix[:, 1]
```

Dấu `:` nghĩa là lấy tất cả hàng. `1` là cột thứ hai vì index bắt đầu từ 0.

### Boolean mask

```python
mask = arr >= 30
arr[mask]
```

Mask là array boolean dùng để lọc phần tử thỏa điều kiện.

### Vectorization

```python
arr * 2
```

Vectorization giúp viết phép toán trên toàn bộ array mà không cần vòng lặp Python.

### Broadcasting

```python
scores + bonus
```

Broadcasting cho phép NumPy tự mở rộng kích thước phù hợp khi cộng array có shape tương thích.

Lỗi hay gặp: cộng hai array shape không tương thích.

### Axis

```python
data_2d.sum(axis=0)
data_2d.sum(axis=1)
```

- `axis=0`: gộp theo hàng, kết quả theo từng cột.
- `axis=1`: gộp theo cột, kết quả theo từng hàng.

Lỗi hay gặp: quên `axis` nên tính tổng toàn bộ dữ liệu thay vì theo cột/hàng.

### DataFrame

```python
df = pd.DataFrame({"name": ["An"], "score": [8.5]})
```

DataFrame là bảng dữ liệu có hàng và cột, rất gần với dữ liệu tabular trong ML.

### Chọn cột và lọc dòng

```python
df["score"]
df[df["score"] >= 7]
```

Cú pháp lọc dùng điều kiện trả về Series boolean.

### `loc` và `iloc`

```python
df.loc[0:1, ["name", "score"]]
df.iloc[0:2, 0:2]
```

- `loc`: chọn theo label/tên.
- `iloc`: chọn theo vị trí số nguyên.

Lỗi hay gặp: dùng `loc` như `iloc` hoặc ngược lại.

### Missing values

```python
df["score"].fillna(df["score"].mean())
```

Missing values thường phải xử lý trước khi train model.

Lỗi hay gặp: fill missing value bằng một giá trị không hợp lý làm sai phân bố dữ liệu.

### Merge

```python
pd.merge(df, classes, on="name", how="left")
```

Merge dùng để gộp hai bảng theo một key chung.

## 4. Lỗi hay gặp

- Nhầm list Python với NumPy array.
- Nhầm shape hàng/cột.
- Nhầm `loc` và `iloc`.
- Quên `axis`.
- Không kiểm tra missing values trước khi train.
- Chained assignment: sửa dữ liệu qua một lát cắt DataFrame có thể gây hành vi khó đoán. Nên tạo bản copy rõ ràng khi cần chỉnh dữ liệu con.

## 5. Mini exercises

1. Tạo array `[1, 2, 3, 4, 5]`, lọc số lớn hơn 3.
2. Tạo matrix 2x3, tính mean theo từng cột.
3. Tạo DataFrame 5 sinh viên, lọc điểm lớn hơn 7.
4. Thêm cột `passed` dựa trên điểm.
5. Tạo hai DataFrame và merge theo cột `id`.

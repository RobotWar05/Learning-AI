# Ôn nhanh NumPy và Pandas

## Bảng lệnh NumPy

| Lệnh | Ý nghĩa |
|---|---|
| `np.array([...])` | Tạo array |
| `arr.shape` | Kích thước array |
| `arr.ndim` | Số chiều |
| `arr.dtype` | Kiểu dữ liệu |
| `arr[mask]` | Lọc bằng boolean mask |
| `arr.reshape(r, c)` | Đổi shape |
| `arr.mean(axis=0)` | Mean theo cột |
| `np.concatenate([...])` | Nối array |

## Bảng lệnh Pandas

| Lệnh | Ý nghĩa |
|---|---|
| `pd.DataFrame(...)` | Tạo DataFrame |
| `pd.read_csv(...)` | Đọc CSV |
| `df.head()` | Xem dòng đầu |
| `df.info()` | Xem thông tin cột |
| `df.describe()` | Thống kê mô tả |
| `df["col"]` | Chọn cột |
| `df[df["col"] > 0]` | Lọc dòng |
| `df.loc[...]` | Chọn theo label |
| `df.iloc[...]` | Chọn theo vị trí |
| `df.groupby("col")` | Nhóm dữ liệu |
| `pd.merge(...)` | Gộp bảng |
| `df.isnull().sum()` | Đếm missing values |
| `df.fillna(...)` | Điền missing values |

## 20 câu hỏi ôn nhanh

1. NumPy array khác list Python ở điểm nào?
2. `shape` cho biết thông tin gì?
3. `ndim` là gì?
4. `dtype` là gì?
5. Boolean mask dùng để làm gì?
6. Vectorization là gì?
7. Broadcasting là gì?
8. `axis=0` nghĩa là gì?
9. `axis=1` nghĩa là gì?
10. DataFrame là gì?
11. Series là gì?
12. `head()` dùng để làm gì?
13. `describe()` cho biết gì?
14. `loc` khác `iloc` như thế nào?
15. `groupby` dùng khi nào?
16. Missing values thường được biểu diễn thế nào?
17. `fillna` khác `dropna` ở đâu?
18. Merge dùng để làm gì?
19. Vì sao cần kiểm tra phân bố label?
20. Vì sao cần tách `X` và `y` trước khi train model?

## 10 câu hỏi dự đoán output

1. Code:

```python
arr = np.array([1, 2, 3])
print(arr + 1)
```

Đáp án: __________

2. Code:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
```

Đáp án: __________

3. Code:

```python
print(np.array([1, 2, 3]) >= 2)
```

Đáp án: __________

4. Code:

```python
data = np.array([[1, 2], [3, 4]])
print(data.sum(axis=0))
```

Đáp án: __________

5. Code:

```python
data = np.array([[1, 2], [3, 4]])
print(data.sum(axis=1))
```

Đáp án: __________

6. Code:

```python
df = pd.DataFrame({"score": [5, 8, 9]})
print(df[df["score"] >= 8])
```

Đáp án: __________

7. Code:

```python
df = pd.DataFrame({"a": [1, None, 3]})
print(df.isnull().sum())
```

Đáp án: __________

8. Code:

```python
df = pd.DataFrame({"label": ["a", "a", "b"], "score": [1, 3, 5]})
print(df.groupby("label")["score"].mean())
```

Đáp án: __________

9. Code:

```python
arr = np.arange(6).reshape(2, 3)
print(arr)
```

Đáp án: __________

10. Code:

```python
df = pd.DataFrame({"x": [1, 2]})
df["y"] = df["x"] * 10
print(df)
```

Đáp án: __________

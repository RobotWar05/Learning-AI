# Giải thích template scikit-learn

## 1. Mục tiêu file code

File `02_sklearn_code_templates.py` cung cấp các mẫu code Machine Learning thường gặp khi ôn thi: chia train/test, scaling, train model, predict, tính metric, confusion matrix, KMeans và cross validation.

## 2. Ý nghĩa `X` và `y`

- `X`: feature matrix, là dữ liệu đầu vào của model.
- `y`: label/target, là kết quả đúng cần học hoặc dự đoán.

Trong supervised learning, luôn cần cả `X` và `y`. Trong clustering như KMeans, thường chỉ có `X`.

## 3. `fit` và `predict`

```python
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `fit`: model học từ dữ liệu train.
- `predict`: model dự đoán trên dữ liệu mới.

Lỗi hay gặp: predict trên train set rồi tưởng đó là kết quả đánh giá cuối cùng.

## 4. Train/test split

```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

`test_size=0.2` nghĩa là 20% dữ liệu dùng làm test. `random_state` giúp kết quả có thể lặp lại.

## 5. StandardScaler

```python
scaler.fit_transform(X_train)
scaler.transform(X_test)
```

Chỉ `fit` scaler trên train data. Test data chỉ dùng `transform`. Làm ngược lại sẽ gây data leakage.

## 6. Metrics

- `accuracy_score`: tỷ lệ đúng.
- `precision_score`: độ chính xác của dự đoán positive.
- `recall_score`: khả năng tìm đủ mẫu positive.
- `f1_score`: cân bằng precision và recall.
- `mean_squared_error`: dùng cho regression.
- `confusion_matrix`: xem TP, FP, FN, TN.

## 7. Các template chính

### Linear Regression

Dùng cho bài toán dự đoán số liên tục. Output là giá trị số.

### Logistic Regression

Dùng cho classification cơ bản, dù tên có chữ regression.

### KNN

Dự đoán dựa trên láng giềng gần nhất. Cần scaling vì dựa trên khoảng cách.

### Decision Tree

Dễ giải thích, nhưng dễ overfit nếu không giới hạn độ sâu.

### KMeans

Dùng để phân cụm khi không có label. Cần chọn `n_clusters`.

### Cross validation

Đánh giá model trên nhiều lần chia dữ liệu để giảm phụ thuộc vào một lần split.

## 8. Lỗi hay gặp

- Quên tách train/test.
- Scale toàn bộ dữ liệu trước khi split, gây data leakage.
- Dùng accuracy cho dữ liệu lệch nhãn nặng.
- Nhầm Logistic Regression là thuật toán regression.
- Quên `stratify=y` khi classification có nguy cơ lệch nhãn.
- Dùng KMeans rồi đánh giá như supervised learning.

## 9. Mini exercises

1. Đổi `test_size` từ 0.25 sang 0.3 và quan sát số mẫu test.
2. Thay KNN bằng `n_neighbors=5`.
3. Thêm `RandomForestClassifier` vào dictionary models.
4. Tính F1 cho Logistic Regression.
5. Giải thích vì sao cần `zero_division=0` trong một số metric.

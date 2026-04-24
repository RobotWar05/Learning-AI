# Bài tập Machine Learning

## Phân loại dạng học

1. Dự đoán giá nhà từ diện tích và vị trí: supervised hay unsupervised?
2. Nhóm khách hàng theo hành vi mua hàng nhưng không có nhãn: supervised hay unsupervised?
3. Robot học đi bằng phần thưởng: thuộc kiểu học nào?

## Regression/classification/clustering

1. Dự đoán điểm thi: regression hay classification?
2. Dự đoán email spam/không spam: regression hay classification?
3. Chia ảnh thành các nhóm tương tự: clustering hay classification?

## Tính accuracy thủ công

Cho:

```text
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]
```

1. Có bao nhiêu dự đoán đúng?
2. Accuracy bằng bao nhiêu?

## Confusion matrix

1. Xác định TP, FP, FN, TN từ `y_true` và `y_pred` ở trên.
2. Tính precision theo lời.
3. Tính recall theo lời.

## Chọn metric

1. Bài toán phát hiện bệnh hiếm nên ưu tiên recall hay accuracy?
2. Bài toán spam email có dữ liệu lệch nhãn thì accuracy có thể gây hiểu nhầm thế nào?
3. Khi nào F1 hữu ích?

## Viết pipeline scikit-learn

Viết pseudo-code gồm:

1. Load data.
2. Tách `X`, `y`.
3. Train/test split.
4. StandardScaler.
5. Model.
6. `fit`.
7. `predict`.
8. Metric.

## Overfitting

1. Giải thích overfitting bằng ví dụ học thuộc đề.
2. Nêu 3 cách giảm overfitting.
3. Decision Tree quá sâu thường gặp rủi ro gì?

## So sánh thuật toán

1. Linear Regression và Logistic Regression khác nhau ở output.
2. KNN và Decision Tree khác nhau ở cách dự đoán.
3. Random Forest cải thiện Decision Tree như thế nào?
4. KMeans khác KNN ở điểm nào?

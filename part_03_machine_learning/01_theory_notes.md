# Ghi chú lý thuyết Machine Learning

## Bản chất

Machine Learning là cách cho máy học quy luật từ dữ liệu thay vì viết tay toàn bộ luật.

## Quy trình cơ bản

1. Thu thập dữ liệu.
2. Làm sạch và tiền xử lý.
3. Tách feature/label.
4. Chia train/test.
5. Chọn model.
6. Train bằng `fit`.
7. Dự đoán bằng `predict`.
8. Đánh giá bằng metric.

## Điều cần phân biệt

- Classification: dự đoán nhãn rời rạc.
- Regression: dự đoán giá trị liên tục.
- Overfitting: học quá sát train data, test kém.
- Underfitting: model quá đơn giản, train và test đều kém.

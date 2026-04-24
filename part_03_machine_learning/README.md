# Phần 3: Machine Learning

## Mục tiêu

Nắm được bản chất Machine Learning, phân biệt các dạng bài toán, hiểu quy trình huấn luyện mô hình và đọc được code scikit-learn cơ bản.

## AI vs ML vs DL

- AI là lĩnh vực rộng về hệ thống có hành vi thông minh.
- ML là nhánh của AI, cho máy học quy luật từ dữ liệu.
- DL là nhánh của ML, dùng neural network nhiều tầng để học biểu diễn dữ liệu.

## Các kiểu học chính

- Supervised learning: dữ liệu có label, ví dụ dự đoán spam/không spam.
- Unsupervised learning: dữ liệu không có label, ví dụ phân cụm khách hàng.
- Reinforcement learning: agent học qua hành động và phần thưởng.

## Dạng bài toán

- Regression: dự đoán số liên tục, ví dụ giá nhà.
- Classification: dự đoán nhãn, ví dụ bệnh/không bệnh.
- Clustering: chia nhóm dữ liệu chưa có nhãn.

## Quy trình ML cơ bản

1. Xác định bài toán.
2. Thu thập dữ liệu.
3. Làm sạch dữ liệu.
4. Tách feature `X` và label `y`.
5. Chia train/test.
6. Chọn model.
7. Train bằng `fit`.
8. Dự đoán bằng `predict`.
9. Đánh giá bằng metric.
10. Điều chỉnh model nếu cần.

## Khái niệm trọng tâm

- Train/test split.
- Feature và label.
- Overfitting và underfitting.
- Loss function.
- Metrics: accuracy, precision, recall, F1, MSE, MAE, RMSE.

## Thuật toán cần học

- Linear Regression.
- Logistic Regression.
- KNN.
- Decision Tree.
- Random Forest ở mức khái niệm.
- Naive Bayes.
- K-means.
- SVM ở mức khái niệm.

## File trong phần này

- [Checklist](./00_checklist.md)
- [Lý thuyết ML](./01_theory_notes.md)
- [Template scikit-learn](./02_sklearn_code_templates.py)
- [Giải thích template scikit-learn](./02_sklearn_code_templates.md)
- [Bài tập](./03_exercises.md)
- [Ôn nhanh](./04_quick_review.md)

## Thứ tự học

1. Đọc AI/ML/DL và các dạng bài toán.
2. Học quy trình train/test/evaluate.
3. Học metric trước khi học nhiều thuật toán.
4. Gõ lại template scikit-learn.
5. Làm bài tập chọn thuật toán và metric.

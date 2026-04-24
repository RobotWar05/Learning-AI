# Ghi chú lý thuyết Machine Learning

## 1. Quan hệ AI/ML/DL

AI là mục tiêu rộng: tạo hệ thống có khả năng xử lý nhiệm vụ cần trí tuệ. ML là cách tiếp cận trong AI, trong đó hệ thống học từ dữ liệu. DL là nhánh của ML dùng neural network nhiều tầng.

## 2. Supervised và unsupervised learning

Supervised learning dùng dữ liệu có nhãn. Mỗi mẫu có input và output đúng. Model học ánh xạ từ input sang output.

Unsupervised learning dùng dữ liệu không có nhãn. Model tìm cấu trúc ẩn, ví dụ nhóm dữ liệu tương tự nhau.

## 3. Regression, classification, clustering

- Regression: output là số liên tục, ví dụ dự đoán nhiệt độ.
- Classification: output là nhãn rời rạc, ví dụ email spam/không spam.
- Clustering: chia nhóm dữ liệu khi chưa có nhãn.

## 4. Loss function

Loss đo mức sai của model trên dữ liệu train. Training là quá trình tìm tham số làm loss giảm.

Ví dụ:

- Regression thường dùng MSE hoặc MAE.
- Classification thường dùng cross entropy.

## 5. Gradient descent

Gradient descent là ý tưởng cập nhật tham số theo hướng làm loss giảm. Không cần nhớ công thức sâu nếu thi cơ bản, nhưng cần hiểu:

- Learning rate quá lớn: dễ dao động hoặc không hội tụ.
- Learning rate quá nhỏ: học rất chậm.

## 6. Train/test/validation

- Train set: dùng để học tham số.
- Validation set: dùng để chọn model/hyperparameter.
- Test set: dùng để đánh giá cuối cùng.

Không đánh giá model chỉ trên train set vì kết quả có thể quá lạc quan.

## 7. Overfitting và underfitting

Overfitting: model học quá sát train data, train tốt nhưng test kém.

Underfitting: model quá đơn giản, train và test đều kém.

## 8. Bias/variance

- Bias cao: model quá đơn giản, dễ underfit.
- Variance cao: model quá nhạy với dữ liệu train, dễ overfit.

Mục tiêu là cân bằng giữa bias và variance.

## 9. Feature scaling

Scaling đưa feature về thang đo phù hợp. Cần chú ý với KNN, SVM, Logistic Regression, neural network. Decision Tree thường ít nhạy với scaling hơn.

## 10. Confusion matrix

Với binary classification:

- TP: dự đoán positive và đúng.
- FP: dự đoán positive nhưng sai.
- FN: dự đoán negative nhưng sai.
- TN: dự đoán negative và đúng.

## 11. Metrics

- Accuracy: tỷ lệ dự đoán đúng.
- Precision: trong các mẫu dự đoán positive, bao nhiêu mẫu thật sự positive.
- Recall: trong các mẫu thật sự positive, model tìm được bao nhiêu.
- F1: trung bình điều hòa giữa precision và recall.
- MSE: trung bình bình phương sai số.
- MAE: trung bình trị tuyệt đối sai số.
- RMSE: căn bậc hai của MSE.

## 12. Khi nào dùng thuật toán nào

| Thuật toán | Dùng khi | Lưu ý |
|---|---|---|
| Linear Regression | Dự đoán số liên tục, quan hệ gần tuyến tính | Dễ giải thích |
| Logistic Regression | Classification cơ bản | Cần scaling trong nhiều trường hợp |
| KNN | Dữ liệu nhỏ, ranh giới đơn giản | Nhạy với scaling |
| Decision Tree | Cần model dễ giải thích | Dễ overfit nếu cây sâu |
| Random Forest | Cần ổn định hơn Decision Tree | Khó giải thích hơn một cây đơn |
| Naive Bayes | Text classification cơ bản | Giả định độc lập mạnh |
| K-means | Phân cụm không nhãn | Cần chọn số cụm `k` |
| SVM | Classification với biên phân tách rõ | Nhạy với scaling và tham số |

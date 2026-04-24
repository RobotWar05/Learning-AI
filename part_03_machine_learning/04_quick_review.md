# Ôn nhanh Machine Learning

## Định nghĩa trọng tâm

| Khái niệm | Ý nghĩa |
|---|---|
| AI | Lĩnh vực tạo hệ thống có hành vi thông minh |
| ML | Máy học quy luật từ dữ liệu |
| DL | ML dùng neural network nhiều tầng |
| Feature | Biến đầu vào |
| Label | Giá trị cần dự đoán |
| Train set | Dữ liệu để học |
| Test set | Dữ liệu để đánh giá |
| Loss | Mức sai cần tối ưu |
| Metric | Thước đo chất lượng |

## Metric

| Metric | Dùng cho | Ý nghĩa |
|---|---|---|
| Accuracy | Classification | Tỷ lệ đúng |
| Precision | Classification | Dự đoán positive có đáng tin không |
| Recall | Classification | Có bỏ sót positive không |
| F1 | Classification lệch nhãn | Cân bằng precision/recall |
| MSE | Regression | Phạt lỗi lớn mạnh |
| MAE | Regression | Sai số tuyệt đối trung bình |
| RMSE | Regression | Căn bậc hai của MSE |

## So sánh thuật toán

| Thuật toán | Loại bài toán | Điểm mạnh | Rủi ro |
|---|---|---|---|
| Linear Regression | Regression | Đơn giản, dễ giải thích | Kém với quan hệ phi tuyến mạnh |
| Logistic Regression | Classification | Baseline tốt | Cần feature phù hợp |
| KNN | Classification | Dễ hiểu | Chậm, nhạy scaling |
| Decision Tree | Classification/Regression | Dễ giải thích | Dễ overfit |
| Random Forest | Classification/Regression | Ổn định hơn tree đơn | Khó giải thích hơn |
| Naive Bayes | Classification | Tốt cho text baseline | Giả định độc lập |
| KMeans | Clustering | Đơn giản | Phải chọn k |
| SVM | Classification | Biên phân tách tốt | Nhạy tham số/scaling |

## 30 câu hỏi ôn thi

1. AI, ML, DL khác nhau thế nào?
2. Supervised learning cần dữ liệu gì?
3. Unsupervised learning dùng khi nào?
4. Regression là gì?
5. Classification là gì?
6. Clustering là gì?
7. Feature là gì?
8. Label là gì?
9. Vì sao cần train/test split?
10. Validation set dùng để làm gì?
11. Overfitting là gì?
12. Underfitting là gì?
13. Bias cao dẫn tới vấn đề gì?
14. Variance cao dẫn tới vấn đề gì?
15. Loss function dùng để làm gì?
16. Gradient descent có mục tiêu gì?
17. Learning rate quá cao gây gì?
18. Accuracy là gì?
19. Precision là gì?
20. Recall là gì?
21. F1 dùng khi nào?
22. Confusion matrix gồm gì?
23. MSE dùng cho bài toán nào?
24. KNN cần scaling vì sao?
25. Decision Tree dễ overfit vì sao?
26. Random Forest khác Decision Tree thế nào?
27. Logistic Regression dùng cho classification hay regression?
28. KMeans có cần label không?
29. Data leakage là gì?
30. Cross validation giúp gì?

## 10 mini case questions

1. Dataset bệnh hiếm, accuracy 99% nhưng model không phát hiện bệnh nào. Metric nào cần xem?
2. Dự đoán giá xe từ năm sản xuất và số km đã đi. Thuộc bài toán gì?
3. Nhóm khách hàng thành 4 nhóm không có nhãn. Dùng thuật toán nào?
4. Model train accuracy 99%, test accuracy 60%. Vấn đề gì?
5. Model train và test đều thấp. Vấn đề gì?
6. Feature có thang đo rất khác nhau, dùng KNN. Cần làm gì?
7. Muốn model dễ giải thích bằng luật if/else. Chọn thuật toán nào?
8. Muốn baseline classification đơn giản cho text. Có thể chọn gì?
9. Chỉ đánh giá trên train set có rủi ro gì?
10. Scale test set bằng `fit_transform` riêng có đúng không? Vì sao?

# Ôn nhanh Deep Learning

## Khái niệm cốt lõi

| Khái niệm | Ý nghĩa |
|---|---|
| Tensor | Mảng số nhiều chiều trong PyTorch |
| Neuron | Đơn vị tính toán cơ bản |
| Weight | Tham số học được |
| Bias | Hệ số lệch |
| Layer | Tầng biến đổi dữ liệu |
| Activation | Hàm phi tuyến |
| Loss | Sai số cần giảm |
| Optimizer | Cách cập nhật tham số |
| Epoch | Một lượt qua train set |
| Batch size | Số mẫu mỗi lần cập nhật |
| Learning rate | Độ lớn bước cập nhật |

## Bảng kiến trúc

| Kiến trúc | Phù hợp với | Ý tưởng chính |
|---|---|---|
| MLP/Dense | Dữ liệu bảng đơn giản | Nhiều fully-connected layers |
| CNN | Ảnh | Convolution học đặc trưng cục bộ |
| RNN/LSTM | Chuỗi | Ghi nhớ trạng thái theo thời gian |
| Transformer | Ngôn ngữ, chuỗi dài | Attention giữa các token |

## 30 câu hỏi ôn thi

1. Deep Learning khác ML truyền thống thế nào?
2. Neuron gồm những thành phần nào?
3. Weight dùng để làm gì?
4. Bias dùng để làm gì?
5. Activation function vì sao cần thiết?
6. ReLU có dạng trực giác ra sao?
7. Sigmoid đưa output về khoảng nào?
8. Softmax dùng khi nào?
9. Dense layer là gì?
10. Forward pass là gì?
11. Backpropagation là gì?
12. Gradient là gì ở mức trực giác?
13. Loss function dùng để làm gì?
14. Optimizer dùng để làm gì?
15. Epoch là gì?
16. Batch size là gì?
17. Learning rate là gì?
18. Learning rate quá cao gây gì?
19. Learning rate quá thấp gây gì?
20. CNN dùng cho dữ liệu nào?
21. RNN dùng cho dữ liệu nào?
22. LSTM cải thiện RNN ở điểm nào?
23. Transformer dùng attention để làm gì?
24. Overfitting trong DL biểu hiện thế nào?
25. Dropout giúp gì?
26. Early stopping là gì?
27. `model.train()` dùng khi nào?
28. `model.eval()` dùng khi nào?
29. `torch.no_grad()` dùng khi nào?
30. Vì sao DL thường cần nhiều dữ liệu?

## 10 câu hỏi đọc code

1. `nn.Linear(2, 4)` nghĩa là gì?
2. `model(X)` gọi hàm nào bên trong model?
3. `loss.item()` dùng để làm gì?
4. Vì sao cần `optimizer.zero_grad()`?
5. `loss.backward()` tạo ra gì?
6. `optimizer.step()` cập nhật gì?
7. Nếu `X.shape` là `[10, 2]`, batch size là bao nhiêu?
8. Khi evaluate, vì sao dùng `torch.no_grad()`?
9. Nếu output shape không khớp target shape, chuyện gì có thể xảy ra?
10. Save model bằng `state_dict` có ý nghĩa gì?

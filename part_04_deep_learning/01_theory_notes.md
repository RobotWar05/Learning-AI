# Ghi chú lý thuyết Deep Learning

## 1. Neuron model

Neuron nhận nhiều input, nhân với weight, cộng bias rồi đưa qua activation function. Ý tưởng cơ bản:

```text
output = activation(weight * input + bias)
```

## 2. Dense layer

Dense layer nối mỗi neuron của layer trước với neuron của layer sau. Trong PyTorch thường dùng `nn.Linear(input_dim, output_dim)`.

## 3. Activation functions

- ReLU: thường dùng ở hidden layers, đơn giản và hiệu quả.
- Sigmoid: đưa output về khoảng 0-1, hay dùng trong binary probability nhưng dễ bão hòa.
- Softmax: biến logits thành phân phối xác suất cho multi-class.

## 4. Loss functions

- MSE: dùng cho regression.
- Cross entropy: dùng cho classification.

Loss càng thấp thường nghĩa là model dự đoán gần target hơn, nhưng cần kiểm tra trên validation/test để tránh overfitting.

## 5. Gradient descent

Gradient descent cập nhật weight theo hướng giảm loss. Optimizer như SGD hoặc Adam là các cách cập nhật tham số.

## 6. Backpropagation

Backpropagation tính gradient của loss theo từng tham số trong mạng. Hiểu trực giác: model xem phần nào làm sai nhiều và điều chỉnh weight để giảm sai số.

## 7. Vì sao DL cần nhiều dữ liệu

Deep Learning có nhiều tham số. Nếu dữ liệu ít, model dễ học thuộc train set. Dữ liệu nhiều và đa dạng giúp model học pattern tổng quát hơn.

## 8. CNN cho ảnh

CNN dùng convolution để học đặc trưng cục bộ như cạnh, góc, texture. Phù hợp với ảnh vì ảnh có cấu trúc không gian.

## 9. RNN/LSTM cho chuỗi

RNN xử lý dữ liệu tuần tự. LSTM cải thiện khả năng ghi nhớ dài hơn RNN thường. Dùng trong chuỗi thời gian, văn bản ngắn, tín hiệu.

## 10. Transformer cho ngôn ngữ/LLM

Transformer dùng attention để học quan hệ giữa các token. Đây là nền tảng của nhiều mô hình ngôn ngữ lớn.

## 11. Overfitting trong DL

Dấu hiệu: train loss giảm tốt nhưng validation loss tăng hoặc accuracy validation kém.

Cách giảm:

- Dropout.
- Regularization.
- Early stopping.
- Data augmentation.
- Giảm độ phức tạp model.

## 12. Các tham số học cần nhớ

- Epoch: một lượt học qua toàn bộ train set.
- Batch size: số mẫu xử lý trong một lần cập nhật.
- Learning rate: độ lớn bước cập nhật tham số.

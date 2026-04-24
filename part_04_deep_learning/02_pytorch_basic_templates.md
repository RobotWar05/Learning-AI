# Giải thích template PyTorch cơ bản

## 1. Mục tiêu file code

File `02_pytorch_basic_templates.py` giúp bạn đọc hiểu cấu trúc tối thiểu của một chương trình PyTorch: tensor, model, forward, loss, optimizer, training loop và evaluation.

## 2. Tensor

```python
X = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
```

Tensor là cấu trúc dữ liệu chính trong PyTorch, tương tự array nhiều chiều nhưng hỗ trợ tính gradient và chạy trên GPU.

Lỗi hay gặp: shape của input không khớp với layer đầu tiên.

## 3. Model và `nn.Module`

```python
class SimpleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
```

Model PyTorch thường kế thừa `nn.Module`. Các layer được khai báo trong `__init__`, còn luồng tính toán được viết trong `forward`.

## 4. Forward

```python
def forward(self, inputs):
    hidden = self.relu(self.linear1(inputs))
    output = self.linear2(hidden)
    return output
```

Forward pass là bước dữ liệu đi từ input qua các layer để tạo prediction.

## 5. Loss

```python
loss_fn = nn.MSELoss()
loss = loss_fn(y_pred, y)
```

Loss đo sai số giữa dự đoán và target. Với classification nhiều lớp, thường dùng `nn.CrossEntropyLoss`.

## 6. Optimizer

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

Optimizer cập nhật weight dựa trên gradient.

## 7. Training loop

```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

- `zero_grad`: xóa gradient cũ.
- `backward`: tính gradient mới.
- `step`: cập nhật tham số.

## 8. Evaluation

```python
model.eval()
with torch.no_grad():
    predictions = model(X)
```

Khi evaluate, dùng `model.eval()` và `torch.no_grad()` để tắt các hành vi training và không lưu gradient.

## 9. Lỗi hay gặp

- Sai tensor shape.
- Quên `optimizer.zero_grad()`.
- Quên `loss.backward()`.
- Quên `optimizer.step()`.
- Không chuyển `model.train()` khi train.
- Không chuyển `model.eval()` khi evaluate.
- Không dùng `torch.no_grad()` trong evaluation.

## 10. Mini exercises

1. Đổi input dimension từ 2 thành 3 và sửa dữ liệu cho đúng.
2. Thêm một hidden layer.
3. Đổi optimizer từ SGD sang Adam.
4. Đổi số epoch từ 3 lên 10.
5. Giải thích từng dòng trong training loop.

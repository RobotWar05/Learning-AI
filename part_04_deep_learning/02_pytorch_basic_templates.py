"""Template PyTorch cơ bản cho ôn thi Deep Learning."""

import torch
from torch import nn


print("=== 1. Create tensor ===")
X = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
y = torch.tensor([[0.0], [1.0]])
print("X shape:", X.shape)
print("y shape:", y.shape)


print("\n=== 2. Simple nn.Module ===")
class SimpleClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(4, 1)

    def forward(self, inputs):
        hidden = self.relu(self.linear1(inputs))
        output = self.linear2(hidden)
        return output


model = SimpleClassifier()
print(model)


print("\n=== 3. nn.Sequential model ===")
sequential_model = nn.Sequential(
    nn.Linear(2, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
)
print(sequential_model)


print("\n=== 4. Loss function and optimizer ===")
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


print("\n=== 5. Training loop skeleton ===")
for epoch in range(3):
    model.train()

    y_pred = model(X)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch + 1}, loss = {loss.item():.4f}")


print("\n=== 6. Evaluation skeleton ===")
model.eval()
with torch.no_grad():
    predictions = model(X)
    eval_loss = loss_fn(predictions, y)
    print("Eval loss:", eval_loss.item())


print("\n=== 7. Save/load example - đang comment để không tạo file phụ ===")
# torch.save(model.state_dict(), "simple_model.pt")
# new_model = SimpleClassifier()
# new_model.load_state_dict(torch.load("simple_model.pt"))
# new_model.eval()

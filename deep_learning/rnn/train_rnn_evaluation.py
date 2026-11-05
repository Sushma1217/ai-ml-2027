import torch
import torch.nn as nn

torch.manual_seed(42)

starts = torch.arange(500, dtype=torch.float32)

sequences = torch.stack(
    [starts, starts + 1, starts + 2],
    dim=1
) / 500

targets = ((starts + 3) / 500).unsqueeze(1)

sequences = sequences.unsqueeze(-1)

# Split into training and testing data
X_train = sequences[:400]
y_train = targets[:400]

X_test = sequences[400:]
y_test = targets[400:]


print("Training input:", X_train.shape) #[:400] selects the first 400 examples.
print("Training targets:", y_train.shape)
print("Testing input:", X_test.shape) #[400:] selects the remaining 100 examples.
print("Testing targets:", y_test.shape)

# Build the RNN model
class NextValueRNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.rnn = nn.RNN(
            input_size=1,
            hidden_size=8,
            batch_first=True
        )

        self.output_layer = nn.Linear(8, 1)

    def forward(self, x):
        outputs, final_hidden = self.rnn(x)

        last_output = outputs[:, -1, :]

        prediction = self.output_layer(last_output)

        return prediction


model = NextValueRNN()
# Why reuse the same model?
# We want to understand the effect of separating training and testing data, not introduce a different architecture at the same time.

# Part C — Train only on training data

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(
    model.parameters(),lr=0.01
)

for epoch in range(100):
    optimizer.zero_grad()
    predictions = model(X_train)
    loss = loss_function(predictions,y_train)

    loss.backward()
    optimizer.step()
    if (epoch+1) % 20 == 0:
        print(f"Epoch {epoch+1}," f"loss {loss.item():.6f}")


# Part D — Evaluate on unseen data
model.eval()

with torch.no_grad():
    test_predictions = model(X_test)
    test_loss = loss_function(test_predictions,y_test)
    mae = torch.mean(torch.abs(test_predictions - y_test))
    mae_original_scale = mae.item() * 500
print("Test MSE:", test_loss.item())
print("Test MAE (normalized):", mae.item())
print("Test MAE (original scale):", mae_original_scale)

# Understand the new concepts:
# - torch.abs() calculates the absolute difference, ignoring whether the prediction is too high or too low.
# - torch.mean() calculates the average of those differences.
# - Multiplying MAE by 500 converts the error back to the original number scale.
# For example, an MAE of 0.004 in normalized values means an average error of 2 original units.

# Part E — Compare actual and predicted values
with torch.no_grad():
    for i in range(5):
        predicted = test_predictions[i].item()*500
        actual = y_test[i].item() *500
        print(f"Actual: {actual:.2f}, "f"Predicted: {predicted:.2f}")
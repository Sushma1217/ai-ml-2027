import torch
import torch.nn as nn


# 1. Define the model architecture
class SimpleNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2, 2)
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = torch.relu(x)

        x = self.output(x)
        x = torch.sigmoid(x)

        return x


# 2. Prepare the dataset
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0]
])


# 3. Create and train the model
model = SimpleNetwork()
loss_function = nn.BCELoss()
optimizer = torch.optim.SGD(
    model.parameters(), lr=0.1
)

for epoch in range(1000):
    predictions = model(X)
    loss = loss_function(predictions, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# 4. Save the trained parameters
torch.save(model.state_dict(), "and_model.pth")
print("model.state_dict()", model.state_dict())
print("Model saved")

# 5. Create a fresh model and load saved parameters
loaded_model = SimpleNetwork()
loaded_model.load_state_dict(torch.load("and_model.pth", weights_only=True))
loaded_model.eval()

# 6. Make predictions without gradient tracking
with torch.no_grad():
    predictions = loaded_model(X)

print("Loaded model predictions:")
print(predictions)

print("model predictions:")
print(model(X))

predicted_classes = (predictions>=0.5).float()
print("Predicted classes:")
print(predicted_classes)

# 7. Predict on a new input
new_input = torch.tensor([[1.0,1.0]])
with torch.no_grad():
    new_prediction =  loaded_model(new_input)
print("New input prediction:", new_prediction.item())
print("Predicted class:", int(new_prediction.item() >= 0.5))

# Questions
# Compare predictions from model and loaded_model on the same inputs. They should match closely.
# Yes they match 
#        [[0.0200],
#         [0.0201],
#         [0.0200],
#         [0.9879]],

# Change new_input to [[0.0, 0.0]] and check its prediction.
# 0.021 

# Temporarily skip the training loop and load the saved parameters into a fresh model.
#  Confirm that loading restores the learned behavior.
# yes tried

# Explain why the architecture must be recreated before loading its parameters.
# so the model follows same meachanism to learn the params like weights or biases
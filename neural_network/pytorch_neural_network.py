import torch
import torch.nn as nn


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


model = SimpleNetwork()

print(model) 
# o/p = (hidden): Linear(in_features=2, out_features=2, bias=True)
#       (output): Linear(in_features=2, out_features=1, bias=True)

# notes:
# nn.Linear(2, 2) =  2 inputs → 2 neurons
# nn.Linear(2, 1) = 2 hidden neurons → 1 output neuron

# Test the forward pass
X= torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])
predictions = model(X)
print("Predictions:")
print(predictions)


# Look at the parameters
for name, parameter in model.named_parameters():
    print(name)
    print(parameter)

# Add the loss function
# BCELoss is PyTorch's ready-made implementation of binary cross entropy.
loss_function = nn.BCELoss()

y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0]
])

predictions = model(X)
loss = loss_function(predictions, y)
print("Loss:", loss.item()) #.807


# Add the optimizer
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.1
)

# Train the network
for epoch in range(1000):
    predictions = model(X)
    loss = loss_function(predictions,y)
    optimizer.zero_grad() #PyTorch stores gradients, so we clear the previous ones before calculating new ones.
    loss.backward()
    optimizer.step() #PyTorch calculates gradients automatically.

    if epoch % 100 ==0:
        print( f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Check the final predictions
with torch.no_grad():
    predictions = model(X)
    print("Final predictions")
    print(predictions)

#  Convert predictions to 0/1
predicted_classes = (predictions >= 0.5).float()

print("Predicted classes:")
print(predicted_classes)
import torch 
import torch.nn as nn

# Generate sequential data
data = torch.sin(torch.arange(0, 100, 0.1))

# Create input sequences and targets
sequence_length = 20

X = []
y = []

for i in range(len(data) - sequence_length):
    X.append(data[i:i + sequence_length])
    y.append(data[i + sequence_length])

X = torch.stack(X).unsqueeze(-1)
y = torch.stack(y).unsqueeze(-1)

print("X shape:", X.shape)
print("y shape:", y.shape)

# Understand the code:
# - torch.sin() generates a repeating wave pattern.
# - sequence_length = 20 means each input contains 20 previous values.
# - X contains the input sequences.
# - y contains the next value we want to predict.
# - unsqueeze(-1) adds the feature dimension.

##############Split the dataset##################
split = int(len(X) * 0.8)

X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

print("Training:", X_train.shape, y_train.shape)
print("Testing:", X_test.shape, y_test.shape)

# Understand:
# - 80% data for training.
# - 20% data for testing.
# - We don't shuffle because we want to preserve chronological order.

#################Create the LSTM model###############
class LSTMPredictor(nn.Module):

    def __init__(self):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=1,
            hidden_size=16,
            batch_first=True
        )

        self.fc = nn.Linear(16, 1)

    def forward(self, x):

        outputs, (hidden, cell) = self.lstm(x)

        last_output = outputs[:, -1, :]

        prediction = self.fc(last_output)

        return prediction


model = LSTMPredictor()

print(model)

# Understand each component:
# Component	Purpose
# nn.LSTM	Learns patterns from sequential data
# input_size=1	One feature per time step
# hidden_size=16	Maintains 16 hidden features
# nn.Linear(16,1)	Converts 16 features into one prediction
# outputs[:, -1, :]	Selects the output from the last time step

# Important: We use the last time-step output to predict the next value.

############Train the model #############
criterion = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 100

for epoch in range(epochs):

    model.train()
    predictions = model(X_train)
    loss = criterion(predictions, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}")
#   What happens here?
# 1. Model receives 20 previous values.
# 2. LSTM processes the sequence.
# 3. Linear layer predicts the next value.
# 4. MSE calculates prediction error.
# 5. Backpropagation calculates gradients.
# 6. Adam updates the model weights.

################Evaluate and predict############
model.eval()

with torch.no_grad():
    predictions = model(X_test)
    test_loss = criterion(predictions, y_test)
    print("Test Loss:", test_loss.item())
    print("Actual values:", y_test[:5].squeeze())
    print("Predicted values:", predictions[:5].squeeze())
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

################Create the RNN model###############
class RNNPredictor(nn.Module):

    def __init__(self):
        super().__init__()

        self.rnn = nn.RNN(
            input_size=1,
            hidden_size=16,
            batch_first=True
        )

        self.fc = nn.Linear(16, 1)

    def forward(self, x):

        outputs, hidden = self.rnn(x)

        last_output = outputs[:, -1, :]

        prediction = self.fc(last_output)

        return prediction

#     Understand these two new things:
# 1. The RNN also returns outputs and hidden state.
# 2. The Linear layer converts the last RNN output into a numerical prediction.


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

# fc = fully connected (or dense) linear layer

##############Train both models################
def train_model(model, X_train, y_train):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001)
    for epoch in range(100):
        model.train()
        predictions = model(X_train)
        loss = criterion(predictions, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch+1}, Loss: {loss.item():.6f}")

    return model

########Now create and train both models:###############
rnn_model = RNNPredictor()
lstm_model = LSTMPredictor()

print("Training RNN")
rnn_model = train_model(rnn_model, X_train, y_train)

print("Training LSTM")
lstm_model = train_model(lstm_model, X_train, y_train)

################Compare test performance####################
criterion = nn.MSELoss()

rnn_model.eval()
lstm_model.eval()

with torch.no_grad():

    rnn_predictions = rnn_model(X_test)
    lstm_predictions = lstm_model(X_test)

    rnn_loss = criterion(rnn_predictions, y_test)
    lstm_loss = criterion(lstm_predictions, y_test)

print("RNN Test Loss:", rnn_loss.item())
print("LSTM Test Loss:", lstm_loss.item())

# Understand:
# - Lower MSE generally means better prediction accuracy on this test set.
# - Both models are evaluated using the same test data.
# - The result can vary because of random initialization and training
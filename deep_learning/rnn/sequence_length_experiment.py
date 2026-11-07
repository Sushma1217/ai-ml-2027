import torch
import torch.nn as nn

torch.manual_seed(42)

data = torch.sin(torch.arange(0, 100, 0.1))

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



################Part B — Create a reusable dataset function#########
def create_sequences(data,sequence_length):
    X=[]
    y=[]
    for i in range(len(data)-sequence_length):
        X.append(data[i:i +sequence_length])
        y.append(data[i+sequence_length])
    X= torch.stack(X).unsqueeze(-1)
    y= torch.stack(y).unsqueeze(-1)
    return X, y  

# Understand these important lines:
# - data[i:i + sequence_length]: selects the historical values.
# - data[i + sequence_length]: selects the next value to predict.
# - torch.stack(): combines the individual sequences into one tensor.
# - unsqueeze(-1): adds the feature dimension required by the RNN/LSTM.

##############Split the dataset##################
X,y = create_sequences(data, 5)
split = int(len(X) * 0.8) 
X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

##############Train both models################
def train_model(model, X_train, y_train):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001)
    for epoch in range(100):
        model.train()
        optimizer.zero_grad()
        predictions = model(X_train)
        loss = criterion(predictions, y_train)
        loss.backward()
        optimizer.step()
        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch+1}, Loss: {loss.item():.6f}")
    return model

###########create and train the model#############
lstm_model = LSTMPredictor()
rnn_model = RNNPredictor()
print("Training LSTM")
lstm_model = train_model(lstm_model, X_train, y_train)
rnn_model = train_model(rnn_model, X_train, y_train)

###########Calculate test MSE for both.################
criterion = nn.MSELoss()
rnn_model.eval()
lstm_model.eval()

with torch.no_grad():
    rnn_predictions = rnn_model(X_test)
    lstm_predictions = lstm_model(X_test)

    rnn_loss =criterion(rnn_predictions,y_test)
    lstm_loss =criterion(lstm_predictions,y_test)
print("RNN Test Loss:", rnn_loss.item())
print("LSTM Test Loss:", lstm_loss.item())


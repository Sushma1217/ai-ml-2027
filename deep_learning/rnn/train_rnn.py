import torch 
import torch.nn as nn

torch.manual_seed(42)

# Generate sequence starting points
starts = torch.arange(500, dtype=torch.float32)

# Create input sequences and next-value targets
sequences = torch.stack(
    [starts, starts + 1, starts + 2],
    dim=1
) / 500

targets = ((starts + 3) / 500).unsqueeze(1)

print("Input shape:", sequences.shape)
print("Target shape:", targets.shape)
print("First input:", sequences[0])
print("First target:", targets[0])

# Input shape: torch.Size([500, 3])
# Target shape: torch.Size([500, 1])

# Understand each part
# - torch.arange(500) creates numbers from 0 to 499.
# - torch.stack(..., dim=1) groups each starting value with its next two values into a sequence of length three.
# - Dividing by 500 scales the values to a smaller range. This can make neural-network training easier to manage.
# - unsqueeze(1) adds a dimension so each target is represented as one value per example.

sequences = sequences.unsqueeze(-1)
print("RNN input shape:", sequences.shape) # torch.Size([500, 3, 1])
# This represents 500 sequences, three time steps per sequence, and one feature at each step.

########## Build the RNN model#####################
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

predictions = model(sequences)

print("Prediction shape:", predictions.shape) #([500, 1])
# Understand the new code
# - hidden_size=8: the RNN maintains eight values in its hidden representation.
# - nn.Linear(8, 1): converts the eight hidden values into one numerical prediction.
# - outputs[:, -1, :]: selects the output at the final time step for every sequence.
# - return prediction: returns one predicted value per input sequence.

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.01)
loss = loss_function(predictions,targets)
print("Initial loss:", loss.item())

# - MSELoss() measures numerical prediction error.
# - Adam updates the model's trainable parameters.
# - lr=0.01 sets the learning rate for this small normalized example.
# The initial loss will vary depending on the model's initial weights.

# ############Train the RNN ####################
for epoch in range(100):
    optimizer.zero_grad()
    predictions = model(sequences)
    loss = loss_function(predictions, targets)

    loss.backward()
    optimizer.step()

    if(epoch+1) % 20 ==0:
        print(f"Epoch {epoch+1}," f"Loss:{loss.item():.6f}")

# What happens in each epoch?
# 1. Clear the previous gradients.
# 2. Pass the sequences through the RNN.
# 3. Calculate the difference between predictions and targets.
# 4. Calculate gradients with backpropagation.
# 5. Update the model's weights.
# An epoch here processes all 500 examples once. We use 100 epochs to give this small model enough opportunities to learn the simple pattern.

# Expected behavior: The loss should generally decrease from its initial value. It might not decrease smoothly at every epoch.


# Part 7 — Test a prediction
model.eval()
test_sequence = torch.tensor([[[100 / 500], [101 / 500], [102 / 500]]],
    dtype=torch.float32)
with torch.no_grad():
    prediction = model(test_sequence).item() #0.20171
print("Predicted next value:", prediction) #0.2017
print("Expected next value:", 103 / 500) # 0.206
print("Predicted original-scale value:", prediction * 500) # 100.859
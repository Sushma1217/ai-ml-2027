sequence = [10,20,30]
running_total = 0

for num in sequence:
    running_total +=num
    # print("Input:", num, "State:", running_total)
# Input: 10 State: 10
# Input: 20 State: 30
# Input: 30 State: 60

# nn.RNN is a PyTorch layer that processes a sequence one step at a time, updating its hidden state as it goes.

import torch
import torch.nn as nn

rnn = nn.RNN(input_size=1,hidden_size=2,batch_first=True)
sequence = torch.tensor(
    [[[10.0], [20.0], [30.0]]]
)
outputs, final_hidden = rnn(sequence)
print("Input shape:", sequence.shape)
print("Outputs shape:", outputs.shape)
print("Final hidden shape:", final_hidden.shape)

# Understand every parameter
# - input_size=1: each time step contains one number.
# - hidden_size=4: the RNN keeps four numbers in its hidden state.
# - batch_first=True: arrange the input as [batch, sequence length, features].
# - sequence: one sequence, three time steps, one feature per step.
# The input shape is [1, 3, 1]:
# - 1 sequence in the batch.
# - 3 time steps.
# - 1 feature per step.

#  output shapes:
# Input shape: torch.Size([1, 3, 1])
# Outputs shape: torch.Size([1, 3, 4])
# Final hidden shape: torch.Size([1, 1, 4])

# Why four values at each step? Because we selected hidden_size=4. The RNN produces one four-value hidden representation for each of the three steps.

# The final hidden state has shape [layers, batch, hidden size]. We used one RNN layer, one sequence, and four hidden values.

# Experiment: Change hidden_size=4 to hidden_size=2. Predict the new output shapes before running the code.
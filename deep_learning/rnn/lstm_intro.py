import torch 
import torch.nn as nn 

# Batch size = 1
# Sequence length = 3
# Features per time step = 1
# Last 1 (Features per time step): How many numbers represent each individual step. At step 1, you only have a single value (10.0), so the feature size is 1.
sequence = torch.tensor([[10.0],[20.0],[30.0]])
print("Input shape:", sequence.shape)

# Part B — Create the LSTM
lstm = nn.LSTM(input_size=1,hidden_size=4,batch_first=True)
# input_size=1: One feature at each time step.
#Each individual time step in your sequence consists of a single value or feature

# hidden_size=4: Four hidden units.
# The LSTM's internal memory capacity. Every time step processes the input and 
# updates a hidden state vector of size 4 (meaning the model extracts 4 features worth of internal context).
# batch_first=True: Input shape starts with batch size.
# Tells PyTorch that your input tensor will be structured as [Batch_Size, Sequence_Length, Features].

outputs, (hidden_state, cell_state) = lstm(sequence)

print("Outputs:", outputs.shape) #torch.Size([1, 3, 4])
print("Hidden state:", hidden_state.shape) #torch.Size([1, 1, 4])
print("Cell state:", cell_state.shape) #torch.Size([1, 1, 4])

# This is the most important difference to understand:
# - outputs: Output at every time step.
# - hidden_state: Final hidden representation.
# - cell_state: Final memory carried by the LSTM.

# Part D — Compare RNN and LSTM outputs
rnn = nn.RNN(input_size=1,hidden_size=4,batch_first=True)

outputs, final_hidden = rnn(sequence)
print("Input shape rnn:", sequence.shape) # ([1, 3, 1])
print("Outputs shape rnn:", outputs.shape) # ([1, 3, 4])
print("Final hidden shape rnn:", final_hidden.shape) #([1, 1, 4]) [Num_Layers * Directions, Batch_Size, Hidden_Size]

# comparison 
# features RNN                      lstm
#  Input shape  ([1, 3, 1])        ([1,3, 1])
# Outputs shape  ([1, 3, 4])        ([1, 3, 4])
# Final hidden shape  ([1, 1, 4])   torch.Size([1, 1, 4])
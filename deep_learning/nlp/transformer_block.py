import torch 
import torch.nn as nn

# Step 1: Create sample input
# Batch size = 1, sequence length = 4, embedding dimension = 8
input_tensor = torch.rand(1,4,8)

# Step 2: Create a Transformer encoder layer
transformer_layer = nn.TransformerEncoderLayer(d_model=8,nhead=2,dim_feedforward=32,dropout=0.0,batch_first=True)

# Step 3: Pass input through the Transformer layer
output = transformer_layer(input_tensor)
print("Input shape:", input_tensor.shape)
print("Output shape:", output.shape)

# Understand these parameters:
# - d_model=8: each token has 8 features.
# - nhead=2: use two attention heads.
# - dim_feedforward=32: the hidden layer inside the feed-forward network has 32 dimensions.
# - batch_first=True: input follows [batch, sequence, embedding].


# Input shape: torch.Size([1, 4, 8])
# Output shape: torch.Size([1, 4, 8])

# Notice that the output shape stays the same. The Transformer changes the representations, not the number of tokens or their embedding dimensions.


# Step 4: Create a causal mask
sequence_length = 4
causal_mask = torch.triu(torch.ones(sequence_length,sequence_length),diagonal=1).bool()
print("Causal mask:",causal_mask)

# Step 5: Pass input with causal mask
masked_output = transformer_layer(input_tensor,src_mask=causal_mask)
print("Masked output shape:", masked_output.shape)

# Understand the mask:
# - torch.ones(4, 4) creates a 4 × 4 matrix.
# - torch.triu(..., diagonal=1) keeps the values above the diagonal.
# - .bool() converts the matrix to Boolean values.
# - In PyTorch's Boolean attention mask, True means that position is blocked.

# Important distinction: This is a causal mask applied to an encoder layer for learning purposes. 
# GPT uses decoder-style Transformer blocks with causal self-attention. 
# An encoder layer by itself is not a complete GPT model.
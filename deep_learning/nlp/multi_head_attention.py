import torch
import torch.nn as nn

# Step 2 — Create sample input

# Batch size = 1
# Sequence length = 3
# Embedding dimension = 8
input_tensor = torch.rand(1,3,8)
print("Input shape:", input_tensor.shape)

# The dimensions mean:
# - 1: one sentence (batch)
# - 3: three tokens
# - 8: eight numbers per token

# Step 3 — Create multi-head attention
attention = nn.MultiheadAttention(embed_dim=8,num_heads=2,batch_first=True)

# Explanation:
# - embed_dim=8: each token has eight dimensions.
# - num_heads=2: we use two attention heads.
# - batch_first=True: input shape follows batch, sequence, embedding order.

# note: The embedding dimension must be divisible by the number of heads. Here, each head works with four dimensions.


# Step 4 — Run attention
output, weights = attention(input_tensor,input_tensor,input_tensor)
# We pass the same input as Query, Key and Value because this is self-attention.

print("Output shape:", output.shape)
print("Attention weights shape:", weights.shape)

# By default, PyTorch averages attention weights across heads. You can request individual head weights with average_attn_weights=False as an additional experiment.


#######################POSITIONAL ENCODING#########################
token_embedding = torch.rand(1,4,8)
print("Token embedding shape:", token_embedding.shape)

# We have four tokens, each represented by eight numbers.

position_embedding = nn.Embedding(num_embeddings=10,embedding_dim=8)
positions = torch.arange(4)
position_vectors = position_embedding(positions)
print("Position vectors shape:", position_vectors.shape)

# nn.Embedding learns a vector for each position.
# torch.arange(4) creates position IDs [0, 1, 2, 3].

# Step 3 — Combine both embeddings
position_vectors = position_vectors.unsqueeze(0)
final_embeddings = token_embedding + position_vectors
print("Final embedding shape:", final_embeddings.shape)



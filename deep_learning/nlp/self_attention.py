import numpy as np

# Three tokens represented by two-dimensional vectors
tokens = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0]
])

print("Token representations:",tokens)


# Step 2 — Create Query, Key and Value
Q = tokens
K = tokens
V = tokens

print("Query:")
print(Q)

print("Key:")
print(K)

print("Value:")
print(V)

# Why are we assigning the same values?
# For this simplified exercise, we are using the token representations directly as Q, K and V.
# In a real Transformer, separate learned weight matrices transform the token representations into Query, Key and Value vectors.


# Step 3 — Calculate attention scores
scores = np.matmul(Q, K.T) #matrix multiplication
#K.T transposes the Key matrix.

# Step 4 — Apply scaling and softmax

# First, scale the scores:

d_k = K.shape[1]
scaled_scores = scores/np.sqrt(d_k)

# Why divide by the square root of d_k?
# When vector dimensions become large, dot-product scores can become large too. Scaling helps keep these scores in a manageable range before applying softmax.

# Now apply softmax:
def softmax(x):
    exp_values = np.exp(x-np.max(x, axis=-1,keepdims=True))
    return exp_values / np.sum(exp_values, axis=-1, keepdims=True)

attention_weights = softmax(scaled_scores)
print("Attention weights:",attention_weights)

# Softmax converts scores into weights that add up to 1 across each row.

# Step 5 — Calculate the final attention output
attention_output = np.matmul(attention_weights,V)
print("Attention output:",attention_output)


# What should you understand from this experiment?
# - The model calculates relationships between tokens.
# - Softmax turns scores into attention weights.
# - The weights determine how much each token's Value contributes to the output.
# - The output contains information combined from multiple tokens.
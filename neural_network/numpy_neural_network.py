import numpy as np

# X = np.array([
# [0, 0],
# [0, 1],
# [1, 0],
# [1, 1]
# ])

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 3]
])

# Notice that X is now a matrix, not a list of individual inputs.


y = np.array([0, 0, 0, 1])

print(X.shape) #(4, 2)
# 4 training examples, 2 features per example

# Create the hidden-layer weights
# 2 input features
#         ↓
# 2 hidden neurons

weights_hidden = np.array([
    [0.5, 0.4],
    [0.2, 0.7]
])

bias_hidden = np.array([0.1, 0.2])

print(weights_hidden.shape) #(2, 2)
print(bias_hidden.shape) #(2,)

# Calculate the hidden layer
z_hidden = np.dot(X, weights_hidden.T) + bias_hidden

# .T means transpose.

# It changes:

# 2 × 2

# into:

# 2 × 2

# In this particular example the dimensions look the same, but the orientation of rows and columns changes.

# For now, remember:

# We transpose the weight matrix so that the dimensions line up correctly for this multiplication.

##### Apply Relu
def relu(z):
    return np.maximum(0,z)

hidden_output = relu(z_hidden)
print(hidden_output)

weights_output = np.array([0.6, 0.3])
bias_output = 0.1
z_output = np.dot(hidden_output, weights_output) + bias_output

# sigmod
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# prediction
prediction = sigmoid(z_output)
print("prediction",prediction)

print("X:", X.shape) #(5,2)- for more records
print("weights_hidden:", weights_hidden.shape)
print("bias_hidden:", bias_hidden.shape)
print("z_hidden:", z_hidden.shape)
print("hidden_output:", hidden_output.shape)
print("weights_output:", weights_output.shape)
print("prediction:", prediction.shape) # for more records (5,)


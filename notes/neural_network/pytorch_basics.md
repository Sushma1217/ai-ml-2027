<!-- # What is a Tensor?
# For now, think of a tensor as PyTorch's version of an array, capable of representing scalars, vectors, matrices, and higher-dimensional data.
# You've already worked with:
# NumPy array
#    ↓
# vector
#    ↓
# matrix

# PyTorch uses:
# Tensor
# for these.
 -->

NumPy:
np.array()

PyTorch:
torch.tensor()

NumPy:
np.dot(x, w)

PyTorch:
torch.dot(x, w)

np.dot(X, weights.T) + bias
torch.matmul(...)

np.maximum(0, z)
torch.relu(z)

Your NumPy:
1 / (1 + np.exp(-z))

PyTorch:
torch.sigmoid(z)

loss.backward() is not gradient descent.
It performs the backward pass and calculates gradients.

Tensor
PyTorch's fundamental data structure for numerical/deep-learning computation.
Automatic differentiation
PyTorch tracks operations and calculates gradients automatically.
requires_grad=True
Tells PyTorch to track operations needed to calculate gradients for that tensor.
.backward()
Calculates gradients by propagating backward from the loss.
.grad
Contains the calculated gradient for a tensor being tracked.

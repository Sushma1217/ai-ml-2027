import torch 

x = torch.tensor([2.0,3.0])
print(x)
print(x.shape)

x = torch.tensor([2.0, 3.0])
w = torch.tensor([0.5, 0.4])

z = torch.dot(x, w)

print(z) 


X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

weights = torch.tensor([
    [0.5, 0.4],
    [0.2, 0.7]
])

bias = torch.tensor([0.1, 0.2])

z= torch.matmul(X, weights.T) + bias
print(z)
print(z.shape)


# PyTorch already provides activation functions.
relu_output = torch.relu(z)
print(relu_output)

sigmoid_output = torch.sigmoid(z)
print(sigmoid_output)

# gradient 
# w = torch.tensor(0.5,requires_grad=True)
# "Keep track of the calculations involving this value because I may want the gradient later.
# calculating gradient manually using numpy

# Let PyTorch calculate a gradient
w= torch.tensor(0.2, requires_grad=True)
target = torch.tensor(1.0)
loss = (w - target) ** 2
print("Loss:", loss)
loss.backward()

print("Gradient:", w.grad)

# You just did the equivalent of manually calculating the gradient from your Day 32 exercise.
# But instead of writing:
# gradient = 2 * (weight - target)

# you told PyTorch: loss.backward()
# loss.backward() is not gradient descent.
# It performs the backward pass and calculates gradients.

gradient = 2 * (0.5 - 1) 
print(gradient) #-1.0
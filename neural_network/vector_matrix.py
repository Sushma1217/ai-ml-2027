import numpy as np

# x= np.array([2,3]) 2.3
# Exercise 1
x = np.array([4, 5]) #4.1

w = np.array([0.5,0.4])
b = 0.1

z = np.dot(x,w)+b

print("z:", z)

# Multiple neurons
# weights = np.array([
#     [0.5, 0.4],
#     [0.2, 0.7]
# ]) #z1 [2.2 2.5]

weights = np.array([
    [0.8, 0.2],
    [0.1, 0.9]
]) # z2 [4.3 5.1]

# Now conceptually: this is the matrix

#              x1     x2

# Neuron 1    0.5    0.4
# Neuron 2    0.2    0.7

# Understand the shape
print(weights.shape) #(2,2) which means 2 neurons, 2 weights per neuron

# Calculate both neurons together
#              x
#              ↓
#        ┌─────────────┐
#        │ 0.5   0.4   │ → neuron 1
# W  =   │             │
#        │ 0.2   0.7   │ → neuron 2
#        └─────────────┘
#              ↓
#        [z1, z2]
# z1 = np.dot(weights,x)


# Then add biases:
bias = np.array([0.1, 0.2])
z2 = np.dot(weights, x) + bias
print(z2) #------------final

# Apply activation to both neurons
def relu(x):
  return np.maximum(0, z)
a= relu(z2)
print(a)

# Exercise 4 Print:
print(x.shape)
print(weights.shape)
print(bias.shape)
print(z2.shape)

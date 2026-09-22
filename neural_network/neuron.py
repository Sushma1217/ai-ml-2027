import numpy as np

# Create two inputs- These are simply the inputs to our neuron.
x1=2
x2=3

# Create two weights
w1 = .5
w2 = .8

# Create a bias
b = .2

# Calculate z
z = x1*w1 + x2*w2 + b
print(z) #3.600

# sigmord function
def sigmod(z):
 return 1/ (1 + np.exp(-z))
print("Neuron output = ", sigmod(z)) # 0.973

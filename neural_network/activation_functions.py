import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

print(sigmoid(-5))
print(sigmoid(-1))
print(sigmoid(0))
print(sigmoid(1))
print(sigmoid(5))

# Implement ReLU
def relu(z):
    return max(0,z)
print(relu(-5))
print(relu(-1))
print(relu(0))
print(relu(1))
print(relu(5))

# Compare Sigmoid and ReLU
values = [-5, -2, -1, 0, 1, 2, 5]
for value in values:
    print(value, sigmoid(value), relu(value))

# demonstrate why nonlinearity matters
def linear(z):
    return z
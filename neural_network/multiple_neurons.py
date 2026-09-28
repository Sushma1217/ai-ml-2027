import math


# Both neurons receive the same inputs, but they have different weights.

x1 = 2.0
x2 = 3.0

# Neuron 1
w1_1 = 0.5
w1_2 = 0.4
b1 = 0.1

# Neuron 2
w2_1 = 0.2
w2_2 = 0.7
b2 = 0.2

# weighted sum
# Neuron 1:
z1 = x1 * w1_1 + x2 * w1_2 + b1

# Neuron 2:
z2 = x1 * w2_1 + x2 * w2_2 + b2

# apply sigmod
output1 = 1/(1+math.exp(z1))
output2 = 1/(1+math.exp(z2))
print("Neuron 1:", output1)
print("Neuron 2:", output2)


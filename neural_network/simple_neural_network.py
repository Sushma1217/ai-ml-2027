import math
from activation_functions import sigmoid, relu

X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y = [0, 0, 0, 1]  # all actual answers
w1 = [0.5, 0.4]
b1 = 0.1

w2 = [0.2, 0.7]
b2 = 0.2

# outout weights
w_out = [0.6, 0.3]
b_out = 0.1


# Forward pass
def forward(x):
    z1 = x[0] * w1[0] + x[1] * w1[1] + b1
    a1 =  relu(z1)
    z2 = x[0] * w2[0] + x[1] * w2[1] + b2
    a2 = relu(z2)
    z_out = a1 * w_out[0] + a2 * w_out[1] + b_out
    prediction = sigmoid(z_out)
    return prediction

# Test the forward pass
# Test the forward pass + calculate loss
for i in range(len(X)):
    prediction = forward(X[i])
    y_true = y[i] # current actual answer
    loss = -(
        y_true * math.log(prediction + 1e-8)
        + (1 - y_true) * math.log(1 - prediction + 1e-8)
    )
    print(X[i], prediction, y_true, loss)
# X[i]        → input
# forward()   → prediction
# y[i]        → actual answer
# prediction + y[i] → loss

# Track the loss
epochs = 1000

if epoch % 100==0:
    print(epoch, loss)
import numpy as np

X = np.array([
[0, 0],
[0, 1],
[1, 0],
[1, 1]
])

y = np.array([0, 0, 0, 1])


weights_hidden = np.array([
    [0.5, 0.4],
    [0.2, 0.7]
])

bias_hidden = np.array([0.1, 0.2])
# weights_output = np.array([0.6, 0.3])
#weights_output = np.array([0.9, 0.1])
weights_output = np.array([0.1, 0.9])
bias_output = 0.1

def relu(z):
    return np.maximum(0,z)

# sigmod
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def forward_pass():
 z_hidden = np.dot(X, weights_hidden.T) + bias_hidden
 hidden_output = relu(z_hidden)
 z_output = np.dot(hidden_output, weights_output) + bias_output
 prediction = sigmoid(z_output)
 return prediction, hidden_output, z_hidden

# Add Binary Cross Entropy
def binary_cross_entropy(y_true, prediction):
    return -np.mean(
        y_true * np.log(prediction + 1e-8)
        + (1 - y_true) * np.log(1 - prediction + 1e-8)
    )

prediction, hidden_output, z_hidden= forward_pass()
loss = binary_cross_entropy(y, prediction) 

# for weights_output = np.array([0.6, 0.3])
# print("Prediction:", prediction) #Prediction: [0.55477924 0.66150316 0.64106741 0.7369159 ]
# print("Loss:", loss)# 0.8055

# for weights_output = np.array([0.9, 0.1])
print("Prediction:", prediction)# Prediction: [0.55230791 0.65475346 0.6637387  0.75212911]
print("Loss:", loss)# 0.810

# for weights_output = np.array([0.1, 0.9])
print("Prediction:", prediction)# [0.57199613 0.72312181 0.62714777 0.76674106]
print("Loss:", loss)# 0.846

# Changing the weights changes the predictions, which changes the loss.



# updating weights
learning_rate = 0.5
epochs = 1000

# relu_derivative = (z_hidden > 0).astype(float) 
# the above line means z > 0  → 1 z <= 0 → 0
# This tells backpropagation:
# "If this neuron was active, allow the gradient through; otherwise, block it.

# Build the training loop 
# we must use range because epochs is just the number 1000. Use:

for epoch in range(epochs): 
        # 1. Forward pass
        prediction, hidden_output,z_hidden = forward_pass()
        # 2. Calculate loss
        loss = binary_cross_entropy(y, prediction)

        # 3. Calculate gradients for outer layer

        N = X.shape[0]

        # Output layer
        dz_output = (prediction - y) / N

        dw_output = np.dot(hidden_output.T, dz_output)
        db_output = np.sum(dz_output)

        # Hidden layer
        relu_derivative = (z_hidden > 0).astype(float)

        dz_hidden = np.outer(dz_output, weights_output) * relu_derivative

        dw_hidden = np.dot(dz_hidden.T, X)
        db_hidden = np.sum(dz_hidden, axis=0)

          # 4. Update weights
        weights_output -= learning_rate * dw_output
        bias_output -= learning_rate * db_output

        weights_hidden -= learning_rate * dw_hidden
        bias_hidden -= learning_rate * db_hidden

        # 5. Print loss
        if epoch % 100 == 0:
            print("Epoch:", epoch, "Loss:", loss)
prediction, _, _ = forward_pass()
print("Final predictions:", prediction) # [0.01932756 0.0193992  0.01938057 0.98836246]
print("Actual:", y)        #Actual: [0 0 0 1]
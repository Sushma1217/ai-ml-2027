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
 return prediction, hidden_output

# Add Binary Cross Entropy
def binary_cross_entropy(y_true, prediction):
    return -np.mean(
        y_true * np.log(prediction + 1e-8)
        + (1 - y_true) * np.log(1 - prediction + 1e-8)
    )

prediction, hidden_output= forward_pass()
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


#How do we calculate the gradient for: weights_output bias_output
# Number of samples
N = X.shape[0]

# Output Layer Gradients
dz_output = (prediction-y)/N 
dw_output = np.dot(hidden_output.T, dz_output)  # Shape: (2,)
db_output = np.sum(dz_output)  # Scalar

# Hidden Layer Gradients (Backpropagation)
dz_hidden = np.outer(dz_output, weights_output) * hidden_output  # Shape: (4, 2)
dw_hidden = np.dot(dz_hidden.T, X)  # Shape: (2, 2)
db_hidden = np.sum(dz_hidden, axis=0)  # Shape: (2,)
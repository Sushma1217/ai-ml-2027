Why this architecture?

We're deliberately using:

ReLU in the hidden layer → learns nonlinear patterns
Sigmoid in the output layer → gives a 0–1 output for binary classification

This is a very common basic neural-network structure.

Training loop

A neural network doesn't learn from one calculation.

It repeatedly does:

Forward pass
↓
Calculate loss
↓
Backpropagation
↓
Calculate gradients
↓
Update weights
↓
Repeat

This repeated process is called the training loop.

# Epoch

An epoch is one complete cycle where a machine learning model sees, analyzes, and learns from every single example in your training dataset.

Example: If your dataset contains 1,000 images, training the model for 1 epoch means it has processed all 1,000 images once. If you train it for 10 epochs, it will cycle through all 1,000 images ten times.

                 FORWARD PASS
                     ↓

Input
↓
Weighted sum
↓
ReLU
↓
Hidden layer
↓
Output neuron
↓
Sigmoid
↓
Prediction
↓
Loss
↓
BACKPROPAGATION
↓
Gradients
↓
GRADIENT DESCENT
↓
Updated weights
↓
Repeat

This is the core neural-network training cycle.

forwrd pass
A forward pass (also called forward propagation) is the process where input data flows through a neural network from the input layer to the output layer to generate a prediction.

4. Learning rate
   Controls how large each weight update is.

5. Parameters

Weights and biases that the network learns.

# interview questions

Q1. What is a forward pass?
it is the process where the data passes through input data flows through a neural network of input layer to output to generate a prediction.

Q2. What happens during backpropagation?
Backpropagation calculates the gradients of the loss with respect to the network's weights and biases by propagating the error backward through the network. Gradient descent then uses those gradients to update the weights and biases to reduce the loss.

What does gradient descent do?
gradient descent uses the gradients to update the weights to minimal the loss

What is an epoch?
one complete pass through of training data

What is the difference between a parameter and a hyperparameter?
params- weights or bias that nueral network learns
hyperparams are the addition configuration or setting that we provide for learning rate, number of epochs, and number of hidden neurons etc to control the model performance

Why are we using ReLU in the hidden layer and sigmoid in the output layer?
relu is a considerably a better for learning non-linearnity and computationally efficient and sigmod is the simple one and can be the probability between 0-1 which is useful for making prediction

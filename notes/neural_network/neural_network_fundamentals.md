                  NEURAL NETWORK

Input Layer Hidden Layer Output Layer

x1 ───────────┐
│ ┌─────────┐
x2 ───────────┼──────→│ Neuron 1│──┐
│ └─────────┘ │
│ │
│ ┌─────────┐ │ ┌──────────┐
└──────→│ Neuron 2│──┼─────→│ Output │
└─────────┘ │ │ Neuron │
│ └────┬─────┘
│ │
│ Sigmoid
│ ↓
│ Prediction
│ ↓
└────────→ Loss
↓
Backpropagation
↓
Gradients
↓
Gradient Descent
↓
Updated Weights

Q1. What happens during the forward pass?
it is the process where input flows through the input payer to output layer and generate the prediction in neural network

Q2. Why do we need weights?
it the parameter that indicates how a particular input feature impact or influence the output prediction.
higher weight - pushes prediction higher
lesser weight - lowers the prediciton influence

Q3. Why do we need bias?
Bias is basically an additional value that lets the neuron shift its output.
it is the value or constant number which helps the model to predic when all the input feature is 0 rather making prediction 0. shifts the prediction up or down to fit in the model.

example
Imagine a loan approval model: if your income and credit score are both zero, the model still needs a baseline starting point—like a minimum risk score—to make a fair decision rather than automatically outputting zero.

Q4. Why do we need activation functions?
activation function takes weighted sum(z) and transform it before passing the result forward. without this a model will stack to linearity, limiting its learning network. activation function introduces the non linearility

Q5. What does loss tell us
it tells us how wrong the model prediction compared to actual.

Q6. What does backpropagation do?
it is the process in which we aim to minimize the loss by adjusting weights using the calculated gradients by moving in a backward way.
Backpropagation calculates gradients; it doesn't itself adjust the weights. Gradient descent performs the update.

Q7. What does gradient descent do?
it uses the gradients calcuated using backpropogation and updates the weights to minimize the loss.

Q8. What is an epoch?
it is one complete passthough of a every single example in training dataset.
for ex: epochs = 1000. in 1 epoch model process all 1000 records.

Q9. What happens if learning rate is too small?
model takes small steps to reach the minimum, weights are updated with tiny value.

"Reaching the minimum" means finding the exact point where the loss is as low as it can possibly get.

Q10. What happens if learning rate is larger?
model takes a larger learning rate takes larger update steps.
Note:A larger learning rate isn't automatically better. If it is too large, training can overshoot or become unstable.

| Concept          | What it does                                            |
| ---------------- | ------------------------------------------------------- |
| Weight           | Controls how strongly an input influences a neuron      |
| Bias             | Shifts the neuron's calculation                         |
| Activation       | Adds nonlinearity                                       |
| Prediction       | Model's output                                          |
| Loss             | Measures prediction error                               |
| Backpropagation  | Calculates gradients                                    |
| Gradient         | Direction/magnitude information for changing parameters |
| Gradient descent | Uses gradients to update parameters                     |
| Epoch            | One complete pass through the training data             |
| Learning rate    | Controls size of weight updates                         |

Part 5 — Connect NumPy to your earlier Logistic Regression
This is important for your interview preparation.
You previously built:
Logistic Regression
↓
weights
↓
weighted sum
↓
sigmoid
↓
prediction
↓
loss
↓
optimization

Your neural network now does:
Neural Network
↓
weights
↓
weighted sums
↓
ReLU
↓
more weighted sums
↓
sigmoid
↓
prediction
↓
loss
↓
backpropagation
↓
gradient descent

Write this comparison in your notes.
The key insight
A neural network is not completely unrelated to Logistic Regression. A single sigmoid neuron is closely related to logistic regression; neural networks extend this idea with multiple neurons and layers plus nonlinear activations.

# activation function?

An activation function takes the neuron's weighted sum z and transforms it before passing the result forward.
z can be any number, The activation function transforms this value.

Sigmoid is useful when we want an output that behaves like a probability for binary classification.
transforms the value(z value) between 0 to 1
we already saw this in your Logistic Regression project.

Don't say it is a probability. Say it produces a value between 0 and 1 that can be interpreted as a probability-like output for binary classification, depending on the model/calibration.

Activation functions introduce nonlinearity into neural networks. Without nonlinear activations, stacking multiple linear layers would still result in a linear function, limiting what the network can learn.

Sigmoid- Binary classification output
Will customer churn?
Yes / No

ReLU- Hidden layers
because it introduces nonlinearity while being simple and computationally efficient.

Softmax- Multi-class classification
for ex: Cat, Dog, Horse

|   z | Sigmoid | ReLU |
| --: | ------: | ---: |
|  -5 |  0.0066 |    0 |
|  -2 |   0.119 |    0 |
|  -1 |    0.26 |    0 |
|   0 |     0.5 |    0 |
|   1 |     0.7 |    1 |
|   2 |    0.88 |    2 |
|   5 |   0.993 |    5 |

Q1. Why does sigmoid always produce a value between 0 and 1?
because of its formula

Q2. What does ReLU do with negative values?
it produces 0 as the relu returns the max values between 0 and z.

Q3.Why do neural networks need nonlinear activation functions?
because in the real word, data is messy and has many features affecting the prediction so we need nonlinear activation functions to understand the complex pattern , not limiting their learning

Q4. Why is sigmoid commonly used for binary classification?
it produces the output between 0 to 1 so by looking at the values we can make the prediction between two class thats why it is used for binary classification

Q5. Why might ReLU be used in hidden layers?
because it introduces nonlinearity while being simple and computationally efficient.

Why are activation functions needed in neural networks?
Activation functions introduce nonlinearity into the network. Without them, even multiple stacked linear layers would behave like a linear model and wouldn't be able to learn complex nonlinear patterns.

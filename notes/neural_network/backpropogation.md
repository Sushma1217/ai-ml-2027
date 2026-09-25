# backpropagation

Backpropagation is the process of working backward from the loss to calculate how much each weight contributed to the error.
Input
↓
Weights
↓
Prediction
↓
Loss
↓
BACKPROPAGATION
↓
Gradients for each weight
↓
GRADIENT DESCENT
↓
Updated weights

So remember this distinction:

Backpropagation calculates the gradients.
Gradient descent uses those gradients to update the weights.

This distinction is very important for interviews.

# Chain rule

Chain rule = break a complicated dependency into smaller steps and combine their effects.

Chain Rule is a calculus rule used to find the rate of change of connected (nested) functions by multiplying their individual rates of change together.

How does w1 affect z?
↓
How does z affect prediction?
↓
How does prediction affect loss?
↓
Combine them
↓
gradient_w1

# derivative

determines how much a loss function changes when we make the tiny adjustment in the weights

# gradient

A gradient is simply a list or collection of derivatives when you have more than one variable.

Why sigmoid derivative is: prediction × (1 - prediction)
because applying calculus rules (the quotient or chain rule) to the original sigmoid formula neatly simplifies into that exact algebraic form.(ggogle answer)

# What's the difference between backpropagation and gradient descent?

Backpropagation calculates the gradients of the loss with respect to the model's weights by propagating the error backward through the network. Gradient descent uses those gradients to update the weights and reduce the loss.

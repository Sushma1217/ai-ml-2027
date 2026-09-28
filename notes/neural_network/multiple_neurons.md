Important idea:

Both neurons see the same inputs, but because they have different weights and biases, they can learn different patterns.

That is the beginning of a hidden layer.

# hidden layer

A hidden layer allows the network to learn multiple patterns from the input instead of trying to solve everything with one neuron.

Why don't we simply use one neuron? Why might two neurons be able to learn something that one neuron cannot?
single neron can work only with linear problems and fails to understand and solve non liner problems.

# network

Input layer | Hidder layer | Outputlayer
x1 ───────────→ [Neuron 1] ──────┐│
├──→ [Output]
│
x2 ───────────→ [Neuron 2] ──────┘

Input layer
Contains the original input features

Hidden layer
Contains neurons that transforms the input and learn patterns

output layer
produces the final prediction

Activation function
An activation function is applied to the weighted sum of inputs before producing the final output of a neuron. It introduces non-linearity, allowing the network to learn complex patterns.
ex: sigmod

Each neuron can learn a different combination/pattern from the same inputs.

This is why increasing the network's capacity from one neuron to multiple neurons matters.

5. Why multiple neurons?
   Different neurons can learn different patterns from the same input because they have different weights and biases.

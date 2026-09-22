What is a neuron?
its the unit that consist of inconnected layers learns the complex pattern by taking the input and make prediction.
used in
image processing, text processing, speech recognition, and prediction tasks.
Learn complex patterns from large datasets.

A neuron is simply a tiny mathematical unit that takes some inputs, gives each input a weight, adds a bias, and produces an output.

. What are inputs?
its the data value fed into neural network

. What are weights?
are the params that determines the influence of the features on output prediction

what is bias
Bias is basically an additional value that lets the neuron shift its output.
"Even if the inputs are small, I want the neuron to have some baseline adjustment."

bias → gives the neuron an additional adjustment

What is z?
total weight calculated

What does sigmoid do?
it takes a value of z and squeez into a strictly number between 0 and 1

Why do we need that?
Because a number between 0 and 1 can be interpreted as a probability-like output in a binary classification setting.

0.90 → strong indication toward class 1
0.20 → strong indication toward class 0
0.50 → uncertain/borderline

What did your neuron output?
0.973

Suppose we change:w1 = 0.5 to w1 = 2.0
What do you expect will happen to the neuron's output?
the value might increase

Give one example where the order of data changes its meaning.
predicting share price based on the previous days prices changes.

#Hidden state
The hidden state is an internal representation that an RNN carries from one step to the next. It can preserve useful information from earlier inputs.

For example, consider this sequence:

10 → 20 → 30

At each step, the RNN receives the current value and the previous hidden state. It uses both to calculate a new hidden state.

Input: 10
RNN step 1 → hidden state h1

Input: 20 + previous state h1

RNN step 2 → hidden state h2

Input: 30 + previous state h2

RNN step 3 → hidden state h3

The state is not a copy of the earlier input. It is a learned numerical representation that can carry information from previous steps.

nn.RNN is a PyTorch layer that processes a sequence one step at a time, updating its hidden state as it goes.

# Day 53 — RNN Fundamentals

## 1. Objective

Understand sequence data, hidden state, and how a basic RNN processes a sequence in PyTorch.

## 2. What is sequence data?

Sequence data consists of ordered observations. Examples include daily temperatures, stock prices and words in a sentence. Order can change the meaning of the data.

## 3. What is an RNN?

A Recurrent Neural Network processes a sequence one element at a time. It carries a hidden state forward so that information from previous steps can influence later steps.

## 4. What is hidden state?

Hidden state is a learned numerical representation that the RNN updates at each time step. It can carry useful information from earlier inputs.

## 5. PyTorch implementation

- `input_size`: number of features at each time step.
- `hidden_size`: number of values in the hidden state.
- `batch_first=True`: input shape is `[batch, sequence length, features]`.
- `outputs`: hidden representations for all time steps.
- `final_hidden`: final hidden state for each RNN layer.

## 6. Example shapes

Input: `[1, 3, 1]`

Output: `[1, 3, 4]`

Final hidden state: `[1, 1, 4]`

These shapes come from one sequence, three time steps, one input feature and four hidden values.

## 7. Important distinction

A randomly initialized RNN can process a sequence, but it has not learned a useful prediction task until it is trained using targets, loss and an optimizer.

## 8. Interview questions

1. What is sequence data?
   a data that follows an ordered observation. for example sales figures, stock price etc

2. Why do we need RNNs?
   rnn is to work on sequence data as it process one feature or ele at a time by carrying some info called hidden state.

3. What is hidden state?
   learned numerical representation that carry some useful info that rnn carry to the next step,

4. What does `input_size` mean?
   number of features at each time step.

5. What does `hidden_size` mean?
   number of val in hidden state
   better way - The number of values maintained in the RNN's hidden representation.

6. What is the difference between `outputs` and `final_hidden`?
   outout- hidden representation of all time layers
   final_hidden - final hidden state of each RNN layer.
   better
   outputs contains the hidden representation at every time step;
   final_hidden contains the last hidden state for each RNN layer.

7. Does creating an RNN mean it has learned to predict?
   noo. training is of learining params against the target, calcualting loss, backward, gradient etc

8. How is an RNN different from a basic feedforward neural network?
   A basic feedforward network processes its input through layers without maintaining a sequence state between time steps. An RNN processes one element at a time and carries a hidden state forward, allowing information from earlier elements to influence later outputs.

Part 1 — Understand the concept (30 minutes)
What is LSTM?

LSTM stands for Long Short-Term Memory. It is a type of recurrent neural network designed to retain useful information over longer sequences.

A basic RNN can struggle to preserve information from much earlier in a sequence because of the vanishing gradient problem.

LSTM uses gates to control what information to remember, update and forget.

Forget gate: Decides what old information to discard.
Input gate: Decides what new information to store.
Cell state: Carries information through the sequence.
Output gate: Decides what information to expose as the output.

Part 2 — Compare RNN and LSTM (15 minutes)
| Basic RNN | LSTM |
|Has hidden state |Has hidden state and cell state|
|Simpler architecture |More complex architecture|
|Can struggle with long-term dependencies |Designed to handle longer-term dependencies better|
|Fewer gates |Uses three gates|

1. Add that LSTM has two states: hidden state (h) and cell state (c).
2. Add the standard hidden-state shape formula:
   [num_layers * num_directions, batch_size, hidden_size]

# BATCH SIZE- REFER MY NOTES

Include:

1. What is LSTM?
   it stands for Long short term memory which helps to retain the information for longer sequences.
2. Why was LSTM introduced?
   because RNN struggles to carry the information in a longer sequences because of the vanishing gradient problem.

3. What is the vanishing gradient problem?
   during backpropagation of the training loop or chain loop the gradient becomes almost zero or shrink results in stoppage of weight updation in the early layers.

4. Explain forget, input and gates.
   forget - tells which information to discard
   input - decides what new information to store
   output - decides what information to show as output

5. What is cell state?
   carries the information through the sequence.

6. Difference between RNN and LSTM.
   RNN- has fewer gates, simple architecture, only hidden state, struggle with long sequence
   LSTM- more gates, complex architeture, hidden and cell state, carries a information for longer sequences

7. Explain the three output shapes from your implementation.
   batchsize, sequence length, Input_size

   batchsize- how many sequences at one
   sequence legth - how many steps per sequence
   input_size - How many features in each array of sequence

# interview questions

Part 5 — Interview questions (15 minutes)

1. What is LSTM and why do we need it?
2. What is the difference between hidden state and cell state?
   Both carry information from previous time steps, but they have different purposes.

Hidden State (h):

- Represents the information the LSTM exposes at the current time step.
- Used to produce the output.
- Passed forward to the next time step.
  Cell State (c):
- Acts as the LSTM's long-term memory.
- Carries important information across multiple time steps.
- Updated using forget and input gates.
  Think of it this way:
- Cell state = What the LSTM remembers.
- Hidden state = What the LSTM currently shares or exposes.

3. What are the three gates in LSTM?
4. How does LSTM help with vanishing gradients?
   First, what is the vanishing gradient problem?

During training, a neural network uses backpropagation to learn from its mistakes. In a basic RNN, gradients can become extremely small as they travel backwards through many time steps.

As a result, the network struggles to learn from older information.

How LSTM solves this:

LSTM uses a separate cell state and three gates to control information flow.
Gate Purpose
Forget gate Decides what old information to discard
Input gate Decides what new information to remember
Output gate Decides what information to expose as output

The cell state provides a more direct path for information and gradients to flow across time steps, helping reduce the vanishing gradient problem.

Interview ans
How does LSTM overcome vanishing gradients?

LSTM uses a cell state and gating mechanisms to regulate information flow. The cell state provides a relatively direct path for gradients to propagate across time steps, helping preserve long-term dependencies and reducing the vanishing gradient problem.

Remember: LSTM reduces the vanishing gradient problem; it does not completely eliminate it.

5. What is the difference between nn.RNN and nn.LSTM in PyTorch?

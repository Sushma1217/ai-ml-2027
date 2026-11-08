sequence_length = 20
Each prediction uses the previous 20 values.

For example:

- Sequence length 5: use 5 previous values to predict the next.
- Sequence length 20: use 20 previous values.
- Sequence length 50: use 50 previous values.
  More historical information is not automatically better. It can make learning more difficult and increase computation.

Your output should look like this:
Sequence length || RNN test MSE || LSTM test MSE
5 ||0.02722|| 0.0550
20 || 0.0241 ||0.1060
50 ||0.0054||0.0663

1. Which sequence length gave the lowest RNN test loss?
   50

2. Which sequence length gave the lowest LSTM test loss?
   5

3. Did increasing sequence length always improve performance?
   Increasing sequence length did not consistently improve both models: LSTM's loss increased from length 5 to 20.

4. Which model performed better in your experiment?
   RNN performed better at lengths 20 and 50.

5. Why might LSTM be more useful when longer-term dependencies matter?
   because of its cell state and gating mechanism which helps to propogate the information directly using cell state for longer term dependencies and its gating mechanishm tries to reduce the vanishing graident problem.

# Interview questions

1. What is sequence length in RNN?
   the lenght or number of values carried forwarded to predict the next values. for ex:sequence_length is 20 then 20 values are carry forwarded.

2. What happens when sequence length increases?
   the loss decresed
3. Does a longer sequence always improve prediction?
   no always as longer sequence leads to more historical data rememberance or carrying which can affect the performance overfitting, gradients flow etc

4. Why are LSTMs useful for long-term dependencies?
   because of its cell state and gating mechanism which helps to propogate the information directly using cell state for longer term dependencies and its gating mechanishm tries to reduce the vanishing graident problem.

5. What is the difference between training loss and test loss?
   training loss- calcualed on training data, helps to min the test or actual loss by uppdating the weights, calculating the gradients during backpropogation.
   test loss- actuals loss on unseen data, indicates the model ability to perform on the real data

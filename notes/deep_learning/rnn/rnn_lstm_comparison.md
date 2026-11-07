RNN LSTM
Simpler architecture | More complex architecture
Uses hidden state Uses |hidden state and cell state
Has no explicit gating mechanism |Uses three gates
Can struggle with long-term dependencies |Designed to handle long-term dependencies better

1. Which model achieved lower test loss?
   Rnn achieved a less test loss with 0.0227 where as LSTM loss is 0.074.

2. Why might LSTM perform better than RNN?
   LSTM might perform well because of its gating mechanism, cell state along with hidden state. it carries the information over long sequence and it helps reduce the vanishing-gradient problem.

Does a more complex model always perform better?
no. complex model tries to learns everything instead of understading the actual concept. so it might perform well in training and might not in the actual prediction which can lead to overfitting issue.

Why did we use the same dataset for both models?
to compare the performance or loss by both the models agains the same dataset.

What happens if we increase the hidden size from 16 to 32?
A larger hidden size gives the model more capacity to learn patterns, but it also increases the number of parameters. The loss may decrease, stay similar, or even increase on test data.
better answer:
Increasing hidden size increases the number of hidden units and the model's learning capacity. It may help capture more complex patterns, but it also increases computation and the risk of overfitting. It does not guarantee lower test loss.

# interview questions

1. What is the main difference between RNN and LSTM?
2. Why does LSTM use a cell state?
3. What is vanishing gradient?
4. What is the purpose of a Linear layer after RNN/LSTM?
5. How do you evaluate a regression model?
   MAE, MSE, R2
6. Does LSTM always outperform RNN?

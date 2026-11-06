Part A — Understand the problem (20 minutes)
What is sequence prediction?

Sequence prediction means using previous values to predict the next value.

Example:
Previous values Expected prediction
10, 20, 30 40
20, 30, 40 50
30, 40, 50 60

This is a simple example of time-series forecasting.

We'll use a sine wave instead of manually creating these numbers so the model can learn a continuous pattern.

Why are we doing this?

- To understand how LSTM learns from sequential data.
- To understand how training works with LSTM.
- To understand how to use LSTM for actual predictions.

Save these concepts:

1. Sequence prediction: Predicting future values using previous observations.
2. Sequence length: Number of previous time steps given to the model.
3. Sliding window: Creating multiple training samples by moving through sequential data.
4. LSTM output: Contains learned representations at every time step.
5. Linear layer: Converts LSTM features into the final prediction.
6. MSE Loss: Measures the difference between actual and predicted numerical values.

# Interview questions

8. What is sequence prediction?
   predicting the next values using the previous information or values or observation.

9. What is a sliding window?
   training with multiple samples by moving through sequenctial data.

10. Why do we use batch_first=True?
    Consider your dataset:
    X.shape = [980, 20, 1]

This means:

- 980 = Number of sequences (batch size).
- 20 = Number of time steps in each sequence.
- 1 = Number of features at each time step.
  Now, PyTorch supports two input arrangements.
  Without batch_first=True
  [sequence_length, batch_size, input_size]

Example:
[20, 980, 1]

With batch_first=True
[batch_size, sequence_length, input_size]

Example:
[980, 20, 1]

Why do we prefer batch_first=True?

Because it allows us to organize input data with batch size as the first dimension, which is often easier to understand and work with.

It does not change how LSTM learns. It only changes the expected layout of the input and output tensors.

Also remember: hidden state and cell state dimensions are not rearranged by batch_first.

Interview-ready answer:

"We use batch_first=True to make the input tensor follow the format [batch_size, sequence_length, input_size] instead of [sequence_length, batch_size, input_size]. It makes data organization easier, especially when working with batches of sequential data."

11. Why do we select outputs[:, -1, :]?
    because the last value contains the accumulated or summarized context of the entire sequence.
    better ans
    We select the output at the last time step because it contains the final hidden representation after processing the sequence. We use this representation to predict the next value.

12. Why do we use a Linear layer after LSTM?
    because linear layers converts the LSTM features into final prediction.

13. Why do we use MSE loss for numerical prediction?
    it measures the avg sequared difference between the predicted and actual values of numerical values.

14. Why should we avoid randomly shuffling time-series data before splitting?
    because the its a sequence prediction mechannism where the future values arre predicted based on the previous observation so shuffling will lead to no proper ordering and prediction may be incorrect.

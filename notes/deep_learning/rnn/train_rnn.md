Today's workflow:
Input sequence

Three observed values

RNN

Processes values and carries hidden state

Linear output layer

Produces one predicted number

Calculate loss and update weights

Learn from the prediction error

concept
The RNN processes the three values and produces a hidden representation at each step. We'll take the final hidden representation and pass it through a linear layer to predict one number.

Mean Squared Error (MSE) loss
it measures the avg squared differece between predicted and correct numeric values.
For a single example:
[\text{Loss}=(\text{prediction}-\text{target})^2\]

If the correct answer is 0.006 and the prediction is 0.010, the squared error is:
[(0.010-0.006)^2=0.000016]

The loss is smaller when predictions are closer to the target.

# Day 54 — Training an RNN for Next-Value Prediction

## 1. Objective

Train a basic RNN to predict the next number in a sequence.

## 2. Dataset

Each input contains three consecutive values. The target is the next value. Values are divided by 500 to keep them in a smaller numerical range.

## 3. Model architecture

- `nn.RNN`: processes the input sequence and maintains a hidden state.
- `hidden_size=8`: maintains eight hidden values.
- `outputs[:, -1, :]`: selects the output at the final time step.
- `nn.Linear(8, 1)`: converts the final representation into one prediction.

## 4. Loss and optimization

- `MSELoss` measures squared numerical prediction error.
- `loss.backward()` calculates gradients.
- `optimizer.step()` updates the model parameters.
- Training repeats across epochs to reduce prediction error.

## 5. Results

- Initial loss: 0.160
- Loss after epoch 100: 0.000079
- Predicted original-scale value: 100.85
- Expected value:0.206

## 6. What I learned

Explain how the RNN uses the sequence and how the loss helps it learn.

## 7. Interview questions

1. Why is this a regression problem?
   because we are predicting continuous numerical value based on one or more independent input feature.

2. Why use MSE loss?
   because it measures the numerical prediction error.

3. What does the RNN hidden state do?
   it carries a useful information to the next layer, usually of numerical representation.

4. Why do we select the final output?
   because it contains the final summary value of entire input sequence.

5. What does `optimizer.step()` do?
   it updates the weights based on the gradients calcualted to minimise the loss.

6. Why do we normalize the values?
   i failed to answer

7. Does a decreasing training loss guarantee good predictions on unseen data?
   No because loss is about how far the model is from the actual prediction. a good prediction depends on model learning the pattern, data imbalance etc

Interview answers to check

1. Why regression? Because the output is a numerical value, not a category.

2. Why MSE? It measures squared differences between predicted and actual numerical values.

3. What does hidden state do? It carries a learned representation of information from previous sequence steps.

4. Why the final output? It represents the sequence after the RNN has processed all three input values.

5. What does optimizer.step() do? It updates trainable parameters using the gradients calculated during backpropagation.

6. Why normalize? Smaller input values can make numerical optimization easier.

7. Does lower training loss guarantee good unseen predictions? No. We need evaluation on data that wasn't used for training.

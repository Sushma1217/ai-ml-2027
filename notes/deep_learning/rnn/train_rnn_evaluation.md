Objective of the exercise.
Learn how to check whether an RNN can predict values it has never seen during training.

Difference between training and testing data.
training data- the data used to train the model, where the model learns the pattern, params
testing data- unseen data, where model uses the learnt params to make the prediction on testing data

Why we used a time-ordered split.

What MAE means, with a simple example.
Mean absolute error, it measures the avg absolute difference between the prediction and actual values.

Training loss and test loss from your run.
Test loss = 1.999
Training loss
Epoch 20,loss 0.003100
Epoch 40,loss 0.000408
Epoch 60,loss 0.000150
Epoch 80,loss 0.000024
Epoch 100,loss 0.000020

Test MAE in original units- 1.7018

Five actual-versus-predicted examples.
Actual: 3.00, Predicted: 7.78
Actual: 4.00, Predicted: 8.65
Actual: 5.00, Predicted: 9.52
Actual: 6.00, Predicted: 10.40
Actual: 7.00, Predicted: 11.27

What you observed about the model's predictions.
not predicted correctly. the loss is too high

# Interview questions

Q1. Why do we split data into training and testing sets?

To check whether the model can make predictions on data it hasn't seen during training.

Q2. What is generalization?

The ability of a model to learn patterns from training data and apply them to unseen data.

Q3. What is MAE?

Mean Absolute Error measures the average absolute difference between actual and predicted values.

Q4. Can training loss be low while test loss is high?

Yes. The model might have learned the training examples well but may not perform well on unseen data. This can indicate overfitting or poor generalization.

Q5. Why use a time-ordered split for time-series data?

Because future observations should not be used to train a model that is being evaluated on earlier or future predictions. A chronological split better represents predicting future values.

stratify=y ensures that your train and test sets have the exact same percentage of 1s and 0s as your original dataset.
Why use it:
If your churn data has 15% "Yes" and 85% "No", stratification prevents a random split from accidentally putting all the "Yes" rows into training and missing them in testing. It keeps your data balanced and your evaluation reliable.

input size: unlike the AND example, the number of input features is not two. One-hot encoding creates additional columns, so the network must use the actual number of processed features.

Concept — Adam: an optimizer that adapts parameter updates during training. For today, you only need to know that it updates weights using the gradients calculated by backpropagation.

<!-- Questions -->

Why do we preprocess before training?
so the raw data contains missing values, skewed, different range and categorical value contains non numerica values which machine cannot understand thats why preprocessing is most crucial step before training, it helps to transform the data by handling the missing, removing irrelevant columns etc which can we used for model training and chances of data misrepresentation will be almost minimal.

Why must the input layer size match the processed feature count?
because of how matrix multiplication works.
during fwd pass, the model multiplies input feature with weights so it should match else pytorch will throw shape mismatch error.

Why are we using BCEWithLogitsLoss instead of BCELoss?
BCEWithLogitsLoss combines both BCELoss and sigmoid into a single formula

What is an epoch?
a single pass through of every values in training dataset is an epoch.

What happened to the training loss?
training loss decreases slowly

What were churn recall and F1?
recall is about out of all positive prediction how many does the model was able to identify, represents True negative. its value is 0.13 for class 1

Precision: Of the customers predicted to churn, how many actually churned?
Recall: Of all customers who actually churned, how many did the model identify?

f1 represent the combined value of precision and recall- 0.22 for class 1

How does the neural network compare with your earlier Logistic Regression model?
logistic - single layer maps input directly to the output.
nn- has hidder layer which makes more powerful for complex data

Why do we save both the preprocessing pipeline and the model?
the model expect the feature in the same encoded or scaling format it was trained on so saving model only is not enough to reproduce the predictions from raw data

# COMPARISON

| Metric    | Logistic Regression | PyTorch Neural Network |
| --------- | ------------------: | ---------------------: |
| Accuracy  |                  78 |                     74 |
| Precision |                0.62 |                    .81 |
| Recall    |                 .51 |                  .0.06 |
| F1        |                0.50 |                   .041 |

Which model has higher churn recall?
logistic regression

Which model has higher F1?
logistic regression

What kinds of mistakes does each model make?
predictiing true negative values

Why might Logistic Regression perform as well as or better than a neural network on tabular data?
because it is best suited to predict when the output is of binary classification as it direct maps the input layer with output where as neural network is considerably good for complex data prediction like image processing as it has hidden layers.

Which model would you choose if identifying as many likely churners as possible were the priority, and what trade-off would that create?
i would choose logistic by considering metrics like recall, precision along with accuracy is more compared to nueral network.

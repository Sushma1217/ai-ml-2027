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
recall is about out of all positive prediction how many does the model was able to identify. its value is 0.02 for class 1

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
| Precision |                0.62 |                    .47 |
| Recall    |                 .51 |                    .81 |
| F1        |                0.50 |                    .60 |

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

## PyTorch Churn Model — Final Experiment Notes

### 1. Objective

Built a neural network using PyTorch to predict customer churn from the Telco Customer Churn dataset. The objective was to apply neural-network concepts to a real dataset and compare the results with Logistic Regression.

### 2. Model Architecture

- Input layer: number of features after preprocessing
- Hidden layer 1: 32 neurons with ReLU
- Hidden layer 2: 16 neurons with ReLU
- Output layer: 1 neuron producing a raw score (logit)
- Loss function: `BCEWithLogitsLoss`
- Optimizer: Adam
- Training epochs: 50

### 3. Data Preprocessing

- Removed `customerID`, as it is an identifier.
- Converted `TotalCharges` to numeric and handled missing values.
- Encoded categorical features using `OneHotEncoder`.
- Scaled numerical features using `StandardScaler`.
- Used a stratified 80/20 train-test split.
- Fitted preprocessing on training data only to avoid data leakage.
- Converted processed features and target labels into PyTorch tensors.

### 4. Class Imbalance

The dataset contains more non-churners than churners. Initially, the model predicted almost every customer as a non-churner, resulting in very low churn recall.

To address this, I used a positive-class weight:

`pos_weight = negative_count / positive_count`

This makes mistakes on the minority churn class more costly during training.

### 5. Final Class-Weighted Model Results

Confusion matrix:

|                 | Predicted No Churn | Predicted Churn |
| --------------- | -----------------: | --------------: |
| Actual No Churn |                696 |             337 |
| Actual Churn    |                 71 |             303 |

| Metric    | Non-churn (0) | Churn (1) |
| --------- | ------------: | --------: |
| Precision |          0.91 |      0.47 |
| Recall    |          0.67 |      0.81 |
| F1-score  |          0.77 |      0.60 |

Overall accuracy: **71%**

### 6. Interpretation

- Churn recall of 0.81 means the model identified approximately 81% of actual churners.
- Churn precision of 0.47 means approximately 47% of customers predicted to churn actually churned.
- The model identified 303 of 374 actual churners and missed 71.
- It incorrectly flagged 337 non-churners as potential churners.
- Class weighting improved churn detection but increased false positives and slightly reduced overall accuracy.

### 7. Learning: Why Accuracy Is Not Enough

Accuracy can be misleading when classes are imbalanced. A model can achieve apparently reasonable accuracy by mostly predicting the majority class while failing to identify churners.

For this problem, churn recall and F1-score provide additional information about the model's ability to identify customers at risk of leaving.

### 8. Logistic Regression vs. Neural Network

Logistic Regression is a useful baseline for this dataset. The neural network's performance must be compared against Logistic Regression using the same test split and corresponding metrics.

A more complex model is not automatically better. Model selection should depend on the business objective and the trade-off between missed churners and false alarms.

### 9. Model Saving and Reproducibility

- Saved the trained model parameters using `torch.save(model.state_dict(), ...)`.
- Saved the fitted preprocessing pipeline using `joblib`.
- Used random seeds to make experiments more reproducible.
- Verified that a freshly loaded model produces matching predictions on the same test inputs.

### 10. Conclusion

This project applied PyTorch to a real classification problem and covered preprocessing, tensor conversion, neural-network training, binary cross-entropy, class weighting, evaluation metrics, and model persistence.

The class-weighted model achieved 81% churn recall and 0.60 churn F1-score in the recorded experiment. These results are specific to the current test split and training setup; they do not establish that the neural network is better than Logistic Regression without a fair comparison.

**Status: Core PyTorch churn experiment completed. Further tuning is deferred.**

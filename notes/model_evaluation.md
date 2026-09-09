# Day 26 — Model Evaluation & Improvement

## Why are we learning this?

An ML engineer doesn't stop when a model produces 78% accuracy. We need to diagnose its weaknesses, compare models, tune them, and choose the right evaluation criteria for the business problem.

## Baseline Model

<!-- # Train accuracy:80.91
# Test accuracy: 78.68
# Precision — Yes:  0.62
# Recall — Yes:   0.51
# F1 — Yes:   0.56
# Confusion Matrix:
# [[915 118]
#  [182 192]] -->

## Confusion Matrix

TN = 915
FP = 118
FN = 182
TP = 192

## Manual Metric Calculation

Accuracy- (TP+TN)/(TP+TN+FP+FN)

# (192+915)/ (915+118+182+192) = .78

# Precision

# TP / (TP + FP)

# 192/(192+118) = .61

# Recall

# TP/(TP+FN)

# 192 /(192+182) = .51

# F1 For now, use:

# 2 × (Precision × Recall)

# ------------------------

# Precision + Recall

# 2*(.61 *.51)/.61+.51 = 0.5098

## Target Distribution

Yes:1869
No: 5163

Percentage:
no- 0.73
Yes - 0.26

Is it balanced?
No

## Majority Baseline

My prediction:

Actual result:

## Class Weight

What does class_weight="balanced" do?
gives more importance to under represented class in training to fix the data imbalance.

## Model Comparison

| Metric    | Original | Balanced |
| --------- | -------: | -------: |
| Accuracy  |       78 |    73.13 |
| Precision |     0.62 |       .5 |
| Recall    |      .51 |      .79 |
| F1        |     0.50 |      .70 |

## Which model would I choose?

the balanced one
Why?
when we look that metrics, the recall is high which means the balanced model was able to predict more customers who churn out of all churn customers which helps company to take some action to retain them.
the precision is low which means the false positive that is the model was able to predict correctly nearly 50% with little more false alarms compared to the original
the metric F1 the combination of recall and precision shows high in balanced model which shows model efficiency

## Parameters vs Hyperparameters

Parameter:
something model learn from the training data
Hyperparameter: something we choose before or during training.

Examples:
params: max, min, avg
Hyperparameter = max_iter, class_weight

## Interview Questions

Why do we need a baseline model?
a simple reference point used to compare and evaluate the performance of the complex model.

# What is class imbalance?

occurs when dataset is not represnted equally

# Why can accuracy be misleading with imbalanced data?

because majority class will have larger impact and can dominate the minor class.

# What does class_weight="balanced" do?

gives more importance to under represented class in training to fix the data imbalance.

# What is a false positive in our churn problem?

it means the customer who did not churn but incorrectly identfied by the model as churn customers, precison is the indicatos.

# What is a false negative?

the model identified as negative but it actually positive, recall is the indicator.
it has major impact on the business as business will not consider to make any measure cause of the incorrect lable classification

# if recall increases but precision decreases, what might have happened?

recall increases means model was able to predict most of the positive cases from all the positive cases of the data point which is a good indicator for model performance.
precision decreases means the model is making false alarms, larger share of its yes predicitons are wrong which is fine because even if take the measure of existing customers there wont be a space for revernue loss.

# What is a model parameter?

the values which model learns during training or fitting for examples weights / coefficients
intercept

# What is a hyperparameter?

something we choose before or during training. for example C max_iter class_weight

# Give an example of each for Logistic Regression.

classifying between whether cusomter will watch movie or not, segregation of mail.

How would you decide which model is better?
we need to look for other indicators like recall, precision, f1 etc along with accuaracy.

Why isn't the model with the highest accuracy automatically the best model?
it just the indication of positive prediction made by model out of the total prediction without evaluation
means we need to check prediction against actual results.

## What confused me

how to compare and combine the business logic with FP, FN etc and interpret

## What became clearer

## AI/ML connection

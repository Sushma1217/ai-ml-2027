# Day 25 — F1 Score & Classification Threshold

## Why are we learning this?

A real ML model isn't judged by one number. We need to understand different types of mistakes and choose metrics based on the business problem.

## F1 Score

My understanding:
F1 score combines precision and recall into a single metric.

F1 is the harmonic mean of precision and recall.

## Precision vs Recall

Model A:
Precision = 90%
Recall = 40%
Model B:
Precision = 70%
Recall = 75%

My choice:
Model B. because it balance well the true positive portion. Recall is very less in model A it means model was able to make only 40% postive prediction correctly out of the all postive values.

## Classification Report

### Yes

Precision = .62
Recall =.51
F1 =.56

### No

Precision = .83
Recall =.89
F1 =.86

## Business Scenario

My choice:
No.

Why?
Model was able to predict No classification accurately than Yes. It was able to predict how many customers did not churn as comapred to churn.

## predict_proba()

My understanding:
a tool that allows to obtain probability estimates of class prediction
returns 2d array
column ordering always
Column 0 - no/false
Column 1- Yes/true

## Classification Threshold

My understanding:
a cutoff probability value that determines which class a model assigns to a data point.

## Manual Challenge

Customer A → churn probability = 0.51
Customer B → churn probability = 0.49

threhold: .5
customer A is 0.51 - Yes
Customer B → No

What do you think would happen if we lowered the threshold to 0.30?
both customer belongs to Yes class

## Interview Questions

What is F1 score?
it is the a single matrix that combines both precision and recall.

Why do we need F1 if we already have precision and recall?
may be easy to read, compare the values

Which metric would you prioritize if missing a positive case is very costly?
recall-as it measures the out of all positive cases how many model was able to predict correctly.

What does predict_proba() give us?
it gives us the prediction with a proabiliy value of the class belongs to.
default is .5

What is a classification threshold?
a cut off line which tells to which class the data point belongs to

What happens if we lower the classification threshold?
model will predict most of the positive cases only.

Why might changing the threshold affect precision and recall?
because it has direct relationship with the determination of positive class the data belongs as lowering threshold results into more positive cases and higher the threhold the model predicts more negative class

## What confused me

business class questions, when to choose recall or precision

## What became clearer

threshold, f1, how to read confustion matrics, probability

## AI/ML connection

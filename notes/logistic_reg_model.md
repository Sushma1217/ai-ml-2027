# Day 23 — First ML Model: Logistic Regression

## 🎯 Why are we learning this?

This is where preprocessing turns into actual machine learning: we give the algorithm training data, let it learn patterns, and use it to predict churn for unseen customers.

## What is Logistic Regression?

My understanding:
a supervised learning alogorithm(which has label) learn to predict the probability of categorical outcome which usually have two choice like yes/no, 0/1 or true or false

## Model Pipeline

My understanding:
a sklearn Pipeline chains the preprocessing steps and model into a single reproducbile workflow.

it combines all the stages like data collection, preprocessing, model deployment and monitoring elemintates manual tasks
stages

1. data preperation -
   1.auto fetching data from db, api or cloud
   2.data cleaning- missing number, duplicates
   3.feature enginerring
2. model enginerring - model training, evaluation, hyper tuning
   3.ops and deployment

## What does fit() do?

fit is learning the parameters or values for example min, max or avergare from feature tain data(X_train).
may be applies the learnt params in Y train and analyse

## What does predict() do?

it is a method used to run the trained model in inference mode which means using a trained machine learning model to make a prediction on new, unseen data.

## Predictions

What did I observe?

## Accuracy

My understanding:
tells us how accurate the prediction is
78% is the accurance of test data
around 4 values got mismatched

## Train vs Test Accuracy

Train: 80.91
Test: 78.68

My observation:
training accuracy is higher

## Overfitting

My understanding:
ML model works perfectly on the train data and fails to make accurate prediction on new unseen data.

## max_iter

My understanding:
allows how many times model can look at the data and process it.

## Interview Questions

Q1

What is Logistic Regression?
algortim used in ml model to predict the results in which a categorical target is associated with two choices such as true/false, 0/1 or yes/no.

Q2

Why can Logistic Regression be used for a Yes/No classification problem?
because this is the best choice as it will classify among two choices

Q3

What does .fit() do?
analyses and learns the parameters in train data like min, max

Q4

What does .predict() do?
it is a method used to run the trained model in inference mode which means using a trained machine learning model to make a prediction on new, unseen data.

Q5

Why do we predict on X_test?
because if we do it on train or whole data we encounter with data leakage issue where the model will learn the parameters with train data and use that to predict the new or unseen data in this way it works by analysing and not memorizing.

Q6

What is accuracy?
how well the model can perform, predict and give the accurate results

Q7

Why can accuracy be misleading for an imbalanced dataset?
accuracy might be dominated by the few categories or numbers values, not a normal range scale.

Q8
What is overfitting?
a condition where the accuracy of the model is more in traing as compared to the test data

## What confused me

pipeline, the steps like im file till transformers but why are we putting preprocessing + model together?
then using fit on pipeline values

## What became clearer

the steps like loading till transformers

## AI/ML connection

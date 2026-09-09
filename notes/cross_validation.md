# Day 27 — Cross Validation

## Why are we learning this?

A single train/test split can give us one estimate of model performance. Cross-validation lets us evaluate the model across multiple training/validation splits, giving us a more reliable view of its performance.

## Why isn't one train/test split enough?

yes because data is imbalanced so sometimes only one class can be divided in the split

## What is Cross Validation?

My understanding:
a resampling technique used to evaluate the performance of model on unseen data by testing over randomly partitions data. it shiffels and divides the data so each data point will go through training and validation

## cv=5

My understanding:
divide the data into 4 random partition so in each state validation will be performed like
Iteration 1: [ Test ] [Train] [Train] [Train] [Train] --> Score 1
Iteration 2: [Train] [ Test ] [Train] [Train] [Train] --> Score 2
Iteration 3: [Train] [Train] [ Test ] [Train] [Train] --> Score 3
Iteration 4: [Train] [Train] [Train] [ Test ] [Train] --> Score 4
Iteration 5: [Train] [Train] [Train] [Train] [ Test ] --> Score 5

## Results

| Metric    |   Mean |   Std |
| --------- | -----: | ----: |
| Accuracy  |   0.75 | 0.013 |
| Precision |  0.522 | 0.016 |
| Recall    | 0.7979 | 0.033 |
| F1        |  0.631 | 0.022 |

## Which metric would I prioritize?

Why?
recall as it tells how many churn customers the model was able to find our of all the churn customers

## Why X_train and not X_test?

we must always use train data during the fit and validation as using test data can make model lazy, it might memorize the params which leads to data leakage.

## Model Stability

My understanding:
Model stability in machine learning means an algorithm produces consistent results when small changes happen to its training data, environment, or parameters

## Interview Questions

"Your model gets 80% accuracy. How do you know it's not just because of a lucky train-test split?"
ans: we can verify using a cross validation which tells us that each data point is considered for training by randomly partitioning the data. when we give CV values it makes sure that in each iteration validation is performed along with training.

# What is cross-validation?

it is resampling techninue used to evaluate the model performace on unseen data by data partition. data is randomly paritioned so that each data point is considred and validation is performed in each iteration.

# why do we use cross-validation?

to evaluate the model performance on future data

# What does cv=5 mean?

means the partition is 5 times and in each iteration validation is performed for example in 1st, the test/ validation in first plance and 2nd iteration its in 2nd place.

# Why do we perform cross-validation on training data?

we must always use train data during the fit and validation as using test data can make model lazy, it might memorize the params which leads to data leakage.

# Why should the test set remain untouched until final evaluation?

because model can memorzise the params and wont learn so when we introduce at the end it can use a fit to learn and perform well in this case can avoid the data leakage.

What does the mean CV score tell us?
the average expected performance of a machine learning model across multiple data splits

What does the standard deviation of CV scores tell us?
how stable and consistent your machine learning model is across different data splits.

#Why might F1 be more useful than accuracy for our churn problem?
because its a metric that combines precision and recall which helps interpret the false negative ans positive values of data prediction by model

What is the difference between a validation set and a test set?
validation set- used for fine tune during the development or processing.
test set- used for final evaluation

How would you explain cross-validation to a non-technical manager?
i can say its a way of cross checking how model performs on different parition like 50:50, 90:10 etc so it can verify all the aspect and give the better results
